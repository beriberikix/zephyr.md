---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/i3c__npcx_8h_source.html
original_path: doxygen/html/i3c__npcx_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_npcx.h

[Go to the documentation of this file.](i3c__npcx_8h.md)

1/\*

2 \* Copyright (c) 2020 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_I3C\_I3C\_NPCX\_H\_

8#define ZEPHYR\_DRIVERS\_I3C\_I3C\_NPCX\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16#ifdef CONFIG\_I3C\_NPCX\_DMA

17

27void npcx\_i3c\_target\_set\_mdma\_buff(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mdma\_rd\_buf,

28 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mdma\_rd\_buf\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mdma\_wr\_buf,

29 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mdma\_wr\_buf\_size);

30

38[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) npcx\_i3c\_target\_get\_mdmafb\_count(const struct [device](structdevice.md) \*dev);

39

47[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) npcx\_i3c\_target\_get\_mdmatb\_count(const struct [device](structdevice.md) \*dev);

48

49#endif

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif /\* ZEPHYR\_DRIVERS\_I3C\_I3C\_NPCX\_H\_ \*/

[device.h](device_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [i3c\_npcx.h](i3c__npcx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
