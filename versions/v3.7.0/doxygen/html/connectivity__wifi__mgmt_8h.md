---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/connectivity__wifi__mgmt_8h.html
original_path: doxygen/html/connectivity__wifi__mgmt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

connectivity\_wifi\_mgmt.h File Reference

Connectivity implementation for drivers exposing the wifi\_mgmt API.
[More...](#details)

`#include <[zephyr/net/conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h_source.md)>`

[Go to the source code of this file.](connectivity__wifi__mgmt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CONNECTIVITY\_WIFI\_MGMT\_CTX\_TYPE](#aa8d1b34502bfcc5c482265148a3bb67a)   void \* |
|  | Context type for generic WIFI\_MGMT connectivity backend. |
| #define | [CONNECTIVITY\_WIFI\_MGMT\_BIND](#a0c5f4f4ce3091c0a6e43292b095f7be3)(dev\_id) |
|  | Associate the generic WIFI\_MGMT implementation with a network device. |

## Detailed Description

Connectivity implementation for drivers exposing the wifi\_mgmt API.

## Macro Definition Documentation

## [◆ ](#a0c5f4f4ce3091c0a6e43292b095f7be3)CONNECTIVITY\_WIFI\_MGMT\_BIND

| #define CONNECTIVITY\_WIFI\_MGMT\_BIND | ( |  | *dev\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_NET\_CONNECTION\_MANAGER\_CONNECTIVITY\_WIFI\_MGMT, \

([CONN\_MGR\_CONN\_DECLARE\_PUBLIC](group__conn__mgr__connectivity__impl.md#ga519cfa66e1a1f0b769ce2bf61a61887f)(CONNECTIVITY\_WIFI\_MGMT); \

CONN\_MGR\_BIND\_CONN(dev\_id, CONNECTIVITY\_WIFI\_MGMT)))

[CONN\_MGR\_CONN\_DECLARE\_PUBLIC](group__conn__mgr__connectivity__impl.md#ga519cfa66e1a1f0b769ce2bf61a61887f)

#define CONN\_MGR\_CONN\_DECLARE\_PUBLIC(conn\_id)

Helper macro to make a conn\_mgr connectivity implementation publicly available.

**Definition** conn\_mgr\_connectivity\_impl.h:145

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:223

Associate the generic WIFI\_MGMT implementation with a network device.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |

## [◆ ](#aa8d1b34502bfcc5c482265148a3bb67a)CONNECTIVITY\_WIFI\_MGMT\_CTX\_TYPE

| #define CONNECTIVITY\_WIFI\_MGMT\_CTX\_TYPE   void \* |
| --- |

Context type for generic WIFI\_MGMT connectivity backend.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr](dir_ba7fd4b3ea28c88570c49772975cd824.md)
- [connectivity\_wifi\_mgmt.h](connectivity__wifi__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
