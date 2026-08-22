---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__video__controls.html
original_path: doxygen/html/group__video__controls.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Video Controls

[Device Driver APIs](group__io__interfaces.md)

Video controls.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [video\_control](structvideo__control.md) |
|  | Video control structure. [More...](structvideo__control.md#details) |
| struct | [video\_ctrl\_range](structvideo__ctrl__range.md) |
| struct | [video\_ctrl\_query](structvideo__ctrl__query.md) |
| struct | [video\_control\_range](structvideo__control__range.md) |
|  | Video control range structure. [More...](structvideo__control__range.md#details) |
| struct | [video\_control\_query](structvideo__control__query.md) |
|  | Video control query structure. [More...](structvideo__control__query.md#details) |

| Base class control IDs | |
| --- | --- |
| enum | [video\_power\_line\_frequency](#ga9db809ab56484b4b5b1a047a97e6920a) { [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) = 0 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) = 1 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) = 2 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) = 3 } |
| enum | [video\_colorfx](#ga99f4b6cf21c8baaf510fbcfccb645960) {     [VIDEO\_COLORFX\_NONE](#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237) = 0 , [VIDEO\_COLORFX\_BW](#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735) = 1 , [VIDEO\_COLORFX\_SEPIA](#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37) = 2 , [VIDEO\_COLORFX\_NEGATIVE](#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0) = 3 ,     [VIDEO\_COLORFX\_EMBOSS](#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0) = 4 , [VIDEO\_COLORFX\_SKETCH](#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc) = 5 , [VIDEO\_COLORFX\_SKY\_BLUE](#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b) = 6 , [VIDEO\_COLORFX\_GRASS\_GREEN](#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1) = 7 ,     [VIDEO\_COLORFX\_SKIN\_WHITEN](#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef) = 8 , [VIDEO\_COLORFX\_VIVID](#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826) = 9 , [VIDEO\_COLORFX\_AQUA](#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c) = 10 , [VIDEO\_COLORFX\_ART\_FREEZE](#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd) = 11 ,     [VIDEO\_COLORFX\_SILHOUETTE](#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25) = 12 , [VIDEO\_COLORFX\_SOLARIZATION](#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715) = 13 , [VIDEO\_COLORFX\_ANTIQUE](#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b) = 14   } |
| #define | [VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)   0x00980900 |
| #define | [VIDEO\_CID\_BRIGHTNESS](#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 0) |
|  | Picture brightness, or more precisely, the black level. |
| #define | [VIDEO\_CID\_CONTRAST](#ga9ca85f6b1d9add05eacb008dc4ccb2e4)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 1) |
|  | Picture contrast or luma gain. |
| #define | [VIDEO\_CID\_SATURATION](#ga200017c2141f5c90ade652224d1d4364)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 2) |
|  | Picture color saturation or chroma gain. |
| #define | [VIDEO\_CID\_HUE](#ga588a1206d5046a7b9e8415db725cae81)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 3) |
|  | Hue or color balance. |
| #define | [VIDEO\_CID\_AUTO\_WHITE\_BALANCE](#ga7e2ce049ed534e1c29ac47d33013e180)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 12) |
|  | Automatic white balance (cameras). |
| #define | [VIDEO\_CID\_RED\_BALANCE](#gab534e6263a6b5caae48543346ba2f7ef)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 14) |
|  | Red chroma balance, as a ratio to the green channel. |
| #define | [VIDEO\_CID\_BLUE\_BALANCE](#gaf4d38f5eed6feb9ef9509c1747a332b8)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 15) |
|  | Blue chroma balance, as a ratio to the green channel. |
| #define | [VIDEO\_CID\_GAMMA](#ga4e38bb3fcb80b2d28fa88186b65e4fea)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 16) |
|  | Gamma adjust. |
| #define | [VIDEO\_CID\_EXPOSURE](#ga24e259a6466537377b7bb8a151311ae1)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 17) |
|  | Image sensor exposure time. |
| #define | [VIDEO\_CID\_AUTOGAIN](#gac1c1d3580b7ff84b6a461cea0b3942e8)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 18) |
|  | Automatic gain control. |
| #define | [VIDEO\_CID\_GAIN](#ga36259be44d9d08b149fd35dd28bbaf50)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 19) |
|  | Gain control. |
| #define | [VIDEO\_CID\_HFLIP](#ga59aa47b6f558ef5ae64a67f4a7ac7e31)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 20) |
|  | Flip the image horizontally: the left side becomes the right side. |
| #define | [VIDEO\_CID\_VFLIP](#ga16651a6825b619399a333ed39e802dfc)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 21) |
|  | Flip the image vertically: the top side becomes the bottom side. |
| #define | [VIDEO\_CID\_POWER\_LINE\_FREQUENCY](#ga762a6c2b0fb032b9ebdfeff5ed15c3de)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 24) |
|  | Frequency of the power line to compensate for, avoiding flicker due to artificial lighting. |
| #define | [VIDEO\_CID\_HUE\_AUTO](#ga9c0df146e6064169a89bd88b10085cec)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 25) |
|  | Enables automatic hue control by the device. |
| #define | [VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE](#ga0670d89542dc532a9c775e8e9c2638b1)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 26) |
|  | White balance settings as a color temperature in Kelvin. |
| #define | [VIDEO\_CID\_SHARPNESS](#gab0509f0d3106bca07658e7cfcb1883cf)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 27) |
|  | Adjusts the sharpness filters in a camera. |
| #define | [VIDEO\_CID\_BACKLIGHT\_COMPENSATION](#ga2f22b11b526154e66440eca74ec5bd66)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 28) |
|  | Adjusts the backlight compensation in a camera. |
| #define | [VIDEO\_CID\_COLORFX](#ga3fe7778ddb5c3f945b7649379a13321e)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 31) |
|  | Selects a color effect. |
| #define | [VIDEO\_CID\_AUTOBRIGHTNESS](#ga46bb41b012b1a2240270817b9ce57637)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 32) |
| #define | [VIDEO\_CID\_BAND\_STOP\_FILTER](#ga5d2c02644e26f6a7f9887d5879231106)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 33) |
|  | Switch the band-stop filter of a camera sensor on or off, or specify its strength. |
| #define | [VIDEO\_CID\_ALPHA\_COMPONENT](#ga78dcca8b4c8b29f23e983974b861f157)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 41) |
|  | Sets the alpha color component. |
| #define | [VIDEO\_CID\_LASTP1](#ga829221ec6ea7348e743173ce5e6bd635)   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 44) |
|  | Last base CID + 1. |

| Camera class controls IDs | |
| --- | --- |
| enum | [video\_exposure\_type](#ga167cf84b8f4259e6cdd333748deafaf6) { [VIDEO\_EXPOSURE\_AUTO](#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b) = 0 , [VIDEO\_EXPOSURE\_MANUAL](#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224) = 1 , [VIDEO\_EXPOSURE\_SHUTTER\_PRIORITY](#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61) = 2 , [VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd) = 3 } |
| enum | [video\_camera\_orientation](#ga1fb4e9981b362010439b9419691ac2af) { [VIDEO\_CAMERA\_ORIENTATION\_FRONT](#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef) = 0 , [VIDEO\_CAMERA\_ORIENTATION\_BACK](#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072) = 1 , [VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL](#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594) = 2 } |
| #define | [VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26)   0x009a0900 |
| #define | [VIDEO\_CID\_EXPOSURE\_AUTO](#gab83ae3ca7fa3da66243431d489be37bd)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 1) |
|  | Enables automatic adjustments of the exposure time and/or iris aperture. |
| #define | [VIDEO\_CID\_EXPOSURE\_ABSOLUTE](#ga036f78623bcae18ea9627d45d1209245)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 2) |
|  | Determines the exposure time of the camera sensor. |
| #define | [VIDEO\_CID\_EXPOSURE\_AUTO\_PRIORITY](#gaa5f2ebd1e1aef2da68be4742941c1f50)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 3) |
|  | Whether the device may dynamically vary the frame rate under the effect of auto-exposure Applicable when [VIDEO\_CID\_EXPOSURE\_AUTO](#gab83ae3ca7fa3da66243431d489be37bd) is set to [VIDEO\_EXPOSURE\_AUTO](#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b) or [VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd). |
| #define | [VIDEO\_CID\_PAN\_RELATIVE](#ga23ed465d76fc54680d1e22422b66c829)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 4) |
|  | This write-only control turns the camera horizontally by the specified amount. |
| #define | [VIDEO\_CID\_TILT\_RELATIVE](#ga7c51639505c7b97fb1953ade5fc72534)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 5) |
|  | This write-only control turns the camera vertically by the specified amount. |
| #define | [VIDEO\_CID\_PAN\_ABSOLUTE](#ga3b45437f606b8717dcadc22d56a706da)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 8) |
|  | This control turns the camera horizontally to the specified position. |
| #define | [VIDEO\_CID\_TILT\_ABSOLUTE](#gae474209914926f2bd38c99e020224b9c)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 9) |
|  | This control turns the camera vertically to the specified position. |
| #define | [VIDEO\_CID\_FOCUS\_ABSOLUTE](#ga9ce95d3c135a9221a8d0431d9df9836b)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 10) |
|  | This control sets the focal point of the camera to the specified position. |
| #define | [VIDEO\_CID\_FOCUS\_RELATIVE](#ga4137146c348efdcc8088f6be1274b164)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 11) |
|  | This write-only control moves the focal point of the camera by the specified amount. |
| #define | [VIDEO\_CID\_FOCUS\_AUTO](#ga031525e88a6c0f915903f5c9068589f4)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 12) |
|  | Enables continuous automatic focus adjustments. |
| #define | [VIDEO\_CID\_ZOOM\_ABSOLUTE](#ga1033858d5515c2016a0cc6ac06fd8b91)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 13) |
|  | Specify the objective lens focal length as an absolute value. |
| #define | [VIDEO\_CID\_ZOOM\_RELATIVE](#ga40e76f27e97549a779a6581bd210b0f4)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 14) |
|  | This write-only control sets the objective lens focal length relatively to the current value. |
| #define | [VIDEO\_CID\_ZOOM\_CONTINUOUS](#ga1a79541da7b7a37d9358fb1a3c42a1b7)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 15) |
|  | Start a continuous zoom movement. |
| #define | [VIDEO\_CID\_IRIS\_ABSOLUTE](#ga452858d6adfec3b58db6b26c96638fb2)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 17) |
|  | This control sets the camera's aperture to the specified value. |
| #define | [VIDEO\_CID\_IRIS\_RELATIVE](#ga8d1452dfe9c190f6e28e5e3dd35c52cc)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 18) |
|  | This write-only control modifies the camera's aperture by the specified amount. |
| #define | [VIDEO\_CID\_WIDE\_DYNAMIC\_RANGE](#ga9d224bc93e5c23317f9ccf89713a18d6)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 21) |
|  | Enables or disables the camera's wide dynamic range feature. |
| #define | [VIDEO\_CID\_PAN\_SPEED](#ga99996bce4091e4223130d9ae5e1024cd)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 32) |
|  | This control turns the camera horizontally at the specific speed. |
| #define | [VIDEO\_CID\_TILT\_SPEED](#ga3bfeedcd519191bcf1d684fd983ca9bc)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 33) |
|  | This control turns the camera vertically at the specified speed. |
| #define | [VIDEO\_CID\_CAMERA\_ORIENTATION](#ga57e5c3f562683a2b7ea1f96a58f633be)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 34) |
|  | This read-only control describes the camera position on the device It by reports where the camera camera is installed, its mounting position on the device. |
| #define | [VIDEO\_CID\_CAMERA\_SENSOR\_ROTATION](#ga0d48a910e8d6797842dc25b33fc3f187)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 35) |
|  | This read-only control describes the orientation of the sensor in the device. |

| Stateful codec controls IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_CODEC\_CLASS\_BASE](#gadf37e306a8d73cec4674422e74ffc85e)   0x00990900 |

| Camera Flash class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_FLASH\_CLASS\_BASE](#ga9e0c8dc67fab1a80f81cd4be2e875954)   0x009c0900 |

| JPEG class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_JPEG\_CLASS\_BASE](#ga9281f5a61120a6de015a9bbc75ee8b91)   0x009d0900 |
| #define | [VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY](#ga883c2a761ea0f00e83c884a5b4b45eee)   ([VIDEO\_CID\_JPEG\_CLASS\_BASE](#ga9281f5a61120a6de015a9bbc75ee8b91) + 3) |
|  | Quality (Q) factor of the JPEG algorithm, also increasing the data size. |

| Image Source class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE](#ga3cc32750dec0096ea873ea13e83d202e)   0x009e0900 |
| #define | [VIDEO\_CID\_ANALOGUE\_GAIN](#ga41b451aace98fb81633983a413d2724f)   ([VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE](#ga3cc32750dec0096ea873ea13e83d202e) + 3) |
|  | Analogue gain control. |

| Image Processing class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7)   0x009f0900 |
| #define | [VIDEO\_CID\_LINK\_FREQ](#ga2142e2819c445b70d82067a3cfb193c8)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7) + 1) |
|  | Link frequency, applicable for the CSI2 based devices. |
| #define | [VIDEO\_CID\_PIXEL\_RATE](#ga6f6eaed7defdbb5f440874c7c6d0a6eb)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7) + 2) |
|  | Pixel rate (pixels/second) in the device's pixel array. |
| #define | [VIDEO\_CID\_TEST\_PATTERN](#gad1ce88a5c071eaeb8d5db9dc722a2cd4)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7) + 3) |
|  | Selection of the type of test pattern to represent. |

| Vendor-specific class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_PRIVATE\_BASE](#ga05e2fe16eafe259061af62ac31dfaeca)   0x08000000 |

| Query flags, to be ORed with the control ID | |
| --- | --- |
| #define | [VIDEO\_CTRL\_FLAG\_NEXT\_CTRL](#ga6fc7bcd4b280b4598ea3a03108881b5c)   0x80000000 |

## Detailed Description

Video controls.

The Video control IDs (CIDs) are introduced with the same name as Linux V4L2 subsystem and under the same class. This facilitates inter-operability and debugging devices end-to-end across Linux and Zephyr.

This list is maintained compatible to the Linux kernel definitions in `linux/include/uapi/linux/v4l2-controls.h`

## Macro Definition Documentation

## [◆ ](#ga78dcca8b4c8b29f23e983974b861f157)VIDEO\_CID\_ALPHA\_COMPONENT

| #define VIDEO\_CID\_ALPHA\_COMPONENT   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 41) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Sets the alpha color component.

Some devices produce data with a user-controllable alpha component. Set the value applied to the alpha channel of every pixel produced.

## [◆ ](#ga41b451aace98fb81633983a413d2724f)VIDEO\_CID\_ANALOGUE\_GAIN

| #define VIDEO\_CID\_ANALOGUE\_GAIN   ([VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE](#ga3cc32750dec0096ea873ea13e83d202e) + 3) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Analogue gain control.

## [◆ ](#ga7e2ce049ed534e1c29ac47d33013e180)VIDEO\_CID\_AUTO\_WHITE\_BALANCE

| #define VIDEO\_CID\_AUTO\_WHITE\_BALANCE   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 12) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Automatic white balance (cameras).

## [◆ ](#ga46bb41b012b1a2240270817b9ce57637)VIDEO\_CID\_AUTOBRIGHTNESS

| #define VIDEO\_CID\_AUTOBRIGHTNESS   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 32) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#gac1c1d3580b7ff84b6a461cea0b3942e8)VIDEO\_CID\_AUTOGAIN

| #define VIDEO\_CID\_AUTOGAIN   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 18) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Automatic gain control.

## [◆ ](#ga2f22b11b526154e66440eca74ec5bd66)VIDEO\_CID\_BACKLIGHT\_COMPENSATION

| #define VIDEO\_CID\_BACKLIGHT\_COMPENSATION   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 28) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Adjusts the backlight compensation in a camera.

The minimum value disables backlight compensation.

## [◆ ](#ga5d2c02644e26f6a7f9887d5879231106)VIDEO\_CID\_BAND\_STOP\_FILTER

| #define VIDEO\_CID\_BAND\_STOP\_FILTER   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 33) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Switch the band-stop filter of a camera sensor on or off, or specify its strength.

Such band-stop filters can be used, for example, to filter out the fluorescent light component.

## [◆ ](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)VIDEO\_CID\_BASE

| #define VIDEO\_CID\_BASE   0x00980900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#gaf4d38f5eed6feb9ef9509c1747a332b8)VIDEO\_CID\_BLUE\_BALANCE

| #define VIDEO\_CID\_BLUE\_BALANCE   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 15) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Blue chroma balance, as a ratio to the green channel.

## [◆ ](#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)VIDEO\_CID\_BRIGHTNESS

| #define VIDEO\_CID\_BRIGHTNESS   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 0) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Picture brightness, or more precisely, the black level.

## [◆ ](#ga0a6e2c6287a67e8aa174bb0130fe4c26)VIDEO\_CID\_CAMERA\_CLASS\_BASE

| #define VIDEO\_CID\_CAMERA\_CLASS\_BASE   0x009a0900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga57e5c3f562683a2b7ea1f96a58f633be)VIDEO\_CID\_CAMERA\_ORIENTATION

| #define VIDEO\_CID\_CAMERA\_ORIENTATION   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 34) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This read-only control describes the camera position on the device It by reports where the camera camera is installed, its mounting position on the device.

This control is particularly meaningful for devices which have a well defined orientation, such as phones, laptops and portable devices since the control is expressed as a position relative to the device's intended usage orientation. , or , are said to have the [VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL](#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594) orientation.

## [◆ ](#ga0d48a910e8d6797842dc25b33fc3f187)VIDEO\_CID\_CAMERA\_SENSOR\_ROTATION

| #define VIDEO\_CID\_CAMERA\_SENSOR\_ROTATION   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 35) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This read-only control describes the orientation of the sensor in the device.

The value is the rotation correction in degrees in the counter-clockwise direction to be applied to the captured images once captured to memory to compensate for the camera sensor mounting rotation.

## [◆ ](#gadf37e306a8d73cec4674422e74ffc85e)VIDEO\_CID\_CODEC\_CLASS\_BASE

| #define VIDEO\_CID\_CODEC\_CLASS\_BASE   0x00990900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga3fe7778ddb5c3f945b7649379a13321e)VIDEO\_CID\_COLORFX

| #define VIDEO\_CID\_COLORFX   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 31) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Selects a color effect.

## [◆ ](#ga9ca85f6b1d9add05eacb008dc4ccb2e4)VIDEO\_CID\_CONTRAST

| #define VIDEO\_CID\_CONTRAST   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 1) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Picture contrast or luma gain.

## [◆ ](#ga24e259a6466537377b7bb8a151311ae1)VIDEO\_CID\_EXPOSURE

| #define VIDEO\_CID\_EXPOSURE   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 17) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Image sensor exposure time.

## [◆ ](#ga036f78623bcae18ea9627d45d1209245)VIDEO\_CID\_EXPOSURE\_ABSOLUTE

| #define VIDEO\_CID\_EXPOSURE\_ABSOLUTE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 2) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Determines the exposure time of the camera sensor.

The exposure time is limited by the frame in terval. Drivers should interpret the values as 100 µs units, where the value 1 stands for 1/10000th of a second, 10000 for 1 second and 100000 for 10 seconds.

## [◆ ](#gab83ae3ca7fa3da66243431d489be37bd)VIDEO\_CID\_EXPOSURE\_AUTO

| #define VIDEO\_CID\_EXPOSURE\_AUTO   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 1) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Enables automatic adjustments of the exposure time and/or iris aperture.

Manual exposure or iris changes when it is not [VIDEO\_EXPOSURE\_MANUAL](#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224) is undefined. Drivers should ignore such requests.

## [◆ ](#gaa5f2ebd1e1aef2da68be4742941c1f50)VIDEO\_CID\_EXPOSURE\_AUTO\_PRIORITY

| #define VIDEO\_CID\_EXPOSURE\_AUTO\_PRIORITY   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 3) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Whether the device may dynamically vary the frame rate under the effect of auto-exposure Applicable when [VIDEO\_CID\_EXPOSURE\_AUTO](#gab83ae3ca7fa3da66243431d489be37bd) is set to [VIDEO\_EXPOSURE\_AUTO](#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b) or [VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd).

Disabled by default: the frame rate must remain constant.

## [◆ ](#ga9e0c8dc67fab1a80f81cd4be2e875954)VIDEO\_CID\_FLASH\_CLASS\_BASE

| #define VIDEO\_CID\_FLASH\_CLASS\_BASE   0x009c0900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga9ce95d3c135a9221a8d0431d9df9836b)VIDEO\_CID\_FOCUS\_ABSOLUTE

| #define VIDEO\_CID\_FOCUS\_ABSOLUTE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 10) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This control sets the focal point of the camera to the specified position.

The unit is undefined. Positive values set the focus closer to the camera, negative values towards infinity.

## [◆ ](#ga031525e88a6c0f915903f5c9068589f4)VIDEO\_CID\_FOCUS\_AUTO

| #define VIDEO\_CID\_FOCUS\_AUTO   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 12) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Enables continuous automatic focus adjustments.

Manual focus adjustments while this control is on (set to 1) is undefined. Drivers should ignore such requests.

## [◆ ](#ga4137146c348efdcc8088f6be1274b164)VIDEO\_CID\_FOCUS\_RELATIVE

| #define VIDEO\_CID\_FOCUS\_RELATIVE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 11) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This write-only control moves the focal point of the camera by the specified amount.

The unit is undefined. Positive values move the focus closer to the camera, negative values towards infinity.

## [◆ ](#ga36259be44d9d08b149fd35dd28bbaf50)VIDEO\_CID\_GAIN

| #define VIDEO\_CID\_GAIN   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 19) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Gain control.

Most devices control only digital gain with this control. Devices that recognise the difference between digital and analogue gain use VIDEO\_CID\_DIGITAL\_GAIN and VIDEO\_CID\_ANALOGUE\_GAIN.

## [◆ ](#ga4e38bb3fcb80b2d28fa88186b65e4fea)VIDEO\_CID\_GAMMA

| #define VIDEO\_CID\_GAMMA   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 16) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Gamma adjust.

## [◆ ](#ga59aa47b6f558ef5ae64a67f4a7ac7e31)VIDEO\_CID\_HFLIP

| #define VIDEO\_CID\_HFLIP   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 20) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Flip the image horizontally: the left side becomes the right side.

## [◆ ](#ga588a1206d5046a7b9e8415db725cae81)VIDEO\_CID\_HUE

| #define VIDEO\_CID\_HUE   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 3) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Hue or color balance.

## [◆ ](#ga9c0df146e6064169a89bd88b10085cec)VIDEO\_CID\_HUE\_AUTO

| #define VIDEO\_CID\_HUE\_AUTO   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 25) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Enables automatic hue control by the device.

Setting [VIDEO\_CID\_HUE](#ga588a1206d5046a7b9e8415db725cae81) while automatic hue control is enabled is undefined. Drivers should ignore such request.

## [◆ ](#ga0329342731999405d1f8d6c89470dff7)VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE

| #define VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE   0x009f0900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga3cc32750dec0096ea873ea13e83d202e)VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE

| #define VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE   0x009e0900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga452858d6adfec3b58db6b26c96638fb2)VIDEO\_CID\_IRIS\_ABSOLUTE

| #define VIDEO\_CID\_IRIS\_ABSOLUTE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 17) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This control sets the camera's aperture to the specified value.

The unit is undefined. Larger values open the iris wider, smaller values close it.

## [◆ ](#ga8d1452dfe9c190f6e28e5e3dd35c52cc)VIDEO\_CID\_IRIS\_RELATIVE

| #define VIDEO\_CID\_IRIS\_RELATIVE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 18) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This write-only control modifies the camera's aperture by the specified amount.

The unit is undefined. Positive values open the iris one step further, negative values close it one step further.

## [◆ ](#ga9281f5a61120a6de015a9bbc75ee8b91)VIDEO\_CID\_JPEG\_CLASS\_BASE

| #define VIDEO\_CID\_JPEG\_CLASS\_BASE   0x009d0900 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#ga883c2a761ea0f00e83c884a5b4b45eee)VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY

| #define VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY   ([VIDEO\_CID\_JPEG\_CLASS\_BASE](#ga9281f5a61120a6de015a9bbc75ee8b91) + 3) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Quality (Q) factor of the JPEG algorithm, also increasing the data size.

## [◆ ](#ga829221ec6ea7348e743173ce5e6bd635)VIDEO\_CID\_LASTP1

| #define VIDEO\_CID\_LASTP1   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 44) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Last base CID + 1.

## [◆ ](#ga2142e2819c445b70d82067a3cfb193c8)VIDEO\_CID\_LINK\_FREQ

| #define VIDEO\_CID\_LINK\_FREQ   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7) + 1) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Link frequency, applicable for the CSI2 based devices.

## [◆ ](#ga3b45437f606b8717dcadc22d56a706da)VIDEO\_CID\_PAN\_ABSOLUTE

| #define VIDEO\_CID\_PAN\_ABSOLUTE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 8) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This control turns the camera horizontally to the specified position.

Positive values move the camera to the right (clockwise when viewed from above), negative values to the left. Drivers should interpret the values as arc seconds, with valid values between -180 \* 3600 and +180 \* 3600 inclusive.

## [◆ ](#ga23ed465d76fc54680d1e22422b66c829)VIDEO\_CID\_PAN\_RELATIVE

| #define VIDEO\_CID\_PAN\_RELATIVE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 4) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This write-only control turns the camera horizontally by the specified amount.

The unit is undefined. A positive value moves the camera to the right (clockwise when viewed from above), a negative value to the left. A value of zero does not cause motion.

## [◆ ](#ga99996bce4091e4223130d9ae5e1024cd)VIDEO\_CID\_PAN\_SPEED

| #define VIDEO\_CID\_PAN\_SPEED   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 32) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This control turns the camera horizontally at the specific speed.

The unit is undefined. A positive value moves the camera to the right (clockwise when viewed from above), a negative value to the left. A value of zero stops the motion if one is in progress and has no effect otherwise.

## [◆ ](#ga6f6eaed7defdbb5f440874c7c6d0a6eb)VIDEO\_CID\_PIXEL\_RATE

| #define VIDEO\_CID\_PIXEL\_RATE   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7) + 2) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Pixel rate (pixels/second) in the device's pixel array.

This control is read-only.

## [◆ ](#ga762a6c2b0fb032b9ebdfeff5ed15c3de)VIDEO\_CID\_POWER\_LINE\_FREQUENCY

| #define VIDEO\_CID\_POWER\_LINE\_FREQUENCY   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 24) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Frequency of the power line to compensate for, avoiding flicker due to artificial lighting.

## [◆ ](#ga05e2fe16eafe259061af62ac31dfaeca)VIDEO\_CID\_PRIVATE\_BASE

| #define VIDEO\_CID\_PRIVATE\_BASE   0x08000000 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## [◆ ](#gab534e6263a6b5caae48543346ba2f7ef)VIDEO\_CID\_RED\_BALANCE

| #define VIDEO\_CID\_RED\_BALANCE   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 14) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Red chroma balance, as a ratio to the green channel.

## [◆ ](#ga200017c2141f5c90ade652224d1d4364)VIDEO\_CID\_SATURATION

| #define VIDEO\_CID\_SATURATION   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 2) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Picture color saturation or chroma gain.

## [◆ ](#gab0509f0d3106bca07658e7cfcb1883cf)VIDEO\_CID\_SHARPNESS

| #define VIDEO\_CID\_SHARPNESS   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 27) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Adjusts the sharpness filters in a camera.

The minimum value disables the filters, higher values give a sharper picture.

## [◆ ](#gad1ce88a5c071eaeb8d5db9dc722a2cd4)VIDEO\_CID\_TEST\_PATTERN

| #define VIDEO\_CID\_TEST\_PATTERN   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](#ga0329342731999405d1f8d6c89470dff7) + 3) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Selection of the type of test pattern to represent.

## [◆ ](#gae474209914926f2bd38c99e020224b9c)VIDEO\_CID\_TILT\_ABSOLUTE

| #define VIDEO\_CID\_TILT\_ABSOLUTE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 9) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This control turns the camera vertically to the specified position.

Positive values move the camera up, negative values down. Drivers should interpret the values as arc seconds, with valid values between -180 \* 3600 and +180 \* 3600 inclusive.

## [◆ ](#ga7c51639505c7b97fb1953ade5fc72534)VIDEO\_CID\_TILT\_RELATIVE

| #define VIDEO\_CID\_TILT\_RELATIVE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 5) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This write-only control turns the camera vertically by the specified amount.

The unit is undefined. A positive value moves the camera up, a negative value down. A value of zero does not cause motion.

## [◆ ](#ga3bfeedcd519191bcf1d684fd983ca9bc)VIDEO\_CID\_TILT\_SPEED

| #define VIDEO\_CID\_TILT\_SPEED   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 33) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This control turns the camera vertically at the specified speed.

The unit is undefined. A positive value moves the camera up, a negative value down. A value of zero stops the motion if one is in progress and has no effect otherwise.

## [◆ ](#ga16651a6825b619399a333ed39e802dfc)VIDEO\_CID\_VFLIP

| #define VIDEO\_CID\_VFLIP   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 21) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Flip the image vertically: the top side becomes the bottom side.

## [◆ ](#ga0670d89542dc532a9c775e8e9c2638b1)VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE

| #define VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE   ([VIDEO\_CID\_BASE](#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 26) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

White balance settings as a color temperature in Kelvin.

A driver should have a minimum range of 2800 (incandescent) to 6500 (daylight).

## [◆ ](#ga9d224bc93e5c23317f9ccf89713a18d6)VIDEO\_CID\_WIDE\_DYNAMIC\_RANGE

| #define VIDEO\_CID\_WIDE\_DYNAMIC\_RANGE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 21) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Enables or disables the camera's wide dynamic range feature.

This feature allows to obtain clear images in situations where intensity of the illumination varies significantly throughout the scene, i.e. there are simultaneously very dark and very bright areas. It is most commonly realized in cameras by combining two subsequent frames with different exposure times.

## [◆ ](#ga1033858d5515c2016a0cc6ac06fd8b91)VIDEO\_CID\_ZOOM\_ABSOLUTE

| #define VIDEO\_CID\_ZOOM\_ABSOLUTE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 13) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Specify the objective lens focal length as an absolute value.

The zoom unit is driver-specific and its value should be a positive integer.

## [◆ ](#ga1a79541da7b7a37d9358fb1a3c42a1b7)VIDEO\_CID\_ZOOM\_CONTINUOUS

| #define VIDEO\_CID\_ZOOM\_CONTINUOUS   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 15) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

Start a continuous zoom movement.

Move the objective lens group at the specified speed until it reaches physical device limits or until an explicit request to stop the movement. A positive value moves the zoom lens group towards the telephoto direction. A value of zero stops the zoom lens group movement. A negative value moves the zoom lens group towards the wide-angle direction. The zoom speed unit is driver-specific.

## [◆ ](#ga40e76f27e97549a779a6581bd210b0f4)VIDEO\_CID\_ZOOM\_RELATIVE

| #define VIDEO\_CID\_ZOOM\_RELATIVE   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 14) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

This write-only control sets the objective lens focal length relatively to the current value.

Positive values move the zoom lens group towards the telephoto direction, negative values towards the wide-angle direction. The zoom unit is driver-specific.

## [◆ ](#ga6fc7bcd4b280b4598ea3a03108881b5c)VIDEO\_CTRL\_FLAG\_NEXT\_CTRL

| #define VIDEO\_CTRL\_FLAG\_NEXT\_CTRL   0x80000000 |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga1fb4e9981b362010439b9419691ac2af)video\_camera\_orientation

| enum [video\_camera\_orientation](#ga1fb4e9981b362010439b9419691ac2af) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

| Enumerator | |
| --- | --- |
| VIDEO\_CAMERA\_ORIENTATION\_FRONT | Camera installed on the user-facing side of a phone/tablet/laptop device. |
| VIDEO\_CAMERA\_ORIENTATION\_BACK | Camera installed on the opposite side of the user. |
| VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL | Camera sensors not directly attached to the device or that can move freely. |

## [◆ ](#ga99f4b6cf21c8baaf510fbcfccb645960)video\_colorfx

| enum [video\_colorfx](#ga99f4b6cf21c8baaf510fbcfccb645960) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

| Enumerator | |
| --- | --- |
| VIDEO\_COLORFX\_NONE |  |
| VIDEO\_COLORFX\_BW |  |
| VIDEO\_COLORFX\_SEPIA |  |
| VIDEO\_COLORFX\_NEGATIVE |  |
| VIDEO\_COLORFX\_EMBOSS |  |
| VIDEO\_COLORFX\_SKETCH |  |
| VIDEO\_COLORFX\_SKY\_BLUE |  |
| VIDEO\_COLORFX\_GRASS\_GREEN |  |
| VIDEO\_COLORFX\_SKIN\_WHITEN |  |
| VIDEO\_COLORFX\_VIVID |  |
| VIDEO\_COLORFX\_AQUA |  |
| VIDEO\_COLORFX\_ART\_FREEZE |  |
| VIDEO\_COLORFX\_SILHOUETTE |  |
| VIDEO\_COLORFX\_SOLARIZATION |  |
| VIDEO\_COLORFX\_ANTIQUE |  |

## [◆ ](#ga167cf84b8f4259e6cdd333748deafaf6)video\_exposure\_type

| enum [video\_exposure\_type](#ga167cf84b8f4259e6cdd333748deafaf6) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

| Enumerator | |
| --- | --- |
| VIDEO\_EXPOSURE\_AUTO |  |
| VIDEO\_EXPOSURE\_MANUAL |  |
| VIDEO\_EXPOSURE\_SHUTTER\_PRIORITY |  |
| VIDEO\_EXPOSURE\_APERTURE\_PRIORITY |  |

## [◆ ](#ga9db809ab56484b4b5b1a047a97e6920a)video\_power\_line\_frequency

| enum [video\_power\_line\_frequency](#ga9db809ab56484b4b5b1a047a97e6920a) |
| --- |

`#include <[zephyr/drivers/video-controls.h](video-controls_8h.md)>`

| Enumerator | |
| --- | --- |
| VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED |  |
| VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ |  |
| VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ |  |
| VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
