---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwdt__window.html
original_path: doxygen/html/structwdt__window.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wdt\_window Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Watchdog Interface](group__watchdog__interface.md)

Watchdog timeout window.
[More...](#details)

`#include <[watchdog.h](watchdog_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [min](#a4e5be19373804f900aa9c1d925f0aace) |
|  | Lower limit of watchdog feed timeout in milliseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max](#a21195de2e42f9a183a1aba0fb0732572) |
|  | Upper limit of watchdog feed timeout in milliseconds. |

## Detailed Description

Watchdog timeout window.

Each installed timeout needs feeding within the specified time window, otherwise the watchdog will trigger. If the watchdog instance does not support window timeouts then min value must be equal to 0.

Note
:   If specified values can not be precisely set they are always rounded up.

## Field Documentation

## [◆ ](#a21195de2e42f9a183a1aba0fb0732572)max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wdt\_window::max |
| --- |

Upper limit of watchdog feed timeout in milliseconds.

## [◆ ](#a4e5be19373804f900aa9c1d925f0aace)min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wdt\_window::min |
| --- |

Lower limit of watchdog feed timeout in milliseconds.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[watchdog.h](watchdog_8h_source.md)

- [wdt\_window](structwdt__window.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
