---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__retained__mem_8h_source.html
original_path: doxygen/html/nrf__retained__mem_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_retained\_mem.h

[Go to the documentation of this file.](nrf__retained__mem_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RETAINED\_MEM\_NRF\_RETAINED\_MEM\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_RETAINED\_MEM\_NRF\_RETAINED\_MEM\_H

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

14#include <[zephyr/drivers/retained\_mem.h](retained__mem_8h.md)>

15

16#if defined(CONFIG\_RETAINED\_MEM\_NRF\_RAM\_CTRL) || defined(\_\_DOXYGEN\_\_)

24int z\_nrf\_retained\_mem\_retention\_apply(void);

25#else

26static inline int z\_nrf\_retained\_mem\_retention\_apply(void)

27{

28 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

29}

30#endif

31

32#ifdef \_\_cplusplus

33}

34#endif

35

36#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RETAINED\_MEM\_NRF\_RETAINED\_MEM\_H \*/

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[retained\_mem.h](retained__mem_8h.md)

Public API for retained memory drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [retained\_mem](dir_aa4ea4b27572691bd7ae1b50e1d0a1cc.md)
- [nrf\_retained\_mem.h](nrf__retained__mem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
