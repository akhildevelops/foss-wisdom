from ultralytics import YOLO
from typing import Self,Tuple
from  ultralytics.engine.results import Results
import numpy
from typing import Dict,List,Tuple,Optional
from ..video_loader import VideoLoader
from dataclasses import dataclass


@dataclass
class BBBox:
    box:numpy.ndarray
    location:str
    def __hash__(self) -> int:
        return hash(self.location)



def common_area(bb1:numpy.ndarray,bb2:numpy.ndarray)->Optional[Tuple[float,numpy.ndarray]]:
    nc = numpy.concatenate([bb1,bb2],axis=0)
    max =numpy.max(nc,axis=0)[:2]
    min = numpy.min(nc,axis=0)[2:]
    if max[0]>min[0] or max[1]>min[1]:
        return None
    nc = numpy.concatenate([nc,numpy.concatenate([max,min]).reshape(1,-1)],axis=0)
    areas = (nc[:,2]-nc[:,0])*(nc[:,3]-nc[:,1])
    proprtion = areas[2]/(areas[0]+areas[1]-areas[2])
    return (proprtion,areas) 

class TimeSpent:
    def __init__(self,model:YOLO,treshold=0.2 ) -> None:
        self.model=model
        self.treshold=treshold
        
    
    @classmethod
    def from_yolo(cls,version:str)->Self:
        yolo = YOLO(version)
        return cls(yolo)
    
    def time_spent(self,video:VideoLoader,bounding_box:List[BBBox]):
        track_ids:Dict[BBBox,Dict[int,List[int]]]={}
        iterator = video.frame_iterator()
        for index,frame in enumerate(iterator):
            analyzed_frame:Results = self.model.track(frame,persist=True)[0]
            for ref_box in bounding_box:
                humans = track_ids.setdefault(ref_box,dict())
                for box in analyzed_frame.boxes:
                    if not (box.cls==0).item():
                        continue
                    if not box.id:
                        continue
                    human_id=box.id.int().item()
                    frames = humans.setdefault(human_id,list())
                    areas = common_area(ref_box.box,box.xyxy)
                    if areas is not None:
                        if areas[1][2]/areas[1][0]>self.treshold:
                            frames.append(index)
        return track_ids
        

        
