---
title: "An Extension of Phase Correlation-Based Image Registration to Estimate Similarity Transform Using Multiple Polar Fourier Transform"
date: 2018-10-01
summary: "Published in Remote Sensing."
authors: ["Dong, Yunyun", "Jiao, Weili", "Long, Tengfei", "He, Guojin", "Gong, Chengjuan"]
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
Image registration is a core technology of many different image processing areas and is widely used in the remote sensing community. The accuracy of image registration largely determines the effect of subsequent applications. In recent years, phase correlation-based image registration has drawn much attention because of its high accuracy and efficiency as well as its robustness to gray difference and even slight changes in content. Many researchers have reported that the phase correlation method can acquire a sub-pixel accuracy of 1 / 10 or even 1 / 100 . However, its performance is acquired only in the case of translation, which limits the scope of the application of the method. However, there are few reports on the estimation of scales and angles based on the phase correlation method. To take advantage of the high accuracy property and other merits of phase correlation-based image registration and extend it to estimate the similarity transform, we proposed a novel algorithm, the Multilayer Polar Fourier Transform (MPFT), which uses a fast and accurate polar Fourier transform with different scaling factors to calculate the log-polar Fourier transform. The structure of the polar grids of MPFT is more similar to the one of the log-polar grid. In particular, for rotation estimation only, the polar grid of MPFT is the calculation grid. To validate its effectiveness and high accuracy in estimating angles and scales, both qualitative and quantitative experiments were carried out. The quantitative experiments included a numerical simulation as well as synthetic and real data experiments. The experimental results showed that the proposed method, MPFT, performs better than the existing phase correlation-based similarity transform estimation methods, the Pseudo-polar Fourier Transform (PPFT) and the Multilayer Fractional Fourier Transform method (MLFFT), and the classical feature-based registration method, Scale-Invariant Feature Transform (SIFT), and its variant, ms-SIFT.

## Method & Results
<!-- Uncomment below and place 'featured.jpg' in this folder -->
<!-- ![](featured.jpg) -->
<!-- *Teaser or key result figure.* -->

## Code & Data
- Code: 
- Data: 

## Citation
```bibtex
@article{dongExtensionPhaseCorrelationBased2018,
  title={An Extension of Phase Correlation-Based Image Registration to Estimate Similarity Transform Using Multiple Polar Fourier Transform},
  author={Dong, Yunyun and Jiao, Weili and Long, Tengfei and He, Guojin and Gong, Chengjuan},
  journal={Remote Sensing},
  year={2018}
}
```
