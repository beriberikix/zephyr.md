---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ptm_8h_source.html
original_path: doxygen/html/ptm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptm.h

[Go to the documentation of this file.](ptm_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_PTM\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_PTM\_H\_

10

17

18#include <stddef.h>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 31](group__pcie__host__ptm__interface.md#gae868e8140938c293ad5685cd77131924)bool [pcie\_ptm\_enable](group__pcie__host__ptm__interface.md#gae868e8140938c293ad5685cd77131924)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf);

32

33#ifdef \_\_cplusplus

34}

35#endif

36

40

41#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_PTM\_H\_ \*/

[pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)

uint32\_t pcie\_bdf\_t

A unique PCI(e) endpoint (bus, device, function).

**Definition** pcie.h:37

[pcie\_ptm\_enable](group__pcie__host__ptm__interface.md#gae868e8140938c293ad5685cd77131924)

bool pcie\_ptm\_enable(pcie\_bdf\_t bdf)

Enable PTM on endpoint.

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [ptm.h](ptm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
