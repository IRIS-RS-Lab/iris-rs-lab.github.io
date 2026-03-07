---
title: "30 m Resolution Global Annual Burned Area Mapping Based on Landsat Images and Google Earth Engine"
date: 2019-02-01
summary: "Published in Remote Sensing."
authors: ["Long, Tengfei", "Zhang, Zhaoming", "He, Guojin", "Jiao, Weili", "Tang, Chao", "Wu, Bingfang", "Zhang, Xiaomei", "Wang, Guizhou", "Yin, Ranyu"]
tags: ["global burned area", "Google Earth Engine", "Landsat", "temporal filtering", "time-series"]
featured: false
external_link: "#no-detail"
links:
  - name: PDF
    url: ""
    icon: hero/document
  - name: Code
    url: ""
    icon: brands/github
---

## Abstract
Heretofore, global Burned Area (BA) products have only been available at coarse spatial resolution, since most of the current global BA products are produced with the help of active fire detection or dense time-series change analysis, which requires very high temporal resolution. In this study, however, we focus on an automated global burned area mapping approach based on Landsat images. By utilizing the huge catalog of satellite imagery, as well as the high-performance computing capacity of Google Earth Engine, we propose an automated pipeline for generating 30-m resolution global-scale annual burned area maps from time-series of Landsat images, and a novel 30-m resolution Global annual Burned Area Map of 2015 (GABAM 2015) was released. All the available Landsat-8 images during 2014--2015 and various spectral indices were utilized to calculate the burned probability of each pixel using random decision forests, which were globally trained with stratified (considering both fire frequency and type of land cover) samples, and a seed-growing approach was conducted to shape the final burned areas after several carefully-designed logical filters (NDVI filter, Normalized Burned Ratio (NBR) filter, and temporal filter). GABAM 2015 consists of spatial extent of fires that occurred during 2015 and not of fires that occurred in previous years. Cross-comparison with the recent Fire\_cci Version 5.0 BA product found a similar spatial distribution and a strong correlation ( R 2 = 0.74) between the burned areas from the two products, although differences were found in specific land cover categories (particularly in agriculture land). Preliminary global validation showed the commission and omission errors of GABAM 2015 to be 13.17\% and 30.13\%, respectively.

## Method & Results
<!-- Uncomment below and place 'featured.jpg' in this folder -->
<!-- ![](featured.jpg) -->
<!-- *Teaser or key result figure.* -->

## Code & Data
- Code: 
- Data: 

## Citation
```bibtex
@article{long30ResolutionGlobal2019,
  title={30 m Resolution Global Annual Burned Area Mapping Based on Landsat Images and Google Earth Engine},
  author={Long, Tengfei and Zhang, Zhaoming and He, Guojin and Jiao, Weili and Tang, Chao and Wu, Bingfang and Zhang, Xiaomei and Wang, Guizhou and Yin, Ranyu},
  journal={Remote Sensing},
  year={2019}
}
```


