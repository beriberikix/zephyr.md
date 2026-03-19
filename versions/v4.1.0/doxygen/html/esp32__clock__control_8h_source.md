---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32__clock__control_8h_source.html
original_path: doxygen/html/esp32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32\_clock\_control.h

[Go to the documentation of this file.](esp32__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2024 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ESP32\_CLOCK\_CONTROL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ESP32\_CLOCK\_CONTROL\_H\_

9

10#if defined(CONFIG\_SOC\_SERIES\_ESP32)

11#include <[zephyr/dt-bindings/clock/esp32\_clock.h](esp32__clock_8h.md)>

12#elif defined(CONFIG\_SOC\_SERIES\_ESP32S2)

13#include <[zephyr/dt-bindings/clock/esp32s2\_clock.h](esp32s2__clock_8h.md)>

14#elif defined(CONFIG\_SOC\_SERIES\_ESP32S3)

15#include <[zephyr/dt-bindings/clock/esp32s3\_clock.h](esp32s3__clock_8h.md)>

16#elif defined(CONFIG\_SOC\_SERIES\_ESP32C2)

17#include <[zephyr/dt-bindings/clock/esp32c2\_clock.h](esp32c2__clock_8h.md)>

18#elif defined(CONFIG\_SOC\_SERIES\_ESP32C3)

19#include <[zephyr/dt-bindings/clock/esp32c3\_clock.h](esp32c3__clock_8h.md)>

20#elif defined(CONFIG\_SOC\_SERIES\_ESP32C6)

21#include <[zephyr/dt-bindings/clock/esp32c6\_clock.h](esp32c6__clock_8h.md)>

22#endif /\* CONFIG\_SOC\_SERIES\_ESP32xx \*/

23

[ 24](esp32__clock__control_8h.md#ae31484bb65af7e1833b735cdb7b3ee86)#define ESP32\_CLOCK\_CONTROL\_SUBSYS\_CPU 50

[ 25](esp32__clock__control_8h.md#aa57dc322f7c168bcdd1a7d36a9113d04)#define ESP32\_CLOCK\_CONTROL\_SUBSYS\_RTC\_FAST 51

[ 26](esp32__clock__control_8h.md#ac0c86530067504b41c00507cfcaddbdb)#define ESP32\_CLOCK\_CONTROL\_SUBSYS\_RTC\_SLOW 52

27

[ 28](structesp32__cpu__clock__config.md)struct [esp32\_cpu\_clock\_config](structesp32__cpu__clock__config.md) {

[ 29](structesp32__cpu__clock__config.md#a7496bee5adc8d235bd4df9b93d791576) int [clk\_src](structesp32__cpu__clock__config.md#a7496bee5adc8d235bd4df9b93d791576);

[ 30](structesp32__cpu__clock__config.md#a181474dc51b7ddca51bc9b56e7a935e4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cpu\_freq](structesp32__cpu__clock__config.md#a181474dc51b7ddca51bc9b56e7a935e4);

[ 31](structesp32__cpu__clock__config.md#a6b7de043a1282e7ea73a2b81b5f0abfd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xtal\_freq](structesp32__cpu__clock__config.md#a6b7de043a1282e7ea73a2b81b5f0abfd);

32};

33

[ 34](structesp32__rtc__clock__config.md)struct [esp32\_rtc\_clock\_config](structesp32__rtc__clock__config.md) {

[ 35](structesp32__rtc__clock__config.md#a2d4090c4e97f15c4ab04d92905d5119c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtc\_fast\_clock\_src](structesp32__rtc__clock__config.md#a2d4090c4e97f15c4ab04d92905d5119c);

[ 36](structesp32__rtc__clock__config.md#ae04b2762e26a5e8d135c91b6f5d360e9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtc\_slow\_clock\_src](structesp32__rtc__clock__config.md#ae04b2762e26a5e8d135c91b6f5d360e9);

37};

38

[ 39](structesp32__clock__config.md)struct [esp32\_clock\_config](structesp32__clock__config.md) {

[ 40](structesp32__clock__config.md#a5cf7a77ea5b5e4780bde683c2cd10526) struct [esp32\_cpu\_clock\_config](structesp32__cpu__clock__config.md) [cpu](structesp32__clock__config.md#a5cf7a77ea5b5e4780bde683c2cd10526);

[ 41](structesp32__clock__config.md#ad42eba0397b1a988357b83a030298078) struct [esp32\_rtc\_clock\_config](structesp32__rtc__clock__config.md) [rtc](structesp32__clock__config.md#ad42eba0397b1a988357b83a030298078);

42};

43

44#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ESP32\_CLOCK\_CONTROL\_H\_ \*/

[esp32\_clock.h](esp32__clock_8h.md)

[esp32c2\_clock.h](esp32c2__clock_8h.md)

[esp32c3\_clock.h](esp32c3__clock_8h.md)

[esp32c6\_clock.h](esp32c6__clock_8h.md)

[esp32s2\_clock.h](esp32s2__clock_8h.md)

[esp32s3\_clock.h](esp32s3__clock_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[esp32\_clock\_config](structesp32__clock__config.md)

**Definition** esp32\_clock\_control.h:39

[esp32\_clock\_config::cpu](structesp32__clock__config.md#a5cf7a77ea5b5e4780bde683c2cd10526)

struct esp32\_cpu\_clock\_config cpu

**Definition** esp32\_clock\_control.h:40

[esp32\_clock\_config::rtc](structesp32__clock__config.md#ad42eba0397b1a988357b83a030298078)

struct esp32\_rtc\_clock\_config rtc

**Definition** esp32\_clock\_control.h:41

[esp32\_cpu\_clock\_config](structesp32__cpu__clock__config.md)

**Definition** esp32\_clock\_control.h:28

[esp32\_cpu\_clock\_config::cpu\_freq](structesp32__cpu__clock__config.md#a181474dc51b7ddca51bc9b56e7a935e4)

uint32\_t cpu\_freq

**Definition** esp32\_clock\_control.h:30

[esp32\_cpu\_clock\_config::xtal\_freq](structesp32__cpu__clock__config.md#a6b7de043a1282e7ea73a2b81b5f0abfd)

uint32\_t xtal\_freq

**Definition** esp32\_clock\_control.h:31

[esp32\_cpu\_clock\_config::clk\_src](structesp32__cpu__clock__config.md#a7496bee5adc8d235bd4df9b93d791576)

int clk\_src

**Definition** esp32\_clock\_control.h:29

[esp32\_rtc\_clock\_config](structesp32__rtc__clock__config.md)

**Definition** esp32\_clock\_control.h:34

[esp32\_rtc\_clock\_config::rtc\_fast\_clock\_src](structesp32__rtc__clock__config.md#a2d4090c4e97f15c4ab04d92905d5119c)

uint32\_t rtc\_fast\_clock\_src

**Definition** esp32\_clock\_control.h:35

[esp32\_rtc\_clock\_config::rtc\_slow\_clock\_src](structesp32__rtc__clock__config.md#ae04b2762e26a5e8d135c91b6f5d360e9)

uint32\_t rtc\_slow\_clock\_src

**Definition** esp32\_clock\_control.h:36

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [esp32\_clock\_control.h](esp32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
