# Yolov1

> pytorch implementation of yolov1 on aerial image dataset

YOLO (You only look once) v1 is proposed by Joseph Redmon et al. The link to original paper is [here](https://arxiv.org/abs/1506.02640.pdf)


## Usage

`bash get_dataset.sh` to download dataset
`bash get_model.sh` to download pretrained model

`python test.py` to visualize or test on image


`python train.py` to start training, arguments include:
```
```


#### Requirements


## Module explanation

`datafunc.py`, `augment.py` is for processing images and bouding box informations
`vggmodel.py`, `resnetmodel.py` is yolo models with vgg backbone and resnet backbone respectively.
`yololoss.py`

`trainer.py` is for training

`predfunc.py`, `visualization.py`, `evaluation.py`

`predictor.py` is for prediction

