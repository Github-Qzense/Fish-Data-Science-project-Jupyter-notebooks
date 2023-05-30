import os
import rembg
from PIL import Image

def remove_bg(input_img_path, output_img_path):
    # Load the input image
    input_image = Image.open(input_img_path)
    file_extensions = ['.png', '.jpg', '.jpeg', '.webp']
    result = any(output_img_path.endswith(extension) for extension in file_extensions)
    if not result:
        output_img_path = output_img_path+"output.png"
        
    # Define the parameters
    params = {
        'rescale': 1.2,
        'alpha_matting': True,
        'alpha_matting_foreground_threshold': 0.7
    }

    # Remove the background with custom parameters
    output_image = rembg.remove(input_image, **params)

    # Remove the background
    # output_image = rembg.remove(input_image)
     
    # Save the result
    output_image.save(output_img_path)

