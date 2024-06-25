import numpy as np
from PIL import Image
import glob
import time

def average_images(image_folder, ext="jpg"):
  image_files = glob.glob(f"{image_folder}/*.{ext}")
  images = [np.array(Image.open(image)) for image in image_files]

  average_image = np.mean(images, axis=0).astype(np.uint8)

  result_image = Image.fromarray(average_image)
  result_image.save(f"output/average_image-{time.time()}.jpg")

average_images("./medias/sequence", "png")
