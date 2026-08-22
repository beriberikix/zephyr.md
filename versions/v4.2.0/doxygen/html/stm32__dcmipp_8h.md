---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32__dcmipp_8h.html
original_path: doxygen/html/stm32__dcmipp_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_dcmipp.h File Reference

[Go to the source code of this file.](stm32__dcmipp_8h_source.md)

| Functions | |
| --- | --- |
| void | [stm32\_dcmipp\_isp\_vsync\_update](#a74db1fc75808b5d306f56a59539a3cab) (DCMIPP\_HandleTypeDef \*hdcmipp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) Pipe) |
| int | [stm32\_dcmipp\_isp\_init](#a37286ed8041fa5de1840151a3d8c5a74) (DCMIPP\_HandleTypeDef \*hdcmipp, const struct [device](structdevice.md) \*source) |
| int | [stm32\_dcmipp\_isp\_start](#a3f46ac0646bb14656fcb89a7720d171a) (void) |
| int | [stm32\_dcmipp\_isp\_stop](#ac395f951a019d41ec3b72156cd6b5ce5) (void) |

## Function Documentation

## [◆ ](#a37286ed8041fa5de1840151a3d8c5a74)stm32\_dcmipp\_isp\_init()

| int stm32\_dcmipp\_isp\_init | ( | DCMIPP\_HandleTypeDef \* | *hdcmipp*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *source* ) |

## [◆ ](#a3f46ac0646bb14656fcb89a7720d171a)stm32\_dcmipp\_isp\_start()

| int stm32\_dcmipp\_isp\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac395f951a019d41ec3b72156cd6b5ce5)stm32\_dcmipp\_isp\_stop()

| int stm32\_dcmipp\_isp\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a74db1fc75808b5d306f56a59539a3cab)stm32\_dcmipp\_isp\_vsync\_update()

| void stm32\_dcmipp\_isp\_vsync\_update | ( | DCMIPP\_HandleTypeDef \* | *hdcmipp*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *Pipe* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [video](dir_70eea7c53f39b9e28dfa8fbbe17c6ab3.md)
- [stm32\_dcmipp.h](stm32__dcmipp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
