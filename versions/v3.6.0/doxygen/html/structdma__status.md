---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdma__status.html
original_path: doxygen/html/structdma__status.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_status Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DMA Interface](group__dma__interface.md)

DMA runtime status structure.
[More...](#details)

`#include <[dma.h](drivers_2dma_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [busy](#a92ec05d9207caa828064661897f2f31c) |
|  | Is the current DMA transfer busy or idle. |
| enum [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) | [dir](#aacfe94ad8e60ea77bca2423bd9bf8409) |
|  | Direction fo the transfer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pending\_length](#a3a33f92b1d100f988fca2bea0a6deb24) |
|  | Pending length to be transferred in bytes, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [free](#a2b481bf13de03e49146eb6a26563776e) |
|  | Available buffers space, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [write\_position](#aa7288b85f41098e59ad4f96dcea4ccde) |
|  | Write position in circular DMA buffer, HW specific. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_position](#afa401acfb26cd26b73e4a52066989847) |
|  | Read position in circular DMA buffer, HW specific. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [total\_copied](#a9f743c98e6343d55eccc27e528b79b1a) |
|  | Total copied, HW specific. |

## Detailed Description

DMA runtime status structure.

## Field Documentation

## [◆ ](#a92ec05d9207caa828064661897f2f31c)busy

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dma\_status::busy |
| --- |

Is the current DMA transfer busy or idle.

## [◆ ](#aacfe94ad8e60ea77bca2423bd9bf8409)dir

| enum [dma\_channel\_direction](group__dma__interface.md#gae442d8ba73be7e53b68165647b0ea402) dma\_status::dir |
| --- |

Direction fo the transfer.

## [◆ ](#a2b481bf13de03e49146eb6a26563776e)free

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_status::free |
| --- |

Available buffers space, HW specific.

## [◆ ](#a3a33f92b1d100f988fca2bea0a6deb24)pending\_length

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_status::pending\_length |
| --- |

Pending length to be transferred in bytes, HW specific.

## [◆ ](#afa401acfb26cd26b73e4a52066989847)read\_position

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_status::read\_position |
| --- |

Read position in circular DMA buffer, HW specific.

## [◆ ](#a9f743c98e6343d55eccc27e528b79b1a)total\_copied

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) dma\_status::total\_copied |
| --- |

Total copied, HW specific.

## [◆ ](#aa7288b85f41098e59ad4f96dcea4ccde)write\_position

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dma\_status::write\_position |
| --- |

Write position in circular DMA buffer, HW specific.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dma.h](drivers_2dma_8h_source.md)

- [dma\_status](structdma__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
