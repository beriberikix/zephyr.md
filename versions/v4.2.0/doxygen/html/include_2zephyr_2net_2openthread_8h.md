---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2net_2openthread_8h.html
original_path: doxygen/html/include_2zephyr_2net_2openthread_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread.h File Reference

OpenThread stack public header.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/kernel/thread.h](kernel_2thread_8h_source.md)>`  
`#include <[openthread.h](include_2zephyr_2net_2openthread_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2net_2openthread_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) |
|  | OpenThread state change callback. [More...](structopenthread__state__changed__cb.md#details) |

| Functions | |
| --- | --- |
| int | [openthread\_state\_changed\_cb\_register](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327) (struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb) |
|  | Registers callbacks which will be called when certain configuration or state changes occur within OpenThread. |
| int | [openthread\_state\_changed\_cb\_unregister](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764) (struct openthread\_context \*ot\_context, struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb) |
|  | Unregisters OpenThread configuration or state changed callbacks. |
| struct openthread\_context \* | [openthread\_get\_default\_context](group__openthread.md#gad975528c91de66cd1054f3584bfcc957) (void) |
|  | Get pointer to default OpenThread context. |
| int | [openthread\_start](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265) (struct openthread\_context \*ot\_context) |
|  | Starts the OpenThread network. |
| void | [openthread\_api\_mutex\_lock](group__openthread.md#ga1f702bb5768795bce5561efe457b1028) (struct openthread\_context \*ot\_context) |
|  | Lock internal mutex before accessing OT API. |
| int | [openthread\_api\_mutex\_try\_lock](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862) (struct openthread\_context \*ot\_context) |
|  | Try to lock internal mutex before accessing OT API. |
| void | [openthread\_api\_mutex\_unlock](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3) (struct openthread\_context \*ot\_context) |
|  | Unlock internal mutex after accessing OT API. |

## Detailed Description

OpenThread stack public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [openthread.h](include_2zephyr_2net_2openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
