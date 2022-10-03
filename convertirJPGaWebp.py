from PIL import Image

im = Image.open('Image.JPG').convert("RGB")

im.save(".png", "png")
