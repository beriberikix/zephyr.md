---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/backend_8h.html
original_path: doxygen/html/backend_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

backend.h File Reference

Public APIs for Host Command backends that respond to host commands.
[More...](#details)

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](backend_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) |
| struct | [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) |
|  | Context for host command backend and handler to pass rx data. [More...](structec__host__cmd__rx__ctx.md#details) |
| struct | [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) |
|  | Context for host command backend and handler to pass tx data. [More...](structec__host__cmd__tx__buf.md#details) |
| struct | [ec\_host\_cmd\_backend\_api](structec__host__cmd__backend__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [ec\_host\_cmd\_backend\_api\_init](group__ec__host__cmd__interface.md#ga811b9c355942811f0fee22c1fa8a5787)) (const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend, struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*tx) |
|  | Initialize a host command backend. |
| typedef int(\* | [ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)) (const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend) |
|  | Sends data to the host. |

| Functions | |
| --- | --- |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_espi](group__ec__host__cmd__interface.md#ga32d7a58724694ab753efbf7f81e8d940) (const struct [device](structdevice.md) \*dev) |
|  | Get the eSPI Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_shi\_npcx](group__ec__host__cmd__interface.md#gaa4562dd46503cf8844a546b102ce01e9) (void) |
|  | Get the SHI NPCX Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_shi\_ite](group__ec__host__cmd__interface.md#ga892fec4587de508805fdf5ace9dd1050) (void) |
|  | Get the SHI ITE Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_uart](group__ec__host__cmd__interface.md#ga558b7690dad9a9a5eb8771fcfeba3b63) (const struct [device](structdevice.md) \*dev) |
|  | Get the UART Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_spi](group__ec__host__cmd__interface.md#ga12574d2eff8f07fd36967ccbc7600e1c) (struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*cs) |
|  | Get the SPI Host Command backend pointer. |

## Detailed Description

Public APIs for Host Command backends that respond to host commands.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [ec\_host\_cmd](dir_d53ada025add0f463456d44507c0d96c.md)
- [backend.h](backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
