---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/video-controls_8h.html
original_path: doxygen/html/video-controls_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video-controls.h File Reference

Public APIs for Video.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](video-controls_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [video\_control](structvideo__control.md) |
|  | Video control structure. [More...](structvideo__control.md#details) |
| struct | [video\_ctrl\_range](structvideo__ctrl__range.md) |
| struct | [video\_ctrl\_query](structvideo__ctrl__query.md) |

| Macros | |
| --- | --- |
| Stateful codec controls IDs | |
| #define | [VIDEO\_CID\_CODEC\_CLASS\_BASE](group__video__controls.md#gadf37e306a8d73cec4674422e74ffc85e)   0x00990900 |
| Camera Flash class control IDs | |
| #define | [VIDEO\_CID\_FLASH\_CLASS\_BASE](group__video__controls.md#ga9e0c8dc67fab1a80f81cd4be2e875954)   0x009c0900 |
| JPEG class control IDs | |
| #define | [VIDEO\_CID\_JPEG\_CLASS\_BASE](group__video__controls.md#ga9281f5a61120a6de015a9bbc75ee8b91)   0x009d0900 |
| #define | [VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY](group__video__controls.md#ga883c2a761ea0f00e83c884a5b4b45eee)   ([VIDEO\_CID\_JPEG\_CLASS\_BASE](group__video__controls.md#ga9281f5a61120a6de015a9bbc75ee8b91) + 3) |
|  | Quality (Q) factor of the JPEG algorithm, also increasing the data size. |
| Image Source class control IDs | |
| #define | [VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE](group__video__controls.md#ga3cc32750dec0096ea873ea13e83d202e)   0x009e0900 |
| #define | [VIDEO\_CID\_ANALOGUE\_GAIN](group__video__controls.md#ga41b451aace98fb81633983a413d2724f)   ([VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE](group__video__controls.md#ga3cc32750dec0096ea873ea13e83d202e) + 3) |
|  | Analogue gain control. |
| Image Processing class control IDs | |
| #define | [VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7)   0x009f0900 |
| #define | [VIDEO\_CID\_LINK\_FREQ](group__video__controls.md#ga2142e2819c445b70d82067a3cfb193c8)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7) + 1) |
|  | Link frequency, applicable for the CSI2 based devices. |
| #define | [VIDEO\_CID\_PIXEL\_RATE](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7) + 2) |
|  | Pixel rate (pixels/second) in the device's pixel array. |
| #define | [VIDEO\_CID\_TEST\_PATTERN](group__video__controls.md#gad1ce88a5c071eaeb8d5db9dc722a2cd4)   ([VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7) + 3) |
|  | Selection of the type of test pattern to represent. |
| Vendor-specific class control IDs | |
| #define | [VIDEO\_CID\_PRIVATE\_BASE](group__video__controls.md#ga05e2fe16eafe259061af62ac31dfaeca)   0x08000000 |
| Query flags, to be ORed with the control ID | |
| #define | [VIDEO\_CTRL\_FLAG\_NEXT\_CTRL](group__video__controls.md#ga6fc7bcd4b280b4598ea3a03108881b5c)   0x80000000 |

| Base class control IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)   0x00980900 |
| #define | [VIDEO\_CID\_BRIGHTNESS](group__video__controls.md#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 0) |
|  | Picture brightness, or more precisely, the black level. |
| #define | [VIDEO\_CID\_CONTRAST](group__video__controls.md#ga9ca85f6b1d9add05eacb008dc4ccb2e4)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 1) |
|  | Picture contrast or luma gain. |
| #define | [VIDEO\_CID\_SATURATION](group__video__controls.md#ga200017c2141f5c90ade652224d1d4364)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 2) |
|  | Picture color saturation or chroma gain. |
| #define | [VIDEO\_CID\_HUE](group__video__controls.md#ga588a1206d5046a7b9e8415db725cae81)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 3) |
|  | Hue or color balance. |
| #define | [VIDEO\_CID\_AUTO\_WHITE\_BALANCE](group__video__controls.md#ga7e2ce049ed534e1c29ac47d33013e180)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 12) |
|  | Automatic white balance (cameras). |
| #define | [VIDEO\_CID\_RED\_BALANCE](group__video__controls.md#gab534e6263a6b5caae48543346ba2f7ef)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 14) |
|  | Red chroma balance, as a ratio to the green channel. |
| #define | [VIDEO\_CID\_BLUE\_BALANCE](group__video__controls.md#gaf4d38f5eed6feb9ef9509c1747a332b8)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 15) |
|  | Blue chroma balance, as a ratio to the green channel. |
| #define | [VIDEO\_CID\_GAMMA](group__video__controls.md#ga4e38bb3fcb80b2d28fa88186b65e4fea)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 16) |
|  | Gamma adjust. |
| #define | [VIDEO\_CID\_EXPOSURE](group__video__controls.md#ga24e259a6466537377b7bb8a151311ae1)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 17) |
|  | Image sensor exposure time. |
| #define | [VIDEO\_CID\_AUTOGAIN](group__video__controls.md#gac1c1d3580b7ff84b6a461cea0b3942e8)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 18) |
|  | Automatic gain control. |
| #define | [VIDEO\_CID\_GAIN](group__video__controls.md#ga36259be44d9d08b149fd35dd28bbaf50)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 19) |
|  | Gain control. |
| #define | [VIDEO\_CID\_HFLIP](group__video__controls.md#ga59aa47b6f558ef5ae64a67f4a7ac7e31)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 20) |
|  | Flip the image horizontally: the left side becomes the right side. |
| #define | [VIDEO\_CID\_VFLIP](group__video__controls.md#ga16651a6825b619399a333ed39e802dfc)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 21) |
|  | Flip the image vertically: the top side becomes the bottom side. |
| #define | [VIDEO\_CID\_POWER\_LINE\_FREQUENCY](group__video__controls.md#ga762a6c2b0fb032b9ebdfeff5ed15c3de)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 24) |
|  | Frequency of the power line to compensate for, avoiding flicker due to artificial lighting. |
| #define | [VIDEO\_CID\_HUE\_AUTO](group__video__controls.md#ga9c0df146e6064169a89bd88b10085cec)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 25) |
|  | Enables automatic hue control by the device. |
| #define | [VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE](group__video__controls.md#ga0670d89542dc532a9c775e8e9c2638b1)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 26) |
|  | White balance settings as a color temperature in Kelvin. |
| #define | [VIDEO\_CID\_SHARPNESS](group__video__controls.md#gab0509f0d3106bca07658e7cfcb1883cf)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 27) |
|  | Adjusts the sharpness filters in a camera. |
| #define | [VIDEO\_CID\_BACKLIGHT\_COMPENSATION](group__video__controls.md#ga2f22b11b526154e66440eca74ec5bd66)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 28) |
|  | Adjusts the backlight compensation in a camera. |
| #define | [VIDEO\_CID\_COLORFX](group__video__controls.md#ga3fe7778ddb5c3f945b7649379a13321e)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 31) |
|  | Selects a color effect. |
| #define | [VIDEO\_CID\_AUTOBRIGHTNESS](group__video__controls.md#ga46bb41b012b1a2240270817b9ce57637)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 32) |
| #define | [VIDEO\_CID\_BAND\_STOP\_FILTER](group__video__controls.md#ga5d2c02644e26f6a7f9887d5879231106)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 33) |
|  | Switch the band-stop filter of a camera sensor on or off, or specify its strength. |
| #define | [VIDEO\_CID\_ALPHA\_COMPONENT](group__video__controls.md#ga78dcca8b4c8b29f23e983974b861f157)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 41) |
|  | Sets the alpha color component. |
| #define | [VIDEO\_CID\_LASTP1](group__video__controls.md#ga829221ec6ea7348e743173ce5e6bd635)   ([VIDEO\_CID\_BASE](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319) + 44) |
|  | Last base CID + 1. |
| enum | [video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a) { [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) = 0 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) = 1 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) = 2 , [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) = 3 } |
| enum | [video\_colorfx](group__video__controls.md#ga99f4b6cf21c8baaf510fbcfccb645960) {     [VIDEO\_COLORFX\_NONE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a9960e8b54cf9070c04664246e67f3237) = 0 , [VIDEO\_COLORFX\_BW](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a52f62a92f6f0e158b1797719efb79735) = 1 , [VIDEO\_COLORFX\_SEPIA](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a483faa51fb4728b89c1a8da60b139a37) = 2 , [VIDEO\_COLORFX\_NEGATIVE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960ac9367e073eef47865d90ba9ae6eb98a0) = 3 ,     [VIDEO\_COLORFX\_EMBOSS](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960aae3d42f32c4f14e371343a32e8132cc0) = 4 , [VIDEO\_COLORFX\_SKETCH](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a789155f47a0302661a71155c1e6045fc) = 5 , [VIDEO\_COLORFX\_SKY\_BLUE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a09b5346a7431c2c0e7415037ee5a6f8b) = 6 , [VIDEO\_COLORFX\_GRASS\_GREEN](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960abd0ddf263af2224bebe12da19711c6a1) = 7 ,     [VIDEO\_COLORFX\_SKIN\_WHITEN](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a3d4856179a0279a23f1597c3c0a615ef) = 8 , [VIDEO\_COLORFX\_VIVID](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a5e77aa2b5530062aaaf1156a340e3826) = 9 , [VIDEO\_COLORFX\_AQUA](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960adb9e16ef9511c8eec1d6dbead4843a4c) = 10 , [VIDEO\_COLORFX\_ART\_FREEZE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a00faf2d7d366f0109d64568839416ccd) = 11 ,     [VIDEO\_COLORFX\_SILHOUETTE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a1c93819be559612ccea3a2781cbb7d25) = 12 , [VIDEO\_COLORFX\_SOLARIZATION](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a2f6f282e1e195bdc29aa6a351c2bc715) = 13 , [VIDEO\_COLORFX\_ANTIQUE](group__video__controls.md#gga99f4b6cf21c8baaf510fbcfccb645960a71acc838d9197b671accab7763c5388b) = 14   } |

| Camera class controls IDs | |
| --- | --- |
| #define | [VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26)   0x009a0900 |
| #define | [VIDEO\_CID\_EXPOSURE\_AUTO](group__video__controls.md#gab83ae3ca7fa3da66243431d489be37bd)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 1) |
|  | Enables automatic adjustments of the exposure time and/or iris aperture. |
| #define | [VIDEO\_CID\_EXPOSURE\_ABSOLUTE](group__video__controls.md#ga036f78623bcae18ea9627d45d1209245)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 2) |
|  | Determines the exposure time of the camera sensor. |
| #define | [VIDEO\_CID\_EXPOSURE\_AUTO\_PRIORITY](group__video__controls.md#gaa5f2ebd1e1aef2da68be4742941c1f50)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 3) |
|  | Whether the device may dynamically vary the frame rate under the effect of auto-exposure Applicable when [VIDEO\_CID\_EXPOSURE\_AUTO](group__video__controls.md#gab83ae3ca7fa3da66243431d489be37bd "VIDEO_CID_EXPOSURE_AUTO") is set to [VIDEO\_EXPOSURE\_AUTO](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b "VIDEO_EXPOSURE_AUTO") or [VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd "VIDEO_EXPOSURE_APERTURE_PRIORITY"). |
| #define | [VIDEO\_CID\_PAN\_RELATIVE](group__video__controls.md#ga23ed465d76fc54680d1e22422b66c829)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 4) |
|  | This write-only control turns the camera horizontally by the specified amount. |
| #define | [VIDEO\_CID\_TILT\_RELATIVE](group__video__controls.md#ga7c51639505c7b97fb1953ade5fc72534)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 5) |
|  | This write-only control turns the camera vertically by the specified amount. |
| #define | [VIDEO\_CID\_PAN\_ABSOLUTE](group__video__controls.md#ga3b45437f606b8717dcadc22d56a706da)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 8) |
|  | This control turns the camera horizontally to the specified position. |
| #define | [VIDEO\_CID\_TILT\_ABSOLUTE](group__video__controls.md#gae474209914926f2bd38c99e020224b9c)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 9) |
|  | This control turns the camera vertically to the specified position. |
| #define | [VIDEO\_CID\_FOCUS\_ABSOLUTE](group__video__controls.md#ga9ce95d3c135a9221a8d0431d9df9836b)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 10) |
|  | This control sets the focal point of the camera to the specified position. |
| #define | [VIDEO\_CID\_FOCUS\_RELATIVE](group__video__controls.md#ga4137146c348efdcc8088f6be1274b164)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 11) |
|  | This write-only control moves the focal point of the camera by the specified amount. |
| #define | [VIDEO\_CID\_FOCUS\_AUTO](group__video__controls.md#ga031525e88a6c0f915903f5c9068589f4)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 12) |
|  | Enables continuous automatic focus adjustments. |
| #define | [VIDEO\_CID\_ZOOM\_ABSOLUTE](group__video__controls.md#ga1033858d5515c2016a0cc6ac06fd8b91)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 13) |
|  | Specify the objective lens focal length as an absolute value. |
| #define | [VIDEO\_CID\_ZOOM\_RELATIVE](group__video__controls.md#ga40e76f27e97549a779a6581bd210b0f4)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 14) |
|  | This write-only control sets the objective lens focal length relatively to the current value. |
| #define | [VIDEO\_CID\_ZOOM\_CONTINUOUS](group__video__controls.md#ga1a79541da7b7a37d9358fb1a3c42a1b7)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 15) |
|  | Start a continuous zoom movement. |
| #define | [VIDEO\_CID\_IRIS\_ABSOLUTE](group__video__controls.md#ga452858d6adfec3b58db6b26c96638fb2)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 17) |
|  | This control sets the camera's aperture to the specified value. |
| #define | [VIDEO\_CID\_IRIS\_RELATIVE](group__video__controls.md#ga8d1452dfe9c190f6e28e5e3dd35c52cc)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 18) |
|  | This write-only control modifies the camera's aperture by the specified amount. |
| #define | [VIDEO\_CID\_WIDE\_DYNAMIC\_RANGE](group__video__controls.md#ga9d224bc93e5c23317f9ccf89713a18d6)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 21) |
|  | Enables or disables the camera's wide dynamic range feature. |
| #define | [VIDEO\_CID\_PAN\_SPEED](group__video__controls.md#ga99996bce4091e4223130d9ae5e1024cd)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 32) |
|  | This control turns the camera horizontally at the specific speed. |
| #define | [VIDEO\_CID\_TILT\_SPEED](group__video__controls.md#ga3bfeedcd519191bcf1d684fd983ca9bc)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 33) |
|  | This control turns the camera vertically at the specified speed. |
| #define | [VIDEO\_CID\_CAMERA\_ORIENTATION](group__video__controls.md#ga57e5c3f562683a2b7ea1f96a58f633be)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 34) |
|  | This read-only control describes the camera position on the device It by reports where the camera camera is installed, its mounting position on the device. |
| #define | [VIDEO\_CID\_CAMERA\_SENSOR\_ROTATION](group__video__controls.md#ga0d48a910e8d6797842dc25b33fc3f187)   ([VIDEO\_CID\_CAMERA\_CLASS\_BASE](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26) + 35) |
|  | This read-only control describes the orientation of the sensor in the device. |
| enum | [video\_exposure\_type](group__video__controls.md#ga167cf84b8f4259e6cdd333748deafaf6) { [VIDEO\_EXPOSURE\_AUTO](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ab77bff3e8a2abd1c823dbb4324e8499b) = 0 , [VIDEO\_EXPOSURE\_MANUAL](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a66ab6044a5961bc14e1ab718d1a91224) = 1 , [VIDEO\_EXPOSURE\_SHUTTER\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6ac92a826dee7a328bb0b43857d6c09c61) = 2 , [VIDEO\_EXPOSURE\_APERTURE\_PRIORITY](group__video__controls.md#gga167cf84b8f4259e6cdd333748deafaf6a8abeb9fbd3156edf9f3057692829cbcd) = 3 } |
| enum | [video\_camera\_orientation](group__video__controls.md#ga1fb4e9981b362010439b9419691ac2af) { [VIDEO\_CAMERA\_ORIENTATION\_FRONT](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa76b044aa6d822af9844632761fefbaef) = 0 , [VIDEO\_CAMERA\_ORIENTATION\_BACK](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afa831cc750dfcb43f74eb3a7ee59b33072) = 1 , [VIDEO\_CAMERA\_ORIENTATION\_EXTERNAL](group__video__controls.md#gga1fb4e9981b362010439b9419691ac2afafcc44933e74389bef0e1f20b7998f594) = 2 } |

## Detailed Description

Public APIs for Video.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
