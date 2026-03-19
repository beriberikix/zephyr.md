---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/system__timer_8h_source.html
original_path: doxygen/html/system__timer_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

system\_timer.h

[Go to the documentation of this file.](system__timer_8h.md)

1/\*

2 \* Copyright (c) 2015 Wind River Systems, Inc.

3 \* Copyright (c) 2019 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SYSTEM\_TIMER\_H\_

16#define ZEPHYR\_INCLUDE\_DRIVERS\_SYSTEM\_TIMER\_H\_

17

18#include <[stdbool.h](stdbool_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

30

[ 73](group__clock__apis.md#ga747c1f4a99a3bc48e7ec65d7bc5e4767)void [sys\_clock\_set\_timeout](group__clock__apis.md#ga747c1f4a99a3bc48e7ec65d7bc5e4767)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks, bool idle);

74

[ 87](group__clock__apis.md#ga6ca2139000b8c75b1ed2c6c1f672ff79)void [sys\_clock\_idle\_exit](group__clock__apis.md#ga6ca2139000b8c75b1ed2c6c1f672ff79)(void);

88

[ 100](group__clock__apis.md#gaa7d3b1bdb8d15c907aaafea3b96ac2b5)void [sys\_clock\_announce](group__clock__apis.md#gaa7d3b1bdb8d15c907aaafea3b96ac2b5)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks);

101

[ 110](group__clock__apis.md#gaa9b6d8eebc69d2808beb0580d974bb84)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_elapsed](group__clock__apis.md#gaa9b6d8eebc69d2808beb0580d974bb84)(void);

111

[ 119](group__clock__apis.md#ga49c900ab49a72c347d0aefb14aecb550)void [sys\_clock\_disable](group__clock__apis.md#ga49c900ab49a72c347d0aefb14aecb550)(void);

120

[ 142](group__clock__apis.md#ga42dcd1878309a82246dbfa26510f868a)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](group__clock__apis.md#ga42dcd1878309a82246dbfa26510f868a)(void);

143

[ 161](group__clock__apis.md#ga25328a181bd0229ef5110c15e8452fc1)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](group__clock__apis.md#ga25328a181bd0229ef5110c15e8452fc1)(void);

162

166

167#ifdef \_\_cplusplus

168}

169#endif

170

171#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SYSTEM\_TIMER\_H\_ \*/

[sys\_clock\_cycle\_get\_64](group__clock__apis.md#ga25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

64 bit hardware cycle counter

[sys\_clock\_cycle\_get\_32](group__clock__apis.md#ga42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

Hardware cycle counter.

[sys\_clock\_disable](group__clock__apis.md#ga49c900ab49a72c347d0aefb14aecb550)

void sys\_clock\_disable(void)

Disable system timer.

[sys\_clock\_idle\_exit](group__clock__apis.md#ga6ca2139000b8c75b1ed2c6c1f672ff79)

void sys\_clock\_idle\_exit(void)

Timer idle exit notification.

[sys\_clock\_set\_timeout](group__clock__apis.md#ga747c1f4a99a3bc48e7ec65d7bc5e4767)

void sys\_clock\_set\_timeout(int32\_t ticks, bool idle)

Set system clock timeout.

[sys\_clock\_announce](group__clock__apis.md#gaa7d3b1bdb8d15c907aaafea3b96ac2b5)

void sys\_clock\_announce(int32\_t ticks)

Announce time progress to the kernel.

[sys\_clock\_elapsed](group__clock__apis.md#gaa9b6d8eebc69d2808beb0580d974bb84)

uint32\_t sys\_clock\_elapsed(void)

Ticks elapsed since last sys\_clock\_announce() call.

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [system\_timer.h](system__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
