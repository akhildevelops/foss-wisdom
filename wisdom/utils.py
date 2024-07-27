import matplotlib.pyplot as plt
import os
import subprocess
import glob
def calculate_avg_times(track_ids,frame_time):
    # Calculate
    cum_time=[0]
    cum_humans=[0]
    avg_time=[0]
    interacted_humans=set()
    for _i,img in enumerate(track_ids[1]):
        i=img[0]
        cum_time.append(cum_time[-1]+len(i)*frame_time)
        interacted_humans.update(i)
        cum_humans.append(len(interacted_humans))
        if cum_humans[-1]!=0:
            avg_time.append(cum_time[-1]/cum_humans[-1])
        else:
            avg_time.append(avg_time[-1])
    return avg_time

def save_img(index,img):
    plt.imsave("data" + "/file%02d.png" % index,img)

def frames_to_video(path:str):
    os.chdir(path)
    subprocess.call([
        'ffmpeg', '-y', '-framerate', '13', '-i', 'file%02d.png', '-r', '30', '-pix_fmt', 'yuv420p',
        'intelligent_video.mp4'
    ])
    for file_name in glob.glob("*.png"):
        os.remove(file_name)
    os.chdir("../")