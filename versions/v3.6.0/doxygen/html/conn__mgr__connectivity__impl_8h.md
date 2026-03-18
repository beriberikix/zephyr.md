---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/conn__mgr__connectivity__impl_8h.html
original_path: doxygen/html/conn__mgr__connectivity__impl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_connectivity\_impl.h File Reference

API for defining conn\_mgr connectivity implementations (allowing ifaces to be used with conn\_mgr\_connectivity).
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`  
`#include <[zephyr/net/conn_mgr_connectivity.h](conn__mgr__connectivity_8h_source.md)>`

[Go to the source code of this file.](conn__mgr__connectivity__impl_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md) |
|  | Connectivity Manager Connectivity API structure. [More...](structconn__mgr__conn__api.md#details) |
| struct | [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md) |
|  | Connectivity Implementation struct. [More...](structconn__mgr__conn__impl.md#details) |
| struct | [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) |
|  | Connectivity Manager network interface binding structure. [More...](structconn__mgr__conn__binding.md#details) |

| Macros | |
| --- | --- |
| #define | [CONN\_MGR\_CONN\_DEFINE](group__conn__mgr__connectivity__impl.md#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)(conn\_id, conn\_api) |
|  | Define a conn\_mgr connectivity implementation that can be bound to network devices. |
| #define | [CONN\_MGR\_CONN\_DECLARE\_PUBLIC](group__conn__mgr__connectivity__impl.md#ga519cfa66e1a1f0b769ce2bf61a61887f)(conn\_id) |
|  | Helper macro to make a conn\_mgr connectivity implementation publicly available. |
| #define | [CONN\_MGR\_BIND\_CONN\_INST](group__conn__mgr__connectivity__impl.md#ga1ac9fb870cd2d698451d896113b723d1)(dev\_id, inst, conn\_id) |
|  | Associate a connectivity implementation with an existing network device instance. |
| #define | [CONN\_MGR\_BIND\_CONN](group__conn__mgr__connectivity__impl.md#ga16633bf29ebac6850b8c511b33bd189f)(dev\_id, conn\_id) |
|  | Associate a connectivity implementation with an existing network device. |

| Functions | |
| --- | --- |
| static struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* | [conn\_mgr\_if\_get\_binding](group__conn__mgr__connectivity__impl.md#ga5fc0ba9d7bf365352e665d1c9a055889) (struct [net\_if](structnet__if.md) \*iface) |
|  | Retrieves the conn\_mgr binding struct for a provided iface if it exists. |
| static void | [conn\_mgr\_binding\_lock](group__conn__mgr__connectivity__impl.md#ga27be6dec40356facce7da18a31a2c12a) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding) |
|  | Lock the passed-in binding, making it safe to access. |
| static void | [conn\_mgr\_binding\_unlock](group__conn__mgr__connectivity__impl.md#ga94a4930a6d7c4db4427dfdfad8f3c154) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding) |
|  | Unlocks the passed-in binding. |
| static void | [conn\_mgr\_binding\_set\_flag](group__conn__mgr__connectivity__impl.md#ga4f0f3244f48c5e0204faf8278c2bd94f) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set the value of the specified connectivity flag for the provided binding. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_binding\_get\_flag](group__conn__mgr__connectivity__impl.md#ga128931a6fabce79829af5aebecd59985) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag) |
|  | Check the value of the specified connectivity flag for the provided binding. |

## Detailed Description

API for defining conn\_mgr connectivity implementations (allowing ifaces to be used with conn\_mgr\_connectivity).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_connectivity\_impl.h](conn__mgr__connectivity__impl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
