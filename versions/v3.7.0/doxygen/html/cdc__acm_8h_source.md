---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cdc__acm_8h_source.html
original_path: doxygen/html/cdc__acm_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_acm.h

[Go to the documentation of this file.](cdc__acm_8h.md)

1/\*

2 \* Copyright (c) 2020 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_CDC\_ACM\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_CDC\_ACM\_H\_

14

15#include <[errno.h](errno_8h.md)>

16

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif /\* \_\_cplusplus \*/

22

[ 31](cdc__acm_8h.md#a0b2e4a171e5d56dba45c3d2e7cef72b4)typedef void (\*[cdc\_dte\_rate\_callback\_t](cdc__acm_8h.md#a0b2e4a171e5d56dba45c3d2e7cef72b4))(const struct [device](structdevice.md) \*dev,

32 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rate);

33

[ 47](cdc__acm_8h.md#a5b71bd70532ed059fb31a1ee3e73eaa5)int [cdc\_acm\_dte\_rate\_callback\_set](cdc__acm_8h.md#a5b71bd70532ed059fb31a1ee3e73eaa5)(const struct [device](structdevice.md) \*dev,

48 [cdc\_dte\_rate\_callback\_t](cdc__acm_8h.md#a0b2e4a171e5d56dba45c3d2e7cef72b4) callback);

49

50#ifdef \_\_cplusplus

51}

52#endif /\* \_\_cplusplus \*/

53

54#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_CDC\_ACM\_H\_ \*/

[cdc\_dte\_rate\_callback\_t](cdc__acm_8h.md#a0b2e4a171e5d56dba45c3d2e7cef72b4)

void(\* cdc\_dte\_rate\_callback\_t)(const struct device \*dev, uint32\_t rate)

A function that is called when the USB host changes the baud rate.

**Definition** cdc\_acm.h:31

[cdc\_acm\_dte\_rate\_callback\_set](cdc__acm_8h.md#a5b71bd70532ed059fb31a1ee3e73eaa5)

int cdc\_acm\_dte\_rate\_callback\_set(const struct device \*dev, cdc\_dte\_rate\_callback\_t callback)

Set the callback for dwDTERate SetLineCoding requests.

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [cdc\_acm.h](cdc__acm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
