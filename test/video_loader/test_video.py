from wisdom.video_loader import VideoLoader
from ..conftest import video_path
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


