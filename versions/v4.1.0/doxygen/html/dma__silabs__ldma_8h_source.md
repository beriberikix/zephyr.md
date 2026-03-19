---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dma__silabs__ldma_8h_source.html
original_path: doxygen/html/dma__silabs__ldma_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_silabs\_ldma.h

[Go to the documentation of this file.](dma__silabs__ldma_8h.md)

1/\*

2 \* Copyright (c) 2025 Silicon Laboratories Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_SILABS\_LDMA\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_SILABS\_LDMA\_H\_

9

10#include <[zephyr/drivers/dma.h](drivers_2dma_8h.md)>

11

[ 12](dma__silabs__ldma_8h.md#a0d4985670c10482d3999d08e4ba1fdc9)#define SILABS\_LDMA\_SOURCE\_MASK GENMASK(21, 16)

[ 13](dma__silabs__ldma_8h.md#a9559b6338f281c62c4cc28a37c6eaa1b)#define SILABS\_LDMA\_SIG\_MASK GENMASK(3, 0)

14

[ 15](dma__silabs__ldma_8h.md#a8b234dbc8be91a1c9ae4b6478a3ba0e9)#define SILABS\_DMA\_SLOT\_SOURCE\_MASK GENMASK(7, 3)

[ 16](dma__silabs__ldma_8h.md#a9ccf7fd9a6101b88a45feaf1170de7d5)#define SILABS\_DMA\_SLOT\_SIG\_MASK GENMASK(2, 0)

17

[ 18](dma__silabs__ldma_8h.md#a46d84aa830d58ab1e63133e3424361fb)#define SILABS\_LDMA\_REQSEL\_TO\_SLOT(signal) \

19 FIELD\_PREP(SILABS\_DMA\_SLOT\_SOURCE\_MASK, FIELD\_GET(SILABS\_LDMA\_SOURCE\_MASK, signal)) | \

20 FIELD\_PREP(SILABS\_DMA\_SLOT\_SIG\_MASK, FIELD\_GET(SILABS\_LDMA\_SIG\_MASK, signal))

21

[ 22](dma__silabs__ldma_8h.md#a8728e84cf05e093c864fe9dc8e9854c4)#define SILABS\_LDMA\_SLOT\_TO\_REQSEL(slot) \

23 FIELD\_PREP(SILABS\_LDMA\_SOURCE\_MASK, FIELD\_GET(SILABS\_DMA\_SLOT\_SOURCE\_MASK, slot)) | \

24 FIELD\_PREP(SILABS\_LDMA\_SIG\_MASK, FIELD\_GET(SILABS\_DMA\_SLOT\_SIG\_MASK, slot))

25

[ 43](dma__silabs__ldma_8h.md#a5f6501ec9e73cb8a3be76c418ebf1456)int [silabs\_ldma\_append\_block](dma__silabs__ldma_8h.md#a5f6501ec9e73cb8a3be76c418ebf1456)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel,

44 struct [dma\_config](structdma__config.md) \*config);

45

46#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_SILABS\_LDMA\_H\_\*/

[silabs\_ldma\_append\_block](dma__silabs__ldma_8h.md#a5f6501ec9e73cb8a3be76c418ebf1456)

int silabs\_ldma\_append\_block(const struct device \*dev, uint32\_t channel, struct dma\_config \*config)

Append a new block to the current channel.

[dma.h](drivers_2dma_8h.md)

Public APIs for the DMA drivers.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[dma\_config](structdma__config.md)

DMA configuration structure.

**Definition** dma.h:197

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_silabs\_ldma.h](dma__silabs__ldma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
