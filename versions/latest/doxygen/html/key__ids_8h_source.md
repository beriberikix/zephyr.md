---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/key__ids_8h_source.html
original_path: doxygen/html/key__ids_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

key\_ids.h

[Go to the documentation of this file.](key__ids_8h.md)

1/\* Copyright (c) 2025 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef ZEPHYR\_PSA\_KEY\_IDS\_H\_

5#define ZEPHYR\_PSA\_KEY\_IDS\_H\_

6

23

24#include <[stdint.h](stdint_8h.md)>

[ 25](key__ids_8h.md#a11e986351c65bd3dc3c0fe2cd9926e4b)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psa\_key\_id\_t](key__ids_8h.md#a11e986351c65bd3dc3c0fe2cd9926e4b);

26

[ 30](key__ids_8h.md#a3e8bcbe8554a07e045a7330196c8a003)#define ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_BEGIN (psa\_key\_id\_t)0x20000

[ 31](key__ids_8h.md#a484d6a1af8ccc3a869b9a2b7753d1c2c)#define ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_SIZE 0x10000 /\* 64 Ki \*/

32

[ 36](key__ids_8h.md#ae4606ebca8aa09c0096897c927981cb6)#define ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_BEGIN (psa\_key\_id\_t)0x30000

[ 37](key__ids_8h.md#a6b459be7f0d6d39cd6bf8d482473b23f)#define ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_SIZE 0x10000 /\* 64 Ki \*/

38

[ 40](key__ids_8h.md#a032913d751fddc7a6a0ac3f98229947d)#define ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_BEGIN (psa\_key\_id\_t)0x20000000

[ 41](key__ids_8h.md#a6b1b95861f2a8b9b9f45e0c8dee04007)#define ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_SIZE 0xC000 /\* 48 Ki \*/

42

[ 44](key__ids_8h.md#ac02d47ca235e44f30e5fa32aa5cbfadc)#define ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_BEGIN (psa\_key\_id\_t)0x20010000

[ 45](key__ids_8h.md#a86a47e671a632befdce9b201a66002d5)#define ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_SIZE 0x100 /\* 256 \*/

46

[ 48](key__ids_8h.md#af0f6e7d2b0798aaaccc3fb3bd12d1b8a)#define ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_BEGIN (psa\_key\_id\_t)0x30000000

[ 49](key__ids_8h.md#ad222fd0bf1eb32eaa23d6bd52d300125)#define ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_SIZE 0x100000 /\* 1 Mi \*/

50

51#endif /\* ZEPHYR\_PSA\_KEY\_IDS\_H\_ \*/

[psa\_key\_id\_t](key__ids_8h.md#a11e986351c65bd3dc3c0fe2cd9926e4b)

uint32\_t psa\_key\_id\_t

**Definition** key\_ids.h:25

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [psa](dir_2e753b890c44631130dcc36a0ce9c9fd.md)
- [key\_ids.h](key__ids_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
