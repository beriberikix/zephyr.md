---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bluetooth_2byteorder_8h_source.html
original_path: doxygen/html/bluetooth_2byteorder_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

113

114#ifdef \_\_cplusplus

115}

116#endif

117

118#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_BYTEORDER\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [byteorder.h](bluetooth_2byteorder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
