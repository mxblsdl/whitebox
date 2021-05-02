import whitebox
import os

wbt = whitebox.WhiteboxTools()
print(os.getcwd())

wbt.filter_lidar_classes(i="0106.las",output="output.las",  exclude_cls='1-5, 7-18')