from PIL import Image
import glob
import time

def blend_images(image_folder, ext="jpg"):
  alpha = 0.5
  image_files = glob.glob(f"{image_folder}/*.{ext}")

  base_image = Image.open(image_files[0])

  for image_file in image_files[1:]:
    current_image = Image.open(image_file)
    base_image = Image.blend(base_image, current_image, alpha)

  base_image.save(f"output/blended_image-alpha{alpha}-{time.time()}.png")

blend_images("./medias/sequence", "png")
