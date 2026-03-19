---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mmc_8h_source.html
original_path: doxygen/html/mmc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mmc.h

[Go to the documentation of this file.](mmc_8h.md)

1/\*

2 \* Copyright 2022 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_SD\_MMC\_H\_

13#define ZEPHYR\_INCLUDE\_SD\_MMC\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/drivers/sdhc.h](sdhc_8h.md)>

17#include <[zephyr/sd/sd.h](sd_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 37](mmc_8h.md#acc996d4fba8673401816a7b41707b96f)int [mmc\_write\_blocks](mmc_8h.md#acc996d4fba8673401816a7b41707b96f)(struct [sd\_card](structsd__card.md) \*card, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*wbuf,

38 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_block, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks);

39

[ 54](mmc_8h.md#aa890ebd312875906583d56ddb1a03560)int [mmc\_read\_blocks](mmc_8h.md#aa890ebd312875906583d56ddb1a03560)(struct [sd\_card](structsd__card.md) \*card, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rbuf,

55 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_block, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks);

56

[ 70](mmc_8h.md#a2dd835a0e88299400cd1b4e1533a7b4b)int [mmc\_ioctl](mmc_8h.md#a2dd835a0e88299400cd1b4e1533a7b4b)(struct [sd\_card](structsd__card.md) \*card, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buf);

71

72#ifdef \_\_cplusplus

73}

74#endif

75

76#endif /\* ZEPHYR\_INCLUDE\_SD\_MMC\_H\_ \*/

[device.h](device_8h.md)

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[mmc\_ioctl](mmc_8h.md#a2dd835a0e88299400cd1b4e1533a7b4b)

int mmc\_ioctl(struct sd\_card \*card, uint8\_t cmd, void \*buf)

Get I/O control data from MMC card.

[mmc\_read\_blocks](mmc_8h.md#aa890ebd312875906583d56ddb1a03560)

int mmc\_read\_blocks(struct sd\_card \*card, uint8\_t \*rbuf, uint32\_t start\_block, uint32\_t num\_blocks)

Read block from MMC card to buffer.

[mmc\_write\_blocks](mmc_8h.md#acc996d4fba8673401816a7b41707b96f)

int mmc\_write\_blocks(struct sd\_card \*card, const uint8\_t \*wbuf, uint32\_t start\_block, uint32\_t num\_blocks)

Write blocks to MMC card from buffer.

[sd.h](sd_8h.md)

Public API for SD subsystem.

[sdhc.h](sdhc_8h.md)

SD Host Controller public API header file.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sd\_card](structsd__card.md)

SD card structure.

**Definition** sd.h:63

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [mmc.h](mmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
