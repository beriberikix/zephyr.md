---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdma__context.html
original_path: doxygen/html/structdma__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_context Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DMA Interface](group__dma__interface.md)

DMA context structure Note: the [dma\_context](structdma__context.md "DMA context structure Note: the dma_context shall be the first member of DMA client driver Data,...") shall be the first member of DMA client driver Data, got by dev->data.
[More...](#details)

`#include <[dma.h](drivers_2dma_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [magic](#a25355c8cc60df536c9a37cdef52aa653) |
|  | magic code to identify the context |
| int | [dma\_channels](#ac6685cf14ca69c7b77160e5031c0a800) |
|  | number of dma channels |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \* | [atomic](#a5b5776088155c9f19488d479924bec8e) |
|  | atomic holding bit flags for each channel to mark as used/unused |

## Detailed Description

DMA context structure Note: the [dma\_context](structdma__context.md "DMA context structure Note: the dma_context shall be the first member of DMA client driver Data,...") shall be the first member of DMA client driver Data, got by dev->data.

## Field Documentation

## [◆ ](#a5b5776088155c9f19488d479924bec8e)atomic

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)\* dma\_context::atomic |
| --- |

atomic holding bit flags for each channel to mark as used/unused

## [◆ ](#ac6685cf14ca69c7b77160e5031c0a800)dma\_channels

| int dma\_context::dma\_channels |
| --- |

number of dma channels

## [◆ ](#a25355c8cc60df536c9a37cdef52aa653)magic

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dma\_context::magic |
| --- |

magic code to identify the context

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dma.h](drivers_2dma_8h_source.md)

- [dma\_context](structdma__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
