---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ordinals_8h.html
original_path: doxygen/html/ordinals_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ordinals.h File Reference

Devicetree node dependency ordinals.
[More...](#details)

[Go to the source code of this file.](ordinals_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_DEP\_ORD](group__devicetree-dep-ord.md#ga5b96dccfd349dd0ddba1812aa942c1bd)(node\_id) |
|  | Get a node's dependency ordinal. |
| #define | [DT\_DEP\_ORD\_STR\_SORTABLE](group__devicetree-dep-ord.md#ga6c31d58b47d826f1a1de1e5d0044e2f7)(node\_id) |
|  | Get a node's dependency ordinal in string sortable form. |
| #define | [DT\_REQUIRES\_DEP\_ORDS](group__devicetree-dep-ord.md#ga22dd1b0c89eb5ddfbfdd1e723d44f509)(node\_id) |
|  | Get a list of dependency ordinals of a node's direct dependencies. |
| #define | [DT\_SUPPORTS\_DEP\_ORDS](group__devicetree-dep-ord.md#ga3f559e9a787792685ed08be124b374ae)(node\_id) |
|  | Get a list of dependency ordinals of what depends directly on a node. |
| #define | [DT\_INST\_DEP\_ORD](group__devicetree-dep-ord.md#ga9c5e6f36c6e7a250368177a9f0713f86)(inst) |
|  | Get a DT\_DRV\_COMPAT instance's dependency ordinal. |
| #define | [DT\_INST\_REQUIRES\_DEP\_ORDS](group__devicetree-dep-ord.md#gac7d43a7916bdc8c46fafeee0213e538c)(inst) |
|  | Get a list of dependency ordinals of a DT\_DRV\_COMPAT instance's direct dependencies. |
| #define | [DT\_INST\_SUPPORTS\_DEP\_ORDS](group__devicetree-dep-ord.md#ga027cc1361d1e059dde039926980e26fa)(inst) |
|  | Get a list of dependency ordinals of what depends directly on a DT\_DRV\_COMPAT instance. |

## Detailed Description

Devicetree node dependency ordinals.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [ordinals.h](ordinals_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
