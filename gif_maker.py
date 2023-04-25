from PIL import Image
import os

def create_gif(png_files, output_gif, duration=100):
    images = [Image.open(file) for file in png_files]
    
    # Save the images as a GIF
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0,
    )

def main():
    # Specify the directory containing the PNG images
    png_dir = 'pngs'
    png_files = [os.path.join(png_dir, f) for f in os.listdir(png_dir) if f.endswith('.png')]

    # Sort the files to maintain the correct order
    png_files.sort()

    # Specify the output GIF file
    output_gif = 'output.gif'

    # Set the duration between frames in milliseconds (e.g., 100 ms)
    duration = 50

    create_gif(png_files, output_gif, duration)

if __name__ == '__main__':
    main()
