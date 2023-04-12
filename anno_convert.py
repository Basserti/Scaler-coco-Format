import json
import os
from tqdm import tqdm


AUTHOR = 'Basserti'


def convert(ptj, sc):
    '''
    Variables:
        ptj - The path to the file with the annotation.
                Example: 'dir1/annotations/instances_default.json'.
        sc - The coefficient by which the image will be scalers.
                Example: '0.5'.
    Output:
        The function returns nothing.
        The result of the work is a folder 
        with a file where all the values are scaled.       
    '''
    
    with open(ptj, "r") as read_file:
        data = json.load(read_file)
    
    ptds = __get_path_to_dir_scale(ptj)
    if not os.path.exists(ptds):
        os.makedirs(ptds)
        
    for image in tqdm(range(len(data['images']))):
        path = data['images'][image]['file_name']
        
        data['images'][image]['file_name'] = path[
            path.rfind('/')+1:path.rfind('.')
        ] + '.png'

        data['images'][image]['width'] = int(
            data['images'][image]['width'] * sc
        )
        data['images'][image]['height'] = int(
            data['images'][image]['height'] * sc
        )

    for index in tqdm(range(len(data['annotations']))):
        for index2 in range(len(data['annotations'][index]['segmentation'][0])):
            data['annotations'][index]['segmentation'][0][index2] *= sc
        for index2 in range(len(data['annotations'][index]['bbox'])):
            data['annotations'][index]['bbox'][index2] *= sc

        tmp = data['annotations'][index]['segmentation'][0]
        n = len(tmp)
        sum1 = 0
        sum2 = 0
        xn = tmp[n-2]
        y1 = tmp[1]

        x1 = tmp[0]
        yn = tmp[n-1]

        for i in range(0, n, 2):
            if i == n-2:
                xi = tmp[i]
                yip1 = tmp[n-i-1]
                xip1 = tmp[n-i-2]
                yi = tmp[i+1]
            else:
                xi = tmp[i]
                yip1 = tmp[i+3]
                xip1 = tmp[i+2]
                yi = tmp[i+1]
            sum1 = sum1 + (xi*yip1)
            sum2 = sum2 + (xip1*yi)

        area_img = abs(sum1-sum2)/2
        data['annotations'][index]['area'] = area_img

    with open(ptds + ptj[ptj.rfind('/'):], "w") as write_backup_file:
        json.dump(data, write_backup_file)
        

def __get_path_to_dir_scale(path):
    '''
    !!! THIS IS LOCAL FUNCTION !!!
    '''
    return path[:path.rfind('/')] + "_scale/"


#if __name__ == '__main__':
#    path_to_json = 'openpits/annotations/instances_default.json'
#    scalar_size = 0.5
#    convert(path_to_json, scalar_size)