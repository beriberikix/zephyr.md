---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mdns__responder_8h_source.html
original_path: doxygen/html/mdns__responder_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mdns\_responder.h

[Go to the documentation of this file.](mdns__responder_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_NET\_MDNS\_RESPONDER\_H\_

15#define ZEPHYR\_INCLUDE\_NET\_MDNS\_RESPONDER\_H\_

16

17#include <stddef.h>

18#include <[zephyr/net/dns\_sd.h](dns__sd_8h.md)>

19

[ 32](mdns__responder_8h.md#a4682ee30bf3e739790dbcaede5485777)int [mdns\_responder\_set\_ext\_records](mdns__responder_8h.md#a4682ee30bf3e739790dbcaede5485777)(const struct [dns\_sd\_rec](structdns__sd__rec.md) \*records, size\_t count);

33

34#endif /\* ZEPHYR\_INCLUDE\_NET\_MDNS\_RESPONDER\_H\_ \*/

[dns\_sd.h](dns__sd_8h.md)

DNS Service Discovery.

[mdns\_responder\_set\_ext\_records](mdns__responder_8h.md#a4682ee30bf3e739790dbcaede5485777)

int mdns\_responder\_set\_ext\_records(const struct dns\_sd\_rec \*records, size\_t count)

Register continuous memory of dns\_sd\_rec records.

[dns\_sd\_rec](structdns__sd__rec.md)

DNS Service Discovery record.

**Definition** dns\_sd.h:215

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mdns\_responder.h](mdns__responder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
