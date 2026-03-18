---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/navigation_8h_source.html
original_path: doxygen/html/navigation_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

navigation.h

[Go to the documentation of this file.](navigation_8h.md)

1/\*

2 \* Copyright (c) 2023 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DATA\_NAVIGATION\_H\_

8#define ZEPHYR\_INCLUDE\_DATA\_NAVIGATION\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11

18

[ 25](structnavigation__data.md)struct [navigation\_data](structnavigation__data.md) {

[ 27](structnavigation__data.md#a02d9f8cea5fe68810123bb2bf554d59c) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [latitude](structnavigation__data.md#a02d9f8cea5fe68810123bb2bf554d59c);

[ 29](structnavigation__data.md#a530eb9c4e3750bbb03b26256794d0914) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [longitude](structnavigation__data.md#a530eb9c4e3750bbb03b26256794d0914);

[ 31](structnavigation__data.md#af9887a29823fc3e083dbd14d1f6cfce1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bearing](structnavigation__data.md#af9887a29823fc3e083dbd14d1f6cfce1);

[ 33](structnavigation__data.md#a5fd501c07c21e66217a7634d7d607d1d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [speed](structnavigation__data.md#a5fd501c07c21e66217a7634d7d607d1d);

[ 35](structnavigation__data.md#addd80254be4619c4ea7707f9c9bc434e) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [altitude](structnavigation__data.md#addd80254be4619c4ea7707f9c9bc434e);

36};

37

[ 49](group__navigation.md#ga99b3460548c6e88cb16391ba77303829)int [navigation\_distance](group__navigation.md#ga99b3460548c6e88cb16391ba77303829)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*distance, const struct [navigation\_data](structnavigation__data.md) \*p1,

50 const struct [navigation\_data](structnavigation__data.md) \*p2);

51

[ 62](group__navigation.md#ga36655c6a733ba4e96cc6bfd055a0bf8b)int [navigation\_bearing](group__navigation.md#ga36655c6a733ba4e96cc6bfd055a0bf8b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bearing, const struct [navigation\_data](structnavigation__data.md) \*from,

63 const struct [navigation\_data](structnavigation__data.md) \*to);

64

68

69#endif /\* ZEPHYR\_INCLUDE\_DATA\_NAVIGATION\_H\_ \*/

[navigation\_bearing](group__navigation.md#ga36655c6a733ba4e96cc6bfd055a0bf8b)

int navigation\_bearing(uint32\_t \*bearing, const struct navigation\_data \*from, const struct navigation\_data \*to)

Calculate the bearing from one navigation point to another.

[navigation\_distance](group__navigation.md#ga99b3460548c6e88cb16391ba77303829)

int navigation\_distance(uint64\_t \*distance, const struct navigation\_data \*p1, const struct navigation\_data \*p2)

Calculate the distance between two navigation points along the surface of the sphere they are relativ...

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[navigation\_data](structnavigation__data.md)

Navigation data structure.

**Definition** navigation.h:25

[navigation\_data::latitude](structnavigation__data.md#a02d9f8cea5fe68810123bb2bf554d59c)

int64\_t latitude

Latitudal position in nanodegrees (0 to +-180E9).

**Definition** navigation.h:27

[navigation\_data::longitude](structnavigation__data.md#a530eb9c4e3750bbb03b26256794d0914)

int64\_t longitude

Longitudal position in nanodegrees (0 to +-180E9).

**Definition** navigation.h:29

[navigation\_data::speed](structnavigation__data.md#a5fd501c07c21e66217a7634d7d607d1d)

uint32\_t speed

Speed in millimeters per second.

**Definition** navigation.h:33

[navigation\_data::altitude](structnavigation__data.md#addd80254be4619c4ea7707f9c9bc434e)

int32\_t altitude

Altitude in millimeters.

**Definition** navigation.h:35

[navigation\_data::bearing](structnavigation__data.md#af9887a29823fc3e083dbd14d1f6cfce1)

uint32\_t bearing

Bearing angle in millidegrees (0 to 360E3).

**Definition** navigation.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [navigation.h](navigation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
