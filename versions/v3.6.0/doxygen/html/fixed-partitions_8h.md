---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fixed-partitions_8h.html
original_path: doxygen/html/fixed-partitions_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fixed-partitions.h File Reference

Flash Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](fixed-partitions_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL](group__devicetree-fixed-partition.md#gafcd93790974c48b10dd1170d14c49bf9)(label) |
|  | Get a node identifier for a fixed partition with a given label property. |
| #define | [DT\_HAS\_FIXED\_PARTITION\_LABEL](group__devicetree-fixed-partition.md#gac402d149d6b527cccf5f955f1ad57fc3)(label) |
|  | Test if a fixed partition with a given label property exists. |
| #define | [DT\_FIXED\_PARTITION\_EXISTS](group__devicetree-fixed-partition.md#ga444fa975d314c342268a6d211627c3d1)(node\_id) |
|  | Test if fixed-partition compatible node exists. |
| #define | [DT\_FIXED\_PARTITION\_ID](group__devicetree-fixed-partition.md#gaf3b448e91dff79ece4d67ef833088ac9)(node\_id) |
|  | Get a numeric identifier for a fixed partition. |
| #define | [DT\_MEM\_FROM\_FIXED\_PARTITION](group__devicetree-fixed-partition.md#gae89b5f21fecae407f3b1baf231e4dba5)(node\_id) |
|  | Get the node identifier of the flash memory for a partition. |
| #define | [DT\_MTD\_FROM\_FIXED\_PARTITION](group__devicetree-fixed-partition.md#ga3484bb9a0cd8c2a4d971989dc58c194e)(node\_id) |
|  | Get the node identifier of the flash controller for a partition. |
| #define | [DT\_FIXED\_PARTITION\_ADDR](group__devicetree-fixed-partition.md#gac8be7ec2cddde3f76f0f096bd3c63546)(node\_id) |
|  | Get the absolute address of a fixed partition. |

## Detailed Description

Flash Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [fixed-partitions.h](fixed-partitions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
