---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/espi__saf_8h.html
original_path: doxygen/html/espi__saf_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_saf.h File Reference

Public APIs for eSPI driver.
[More...](#details)

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/espi_saf.h>`

[Go to the source code of this file.](espi__saf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [espi\_saf\_cfg](structespi__saf__cfg.md) |
|  | eSPI SAF configuration parameters [More...](structespi__saf__cfg.md#details) |
| struct | [espi\_saf\_packet](structespi__saf__packet.md) |
|  | eSPI SAF transaction packet format [More...](structespi__saf__packet.md#details) |

| Functions | |
| --- | --- |
| int | [espi\_saf\_config](group__espi__interface.md#ga34b0f6336aec45016d97528767b09434) (const struct [device](structdevice.md) \*dev, const struct [espi\_saf\_cfg](structespi__saf__cfg.md) \*cfg) |
|  | Configure operation of a eSPI controller. |
| int | [espi\_saf\_set\_protection\_regions](group__espi__interface.md#ga273a9707f3ca501ed2dd3019cdeaa363) (const struct [device](structdevice.md) \*dev, const struct espi\_saf\_protection \*pr) |
|  | Set one or more SAF protection regions. |
| int | [espi\_saf\_activate](group__espi__interface.md#gaafe30738c18a16b056ed8dcf8638eb84) (const struct [device](structdevice.md) \*dev) |
|  | Activate SAF block. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [espi\_saf\_get\_channel\_status](group__espi__interface.md#ga8b53a93559f0c67953e283f59107aa22) (const struct [device](structdevice.md) \*dev) |
|  | Query to see if SAF is ready. |
| int | [espi\_saf\_flash\_read](group__espi__interface.md#ga0f5017eac05f928e635fec8e5f877c7d) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Sends a read request packet for slave attached flash. |
| int | [espi\_saf\_flash\_write](group__espi__interface.md#ga104175f74019e58b8b7901f3dae245db) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Sends a write request packet for slave attached flash. |
| int | [espi\_saf\_flash\_erase](group__espi__interface.md#ga15855a2ac593b97dc1a3e83ac9eda300) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Sends a write request packet for slave attached flash. |
| int | [espi\_saf\_flash\_unsuccess](group__espi__interface.md#ga6c54d9274b1a8e883484bd892f606fd5) (const struct [device](structdevice.md) \*dev, struct [espi\_saf\_packet](structespi__saf__packet.md) \*pckt) |
|  | Response unsuccessful completion for slave attached flash. |
| static void | [espi\_saf\_init\_callback](group__espi__interface.md#ga324283c28e6a33be112571621d1568e8) (struct espi\_callback \*callback, [espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46) handler, enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type) |
|  | Callback model. |
| static int | [espi\_saf\_add\_callback](group__espi__interface.md#gadb881f847082f713bb0159d1e474980a) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Add an application callback. |
| static int | [espi\_saf\_remove\_callback](group__espi__interface.md#gaf987842bc7dad310c7270aed50086af9) (const struct [device](structdevice.md) \*dev, struct espi\_callback \*callback) |
|  | Remove an application callback. |

## Detailed Description

Public APIs for eSPI driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [espi\_saf.h](espi__saf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
