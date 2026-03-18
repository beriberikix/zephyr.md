---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2power_2atmel__sam__supc_8h.html
original_path: doxygen/html/drivers_2power_2atmel__sam__supc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atmel\_sam\_supc.h File Reference

[Go to the source code of this file.](drivers_2power_2atmel__sam__supc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SAM\_DT\_SUPC\_CONTROLLER](#a694ffc7f2cd3ac2dad7a19111f983f5c)   [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(supc)) |
| #define | [SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID](#a30156dd2f0f5f9a1daea631866f9fbb7)(node\_id) |
| #define | [SAM\_DT\_INST\_SUPC\_WAKEUP\_SOURCE\_ID](#ad12cd5eb9bcaea5ac08a39f1218dfff6)(inst) |

## Macro Definition Documentation

## [◆ ](#ad12cd5eb9bcaea5ac08a39f1218dfff6)SAM\_DT\_INST\_SUPC\_WAKEUP\_SOURCE\_ID

| #define SAM\_DT\_INST\_SUPC\_WAKEUP\_SOURCE\_ID | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID](#a30156dd2f0f5f9a1daea631866f9fbb7)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID](#a30156dd2f0f5f9a1daea631866f9fbb7)

#define SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID(node\_id)

**Definition** atmel\_sam\_supc.h:12

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

## [◆ ](#a694ffc7f2cd3ac2dad7a19111f983f5c)SAM\_DT\_SUPC\_CONTROLLER

| #define SAM\_DT\_SUPC\_CONTROLLER   [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(supc)) |
| --- |

## [◆ ](#a30156dd2f0f5f9a1daea631866f9fbb7)SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID

| #define SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, wakeup\_source\_id wakeup\_source\_id)

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:809

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [power](dir_0407a529497ae7b6e6f3b04cc7899a88.md)
- [atmel\_sam\_supc.h](drivers_2power_2atmel__sam__supc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
