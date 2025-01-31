1.First install the environment.
  pip install -r requirements.txt

2.Once the dataset is downloaded to the specified location for processing and placed correctly, it is a public dataset.
  The link to the datasets is:
  TT100K_2021:https://cg.cs.tsinghua.edu.cn/traffic-sign/
  CCTSDB_2021:https://github.com/csust7zhangjm/CCTSDB2021
  
  in the datasets folder
  process.py:The TT100K_2021 dataset was processed to obtain the YOLO format dataset, and a large number of 45 categories of traffic sign pictures were filtered. 
  split_data.py:The TT100K_2021 dataset is divided into a 7:1:2 ratio.

3.Configure several paths in the TT100K_2021.yaml file.

4.Execute python train.py to start training.







《Enhanced YOLOv8n for Traffic Sign Detection with Improved Feature Extraction and Fusion》

 The Visual Computer
