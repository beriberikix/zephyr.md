---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32__dcmipp_8h_source.html
original_path: doxygen/html/stm32__dcmipp_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_dcmipp.h

[Go to the documentation of this file.](stm32__dcmipp_8h.md)

1/\*

2 \* Copyright (c) 2025 STMicroelectronics.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_VIDEO\_STM32\_DCMIPP\_H\_

8#define ZEPHYR\_INCLUDE\_VIDEO\_STM32\_DCMIPP\_H\_

9

10/\* Prototypes of ISP external handler weak functions \*/

[ 11](stm32__dcmipp_8h.md#a74db1fc75808b5d306f56a59539a3cab)void [stm32\_dcmipp\_isp\_vsync\_update](stm32__dcmipp_8h.md#a74db1fc75808b5d306f56a59539a3cab)(DCMIPP\_HandleTypeDef \*hdcmipp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) Pipe);

[ 12](stm32__dcmipp_8h.md#a37286ed8041fa5de1840151a3d8c5a74)int [stm32\_dcmipp\_isp\_init](stm32__dcmipp_8h.md#a37286ed8041fa5de1840151a3d8c5a74)(DCMIPP\_HandleTypeDef \*hdcmipp, const struct [device](structdevice.md) \*source);

[ 13](stm32__dcmipp_8h.md#a3f46ac0646bb14656fcb89a7720d171a)int [stm32\_dcmipp\_isp\_start](stm32__dcmipp_8h.md#a3f46ac0646bb14656fcb89a7720d171a)(void);

[ 14](stm32__dcmipp_8h.md#ac395f951a019d41ec3b72156cd6b5ce5)int [stm32\_dcmipp\_isp\_stop](stm32__dcmipp_8h.md#ac395f951a019d41ec3b72156cd6b5ce5)(void);

15

16#endif /\* ZEPHYR\_INCLUDE\_VIDEO\_STM32\_DCMIPP\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stm32\_dcmipp\_isp\_init](stm32__dcmipp_8h.md#a37286ed8041fa5de1840151a3d8c5a74)

int stm32\_dcmipp\_isp\_init(DCMIPP\_HandleTypeDef \*hdcmipp, const struct device \*source)

[stm32\_dcmipp\_isp\_start](stm32__dcmipp_8h.md#a3f46ac0646bb14656fcb89a7720d171a)

int stm32\_dcmipp\_isp\_start(void)

[stm32\_dcmipp\_isp\_vsync\_update](stm32__dcmipp_8h.md#a74db1fc75808b5d306f56a59539a3cab)

void stm32\_dcmipp\_isp\_vsync\_update(DCMIPP\_HandleTypeDef \*hdcmipp, uint32\_t Pipe)

[stm32\_dcmipp\_isp\_stop](stm32__dcmipp_8h.md#ac395f951a019d41ec3b72156cd6b5ce5)

int stm32\_dcmipp\_isp\_stop(void)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video](dir_70eea7c53f39b9e28dfa8fbbe17c6ab3.md)
- [stm32\_dcmipp.h](stm32__dcmipp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
