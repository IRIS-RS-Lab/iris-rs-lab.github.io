---
title: "Eliminating the Effect of Image Border with Image Periodic Decomposition for Phase Correlation Based Remote Sensing Image Registration"
date: 2019-05-01
summary: "Published in Sensors."
authors: ["Dong, Yunyun", "Jiao, Weili", "Long, Tengfei", "Liu, Lanfa", "He, Guojin"]
tags: []
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
In the remote sensing community, accurate image registration is the prerequisite of the subsequent application of remote sensing images. Phase correlation based image registration has drawn extensive attention due to its high accuracy and high efficiency. However, when the Discrete Fourier Transform (DFT) of an image is computed, the image is implicitly assumed to be periodic. In practical application, it is impossible to meet the periodic condition that opposite borders of an image are alike, and image always shows strong discontinuities across the frame border. The discontinuities cause a severe artifact in the Fourier Transform, namely the known cross structure composed of high energy coefficients along the axes. Here, this phenomenon was referred to as effect of image border. Even worse, the effect of image border corrupted its registration accuracy and success rate. Currently, the main solution is blurring out the border of the image by weighting window function on the reference and sensed image. However, the approach also inevitably filters out non-border information of an image. The existing understanding is that the design of window function should filter as little information as possible, which can improve the registration success rate and accuracy of methods based on phase correlation. In this paper, another approach of eliminating the effect of image border is proposed, namely decomposing the image into two images: one being the periodic image and the other the smooth image. Replacing the original image by the periodic one does not suffer from the effect on the image border when applying Fourier Transform. The smooth image is analogous to an error image, which has little information except at the border. Extensive experiments were carried out and showed that the novel algorithm of eliminating the image border can improve the success rate and accuracy of phase correlation based image registration in some certain cases. Additionally, we obtained a new understanding of the role of window function in eliminating the effect of image border, which is helpful for researchers to select the optimal method of eliminating the effect of image border to improve the registration success rate and accuracy.

## Method & Results
<!-- Uncomment below and place 'featured.jpg' in this folder -->
<!-- ![](featured.jpg) -->
<!-- *Teaser or key result figure.* -->

## Code & Data
- Code: 
- Data: 

## Citation
```bibtex
@article{dongEliminatingEffectImage2019,
  title={Eliminating the Effect of Image Border with Image Periodic Decomposition for Phase Correlation Based Remote Sensing Image Registration},
  author={Dong, Yunyun and Jiao, Weili and Long, Tengfei and Liu, Lanfa and He, Guojin},
  journal={Sensors},
  year={2019}
}
```
