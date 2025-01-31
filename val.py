import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp/weights/best.pt')
    model.val(data='TT100K_2021.yaml',
              split='test',
              imgsz=640,
              batch=1,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )