---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/clocks_8h.html
original_path: doxygen/html/clocks_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clocks.h File Reference

Clocks Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](clocks_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0)(node\_id, idx) |
|  | Test if a node has a clocks phandle-array property at a given index. |
| #define | [DT\_CLOCKS\_HAS\_NAME](group__devicetree-clocks.md#ga9d32df36dd18c4839e6e9efe509b17a4)(node\_id, name) |
|  | Test if a node has a clock-names array property holds a given name. |
| #define | [DT\_NUM\_CLOCKS](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3)(node\_id) |
|  | Get the number of elements in a clocks property. |
| #define | [DT\_CLOCKS\_CTLR\_BY\_IDX](group__devicetree-clocks.md#gab36c92fc26c3517031bce342148308c3)(node\_id, idx) |
|  | Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index. |
| #define | [DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)(node\_id) |
|  | Equivalent to [DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, 0)](group__devicetree-clocks.md#gab36c92fc26c3517031bce342148308c3 "Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index..."). |
| #define | [DT\_CLOCKS\_CTLR\_BY\_NAME](group__devicetree-clocks.md#gaf4c92378a2599ee7024f914ea3584404)(node\_id, name) |
|  | Get the node identifier for the controller phandle from a clocks phandle-array property by name. |
| #define | [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, idx, cell) |
|  | Get a clock specifier's cell value at an index. |
| #define | [DT\_CLOCKS\_CELL\_BY\_NAME](group__devicetree-clocks.md#gaca32bfb478ac92e6a760ad0761328d5a)(node\_id, name, cell) |
|  | Get a clock specifier's cell value by name. |
| #define | [DT\_CLOCKS\_CELL](group__devicetree-clocks.md#ga211bc385cbbb1d8b8fa52e2e0a52d23d)(node\_id, cell) |
|  | Equivalent to [DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, 0, cell)](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8 "Get a clock specifier's cell value at an index."). |
| #define | [DT\_INST\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gaf8ebb6ccd4915cc4069e92f804fb63ac)(inst, idx) |
|  | Equivalent to [DT\_CLOCKS\_HAS\_IDX(DT\_DRV\_INST(inst), idx)](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0 "Test if a node has a clocks phandle-array property at a given index."). |
| #define | [DT\_INST\_CLOCKS\_HAS\_NAME](group__devicetree-clocks.md#ga6b2997f105a29ff5c136f3dbb6120287)(inst, name) |
|  | Equivalent to DT\_CLOCK\_HAS\_NAME(DT\_DRV\_INST(inst), name). |
| #define | [DT\_INST\_NUM\_CLOCKS](group__devicetree-clocks.md#gadab88fe4063540efc136e5ae270c7cfa)(inst) |
|  | Equivalent to [DT\_NUM\_CLOCKS(DT\_DRV\_INST(inst))](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3 "Get the number of elements in a clocks property."). |
| #define | [DT\_INST\_CLOCKS\_CTLR\_BY\_IDX](group__devicetree-clocks.md#gac4a7a89937eae57960a2091d7edc5fd3)(inst, idx) |
|  | Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index. |
| #define | [DT\_INST\_CLOCKS\_CTLR](group__devicetree-clocks.md#gaeebaf3a45822d86dfeb38a3fda66dc54)(inst) |
|  | Equivalent to [DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, 0)](group__devicetree-clocks.md#gac4a7a89937eae57960a2091d7edc5fd3 "Get the node identifier for the controller phandle from a "clocks" phandle-array property at an index..."). |
| #define | [DT\_INST\_CLOCKS\_CTLR\_BY\_NAME](group__devicetree-clocks.md#ga209f77daee5016ed0d0d678ec6ec57b7)(inst, name) |
|  | Get the node identifier for the controller phandle from a clocks phandle-array property by name. |
| #define | [DT\_INST\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga5bee2e489f0818f0f2d1ec6d195bd3a8)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's clock specifier's cell value at an index. |
| #define | [DT\_INST\_CLOCKS\_CELL\_BY\_NAME](group__devicetree-clocks.md#ga976ab2adb237e5f1e0ba3496e9322d14)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's clock specifier's cell value by name. |
| #define | [DT\_INST\_CLOCKS\_CELL](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)(inst, cell) |
|  | Equivalent to [DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell)](group__devicetree-clocks.md#ga5bee2e489f0818f0f2d1ec6d195bd3a8 "Get a DT_DRV_COMPAT instance's clock specifier's cell value at an index."). |

## Detailed Description

Clocks Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [clocks.h](clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
