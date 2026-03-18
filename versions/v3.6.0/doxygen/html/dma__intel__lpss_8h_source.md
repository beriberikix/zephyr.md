---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__intel__lpss_8h_source.html
original_path: doxygen/html/dma__intel__lpss_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_intel\_lpss.h

[Go to the documentation of this file.](dma__intel__lpss_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_INTEL\_LPSS\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_INTEL\_LPSS\_H\_

9

[ 10](dma__intel__lpss_8h.md#a30a9efb6d3b728e258083d8c9abb617f)#define DMA\_INTEL\_LPSS\_OFFSET 0x800

[ 11](dma__intel__lpss_8h.md#abc9f1a6bfba312cf78ab7800d3b8c589)#define DMA\_INTEL\_LPSS\_REMAP\_LOW 0x240

[ 12](dma__intel__lpss_8h.md#a2fa4dfb43c0fc5223d0e17932d6c97ee)#define DMA\_INTEL\_LPSS\_REMAP\_HI 0x244

[ 13](dma__intel__lpss_8h.md#a1dd74ce0e651a2fad8abf337ac0bf1aa)#define DMA\_INTEL\_LPSS\_TX\_CHAN 0

[ 14](dma__intel__lpss_8h.md#a3797b7de5ebf86a3c722e7667239cb3f)#define DMA\_INTEL\_LPSS\_RX\_CHAN 1

[ 15](dma__intel__lpss_8h.md#a93cbdc5d852735e260d4b767cc591977)#define DMA\_INTEL\_LPSS\_ADDR\_RIGHT\_SHIFT 32

16

[ 17](dma__intel__lpss_8h.md#a769db0413f8ca5fe4c03d1701581edfa)void [dma\_intel\_lpss\_isr](dma__intel__lpss_8h.md#a769db0413f8ca5fe4c03d1701581edfa)(const struct [device](structdevice.md) \*dev);

[ 18](dma__intel__lpss_8h.md#a4a5438ab5a164e80c0564fc73e8b9764)int [dma\_intel\_lpss\_setup](dma__intel__lpss_8h.md#a4a5438ab5a164e80c0564fc73e8b9764)(const struct [device](structdevice.md) \*dev);

[ 19](dma__intel__lpss_8h.md#aaf5eefbe0476083a87e5c2724a99a73d)void [dma\_intel\_lpss\_set\_base](dma__intel__lpss_8h.md#aaf5eefbe0476083a87e5c2724a99a73d)(const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) base);

20

21#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_INTEL\_LPSS\_H\_ \*/

[dma\_intel\_lpss\_setup](dma__intel__lpss_8h.md#a4a5438ab5a164e80c0564fc73e8b9764)

int dma\_intel\_lpss\_setup(const struct device \*dev)

[dma\_intel\_lpss\_isr](dma__intel__lpss_8h.md#a769db0413f8ca5fe4c03d1701581edfa)

void dma\_intel\_lpss\_isr(const struct device \*dev)

[dma\_intel\_lpss\_set\_base](dma__intel__lpss_8h.md#aaf5eefbe0476083a87e5c2724a99a73d)

void dma\_intel\_lpss\_set\_base(const struct device \*dev, uintptr\_t base)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_intel\_lpss.h](dma__intel__lpss_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
