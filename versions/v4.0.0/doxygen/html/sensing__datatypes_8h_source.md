---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sensing__datatypes_8h_source.html
original_path: doxygen/html/sensing__datatypes_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_datatypes.h

[Go to the documentation of this file.](sensing__datatypes_8h.md)

1/\*

2 \* Copyright (c) 2022-2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SENSING\_DATATYPES\_H\_

8#define ZEPHYR\_INCLUDE\_SENSING\_DATATYPES\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

12

18

[ 47](structsensing__sensor__value__header.md)struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) {

[ 49](structsensing__sensor__value__header.md#aa8efbfd682535deca1172cb192c1a86c) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [base\_timestamp](structsensing__sensor__value__header.md#aa8efbfd682535deca1172cb192c1a86c);

[ 51](structsensing__sensor__value__header.md#a147989d4c36de1cbd83093a2c5d90950) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reading\_count](structsensing__sensor__value__header.md#a147989d4c36de1cbd83093a2c5d90950);

52};

53

58

[ 67](structsensing__sensor__value__3d__q31.md)struct [sensing\_sensor\_value\_3d\_q31](structsensing__sensor__value__3d__q31.md) {

[ 69](structsensing__sensor__value__3d__q31.md#a163e62d50de3b5f61688ff9b00db0dcd) struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) [header](structsensing__sensor__value__3d__q31.md#a163e62d50de3b5f61688ff9b00db0dcd);

[ 70](structsensing__sensor__value__3d__q31.md#af0db9faee6eaabff7f9c2f955873378b) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensing__sensor__value__3d__q31.md#af0db9faee6eaabff7f9c2f955873378b);

71 struct {

[ 73](structsensing__sensor__value__3d__q31.md#a1bf323a7bb69af0801acebfe03e35b7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensing__sensor__value__3d__q31.md#a1bf323a7bb69af0801acebfe03e35b7a);

74 union {

[ 82](structsensing__sensor__value__3d__q31.md#a68eefb9ba2e8d954e8ea3c4f30893f3f) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [v](structsensing__sensor__value__3d__q31.md#a68eefb9ba2e8d954e8ea3c4f30893f3f)[3];

83 struct {

[ 84](structsensing__sensor__value__3d__q31.md#ad1d2f43d1a9a4b5333ac1b8531d6c94c) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [x](structsensing__sensor__value__3d__q31.md#ad1d2f43d1a9a4b5333ac1b8531d6c94c);

[ 85](structsensing__sensor__value__3d__q31.md#a721b9cd33e360691b9fb07a90c3f4df2) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [y](structsensing__sensor__value__3d__q31.md#a721b9cd33e360691b9fb07a90c3f4df2);

[ 86](structsensing__sensor__value__3d__q31.md#abbf0f5aaae8978eba1e5f3e2ffad20d0) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [z](structsensing__sensor__value__3d__q31.md#abbf0f5aaae8978eba1e5f3e2ffad20d0);

87 };

88 };

[ 89](structsensing__sensor__value__3d__q31.md#aea782e09d486595b5fbd7a94f3bde253) } [readings](structsensing__sensor__value__3d__q31.md#aea782e09d486595b5fbd7a94f3bde253)[1];

90};

91

[ 97](structsensing__sensor__value__uint32.md)struct [sensing\_sensor\_value\_uint32](structsensing__sensor__value__uint32.md) {

[ 99](structsensing__sensor__value__uint32.md#adfb3431b5b5e90d29931b9861c9dcd21) struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) [header](structsensing__sensor__value__uint32.md#adfb3431b5b5e90d29931b9861c9dcd21);

100 struct {

[ 102](structsensing__sensor__value__uint32.md#a1fd1c1d018a3793e56e4d0bfded03812) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensing__sensor__value__uint32.md#a1fd1c1d018a3793e56e4d0bfded03812);

[ 107](structsensing__sensor__value__uint32.md#a10d8f7d8f36c4969552b297ed34bf592) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [v](structsensing__sensor__value__uint32.md#a10d8f7d8f36c4969552b297ed34bf592);

[ 108](structsensing__sensor__value__uint32.md#af30e831ebd860b0dec15733220bdb9df) } [readings](structsensing__sensor__value__uint32.md#af30e831ebd860b0dec15733220bdb9df)[1];

109};

110

[ 116](structsensing__sensor__value__q31.md)struct [sensing\_sensor\_value\_q31](structsensing__sensor__value__q31.md) {

[ 118](structsensing__sensor__value__q31.md#af3dbde41e764de34d1b2b38800909da9) struct [sensing\_sensor\_value\_header](structsensing__sensor__value__header.md) [header](structsensing__sensor__value__q31.md#af3dbde41e764de34d1b2b38800909da9);

[ 119](structsensing__sensor__value__q31.md#a555e1bec3fe6f781fd12c13a097d4f16) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensing__sensor__value__q31.md#a555e1bec3fe6f781fd12c13a097d4f16);

120 struct {

[ 122](structsensing__sensor__value__q31.md#aff3865d5645e7cb53718b4f09b20b162) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp\_delta](structsensing__sensor__value__q31.md#aff3865d5645e7cb53718b4f09b20b162);

[ 127](structsensing__sensor__value__q31.md#ad3ed83faec34ebce96e57e23aab36101) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [v](structsensing__sensor__value__q31.md#ad3ed83faec34ebce96e57e23aab36101);

[ 128](structsensing__sensor__value__q31.md#a94e301bf8a27dfdb0e5e6c2d6540b83b) } [readings](structsensing__sensor__value__q31.md#a94e301bf8a27dfdb0e5e6c2d6540b83b)[1];

129};

130

134

135#endif /\*ZEPHYR\_INCLUDE\_SENSING\_DATATYPES\_H\_\*/

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[types.h](include_2zephyr_2dsp_2types_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[sensing\_sensor\_value\_3d\_q31](structsensing__sensor__value__3d__q31.md)

Sensor value data structure types based on common data types.

**Definition** sensing\_datatypes.h:67

[sensing\_sensor\_value\_3d\_q31::header](structsensing__sensor__value__3d__q31.md#a163e62d50de3b5f61688ff9b00db0dcd)

struct sensing\_sensor\_value\_header header

Header of the sensor value data structure.

**Definition** sensing\_datatypes.h:69

[sensing\_sensor\_value\_3d\_q31::timestamp\_delta](structsensing__sensor__value__3d__q31.md#a1bf323a7bb69af0801acebfe03e35b7a)

uint32\_t timestamp\_delta

Timestamp delta of the reading.

**Definition** sensing\_datatypes.h:73

[sensing\_sensor\_value\_3d\_q31::v](structsensing__sensor__value__3d__q31.md#a68eefb9ba2e8d954e8ea3c4f30893f3f)

q31\_t v[3]

3D vector of the reading represented as an array.

**Definition** sensing\_datatypes.h:82

[sensing\_sensor\_value\_3d\_q31::y](structsensing__sensor__value__3d__q31.md#a721b9cd33e360691b9fb07a90c3f4df2)

q31\_t y

Y value of the 3D vector.

**Definition** sensing\_datatypes.h:85

[sensing\_sensor\_value\_3d\_q31::z](structsensing__sensor__value__3d__q31.md#abbf0f5aaae8978eba1e5f3e2ffad20d0)

q31\_t z

Z value of the 3D vector.

**Definition** sensing\_datatypes.h:86

[sensing\_sensor\_value\_3d\_q31::x](structsensing__sensor__value__3d__q31.md#ad1d2f43d1a9a4b5333ac1b8531d6c94c)

q31\_t x

X value of the 3D vector.

**Definition** sensing\_datatypes.h:84

[sensing\_sensor\_value\_3d\_q31::readings](structsensing__sensor__value__3d__q31.md#aea782e09d486595b5fbd7a94f3bde253)

struct sensing\_sensor\_value\_3d\_q31::@176346110177305251225137216044006321172315250021 readings[1]

Array of readings.

[sensing\_sensor\_value\_3d\_q31::shift](structsensing__sensor__value__3d__q31.md#af0db9faee6eaabff7f9c2f955873378b)

int8\_t shift

The shift value for the q31\_t v[3] reading.

**Definition** sensing\_datatypes.h:70

[sensing\_sensor\_value\_header](structsensing__sensor__value__header.md)

sensor value header

**Definition** sensing\_datatypes.h:47

[sensing\_sensor\_value\_header::reading\_count](structsensing__sensor__value__header.md#a147989d4c36de1cbd83093a2c5d90950)

uint16\_t reading\_count

Count of this data readings.

**Definition** sensing\_datatypes.h:51

[sensing\_sensor\_value\_header::base\_timestamp](structsensing__sensor__value__header.md#aa8efbfd682535deca1172cb192c1a86c)

uint64\_t base\_timestamp

Base timestamp of this data readings, unit is micro seconds.

**Definition** sensing\_datatypes.h:49

[sensing\_sensor\_value\_q31](structsensing__sensor__value__q31.md)

Sensor value data structure for single 1-axis value.

**Definition** sensing\_datatypes.h:116

[sensing\_sensor\_value\_q31::shift](structsensing__sensor__value__q31.md#a555e1bec3fe6f781fd12c13a097d4f16)

int8\_t shift

The shift value for the q31\_t v reading.

**Definition** sensing\_datatypes.h:119

[sensing\_sensor\_value\_q31::readings](structsensing__sensor__value__q31.md#a94e301bf8a27dfdb0e5e6c2d6540b83b)

struct sensing\_sensor\_value\_q31::@361124063133311063317235364315054120365236072176 readings[1]

Array of readings.

[sensing\_sensor\_value\_q31::v](structsensing__sensor__value__q31.md#ad3ed83faec34ebce96e57e23aab36101)

q31\_t v

Value of the reading.

**Definition** sensing\_datatypes.h:127

[sensing\_sensor\_value\_q31::header](structsensing__sensor__value__q31.md#af3dbde41e764de34d1b2b38800909da9)

struct sensing\_sensor\_value\_header header

Header of the sensor value data structure.

**Definition** sensing\_datatypes.h:118

[sensing\_sensor\_value\_q31::timestamp\_delta](structsensing__sensor__value__q31.md#aff3865d5645e7cb53718b4f09b20b162)

uint32\_t timestamp\_delta

Timestamp delta of the reading.

**Definition** sensing\_datatypes.h:122

[sensing\_sensor\_value\_uint32](structsensing__sensor__value__uint32.md)

Sensor value data structure for single 1-axis value.

**Definition** sensing\_datatypes.h:97

[sensing\_sensor\_value\_uint32::v](structsensing__sensor__value__uint32.md#a10d8f7d8f36c4969552b297ed34bf592)

uint32\_t v

Value of the reading.

**Definition** sensing\_datatypes.h:107

[sensing\_sensor\_value\_uint32::timestamp\_delta](structsensing__sensor__value__uint32.md#a1fd1c1d018a3793e56e4d0bfded03812)

uint32\_t timestamp\_delta

Timestamp delta of the reading.

**Definition** sensing\_datatypes.h:102

[sensing\_sensor\_value\_uint32::header](structsensing__sensor__value__uint32.md#adfb3431b5b5e90d29931b9861c9dcd21)

struct sensing\_sensor\_value\_header header

Header of the sensor value data structure.

**Definition** sensing\_datatypes.h:99

[sensing\_sensor\_value\_uint32::readings](structsensing__sensor__value__uint32.md#af30e831ebd860b0dec15733220bdb9df)

struct sensing\_sensor\_value\_uint32::@147360220120047335200013155150264177225355007267 readings[1]

Array of readings.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sensing](dir_89ae873b54fa3664e4a65bb9dc3973c9.md)
- [sensing\_datatypes.h](sensing__datatypes_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
