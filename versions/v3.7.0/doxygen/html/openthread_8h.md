---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/openthread_8h.html
original_path: doxygen/html/openthread_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread.h File Reference

OpenThread L2 stack public header.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <openthread/instance.h>`

[Go to the source code of this file.](openthread_8h_source.md)

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
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [openthread\_thread\_id\_get](group__openthread.md#ga9499c4c69a0094f0b7ef803ac05fb19a) (void) |
|  | Get OpenThread thread identification. |
| struct openthread\_context \* | [openthread\_get\_default\_context](group__openthread.md#gad975528c91de66cd1054f3584bfcc957) (void) |
|  | Get pointer to default OpenThread context. |
| struct otInstance \* | [openthread\_get\_default\_instance](group__openthread.md#ga517a538fa32afac8ca8968ada2cea89d) (void) |
|  | Get pointer to default OpenThread instance. |
| int | [openthread\_start](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265) (struct openthread\_context \*ot\_context) |
|  | Starts the OpenThread network. |
| void | [openthread\_api\_mutex\_lock](group__openthread.md#ga1f702bb5768795bce5561efe457b1028) (struct openthread\_context \*ot\_context) |
|  | Lock internal mutex before accessing OT API. |
| int | [openthread\_api\_mutex\_try\_lock](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862) (struct openthread\_context \*ot\_context) |
|  | Try to lock internal mutex before accessing OT API. |
| void | [openthread\_api\_mutex\_unlock](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3) (struct openthread\_context \*ot\_context) |
|  | Unlock internal mutex after accessing OT API. |

## Detailed Description

OpenThread L2 stack public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [openthread.h](openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
