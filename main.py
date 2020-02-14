from PIL import Image
import os


def resize_image(image_path, new_dimension):
    try:
        img = Image.open(image_path)
        resized_img = img.resize((new_dimension, new_dimension))

        output_path = f'{os.path.splitext(image_path)[0]}_result_{new_dimension}x{new_dimension}{os.path.splitext(image_path)[1]}'

        resized_img.save(output_path)

        print(f'Image saved at {output_path}')
    except FileNotFoundError:
        print(f'File not found')


if __name__ == '__main__':
    while True:
        file_path = input('Please enter the entire path to the image: ')
        if os.path.exists(file_path):
            break
    try:
        dimension = int(input('Enter positive integer for dimensions of square image: '))
        assert isinstance(dimension, int)
    except ValueError:
        print("Dimension input was not a positive integer")
        exit(1)
    resize_image(file_path, dimension)