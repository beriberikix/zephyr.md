---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2reset_8h.html
original_path: doxygen/html/devicetree_2reset_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reset.h File Reference

Reset Controller Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](devicetree_2reset_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_RESET\_CTLR\_BY\_IDX](group__devicetree-reset-controller.md#gaa730fe6a58ee0a2d9daf7e125048f9e6)(node\_id, idx) |
|  | Get the node identifier for the controller phandle from a "resets" phandle-array property at an index. |
| #define | [DT\_RESET\_CTLR](group__devicetree-reset-controller.md#ga55afbfa565375eb4b233051f7065e504)(node\_id) |
|  | Equivalent to [DT\_RESET\_CTLR\_BY\_IDX(node\_id, 0)](group__devicetree-reset-controller.md#gaa730fe6a58ee0a2d9daf7e125048f9e6 "Get the node identifier for the controller phandle from a "resets" phandle-array property at an index..."). |
| #define | [DT\_RESET\_CTLR\_BY\_NAME](group__devicetree-reset-controller.md#ga5bc0702036df3a38ceb2d2741ee0717d)(node\_id, name) |
|  | Get the node identifier for the controller phandle from a resets phandle-array property by name. |
| #define | [DT\_RESET\_CELL\_BY\_IDX](group__devicetree-reset-controller.md#ga17918c75ef82acea60d7e65b6f1cee0a)(node\_id, idx, cell) |
|  | Get a reset specifier's cell value at an index. |
| #define | [DT\_RESET\_CELL\_BY\_NAME](group__devicetree-reset-controller.md#ga102229a7a1a30a29c5a5bf2bb0d42ada)(node\_id, name, cell) |
|  | Get a reset specifier's cell value by name. |
| #define | [DT\_RESET\_CELL](group__devicetree-reset-controller.md#ga626173f9cd280016f9f743d12bc4c047)(node\_id, cell) |
|  | Equivalent to [DT\_RESET\_CELL\_BY\_IDX(node\_id, 0, cell)](group__devicetree-reset-controller.md#ga17918c75ef82acea60d7e65b6f1cee0a "Get a reset specifier's cell value at an index."). |
| #define | [DT\_INST\_RESET\_CTLR\_BY\_IDX](group__devicetree-reset-controller.md#ga44cc59dc014eb69aacd4b6fedb5b2a54)(inst, idx) |
|  | Get the node identifier for the controller phandle from a "resets" phandle-array property at an index. |
| #define | [DT\_INST\_RESET\_CTLR](group__devicetree-reset-controller.md#gadc32a356d6a18689ca4a20cc657ce600)(inst) |
|  | Equivalent to [DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, 0)](group__devicetree-reset-controller.md#ga44cc59dc014eb69aacd4b6fedb5b2a54 "Get the node identifier for the controller phandle from a "resets" phandle-array property at an index..."). |
| #define | [DT\_INST\_RESET\_CTLR\_BY\_NAME](group__devicetree-reset-controller.md#ga66352f34890886dc20fdaa3a3f9beea9)(inst, name) |
|  | Get the node identifier for the controller phandle from a resets phandle-array property by name. |
| #define | [DT\_INST\_RESET\_CELL\_BY\_IDX](group__devicetree-reset-controller.md#ga9727e93185d96b84ec2d53ef07597a02)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's reset specifier's cell value at an index. |
| #define | [DT\_INST\_RESET\_CELL\_BY\_NAME](group__devicetree-reset-controller.md#ga3d914f91e6f1514d2b0d6ec61cf92a5e)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's reset specifier's cell value by name. |
| #define | [DT\_INST\_RESET\_CELL](group__devicetree-reset-controller.md#gad078f74edd7e672f6c3fda91dec01f12)(inst, cell) |
|  | Equivalent to [DT\_INST\_RESET\_CELL\_BY\_IDX(inst, 0, cell)](group__devicetree-reset-controller.md#ga9727e93185d96b84ec2d53ef07597a02 "Get a DT_DRV_COMPAT instance's reset specifier's cell value at an index."). |
| #define | [DT\_RESET\_ID\_BY\_IDX](group__devicetree-reset-controller.md#ga4259b4aa8bfe6f4ccb268c180541237d)(node\_id, idx) |
|  | Get a Reset Controller specifier's id cell at an index. |
| #define | [DT\_RESET\_ID](group__devicetree-reset-controller.md#gae8a5453df7ac3710858937485a9ee49b)(node\_id) |
|  | Equivalent to [DT\_RESET\_ID\_BY\_IDX(node\_id, 0)](group__devicetree-reset-controller.md#ga4259b4aa8bfe6f4ccb268c180541237d "Get a Reset Controller specifier's id cell at an index."). |
| #define | [DT\_INST\_RESET\_ID\_BY\_IDX](group__devicetree-reset-controller.md#gac42ce32f6e5fd1ae2b449bcf60d70afc)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's Reset Controller specifier's id cell value at an index. |
| #define | [DT\_INST\_RESET\_ID](group__devicetree-reset-controller.md#ga64080e5a9a0a568975323e637127e20f)(inst) |
|  | Equivalent to [DT\_INST\_RESET\_ID\_BY\_IDX(inst, 0)](group__devicetree-reset-controller.md#gac42ce32f6e5fd1ae2b449bcf60d70afc "Get a DT_DRV_COMPAT instance's Reset Controller specifier's id cell value at an index."). |

## Detailed Description

Reset Controller Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [reset.h](devicetree_2reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
