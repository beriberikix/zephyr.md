---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/video-controls_8h.html
original_path: doxygen/html/video-controls_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video-controls.h File Reference

Public APIs for Video.
[More...](#details)

[Go to the source code of this file.](video-controls_8h_source.md)

| Macros | |
| --- | --- |
| Stateful codec controls IDs | |
| #define | [VIDEO\_CID\_CODEC\_CLASS\_BASE](group__video__controls.md#gadf37e306a8d73cec4674422e74ffc85e)   0x00990900 |
| Camera class controls IDs | |
| #define | [VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26)   0x009a0900 |
| #define | [VIDEO\_CID\_ZOOM\_ABSOLUTE](group__video__controls.md#ga1033858d5515c2016a0cc6ac06fd8b91)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 13) |
|  | Amount of optical zoom applied through to the camera optics. |
| Camera Flash class control IDs | |
| #define | [VIDEO\_CID\_FLASH\_CLASS\_BASE](group__video__controls.md#ga9e0c8dc67fab1a80f81cd4be2e875954)   0x009c0900 |
| JPEG class control IDs | |
| #define | [VIDEO\_CID\_JPEG\_CLASS\_BASE](group__video__controls.md#ga9281f5a61120a6de015a9bbc75ee8b91)   0x009d0900 |
| #define | [VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY](group__video__controls.md#ga883c2a761ea0f00e83c884a5b4b45eee)   ([VIDEO\_CID\_JPEG\_CLASS\_BASE](group__video__controls.md#ga9281f5a61120a6de015a9bbc75ee8b91) + 3) |
|  | Quality (Q) factor of the JPEG algorithm, also increasing the data size. |
| Image Source class control IDs | |
| #define | [VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE](group__video__controls.md#ga3cc32750dec0096ea873ea13e83d202e)   0x009e0900 |
| Image Processing class control IDs | |
| #define | [VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7)   0x009f0900 |
| #define | [VIDEO\_CID\_PIXEL\_RATE](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7) + 2) |
|  | Pixel rate (pixels/second) in the device's pixel array. |
| #define | [VIDEO\_CID\_TEST\_PATTERN](group__video__controls.md#gad1ce88a5c071eaeb8d5db9dc722a2cd4)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7) + 3) |
|  | Selection of the type of test pattern to represent. |
| Vendor-specific class control IDs | |
| #define | [VIDEO\_CID\_PRIVATE\_BASE](group__video__controls.md#ga05e2fe16eafe259061af62ac31dfaeca)   0x08000000 |

| Base class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)   0x00980900 |
| #define | [VIDEO\_CID\_BRIGHTNESS](group__video__controls.md#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 0) |
|  | Amount of perceived light of the image, the luma (Y') value. |
| #define | [VIDEO\_CID\_CONTRAST](group__video__controls.md#ga9ca85f6b1d9add05eacb008dc4ccb2e4)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 1) |
|  | Amount of difference between the bright colors and dark colors. |
| #define | [VIDEO\_CID\_SATURATION](group__video__controls.md#ga200017c2141f5c90ade652224d1d4364)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 2) |
|  | Colorfulness of the image while preserving its brightness. |
| #define | [VIDEO\_CID\_HUE](group__video__controls.md#ga588a1206d5046a7b9e8415db725cae81)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 3) |
|  | Shift in the tint of every colors, clockwise in a RGB color wheel. |
| #define | [VIDEO\_CID\_EXPOSURE](group__video__controls.md#ga24e259a6466537377b7bb8a151311ae1)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 17) |
|  | Amount of time an image sensor is exposed to light, affecting the brightness. |
| #define | [VIDEO\_CID\_GAIN](group__video__controls.md#ga36259be44d9d08b149fd35dd28bbaf50)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 19) |
|  | Amount of amplification performed to each pixel electrical signal, affecting the brightness. |
| #define | [VIDEO\_CID\_HFLIP](group__video__controls.md#ga59aa47b6f558ef5ae64a67f4a7ac7e31)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 20) |
|  | Flip the image horizontally: the left side becomes the right side. |
| #define | [VIDEO\_CID\_VFLIP](group__video__controls.md#ga16651a6825b619399a333ed39e802dfc)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 21) |
|  | Flip the image vertically: the top side becomes the bottom side. |
| #define | [VIDEO\_CID\_POWER\_LINE\_FREQUENCY](group__video__controls.md#ga762a6c2b0fb032b9ebdfeff5ed15c3de)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 24) |
|  | Frequency of the power line to compensate for, avoiding flicker due to artificial lighting. |
| #define | [VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE](group__video__controls.md#ga0670d89542dc532a9c775e8e9c2638b1)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 26) |
|  | Balance of colors in direction of blue (cold) or red (warm). |
| enum | [video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a) { [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) = 0 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) = 1 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) = 2 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) = 3 } |

## Detailed Description

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
