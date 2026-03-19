---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm__clock__control_8h_source.html
original_path: doxygen/html/arm__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_clock\_control.h

[Go to the documentation of this file.](arm__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2016 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ARM\_CLOCK\_CONTROL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ARM\_CLOCK\_CONTROL\_H\_

9

10#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

11

17

18/\* CMSDK BUS Mapping \*/

[ 19](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50ef)enum [arm\_bus\_type\_t](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50ef) {

[ 20](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393) [CMSDK\_AHB](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393) = 0,

[ 21](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80) [CMSDK\_APB](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80),

22};

23

24/\* CPU States \*/

[ 25](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1)enum [arm\_soc\_state\_t](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1) {

[ 26](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf) [SOC\_ACTIVE](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf) = 0,

[ 27](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094) [SOC\_SLEEP](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094),

[ 28](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98) [SOC\_DEEPSLEEP](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98),

29};

30

[ 31](structarm__clock__control__t.md)struct [arm\_clock\_control\_t](structarm__clock__control__t.md) {

32 /\* ARM family SoCs supported Bus types \*/

[ 33](structarm__clock__control__t.md#ab596009f00c33d84af817c860bdb9e40) enum [arm\_bus\_type\_t](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50ef) [bus](structarm__clock__control__t.md#ab596009f00c33d84af817c860bdb9e40);

34 /\* Clock can be configured for 3 states: Active, Sleep, Deep Sleep \*/

[ 35](structarm__clock__control__t.md#a46cd4433f02663f09022a71ae7fe6550) enum [arm\_soc\_state\_t](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1) [state](structarm__clock__control__t.md#a46cd4433f02663f09022a71ae7fe6550);

36 /\* Identifies the device on the bus \*/

[ 37](structarm__clock__control__t.md#ab2946697523620aa1f52ae69c636721e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [device](structarm__clock__control__t.md#ab2946697523620aa1f52ae69c636721e);

38};

39

40#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_ARM\_CLOCK\_CONTROL\_H\_ \*/

[arm\_soc\_state\_t](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1)

arm\_soc\_state\_t

**Definition** arm\_clock\_control.h:25

[SOC\_SLEEP](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094)

@ SOC\_SLEEP

**Definition** arm\_clock\_control.h:27

[SOC\_ACTIVE](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf)

@ SOC\_ACTIVE

**Definition** arm\_clock\_control.h:26

[SOC\_DEEPSLEEP](arm__clock__control_8h.md#a0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98)

@ SOC\_DEEPSLEEP

**Definition** arm\_clock\_control.h:28

[arm\_bus\_type\_t](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50ef)

arm\_bus\_type\_t

**Definition** arm\_clock\_control.h:19

[CMSDK\_APB](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80)

@ CMSDK\_APB

**Definition** arm\_clock\_control.h:21

[CMSDK\_AHB](arm__clock__control_8h.md#af000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393)

@ CMSDK\_AHB

**Definition** arm\_clock\_control.h:20

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[arm\_clock\_control\_t](structarm__clock__control__t.md)

**Definition** arm\_clock\_control.h:31

[arm\_clock\_control\_t::state](structarm__clock__control__t.md#a46cd4433f02663f09022a71ae7fe6550)

enum arm\_soc\_state\_t state

**Definition** arm\_clock\_control.h:35

[arm\_clock\_control\_t::device](structarm__clock__control__t.md#ab2946697523620aa1f52ae69c636721e)

uint32\_t device

**Definition** arm\_clock\_control.h:37

[arm\_clock\_control\_t::bus](structarm__clock__control__t.md#ab596009f00c33d84af817c860bdb9e40)

enum arm\_bus\_type\_t bus

**Definition** arm\_clock\_control.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [arm\_clock\_control.h](arm__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
