---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mcux__snvs__rtc_8h_source.html
original_path: doxygen/html/mcux__snvs__rtc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_snvs\_rtc.h

[Go to the documentation of this file.](mcux__snvs__rtc_8h.md)

1/\*

2 \* Copyright (c) 2021 Basalte bv

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

21#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_MCUX\_SNVS\_H\_

22#define ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_MCUX\_SNVS\_H\_

23

24#include <[zephyr/device.h](device_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 41](mcux__snvs__rtc_8h.md#a9f9c1ee4ccae8d219507778f4bebae6e)int [mcux\_snvs\_rtc\_set](mcux__snvs__rtc_8h.md#a9f9c1ee4ccae8d219507778f4bebae6e)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ticks);

42

43#ifdef \_\_cplusplus

44}

45#endif

46

47#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_MCUX\_SNVS\_H\_ \*/

[device.h](device_8h.md)

[mcux\_snvs\_rtc\_set](mcux__snvs__rtc_8h.md#a9f9c1ee4ccae8d219507778f4bebae6e)

int mcux\_snvs\_rtc\_set(const struct device \*dev, uint32\_t ticks)

Set the current counter value.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [mcux\_snvs\_rtc.h](mcux__snvs__rtc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
