---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/iar_8h_source.html
original_path: doxygen/html/iar_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iar.h

[Go to the documentation of this file.](iar_8h.md)

1/\*

2 \* Copyright (c) 2025 IAR Systems AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TOOLCHAIN\_IAR\_H\_

8#define ZEPHYR\_INCLUDE\_TOOLCHAIN\_IAR\_H\_

9

[ 10](iar_8h.md#a763b60a74b3b8917b8a91614f1d443e4)#define TOOLCHAIN\_HAS\_PRAGMA\_DIAG

11

12#define \_TOOLCHAIN\_DISABLE\_WARNING(warning) TOOLCHAIN\_PRAGMA(diag\_suppress = warning)

13#define \_TOOLCHAIN\_ENABLE\_WARNING(warning) TOOLCHAIN\_PRAGMA(diag\_default = warning)

14

[ 15](iar_8h.md#a1f08471f8dba6ce2a3e0f38bea73d7b5)#define TOOLCHAIN\_DISABLE\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(warning)

[ 16](iar_8h.md#a5365fdbb6323f48ddca9ab4149e9a561)#define TOOLCHAIN\_ENABLE\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(warning)

17

[ 18](iar_8h.md#aace39dc11f4da885c3a75210519cff13)#define TOOLCHAIN\_DISABLE\_IAR\_WARNING(warning) \_TOOLCHAIN\_DISABLE\_WARNING(warning)

[ 19](iar_8h.md#a8a1fc59f2665be53c4e183d295d91e15)#define TOOLCHAIN\_ENABLE\_IAR\_WARNING(warning) \_TOOLCHAIN\_ENABLE\_WARNING(warning)

20

21/\* Generic warnings \*/

22

23

31#ifndef TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER

[ 32](iar_8h.md#aef9c3722dc2b189226eb2e6223c080bf)#define TOOLCHAIN\_WARNING\_ADDRESS\_OF\_PACKED\_MEMBER Pa039

33#endif

34

42#ifndef TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS

[ 43](iar_8h.md#a8b81dbfdc3dde900a58540709a4f1dff)#define TOOLCHAIN\_WARNING\_ARRAY\_BOUNDS Pe001

44#endif

45

53#ifndef TOOLCHAIN\_WARNING\_ATTRIBUTES

[ 54](iar_8h.md#a5f5fef9bda4762c368f26c9028cdd34a)#define TOOLCHAIN\_WARNING\_ATTRIBUTES Pe1097

55#endif

56

65#ifndef TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR

[ 66](iar_8h.md#a003b55bfd0a8b95a4e57e419eb980a39)#define TOOLCHAIN\_WARNING\_DELETE\_NON\_VIRTUAL\_DTOR Pe001

67#endif

68

76#ifndef TOOLCHAIN\_WARNING\_EXTRA

[ 77](iar_8h.md#a64d8f26c21ee3639e82d93783e09387e)#define TOOLCHAIN\_WARNING\_EXTRA Pe001

78#endif

79

87#ifndef TOOLCHAIN\_WARNING\_NONNULL

[ 88](iar_8h.md#af990df9b277505b97d4c9c2549fffa9f)#define TOOLCHAIN\_WARNING\_NONNULL Pe001

89#endif

90

98#ifndef TOOLCHAIN\_WARNING\_POINTER\_ARITH

[ 99](iar_8h.md#a9c83552055a1817801dedc6655fc0cbf)#define TOOLCHAIN\_WARNING\_POINTER\_ARITH Pe1143

100#endif

101

109#ifndef TOOLCHAIN\_WARNING\_SHADOW

[ 110](iar_8h.md#ae917ae1adad468956fa5d28a50d10670)#define TOOLCHAIN\_WARNING\_SHADOW Pe001

111#endif

112

120#ifndef TOOLCHAIN\_WARNING\_UNUSED\_LABEL

[ 121](iar_8h.md#a49dfbc1f801e1f3ae9a0dfaee4b1b5c9)#define TOOLCHAIN\_WARNING\_UNUSED\_LABEL Pe001

122#endif

123

[ 131](iar_8h.md#ac567335f987f8f89640e22bd8e3e9385)#define TOOLCHAIN\_WARNING\_UNUSED\_VARIABLE Pe001

132

[ 133](iar_8h.md#af90e0047b2708d02d3f69cd019a584df)#define TOOLCHAIN\_WARNING\_UNUSED\_FUNCTION Pe001

134

135#ifdef \_\_ICCARM\_\_

136#include "[iar/iccarm.h](iccarm_8h.md)"

137#endif

138#ifdef \_\_ICCRISCV\_\_

139#include "iar/iccriscv.h"

140#endif

141

142#endif /\* ZEPHYR\_INCLUDE\_TOOLCHAIN\_ICCARM\_H\_ \*/

[iccarm.h](iccarm_8h.md)

ICCARM toolchain abstraction.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [toolchain](dir_be36829470ed0f3c1e0f3c9ff3246c22.md)
- [iar.h](iar_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
