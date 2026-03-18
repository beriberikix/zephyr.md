---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socketcan__utils_8h_source.html
original_path: doxygen/html/socketcan__utils_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socketcan\_utils.h

[Go to the documentation of this file.](socketcan__utils_8h.md)

1

6

7/\*

8 \* Copyright (c) 2019 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_UTILS\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_UTILS\_H\_

15

16#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

17#include <[zephyr/net/socketcan.h](socketcan_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

[ 36](group__socket__can.md#gaccedf1d7bf2131797e53a16dc93cd7e1)static inline void [socketcan\_to\_can\_frame](group__socket__can.md#gaccedf1d7bf2131797e53a16dc93cd7e1)(const struct [socketcan\_frame](structsocketcan__frame.md) \*sframe,

37 struct [can\_frame](structcan__frame.md) \*zframe)

38{

39 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(zframe, 0, sizeof(\*zframe));

40

41 zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) |= (sframe->[can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31)) != 0 ? [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3) : 0;

42 zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) |= (sframe->[can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30)) != 0 ? [CAN\_FRAME\_RTR](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f) : 0;

43 zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) |= (sframe->[flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d) & [CANFD\_FDF](group__socket__can.md#ga409cae306f00226ef192320f4f01f51c)) != 0 ? [CAN\_FRAME\_FDF](group__can__interface.md#ga22f85e1d16b93e46200f9673abdbb589) : 0;

44 zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) |= (sframe->[flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d) & [CANFD\_BRS](group__socket__can.md#gace1d124719f8eac5f59788811c4afaf4)) != 0 ? [CAN\_FRAME\_BRS](group__can__interface.md#ga1fdf15ce4a3b333488f9b630ec836d52) : 0;

45 zframe->[id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d) = sframe->[can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(29);

46 zframe->[dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47) = [can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)(sframe->[len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731));

47

48 if ((zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_RTR](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)) == 0U) {

49 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(zframe->[data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960), sframe->[data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623),

50 [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(sframe->[len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731), [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(sizeof(sframe->[data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)), sizeof(zframe->[data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)))));

51 }

52}

53

[ 60](group__socket__can.md#ga49ffbe49124fdc472946fd0978f9a6d5)static inline void [socketcan\_from\_can\_frame](group__socket__can.md#ga49ffbe49124fdc472946fd0978f9a6d5)(const struct [can\_frame](structcan__frame.md) \*zframe,

61 struct [socketcan\_frame](structsocketcan__frame.md) \*sframe)

62{

63 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sframe, 0, sizeof(\*sframe));

64

65 sframe->[can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) = zframe->[id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d);

66 sframe->[can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) |= (zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)) != 0 ? [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) : 0;

67 sframe->[can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6) |= (zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_RTR](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)) != 0 ? [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30) : 0;

68 sframe->[len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731) = [can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)(zframe->[dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47));

69

70 if ((zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_FDF](group__can__interface.md#ga22f85e1d16b93e46200f9673abdbb589)) != 0) {

71 sframe->[flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d) |= [CANFD\_FDF](group__socket__can.md#ga409cae306f00226ef192320f4f01f51c);

72 }

73

74 if ((zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_BRS](group__can__interface.md#ga1fdf15ce4a3b333488f9b630ec836d52)) != 0) {

75 sframe->[flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d) |= [CANFD\_BRS](group__socket__can.md#gace1d124719f8eac5f59788811c4afaf4);

76 }

77

78 if ((zframe->[flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c) & [CAN\_FRAME\_RTR](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)) == 0U) {

79 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(sframe->[data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623), zframe->[data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960),

80 [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(sframe->[len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731), [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(sizeof(zframe->[data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)), sizeof(sframe->[data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)))));

81 }

82}

83

[ 90](group__socket__can.md#ga040c4882d349cdc3c568f3580e823cba)static inline void [socketcan\_to\_can\_filter](group__socket__can.md#ga040c4882d349cdc3c568f3580e823cba)(const struct [socketcan\_filter](structsocketcan__filter.md) \*sfilter,

91 struct [can\_filter](structcan__filter.md) \*zfilter)

92{

93 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(zfilter, 0, sizeof(\*zfilter));

94

95 zfilter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) |= (sfilter->[can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31)) != 0 ? [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f) : 0;

96 zfilter->[id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9) = sfilter->[can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(29);

97 zfilter->[mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94) = sfilter->[can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9) & [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(29);

98}

99

[ 106](group__socket__can.md#gaf5cee7f0d6385c6fc4736e9399ed06b3)static inline void [socketcan\_from\_can\_filter](group__socket__can.md#gaf5cee7f0d6385c6fc4736e9399ed06b3)(const struct [can\_filter](structcan__filter.md) \*zfilter,

107 struct [socketcan\_filter](structsocketcan__filter.md) \*sfilter)

108{

109 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(sfilter, 0, sizeof(\*sfilter));

110

111 sfilter->[can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47) = zfilter->[id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9);

112 sfilter->[can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47) |= (zfilter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) != 0 ? [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) : 0;

113

114 sfilter->[can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9) = zfilter->[mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94);

115 sfilter->[can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9) |= (zfilter->[flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de) & [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)) != 0 ? [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) : 0;

116

117 if (![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_CAN\_ACCEPT\_RTR)) {

118 sfilter->[can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9) |= [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30);

119 }

120}

121

125

126#ifdef \_\_cplusplus

127}

128#endif

129

130#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKETCAN\_H\_ \*/

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[CAN\_FRAME\_BRS](group__can__interface.md#ga1fdf15ce4a3b333488f9b630ec836d52)

#define CAN\_FRAME\_BRS

Frame uses CAN FD Baud Rate Switch (BRS).

**Definition** can.h:160

[CAN\_FRAME\_FDF](group__can__interface.md#ga22f85e1d16b93e46200f9673abdbb589)

#define CAN\_FRAME\_FDF

Frame uses CAN FD format (FDF).

**Definition** can.h:157

[can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3)

static uint8\_t can\_bytes\_to\_dlc(uint8\_t num\_bytes)

Convert from number of bytes to Data Length Code (DLC).

**Definition** can.h:1754

[CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)

#define CAN\_FRAME\_IDE

Frame uses extended (29-bit) CAN ID.

**Definition** can.h:151

[can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601)

static uint8\_t can\_dlc\_to\_bytes(uint8\_t dlc)

Convert from Data Length Code (DLC) to the number of data bytes.

**Definition** can.h:1739

[CAN\_FRAME\_RTR](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)

#define CAN\_FRAME\_RTR

Frame is a Remote Transmission Request (RTR).

**Definition** can.h:154

[CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)

#define CAN\_FILTER\_IDE

Filter matches frames with extended (29-bit) CAN IDs.

**Definition** can.h:211

[socketcan\_to\_can\_filter](group__socket__can.md#ga040c4882d349cdc3c568f3580e823cba)

static void socketcan\_to\_can\_filter(const struct socketcan\_filter \*sfilter, struct can\_filter \*zfilter)

Translate a socketcan\_filter struct to a can\_filter struct.

**Definition** socketcan\_utils.h:90

[CANFD\_FDF](group__socket__can.md#ga409cae306f00226ef192320f4f01f51c)

#define CANFD\_FDF

Mark CAN FD for dual use of struct canfd\_frame.

**Definition** socketcan.h:64

[socketcan\_from\_can\_frame](group__socket__can.md#ga49ffbe49124fdc472946fd0978f9a6d5)

static void socketcan\_from\_can\_frame(const struct can\_frame \*zframe, struct socketcan\_frame \*sframe)

Translate a can\_frame struct to a socketcan\_frame struct.

**Definition** socketcan\_utils.h:60

[socketcan\_to\_can\_frame](group__socket__can.md#gaccedf1d7bf2131797e53a16dc93cd7e1)

static void socketcan\_to\_can\_frame(const struct socketcan\_frame \*sframe, struct can\_frame \*zframe)

Translate a socketcan\_frame struct to a can\_frame struct.

**Definition** socketcan\_utils.h:36

[CANFD\_BRS](group__socket__can.md#gace1d124719f8eac5f59788811c4afaf4)

#define CANFD\_BRS

Bit rate switch (second bitrate for payload data).

**Definition** socketcan.h:62

[socketcan\_from\_can\_filter](group__socket__can.md#gaf5cee7f0d6385c6fc4736e9399ed06b3)

static void socketcan\_from\_can\_filter(const struct can\_filter \*zfilter, struct socketcan\_filter \*sfilter)

Translate a can\_filter struct to a socketcan\_filter struct.

**Definition** socketcan\_utils.h:106

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:391

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

[socketcan.h](socketcan_8h.md)

SocketCAN definitions.

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:218

[can\_filter::mask](structcan__filter.md#a15632117f3f031fbbeb28ef562f9ac94)

uint32\_t mask

CAN identifier matching mask.

**Definition** can.h:224

[can\_filter::flags](structcan__filter.md#a7616e21f33be5fb43094d44530a1c5de)

uint8\_t flags

Flags.

**Definition** can.h:226

[can\_filter::id](structcan__filter.md#adf2b18eab11d360780707478a1f624b9)

uint32\_t id

CAN identifier to match.

**Definition** can.h:220

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:172

[can\_frame::dlc](structcan__frame.md#a014c42277e886906e6c761bc6f21fb47)

uint8\_t dlc

Data Length Code (DLC) indicating data length in bytes.

**Definition** can.h:176

[can\_frame::flags](structcan__frame.md#a1e71125342a01a6e5a68a14cb075ce7c)

uint8\_t flags

Flags.

**Definition** can.h:178

[can\_frame::id](structcan__frame.md#a7ad0d8d62322affafbfd23839ee81d5d)

uint32\_t id

Standard (11-bit) or extended (29-bit) CAN identifier.

**Definition** can.h:174

[can\_frame::data](structcan__frame.md#ac4b43443b2a338d35f0e1d3ef8355960)

uint8\_t data[CAN\_MAX\_DLEN]

Payload data accessed as unsigned 8 bit values.

**Definition** can.h:197

[socketcan\_filter](structsocketcan__filter.md)

CAN filter for Linux SocketCAN compatibility.

**Definition** socketcan.h:131

[socketcan\_filter::can\_mask](structsocketcan__filter.md#a841857f05f1e1a887be50d8e507a03f9)

socketcan\_id\_t can\_mask

The mask applied to can\_id for matching.

**Definition** socketcan.h:135

[socketcan\_filter::can\_id](structsocketcan__filter.md#a9217950edb190dc70783d9b87676ae47)

socketcan\_id\_t can\_id

The CAN identifier to match.

**Definition** socketcan.h:133

[socketcan\_frame](structsocketcan__frame.md)

CAN frame for Linux SocketCAN compatibility.

**Definition** socketcan.h:110

[socketcan\_frame::can\_id](structsocketcan__frame.md#a43511a491c9b8cf63b4ff592eb77a6e6)

socketcan\_id\_t can\_id

32-bit CAN ID + EFF/RTR/ERR flags.

**Definition** socketcan.h:112

[socketcan\_frame::data](structsocketcan__frame.md#a4ab22ff419e3c7397c64a1309cbdb623)

uint8\_t data[8U]

The payload data.

**Definition** socketcan.h:123

[socketcan\_frame::len](structsocketcan__frame.md#aa21e8007363ab0183c7b9d6c59cb4731)

uint8\_t len

Frame payload length in bytes.

**Definition** socketcan.h:114

[socketcan\_frame::flags](structsocketcan__frame.md#af9ddb322cdc3d886182cce65f673177d)

uint8\_t flags

Additional flags for CAN FD.

**Definition** socketcan.h:116

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socketcan\_utils.h](socketcan__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
