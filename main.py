# Imports packages
from wisdom.video_loader import VideoLoader
from wisdom.retail.time_spent import TimeSpent,BBBox
from wisdom.model import Model
from wisdom.utils import calculate_avg_times,save_img,frames_to_video
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def main():

    # Initializes Video Loader and fetches the video from the endpoint to store in the path ./retail_store.mp4
    video = VideoLoader.from_url('https://github.com/akhildevelops/streamlit/raw/main/retail_store.mp4')
    metadata = video.metadata()
    # Initializes Machine learning model
    model = Model.default()
    
    # References billing counter in the video
    billing_counter_reference = BBBox(np.array([[80,51,208,113]]),"billing_counter")

    # Registers and analyses each video frame to identify customers present near the billing counter.
    # For implementation details check README.md
    ts = TimeSpent(model.model)
    track_ids = ts.time_spent(video,[billing_counter_reference])

    # Calculates average cumulative  time spent at the counter.
    # i.e, average time of the billing counter progresses with time.
    avg_time = calculate_avg_times(track_ids,metadata.frame_time)

    # Plot the averragetime in the graph.
    plt.plot(list(map(lambda x: x*metadata.frame_time,range(len(avg_time)))),avg_time)
    plt.savefig("billing_counter_avg_time.png")

    # Create an annotated video from the image frames.
    # For more info check README.md
    Path("data").mkdir(exist_ok=True)
    threads = ThreadPoolExecutor()
    assert metadata.n_frames==sum(1 for _ in threads.map(lambda index: save_img(index[0],index[1][1]), enumerate(track_ids[1])))
    frames_to_video("data")

    print("Check the annotated Video at data/intelligent_video.mp4")
    
if __name__=="__main__":
    main()
    
