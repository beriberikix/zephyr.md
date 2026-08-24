---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/bluetooth_2mesh_2keys_8h_source.html
original_path: doxygen/html/bluetooth_2mesh_2keys_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

keys.h

[Go to the documentation of this file.](bluetooth_2mesh_2keys_8h.md)

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

15#include <psa/crypto.h>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 22](structbt__mesh__key.md)struct [bt\_mesh\_key](structbt__mesh__key.md) {

[ 24](structbt__mesh__key.md#a50acd9d36423b22aab033795b9d29d78) [psa\_key\_id\_t](key__ids_8h.md#a11e986351c65bd3dc3c0fe2cd9926e4b) [key](structbt__mesh__key.md#a50acd9d36423b22aab033795b9d29d78);

25};

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_KEYS\_H\_ \*/

[psa\_key\_id\_t](key__ids_8h.md#a11e986351c65bd3dc3c0fe2cd9926e4b)

uint32\_t psa\_key\_id\_t

**Definition** key\_ids.h:25

[stdint.h](stdint_8h.md)

[bt\_mesh\_key](structbt__mesh__key.md)

The structure that keeps representation of key.

**Definition** keys.h:22

[bt\_mesh\_key::key](structbt__mesh__key.md#a50acd9d36423b22aab033795b9d29d78)

psa\_key\_id\_t key

PSA key representation is the PSA key identifier.

**Definition** keys.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [keys.h](bluetooth_2mesh_2keys_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
