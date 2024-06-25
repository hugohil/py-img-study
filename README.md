You'll need some libraries:


```bash
$ python3 -m pip install numpy pillow opencv-python
```


If you have a timelapse video and need the image sequence, you can run:

```bash
$ ffmpeg -i input.mp4 output_%04d.png
```
