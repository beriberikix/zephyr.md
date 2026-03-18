---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lc3_8h_source.html
original_path: doxygen/html/lc3_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lc3.h

[Go to the documentation of this file.](lc3_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020 Intel Corporation

8 \* Copyright (c) 2022-2024 Nordic Semiconductor ASA

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_LC3\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_LC3\_H\_

14

21

22#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

23#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h.md)>

24#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 48](group__BT__AUDIO__CODEC__LC3.md#ga8d679b241585ff5ebff0d97bb22dfda9)#define BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \

49 \_max\_frames\_per\_sdu) \

50 { \

51 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ, BT\_BYTES\_LIST\_LE16(\_freq)), \

52 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION, (\_duration)), \

53 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT, (\_chan\_count)), \

54 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN, \

55 BT\_BYTES\_LIST\_LE16(\_len\_min), \

56 BT\_BYTES\_LIST\_LE16(\_len\_max)), \

57 COND\_CODE\_1(\_max\_frames\_per\_sdu, (), \

58 (BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT, \

59 (\_max\_frames\_per\_sdu)))) \

60 }

61

[ 67](group__BT__AUDIO__CODEC__LC3.md#ga9b5d5e300a7b41060329dbdd2cd073f6)#define BT\_AUDIO\_CODEC\_CAP\_LC3\_META(\_prefer\_context) \

68 { \

69 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT, \

70 BT\_BYTES\_LIST\_LE16(\_prefer\_context)) \

71 }

72

[ 84](group__BT__AUDIO__CODEC__LC3.md#gac474746e7314ebf7ed77b8937191cdc1)#define BT\_AUDIO\_CODEC\_CAP\_LC3(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \

85 \_max\_frames\_per\_sdu, \_prefer\_context) \

86 BT\_AUDIO\_CODEC\_CAP(BT\_HCI\_CODING\_FORMAT\_LC3, 0x0000, 0x0000, \

87 BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA(\_freq, \_duration, \_chan\_count, \_len\_min, \

88 \_len\_max, \_max\_frames\_per\_sdu), \

89 BT\_AUDIO\_CODEC\_CAP\_LC3\_META(\_prefer\_context))

90

[ 101](group__BT__AUDIO__CODEC__LC3.md#ga497ff0aa1d7dcfeea6ec549e5fb155d6)#define BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu) \

102 { \

103 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_FREQ, (\_freq)), \

104 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_DURATION, (\_duration)), \

105 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC, BT\_BYTES\_LIST\_LE32(\_loc)), \

106 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN, BT\_BYTES\_LIST\_LE16(\_len)), \

107 COND\_CODE\_1(\_frames\_per\_sdu, (), \

108 (BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU, \

109 (\_frames\_per\_sdu)))) \

110 }

111

[ 113](group__BT__AUDIO__CODEC__LC3.md#ga2c00f8bd526305d878624c6f1b8030f8)#define BT\_AUDIO\_CODEC\_CFG\_LC3\_META(\_stream\_context) \

114 { \

115 BT\_AUDIO\_CODEC\_DATA(BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT, \

116 BT\_BYTES\_LIST\_LE16(\_stream\_context)) \

117 }

118

[ 129](group__BT__AUDIO__CODEC__LC3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)#define BT\_AUDIO\_CODEC\_LC3\_CONFIG(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context) \

130 BT\_AUDIO\_CODEC\_CFG( \

131 BT\_HCI\_CODING\_FORMAT\_LC3, 0x0000, 0x0000, \

132 BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu), \

133 BT\_AUDIO\_CODEC\_CFG\_LC3\_META(\_stream\_context))

134

135#ifdef \_\_cplusplus

136}

137#endif

138

142

143#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_LC3\_H\_ \*/

[byteorder.h](bluetooth_2byteorder_8h.md)

Bluetooth byteorder API.

[hci\_types.h](hci__types_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [lc3.h](lc3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
