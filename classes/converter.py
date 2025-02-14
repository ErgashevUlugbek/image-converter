import os
from PIL import Image

class ImageConverter:
    max_width = None
    max_height = None
    folder = ''
    count = 0

    def __init__(self):
        pass

    def set_source_path(self, source_path):
        self.folder = source_path

    def convert_to_webp(self, input_path, output_path):
        with Image.open(input_path) as img:
            # Save as WebP
            img.save(output_path, "WEBP", quality=90)
        os.remove(input_path)
        self.count += 1

    def batch_convert(self):
        for file in os.listdir(self.folder):
            print(file)
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
                input_path = os.path.join(self.folder, file)
                output_path = os.path.join(self.folder, os.path.splitext(file)[0] + ".webp")
                self.convert_to_webp(input_path, output_path)
                print(f"Converted: {file} -> {output_path}")
