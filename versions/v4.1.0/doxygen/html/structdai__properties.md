---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdai__properties.html
original_path: doxygen/html/structdai__properties.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dai\_properties Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DAI Interface](group__dai__interface.md)

DAI properties.
[More...](#details)

`#include <[dai.h](dai_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fifo\_address](#a98053c85634b80b144bda05d83f2eb7e) |
|  | Fifo hw address for e.g. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fifo\_depth](#a9b056f0ff59b473d3040851642d1601c) |
|  | Fifo depth. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dma\_hs\_id](#a7203f5c97aaf8f48f9eb51d88424afce) |
|  | DMA handshake id. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [reg\_init\_delay](#a8fc2d359fe889b3a46ecc8918a82f680) |
|  | Delay for initializing registers. |
| int | [stream\_id](#adab0f1199c7169a521329adc98c2f0ac) |
|  | Stream ID. |

## Detailed Description

DAI properties.

This struct is used with APIs get\_properties function to query DAI properties like fifo address and dma handshake. These are needed for example to setup dma outside the driver code.

## Field Documentation

## [◆ ](#a7203f5c97aaf8f48f9eb51d88424afce)dma\_hs\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_properties::dma\_hs\_id |
| --- |

DMA handshake id.

## [◆ ](#a98053c85634b80b144bda05d83f2eb7e)fifo\_address

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_properties::fifo\_address |
| --- |

Fifo hw address for e.g.

when connecting to dma.

## [◆ ](#a9b056f0ff59b473d3040851642d1601c)fifo\_depth

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_properties::fifo\_depth |
| --- |

Fifo depth.

## [◆ ](#a8fc2d359fe889b3a46ecc8918a82f680)reg\_init\_delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_properties::reg\_init\_delay |
| --- |

Delay for initializing registers.

## [◆ ](#adab0f1199c7169a521329adc98c2f0ac)stream\_id

| int dai\_properties::stream\_id |
| --- |

Stream ID.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dai.h](dai_8h_source.md)

- [dai\_properties](structdai__properties.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
