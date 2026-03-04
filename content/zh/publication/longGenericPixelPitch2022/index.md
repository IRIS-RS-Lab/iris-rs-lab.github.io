---
title: "A Generic Pixel Pitch Calibration Method for Fundus Camera via Automated ROI Extraction"
date: 2022-11-01
summary: "Published in Sensors."
authors: ["Long, Tengfei", "Xu, Yi", "Zou, Haidong", "Lu, Lina", "Yuan, Tianyi", "Dong, Zhou", "Dong, Jiqun", "Ke, Xin", "Ling, Saiguang", "Ma, Yingyan"]
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
Pixel pitch calibration is an essential step to make the fundus structures in the fundus image quantitatively measurable, which is important for the diagnosis and treatment of many diseases, e.g., diabetes, arteriosclerosis, hereditary optic atrophy, etc. The conventional calibration approaches require the specific parameters of the fundus camera or several specially shot images of the chess board, but these are generally not accessible, and the calibration results cannot be generalized to other cameras. Based on automated ROI (region of interest) and optic disc detection, the diameter ratio of ROI and optic disc (ROI--disc ratio) is quantitatively analyzed for a large number of fundus images. With the prior knowledge of the average diameter of an optic disc in fundus, the pixel pitch can be statistically estimated from a large number of fundus images captured by a specific camera without the availability of chess board images or detailed specifics of the fundus camera. Furthermore, for fundus cameras of FOV (fixed field-of-view), the pixel pitch of a fundus image of 45$^\circ$ FOV can be directly estimated according to the automatically measured diameter of ROI in the pixel. The average ROI--disc ratio is approximately constant, i.e., 6.404 \textpm 0.619 in the pixel, according to 40,600 fundus images, captured by different cameras, of 45$^\circ$ FOV. In consequence, the pixel pitch of a fundus image of 45$^\circ$ FOV can be directly estimated according to the automatically measured diameter of ROI in the pixel, and results show the pixel pitches of Canon CR2, Topcon NW400, Zeiss Visucam 200, and Newvision RetiCam 3100 cameras are 6.825 \textpm 0.666 $\mu$m, 6.625 \textpm 0.647 $\mu$m, 5.793 \textpm 0.565 $\mu$m, and 5.884 \textpm 0.574 $\mu$m, respectively. Compared with the manually measured pixel pitches, based on the method of ISO 10940:2009, i.e., 6.897 $\mu$m, 6.807 $\mu$m, 5.693 $\mu$m, and 6.050 $\mu$m, respectively, the bias of the proposed method is less than 5\%. Since our method doesn't require chess board images or detailed specifics, the fundus structures on the fundus image can be measured accurately, according to the pixel pitch obtained by this method, without knowing the type and parameters of the camera.

## Method & Results
<!-- Uncomment below and place 'featured.jpg' in this folder -->
<!-- ![](featured.jpg) -->
<!-- *Teaser or key result figure.* -->

## Code & Data
- Code: 
- Data: 

## Citation
```bibtex
@article{longGenericPixelPitch2022,
  title={A Generic Pixel Pitch Calibration Method for Fundus Camera via Automated ROI Extraction},
  author={Long, Tengfei and Xu, Yi and Zou, Haidong and Lu, Lina and Yuan, Tianyi and Dong, Zhou and Dong, Jiqun and Ke, Xin and Ling, Saiguang and Ma, Yingyan},
  journal={Sensors},
  year={2022}
}
```
