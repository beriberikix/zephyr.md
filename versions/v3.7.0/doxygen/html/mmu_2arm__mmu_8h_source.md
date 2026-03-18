---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mmu_2arm__mmu_8h_source.html
original_path: doxygen/html/mmu_2arm__mmu_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

13/\*

14 \* Comp.:

15 \* ARM Architecture Reference Manual, ARMv7-A and ARMv7-R edition,

16 \* ARM document ID DDI0406C Rev. d, March 2018

17 \* Memory type definitions:

18 \* Table B3-10, chap. B3.8.2, p. B3-1363f.

19 \* Outer / inner cache attributes for cacheable memory:

20 \* Table B3-11, chap. B3.8.2, p. B3-1364

21 \*/

22

23/\*

24 \* The following definitions are used when specifying a memory

25 \* range to be mapped at boot time using the MMU\_REGION\_ENTRY

26 \* macro.

27 \*/

[ 28](mmu_2arm__mmu_8h.md#aef13623eed6a774294ff117f0f1260d3)#define MT\_STRONGLY\_ORDERED BIT(0)

[ 29](mmu_2arm__mmu_8h.md#ab0d5bcaf320e734ca524c213bb950de1)#define MT\_DEVICE BIT(1)

[ 30](mmu_2arm__mmu_8h.md#a8b006dab179dfa8965dcef3ac302746d)#define MT\_NORMAL BIT(2)

[ 31](mmu_2arm__mmu_8h.md#aea34d2f5ddb576d5d54a82fa63778ce1)#define MT\_MASK 0x7

32

[ 33](mmu_2arm__mmu_8h.md#a798d4c3b727dc70d39bdce4485e75b63)#define MPERM\_R BIT(3)

[ 34](mmu_2arm__mmu_8h.md#a3a8f3c247e82832a527c9998daddab51)#define MPERM\_W BIT(4)

[ 35](mmu_2arm__mmu_8h.md#a18d392d8f4282d5e0f4b7b4950667a10)#define MPERM\_X BIT(5)

[ 36](mmu_2arm__mmu_8h.md#abcbc3a051ff2302bfcf9496220f572b1)#define MPERM\_UNPRIVILEGED BIT(6)

37

[ 38](mmu_2arm__mmu_8h.md#a8a5663c1705ebc0fed3165acedee100b)#define MATTR\_NON\_SECURE BIT(7)

[ 39](mmu_2arm__mmu_8h.md#a674920d803fe277dd364d324bd9de3d3)#define MATTR\_NON\_GLOBAL BIT(8)

[ 40](mmu_2arm__mmu_8h.md#a61a894a354c54f67395d0e9293e4cf31)#define MATTR\_SHARED BIT(9)

[ 41](mmu_2arm__mmu_8h.md#a67253d34ae4dc883c58116c1354f3e2d)#define MATTR\_CACHE\_OUTER\_WB\_WA BIT(10)

[ 42](mmu_2arm__mmu_8h.md#a47edb43bfd4a767ed8365d78aca9d4a6)#define MATTR\_CACHE\_OUTER\_WT\_nWA BIT(11)

[ 43](mmu_2arm__mmu_8h.md#a875777d8e87e20dc861d0439ddfcfd19)#define MATTR\_CACHE\_OUTER\_WB\_nWA BIT(12)

[ 44](mmu_2arm__mmu_8h.md#aefd9b92f9576e6565d02cd1902d97d33)#define MATTR\_CACHE\_INNER\_WB\_WA BIT(13)

[ 45](mmu_2arm__mmu_8h.md#a21ace71b252adcf3ef4903c28feb9254)#define MATTR\_CACHE\_INNER\_WT\_nWA BIT(14)

[ 46](mmu_2arm__mmu_8h.md#aa864871d6a9bcd964b356d16d284e6fa)#define MATTR\_CACHE\_INNER\_WB\_nWA BIT(15)

47

[ 48](mmu_2arm__mmu_8h.md#afa2923609302c3ae56b387ae2cc7d28f)#define MATTR\_MAY\_MAP\_L1\_SECTION BIT(16)

49

50/\*

51 \* The following macros are used for adding constant entries

52 \* mmu\_regions array of the mmu\_config struct. Use MMU\_REGION\_ENTRY

53 \* for the specification of mappings whose PA and VA differ,

54 \* the use of MMU\_REGION\_FLAT\_ENTRY always results in an identity

55 \* mapping, which are used for the mappings of the Zephyr image's

56 \* code and data.

57 \*/

[ 58](mmu_2arm__mmu_8h.md#a7ab46a0bcc5d7f2645f98067ed78ac8f)#define MMU\_REGION\_ENTRY(\_name, \_base\_pa, \_base\_va, \_size, \_attrs) \

59 {\

60 .name = \_name, \

61 .base\_pa = \_base\_pa, \

62 .base\_va = \_base\_va, \

63 .size = \_size, \

64 .attrs = \_attrs, \

65 }

66

[ 67](mmu_2arm__mmu_8h.md#a7a9f450388792a5c053dd227207d255f)#define MMU\_REGION\_FLAT\_ENTRY(name, adr, sz, attrs) \

68 MMU\_REGION\_ENTRY(name, adr, adr, sz, attrs)

69

70/\*

71 \* @brief Auto generate mmu region entry for node\_id

72 \*

73 \* Example usage:

74 \*

75 \* @code{.c}

76 \* DT\_FOREACH\_STATUS\_OKAY\_VARGS(nxp\_imx\_gpio,

77 \* MMU\_REGION\_DT\_FLAT\_ENTRY,

78 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

79 \* @endcode

80 \*

81 \* @note Since devicetree\_generated.h does not include

82 \* node\_id##\_P\_reg\_FOREACH\_PROP\_ELEM\* definitions,

83 \* we can't automate dts node with multiple reg

84 \* entries.

85 \*/

[ 86](mmu_2arm__mmu_8h.md#a345c9537de9d7439c853b7f5c275d0cf)#define MMU\_REGION\_DT\_FLAT\_ENTRY(node\_id, attrs) \

87 MMU\_REGION\_FLAT\_ENTRY(DT\_NODE\_FULL\_NAME(node\_id), \

88 DT\_REG\_ADDR(node\_id), \

89 DT\_REG\_SIZE(node\_id), \

90 attrs),

91

92/\*

93 \* @brief Auto generate mmu region entry for status = "okay"

94 \* nodes compatible to a driver

95 \*

96 \* Example usage:

97 \*

98 \* @code{.c}

99 \* MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(nxp\_imx\_gpio,

100 \* (MT\_DEVICE\_nGnRnE | MT\_P\_RW\_U\_NA | MT\_NS))

101 \* @endcode

102 \*

103 \* @note This is a wrapper of @ref MMU\_REGION\_DT\_FLAT\_ENTRY

104 \*/

[ 105](mmu_2arm__mmu_8h.md#a3266a39e2c823047ab9a9162be60daf4)#define MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY(compat, attr) \

106 DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, \

107 MMU\_REGION\_DT\_FLAT\_ENTRY, attr)

108

109/\* Region definition data structure \*/

[ 110](structarm__mmu__region.md)struct [arm\_mmu\_region](structarm__mmu__region.md) {

111 /\* Region Base Physical Address \*/

[ 112](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78);

113 /\* Region Base Virtual Address \*/

[ 114](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3);

115 /\* Region size \*/

[ 116](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532) size\_t [size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532);

117 /\* Region Name \*/

[ 118](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2) const char \*[name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2);

119 /\* Region Attributes \*/

[ 120](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604);

121};

122

123/\* MMU configuration data structure \*/

[ 124](structarm__mmu__config.md)struct [arm\_mmu\_config](structarm__mmu__config.md) {

125 /\* Number of regions \*/

[ 126](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a);

127 /\* Regions \*/

[ 128](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5) const struct [arm\_mmu\_region](structarm__mmu__region.md) \*[mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5);

129};

130

131/\*

132 \* Reference to the MMU configuration.

133 \*

134 \* This struct is defined and populated for each SoC (in the SoC definition),

135 \* and holds the build-time configuration information for the fixed MMU

136 \* regions enabled during kernel initialization.

137 \*/

138extern const struct [arm\_mmu\_config](structarm__mmu__config.md) [mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216);

139

140int z\_arm\_mmu\_init(void);

141

142#endif /\* \_ASMLANGUAGE \*/

143

144#endif /\* ZEPHYR\_INCLUDE\_ARCH\_AARCH32\_ARM\_MMU\_H\_ \*/

[mmu\_config](mmu_2arm__mmu_8h.md#afb6753aab93fd940c3fc43c11a908216)

const struct arm\_mmu\_config mmu\_config

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[arm\_mmu\_config](structarm__mmu__config.md)

**Definition** arm\_mmu.h:124

[arm\_mmu\_config::mmu\_regions](structarm__mmu__config.md#a98267b2426c7fbf6cf7f8596005195c5)

const struct arm\_mmu\_region \* mmu\_regions

**Definition** arm\_mmu.h:128

[arm\_mmu\_config::num\_regions](structarm__mmu__config.md#ae3ad61d92f4d5a6c7d87c5546730f67a)

uint32\_t num\_regions

**Definition** arm\_mmu.h:126

[arm\_mmu\_region](structarm__mmu__region.md)

**Definition** arm\_mmu.h:110

[arm\_mmu\_region::base\_va](structarm__mmu__region.md#a43861340707e9ce8e25e7221e194edc3)

uintptr\_t base\_va

**Definition** arm\_mmu.h:114

[arm\_mmu\_region::size](structarm__mmu__region.md#a501975cbb6ff57c223dc8a43220be532)

size\_t size

**Definition** arm\_mmu.h:116

[arm\_mmu\_region::base\_pa](structarm__mmu__region.md#a69c68977967812f3f24f5fc3406eff78)

uintptr\_t base\_pa

**Definition** arm\_mmu.h:112

[arm\_mmu\_region::name](structarm__mmu__region.md#a6ddf903ada2e19f82eb9405a6d8318a2)

const char \* name

**Definition** arm\_mmu.h:118

[arm\_mmu\_region::attrs](structarm__mmu__region.md#acd528aff43956e69e17e70100a109604)

uint32\_t attrs

**Definition** arm\_mmu.h:120

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mmu](dir_f6f11dc85c806d5d35780c9904432735.md)
- [arm\_mmu.h](mmu_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
