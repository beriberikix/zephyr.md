---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/keys_8h_source.html
original_path: doxygen/html/keys_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

keys.h

[Go to the documentation of this file.](keys_8h.md)

1

4

5/\*

6 \* Copyright (c) 2023 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_KEYS\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_KEYS\_H\_

13

14#include <[stdint.h](stdint_8h.md)>

15#if defined CONFIG\_BT\_MESH\_USES\_MBEDTLS\_PSA || defined CONFIG\_BT\_MESH\_USES\_TFM\_PSA

16#include <psa/crypto.h>

17#endif

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

23#if defined CONFIG\_BT\_MESH\_USES\_MBEDTLS\_PSA || defined CONFIG\_BT\_MESH\_USES\_TFM\_PSA

24

26struct bt\_mesh\_key {

28 psa\_key\_id\_t key;

29};

30

31#elif defined CONFIG\_BT\_MESH\_USES\_TINYCRYPT

32

34struct bt\_mesh\_key {

36 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16];

37};

38

39#else

40#error "Crypto library has not been chosen"

41#endif

42

43#ifdef \_\_cplusplus

44}

45#endif

46

47#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_KEYS\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [keys.h](keys_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
