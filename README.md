# Scaler-coco-Format
Scaling a data set in COCO format.

The result of the work is a scaled dataset in the source directory with the prefix '_scaler'.

Example for `Jupyter Notebook`:
``` Jupyter
from coco_scaler_convert import scaler_convertor

scaler_convertor('dataset/', 0.5)
```
If the directory name is "dataset", then the dataset is scaled to 0.5 of its size.

Example for `Shell`:
``` Shell
python coco_scaler_convert.py
```
If the directory name is different from "dataset" or you need to choose a different value for scaling, then you need to pass the file name and the scaling variable.

Example for `Shell`:
``` Shell
python coco_scaler_convert.py dataset/ 0.5
```

Version 1.0
