import os
from PIL import Image
from tqdm import tqdm


AUTHOR = 'Basserti'


def scale_image(ptd, sc):
    '''
    Variables:
        ptd - The path to the directory where the images are located.
                Example: 'dir1/dir_with_images/'.
        sc - The coefficient by which the image will be scalers.
                Example: '0.5'.
    Output:
        The function returns nothing.
        The result of the work is a folder with images of the selected scale.        
    '''
    ptds = __get_path_to_dir_scale(ptd)

    if not os.path.exists(ptds):
        os.makedirs(ptds)

    images = []

    try:
        path_images = os.listdir(ptd)
        path_images.sort(key=len)
    except OSError as err:
        print("OS error:", err)

    try:
        for path in path_images:
            images.append(Image.open(ptd + path))
    except OSError as err:
        print("OS error:", err)

    for img in tqdm(images):
        name = ptds + img.filename.replace(ptd, '')
        with Image.open(img.filename) as im:
            im.resize(
                (int(im.size[0] * sc),
                 int(im.size[1] * sc))
            ).save(name[:name.rfind('.')]+'.PNG')



def __get_path_to_dir_scale(path):
    '''
    !!! THIS IS LOCAL FUNCTION !!!
    '''
    return path[:path.rfind('/')] + "_scale/"
                

#if __name__ == '__main__':
#    path_to_dir = 'openpits/images/'
#    scalar_size = 0.5
#    resize(path_to_dir, scalar_size)