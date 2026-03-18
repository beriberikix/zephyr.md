---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fixed-partitions_8h_source.html
original_path: doxygen/html/fixed-partitions_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fixed-partitions.h

[Go to the documentation of this file.](fixed-partitions_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020, Linaro Ltd.

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_FIXED\_PARTITION\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_FIXED\_PARTITION\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 52](group__devicetree-fixed-partition.md#gafcd93790974c48b10dd1170d14c49bf9)#define DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL(label) \

53 DT\_CAT(DT\_COMPAT\_fixed\_partitions\_LABEL\_, label)

54

[ 61](group__devicetree-fixed-partition.md#gac402d149d6b527cccf5f955f1ad57fc3)#define DT\_HAS\_FIXED\_PARTITION\_LABEL(label) \

62 IS\_ENABLED(DT\_CAT3(DT\_COMPAT\_fixed\_partitions\_LABEL\_, label, \_EXISTS))

63

[ 70](group__devicetree-fixed-partition.md#ga444fa975d314c342268a6d211627c3d1)#define DT\_FIXED\_PARTITION\_EXISTS(node\_id) \

71 DT\_NODE\_HAS\_COMPAT(DT\_PARENT(node\_id), fixed\_partitions)

72

[ 78](group__devicetree-fixed-partition.md#gaf3b448e91dff79ece4d67ef833088ac9)#define DT\_FIXED\_PARTITION\_ID(node\_id) DT\_CAT(node\_id, \_PARTITION\_ID)

79

[ 86](group__devicetree-fixed-partition.md#gae89b5f21fecae407f3b1baf231e4dba5)#define DT\_MEM\_FROM\_FIXED\_PARTITION(node\_id) \

87 COND\_CODE\_1(DT\_NODE\_HAS\_COMPAT(DT\_GPARENT(node\_id), soc\_nv\_flash), (DT\_GPARENT(node\_id)), \

88 (DT\_INVALID\_NODE))

89

[ 96](group__devicetree-fixed-partition.md#ga3484bb9a0cd8c2a4d971989dc58c194e)#define DT\_MTD\_FROM\_FIXED\_PARTITION(node\_id) \

97 COND\_CODE\_1(DT\_NODE\_EXISTS(DT\_MEM\_FROM\_FIXED\_PARTITION(node\_id)), \

98 (DT\_PARENT(DT\_MEM\_FROM\_FIXED\_PARTITION(node\_id))), (DT\_GPARENT(node\_id)))

99

[ 133](group__devicetree-fixed-partition.md#gac8be7ec2cddde3f76f0f096bd3c63546)#define DT\_FIXED\_PARTITION\_ADDR(node\_id) \

134 (DT\_REG\_ADDR(DT\_MEM\_FROM\_FIXED\_PARTITION(node\_id)) + DT\_REG\_ADDR(node\_id))

135

139

140#ifdef \_\_cplusplus

141}

142#endif

143

144#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_FIXED\_PARTITION\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [fixed-partitions.h](fixed-partitions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
