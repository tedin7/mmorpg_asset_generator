from PIL import Image
import os

def fill_transparent_with_black(input_path, output_path):
    # Open the image
    img = Image.open(input_path)
    
    # Convert to RGBA if it's not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create a new image with black background
    background = Image.new('RGBA', img.size, (0, 0, 0, 255))
    
    # Paste the original image on the background
    background.paste(img, (0, 0), img)
    
    # Convert back to RGB (removing alpha channel)
    background = background.convert('RGB')
    
    # Save the result
    background.save(output_path)

def process_directory(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process all PNG files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            fill_transparent_with_black(input_path, output_path)
            print(f"Processed: {filename}")

# Example usage
input_directory = "input"
output_directory = "data"

process_directory(input_directory, output_directory)