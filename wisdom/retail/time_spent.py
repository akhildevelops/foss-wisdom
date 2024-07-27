from ultralytics import YOLO
from typing import Self
from  ultralytics.engine.results import Results
import numpy
from typing import Dict,List
from ..video_loader import VideoLoader
from dataclasses import dataclass

@dataclass
class Human:
    id:int
    frame_ids:List[int]

def common_area(bb1:numpy.ndarray,bb2:numpy.ndarray)->float:
    nc = numpy.concatenate([bb1,bb2],axis=0)
    max =numpy.max(nc,axis=0)[:2]
    min = numpy.min(nc,axis=0)[2:]
    if max[0]>min[0] or max[1]>min[1]:
        return 0
    nc = numpy.concatenate([nc,numpy.concatenate([max,min]).reshape(1,-1)],axis=0)
    areas = (nc[:,2]-nc[:,0])*(nc[:,3]-nc[:,1])
    proprtion = areas[2]/(areas[0]+areas[1]-areas[2])
    return proprtion 

class TimeSpent:
    def __init__(self,model:YOLO ) -> None:
        self.model=model
        self.track_ids:Dict[int,Human]={}
    
    @classmethod
    def from_yolo(cls,version:str)->Self:
        yolo = YOLO(version)
        return cls(yolo)
    
    def time_spent(self,video:VideoLoader,bounding_box:List[numpy.ndarray],treshold:float=0.5):
        iterator = video.frame_iterator()
        metadata=video.metadata()
        for index,frame in enumerate(iterator):
            analyzed_frame:Results = self.model.track(frame,persist=True)
            for box in analyzed_frame.boxes:
                human = self.track_ids.setdefault(box.id.int().item(), Human(index,list()) if (box.cls==0).item() else None)
                if human:
                    # check_iou(box.)
                    human.frame_ids.append(index)
            

        
