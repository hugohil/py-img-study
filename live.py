import cv2
import numpy as np
from PIL import Image
import glob
import time

def create_video_from_images(image_folder, ext, speed=1, fps=30):
  image_files = glob.glob(f"{image_folder}/*.{ext}")
  images = [np.array(Image.open(image)) for image in image_files]

  height, width, layers = images[0].shape
  size = (width, height)

  output_video_path = f"output/live-speed{speed}-{time.time()}.mp4"

  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  video = cv2.VideoWriter(output_video_path, fourcc, fps * speed, size)

  for image in images:
    image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    video.write(image_cv)

  video.release()

create_video_from_images("./medias/sequence", "png", 1, 30)