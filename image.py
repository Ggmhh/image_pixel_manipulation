from PIL import Image
import os

def resize_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                resized_img = img.resize((width, height), Image.LANCZOS)
                resized_img.save(output_path)
                print(f"Изображение {filename} успешно изменено")

input_folder = input("Введите путь к папке с изображениями: ")
output_folder = input("Введите путь к папке для сохранения измененных изображений: ")
width = int(input("Введите ширину изображения: "))
height = int(input("Введите высоту изображения: "))

resize_images(input_folder, output_folder, width, height)
