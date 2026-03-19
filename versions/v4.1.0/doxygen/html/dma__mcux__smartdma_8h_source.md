---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dma__mcux__smartdma_8h_source.html
original_path: doxygen/html/dma__mcux__smartdma_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_smartdma.h

[Go to the documentation of this file.](dma__mcux__smartdma_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_SMARTDMA\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_SMARTDMA\_H\_

9

[ 20](dma__mcux__smartdma_8h.md#a72c469e163fc727135224893adbf757e)void [dma\_smartdma\_install\_fw](dma__mcux__smartdma_8h.md#a72c469e163fc727135224893adbf757e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*firmware,

21 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

22

23#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_SMARTDMA\_H\_ \*/

[dma\_smartdma\_install\_fw](dma__mcux__smartdma_8h.md#a72c469e163fc727135224893adbf757e)

void dma\_smartdma\_install\_fw(const struct device \*dev, uint8\_t \*firmware, uint32\_t len)

install SMARTDMA firmware

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_smartdma.h](dma__mcux__smartdma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
