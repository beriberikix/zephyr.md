---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mmu_2arm__mmu_8h_source.html
original_path: doxygen/html/mmu_2arm__mmu_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mmu.h

[Go to the documentation of this file.](mmu_2arm__mmu_8h.md)

1/\*

2 \* ARMv7 MMU support

3 \*

4 \* Copyright (c) 2021 Weidmueller Interface GmbH & Co. KG

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_AARCH32\_ARM\_MMU\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_AARCH32\_ARM\_MMU\_H\_

10

11#ifndef \_ASMLANGUAGE

12

13#include <[stdint.h](stdint_8h.md)>

14#include <[stdlib.h](stdlib_8h.md)>

15

16/\*

17 \* Comp.:

18 \* ARM Architecture Reference Manual, ARMv7-A and ARMv7-R edition,

19 \* ARM document ID DDI0406C Rev. d, March 2018

20 \* Memory type definitions:

21 \* Table B3-10, chap. B3.8.2, p. B3-1363f.

22 \* Outer / inner cache attributes for cacheable memory:

23 \* Table B3-11, chap. B3.8.2, p. B3-1364

24 \*/

25

26/\*

27 \* The following definitions are used when specifying a memory

28 \* range to be mapped at boot time using the MMU\_REGION\_ENTRY

29 \* macro.

30 \*/

[ 31](mmu_2arm__mmu_8h.md#aef13623eed6a774294ff117f0f1260d3)#define MT\_STRONGLY\_ORDERED BIT(0)

[ 32](mmu_2arm__mmu_8h.md#ab0d5bcaf320e734ca524c213bb950de1)#define MT\_DEVICE BIT(1)

[ 33](mmu_2arm__mmu_8h.md#a8b006dab179dfa8965dcef3ac302746d)#define MT\_NORMAL BIT(2)

[ 34](mmu_2arm__mmu_8h.md#aea34d2f5ddb576d5d54a82fa63778ce1)#define MT\_MASK 0x7

35

[ 36](mmu_2arm__mmu_8h.md#a798d4c3b727dc70d39bdce4485e75b63)#define MPERM\_R BIT(3)

[ 37](mmu_2arm__mmu_8h.md#a3a8f3c247e82832a527c9998daddab51)#define MPERM\_W BIT(4)

[ 38](mmu_2arm__mmu_8h.md#a18d392d8f4282d5e0f4b7b4950667a10)#define MPERM\_X BIT(5)

[ 39](mmu_2arm__mmu_8h.md#abcbc3a051ff2302bfcf9496220f572b1)#define MPERM\_UNPRIVILEGED BIT(6)

40

[ 41](mmu_2arm__mmu_8h.md#a8a5663c1705ebc0fed3165acedee100b)#define MATTR\_NON\_SECURE BIT(7)

[ 42](mmu_2arm__mmu_8h.md#a674920d803fe277dd364d324bd9de3d3)#define MATTR\_NON\_GLOBAL BIT(8)

[ 43](mmu_2arm__mmu_8h.md#a61a894a354c54f67395d0e9293e4cf31)#define MATTR\_SHARED BIT(9)

[ 44](mmu_2arm__mmu_8h.md#a67253d34ae4dc883c58116c1354f3e2d)#define MATTR\_CACHE\_OUTER\_WB\_WA BIT(10)

[ 45](mmu_2arm__mmu_8h.md#a47edb43bfd4a767ed8365d78aca9d4a6)#define MATTR\_CACHE\_OUTER\_WT\_nWA BIT(11)

[ 46](mmu_2arm__mmu_8h.md#a875777d8e87e20dc861d0439ddfcfd19)#define MATTR\_CACHE\_OUTER\_WB\_nWA BIT(12)

[ 47](mmu_2arm__mmu_8h.md#aefd9b92f9576e6565d02cd1902d97d33)#define MATTR\_CACHE\_INNER\_WB\_WA BIT(13)

[ 48](mmu_2arm__mmu_8h.md#a21ace71b252adcf3ef4903c28feb9254)#define MATTR\_CACHE\_INNER\_WT\_nWA BIT(14)

[ 49](mmu_2arm__mmu_8h.md#aa864871d6a9bcd964b356d16d284e6fa)#define MATTR\_CACHE\_INNER\_WB\_nWA BIT(15)

50

[ 51](mmu_2arm__mmu_8h.md#afa2923609302c3ae56b387ae2cc7d28f)#define MATTR\_MAY\_MAP\_L1\_SECTION BIT(16)

52

53/\*

54 \* The following macros are used for adding constant entries

55 \* mmu\_regions array of the mmu\_config struct. Use MMU\_REGION\_ENTRY

56 \* for the specification of mappings whose PA and VA differ,

57 \* the use of MMU\_REGION\_FLAT\_ENTRY always results in an identity

58 \* mapping, which are used for the mappings of the Zephyr image's

59 \* code and data.

60 \*/

[ 61](mmu_2arm__mmu_8h.md#a7ab46a0bcc5d7f2645f98067ed78ac8f)#define MMU\_REGION\_ENTRY(\_name, \_base\_pa, \_base\_va, \_size, \_attrs) \

62 {\

63 .name = \_name, \

64 .base\_pa = \_base\_pa, \

65 .base\_va = \_base\_va, \

66 .size = \_size, \

67 .attrs = \_attrs, \

68 }

69

[ 70](mmu_2arm__mmu_8h.md#a7a9f450388792a5c053dd227207d255f)#define MMU\_REGION\_FLAT\_ENTRY(name, adr, sz, attrs) \

71 MMU\_REGION\_ENTRY(name, adr, adr, sz, attrs)

72

73/\*

74 \* @brief Auto generate mmu region entry for node\_id

75 \*

76 \* Example usage:

77 \*

78 \* @code{.c}

79 \* DT\_FOREACH\_STATUS\_OKAY\_VARGS(nxp\_imx\_gpio,

80 \* MMU\_REGION\_DT\_FLAT\_ENTRY,

81 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

82 \* @endcode

83 \*

84 \* @note Since devicetree\_generated.h does not include

85 \* node\_id##\_P\_reg\_FOREACH\_PROP\_ELEM\* definitions,

86 \* we can't automate dts node with multiple reg

87 \* entries.

88 \*/

[ 89](mmu_2arm__mmu_8h.md#a345c9537de9d7439c853b7f5c275d0cf)#define MMU\_REGION\_DT\_FLAT\_ENTRY(node\_id, attrs) \

90 MMU\_REGION\_FLAT\_ENTRY(DT\_NODE\_FULL\_NAME(node\_id), \

91 DT\_REG\_ADDR(node\_id), \

92 DT\_REG\_SIZE(node\_id), \

93 attrs),

94

95/\*

96 \* @brief Auto generate mmu region entry for status = "okay"

97 \* nodes compatible to a driver

98 \*

99 \* Example usage:

100 \*

101 \* @code{.c}

102 \* MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(nxp\_imx\_gpio,

103 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

104 \* @endcode

105 \*

106 \* @note This is a wrapper of @ref MMU\_REGION\_DT\_FLAT\_ENTRY

107 \*/

[ 108](mmu_2arm__mmu_8h.md#a3266a39e2c823047ab9a9162be60daf4)#define MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(compat, attr) \

109 DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, \

110 MMU\_REGION\_DT\_FLAT\_ENTRY, attr)

111

112/\* Region definition data structure \*/

[ 113](structarm__mmu__region.md)struct [arm\_mmu\_region](structarm__mmu__region.md) {

114 /\* Region Base Physical Address \*/

[ 115](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78);

116 /\* Region Base Virtual Address \*/

[ 117](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3);

118 /\* Region size \*/

[ 119](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532) size\_t [size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532);

120 /\* Region Name \*/

[ 121](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2) const char \*[name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2);

122 /\* Region Attributes \*/

[ 123](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604);

124};

125

126/\* MMU configuration data structure \*/

[ 127](structarm__mmu__config.md)struct [arm\_mmu\_config](structarm__mmu__config.md) {

128 /\* Number of regions \*/

[ 129](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a);

130 /\* Regions \*/

[ 131](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5) const struct [arm\_mmu\_region](structarm__mmu__region.md) \*[mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5);

132};

133

134/\*

135 \* Reference to the MMU configuration.

136 \*

137 \* This struct is defined and populated for each SoC (in the SoC definition),

138 \* and holds the build-time configuration information for the fixed MMU

139 \* regions enabled during kernel initialization.

140 \*/

141extern const struct [arm\_mmu\_config](structarm__mmu__config.md) [mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216);

142

143int z\_arm\_mmu\_init(void);

144

145#endif /\* \_ASMLANGUAGE \*/

146

147#endif /\* ZEPHYR\_INCLUDE\_ARCH\_AARCH32\_ARM\_MMU\_H\_ \*/

[mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216)

const struct arm\_mmu\_config mmu\_config

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[stdlib.h](stdlib_8h.md)

[arm\_mmu\_config](structarm__mmu__config.md)

**Definition** arm\_mmu.h:127

[arm\_mmu\_config::mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5)

const struct arm\_mmu\_region \* mmu\_regions

**Definition** arm\_mmu.h:131

[arm\_mmu\_config::num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a)

uint32\_t num\_regions

**Definition** arm\_mmu.h:129

[arm\_mmu\_region](structarm__mmu__region.md)

**Definition** arm\_mmu.h:113

[arm\_mmu\_region::base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3)

uintptr\_t base\_va

**Definition** arm\_mmu.h:117

[arm\_mmu\_region::size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532)

size\_t size

**Definition** arm\_mmu.h:119

[arm\_mmu\_region::base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78)

uintptr\_t base\_pa

**Definition** arm\_mmu.h:115

[arm\_mmu\_region::name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2)

const char \* name

**Definition** arm\_mmu.h:121

[arm\_mmu\_region::attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604)

uint32\_t attrs

**Definition** arm\_mmu.h:123

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mmu](dir_f6f11dc85c806d5d35780c9904432735.md)
- [arm\_mmu.h](mmu_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
