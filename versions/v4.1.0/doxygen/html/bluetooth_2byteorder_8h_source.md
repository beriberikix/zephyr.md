---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bluetooth_2byteorder_8h_source.html
original_path: doxygen/html/bluetooth_2byteorder_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

byteorder.h

[Go to the documentation of this file.](bluetooth_2byteorder_8h.md)

1

4

5/\*

6 \* Copyright (c) 2023 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_BYTEORDER\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_BYTEORDER\_H\_

13

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

25

[ 36](group__bt__byteorder.md#ga83b5828023306b4bbf354ca3d6d6c6f2)#define BT\_BYTES\_LIST\_LE16(\_v) \

37 (((\_v) >> 0) & 0xFFU), \

38 (((\_v) >> 8) & 0xFFU) \

39

40

[ 50](group__bt__byteorder.md#ga68d63372c0b7e981d7ae715250c42261)#define BT\_BYTES\_LIST\_LE24(\_v) \

51 BT\_BYTES\_LIST\_LE16(\_v), \

52 (((\_v) >> 16) & 0xFFU) \

53

54

[ 64](group__bt__byteorder.md#ga0bf0275f0eea70eb5ae6002edeb1b812)#define BT\_BYTES\_LIST\_LE32(\_v) \

65 BT\_BYTES\_LIST\_LE24(\_v), \

66 (((\_v) >> 24) & 0xFFU) \

67

68

[ 78](group__bt__byteorder.md#gadd963cf0f7898e5e143b5d2fd79839ef)#define BT\_BYTES\_LIST\_LE40(\_v) \

79 BT\_BYTES\_LIST\_LE24(\_v), \

80 BT\_BYTES\_LIST\_LE16((\_v) >> 24) \

81

82

[ 92](group__bt__byteorder.md#ga6211946252ccd004f8ed35addee462f6)#define BT\_BYTES\_LIST\_LE48(\_v) \

93 BT\_BYTES\_LIST\_LE32(\_v), \

94 BT\_BYTES\_LIST\_LE16((\_v) >> 32) \

95

96

[ 106](group__bt__byteorder.md#ga52500bb74dcf28535cb70823ce8aed18)#define BT\_BYTES\_LIST\_LE64(\_v) \

107 BT\_BYTES\_LIST\_LE32(\_v), \

108 BT\_BYTES\_LIST\_LE32((\_v) >> 32) \

109

110

[ 120](group__bt__byteorder.md#ga50c0737d9c82bd8d86839614e5dc35f7)#define BT\_BYTES\_LIST\_BE16(\_v) (((\_v) >> 8) & 0xFFU), (((\_v) >> 0) & 0xFFU)

121

[ 132](group__bt__byteorder.md#ga0c728bcd2941ef6d5c5b174dcede4f54)#define BT\_BYTES\_LIST\_BE24(\_v) (((\_v) >> 16) & 0xFFU), BT\_BYTES\_LIST\_BE16(\_v)

133

[ 144](group__bt__byteorder.md#gab6ccd0fdb5f6d2d5214465037388f470)#define BT\_BYTES\_LIST\_BE32(\_v) (((\_v) >> 24) & 0xFFU), BT\_BYTES\_LIST\_BE24(\_v)

145

[ 156](group__bt__byteorder.md#ga346b3e8d3b98fd7d532a191459f51a96)#define BT\_BYTES\_LIST\_BE40(\_v) BT\_BYTES\_LIST\_BE16((\_v) >> 24), BT\_BYTES\_LIST\_BE24(\_v)

157

[ 168](group__bt__byteorder.md#gad7af352ecb0f523fbd566adc1f04664a)#define BT\_BYTES\_LIST\_BE48(\_v) BT\_BYTES\_LIST\_BE16((\_v) >> 32), BT\_BYTES\_LIST\_BE32(\_v)

169

[ 180](group__bt__byteorder.md#gaec9f6617a3e8b10f381c6fa51a513593)#define BT\_BYTES\_LIST\_BE64(\_v) BT\_BYTES\_LIST\_BE32((\_v) >> 32), BT\_BYTES\_LIST\_BE32(\_v)

181

185

186#ifdef \_\_cplusplus

187}

188#endif

189

190#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BYTEORDER\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [byteorder.h](bluetooth_2byteorder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
