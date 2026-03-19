---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsdhc__host__props.html
original_path: doxygen/html/structsdhc__host__props.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdhc\_host\_props Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SDHC interface](group__sdhc__interface.md)

SD host controller properties.
[More...](#details)

`#include <[sdhc.h](sdhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [f\_max](#aef7123dfa5690bc0525aa40dc623307c) |
|  | Max bus frequency. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [f\_min](#a28c69ba3fdae1393daa551f3f9b91057) |
|  | Min bus frequency. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [power\_delay](#a7f7b22b7b8fb46df0ec19e2bef2a4702) |
|  | Delay to allow SD to power up or down (in ms). |
| struct [sdhc\_host\_caps](structsdhc__host__caps.md) | [host\_caps](#ad60bf89e594a031f6be015888466a113) |
|  | Host capability bitfield. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_current\_330](#afebe4aad820c1672635fd30aacec20e4) |
|  | Max current (in mA) at 3.3V. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_current\_300](#ac247312c9b10768fe878afc5c85d9eba) |
|  | Max current (in mA) at 3.0V. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_current\_180](#a43d2b80ec0a5682783e4297c734a3c88) |
|  | Max current (in mA) at 1.8V. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_spi](#abb18e33d99ed1e4a4400dccd2149816f) |
|  | Is the host using SPI mode. |

## Detailed Description

SD host controller properties.

Populated by the host controller using [sdhc\_get\_host\_props](group__sdhc__interface.md#gab55cf88ae79e5aa9e2110b298048df8e "sdhc_get_host_props") api.

## Field Documentation

## [◆ ](#aef7123dfa5690bc0525aa40dc623307c)f\_max

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_props::f\_max |
| --- |

Max bus frequency.

## [◆ ](#a28c69ba3fdae1393daa551f3f9b91057)f\_min

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_props::f\_min |
| --- |

Min bus frequency.

## [◆ ](#ad60bf89e594a031f6be015888466a113)host\_caps

| struct [sdhc\_host\_caps](structsdhc__host__caps.md) sdhc\_host\_props::host\_caps |
| --- |

Host capability bitfield.

## [◆ ](#abb18e33d99ed1e4a4400dccd2149816f)is\_spi

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sdhc\_host\_props::is\_spi |
| --- |

Is the host using SPI mode.

## [◆ ](#a43d2b80ec0a5682783e4297c734a3c88)max\_current\_180

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_host\_props::max\_current\_180 |
| --- |

Max current (in mA) at 1.8V.

## [◆ ](#ac247312c9b10768fe878afc5c85d9eba)max\_current\_300

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_host\_props::max\_current\_300 |
| --- |

Max current (in mA) at 3.0V.

## [◆ ](#afebe4aad820c1672635fd30aacec20e4)max\_current\_330

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sdhc\_host\_props::max\_current\_330 |
| --- |

Max current (in mA) at 3.3V.

## [◆ ](#a7f7b22b7b8fb46df0ec19e2bef2a4702)power\_delay

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sdhc\_host\_props::power\_delay |
| --- |

Delay to allow SD to power up or down (in ms).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sdhc.h](sdhc_8h_source.md)

- [sdhc\_host\_props](structsdhc__host__props.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
