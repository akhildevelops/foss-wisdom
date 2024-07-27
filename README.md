# Visdom
Wisdom is a video intelligence platform

Objective:
[] Create a time series graph and live banner of avg time spent in billing counter.
[] Create a time series graph of avg time spent near the shelf.
[] Create live widget of number of people present in the store.

Implementation:
- Read the video feed into python   
- Define the bounding boxes for billing counter / rack
- Identify humans with bounding boxes in each frame and detect if they fall under billing counter / rack
- record number of frames that human is present in the pre-defined boxes
- Calculate avg wait time by (no: of total detected frames * frame time) / no: of humans
- To detect humans / track get an image encoder model and compare the bounding boxes images.
- Calculate avg video frame time
- 
