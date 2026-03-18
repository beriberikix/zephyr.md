---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2reset_8h.html
original_path: doxygen/html/drivers_2reset_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reset.h File Reference

Public Reset Controller driver APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/reset.h>`

[Go to the source code of this file.](drivers_2reset_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [reset\_dt\_spec](structreset__dt__spec.md) |
|  | Reset controller device configuration. [More...](structreset__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [RESET\_DT\_SPEC\_GET\_BY\_IDX](group__reset__controller__interface.md#ga9f2e9e2e14a6ec9d2848979c77ecad9b)(node\_id, idx) |
|  | Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| #define | [RESET\_DT\_SPEC\_GET](group__reset__controller__interface.md#gac4b466f492ae7a1c4e19647f41749c6b)(node\_id) |
|  | Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](group__reset__controller__interface.md#ga9f2e9e2e14a6ec9d2848979c77ecad9b "Static initializer for a reset_dt_spec."). |
| #define | [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX](group__reset__controller__interface.md#ga539688cb73d17aa02b137fc90965350b)(inst, idx) |
|  | Static initializer for a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")` from a DT\_DRV\_COMPAT instance's Reset Controller property at an index. |
| #define | [RESET\_DT\_SPEC\_INST\_GET](group__reset__controller__interface.md#ga1557bbcabdf02c3db1aa0705ce80baf0)(inst) |
|  | Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](group__reset__controller__interface.md#ga539688cb73d17aa02b137fc90965350b "Static initializer for a reset_dt_spec from a DT_DRV_COMPAT instance's Reset Controller property at a..."). |

| Functions | |
| --- | --- |
| int | [reset\_status](group__reset__controller__interface.md#gad58d0bfcf0b9cd4ba11b163e97ba8762) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the reset status. |
| static int | [reset\_status\_dt](group__reset__controller__interface.md#gaa5d00726d387ff44244bc939a943963d) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the reset status from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| int | [reset\_line\_assert](group__reset__controller__interface.md#gab7b58d253be9083b4ed7c35bc60c6aa6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Put the device in reset state. |
| static int | [reset\_line\_assert\_dt](group__reset__controller__interface.md#gabfe4a15880e38cbf30e293f9143d5080) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec) |
|  | Assert the reset state from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| int | [reset\_line\_deassert](group__reset__controller__interface.md#gaadd2d70e57e620e9f12900c561fea941) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Take out the device from reset state. |
| static int | [reset\_line\_deassert\_dt](group__reset__controller__interface.md#ga7c747373b556ee1c00bad4afcdd138c0) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec) |
|  | Deassert the reset state from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |
| int | [reset\_line\_toggle](group__reset__controller__interface.md#ga29fb7d474e46d7a5a69ab8fb87ddbc5e) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Reset the device. |
| static int | [reset\_line\_toggle\_dt](group__reset__controller__interface.md#gaf3db170375c24999ea1b1954fb3ae184) (const struct [reset\_dt\_spec](structreset__dt__spec.md) \*spec) |
|  | Reset the device from a `[reset_dt_spec](structreset__dt__spec.md "Reset controller device configuration.")`. |

## Detailed Description

Public Reset Controller driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [reset.h](drivers_2reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
