---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__conn__mgr__connectivity__impl.html
original_path: doxygen/html/group__conn__mgr__connectivity__impl.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Connection Manager Connectivity Implementation API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Connection Manager Connectivity Implementation API.
[More...](#details)

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
| #define | [CONN\_MGR\_CONN\_DEFINE](#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)(conn\_id, conn\_api) |
|  | Define a conn\_mgr connectivity implementation that can be bound to network devices. |
| #define | [CONN\_MGR\_CONN\_DECLARE\_PUBLIC](#ga519cfa66e1a1f0b769ce2bf61a61887f)(conn\_id) |
|  | Helper macro to make a conn\_mgr connectivity implementation publicly available. |
| #define | [CONN\_MGR\_BIND\_CONN\_INST](#ga1ac9fb870cd2d698451d896113b723d1)(dev\_id, inst, conn\_id) |
|  | Associate a connectivity implementation with an existing network device instance. |
| #define | [CONN\_MGR\_BIND\_CONN](#ga16633bf29ebac6850b8c511b33bd189f)(dev\_id, conn\_id) |
|  | Associate a connectivity implementation with an existing network device. |

| Functions | |
| --- | --- |
| static struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* | [conn\_mgr\_if\_get\_binding](#ga5fc0ba9d7bf365352e665d1c9a055889) (struct [net\_if](structnet__if.md) \*iface) |
|  | Retrieves the conn\_mgr binding struct for a provided iface if it exists. |
| static void | [conn\_mgr\_binding\_lock](#ga27be6dec40356facce7da18a31a2c12a) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding) |
|  | Lock the passed-in binding, making it safe to access. |
| static void | [conn\_mgr\_binding\_unlock](#ga94a4930a6d7c4db4427dfdfad8f3c154) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding) |
|  | Unlocks the passed-in binding. |
| static void | [conn\_mgr\_binding\_set\_flag](#ga4f0f3244f48c5e0204faf8278c2bd94f) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set the value of the specified connectivity flag for the provided binding. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_binding\_get\_flag](#ga128931a6fabce79829af5aebecd59985) (struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag) |
|  | Check the value of the specified connectivity flag for the provided binding. |

## Detailed Description

Connection Manager Connectivity Implementation API.

## Macro Definition Documentation

## [◆ ](#ga16633bf29ebac6850b8c511b33bd189f)CONN\_MGR\_BIND\_CONN

| #define CONN\_MGR\_BIND\_CONN | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *conn\_id* ) |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

**Value:**

[CONN\_MGR\_BIND\_CONN\_INST](#ga1ac9fb870cd2d698451d896113b723d1)(dev\_id, 0, conn\_id)

[CONN\_MGR\_BIND\_CONN\_INST](#ga1ac9fb870cd2d698451d896113b723d1)

#define CONN\_MGR\_BIND\_CONN\_INST(dev\_id, inst, conn\_id)

Associate a connectivity implementation with an existing network device instance.

**Definition** conn\_mgr\_connectivity\_impl.h:211

Associate a connectivity implementation with an existing network device.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | conn\_id | Name of the connectivity implementation to associate. |

## [◆ ](#ga1ac9fb870cd2d698451d896113b723d1)CONN\_MGR\_BIND\_CONN\_INST

| #define CONN\_MGR\_BIND\_CONN\_INST | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *inst*, |
|  |  |  | *conn\_id* ) |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

**Value:**

[K\_MUTEX\_DEFINE](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)(CONN\_MGR\_CONN\_BINDING\_GET\_MUTEX(dev\_id, inst)); \

static CONN\_MGR\_CONN\_IMPL\_GET\_CTX\_TYPE(conn\_id) \

CONN\_MGR\_CONN\_BINDING\_GET\_DATA(dev\_id, inst); \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md), \

CONN\_MGR\_CONN\_BINDING\_GET\_NAME(dev\_id, inst)) = { \

.iface = NET\_IF\_GET(dev\_id, inst), \

.impl = &(CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id)), \

.ctx = &(CONN\_MGR\_CONN\_BINDING\_GET\_DATA(dev\_id, inst)), \

.mutex = &(CONN\_MGR\_CONN\_BINDING\_GET\_MUTEX(dev\_id, inst)) \

};

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[K\_MUTEX\_DEFINE](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)

#define K\_MUTEX\_DEFINE(name)

Statically define and initialize a mutex.

**Definition** kernel.h:2960

[conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md)

Connectivity Manager network interface binding structure.

**Definition** conn\_mgr\_connectivity\_impl.h:160

Associate a connectivity implementation with an existing network device instance.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | inst | Network device instance. |
    | conn\_id | Name of the connectivity implementation to associate. |

## [◆ ](#ga519cfa66e1a1f0b769ce2bf61a61887f)CONN\_MGR\_CONN\_DECLARE\_PUBLIC

| #define CONN\_MGR\_CONN\_DECLARE\_PUBLIC | ( |  | *conn\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

**Value:**

extern const struct [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md) CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id)

[conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md)

Connectivity Implementation struct.

**Definition** conn\_mgr\_connectivity\_impl.h:126

Helper macro to make a conn\_mgr connectivity implementation publicly available.

## [◆ ](#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)CONN\_MGR\_CONN\_DEFINE

| #define CONN\_MGR\_CONN\_DEFINE | ( |  | *conn\_id*, |
| --- | --- | --- | --- |
|  |  |  | *conn\_api* ) |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

**Value:**

const struct [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md) CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id) = { \

.api = conn\_api, \

};

Define a conn\_mgr connectivity implementation that can be bound to network devices.

Parameters
:   | conn\_id | The name of the new connectivity implementation |
    | --- | --- |
    | conn\_api | A pointer to a [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md "Connectivity Manager Connectivity API structure.") struct |

## Function Documentation

## [◆ ](#ga128931a6fabce79829af5aebecd59985)conn\_mgr\_binding\_get\_flag()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) conn\_mgr\_binding\_get\_flag | ( | struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* | *binding*, | | --- | --- | --- | --- | |  |  | enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) | *flag* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

Check the value of the specified connectivity flag for the provided binding.

Can be used from any thread or callback without calling [conn\_mgr\_binding\_lock](#ga27be6dec40356facce7da18a31a2c12a).

For use only by connectivity implementations

Parameters
:   | binding | The binding to check |
    | --- | --- |
    | flag | The flag to check |

Returns
:   bool The value of the specified flag

## [◆ ](#ga27be6dec40356facce7da18a31a2c12a)conn\_mgr\_binding\_lock()

| | void conn\_mgr\_binding\_lock | ( | struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* | *binding* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

Lock the passed-in binding, making it safe to access.

Call this whenever accessing binding data, unless inside a [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md "Connectivity Manager Connectivity API structure.") callback, where it is called automatically by conn\_mgr.

Reentrant.

For use only by connectivity implementations.

Parameters
:   | binding | - Binding to lock |
    | --- | --- |

## [◆ ](#ga4f0f3244f48c5e0204faf8278c2bd94f)conn\_mgr\_binding\_set\_flag()

| | void conn\_mgr\_binding\_set\_flag | ( | struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* | *binding*, | | --- | --- | --- | --- | |  |  | enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) | *flag*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

Set the value of the specified connectivity flag for the provided binding.

Can be used from any thread or callback without calling [conn\_mgr\_binding\_lock](#ga27be6dec40356facce7da18a31a2c12a).

For use only by connectivity implementations

Parameters
:   | binding | The binding to check |
    | --- | --- |
    | flag | The flag to check |
    | value | New value for the specified flag |

## [◆ ](#ga94a4930a6d7c4db4427dfdfad8f3c154)conn\_mgr\_binding\_unlock()

| | void conn\_mgr\_binding\_unlock | ( | struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* | *binding* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

Unlocks the passed-in binding.

Call this after any call to [conn\_mgr\_binding\_lock](#ga27be6dec40356facce7da18a31a2c12a) once done accessing binding data.

Reentrant.

For use only by connectivity implementations.

Parameters
:   | binding | - Binding to unlock |
    | --- | --- |

## [◆ ](#ga5fc0ba9d7bf365352e665d1c9a055889)conn\_mgr\_if\_get\_binding()

| | struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \* conn\_mgr\_if\_get\_binding | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity_impl.h](conn__mgr__connectivity__impl_8h.md)>`

Retrieves the conn\_mgr binding struct for a provided iface if it exists.

Bindings for connectivity implementations with missing API structs are ignored.

For use only by connectivity implementations.

Parameters
:   | iface | - bound network interface to obtain the binding struct for. |
    | --- | --- |

Returns
:   struct conn\_mgr\_conn\_binding\* Pointer to the retrieved binding struct if it exists, NULL otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
