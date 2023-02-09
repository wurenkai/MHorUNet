# MHorUNet
This is the official code repository for "MHorUNet:High-order Spatial Interaction UNet for Skin Lesion Segmentation", 

**0. Main Environments**
- python 3.8
- pytorch 1.8.0
- torchvision 0.9.0

**1. Prepare the dataset.**

1- Download the ISIC 2017 train dataset from [this](https://challenge.isic-archive.com/data) link and extract both training dataset and ground truth folders inside the `/data/dataset_isic17/`. </br>
2- Run `Prepare_ISIC2017.py` for data preperation and dividing data to train,validation and test sets. </br>

**Notice:**
For training and evaluating on ISIC 2018 and pH2 follow the bellow steps: :</br>
1- Download the ISIC 2018 train dataset from [this](https://challenge.isic-archive.com/data) link and extract both training dataset and ground truth folders inside the `/data/dataset_isic18/`. </br> then Run ` Prepare_ISIC2018.py` for data preperation and dividing data to train,validation and test sets. </br>
2- Download the ph2 dataset from [this](https://www.dropbox.com/s/k88qukc20ljnbuo/PH2Dataset.rar) link and extract it then Run ` 	Prepare_PH2_test.py` for data preperation and dividing data to train,validation and test sets. </br>

**2. Train the MHorUNet.**
```
python train.py
```
- After trianing, you could obtain the outputs in './results/'

**3. Test the MHorUNet.**
First, in the test.py file, you should change the address of the checkpoint in 'resume_model' and fill in the location of the test data in 'data_path'.
```
python test.py
```
- After testing, you could obtain the outputs in './results/'

## References

---
