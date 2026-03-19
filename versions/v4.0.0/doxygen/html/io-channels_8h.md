---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/io-channels_8h.html
original_path: doxygen/html/io-channels_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

io-channels.h File Reference

IO channels devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](io-channels_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX](group__devicetree-io-channels.md#gaf5bbae59dca995d827ff3ec8b9ce187c)(node\_id, idx) |
|  | Get the node identifier for the node referenced by an io-channels property at an index. |
| #define | [DT\_IO\_CHANNELS\_CTLR\_BY\_NAME](group__devicetree-io-channels.md#ga1d6422230eb139beec9ac0f25ca2eab3)(node\_id, name) |
|  | Get the node identifier for the node referenced by an io-channels property by name. |
| #define | [DT\_IO\_CHANNELS\_CTLR](group__devicetree-io-channels.md#gaef1d0ee74798d9e60f5c5fa0c0f8db48)(node\_id) |
|  | Equivalent to [DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, 0)](group__devicetree-io-channels.md#gaf5bbae59dca995d827ff3ec8b9ce187c "Get the node identifier for the node referenced by an io-channels property at an index."). |
| #define | [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX](group__devicetree-io-channels.md#gacf417be0bda7b8ddfb20503f8d846822)(inst, idx) |
|  | Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property at an index. |
| #define | [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_NAME](group__devicetree-io-channels.md#gacd4b12a7698d44b56673e66643c2f88f)(inst, name) |
|  | Get the node identifier from a DT\_DRV\_COMPAT instance's io-channels property by name. |
| #define | [DT\_INST\_IO\_CHANNELS\_CTLR](group__devicetree-io-channels.md#gaf25c454ac2cf285b3efa2e9a4251dd0e)(inst) |
|  | Equivalent to [DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, 0)](group__devicetree-io-channels.md#gacf417be0bda7b8ddfb20503f8d846822 "Get the node identifier from a DT_DRV_COMPAT instance's io-channels property at an index."). |
| #define | [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX](group__devicetree-io-channels.md#ga290c912d0a96ba65bb44341a783fac19)(node\_id, idx) |
|  | Get an io-channels specifier input cell at an index. |
| #define | [DT\_IO\_CHANNELS\_INPUT\_BY\_NAME](group__devicetree-io-channels.md#ga6870a8215f61f87c3cb8f137a7bbbcc3)(node\_id, name) |
|  | Get an io-channels specifier input cell by name. |
| #define | [DT\_IO\_CHANNELS\_INPUT](group__devicetree-io-channels.md#gadcb598f00280ae1fa488e7982971e7d6)(node\_id) |
|  | Equivalent to [DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, 0)](group__devicetree-io-channels.md#ga290c912d0a96ba65bb44341a783fac19 "Get an io-channels specifier input cell at an index."). |
| #define | [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX](group__devicetree-io-channels.md#gac396f180ab5b24bdca01c021447a0211)(inst, idx) |
|  | Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property at an index. |
| #define | [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_NAME](group__devicetree-io-channels.md#ga09cbce4296bd4982d2ed1e5cea45da5e)(inst, name) |
|  | Get an input cell from the "DT\_DRV\_INST(inst)" io-channels property by name. |
| #define | [DT\_INST\_IO\_CHANNELS\_INPUT](group__devicetree-io-channels.md#ga736d38a4e3a3a5e2e294e50df805c320)(inst) |
|  | Equivalent to [DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, 0)](group__devicetree-io-channels.md#gac396f180ab5b24bdca01c021447a0211 "Get an input cell from the "DT_DRV_INST(inst)" io-channels property at an index."). |

## Detailed Description

IO channels devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [io-channels.h](io-channels_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
