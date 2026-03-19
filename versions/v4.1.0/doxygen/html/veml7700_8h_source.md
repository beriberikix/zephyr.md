---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/veml7700_8h_source.html
original_path: doxygen/html/veml7700_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

veml7700.h

[Go to the documentation of this file.](veml7700_8h.md)

1/\*

2 \* Copyright (c) 2023 Andreas Kilian

3 \* Copyright (c) 2024 Jeff Welder (Ellenby Technologies, Inc.)

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEML7700\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEML7700\_H\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 18](veml7700_8h.md#ac67394dec210f9c64ae0f25bc24b2b4d)#define VEML7700\_ALS\_GAIN\_ELEM\_COUNT 4

[ 22](veml7700_8h.md#ab3f2271ebacc28dc6b846f696a26e9c0)#define VEML7700\_ALS\_IT\_ELEM\_COUNT 6

23

[ 30](veml7700_8h.md#a69af2a92e4e816f269d98e86ffe522b8)#define VEML7700\_ALS\_INT\_LOW\_MASK BIT(15)

[ 37](veml7700_8h.md#a4af944750098802779ef6d018ed1aa7b)#define VEML7700\_ALS\_INT\_HIGH\_MASK BIT(14)

38

[ 42](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565d)enum [veml7700\_als\_gain](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565d) {

[ 43](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da32ee11119f685ae203e9c69e7246c722) [VEML7700\_ALS\_GAIN\_1](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da32ee11119f685ae203e9c69e7246c722) = 0x00, /\* 0b00 \*/

[ 44](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da8053068f9d24805ce24f4fcead41bac2) [VEML7700\_ALS\_GAIN\_2](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da8053068f9d24805ce24f4fcead41bac2) = 0x01, /\* 0b01 \*/

[ 45](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da9a675080f74e21da950bacd74d3880cb) [VEML7700\_ALS\_GAIN\_1\_8](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da9a675080f74e21da950bacd74d3880cb) = 0x02, /\* 0b10 \*/

[ 46](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da276d18739e9bfe76c5bf91750c051cfd) [VEML7700\_ALS\_GAIN\_1\_4](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da276d18739e9bfe76c5bf91750c051cfd) = 0x03, /\* 0b11 \*/

47};

48

[ 52](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384b)enum [veml7700\_als\_it](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384b) {

[ 53](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba59491f48a2563a32c23d87608a5c289a) [VEML7700\_ALS\_IT\_25](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba59491f48a2563a32c23d87608a5c289a),

[ 54](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384baf7677738fb31f8b76f374ddcb8529c55) [VEML7700\_ALS\_IT\_50](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384baf7677738fb31f8b76f374ddcb8529c55),

[ 55](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba297e6e0e46f719b15e235bdaf312c27c) [VEML7700\_ALS\_IT\_100](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba297e6e0e46f719b15e235bdaf312c27c),

[ 56](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384bae52d52519dd988fd096a7e27470d8f65) [VEML7700\_ALS\_IT\_200](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384bae52d52519dd988fd096a7e27470d8f65),

[ 57](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba7a1da11c0773ef10cd2f0302c2bf0f7a) [VEML7700\_ALS\_IT\_400](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba7a1da11c0773ef10cd2f0302c2bf0f7a),

[ 58](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba8e8c54868774a5bd634b6deba30256c2) [VEML7700\_ALS\_IT\_800](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba8e8c54868774a5bd634b6deba30256c2)

59};

60

[ 64](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146)enum [veml7700\_int\_mode](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146) {

[ 65](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a81b919fc1c21b8202a76013a8229534f) [VEML7700\_INT\_DISABLED](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a81b919fc1c21b8202a76013a8229534f) = 0xFF,

[ 66](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a111482232b5fa120313fe9f3beae0f59) [VEML7700\_ALS\_PERS\_1](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a111482232b5fa120313fe9f3beae0f59) = 0x00, /\* 0b00 \*/

[ 67](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146aed9dbc590b13588f802335329b1fef2a) [VEML7700\_ALS\_PERS\_2](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146aed9dbc590b13588f802335329b1fef2a) = 0x01, /\* 0b01 \*/

[ 68](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a5a8ddd8d08092ded93e07ce64f78a9c2) [VEML7700\_ALS\_PERS\_4](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a5a8ddd8d08092ded93e07ce64f78a9c2) = 0x02, /\* 0b10 \*/

[ 69](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a01121c07606684416e34746df20334b5) [VEML7700\_ALS\_PERS\_8](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a01121c07606684416e34746df20334b5) = 0x03, /\* 0b11 \*/

70};

71

[ 88](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442)enum [sensor\_attribute\_veml7700](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442) {

[ 94](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442adfd7b70862fbf124dae9404711360bac) [SENSOR\_ATTR\_VEML7700\_GAIN](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442adfd7b70862fbf124dae9404711360bac) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 100](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442a0d87dcb30a761c3c9eb1dbd102617153) [SENSOR\_ATTR\_VEML7700\_ITIME](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442a0d87dcb30a761c3c9eb1dbd102617153),

[ 117](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442a7e1a16c7cfe7c5267e573b683a817b95) [SENSOR\_ATTR\_VEML7700\_INT\_MODE](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442a7e1a16c7cfe7c5267e573b683a817b95),

118};

119

[ 123](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936)enum [sensor\_channel\_veml7700](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936) {

[ 136](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936aeb3a68fec9edb12d314f6aba43389421) [SENSOR\_CHAN\_VEML7700\_RAW\_COUNTS](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936aeb3a68fec9edb12d314f6aba43389421) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

137

[ 145](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936a658e0bf9672adbc81aa80d3fd44b6627) [SENSOR\_CHAN\_VEML7700\_WHITE\_RAW\_COUNTS](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936a658e0bf9672adbc81aa80d3fd44b6627),

146

[ 157](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936a059f5aef8916164ccab1c2239e7f2465) [SENSOR\_CHAN\_VEML7700\_INTERRUPT](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936a059f5aef8916164ccab1c2239e7f2465),

158};

159

160#ifdef \_\_cplusplus

161}

162#endif

163

164#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEML7700\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[veml7700\_als\_it](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384b)

veml7700\_als\_it

VEML7700 integration time options for ambient light measurements.

**Definition** veml7700.h:52

[VEML7700\_ALS\_IT\_100](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba297e6e0e46f719b15e235bdaf312c27c)

@ VEML7700\_ALS\_IT\_100

**Definition** veml7700.h:55

[VEML7700\_ALS\_IT\_25](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba59491f48a2563a32c23d87608a5c289a)

@ VEML7700\_ALS\_IT\_25

**Definition** veml7700.h:53

[VEML7700\_ALS\_IT\_400](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba7a1da11c0773ef10cd2f0302c2bf0f7a)

@ VEML7700\_ALS\_IT\_400

**Definition** veml7700.h:57

[VEML7700\_ALS\_IT\_800](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384ba8e8c54868774a5bd634b6deba30256c2)

@ VEML7700\_ALS\_IT\_800

**Definition** veml7700.h:58

[VEML7700\_ALS\_IT\_200](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384bae52d52519dd988fd096a7e27470d8f65)

@ VEML7700\_ALS\_IT\_200

**Definition** veml7700.h:56

[VEML7700\_ALS\_IT\_50](veml7700_8h.md#a0a65ceba1f3f7b25309033a8e6c3384baf7677738fb31f8b76f374ddcb8529c55)

@ VEML7700\_ALS\_IT\_50

**Definition** veml7700.h:54

[veml7700\_int\_mode](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146)

veml7700\_int\_mode

VEML7700 ALS interrupt persistence protect number options.

**Definition** veml7700.h:64

[VEML7700\_ALS\_PERS\_8](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a01121c07606684416e34746df20334b5)

@ VEML7700\_ALS\_PERS\_8

**Definition** veml7700.h:69

[VEML7700\_ALS\_PERS\_1](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a111482232b5fa120313fe9f3beae0f59)

@ VEML7700\_ALS\_PERS\_1

**Definition** veml7700.h:66

[VEML7700\_ALS\_PERS\_4](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a5a8ddd8d08092ded93e07ce64f78a9c2)

@ VEML7700\_ALS\_PERS\_4

**Definition** veml7700.h:68

[VEML7700\_INT\_DISABLED](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146a81b919fc1c21b8202a76013a8229534f)

@ VEML7700\_INT\_DISABLED

**Definition** veml7700.h:65

[VEML7700\_ALS\_PERS\_2](veml7700_8h.md#a1f84fa22aa00479b23ada96982aa0146aed9dbc590b13588f802335329b1fef2a)

@ VEML7700\_ALS\_PERS\_2

**Definition** veml7700.h:67

[sensor\_channel\_veml7700](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936)

sensor\_channel\_veml7700

VEML7700 specific sensor channels.

**Definition** veml7700.h:123

[SENSOR\_CHAN\_VEML7700\_INTERRUPT](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936a059f5aef8916164ccab1c2239e7f2465)

@ SENSOR\_CHAN\_VEML7700\_INTERRUPT

This channel is used to query the ALS interrupt state (ALS\_INT).

**Definition** veml7700.h:157

[SENSOR\_CHAN\_VEML7700\_WHITE\_RAW\_COUNTS](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936a658e0bf9672adbc81aa80d3fd44b6627)

@ SENSOR\_CHAN\_VEML7700\_WHITE\_RAW\_COUNTS

Channel for white light sensor values.

**Definition** veml7700.h:145

[SENSOR\_CHAN\_VEML7700\_RAW\_COUNTS](veml7700_8h.md#a2680058e5ede3f8c76e191e19ef68936aeb3a68fec9edb12d314f6aba43389421)

@ SENSOR\_CHAN\_VEML7700\_RAW\_COUNTS

Channel for raw ALS sensor values.

**Definition** veml7700.h:136

[sensor\_attribute\_veml7700](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442)

sensor\_attribute\_veml7700

VEML7700 specific sensor attributes.

**Definition** veml7700.h:88

[SENSOR\_ATTR\_VEML7700\_ITIME](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442a0d87dcb30a761c3c9eb1dbd102617153)

@ SENSOR\_ATTR\_VEML7700\_ITIME

Integration time setting for ALS measurements (ALS\_IT).

**Definition** veml7700.h:100

[SENSOR\_ATTR\_VEML7700\_INT\_MODE](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442a7e1a16c7cfe7c5267e573b683a817b95)

@ SENSOR\_ATTR\_VEML7700\_INT\_MODE

Enable or disable use of ALS interrupt (ALS\_INT\_EN and ALS\_PERS).

**Definition** veml7700.h:117

[SENSOR\_ATTR\_VEML7700\_GAIN](veml7700_8h.md#a26c425381bfcb7f264c79d505d900442adfd7b70862fbf124dae9404711360bac)

@ SENSOR\_ATTR\_VEML7700\_GAIN

Gain setting for ALS measurements (ALS\_GAIN).

**Definition** veml7700.h:94

[veml7700\_als\_gain](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565d)

veml7700\_als\_gain

VEML7700 gain options for ambient light measurements.

**Definition** veml7700.h:42

[VEML7700\_ALS\_GAIN\_1\_4](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da276d18739e9bfe76c5bf91750c051cfd)

@ VEML7700\_ALS\_GAIN\_1\_4

**Definition** veml7700.h:46

[VEML7700\_ALS\_GAIN\_1](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da32ee11119f685ae203e9c69e7246c722)

@ VEML7700\_ALS\_GAIN\_1

**Definition** veml7700.h:43

[VEML7700\_ALS\_GAIN\_2](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da8053068f9d24805ce24f4fcead41bac2)

@ VEML7700\_ALS\_GAIN\_2

**Definition** veml7700.h:44

[VEML7700\_ALS\_GAIN\_1\_8](veml7700_8h.md#ad4a2d50801f3f4d2e1390e6c5dac565da9a675080f74e21da950bacd74d3880cb)

@ VEML7700\_ALS\_GAIN\_1\_8

**Definition** veml7700.h:45

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [veml7700.h](veml7700_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
