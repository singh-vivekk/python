import time
import concurrent.futures
from PIL import Image, ImageFilter

import os

# for i in img_names:
#     print(i)

# img_names = [
#     'photo-1516117172878-fd2c41f4a759.jpg',
#     'photo-1532009324734-20a7a5813719.jpg',
#     'photo-1524429656589-6633a470097c.jpg',
#     'photo-1530224264768-7ff8c1789d79.jpg',
#     'photo-1564135624576-c5c88640f235.jpg',
#     'photo-1541698444083-023c97d3f4b6.jpg',
#     'photo-1522364723953-452d3431c267.jpg',
#     'photo-1513938709626-033611b8cc03.jpg',
#     'photo-1507143550189-fed454f93097.jpg',
#     'photo-1493976040374-85c8e12f0c0e.jpg',
#     'photo-1504198453319-5ce911bafcde.jpg',
#     'photo-1530122037265-a5f1f91d3b99.jpg',
#     'photo-1516972810927-80185027ca84.jpg',
#     'photo-1550439062-609e1531270e.jpg',
#     'photo-1549692520-acc6669e2f0c.jpg'
# ]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    print("inside method call...")
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(5))
    img_name = img_name.split('\\')[-1]

    path = r'C:\Users\Administrator\Desktop\imgs'
    path = path + '\processed'
    img_name = f'{path}/{img_name}'

    img.thumbnail(size)
    img.save(f'{img_name}')
    print(f'{img_name} was processed...')

if __name__ == '__main__':

    img_names = []
    path = r'C:\Users\Administrator\Desktop\imgs'
    img_names = os.listdir(path)
    img_names = list(img_names)
    print(type(img_names))

    print(img_names)

    img_names = [path+'\\'+img_name for img_name in img_names]
    print(img_names)

# MultiProcessing :
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_image, img_names)

# MultiThreading :
    print("between multiprocessing and Multithreading")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(process_image, img_names)

# Sequential execution:
    # for img_name in img_names:
    #     if img_name.__contains__('.jpg'):
    #         process_image(img_name)

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')