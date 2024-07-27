from pathlib import Path
import pytest
import requests

test_dir = Path("test")
video_path = test_dir/"video.mp4"
video_path.parent.mkdir(parents=True,exist_ok=True)

def youtube_video_download(url:str,local_path:Path):
    print("Downloading video from %s to %s ",url,local_path)
    loader = requests.get(url)
    with open(local_path, 'wb') as f:
            for chunk in loader.iter_content(chunk_size=1024 * 4): 
                f.write(chunk)
    print("Finished Downloading")

@pytest.fixture(autouse=True,scope="session")
def download():
    if not video_path.exists():
        youtube_video_download('https://github.com/akhildevelops/streamlit/raw/main/retail_store.mp4',video_path)