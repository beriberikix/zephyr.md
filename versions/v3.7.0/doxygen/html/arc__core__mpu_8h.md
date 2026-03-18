---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arc__core__mpu_8h.html
original_path: doxygen/html/arc__core__mpu_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_core\_mpu.h File Reference

[Go to the source code of this file.](arc__core__mpu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [THREAD\_STACK\_USER\_REGION](#a22720cafd5b56a589fdf78e9fde34df5)   0x0 |
| #define | [THREAD\_STACK\_REGION](#aa100568c6cd354bf10d8567342d7c015)   0x1 |
| #define | [THREAD\_APP\_DATA\_REGION](#a6d410aa5ef2d4566c6169b2be511469f)   0x2 |
| #define | [THREAD\_STACK\_GUARD\_REGION](#abfa3cdf9032f9ae166772cc135777857)   0x3 |
| #define | [THREAD\_DOMAIN\_PARTITION\_REGION](#a7ad5bda29d5cd51209673c0b7650c0d0)   0x4 |

| Functions | |
| --- | --- |
| void | [arc\_core\_mpu\_configure\_mem\_domain](#a59ab30984101e12346194700ac788c02) (struct [k\_thread](structk__thread.md) \*thread) |
| void | [arc\_core\_mpu\_remove\_mem\_domain](#a65c60aedd91088211a87668e21710792) (struct [k\_mem\_domain](structk__mem__domain.md) \*mem\_domain) |
| void | [arc\_core\_mpu\_remove\_mem\_partition](#a336c96a063f41feb6e40553da7d24b8d) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) partition\_id) |
| int | [arc\_core\_mpu\_get\_max\_domain\_partition\_regions](#ac5545b4f32734d39d0ea595ec946c798) (void) |
| int | [arc\_core\_mpu\_buffer\_validate](#ac51c1ffa76948c631893ce9a2e61aa55) (const void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int write) |
| void | [configure\_mpu\_thread](#a3f143241fb106da87db9cf78539ff802) (struct [k\_thread](structk__thread.md) \*thread) |

## Macro Definition Documentation

## [◆ ](#a6d410aa5ef2d4566c6169b2be511469f)THREAD\_APP\_DATA\_REGION

| #define THREAD\_APP\_DATA\_REGION   0x2 |
| --- |

## [◆ ](#a7ad5bda29d5cd51209673c0b7650c0d0)THREAD\_DOMAIN\_PARTITION\_REGION

| #define THREAD\_DOMAIN\_PARTITION\_REGION   0x4 |
| --- |

## [◆ ](#abfa3cdf9032f9ae166772cc135777857)THREAD\_STACK\_GUARD\_REGION

| #define THREAD\_STACK\_GUARD\_REGION   0x3 |
| --- |

## [◆ ](#aa100568c6cd354bf10d8567342d7c015)THREAD\_STACK\_REGION

| #define THREAD\_STACK\_REGION   0x1 |
| --- |

## [◆ ](#a22720cafd5b56a589fdf78e9fde34df5)THREAD\_STACK\_USER\_REGION

| #define THREAD\_STACK\_USER\_REGION   0x0 |
| --- |

## Function Documentation

## [◆ ](#ac51c1ffa76948c631893ce9a2e61aa55)arc\_core\_mpu\_buffer\_validate()

| int arc\_core\_mpu\_buffer\_validate | ( | const void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | int | *write* ) |

## [◆ ](#a59ab30984101e12346194700ac788c02)arc\_core\_mpu\_configure\_mem\_domain()

| void arc\_core\_mpu\_configure\_mem\_domain | ( | struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac5545b4f32734d39d0ea595ec946c798)arc\_core\_mpu\_get\_max\_domain\_partition\_regions()

| int arc\_core\_mpu\_get\_max\_domain\_partition\_regions | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a65c60aedd91088211a87668e21710792)arc\_core\_mpu\_remove\_mem\_domain()

| void arc\_core\_mpu\_remove\_mem\_domain | ( | struct [k\_mem\_domain](structk__mem__domain.md) \* | *mem\_domain* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a336c96a063f41feb6e40553da7d24b8d)arc\_core\_mpu\_remove\_mem\_partition()

| void arc\_core\_mpu\_remove\_mem\_partition | ( | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *partition\_id* ) |

## [◆ ](#a3f143241fb106da87db9cf78539ff802)configure\_mpu\_thread()

| void configure\_mpu\_thread | ( | struct [k\_thread](structk__thread.md) \* | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [mpu](dir_c51b2f0fffc5b62554252c09f16a5032.md)
- [arc\_core\_mpu.h](arc__core__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
