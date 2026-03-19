---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp__lp__flexcomm_8h.html
original_path: doxygen/html/nxp__lp__flexcomm_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_lp\_flexcomm.h File Reference

`#include "fsl_lpflexcomm.h"`

[Go to the source code of this file.](nxp__lp__flexcomm_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [child\_isr\_t](#af38501b5aa1350ebc2c03be9b6623353)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| void | [nxp\_lp\_flexcomm\_setirqhandler](#a259055f21461b4dead75cdec3243719e) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*child\_dev, LP\_FLEXCOMM\_PERIPH\_T periph, [child\_isr\_t](#af38501b5aa1350ebc2c03be9b6623353) handler) |

## Typedef Documentation

## [◆ ](#af38501b5aa1350ebc2c03be9b6623353)child\_isr\_t

| typedef void(\* child\_isr\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

## Function Documentation

## [◆ ](#a259055f21461b4dead75cdec3243719e)nxp\_lp\_flexcomm\_setirqhandler()

| void nxp\_lp\_flexcomm\_setirqhandler | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *child\_dev*, |
|  |  | LP\_FLEXCOMM\_PERIPH\_T | *periph*, |
|  |  | [child\_isr\_t](#af38501b5aa1350ebc2c03be9b6623353) | *handler* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [nxp\_lp\_flexcomm.h](nxp__lp__flexcomm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
