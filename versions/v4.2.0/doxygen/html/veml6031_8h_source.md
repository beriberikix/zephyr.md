---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/veml6031_8h_source.html
original_path: doxygen/html/veml6031_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

veml6031.h

[Go to the documentation of this file.](veml6031_8h.md)

1/\*

2 \* Copyright (c) 2025 Andreas Klinger

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEML6031\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEML6031\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 17](veml6031_8h.md#a80407fb0f3f0f2b5d1b38ff5c3866ac2)#define VEML6031\_IT\_COUNT 8

18

[ 22](veml6031_8h.md#ab012f37d591068026144c58f91579c9c)#define VEML6031\_DIV4\_COUNT 2

23

[ 27](veml6031_8h.md#a50967c3d3a992f86809c453dae11ac63)#define VEML6031\_GAIN\_COUNT 4

28

[ 32](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48)enum [veml6031\_it](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48) {

[ 33](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48af5f3b0abfe29e054a836fc23230e9ce3) [VEML6031\_IT\_3\_125](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48af5f3b0abfe29e054a836fc23230e9ce3),

[ 34](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48aaa372f638dea84de8fc956fd3495faa4) [VEML6031\_IT\_6\_25](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48aaa372f638dea84de8fc956fd3495faa4),

[ 35](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a723461db85c4290a55a382f2b6fec943) [VEML6031\_IT\_12\_5](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a723461db85c4290a55a382f2b6fec943),

[ 36](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a2b1ef63fb3639cd3ec9827b38b087d65) [VEML6031\_IT\_25](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a2b1ef63fb3639cd3ec9827b38b087d65),

[ 37](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48ad6e9f49df7626211bcc75060815367b4) [VEML6031\_IT\_50](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48ad6e9f49df7626211bcc75060815367b4),

[ 38](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a178b82ca661215ef933a18c6c145c23c) [VEML6031\_IT\_100](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a178b82ca661215ef933a18c6c145c23c),

[ 39](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48ae6c2cca74f808ff39719688f38cd3d43) [VEML6031\_IT\_200](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48ae6c2cca74f808ff39719688f38cd3d43),

[ 40](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a2dffb8d61fb3def0fe80254d13d60e34) [VEML6031\_IT\_400](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a2dffb8d61fb3def0fe80254d13d60e34),

41};

42

[ 46](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738)enum [veml6031\_div4](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738) {

[ 47](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022) [VEML6031\_SIZE\_4\_4](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022) = 0x00, /\* 0b0 \*/

[ 48](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3) [VEML6031\_SIZE\_1\_4](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3) = 0x01, /\* 0b1 \*/

49};

50

[ 54](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25)enum [veml6031\_gain](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25) {

[ 55](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a4d96f11df7a9082d2c277eec776f577e) [VEML6031\_GAIN\_1](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a4d96f11df7a9082d2c277eec776f577e) = 0x00, /\* 0b00 \*/

[ 56](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a65040b101009f8c7b5e696343cc9c600) [VEML6031\_GAIN\_2](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a65040b101009f8c7b5e696343cc9c600) = 0x01, /\* 0b01 \*/

[ 57](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a7e304d4c5a83dfa972772f6fe1c2fa05) [VEML6031\_GAIN\_0\_66](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a7e304d4c5a83dfa972772f6fe1c2fa05) = 0x02, /\* 0b10 \*/

[ 58](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25aed832ee21e860b63ec585abfffa45c3a) [VEML6031\_GAIN\_0\_5](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25aed832ee21e860b63ec585abfffa45c3a) = 0x03, /\* 0b11 \*/

59};

60

[ 64](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53)enum [veml6031\_pers](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53) {

[ 65](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a047fdfb8b35507eee3cd58ba05555171) [VEML6031\_PERS\_1](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a047fdfb8b35507eee3cd58ba05555171) = 0x00, /\* 0b00 \*/

[ 66](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a278d3868b2f6555666b09f6d141268bf) [VEML6031\_PERS\_2](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a278d3868b2f6555666b09f6d141268bf) = 0x01, /\* 0b01 \*/

[ 67](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a54fa5f703a1e6b84fabb8969c6f1c146) [VEML6031\_PERS\_4](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a54fa5f703a1e6b84fabb8969c6f1c146) = 0x02, /\* 0b10 \*/

[ 68](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a80a1e637ca842bd31541ad4a1a7fafec) [VEML6031\_PERS\_8](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a80a1e637ca842bd31541ad4a1a7fafec) = 0x03, /\* 0b11 \*/

69};

70

[ 95](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacc)enum [sensor\_attribute\_veml6031](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacc) {

[ 101](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80) [SENSOR\_ATTR\_VEML6031\_IT](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80) = [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3),

[ 107](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c) [SENSOR\_ATTR\_VEML6031\_DIV4](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c),

[ 113](veml6031_8h.md#ae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a) [SENSOR\_ATTR\_VEML6031\_GAIN](veml6031_8h.md#ae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a),

[ 119](veml6031_8h.md#ae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07) [SENSOR\_ATTR\_VEML6031\_PERS](veml6031_8h.md#ae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07),

120};

121

[ 125](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9)enum [sensor\_channel\_veml6031](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9) {

[ 143](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d) [SENSOR\_CHAN\_VEML6031\_ALS\_RAW\_COUNTS](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d) = [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12),

144

[ 152](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65) [SENSOR\_CHAN\_VEML6031\_IR\_RAW\_COUNTS](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65),

153};

154

155#ifdef \_\_cplusplus

156}

157#endif

158

159#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_VEML6031\_H\_ \*/

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:372

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

[veml6031\_pers](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53)

veml6031\_pers

VEML6031 ALS interrupt persistence protect number options.

**Definition** veml6031.h:64

[VEML6031\_PERS\_1](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a047fdfb8b35507eee3cd58ba05555171)

@ VEML6031\_PERS\_1

**Definition** veml6031.h:65

[VEML6031\_PERS\_2](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a278d3868b2f6555666b09f6d141268bf)

@ VEML6031\_PERS\_2

**Definition** veml6031.h:66

[VEML6031\_PERS\_4](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a54fa5f703a1e6b84fabb8969c6f1c146)

@ VEML6031\_PERS\_4

**Definition** veml6031.h:67

[VEML6031\_PERS\_8](veml6031_8h.md#a087e06d636c5117ee42b48257d756a53a80a1e637ca842bd31541ad4a1a7fafec)

@ VEML6031\_PERS\_8

**Definition** veml6031.h:68

[veml6031\_gain](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25)

veml6031\_gain

VEML6031 gain options for ambient light measurements.

**Definition** veml6031.h:54

[VEML6031\_GAIN\_1](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a4d96f11df7a9082d2c277eec776f577e)

@ VEML6031\_GAIN\_1

**Definition** veml6031.h:55

[VEML6031\_GAIN\_2](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a65040b101009f8c7b5e696343cc9c600)

@ VEML6031\_GAIN\_2

**Definition** veml6031.h:56

[VEML6031\_GAIN\_0\_66](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25a7e304d4c5a83dfa972772f6fe1c2fa05)

@ VEML6031\_GAIN\_0\_66

**Definition** veml6031.h:57

[VEML6031\_GAIN\_0\_5](veml6031_8h.md#a50e6ea4bf25a4afd2bd3702200f46b25aed832ee21e860b63ec585abfffa45c3a)

@ VEML6031\_GAIN\_0\_5

**Definition** veml6031.h:58

[veml6031\_it](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48)

veml6031\_it

VEML6031 integration time options for ambient light measurements.

**Definition** veml6031.h:32

[VEML6031\_IT\_100](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a178b82ca661215ef933a18c6c145c23c)

@ VEML6031\_IT\_100

**Definition** veml6031.h:38

[VEML6031\_IT\_25](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a2b1ef63fb3639cd3ec9827b38b087d65)

@ VEML6031\_IT\_25

**Definition** veml6031.h:36

[VEML6031\_IT\_400](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a2dffb8d61fb3def0fe80254d13d60e34)

@ VEML6031\_IT\_400

**Definition** veml6031.h:40

[VEML6031\_IT\_12\_5](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48a723461db85c4290a55a382f2b6fec943)

@ VEML6031\_IT\_12\_5

**Definition** veml6031.h:35

[VEML6031\_IT\_6\_25](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48aaa372f638dea84de8fc956fd3495faa4)

@ VEML6031\_IT\_6\_25

**Definition** veml6031.h:34

[VEML6031\_IT\_50](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48ad6e9f49df7626211bcc75060815367b4)

@ VEML6031\_IT\_50

**Definition** veml6031.h:37

[VEML6031\_IT\_200](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48ae6c2cca74f808ff39719688f38cd3d43)

@ VEML6031\_IT\_200

**Definition** veml6031.h:39

[VEML6031\_IT\_3\_125](veml6031_8h.md#a61335b989567d52fe7188a3d2a738c48af5f3b0abfe29e054a836fc23230e9ce3)

@ VEML6031\_IT\_3\_125

**Definition** veml6031.h:33

[veml6031\_div4](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738)

veml6031\_div4

VEML6031 size options for ambient light measurements.

**Definition** veml6031.h:46

[VEML6031\_SIZE\_4\_4](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022)

@ VEML6031\_SIZE\_4\_4

**Definition** veml6031.h:47

[VEML6031\_SIZE\_1\_4](veml6031_8h.md#a8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3)

@ VEML6031\_SIZE\_1\_4

**Definition** veml6031.h:48

[sensor\_attribute\_veml6031](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacc)

sensor\_attribute\_veml6031

VEML6031 specific sensor attributes.

**Definition** veml6031.h:95

[SENSOR\_ATTR\_VEML6031\_DIV4](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c)

@ SENSOR\_ATTR\_VEML6031\_DIV4

Effective photodiode size (DIV4).

**Definition** veml6031.h:107

[SENSOR\_ATTR\_VEML6031\_IT](veml6031_8h.md#ae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80)

@ SENSOR\_ATTR\_VEML6031\_IT

Integration time setting for ALS measurements (IT).

**Definition** veml6031.h:101

[SENSOR\_ATTR\_VEML6031\_PERS](veml6031_8h.md#ae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07)

@ SENSOR\_ATTR\_VEML6031\_PERS

ALS persistence protect number setting (PERS).

**Definition** veml6031.h:119

[SENSOR\_ATTR\_VEML6031\_GAIN](veml6031_8h.md#ae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a)

@ SENSOR\_ATTR\_VEML6031\_GAIN

Gain setting for ALS measurements (GAIN).

**Definition** veml6031.h:113

[sensor\_channel\_veml6031](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9)

sensor\_channel\_veml6031

VEML6031 specific sensor channels.

**Definition** veml6031.h:125

[SENSOR\_CHAN\_VEML6031\_ALS\_RAW\_COUNTS](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d)

@ SENSOR\_CHAN\_VEML6031\_ALS\_RAW\_COUNTS

Channel for raw ALS sensor values.

**Definition** veml6031.h:143

[SENSOR\_CHAN\_VEML6031\_IR\_RAW\_COUNTS](veml6031_8h.md#af62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65)

@ SENSOR\_CHAN\_VEML6031\_IR\_RAW\_COUNTS

Channel for IR sensor values.

**Definition** veml6031.h:152

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [veml6031.h](veml6031_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
