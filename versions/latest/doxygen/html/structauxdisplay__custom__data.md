---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structauxdisplay__custom__data.html
original_path: doxygen/html/structauxdisplay__custom__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

auxdisplay\_custom\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Text Display Interface](group__auxdisplay__interface.md)

Structure for a custom command.
[More...](#details)

`#include <[auxdisplay.h](auxdisplay_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#acfd41be1569cc43bd09824c5e46b8d51) |
|  | Raw command data to be sent. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#ac995ecff9634acbc535a47b37134c6e1) |
|  | Length of supplied data. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#aa9c3b2af7c07e71e8cc5cd3eae058729) |
|  | Display-driver specific options for command. |

## Detailed Description

Structure for a custom command.

This may be extended by specific drivers.

## Field Documentation

## [◆ ](#acfd41be1569cc43bd09824c5e46b8d51)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* auxdisplay\_custom\_data::data |
| --- |

Raw command data to be sent.

## [◆ ](#ac995ecff9634acbc535a47b37134c6e1)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) auxdisplay\_custom\_data::len |
| --- |

Length of supplied data.

## [◆ ](#aa9c3b2af7c07e71e8cc5cd3eae058729)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) auxdisplay\_custom\_data::options |
| --- |

Display-driver specific options for command.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[auxdisplay.h](auxdisplay_8h_source.md)

- [auxdisplay\_custom\_data](structauxdisplay__custom__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
