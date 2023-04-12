from img_scaler import scale_image
from anno_convert import convert


AUTHOR = 'Basserti'


def scaler_convertor(ptd_dataset, scaler_size):
    '''
    Variables:
        ptd_dataset - The path to the dataset.
                Example: 'dataset/'.
        scaler_size - The coefficient by which the image will be scalers.
                    Example: '0.5'.
    Output:
        The function returns nothing.
        The result of the work is a scaled dataset
        in the source directory with the prefix '_scaler'. 
    '''
    ptj = ptd_dataset + "annotations/instances_default.json"
    ptdi = ptd_dataset + "images/"
    print('Scaled images')
    scale_image(ptd=ptdi, sc=scaler_size)
    print('Json Conversion')
    convert(ptj=ptj, sc=scaler_size)