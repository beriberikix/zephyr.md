---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree__regions_8h_source.html
original_path: doxygen/html/devicetree__regions_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree\_regions.h

[Go to the documentation of this file.](devicetree__regions_8h.md)

1/\*

2 \* Copyright (c) 2021, Commonwealth Scientific and Industrial Research

3 \* Organisation (CSIRO) ABN 41 687 119 230.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*

7 \* Generate memory regions from devicetree nodes.

8 \*/

9

10#ifndef ZEPHYR\_INCLUDE\_LINKER\_DEVICETREE\_REGIONS\_H\_

11#define ZEPHYR\_INCLUDE\_LINKER\_DEVICETREE\_REGIONS\_H\_

12

13#include <[zephyr/devicetree.h](devicetree_8h.md)>

14#include <[zephyr/sys/util.h](sys_2util_8h.md)>

15#include <[zephyr/toolchain.h](toolchain_8h.md)>

16

[ 48](devicetree__regions_8h.md#a9df6c66f56e571a0dada9ab46b40ba26)#define LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id) \

49 DT\_STRING\_TOKEN(node\_id, zephyr\_memory\_region)

50

[ 82](devicetree__regions_8h.md#a3244e16032cc575ab5c7275caca14801)#define LINKER\_DT\_NODE\_REGION\_NAME(node\_id) \

83 STRINGIFY(LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id))

84

86

87#define \_DT\_COMPATIBLE zephyr\_memory\_region

88

89#define \_DT\_SECTION\_PREFIX(node\_id) UTIL\_CAT(\_\_, LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id))

90#define \_DT\_SECTION\_START(node\_id) UTIL\_CAT(\_DT\_SECTION\_PREFIX(node\_id), \_start)

91#define \_DT\_SECTION\_END(node\_id) UTIL\_CAT(\_DT\_SECTION\_PREFIX(node\_id), \_end)

92#define \_DT\_SECTION\_SIZE(node\_id) UTIL\_CAT(\_DT\_SECTION\_PREFIX(node\_id), \_size)

93#define \_DT\_SECTION\_LOAD(node\_id) UTIL\_CAT(\_DT\_SECTION\_PREFIX(node\_id), \_load\_start)

94

117#define \_REGION\_DECLARE(node\_id) \

118 LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id) : \

119 ORIGIN = DT\_REG\_ADDR(node\_id), \

120 LENGTH = DT\_REG\_SIZE(node\_id)

121

152#define \_SECTION\_DECLARE(node\_id) \

153 LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id) (NOLOAD) : \

154 { \

155 \_DT\_SECTION\_START(node\_id) = .; \

156 KEEP(\*(LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id))) \

157 KEEP(\*(LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id).\*)) \

158 \_DT\_SECTION\_END(node\_id) = .; \

159 } > LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id) \

160 \_DT\_SECTION\_SIZE(node\_id) = \_DT\_SECTION\_END(node\_id) - \_DT\_SECTION\_START(node\_id); \

161 \_DT\_SECTION\_LOAD(node\_id) = LOADADDR(LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id));

162

164

[ 173](devicetree__regions_8h.md#a1b743e1c6c735c87d4fbd2094819c573)#define LINKER\_DT\_REGIONS() \

174 DT\_FOREACH\_STATUS\_OKAY(\_DT\_COMPATIBLE, \_REGION\_DECLARE)

175

[ 180](devicetree__regions_8h.md#a171f1425c840f60dd94722ff046e0e81)#define LINKER\_DT\_SECTIONS() \

181 DT\_FOREACH\_STATUS\_OKAY(\_DT\_COMPATIBLE, \_SECTION\_DECLARE)

182

183#endif /\* ZEPHYR\_INCLUDE\_LINKER\_DEVICETREE\_REGIONS\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [devicetree\_regions.h](devicetree__regions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
