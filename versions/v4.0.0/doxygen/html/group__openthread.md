---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__openthread.html
original_path: doxygen/html/group__openthread.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

OpenThread L2 abstraction layer

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md)

OpenThread Layer 2 abstraction layer.
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
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [openthread\_thread\_id\_get](#ga9499c4c69a0094f0b7ef803ac05fb19a) (void) |
|  | Get OpenThread thread identification. |
| struct openthread\_context \* | [openthread\_get\_default\_context](#gad975528c91de66cd1054f3584bfcc957) (void) |
|  | Get pointer to default OpenThread context. |
| struct otInstance \* | [openthread\_get\_default\_instance](#ga517a538fa32afac8ca8968ada2cea89d) (void) |
|  | Get pointer to default OpenThread instance. |
| int | [openthread\_start](#ga4674b60779f2fd0adaa9c96afb840265) (struct openthread\_context \*ot\_context) |
|  | Starts the OpenThread network. |
| void | [openthread\_api\_mutex\_lock](#ga1f702bb5768795bce5561efe457b1028) (struct openthread\_context \*ot\_context) |
|  | Lock internal mutex before accessing OT API. |
| int | [openthread\_api\_mutex\_try\_lock](#ga05c5792a8d2ceaf93336f62760c74862) (struct openthread\_context \*ot\_context) |
|  | Try to lock internal mutex before accessing OT API. |
| void | [openthread\_api\_mutex\_unlock](#ga0c3cb86690f2b1b714ad655b7df23bf3) (struct openthread\_context \*ot\_context) |
|  | Unlock internal mutex after accessing OT API. |

## Detailed Description

OpenThread Layer 2 abstraction layer.

Since
:   1.11

Version
:   0.8.0

## Function Documentation

## [◆ ](#ga1f702bb5768795bce5561efe457b1028)openthread\_api\_mutex\_lock()

| void openthread\_api\_mutex\_lock | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[openthread.h](openthread_8h.md)>`

Lock internal mutex before accessing OT API.

OpenThread API is not thread-safe, therefore before accessing any API function, it's needed to lock the internal mutex, to prevent the OpenThread thread from preempting the API call.

Parameters
:   | ot\_context | Context to lock. |
    | --- | --- |

## [◆ ](#ga05c5792a8d2ceaf93336f62760c74862)openthread\_api\_mutex\_try\_lock()

| int openthread\_api\_mutex\_try\_lock | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[openthread.h](openthread_8h.md)>`

Try to lock internal mutex before accessing OT API.

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

`#include <[openthread.h](openthread_8h.md)>`

Unlock internal mutex after accessing OT API.

Parameters
:   | ot\_context | Context to unlock. |
    | --- | --- |

## [◆ ](#gad975528c91de66cd1054f3584bfcc957)openthread\_get\_default\_context()

| struct openthread\_context \* openthread\_get\_default\_context | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[openthread.h](openthread_8h.md)>`

Get pointer to default OpenThread context.

Return values
:   | !NULL | On success. |
    | --- | --- |
    | NULL | On failure. |

## [◆ ](#ga517a538fa32afac8ca8968ada2cea89d)openthread\_get\_default\_instance()

| struct otInstance \* openthread\_get\_default\_instance | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[openthread.h](openthread_8h.md)>`

Get pointer to default OpenThread instance.

Return values
:   | !NULL | On success. |
    | --- | --- |
    | NULL | On failure. |

## [◆ ](#ga4674b60779f2fd0adaa9c96afb840265)openthread\_start()

| int openthread\_start | ( | struct openthread\_context \* | *ot\_context* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[openthread.h](openthread_8h.md)>`

Starts the OpenThread network.

Depends on active settings: it uses stored network configuration, start joining procedure or uses default network configuration. Additionally when the device is MTD, it sets the SED mode to properly attach the network.

Parameters
:   | ot\_context |  |
    | --- | --- |

## [◆ ](#ga46471bc0ccdf1f953b81dd9720883327)openthread\_state\_changed\_cb\_register()

| int openthread\_state\_changed\_cb\_register | ( | struct openthread\_context \* | *ot\_context*, |
| --- | --- | --- | --- |
|  |  | struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \* | *cb* ) |

`#include <[openthread.h](openthread_8h.md)>`

Registers callbacks which will be called when certain configuration or state changes occur within OpenThread.

Parameters
:   | ot\_context | the OpenThread context to register the callback with. |
    | --- | --- |
    | cb | callback struct to register. |

## [◆ ](#ga89eaabc16f6feb84b61f97c5e5cac764)openthread\_state\_changed\_cb\_unregister()

| int openthread\_state\_changed\_cb\_unregister | ( | struct openthread\_context \* | *ot\_context*, |
| --- | --- | --- | --- |
|  |  | struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \* | *cb* ) |

`#include <[openthread.h](openthread_8h.md)>`

Unregisters OpenThread configuration or state changed callbacks.

Parameters
:   | ot\_context | the OpenThread context to unregister the callback from. |
    | --- | --- |
    | cb | callback struct to unregister. |

## [◆ ](#ga9499c4c69a0094f0b7ef803ac05fb19a)openthread\_thread\_id\_get()

| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) openthread\_thread\_id\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[openthread.h](openthread_8h.md)>`

Get OpenThread thread identification.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
