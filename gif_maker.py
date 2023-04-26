import os
from PIL import Image

def process_image(img):
    img = img.convert('RGBA')
    width, height = img.size
    gif_img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            r, g, b, a = pixel

            if a < 128:
                gif_img.putpixel((x, y), (255, 255, 255, 0))
            else:
                gif_img.putpixel((x, y), (r, g, b, 255))

    # Create a palette with a transparent color
    palette = bytearray([255, 255, 255, 0, 0, 0] * 86)  # 86 * 3 = 258
    palette[0:3] = (255, 255, 255)
    palette[3:6] = (0, 0, 0)

    gif_img = gif_img.convert('P', palette=Image.ADAPTIVE, colors=256)
    gif_img.info['transparency'] = 0  # Set the first color in the palette as transparent

    return gif_img


def main():
    input_directory = 'pngs'
    output_filename = 'output.gif'
    
    png_files = [f for f in os.listdir(input_directory) if f.endswith('.png')]
    png_files.sort()

    images = []
    total_images = len(png_files)
    progress_interval = total_images // 10

    for index, png_file in enumerate(png_files):
        png_path = os.path.join(input_directory, png_file)
        img = Image.open(png_path)
        gif_img = process_image(img)
        images.append(gif_img)

        # Progress reporting
        if (index + 1) % progress_interval == 0:
            progress = int(((index + 1) / total_images) * 100)
            print(f"{progress}% completed")

    if images:
        images[0].save(
            output_filename,
            save_all=True,
            append_images=images[1:],
            duration=50,
            loop=0,
            transparency=0,
            disposal=2,
            optimize=False
        )
        print(f"GIF saved as {output_filename}")
    else:
        print("No PNG files found in the 'pngs' directory")

if __name__ == "__main__":
    main()
