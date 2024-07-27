from dataclasses import dataclass
from typing import Any
from ultralytics import YOLO
@dataclass
class Model:
    model:YOLO
    @classmethod
    def default(cls):
        return cls(YOLO("yolov8l.pt"))
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.model(*args,**kwds)