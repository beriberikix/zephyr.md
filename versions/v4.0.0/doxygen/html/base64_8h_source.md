---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/base64_8h_source.html
original_path: doxygen/html/base64_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

base64.h

[Go to the documentation of this file.](base64_8h.md)

1/\*

2 \* RFC 1521 base64 encoding/decoding

3 \*

4 \* Copyright (C) 2018, Nordic Semiconductor ASA

5 \* Copyright (C) 2006-2015, ARM Limited, All Rights Reserved

6 \* SPDX-License-Identifier: Apache-2.0

7 \*

8 \* Licensed under the Apache License, Version 2.0 (the "License"); you may

9 \* not use this file except in compliance with the License.

10 \* You may obtain a copy of the License at

11 \*

12 \* http://www.apache.org/licenses/LICENSE-2.0

13 \*

14 \* Unless required by applicable law or agreed to in writing, software

15 \* distributed under the License is distributed on an "AS IS" BASIS, WITHOUT

16 \* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

17 \* See the License for the specific language governing permissions and

18 \* limitations under the License.

19 \*

20 \* Adapted for Zephyr by Carles Cufi (carles.cufi@nordicsemi.no)

21 \* - Removed mbedtls\_ prefixes

22 \* - Reworked coding style

23 \*/

24#ifndef ZEPHYR\_INCLUDE\_SYS\_BASE64\_H\_

25#define ZEPHYR\_INCLUDE\_SYS\_BASE64\_H\_

26

27#include <stddef.h>

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

42

[ 62](group__base64.md#gaaff09edf41470c26d5a54d18c4f91ba0)int [base64\_encode](group__base64.md#gaaff09edf41470c26d5a54d18c4f91ba0)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, size\_t dlen, size\_t \*olen, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src,

63 size\_t slen);

64

[ 81](group__base64.md#ga9e84f3adc54120fb1f1ccffb1bac8c5c)int [base64\_decode](group__base64.md#ga9e84f3adc54120fb1f1ccffb1bac8c5c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, size\_t dlen, size\_t \*olen, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src,

82 size\_t slen);

83

87

88#ifdef \_\_cplusplus

89}

90#endif

91

92#endif /\* ZEPHYR\_INCLUDE\_SYS\_BASE64\_H\_ \*/

[base64\_decode](group__base64.md#ga9e84f3adc54120fb1f1ccffb1bac8c5c)

int base64\_decode(uint8\_t \*dst, size\_t dlen, size\_t \*olen, const uint8\_t \*src, size\_t slen)

Decode a base64-formatted buffer.

[base64\_encode](group__base64.md#gaaff09edf41470c26d5a54d18c4f91ba0)

int base64\_encode(uint8\_t \*dst, size\_t dlen, size\_t \*olen, const uint8\_t \*src, size\_t slen)

Encode a buffer into base64 format.

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [base64.h](base64_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
