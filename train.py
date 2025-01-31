import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8n-RFAConv-CA-ASF-WIoUv3.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='TT100K_2021.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=32,
                close_mosaic=10,
                workers=8,
                device='0',
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )
    
