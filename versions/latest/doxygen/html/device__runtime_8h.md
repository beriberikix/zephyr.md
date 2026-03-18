---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/device__runtime_8h.html
original_path: doxygen/html/device__runtime_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device\_runtime.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](device__runtime_8h_source.md)

| Functions | |
| --- | --- |
| int | [pm\_device\_runtime\_auto\_enable](group__subsys__pm__device__runtime.md#gadc36f344b2cb40c33d5b37eefd120c98) (const struct [device](structdevice.md) \*dev) |
|  | Automatically enable device runtime based on devicetree properties. |
| int | [pm\_device\_runtime\_enable](group__subsys__pm__device__runtime.md#gaabcd2cc694c9e201dd87bf42f02b454c) (const struct [device](structdevice.md) \*dev) |
|  | Enable device runtime PM. |
| int | [pm\_device\_runtime\_disable](group__subsys__pm__device__runtime.md#gaa7fc78138e282b0eae7da67876baee80) (const struct [device](structdevice.md) \*dev) |
|  | Disable device runtime PM. |
| int | [pm\_device\_runtime\_get](group__subsys__pm__device__runtime.md#ga530d4be65757fb2276ab6f631953e045) (const struct [device](structdevice.md) \*dev) |
|  | Resume a device based on usage count. |
| int | [pm\_device\_runtime\_put](group__subsys__pm__device__runtime.md#ga98daba53a992fb6bd2c2b31cb445844f) (const struct [device](structdevice.md) \*dev) |
|  | Suspend a device based on usage count. |
| int | [pm\_device\_runtime\_put\_async](group__subsys__pm__device__runtime.md#ga9e90089b0ab78f365905418646e196c6) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Suspend a device based on usage count (asynchronously). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_runtime\_is\_enabled](group__subsys__pm__device__runtime.md#ga605cd2a3d0ea31efe6bd0b9a6f723219) (const struct [device](structdevice.md) \*dev) |
|  | Check if device runtime is enabled for a given device. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [pm](dir_7e6ac69b960794fd0df7b746be7e9a24.md)
- [device\_runtime.h](device__runtime_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
