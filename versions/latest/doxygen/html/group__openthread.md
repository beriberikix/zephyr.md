---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__openthread.html
original_path: doxygen/html/group__openthread.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

OpenThread stack

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md)

OpenThread stack public header.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) |
|  | OpenThread state change callback. [More...](structopenthread__state__changed__cb.md#details) |

| Functions | |
| --- | --- |
| int | [openthread\_state\_changed\_cb\_register](#ga46471bc0ccdf1f953b81dd9720883327) (struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb) |
|  | Registers callbacks which will be called when certain configuration or state changes occur within OpenThread. |
| int | [openthread\_state\_changed\_cb\_unregister](#ga89eaabc16f6feb84b61f97c5e5cac764) (struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb) |
|  | Unregisters OpenThread configuration or state changed callbacks. |
| struct openthread\_context \* | [openthread\_get\_default\_context](#gad975528c91de66cd1054f3584bfcc957) (void) |
|  | Get pointer to default OpenThread context. |
| int | [openthread\_start](#ga4674b60779f2fd0adaa9c96afb840265) (struct openthread\_context \*ot\_context) |
|  | Starts the OpenThread network. |
| void | [openthread\_api\_mutex\_lock](#ga1f702bb5768795bce5561efe457b1028) (struct openthread\_context \*ot\_context) |
|  | Lock internal mutex before accessing OT API. |
| int | [openthread\_api\_mutex\_try\_lock](#ga05c5792a8d2ceaf93336f62760c74862) (struct openthread\_context \*ot\_context) |
|  | Try to lock internal mutex before accessing OT API. |
| void | [openthread\_api\_mutex\_unlock](#ga0c3cb86690f2b1b714ad655b7df23bf3) (struct openthread\_context \*ot\_context) |
|  | Unlock internal mutex after accessing OT API. |

## Detailed Description

OpenThread stack public header.

Since
:   1.11

Version
:   0.8.0

## Function Documentation

## [◆ ](#ga1f702bb5768795bce5561efe457b1028)openthread\_api\_mutex\_lock()

| void openthread\_api\_mutex\_lock | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Lock internal mutex before accessing OT API.

**[Deprecated](deprecated.md#_deprecated000023)**
:   use [openthread\_mutex\_lock](modules_2openthread_2include_2openthread_8h.md#ae3945bc3549118dc5420f9859588282d "openthread_mutex_lock").

OpenThread API is not thread-safe, therefore before accessing any API function, it's needed to lock the internal mutex, to prevent the OpenThread thread from preempting the API call.

Parameters
:   | ot\_context | Context to lock. |
    | --- | --- |

## [◆ ](#ga05c5792a8d2ceaf93336f62760c74862)openthread\_api\_mutex\_try\_lock()

| int openthread\_api\_mutex\_try\_lock | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Try to lock internal mutex before accessing OT API.

**[Deprecated](deprecated.md#_deprecated000024)**
:   use [openthread\_mutex\_try\_lock](modules_2openthread_2include_2openthread_8h.md#ab5669622dfd83d3a5175fa47325dade3 "openthread_mutex_try_lock") instead.

This function behaves like [openthread\_api\_mutex\_lock()](#ga1f702bb5768795bce5561efe457b1028) provided that the internal mutex is unlocked. Otherwise, it exists immediately and returns a negative value.

Parameters
:   | ot\_context | Context to lock. |
    | --- | --- |

Return values
:   | 0 | On success. |
    | --- | --- |
    | <0 | On failure. |

## [◆ ](#ga0c3cb86690f2b1b714ad655b7df23bf3)openthread\_api\_mutex\_unlock()

| void openthread\_api\_mutex\_unlock | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Unlock internal mutex after accessing OT API.

**[Deprecated](deprecated.md#_deprecated000025)**
:   use [openthread\_mutex\_unlock](modules_2openthread_2include_2openthread_8h.md#a420c3321272141f63ea86166b84ec845 "openthread_mutex_unlock") instead.

Parameters
:   | ot\_context | Context to unlock. |
    | --- | --- |

## [◆ ](#gad975528c91de66cd1054f3584bfcc957)openthread\_get\_default\_context()

| struct openthread\_context \* openthread\_get\_default\_context | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Get pointer to default OpenThread context.

Return values
:   | !NULL | On success. |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | On failure. |

## [◆ ](#ga4674b60779f2fd0adaa9c96afb840265)openthread\_start()

| int openthread\_start | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Starts the OpenThread network.

**[Deprecated](deprecated.md#_deprecated000022)**
:   use [openthread\_run](modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392 "openthread_run") instead.

Depends on active settings: it uses stored network configuration, start joining procedure or uses default network configuration. Additionally when the device is MTD, it sets the SED mode to properly attach the network.

Parameters
:   | ot\_context |  |
    | --- | --- |

## [◆ ](#ga46471bc0ccdf1f953b81dd9720883327)openthread\_state\_changed\_cb\_register()

| int openthread\_state\_changed\_cb\_register | ( | struct openthread\_context \* | *ot\_context*, |
| --- | --- | --- | --- |
|  |  | struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \* | *cb* ) |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Registers callbacks which will be called when certain configuration or state changes occur within OpenThread.

**[Deprecated](deprecated.md#_deprecated000020)**
:   use [openthread\_state\_changed\_callback\_register](modules_2openthread_2include_2openthread_8h.md#a4178b72288585869e2c941acdc21db57 "openthread_state_changed_callback_register") instead.

Parameters
:   | ot\_context | the OpenThread context to register the callback with. |
    | --- | --- |
    | cb | callback struct to register. |

## [◆ ](#ga89eaabc16f6feb84b61f97c5e5cac764)openthread\_state\_changed\_cb\_unregister()

| int openthread\_state\_changed\_cb\_unregister | ( | struct openthread\_context \* | *ot\_context*, |
| --- | --- | --- | --- |
|  |  | struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \* | *cb* ) |

`#include <[zephyr/net/openthread.h](include_2zephyr_2net_2openthread_8h.md)>`

Unregisters OpenThread configuration or state changed callbacks.

**[Deprecated](deprecated.md#_deprecated000021)**
:   use [openthread\_state\_changed\_callback\_unregister](modules_2openthread_2include_2openthread_8h.md#ae4ad25613f8eada1a0a29426a2f4a518 "openthread_state_changed_callback_unregister") instead.

Parameters
:   | ot\_context | the OpenThread context to unregister the callback from. |
    | --- | --- |
    | cb | callback struct to unregister. |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
