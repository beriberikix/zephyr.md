---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi3c__ccc__mwl.html
original_path: doxygen/html/structi3c__ccc__mwl.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_mwl Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for SETMWL/GETMWL CCC (Set/Get Maximum Write Length).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a5312fa1fc7cc93dfdf88d490352cf08e) |
|  | Maximum Write Length. |

## Detailed Description

Payload for SETMWL/GETMWL CCC (Set/Get Maximum Write Length).

Note
:   For drivers and help functions, the raw data coming back from target device is in big endian. This needs to be translated back to CPU endianness before passing back to function caller.

## Field Documentation

## [◆ ](#a5312fa1fc7cc93dfdf88d490352cf08e)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_ccc\_mwl::len |
| --- |

Maximum Write Length.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_mwl](structi3c__ccc__mwl.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
