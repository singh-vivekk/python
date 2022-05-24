import time
import concurrent.futures
from PIL import Image, ImageFilter
import requests
import multiprocessing
import numpy as np
from timebudget import timebudget

timebudget.set_quiet()         # don't show measurements as they happen
timebudget.report_at_exit()    # Generate report when the prog exits

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

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


# to download images
@timebudget
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    uimg_name = np.random.randint(1000000000)
    img_name = f'{img_name}{uimg_name}.jpg'
    with open(img_name, 'wb+') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

    process_image(img_name)
    print("\n Download and processing completed ")


if __name__ == '__main__':

    # img_names = []

# MultiProcessing :
#     with concurrent.futures.ProcessPoolExecutor() as executor:
        # results = executor.map(process_image, img_names)
        # results = executor.map(download_image, img_urls)


# MultiThreading :
#     print("between multiprocessing and Multithreading")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # results = executor.map(process_image, img_names)
        results = executor.map(download_image, img_urls)

# Sequential execution:
    # for img_name in img_names:
    #     if img_name.__contains__('.jpg'):
    #         process_image(img_name)

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')