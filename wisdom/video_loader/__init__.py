import cv2
from typing import Iterator,Optional
from dataclasses import dataclass
from datetime import timedelta
import numpy
import requests
from pathlib import Path
@dataclass
class VideoMetadata:
    n_frames:int
    fps:float
    width:int
    height:int

    @property
    def frame_time(self)->float:
        return 1/self.fps
    
    @property
    def video_length(self)->timedelta:
        return timedelta(seconds=self.n_frames*self.fps)


class VideoLoader:
    def __init__(self,path:str,restrict_frames:Optional[int]) -> None:
        self.path = path
        self._video = cv2.VideoCapture(path)
        self.restrict_frames= restrict_frames if restrict_frames else float('inf')
  
    def metadata(self):
        return VideoMetadata(int(self._video.get(cv2.CAP_PROP_FRAME_COUNT)),int(self._video.get(cv2.CAP_PROP_FPS)),int(self._video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(self._video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    def frame_iterator(self)->Iterator[numpy.ndarray]:
        counter=0
        while counter<self.restrict_frames:
            success, frame = self._video.read()
            if not success:
                return
            yield cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            counter+=1
    @classmethod
    def from_url(cls,url:str,path:Optional[str]=None,restrict_frames:Optional[int]=None):
        if not path:
            path="./retail_store.mp4"
        print("Downloading video from %s to %s "%(url,path))
        if Path(path).exists():
            print("Skipping download as %s is already present"%path)
        loader = requests.get(url)
        with open(path, 'wb') as f:
                for chunk in loader.iter_content(chunk_size=1024 * 4): 
                    f.write(chunk)
        print("Finished Downloading")
        return cls(path,restrict_frames)



