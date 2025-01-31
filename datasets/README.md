"Dataset placement folder"

File placement format：
datasets/
  TT100K_2021/
          images/
              train/
                  *.jpg
              val/
                  *.jpg
              test/
                  *.jpg
          labels/
              train/
                  *.txt
              val/
                  *.txt
              test/
                  *.txt

CCTSDB_2021 Similar


process.py:The TT100K_2021 dataset was processed to obtain the YOLO format dataset, and a large number of 45 categories of traffic sign pictures were filtered.
split_data.py:The TT100K_2021 dataset is divided into a 7:1:2 ratio
