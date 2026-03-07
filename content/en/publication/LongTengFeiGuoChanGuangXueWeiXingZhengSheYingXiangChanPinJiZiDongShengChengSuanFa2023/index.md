---
title: "国产光学卫星正射影像产品及自动生成算法"
date: 2023-04-01
summary: "Published in 遥感学报."
authors: ["龙腾飞", "焦伟利", "何国金", "王桂周", "张兆明"]
tags: ["notion"]
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
正射校正是卫星遥感影像后续处理、分析与应用的必要基础，而目前光学卫星数据自主定位精度尚不能达到1---2像元，正射影像产品的生产仍需依赖地面控制点对成像几何模型进行修正。针对国产光学卫星数据的现状、特点和应用需求，中国遥感卫星地面站自主研发了国产光学卫星正射影像产品和自动正射系统，本文从精细化影像自动配准、成像几何模型优化、影像正射校正、几何不确定度评估、太阳照射和卫星观测角度计算、基于地理格网的影像剖分等方面对相关产品及其自动生成算法进行介绍。其中，基于L1范数约束最小二乘的RPC模型全参数优化方法，可在影像幅宽较大或几何定标精度不足时获得比常规附加像方仿射变换参数的RPC模型更高的校正精度；提出顾及控制点精度的区域网平差方法，在利用从空间分辨率较低的参考影像获取的控制点修正成像几何模型时，可在满足参考影像几何约束的前提下，通过多次观测减小成像几何模型的随机误差、提高影像的几何定位精度；基于不确定度传播理论，建立了正射影像产品逐像元几何不确定度评估方法。试验结果表明，本文算法可用于规模化的正射影像产品生产，分布于全国不同区域的实测检查点表明所生产的16 m分辨率国产高分正射影像产品绝对几何精度可达到2像元以内。

## Method & Results
<!-- Uncomment below and place 'featured.jpg' in this folder -->
<!-- ![](featured.jpg) -->
<!-- *Teaser or key result figure.* -->

## Code & Data
- Code: 
- Data: 

## Citation
```bibtex
@article{LongTengFeiGuoChanGuangXueWeiXingZhengSheYingXiangChanPinJiZiDongShengChengSuanFa2023,
  title={国产光学卫星正射影像产品及自动生成算法},
  author={龙腾飞 and 焦伟利 and 何国金 and 王桂周 and 张兆明},
  journal={遥感学报},
  year={2023}
}
```


