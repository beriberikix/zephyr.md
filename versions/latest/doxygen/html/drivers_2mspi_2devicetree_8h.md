---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2mspi_2devicetree_8h.html
original_path: doxygen/html/drivers_2mspi_2devicetree_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree.h File Reference

`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](drivers_2mspi_2devicetree_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MSPI\_DEVICE\_CONFIG\_DT](group__mspi__devicetree.md#gaa8e730d85dede3d1e5dc9f69f30098b2)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") from devicetree. |
| #define | [MSPI\_DEVICE\_CONFIG\_DT\_INST](group__mspi__devicetree.md#ga52ebf325f9a1eb7d9fda6736ac8188f1)(inst) |
|  | Structure initializer for struct [mspi\_dev\_cfg](structmspi__dev__cfg.md "MSPI controller device specific configuration.") from devicetree instance. |
| #define | [MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK](group__mspi__devicetree.md#ga01a618fadb0147bf5abf42972a17f594)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree. |
| #define | [MSPI\_XIP\_CONFIG\_DT](group__mspi__devicetree.md#ga24a88651c634c5ab5630e7844ff98e4b)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree. |
| #define | [MSPI\_XIP\_CONFIG\_DT\_INST](group__mspi__devicetree.md#gafe739210f9f5cab4ab71bd61ec5af03f)(inst) |
|  | Structure initializer for struct [mspi\_xip\_cfg](structmspi__xip__cfg.md "MSPI controller XIP configuration.") from devicetree instance. |
| #define | [MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK](group__mspi__devicetree.md#gad1f36df770167384cc4e3f2c9be07d34)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree. |
| #define | [MSPI\_SCRAMBLE\_CONFIG\_DT](group__mspi__devicetree.md#ga10ee161794b5c7986a4411b8fc90ea7d)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree. |
| #define | [MSPI\_SCRAMBLE\_CONFIG\_DT\_INST](group__mspi__devicetree.md#gaa9b32a8f6984468b5198524bea42ed8c)(inst) |
|  | Structure initializer for struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md "MSPI controller scramble configuration.") from devicetree instance. |
| #define | [MSPI\_DEVICE\_ID\_DT](group__mspi__devicetree.md#gafa7c0d76c85a31004d72392016da1246)(mspi\_dev) |
|  | Structure initializer for struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") from devicetree. |
| #define | [MSPI\_DEVICE\_ID\_DT\_INST](group__mspi__devicetree.md#gabfd0d3beb91762e939636c87a91a6673)(inst) |
|  | Structure initializer for struct [mspi\_dev\_id](structmspi__dev__id.md "MSPI device ID The controller can identify its devices and determine whether the access is allowed in...") from devicetree instance. |
| #define | [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET](group__mspi__devicetree.md#ga0a91ef9392be4493ede6cea607ee8728)(mspi\_dev) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI device's chip enable pin. |
| #define | [MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_INST\_GET](group__mspi__devicetree.md#ga0b98f7a625324abce90933cb2395fb17)(inst) |
|  | Get a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI device's chip enable pin. |
| #define | [MSPI\_CE\_GPIOS\_DT\_SPEC\_GET](group__mspi__devicetree.md#ga1ca28d7ead69cd3a5e26198bc6815b54)(node\_id) |
|  | Get an array of struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") from devicetree for a MSPI controller. |
| #define | [MSPI\_CE\_GPIOS\_DT\_SPEC\_INST\_GET](group__mspi__devicetree.md#ga5ae4bd8071da4babd0bdf9767e9542e4)(inst) |
|  | Get an array of struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for a MSPI controller. |
| #define | [MSPI\_CE\_CONTROL\_INIT](group__mspi__devicetree.md#ga501b2e19e358083f2b47838cde58a676)(node\_id, delay\_) |
|  | Initialize and get a pointer to a `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` from a devicetree node identifier. |
| #define | [MSPI\_CE\_CONTROL\_INIT\_INST](group__mspi__devicetree.md#gacec91c9080052adf96aa5d36c6301d8c)(inst, delay\_) |
|  | Get a pointer to a `[mspi_ce_control](structmspi__ce__control.md "MSPI Chip Select control structure.")` from a devicetree node. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mspi](dir_288d6185a21193ccd9a81f08240fb63b.md)
- [devicetree.h](drivers_2mspi_2devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
