from wisdom.video_loader import VideoLoader
from ..conftest import video_path
from wisdom.retail.time_spent import TimeSpent,BBBox
from ultralytics import YOLO
import numpy as np
def test_video_metadata():
    v = VideoLoader(video_path)
    metadata = v.metadata()
    assert metadata.fps==13
    assert metadata.n_frames==1283
    assert metadata.width==634
    assert metadata.height==360

def test_video_iterator():
    v = VideoLoader(video_path)
    frames = v.frame_iterator()
    assert sum(1 for _ in frames)==1283

def test_video_timespent():
    v=VideoLoader(video_path)
    model = YOLO("yolov8n.pt")
    ts = TimeSpent(model)
    bbox1 = BBBox(np.array([[27,51,141,113]]),"billing_counter")
    track_ids = ts.time_spent(v,[bbox1])
    assert track_ids
    
