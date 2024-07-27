import cv2
from typing import Iterator
from dataclasses import dataclass
from datetime import timedelta
import numpy

@dataclass
class VideoMetadata:
    n_frames:int
    fps:float
    width:int
    height:int

    @property
    def frame_time(self)->float:
        return timedelta(seconds=1/self.fps)
    
    @property
    def video_length(self)->timedelta:
        return timedelta(seconds=self.n_frames*self.fps)


class VideoLoader:
    def __init__(self,path:str) -> None:
        self.path = path
        self._video = cv2.VideoCapture(path)
  
    def metadata(self):
        return VideoMetadata(int(self._video.get(cv2.CAP_PROP_FRAME_COUNT)),int(self._video.get(cv2.CAP_PROP_FPS)),int(self._video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(self._video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
    def frame_iterator(self)->Iterator[numpy.ndarray]:
        while True:
            success, frame = self._video.read()
            if not success:
                return
            yield cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


