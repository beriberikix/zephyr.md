---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sgp40_8h_source.html
original_path: doxygen/html/sgp40_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sgp40.h

[Go to the documentation of this file.](sgp40_8h.md)

1/\*

2 \* Copyright (c) 2021, Leonard Pollak

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SGP40\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SGP40\_H\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 22](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9)enum [sensor\_attribute\_sgp40](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9) {

23 /\* Temperature in degC; only the integer part is used \*/

[ 24](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419) [SENSOR\_ATTR\_SGP40\_TEMPERATURE](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

25 /\* Relative Humidity in %; only the integer part is used \*/

[ 26](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3) [SENSOR\_ATTR\_SGP40\_HUMIDITY](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3)

27};

28

29#ifdef \_\_cplusplus

30}

31#endif

32

33#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_SGP40\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[sensor\_attribute\_sgp40](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9)

sensor\_attribute\_sgp40

**Definition** sgp40.h:22

[SENSOR\_ATTR\_SGP40\_TEMPERATURE](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419)

@ SENSOR\_ATTR\_SGP40\_TEMPERATURE

**Definition** sgp40.h:24

[SENSOR\_ATTR\_SGP40\_HUMIDITY](sgp40_8h.md#ae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3)

@ SENSOR\_ATTR\_SGP40\_HUMIDITY

**Definition** sgp40.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [sgp40.h](sgp40_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
