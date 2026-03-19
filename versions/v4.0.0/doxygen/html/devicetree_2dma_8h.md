---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2dma_8h.html
original_path: doxygen/html/devicetree_2dma_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma.h File Reference

DMA Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](devicetree_2dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_DMAS\_CTLR\_BY\_IDX](group__devicetree-dmas.md#gac74e56d90f8abe4bb0b53acddb618a3a)(node\_id, idx) |
|  | Get the node identifier for the DMA controller from a dmas property at an index. |
| #define | [DT\_DMAS\_CTLR\_BY\_NAME](group__devicetree-dmas.md#ga8c148fc826dee34f5e4601f4a7aa9f55)(node\_id, name) |
|  | Get the node identifier for the DMA controller from a dmas property by name. |
| #define | [DT\_DMAS\_CTLR](group__devicetree-dmas.md#ga09a22a0e5133dc7514680c16373f6ad3)(node\_id) |
|  | Equivalent to [DT\_DMAS\_CTLR\_BY\_IDX(node\_id, 0)](group__devicetree-dmas.md#gac74e56d90f8abe4bb0b53acddb618a3a "Get the node identifier for the DMA controller from a dmas property at an index."). |
| #define | [DT\_INST\_DMAS\_CTLR\_BY\_IDX](group__devicetree-dmas.md#ga5dbb1f22a0098a3493fd6f4cef9985a9)(inst, idx) |
|  | Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property at an index. |
| #define | [DT\_INST\_DMAS\_CTLR\_BY\_NAME](group__devicetree-dmas.md#gad098f0b51ee1f629c1259ca346f49303)(inst, name) |
|  | Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property by name. |
| #define | [DT\_INST\_DMAS\_CTLR](group__devicetree-dmas.md#ga32025fb8590eec09adaff23db1138e75)(inst) |
|  | Equivalent to [DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, 0)](group__devicetree-dmas.md#ga5dbb1f22a0098a3493fd6f4cef9985a9 "Get the node identifier for the DMA controller from a DT_DRV_COMPAT instance's dmas property at an in..."). |
| #define | [DT\_DMAS\_CELL\_BY\_IDX](group__devicetree-dmas.md#ga8aff7a91d19482964b8b56cb558c1b59)(node\_id, idx, cell) |
|  | Get a DMA specifier's cell value at an index. |
| #define | [DT\_INST\_DMAS\_CELL\_BY\_IDX](group__devicetree-dmas.md#gad4e1a8f22b8943328df2a3f8f2a149b7)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value at an index. |
| #define | [DT\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga1b80ae7fee6bcc9aa2ad03435e70dd14)(node\_id, name, cell) |
|  | Get a DMA specifier's cell value by name. |
| #define | [DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value by name. |
| #define | [DT\_DMAS\_HAS\_IDX](group__devicetree-dmas.md#gab789e18935628f40d80f3b64ca5cbe80)(node\_id, idx) |
|  | Is index "idx" valid for a dmas property? |
| #define | [DT\_INST\_DMAS\_HAS\_IDX](group__devicetree-dmas.md#gaff634d5b2a342c73f001a5ee64b70829)(inst, idx) |
|  | Is index "idx" valid for a DT\_DRV\_COMPAT instance's dmas property? |
| #define | [DT\_DMAS\_HAS\_NAME](group__devicetree-dmas.md#ga865adb5b82c63e7f63451b96cd5a6404)(node\_id, name) |
|  | Does a dmas property have a named element? |
| #define | [DT\_INST\_DMAS\_HAS\_NAME](group__devicetree-dmas.md#gad60c155da3d850a61365ca7d12dc1813)(inst, name) |
|  | Does a DT\_DRV\_COMPAT instance's dmas property have a named element? |

## Detailed Description

DMA Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [dma.h](devicetree_2dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
