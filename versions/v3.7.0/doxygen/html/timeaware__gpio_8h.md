---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/timeaware__gpio_8h.html
original_path: doxygen/html/timeaware__gpio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timeaware\_gpio.h File Reference

Public APIs for Time-aware GPIO drivers.
[More...](#details)

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/internal/syscall_handler.h](syscall__handler_8h_source.md)>`  
`#include <zephyr/syscalls/timeaware_gpio.h>`

[Go to the source code of this file.](timeaware__gpio_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [tgpio\_pin\_polarity](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c) { [TGPIO\_RISING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) = 0 , [TGPIO\_FALLING\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98) , [TGPIO\_TOGGLE\_EDGE](group__tgpio__interface.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9) } |
|  | Event polarity. [More...](group__tgpio__interface.md#gae05efc7d3232c308ae614b73688aa92c) |

| Functions | |
| --- | --- |
| int | [tgpio\_port\_get\_time](group__tgpio__interface.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*current\_time) |
|  | Get time from ART timer. |
| int | [tgpio\_port\_get\_cycles\_per\_second](group__tgpio__interface.md#gaccc8c2ed61ffabed71d5a410f10992da) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*cycles) |
|  | Get current running rate. |
| int | [tgpio\_pin\_disable](group__tgpio__interface.md#ga724d1410e73eba65c5d343b534424879) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin) |
|  | Disable operation on pin. |
| int | [tgpio\_pin\_config\_ext\_timestamp](group__tgpio__interface.md#ga4c35c5941848a1b060366e6ccb9e655e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_polarity) |
|  | Enable/Continue operation on pin. |
| int | [tgpio\_pin\_periodic\_output](group__tgpio__interface.md#gaec3b6161e701b9f2124470da9c202301) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) start\_time, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) repeat\_interval, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) periodic\_enable) |
|  | Enable periodic pulse generation on a pin. |
| int | [tgpio\_pin\_read\_ts\_ec](group__tgpio__interface.md#ga2f351d5d09b1f5bc7d71bce18979a0c2) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pin, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*timestamp, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*event\_count) |
|  | Read timestamp and event counter from TGPIO. |

## Detailed Description

Public APIs for Time-aware GPIO drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [timeaware\_gpio](dir_6bb0264ea02bd365c18848a4d9878330.md)
- [timeaware\_gpio.h](timeaware__gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
