---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/emul__stub__device_8h.html
original_path: doxygen/html/emul__stub__device_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_stub\_device.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](emul__stub__device_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [emul\_stub\_dev\_data](structemul__stub__dev__data.md) |
| struct | [emul\_stub\_dev\_config](structemul__stub__dev__config.md) |
| struct | [emul\_stub\_dev\_api](structemul__stub__dev__api.md) |

| Macros | |
| --- | --- |
| #define | [EMUL\_STUB\_DEVICE](#ae42dec3fd3ebdfc8ab5c1b9eabea26d0)(n) |

## Macro Definition Documentation

## [◆ ](#ae42dec3fd3ebdfc8ab5c1b9eabea26d0)EMUL\_STUB\_DEVICE

| #define EMUL\_STUB\_DEVICE | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_maybe\_unused static int emul\_init\_stub\_##n(const struct [device](structdevice.md) \*dev) \

{ \

ARG\_UNUSED(dev); \

return 0; \

} \

\

static struct [emul\_stub\_dev\_data](structemul__stub__dev__data.md) stub\_data\_##n; \

static struct [emul\_stub\_dev\_config](structemul__stub__dev__config.md) stub\_config\_##n; \

static struct [emul\_stub\_dev\_api](structemul__stub__dev__api.md) stub\_api\_##n; \

DEVICE\_DT\_INST\_DEFINE(n, &emul\_init\_stub\_##n, NULL, &stub\_data\_##n, &stub\_config\_##n, \

POST\_KERNEL, CONFIG\_KERNEL\_INIT\_PRIORITY\_DEVICE, &stub\_api\_##n);

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[emul\_stub\_dev\_api](structemul__stub__dev__api.md)

**Definition** emul\_stub\_device.h:23

[emul\_stub\_dev\_config](structemul__stub__dev__config.md)

**Definition** emul\_stub\_device.h:20

[emul\_stub\_dev\_data](structemul__stub__dev__data.md)

**Definition** emul\_stub\_device.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_stub\_device.h](emul__stub__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
