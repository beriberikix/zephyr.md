---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/connectivity__wifi__mgmt_8h_source.html
original_path: doxygen/html/connectivity__wifi__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

connectivity\_wifi\_mgmt.h

[Go to the documentation of this file.](connectivity__wifi__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2024 CSIRO

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_WIFI\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_WIFI\_MGMT\_H\_

14

15#include <[zephyr/net/conn\_mgr\_connectivity\_impl.h](conn__mgr__connectivity__impl_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 24](connectivity__wifi__mgmt_8h.md#aa8d1b34502bfcc5c482265148a3bb67a)#define CONNECTIVITY\_WIFI\_MGMT\_CTX\_TYPE void \*

25

[ 31](connectivity__wifi__mgmt_8h.md#a0c5f4f4ce3091c0a6e43292b095f7be3)#define CONNECTIVITY\_WIFI\_MGMT\_BIND(dev\_id) \

32 IF\_ENABLED(CONFIG\_NET\_CONNECTION\_MANAGER\_CONNECTIVITY\_WIFI\_MGMT, \

33 (CONN\_MGR\_CONN\_DECLARE\_PUBLIC(CONNECTIVITY\_WIFI\_MGMT); \

34 CONN\_MGR\_BIND\_CONN(dev\_id, CONNECTIVITY\_WIFI\_MGMT)))

35

36#ifdef \_\_cplusplus

37}

38#endif

39

40#endif /\* ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_WIFI\_MGMT\_H\_ \*/

[conn\_mgr\_connectivity\_impl.h](conn__mgr__connectivity__impl_8h.md)

API for defining conn\_mgr connectivity implementations (allowing ifaces to be used with conn\_mgr\_conn...

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr](dir_ba7fd4b3ea28c88570c49772975cd824.md)
- [connectivity\_wifi\_mgmt.h](connectivity__wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
