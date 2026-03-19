---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nordic-owned-memory_8h_source.html
original_path: doxygen/html/nordic-owned-memory_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-owned-memory.h

[Go to the documentation of this file.](nordic-owned-memory_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESERVED\_MEMORY\_NORDIC\_OWNED\_MEMORY\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESERVED\_MEMORY\_NORDIC\_OWNED\_MEMORY\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

15

[ 17](nordic-owned-memory_8h.md#af64e25183317e21ccb2499c97d9afdff)#define NRF\_PERM\_R BIT(0)

[ 19](nordic-owned-memory_8h.md#a0c02f911d592b79403024ff6ae924dad)#define NRF\_PERM\_W BIT(1)

[ 21](nordic-owned-memory_8h.md#a5e9cae0aa74888ed91dd7c3ffef23ec2)#define NRF\_PERM\_X BIT(2)

[ 23](nordic-owned-memory_8h.md#a8e96aeef751fbb1c3bf2bdee474ea097)#define NRF\_PERM\_S BIT(3)

[ 25](nordic-owned-memory_8h.md#a758490f83493121bfc04445af185efed)#define NRF\_PERM\_NSC BIT(4)

26

30

36

[ 37](nordic-owned-memory_8h.md#ae977886b6f509bcda34b3864cf5b06e2)#define NRF\_PERM\_RW (NRF\_PERM\_R | NRF\_PERM\_W)

[ 38](nordic-owned-memory_8h.md#a7de269dc15b92b49d3b865cd00dcb66e)#define NRF\_PERM\_RX (NRF\_PERM\_R | NRF\_PERM\_X)

[ 39](nordic-owned-memory_8h.md#adbc1087aa45ce5a82562b76e703422f6)#define NRF\_PERM\_RS (NRF\_PERM\_R | NRF\_PERM\_S)

[ 40](nordic-owned-memory_8h.md#af7f291c2ca6d2c9366f123b229dcddeb)#define NRF\_PERM\_WX (NRF\_PERM\_W | NRF\_PERM\_X)

[ 41](nordic-owned-memory_8h.md#af7592990797753acf9e035e9a226b20a)#define NRF\_PERM\_WS (NRF\_PERM\_W | NRF\_PERM\_S)

[ 42](nordic-owned-memory_8h.md#a98ec396cd8e0918c730607ee100bf76c)#define NRF\_PERM\_XS (NRF\_PERM\_X | NRF\_PERM\_S)

[ 43](nordic-owned-memory_8h.md#a5e83619291670695a30b72232ba51d2d)#define NRF\_PERM\_RWX (NRF\_PERM\_R | NRF\_PERM\_W | NRF\_PERM\_X)

[ 44](nordic-owned-memory_8h.md#a0967ce2b4641901b0f002eb3d0134eed)#define NRF\_PERM\_RWS (NRF\_PERM\_R | NRF\_PERM\_W | NRF\_PERM\_S)

[ 45](nordic-owned-memory_8h.md#aee7d5b93a610deca9a6aa66314ed664c)#define NRF\_PERM\_RXS (NRF\_PERM\_R | NRF\_PERM\_X | NRF\_PERM\_S)

[ 46](nordic-owned-memory_8h.md#a4b8d7cae0009bbaa43b181389ae37d01)#define NRF\_PERM\_WXS (NRF\_PERM\_W | NRF\_PERM\_X | NRF\_PERM\_S)

[ 47](nordic-owned-memory_8h.md#a5ef62494ad09d23f0f2d35ffc7d7c91e)#define NRF\_PERM\_RWXS (NRF\_PERM\_R | NRF\_PERM\_W | NRF\_PERM\_X | NRF\_PERM\_S)

48

52

53#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESERVED\_MEMORY\_NORDIC\_OWNED\_MEMORY\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reserved-memory](dir_94de8f1f6a225c49dc7403fa9fb5eacb.md)
- [nordic-owned-memory.h](nordic-owned-memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
