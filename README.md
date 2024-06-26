<div id="top" align="center">

# MHorUNet
**MHorUNet:High-order Spatial Interaction UNet for Skin Lesion Segmentation**
  [[paper link]](https://doi.org/10.1016/j.bspc.2023.105517)
  
  Renkai Wu, Pengchen Liang, Xuan Huang, Liu Shi, Yuandong Gu, Haiqin Zhu*, Qing Chang*

</div>

**0. Main Environments**
- python 3.8
- pytorch 1.8.0
- torchvision 0.9.0

**1. Prepare the dataset.**

1- Download the ISIC 2017 train dataset from [this](https://challenge.isic-archive.com/data) link and extract both training dataset and ground truth folders inside the `/data/dataset_isic17/`. </br>
2- Run `Prepare_ISIC2017.py` for data preparation and dividing data to train,validation and test sets. </br>

**Notice:**
For training and evaluating on ISIC 2018 and pH2 follow the bellow steps: :</br>
1- Download the ISIC 2018 train dataset from [this](https://challenge.isic-archive.com/data) link and extract both training dataset and ground truth folders inside the `/data/dataset_isic18/`. </br> then Run ` Prepare_ISIC2018.py` for data preparation and dividing data to train,validation and test sets. </br>
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

## Citation
If you find this repository helpful, please consider citing:
```
@article{wu2024mhorunet,
  title={MHorUNet: High-order spatial interaction UNet for skin lesion segmentation},
  author={Wu, Renkai and Liang, Pengchen and Huang, Xuan and Shi, Liu and Gu, Yuandong and Zhu, Haiqin and Chang, Qing},
  journal={Biomedical Signal Processing and Control},
  volume={88},
  pages={105517},
  year={2024},
  publisher={Elsevier}
}
```

## References
- [HorNet](https://github.com/raoyongming/HorNet)
- [MALUNet](https://github.com/JCruan519/MALUNet)
---
