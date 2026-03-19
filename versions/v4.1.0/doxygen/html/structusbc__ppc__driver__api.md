---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbc__ppc__driver__api.html
original_path: doxygen/html/structusbc__ppc__driver__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_ppc\_driver\_api Struct Reference

Structure with pointers to the functions implemented by driver.
[More...](#details)

`#include <[usbc_ppc.h](usbc__ppc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [is\_dead\_battery\_mode](#a832320573b2adab1d748e5e761690733) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [exit\_dead\_battery\_mode](#a4ba2f654765130d5562f56243967bf58) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [is\_vbus\_source](#aab74a38a9c055efdfd0198143f12c9ff) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [is\_vbus\_sink](#a93b91d21d4d2edda1d457f4144800f37) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [set\_snk\_ctrl](#af4a66a11b66d48818123434c59553f0d) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_src\_ctrl](#a20ddefaee68808414f4075cc513a8660) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_vbus\_discharge](#a1c2c21070ee18b7b5df09a6b6ed618b6) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [is\_vbus\_present](#a8bf73dee9ba920f1b426038f62d5c9db) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [set\_event\_handler](#a8f82ae3af5452d9cd0852bf15fcab573) )(const struct [device](structdevice.md) \*dev, [usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data) |
| int(\* | [dump\_regs](#adce51ae345d5fc417f3767476af36276) )(const struct [device](structdevice.md) \*dev) |

## Detailed Description

Structure with pointers to the functions implemented by driver.

## Field Documentation

## [◆ ](#adce51ae345d5fc417f3767476af36276)dump\_regs

| int(\* usbc\_ppc\_driver\_api::dump\_regs) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a4ba2f654765130d5562f56243967bf58)exit\_dead\_battery\_mode

| int(\* usbc\_ppc\_driver\_api::exit\_dead\_battery\_mode) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a832320573b2adab1d748e5e761690733)is\_dead\_battery\_mode

| int(\* usbc\_ppc\_driver\_api::is\_dead\_battery\_mode) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a8bf73dee9ba920f1b426038f62d5c9db)is\_vbus\_present

| int(\* usbc\_ppc\_driver\_api::is\_vbus\_present) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a93b91d21d4d2edda1d457f4144800f37)is\_vbus\_sink

| int(\* usbc\_ppc\_driver\_api::is\_vbus\_sink) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#aab74a38a9c055efdfd0198143f12c9ff)is\_vbus\_source

| int(\* usbc\_ppc\_driver\_api::is\_vbus\_source) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a8f82ae3af5452d9cd0852bf15fcab573)set\_event\_handler

| int(\* usbc\_ppc\_driver\_api::set\_event\_handler) (const struct [device](structdevice.md) \*dev, [usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data) |
| --- |

## [◆ ](#af4a66a11b66d48818123434c59553f0d)set\_snk\_ctrl

| int(\* usbc\_ppc\_driver\_api::set\_snk\_ctrl) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a20ddefaee68808414f4075cc513a8660)set\_src\_ctrl

| int(\* usbc\_ppc\_driver\_api::set\_src\_ctrl) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a1c2c21070ee18b7b5df09a6b6ed618b6)set\_vbus\_discharge

| int(\* usbc\_ppc\_driver\_api::set\_vbus\_discharge) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_ppc.h](usbc__ppc_8h_source.md)

- [usbc\_ppc\_driver\_api](structusbc__ppc__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
