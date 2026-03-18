---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmspi__callback__context.html
original_path: doxygen/html/structmspi__callback__context.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_callback\_context Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI callback API](group__mspi__callback__api.md)

MSPI callback context.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [mspi\_event](structmspi__event.md) | [mspi\_evt](#a5649bddfac23544522969fc9e500eb0c) |
|  | MSPI event. |
| void \* | [ctx](#ab2225b77f4d9e0403192c0ab11482e2e) |
|  | user defined context |

## Detailed Description

MSPI callback context.

## Field Documentation

## [◆ ](#ab2225b77f4d9e0403192c0ab11482e2e)ctx

| void\* mspi\_callback\_context::ctx |
| --- |

user defined context

## [◆ ](#a5649bddfac23544522969fc9e500eb0c)mspi\_evt

| struct [mspi\_event](structmspi__event.md) mspi\_callback\_context::mspi\_evt |
| --- |

MSPI event.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_callback\_context](structmspi__callback__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
