---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/devicetree_2pinctrl_8h.html
original_path: doxygen/html/devicetree_2pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl.h File Reference

Devicetree pin control helpers.
[More...](#details)

[Go to the source code of this file.](devicetree_2pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_PINCTRL\_BY\_IDX](group__devicetree-pinctrl.md#ga24089220a93bc955700fba2c6170090e)(node\_id, pc\_idx, idx) |
|  | Get a node identifier for a phandle in a pinctrl property by index. |
| #define | [DT\_PINCTRL\_0](group__devicetree-pinctrl.md#gaf4e6f811ea4b1698c048d5dd8bfa604a)(node\_id, idx) |
|  | Get a node identifier from a pinctrl-0 property. |
| #define | [DT\_PINCTRL\_BY\_NAME](group__devicetree-pinctrl.md#ga1cd336f902738fd684f3d81b3fb6caae)(node\_id, name, idx) |
|  | Get a node identifier for a phandle inside a pinctrl node by name. |
| #define | [DT\_PINCTRL\_NAME\_TO\_IDX](group__devicetree-pinctrl.md#ga36eb691efc2a4854ccb62555aeade785)(node\_id, name) |
|  | Convert a pinctrl name to its corresponding index. |
| #define | [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN](group__devicetree-pinctrl.md#ga47b0e5a18919f9f4829209cccbdeb430)(node\_id, pc\_idx) |
|  | Convert a pinctrl property index to its name as a token. |
| #define | [DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN](group__devicetree-pinctrl.md#gaa6eec236ccde612e88017b027f4ba711)(node\_id, pc\_idx) |
|  | Like [DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN()](group__devicetree-pinctrl.md#ga47b0e5a18919f9f4829209cccbdeb430 "Convert a pinctrl property index to its name as a token."), but with an uppercased result. |
| #define | [DT\_NUM\_PINCTRLS\_BY\_IDX](group__devicetree-pinctrl.md#ga6ae1bab2a71cb628405ec43d38705606)(node\_id, pc\_idx) |
|  | Get the number of phandles in a pinctrl property. |
| #define | [DT\_NUM\_PINCTRLS\_BY\_NAME](group__devicetree-pinctrl.md#gaf96f1c82cc08008882f52e719ecd348c)(node\_id, name) |
|  | Like [DT\_NUM\_PINCTRLS\_BY\_IDX()](group__devicetree-pinctrl.md#ga6ae1bab2a71cb628405ec43d38705606 "Get the number of phandles in a pinctrl property."), but by name instead. |
| #define | [DT\_NUM\_PINCTRL\_STATES](group__devicetree-pinctrl.md#gaa2a012ce1d9ba026ee90001ae7f80381)(node\_id) |
|  | Get the number of pinctrl properties in a node. |
| #define | [DT\_PINCTRL\_HAS\_IDX](group__devicetree-pinctrl.md#ga5f1493cbfb7578b8fe3e37953aa9feaa)(node\_id, pc\_idx) |
|  | Test if a node has a pinctrl property with an index. |
| #define | [DT\_PINCTRL\_HAS\_NAME](group__devicetree-pinctrl.md#gac9cd8112ad745f34eb6f6e4a13d7fd7e)(node\_id, name) |
|  | Test if a node has a pinctrl property with a name. |
| #define | [DT\_INST\_PINCTRL\_BY\_IDX](group__devicetree-pinctrl.md#ga3388742fe3fb1f32a03566730890eaf0)(inst, pc\_idx, idx) |
|  | Get a node identifier for a phandle in a pinctrl property by index for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_0](group__devicetree-pinctrl.md#ga3cd59afe76bc5d82b63ef21cae451f11)(inst, idx) |
|  | Get a node identifier from a pinctrl-0 property for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_BY\_NAME](group__devicetree-pinctrl.md#ga4c171c27a91bd85e49b725bda6c05619)(inst, name, idx) |
|  | Get a node identifier for a phandle inside a pinctrl node for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_NAME\_TO\_IDX](group__devicetree-pinctrl.md#ga12c18d8d9724d98d121d8118b43686c3)(inst, name) |
|  | Convert a pinctrl name to its corresponding index for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_TOKEN](group__devicetree-pinctrl.md#ga80c3fb3defb7315877dc48db2932ef70)(inst, pc\_idx) |
|  | Convert a pinctrl index to its name as an uppercased token. |
| #define | [DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN](group__devicetree-pinctrl.md#ga6d01324cecb6db502c46c42817c56bc9)(inst, pc\_idx) |
|  | Convert a pinctrl index to its name as an uppercased token. |
| #define | [DT\_INST\_NUM\_PINCTRLS\_BY\_IDX](group__devicetree-pinctrl.md#ga1de8198573428ec717733204d91f0391)(inst, pc\_idx) |
|  | Get the number of phandles in a pinctrl property for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_NUM\_PINCTRLS\_BY\_NAME](group__devicetree-pinctrl.md#gae253489146c61cb075f06192948275ff)(inst, name) |
|  | Like [DT\_INST\_NUM\_PINCTRLS\_BY\_IDX()](group__devicetree-pinctrl.md#ga1de8198573428ec717733204d91f0391 "Get the number of phandles in a pinctrl property for a DT_DRV_COMPAT instance."), but by name instead. |
| #define | [DT\_INST\_NUM\_PINCTRL\_STATES](group__devicetree-pinctrl.md#ga4e91cf82c2a7aaecdb43761b217231d4)(inst) |
|  | Get the number of pinctrl properties in a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_PINCTRL\_HAS\_IDX](group__devicetree-pinctrl.md#ga53f17d0a6061cad7270544068f1cb003)(inst, pc\_idx) |
|  | Test if a DT\_DRV\_COMPAT instance has a pinctrl property with an index. |
| #define | [DT\_INST\_PINCTRL\_HAS\_NAME](group__devicetree-pinctrl.md#ga0e2af9dde68b57f6b1ffc86143fc2e40)(inst, name) |
|  | Test if a DT\_DRV\_COMPAT instance has a pinctrl property with a name. |

## Detailed Description

Devicetree pin control helpers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [pinctrl.h](devicetree_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
