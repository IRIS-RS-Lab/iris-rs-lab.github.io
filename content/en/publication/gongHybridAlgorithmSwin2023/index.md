---
title: "A Hybrid Algorithm with Swin Transformer and Convolution for Cloud Detection"
date: 2023-01-01
summary: "Published in Remote Sensing."
authors: ["Gong, Chengjuan", "Long, Tengfei", "Yin, Ranyu", "Jiao, Weili", "Wang, Guizhou"]
tags: ["notion"]
featured: false
links:
  - name: PDF
    url: ""
    icon: hero/document
  - name: Code
    url: ""
    icon: brands/github
---

## Abstract
Cloud detection is critical in remote sensing image processing, and convolutional neural networks (CNNs) have significantly advanced this field. However, traditional CNNs primarily focus on extracting local features, which can be challenging for cloud detection due to the variability in the size, shape, and boundaries of clouds. To address this limitation, we propose a hybrid Swin transformer--CNN cloud detection (STCCD) network that combines the strengths of both architectures. The STCCD network employs a novel dual-stream encoder that integrates Swin transformer and CNN blocks. Swin transformers can capture global context features more effectively than traditional CNNs, while CNNs excel at extracting local features. The two streams are fused via a fusion coupling module (FCM) to produce a richer representation of the input image. To further enhance the network's ability in extracting cloud features, we incorporate a feature fusion module based on the attention mechanism (FFMAM) and an aggregation multiscale feature module (AMSFM). The FFMAM selectively merges global and local features based on their importance, while the AMSFM aggregates feature maps from different spatial scales to obtain a more comprehensive representation of the cloud mask. We evaluated the STCCD network on three challenging cloud detection datasets (GF1-WHU, SPARCS, and AIR-CD), as well as the L8-Biome dataset to assess its generalization capability. The results show that the STCCD network outperformed other state-of-the-art methods on all datasets. Notably, the STCCD model, trained on only four bands (visible and near-infrared) of the GF1-WHU dataset, outperformed the official Landsat-8 Fmask algorithm in the L8-Biome dataset, which uses additional bands (shortwave infrared, cirrus, and thermal).

## Method & Results
<!-- Uncomment below and place 'featured.jpg' in this folder -->
<!-- ![](featured.jpg) -->
<!-- *Teaser or key result figure.* -->

## Code & Data
- Code: 
- Data: 

## Citation
```bibtex
@article{gongHybridAlgorithmSwin2023,
  title={A Hybrid Algorithm with Swin Transformer and Convolution for Cloud Detection},
  author={Gong, Chengjuan and Long, Tengfei and Yin, Ranyu and Jiao, Weili and Wang, Guizhou},
  journal={Remote Sensing},
  year={2023}
}
```
