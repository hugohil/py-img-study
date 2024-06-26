from PIL import Image
import numpy as np
import cv2
import glob
import time

def chrono_images(image_folder, ext="jpg", step=2):
  image_files = glob.glob(f"{image_folder}/*.{ext}")

  base_image = Image.open(image_files[0])
  base_image_np = np.array(base_image).astype(np.int32)

  for image_file in image_files[1::step]:
    current_image_np = np.array(Image.open(image_file)).astype(np.int32)

    subtracted_image_np = np.abs(base_image_np - current_image_np).astype(np.uint8)
    # subtracted_image = cv2.cvtColor(subtracted_image_np, cv2.COLOR_BGR2RGB)
    subtracted_image = Image.fromarray(subtracted_image_np.astype(np.uint8))

    base_image.paste(subtracted_image)
    base_image_np = np.array(base_image).astype(np.int32)

  base_image.save(f"output/chrono_image-{time.time()}.png")

chrono_images("./medias/seq3", "png", 30)
