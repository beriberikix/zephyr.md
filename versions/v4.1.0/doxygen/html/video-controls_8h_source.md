---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/video-controls_8h_source.html
original_path: doxygen/html/video-controls_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video-controls.h

[Go to the documentation of this file.](video-controls_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited.

3 \* Copyright (c) 2024 tinyVision.ai Inc.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_VIDEO\_CONTROLS\_H\_

8#define ZEPHYR\_INCLUDE\_VIDEO\_CONTROLS\_H\_

9

15

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 40](group__video__controls.md#ga4b56ce06ae4f6ca5b7ac9fd5a7b21319)#define VIDEO\_CID\_BASE 0x00980900

41

[ 43](group__video__controls.md#ga1529eeb7c36bfe53e3916dbd9c6f5b1e)#define VIDEO\_CID\_BRIGHTNESS (VIDEO\_CID\_BASE + 0)

44

[ 46](group__video__controls.md#ga9ca85f6b1d9add05eacb008dc4ccb2e4)#define VIDEO\_CID\_CONTRAST (VIDEO\_CID\_BASE + 1)

47

[ 49](group__video__controls.md#ga200017c2141f5c90ade652224d1d4364)#define VIDEO\_CID\_SATURATION (VIDEO\_CID\_BASE + 2)

50

[ 52](group__video__controls.md#ga588a1206d5046a7b9e8415db725cae81)#define VIDEO\_CID\_HUE (VIDEO\_CID\_BASE + 3)

53

[ 55](group__video__controls.md#ga24e259a6466537377b7bb8a151311ae1)#define VIDEO\_CID\_EXPOSURE (VIDEO\_CID\_BASE + 17)

56

[ 58](group__video__controls.md#ga36259be44d9d08b149fd35dd28bbaf50)#define VIDEO\_CID\_GAIN (VIDEO\_CID\_BASE + 19)

59

[ 61](group__video__controls.md#ga59aa47b6f558ef5ae64a67f4a7ac7e31)#define VIDEO\_CID\_HFLIP (VIDEO\_CID\_BASE + 20)

62

[ 64](group__video__controls.md#ga16651a6825b619399a333ed39e802dfc)#define VIDEO\_CID\_VFLIP (VIDEO\_CID\_BASE + 21)

65

[ 67](group__video__controls.md#ga762a6c2b0fb032b9ebdfeff5ed15c3de)#define VIDEO\_CID\_POWER\_LINE\_FREQUENCY (VIDEO\_CID\_BASE + 24)

[ 68](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a)enum [video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a) {

[ 69](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93) = 0,

[ 70](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10) = 1,

[ 71](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796) = 2,

[ 72](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) [VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0) = 3,

73};

74

[ 76](group__video__controls.md#ga0670d89542dc532a9c775e8e9c2638b1)#define VIDEO\_CID\_WHITE\_BALANCE\_TEMPERATURE (VIDEO\_CID\_BASE + 26)

77

81

[ 86](group__video__controls.md#gadf37e306a8d73cec4674422e74ffc85e)#define VIDEO\_CID\_CODEC\_CLASS\_BASE 0x00990900

87

91

[ 96](group__video__controls.md#ga0a6e2c6287a67e8aa174bb0130fe4c26)#define VIDEO\_CID\_CAMERA\_CLASS\_BASE 0x009a0900

97

[ 99](group__video__controls.md#ga1033858d5515c2016a0cc6ac06fd8b91)#define VIDEO\_CID\_ZOOM\_ABSOLUTE (VIDEO\_CID\_CAMERA\_CLASS\_BASE + 13)

100

104

[ 109](group__video__controls.md#ga9e0c8dc67fab1a80f81cd4be2e875954)#define VIDEO\_CID\_FLASH\_CLASS\_BASE 0x009c0900

110

114

[ 119](group__video__controls.md#ga9281f5a61120a6de015a9bbc75ee8b91)#define VIDEO\_CID\_JPEG\_CLASS\_BASE 0x009d0900

120

[ 122](group__video__controls.md#ga883c2a761ea0f00e83c884a5b4b45eee)#define VIDEO\_CID\_JPEG\_COMPRESSION\_QUALITY (VIDEO\_CID\_JPEG\_CLASS\_BASE + 3)

123

127

[ 132](group__video__controls.md#ga3cc32750dec0096ea873ea13e83d202e)#define VIDEO\_CID\_IMAGE\_SOURCE\_CLASS\_BASE 0x009e0900

133

137

[ 142](group__video__controls.md#ga0329342731999405d1f8d6c89470dff7)#define VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE 0x009f0900

143

[ 145](group__video__controls.md#ga6f6eaed7defdbb5f440874c7c6d0a6eb)#define VIDEO\_CID\_PIXEL\_RATE (VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE + 2)

146

[ 148](group__video__controls.md#gad1ce88a5c071eaeb8d5db9dc722a2cd4)#define VIDEO\_CID\_TEST\_PATTERN (VIDEO\_CID\_IMAGE\_PROC\_CLASS\_BASE + 3)

149

153

[ 158](group__video__controls.md#ga05e2fe16eafe259061af62ac31dfaeca)#define VIDEO\_CID\_PRIVATE\_BASE 0x08000000

159

163

164#ifdef \_\_cplusplus

165}

166#endif

167

171

172#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_H\_ \*/

[video\_power\_line\_frequency](group__video__controls.md#ga9db809ab56484b4b5b1a047a97e6920a)

video\_power\_line\_frequency

**Definition** video-controls.h:68

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa596b3bec6771ef15392bfcee9fc47f93)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_DISABLED

**Definition** video-controls.h:69

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aa817468b493999a2ba979a249bc0cffe0)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_AUTO

**Definition** video-controls.h:72

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad34ec7a0db40ee5b1dbfc6de79834796)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_60HZ

**Definition** video-controls.h:71

[VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ](group__video__controls.md#gga9db809ab56484b4b5b1a047a97e6920aad47b0f6914d0e949d17faa61b9fc2c10)

@ VIDEO\_CID\_POWER\_LINE\_FREQUENCY\_50HZ

**Definition** video-controls.h:70

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video-controls.h](video-controls_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
