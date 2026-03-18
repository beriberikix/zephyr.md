---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mfd_2tle9104_8h_source.html
original_path: doxygen/html/mfd_2tle9104_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tle9104.h

[Go to the documentation of this file.](mfd_2tle9104_8h.md)

1/\*

2 \* Copyright (c) 2024 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_TLE9104\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_TLE9104\_H\_

8

9#include <[stdbool.h](stdbool_8h.md)>

10#include <[zephyr/device.h](device_8h.md)>

11

[ 12](mfd_2tle9104_8h.md#a3f6f8709aa1b46781268154e34c298a9)#define TLE9104\_GPIO\_COUNT 4

13

[ 14](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0)enum [tle9104\_on\_state\_diagnostics](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0) {

15 /\* overtemperature \*/

[ 16](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a359b0a412ecb9de36e12a50946dc2173) [TLE9104\_ONDIAG\_OT](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a359b0a412ecb9de36e12a50946dc2173) = 5,

17 /\* overcurrent timeout \*/

[ 18](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a36e248aad4b5b47c338589d86f4e2925) [TLE9104\_ONDIAG\_OCTIME](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a36e248aad4b5b47c338589d86f4e2925) = 4,

19 /\* overtemperature during overcurrent \*/

[ 20](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a7cea6cba428b062f1951809d12e15685) [TLE9104\_ONDIAG\_OCOT](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a7cea6cba428b062f1951809d12e15685) = 3,

21 /\* short to battery \*/

[ 22](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a9d82a99fcc6ea7017e38959d5e299f4c) [TLE9104\_ONDIAG\_SCB](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a9d82a99fcc6ea7017e38959d5e299f4c) = 2,

23 /\* no failure \*/

[ 24](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a7aace824362e7c51841585b9f3a64ca4) [TLE9104\_ONDIAG\_NOFAIL](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a7aace824362e7c51841585b9f3a64ca4) = 1,

25 /\* no diagnosis done \*/

[ 26](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0addb7f997401544e59dc6a181c1341679) [TLE9104\_ONDIAG\_UNKNOWN](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0addb7f997401544e59dc6a181c1341679) = 0,

27};

28

[ 29](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3)enum [tle9104\_off\_state\_diagnostics](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3) {

30 /\* short to ground \*/

[ 31](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3abc547081143f840a6261d807fa72284e) [TLE9104\_OFFDIAG\_SCG](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3abc547081143f840a6261d807fa72284e) = 3,

32 /\* open load \*/

[ 33](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3ac37a0b72b862d7279572eaf960e5507d) [TLE9104\_OFFDIAG\_OL](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3ac37a0b72b862d7279572eaf960e5507d) = 2,

34 /\* no failure \*/

[ 35](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3a2dfab15a18c96bcbe413a4ed94da6af7) [TLE9104\_OFFDIAG\_NOFAIL](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3a2dfab15a18c96bcbe413a4ed94da6af7) = 1,

36 /\* no diagnosis done \*/

[ 37](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3ad16bbd2e028e21957316609bda7f8393) [TLE9104\_OFFDIAG\_UNKNOWN](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3ad16bbd2e028e21957316609bda7f8393) = 0,

38};

39

[ 40](structgpio__tle9104__channel__diagnostics.md)struct [gpio\_tle9104\_channel\_diagnostics](structgpio__tle9104__channel__diagnostics.md) {

[ 41](structgpio__tle9104__channel__diagnostics.md#a85b90c4dbf15bfbefb6646de10b6c634) enum [tle9104\_on\_state\_diagnostics](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0) [on](structgpio__tle9104__channel__diagnostics.md#a85b90c4dbf15bfbefb6646de10b6c634): 3;

[ 42](structgpio__tle9104__channel__diagnostics.md#adbc7944242d212933d510881541f9d66) enum [tle9104\_off\_state\_diagnostics](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3) [off](structgpio__tle9104__channel__diagnostics.md#adbc7944242d212933d510881541f9d66): 2;

43};

44

[ 53](mfd_2tle9104_8h.md#a3fbd8b8e3cdf6998990d055a6e503361)int [tle9104\_get\_diagnostics](mfd_2tle9104_8h.md#a3fbd8b8e3cdf6998990d055a6e503361)(const struct [device](structdevice.md) \*dev,

54 struct [gpio\_tle9104\_channel\_diagnostics](structgpio__tle9104__channel__diagnostics.md) diag[[TLE9104\_GPIO\_COUNT](mfd_2tle9104_8h.md#a3f6f8709aa1b46781268154e34c298a9)]);

[ 62](mfd_2tle9104_8h.md#a1c4925c222bbdd94c0fe1eb295244ec3)int [tle9104\_clear\_diagnostics](mfd_2tle9104_8h.md#a1c4925c222bbdd94c0fe1eb295244ec3)(const struct [device](structdevice.md) \*dev);

[ 71](mfd_2tle9104_8h.md#a5febfb7f1b4fd5859bf503e9ff4c2ed4)int [tle9104\_write\_state](mfd_2tle9104_8h.md#a5febfb7f1b4fd5859bf503e9ff4c2ed4)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

72

73#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_TLE9104\_H\_ \*/

[device.h](device_8h.md)

[tle9104\_clear\_diagnostics](mfd_2tle9104_8h.md#a1c4925c222bbdd94c0fe1eb295244ec3)

int tle9104\_clear\_diagnostics(const struct device \*dev)

clear the diagnostics of the outputs

[TLE9104\_GPIO\_COUNT](mfd_2tle9104_8h.md#a3f6f8709aa1b46781268154e34c298a9)

#define TLE9104\_GPIO\_COUNT

**Definition** tle9104.h:12

[tle9104\_get\_diagnostics](mfd_2tle9104_8h.md#a3fbd8b8e3cdf6998990d055a6e503361)

int tle9104\_get\_diagnostics(const struct device \*dev, struct gpio\_tle9104\_channel\_diagnostics diag[4])

get the diagnostics of the outputs

[tle9104\_write\_state](mfd_2tle9104_8h.md#a5febfb7f1b4fd5859bf503e9ff4c2ed4)

int tle9104\_write\_state(const struct device \*dev, uint8\_t state)

write output state

[tle9104\_on\_state\_diagnostics](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0)

tle9104\_on\_state\_diagnostics

**Definition** tle9104.h:14

[TLE9104\_ONDIAG\_OT](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a359b0a412ecb9de36e12a50946dc2173)

@ TLE9104\_ONDIAG\_OT

**Definition** tle9104.h:16

[TLE9104\_ONDIAG\_OCTIME](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a36e248aad4b5b47c338589d86f4e2925)

@ TLE9104\_ONDIAG\_OCTIME

**Definition** tle9104.h:18

[TLE9104\_ONDIAG\_NOFAIL](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a7aace824362e7c51841585b9f3a64ca4)

@ TLE9104\_ONDIAG\_NOFAIL

**Definition** tle9104.h:24

[TLE9104\_ONDIAG\_OCOT](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a7cea6cba428b062f1951809d12e15685)

@ TLE9104\_ONDIAG\_OCOT

**Definition** tle9104.h:20

[TLE9104\_ONDIAG\_SCB](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0a9d82a99fcc6ea7017e38959d5e299f4c)

@ TLE9104\_ONDIAG\_SCB

**Definition** tle9104.h:22

[TLE9104\_ONDIAG\_UNKNOWN](mfd_2tle9104_8h.md#aa40748ba46d1bc413f8bf3caa5d7b4b0addb7f997401544e59dc6a181c1341679)

@ TLE9104\_ONDIAG\_UNKNOWN

**Definition** tle9104.h:26

[tle9104\_off\_state\_diagnostics](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3)

tle9104\_off\_state\_diagnostics

**Definition** tle9104.h:29

[TLE9104\_OFFDIAG\_NOFAIL](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3a2dfab15a18c96bcbe413a4ed94da6af7)

@ TLE9104\_OFFDIAG\_NOFAIL

**Definition** tle9104.h:35

[TLE9104\_OFFDIAG\_SCG](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3abc547081143f840a6261d807fa72284e)

@ TLE9104\_OFFDIAG\_SCG

**Definition** tle9104.h:31

[TLE9104\_OFFDIAG\_OL](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3ac37a0b72b862d7279572eaf960e5507d)

@ TLE9104\_OFFDIAG\_OL

**Definition** tle9104.h:33

[TLE9104\_OFFDIAG\_UNKNOWN](mfd_2tle9104_8h.md#acd342488b1a9b0e2b4a0e79a1441d8e3ad16bbd2e028e21957316609bda7f8393)

@ TLE9104\_OFFDIAG\_UNKNOWN

**Definition** tle9104.h:37

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[gpio\_tle9104\_channel\_diagnostics](structgpio__tle9104__channel__diagnostics.md)

**Definition** tle9104.h:40

[gpio\_tle9104\_channel\_diagnostics::on](structgpio__tle9104__channel__diagnostics.md#a85b90c4dbf15bfbefb6646de10b6c634)

enum tle9104\_on\_state\_diagnostics on

**Definition** tle9104.h:41

[gpio\_tle9104\_channel\_diagnostics::off](structgpio__tle9104__channel__diagnostics.md#adbc7944242d212933d510881541f9d66)

enum tle9104\_off\_state\_diagnostics off

**Definition** tle9104.h:42

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [tle9104.h](mfd_2tle9104_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
