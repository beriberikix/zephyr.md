---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dma__mcux__smartdma_8h_source.html
original_path: doxygen/html/dma__mcux__smartdma_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

10/\* Write RGB565 data to MIPI DSI via DMA. \*/

[ 11](dma__mcux__smartdma_8h.md#a2b2585f7729443c19987c81a6a89a353)#define DMA\_SMARTDMA\_MIPI\_RGB565\_DMA 0

12/\* Write RGB888 data to MIPI DSI via DMA \*/

[ 13](dma__mcux__smartdma_8h.md#a62fd85940a8765ed652e490f65ef609e)#define DMA\_SMARTDMA\_MIPI\_RGB888\_DMA 1

14/\* Write RGB565 data to MIPI DSI via DMA. Rotate output data by 180 degrees \*/

[ 15](dma__mcux__smartdma_8h.md#a86dcedc54234c6091b7cab8aa7ab598b)#define DMA\_SMARTDMA\_MIPI\_RGB565\_180 2

16/\* Write RGB888 data to MIPI DSI via DMA. Rotate output data by 180 degrees \*/

[ 17](dma__mcux__smartdma_8h.md#a1f534964f658e9b944637c3fb49c9783)#define DMA\_SMARTDMA\_MIPI\_RGB888\_180 3

18

19/\* Write RGB565 data to MIPI DSI via DMA. Swap data endianness, so that

20 \* little endian RGB565 data will be written big endian style.

21 \*/

[ 22](dma__mcux__smartdma_8h.md#a948bb5d59ec4b5347304006c7335e4bf)#define DMA\_SMARTDMA\_MIPI\_RGB565\_DMA\_SWAP 4

23/\* Write RGB888 data to MIPI DSI via DMA. Swap data endianness, so that

24 \* little endian RGB888 data will be written big endian style.

25 \*/

[ 26](dma__mcux__smartdma_8h.md#a5cd0156a4a3870c576917f152793580b)#define DMA\_SMARTDMA\_MIPI\_RGB888\_DMA\_SWAP 5

27/\* Write RGB565 data to MIPI DSI via DMA. Rotate output data by 180 degrees,

28 \* and swap data endianness

29 \*/

[ 30](dma__mcux__smartdma_8h.md#a1881916a14a35d65bc5684e74aed8b4c)#define DMA\_SMARTDMA\_MIPI\_RGB565\_180\_SWAP 6

31/\* Write RGB888 data to MIPI DSI via DMA. Rotate output data by 180 degrees,

32 \* and swap data endianness

33 \*/

[ 34](dma__mcux__smartdma_8h.md#a31da9953266f56e8aa2ab271cedcef11)#define DMA\_SMARTDMA\_MIPI\_RGB888\_180\_SWAP 7

35

36

37

[ 48](dma__mcux__smartdma_8h.md#a72c469e163fc727135224893adbf757e)void [dma\_smartdma\_install\_fw](dma__mcux__smartdma_8h.md#a72c469e163fc727135224893adbf757e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*firmware,

49 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

50

[ 51](dma__mcux__smartdma_8h.md#af41c61ae669ce510d514ccb9ff6204f9)#define GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD(threshold) (threshold & 0x3)

52

53#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_MCUX\_SMARTDMA\_H\_ \*/

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

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_smartdma.h](dma__mcux__smartdma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
