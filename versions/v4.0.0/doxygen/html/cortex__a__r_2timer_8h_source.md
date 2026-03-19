---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cortex__a__r_2timer_8h_source.html
original_path: doxygen/html/cortex__a__r_2timer_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timer.h

[Go to the documentation of this file.](cortex__a__r_2timer_8h.md)

1/\*

2 \* Copyright (c) 2021 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_TIMER\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_TIMER\_H\_

9

10#ifdef CONFIG\_ARM\_ARCH\_TIMER

11

12#ifndef \_ASMLANGUAGE

13

14#include <[zephyr/drivers/timer/arm\_arch\_timer.h](arm__arch__timer_8h.md)>

15#include <[zephyr/sys/device\_mmio.h](device__mmio_8h.md)>

16#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22#define ARM\_ARCH\_TIMER\_BASE DT\_REG\_ADDR\_BY\_IDX(ARM\_TIMER\_NODE, 0)

23#define ARM\_ARCH\_TIMER\_IRQ ARM\_TIMER\_VIRTUAL\_IRQ

24#define ARM\_ARCH\_TIMER\_PRIO ARM\_TIMER\_VIRTUAL\_PRIO

25#define ARM\_ARCH\_TIMER\_FLAGS ARM\_TIMER\_VIRTUAL\_FLAGS

26

27#define TIMER\_CNT\_LOWER 0x00

28#define TIMER\_CNT\_UPPER 0x04

29#define TIMER\_CTRL 0x08

30#define TIMER\_ISR 0x0c

31#define TIMER\_CMP\_LOWER 0x10

32#define TIMER\_CMP\_UPPER 0x14

33

34#define TIMER\_IRQ\_ENABLE BIT(2)

35#define TIMER\_COMP\_ENABLE BIT(1)

36#define TIMER\_ENABLE BIT(0)

37

38#define TIMER\_ISR\_EVENT\_FLAG BIT(0)

39

40[DEVICE\_MMIO\_TOPLEVEL\_STATIC](group__device-mmio-toplevel.md#ga80456633db67dbb23d32e2ae7cc93512)(timer\_regs, [ARM\_TIMER\_NODE](arm__arch__timer_8h.md#aea7a05797c3c8202e22fbde7784e6f42));

41

42#define TIMER\_REG\_GET(offs) (DEVICE\_MMIO\_TOPLEVEL\_GET(timer\_regs) + offs)

43

44static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_init](armv8__timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)(void)

45{

46 [DEVICE\_MMIO\_TOPLEVEL\_MAP](group__device-mmio-toplevel.md#ga6533dfab1e1bab2a11654abf4231379b)(timer\_regs, [K\_MEM\_CACHE\_NONE](group__kernel__memory__management.md#gaae7605452be94d1bd6e0364e9db113c6));

47}

48

49static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_set\_compare](armv8__timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

50{

51 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lower = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))val;

52 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) upper = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(val >> 32);

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl;

54

55 /\* Disable IRQ and comparator \*/

56 ctrl = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_CTRL));

57 ctrl &= ~(TIMER\_COMP\_ENABLE | TIMER\_IRQ\_ENABLE);

58 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(ctrl, TIMER\_REG\_GET(TIMER\_CTRL));

59

60 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(lower, TIMER\_REG\_GET(TIMER\_CMP\_LOWER));

61 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(upper, TIMER\_REG\_GET(TIMER\_CMP\_UPPER));

62

63 /\* enable comparator back, let set\_irq\_mask enabling the IRQ again \*/

64 ctrl |= TIMER\_COMP\_ENABLE;

65 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(ctrl, TIMER\_REG\_GET(TIMER\_CTRL));

66}

67

68#if defined(CONFIG\_ARM\_ARCH\_TIMER\_ERRATUM\_740657)

69

70/\*

71 \* R/W access to the event flag register is required for the timer errata

72 \* 740657 workaround -> comp. ISR implementation in arm\_arch\_timer.c.

73 \* This functionality is not present in the aarch64 implementation of the

74 \* ARM global timer access functions.

75 \*

76 \* comp. ARM Cortex-A9 processors Software Developers Errata Notice,

77 \* ARM document ID032315.

78 \*/

79

80static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) arm\_arch\_timer\_get\_int\_status(void)

81{

82 return ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))([sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_ISR)) & TIMER\_ISR\_EVENT\_FLAG);

83}

84

85static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arm\_arch\_timer\_clear\_int\_status(void)

86{

87 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(TIMER\_ISR\_EVENT\_FLAG, TIMER\_REG\_GET(TIMER\_ISR));

88}

89

90#endif /\* CONFIG\_ARM\_ARCH\_TIMER\_ERRATUM\_740657 \*/

91

92static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_enable](armv8__timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)(bool enable)

93{

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl;

95

96 ctrl = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_CTRL));

97 if (enable) {

98 ctrl |= TIMER\_ENABLE;

99 } else {

100 ctrl &= ~TIMER\_ENABLE;

101 }

102

103 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(ctrl, TIMER\_REG\_GET(TIMER\_CTRL));

104}

105

106static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arm\_arch\_timer\_set\_irq\_mask](armv8__timer_8h.md#a5969eb25741240dd0030acb92018038c)(bool mask)

107{

108 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl;

109

110 ctrl = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_CTRL));

111 if (mask) {

112 ctrl &= ~TIMER\_IRQ\_ENABLE;

113 } else {

114 ctrl |= TIMER\_IRQ\_ENABLE;

115 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(1, TIMER\_REG\_GET(TIMER\_ISR));

116 }

117 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(ctrl, TIMER\_REG\_GET(TIMER\_CTRL));

118}

119

120static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arm\_arch\_timer\_count](armv8__timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)(void)

121{

122 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lower;

123 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) upper, upper\_saved;

124

125 /\* To get the value from the Global Timer Counter register proceed

126 \* as follows:

127 \* 1. Read the upper 32-bit timer counter register.

128 \* 2. Read the lower 32-bit timer counter register.

129 \* 3. Read the upper 32-bit timer counter register again. If the value

130 \* is different to the 32-bit upper value read previously,

131 \* go back to step 2.

132 \* Otherwise the 64-bit timer counter value is correct.

133 \*/

134 upper = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_CNT\_UPPER));

135 do {

136 upper\_saved = upper;

137 lower = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_CNT\_LOWER));

138 upper = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(TIMER\_REG\_GET(TIMER\_CNT\_UPPER));

139 } while (upper != upper\_saved);

140

141 return (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))upper) << 32 | lower;

142}

143

144#ifdef \_\_cplusplus

145}

146#endif

147

148#endif /\* \_ASMLANGUAGE \*/

149

150#endif /\* CONFIG\_ARM\_ARCH\_TIMER \*/

151

152#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_CORTEX\_A\_R\_TIMER\_H\_ \*/

[arm\_arch\_timer.h](arm__arch__timer_8h.md)

[ARM\_TIMER\_NODE](arm__arch__timer_8h.md#aea7a05797c3c8202e22fbde7784e6f42)

#define ARM\_TIMER\_NODE

**Definition** arm\_arch\_timer.h:14

[arm\_arch\_timer\_count](armv8__timer_8h.md#a27c012fc420c6dab58e101b565bc1ed1)

static ALWAYS\_INLINE uint64\_t arm\_arch\_timer\_count(void)

**Definition** armv8\_timer.h:63

[arm\_arch\_timer\_set\_irq\_mask](armv8__timer_8h.md#a5969eb25741240dd0030acb92018038c)

static ALWAYS\_INLINE void arm\_arch\_timer\_set\_irq\_mask(bool mask)

**Definition** armv8\_timer.h:48

[arm\_arch\_timer\_set\_compare](armv8__timer_8h.md#ac2bf0a61b818c6d27eea31611471ed55)

static ALWAYS\_INLINE void arm\_arch\_timer\_set\_compare(uint64\_t val)

**Definition** armv8\_timer.h:28

[arm\_arch\_timer\_enable](armv8__timer_8h.md#acbb90cd040cb2ada7562aa68c386861e)

static ALWAYS\_INLINE void arm\_arch\_timer\_enable(unsigned char enable)

**Definition** armv8\_timer.h:33

[arm\_arch\_timer\_init](armv8__timer_8h.md#ada947e26d82e5ee70218ecde101eb85f)

static ALWAYS\_INLINE void arm\_arch\_timer\_init(void)

**Definition** armv8\_timer.h:24

[device\_mmio.h](device__mmio_8h.md)

[DEVICE\_MMIO\_TOPLEVEL\_MAP](group__device-mmio-toplevel.md#ga6533dfab1e1bab2a11654abf4231379b)

#define DEVICE\_MMIO\_TOPLEVEL\_MAP(name, flags)

Set up memory for a driver'sMMIO region.

**Definition** device\_mmio.h:715

[DEVICE\_MMIO\_TOPLEVEL\_STATIC](group__device-mmio-toplevel.md#ga80456633db67dbb23d32e2ae7cc93512)

#define DEVICE\_MMIO\_TOPLEVEL\_STATIC(name, node\_id)

Declare top-level storage for MMIO information, static scope.

**Definition** device\_mmio.h:661

[K\_MEM\_CACHE\_NONE](group__kernel__memory__management.md#gaae7605452be94d1bd6e0364e9db113c6)

#define K\_MEM\_CACHE\_NONE

No caching.

**Definition** mm.h:34

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:70

[sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)

static ALWAYS\_INLINE uint32\_t sys\_read32(mem\_addr\_t addr)

**Definition** sys-io-common.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [timer.h](cortex__a__r_2timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
