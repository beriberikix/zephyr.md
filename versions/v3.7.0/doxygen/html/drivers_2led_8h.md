---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2led_8h.html
original_path: doxygen/html/drivers_2led_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led.h File Reference

Public LED driver APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/led.h>`

[Go to the source code of this file.](drivers_2led_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [led\_info](structled__info.md) |
|  | LED information structure. [More...](structled__info.md#details) |
| struct | [led\_driver\_api](structled__driver__api.md) |
|  | LED driver API. [More...](structled__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off) |
|  | Callback API for blinking an LED. |
| typedef int(\* | [led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, const struct [led\_info](structled__info.md) \*\*info) |
|  | Optional API callback to get LED information. |
| typedef int(\* | [led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Callback API for setting brightness of an LED. |
| typedef int(\* | [led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color) |
|  | Optional API callback to set the colors of a LED. |
| typedef int(\* | [led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Callback API for turning on an LED. |
| typedef int(\* | [led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Callback API for turning off an LED. |
| typedef int(\* | [led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Callback API for writing a strip of LED channels. |

| Functions | |
| --- | --- |
| int | [led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off) |
|  | Blink an LED. |
| int | [led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, const struct [led\_info](structled__info.md) \*\*info) |
|  | Get LED information. |
| int | [led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set LED brightness. |
| int | [led\_write\_channels](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Write/update a strip of LED channels. |
| int | [led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set a single LED channel. |
| int | [led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color) |
|  | Set LED color. |
| int | [led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Turn on an LED. |
| int | [led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led) |
|  | Turn off an LED. |

## Detailed Description

Public LED driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led.h](drivers_2led_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
