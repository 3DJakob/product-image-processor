from PIL import Image
import os

def add_background(image_path, background_color=(233, 233, 233)):
    img = Image.open(image_path)
    # Create a new image with a solid background
    new_img = Image.new("RGB", img.size, background_color)
    # Paste the original image onto the new image with alpha blending
    new_img.paste(img, (0, 0), img)    
    return new_img

def main():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Create an output directory if it doesn't exist
    output_directory = os.path.join(current_directory, "output")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    
    # Filter out only image files
    image_files = [file for file in files if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    
    # Process each image file
    total_images = len(image_files)
    for i, image_file in enumerate(image_files, start=1):
        # Construct the full path to the image
        image_path = os.path.join(current_directory, image_file)
        
        # Add a background to the image
        new_image = add_background(image_path)
        
        # Save the new image with a background in the output directory
        output_path = os.path.join(output_directory, f'bg_{image_file}')
        new_image.save(output_path)
        
        # Show the progress
        print(f"Exporting image {i}/{total_images}", end='\r', flush=True)

if __name__ == "__main__":
    main()