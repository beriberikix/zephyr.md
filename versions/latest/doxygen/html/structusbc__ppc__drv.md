---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbc__ppc__drv.html
original_path: doxygen/html/structusbc__ppc__drv.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_ppc\_drv Struct Reference

Structure with pointers to the functions implemented by driver.
[More...](#details)

`#include <[usbc_ppc.h](usbc__ppc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [is\_dead\_battery\_mode](#a2641a5d2f8082a9fea2897d60992a81d) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [exit\_dead\_battery\_mode](#ac66444729d18d875432ac4d31610c1cc) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [is\_vbus\_source](#a3801f17cd627d99790cfbe45a20831e1) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [is\_vbus\_sink](#aa67d808b77e460159f6021e32701ede4) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [set\_snk\_ctrl](#a60f5d5d55a4037d380338830da3b7aef) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_src\_ctrl](#a18b223b9167e3d1aaa524a4f9aec87d5) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [set\_vbus\_discharge](#a5581e4e8c5dd709e85cca3ca3fe9ec09) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| int(\* | [is\_vbus\_present](#acfb87bd73f5ed0114e988c24b43910ec) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [set\_event\_handler](#a0bd893a73fad130849ad9549f6b3b9fd) )(const struct [device](structdevice.md) \*dev, [usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data) |
| int(\* | [dump\_regs](#a8b1880f4935bfc32594e8f900d4cf97d) )(const struct [device](structdevice.md) \*dev) |

## Detailed Description

Structure with pointers to the functions implemented by driver.

## Field Documentation

## [◆ ](#a8b1880f4935bfc32594e8f900d4cf97d)dump\_regs

| int(\* usbc\_ppc\_drv::dump\_regs) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#ac66444729d18d875432ac4d31610c1cc)exit\_dead\_battery\_mode

| int(\* usbc\_ppc\_drv::exit\_dead\_battery\_mode) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a2641a5d2f8082a9fea2897d60992a81d)is\_dead\_battery\_mode

| int(\* usbc\_ppc\_drv::is\_dead\_battery\_mode) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#acfb87bd73f5ed0114e988c24b43910ec)is\_vbus\_present

| int(\* usbc\_ppc\_drv::is\_vbus\_present) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#aa67d808b77e460159f6021e32701ede4)is\_vbus\_sink

| int(\* usbc\_ppc\_drv::is\_vbus\_sink) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a3801f17cd627d99790cfbe45a20831e1)is\_vbus\_source

| int(\* usbc\_ppc\_drv::is\_vbus\_source) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a0bd893a73fad130849ad9549f6b3b9fd)set\_event\_handler

| int(\* usbc\_ppc\_drv::set\_event\_handler) (const struct [device](structdevice.md) \*dev, [usbc\_ppc\_event\_cb\_t](usbc__ppc_8h.md#a8195a7a51eb5bd3cbcec985b97b84e73) handler, void \*data) |
| --- |

## [◆ ](#a60f5d5d55a4037d380338830da3b7aef)set\_snk\_ctrl

| int(\* usbc\_ppc\_drv::set\_snk\_ctrl) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a18b223b9167e3d1aaa524a4f9aec87d5)set\_src\_ctrl

| int(\* usbc\_ppc\_drv::set\_src\_ctrl) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a5581e4e8c5dd709e85cca3ca3fe9ec09)set\_vbus\_discharge

| int(\* usbc\_ppc\_drv::set\_vbus\_discharge) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_ppc.h](usbc__ppc_8h_source.md)

- [usbc\_ppc\_drv](structusbc__ppc__drv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
