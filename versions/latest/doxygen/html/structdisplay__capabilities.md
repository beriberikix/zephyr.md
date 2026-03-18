---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdisplay__capabilities.html
original_path: doxygen/html/structdisplay__capabilities.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

display\_capabilities Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Display Interface](group__display__interface.md)

Structure holding display capabilities.
[More...](#details)

`#include <[display.h](display_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [x\_resolution](#a09fa14e2c53126d5602cb7b51e21145f) |
|  | Display resolution in the X direction. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [y\_resolution](#a2cacb194139aaff90fd56b469f6de4a9) |
|  | Display resolution in the Y direction. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [supported\_pixel\_formats](#a07548bdd9671dd696b38a5bcf1599412) |
|  | Bitwise or of pixel formats supported by the display. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [screen\_info](#ac4a9098db4c2f721fa550c6142f541a9) |
|  | Information about display panel. |
| enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) | [current\_pixel\_format](#aed51c9efdc76972fecfa8a733c2a8d0c) |
|  | Currently active pixel format for the display. |
| enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) | [current\_orientation](#a18986f5d2c385766d5ad3d68edd85887) |
|  | Current display orientation. |

## Detailed Description

Structure holding display capabilities.

## Field Documentation

## [◆ ](#a18986f5d2c385766d5ad3d68edd85887)current\_orientation

| enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) display\_capabilities::current\_orientation |
| --- |

Current display orientation.

## [◆ ](#aed51c9efdc76972fecfa8a733c2a8d0c)current\_pixel\_format

| enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) display\_capabilities::current\_pixel\_format |
| --- |

Currently active pixel format for the display.

## [◆ ](#ac4a9098db4c2f721fa550c6142f541a9)screen\_info

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) display\_capabilities::screen\_info |
| --- |

Information about display panel.

## [◆ ](#a07548bdd9671dd696b38a5bcf1599412)supported\_pixel\_formats

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) display\_capabilities::supported\_pixel\_formats |
| --- |

Bitwise or of pixel formats supported by the display.

## [◆ ](#a09fa14e2c53126d5602cb7b51e21145f)x\_resolution

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) display\_capabilities::x\_resolution |
| --- |

Display resolution in the X direction.

## [◆ ](#a2cacb194139aaff90fd56b469f6de4a9)y\_resolution

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) display\_capabilities::y\_resolution |
| --- |

Display resolution in the Y direction.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[display.h](display_8h_source.md)

- [display\_capabilities](structdisplay__capabilities.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
