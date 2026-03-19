---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2i3c_2devicetree_8h.html
original_path: doxygen/html/drivers_2i3c_2devicetree_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](drivers_2i3c_2devicetree_8h_source.md)

| Macros | |
| --- | --- |
| #define | [I3C\_DEVICE\_ID\_DT](group__i3c__devicetree.md#ga917b45ec38e08d0c464cebe3372b682e)(node\_id) |
|  | Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from devicetree. |
| #define | [I3C\_DEVICE\_ID\_DT\_INST](group__i3c__devicetree.md#gadc45c0fdd41c081a0c3767159aae0c57)(inst) |
|  | Structure initializer for [i3c\_device\_id](structi3c__device__id.md "Structure used for matching I3C devices.") from devicetree instance. |
| #define | [I3C\_DEVICE\_DESC\_DT](group__i3c__devicetree.md#ga07eca721a06080900d976474138346fc)(node\_id) |
|  | Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree. |
| #define | [I3C\_DEVICE\_DESC\_DT\_INST](group__i3c__devicetree.md#gafb9b50f7d6e288d1722db5b4176742e9)(inst) |
|  | Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree instance. |
| #define | [I3C\_DEVICE\_DESC\_DT\_FILTERED](group__i3c__devicetree.md#gae5c3df5af3fe52476a506c4eff34ca1e)(node\_id) |
|  | Structure initializer for [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree. |
| #define | [I3C\_DEVICE\_ARRAY\_DT](group__i3c__devicetree.md#ga88aac6c42bbcd2f3276b6686c6786363)(node\_id) |
|  | Array initializer for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree. |
| #define | [I3C\_DEVICE\_ARRAY\_DT\_INST](group__i3c__devicetree.md#ga3153fd2d2b68eb760730827f6d6986c5)(inst) |
|  | Array initializer for a list of [i3c\_device\_desc](structi3c__device__desc.md "Structure describing a I3C target device.") from devicetree instance. |
| #define | [I3C\_DEVICE\_DT\_DEFINE](group__i3c__devicetree.md#gaab3219d45b125dd12d583bfd1823a61c)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with I3C target device specifics. |
| #define | [I3C\_DEVICE\_DT\_INST\_DEFINE](group__i3c__devicetree.md#ga77a471977d2c6edc530d3ce0febb8dbe)(inst, ...) |
|  | Like I3C\_TARGET\_DT\_DEFINE() for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [I3C\_I2C\_DEVICE\_DESC\_DT](group__i3c__devicetree.md#gaf317b1bcec787d594d3952dda2b9dc51)(node\_id) |
|  | Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree. |
| #define | [I3C\_I2C\_DEVICE\_DESC\_DT\_INST](group__i3c__devicetree.md#ga4c004a38164a56a1d1d027f2d29974e4)(inst) |
|  | Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree instance. |
| #define | [I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED](group__i3c__devicetree.md#ga703052c71216a4f152028540592ad581)(node\_id) |
|  | Structure initializer for [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree. |
| #define | [I3C\_I2C\_DEVICE\_ARRAY\_DT](group__i3c__devicetree.md#ga78f4d3fa3977989a731e33089d535701)(node\_id) |
|  | Array initializer for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree. |
| #define | [I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST](group__i3c__devicetree.md#gab441564c36a5d7e0856bba5eed51906f)(inst) |
|  | Array initializer for a list of [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md "Structure describing a I2C device on I3C bus.") from devicetree instance. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [devicetree.h](drivers_2i3c_2devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
