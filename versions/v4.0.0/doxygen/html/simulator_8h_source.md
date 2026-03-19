---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/simulator_8h_source.html
original_path: doxygen/html/simulator_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

simulator.h

[Go to the documentation of this file.](simulator_8h.md)

1/\*

2 \* Copyright (c) 2020 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_SIMULATOR\_H\_

8#define ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_SIMULATOR\_H\_

9

15

16/\* For ec\_host\_cmd\_backend\_api\_send function pointer type \*/

17#include <[zephyr/mgmt/ec\_host\_cmd/backend.h](backend_8h.md)>

18

[ 31](simulator_8h.md#a4ed1a006639d068f95732a1d30ba001b)void [ec\_host\_cmd\_backend\_sim\_install\_send\_cb](simulator_8h.md#a4ed1a006639d068f95732a1d30ba001b)([ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5) cb,

32 struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*\*tx\_buf);

33

[ 46](simulator_8h.md#aecf09d7134542c3bec94c131136c1f40)int [ec\_host\_cmd\_backend\_sim\_data\_received](simulator_8h.md#aecf09d7134542c3bec94c131136c1f40)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t len);

47

48#endif /\* ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_SIMULATOR\_H\_ \*/

[backend.h](backend_8h.md)

Public APIs for Host Command backends that respond to host commands.

[ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)

int(\* ec\_host\_cmd\_backend\_api\_send)(const struct ec\_host\_cmd\_backend \*backend)

Sends data to the host.

**Definition** backend.h:104

[ec\_host\_cmd\_backend\_sim\_install\_send\_cb](simulator_8h.md#a4ed1a006639d068f95732a1d30ba001b)

void ec\_host\_cmd\_backend\_sim\_install\_send\_cb(ec\_host\_cmd\_backend\_api\_send cb, struct ec\_host\_cmd\_tx\_buf \*\*tx\_buf)

Install callback for when this device would sends data to host.

[ec\_host\_cmd\_backend\_sim\_data\_received](simulator_8h.md#aecf09d7134542c3bec94c131136c1f40)

int ec\_host\_cmd\_backend\_sim\_data\_received(const uint8\_t \*buffer, size\_t len)

Simulate receiving data from host as passed in to this function.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md)

Context for host command backend and handler to pass tx data.

**Definition** backend.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [ec\_host\_cmd](dir_d53ada025add0f463456d44507c0d96c.md)
- [simulator.h](simulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
