---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/4_2lib__helpers_8h_source.html
original_path: doxygen/html/4_2lib__helpers_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lib\_helpers.h

[Go to the documentation of this file.](4_2lib__helpers_8h.md)

1/\*

2 \* Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM64\_LIB\_HELPERS\_H\_

8#define ZEPHYR\_INCLUDE\_ARCH\_ARM64\_LIB\_HELPERS\_H\_

9

10#ifndef \_ASMLANGUAGE

11

12#include <[zephyr/arch/arm64/cpu.h](arm64_2cpu_8h.md)>

13#include <[stdint.h](stdint_8h.md)>

14

15/\* All the macros need a memory clobber \*/

16

[ 17](4_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)#define read\_sysreg(reg) \

18({ \

19 uint64\_t reg\_val; \

20 \_\_asm\_\_ volatile ("mrs %0, " STRINGIFY(reg) \

21 : "=r" (reg\_val) :: "memory"); \

22 reg\_val; \

23})

24

[ 25](4_2lib__helpers_8h.md#adfcf211009c840e6f89530db728f9047)#define write\_sysreg(val, reg) \

26({ \

27 \_\_asm\_\_ volatile ("msr " STRINGIFY(reg) ", %0" \

28 :: "r" (val) : "memory"); \

29})

30

[ 31](4_2lib__helpers_8h.md#a71bba9d3a17e4940df59c934c24910c2)#define zero\_sysreg(reg) \

32({ \

33 \_\_asm\_\_ volatile ("msr " STRINGIFY(reg) ", xzr" \

34 ::: "memory"); \

35})

36

[ 37](4_2lib__helpers_8h.md#a3d4f0150b724754e8a1aaf8ca594eee1)#define MAKE\_REG\_HELPER(reg) \

38 static ALWAYS\_INLINE uint64\_t read\_##reg(void) \

39 { \

40 return read\_sysreg(reg); \

41 } \

42 static ALWAYS\_INLINE void write\_##reg(uint64\_t val) \

43 { \

44 write\_sysreg(val, reg); \

45 } \

46 static ALWAYS\_INLINE void zero\_##reg(void) \

47 { \

48 zero\_sysreg(reg); \

49 }

50

[ 51](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)#define MAKE\_REG\_HELPER\_EL123(reg) \

52 MAKE\_REG\_HELPER(reg##\_el1) \

53 MAKE\_REG\_HELPER(reg##\_el2) \

54 MAKE\_REG\_HELPER(reg##\_el3)

55

[ 56](4_2lib__helpers_8h.md#ac1121f82e3e380c62f9a67c715ba8677)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(ccsidr\_el1);

[ 57](4_2lib__helpers_8h.md#a99653091c171cac6f776e2907ac3d650)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(clidr\_el1);

[ 58](4_2lib__helpers_8h.md#a258a47c46f638d2d41b30cff783ac247)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cntfrq\_el0);

[ 59](4_2lib__helpers_8h.md#a365533eca13537bbcc213bf3f81c99ca)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cnthctl\_el2);

[ 60](4_2lib__helpers_8h.md#a92fe38d7dc9ff6dfe94cecd817e5e114)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cnthp\_ctl\_el2);

[ 61](4_2lib__helpers_8h.md#a2541497f8943726a17bfc92a20db8c7b)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cnthps\_ctl\_el2);

[ 62](4_2lib__helpers_8h.md#ab8455d86f57ccec61fa1ad6784c573f7)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cntv\_ctl\_el0)

[ 63](4_2lib__helpers_8h.md#abbcd760c3f58b5c7059fb3737532ea27)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cntv\_cval\_el0)

[ 64](4_2lib__helpers_8h.md#a0e7c74f6816ea2107dca43a9d32de547)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cntvct\_el0);

[ 65](4_2lib__helpers_8h.md#a37f4664b1135f74548febe1277208d52)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(cntvoff\_el2);

[ 66](4_2lib__helpers_8h.md#ab8bf450426e6ffd01784e74a89b368e5)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(currentel);

[ 67](4_2lib__helpers_8h.md#a65b1b152322196bdbc0e62ed95d12232)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(csselr\_el1);

[ 68](4_2lib__helpers_8h.md#a973d6a3b1193bde3f6ac9a1724c6a00d)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(daif)

[ 69](4_2lib__helpers_8h.md#a89b8f2d4ea6411ec86d645ae1fb98aad)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(hcr\_el2);

[ 70](4_2lib__helpers_8h.md#a38462e114f3f2c73503e48cf02df81c6)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(id\_aa64pfr0\_el1);

[ 71](4_2lib__helpers_8h.md#af4e219eb3d55882641f8094fac36b95b)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(id\_aa64mmfr0\_el1);

[ 72](4_2lib__helpers_8h.md#a91995e9b71b5f1f20dedbb03e936f72d)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(mpidr\_el1);

[ 73](4_2lib__helpers_8h.md#a92d207ebc45d5dd145e55540c4cb9e36)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(par\_el1);

74#if !defined(CONFIG\_ARMV8\_R)

[ 75](4_2lib__helpers_8h.md#a2ecebc3990ec0603018199b9682c0cc3)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(scr\_el3);

76#endif /\* CONFIG\_ARMV8\_R \*/

[ 77](4_2lib__helpers_8h.md#a5d96400189d120420955eec6d7229490)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(tpidrro\_el0);

[ 78](4_2lib__helpers_8h.md#ae946a95c234051b71c028d2b7d9de0e8)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(vmpidr\_el2);

[ 79](4_2lib__helpers_8h.md#abe1d7328798802e0d21d2ff4872dcafe)[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(sp\_el0);

80

[ 81](4_2lib__helpers_8h.md#a4c6d250f1d7fa3d6e29f2f2ba72e4814)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(actlr)

[ 82](4_2lib__helpers_8h.md#af51b5eb362da6a7b8a68d2fb2ddbe453)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(cpacr)

[ 83](4_2lib__helpers_8h.md#a349cf93efd70254bd3e5fbef197cc052)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(cptr)

[ 84](4_2lib__helpers_8h.md#a2a485cffc625f93557920bf4133aece1)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(elr)

[ 85](4_2lib__helpers_8h.md#a76bd170ab59044a86a84104860eed913)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(esr)

[ 86](4_2lib__helpers_8h.md#a79b816489c74dbd265c09756022c122b)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(far)

[ 87](4_2lib__helpers_8h.md#a84567a9ef9c0acae2f49504794f05d22)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(mair)

[ 88](4_2lib__helpers_8h.md#a2c94db4a9a4365c193d8f62566777369)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(sctlr)

[ 89](4_2lib__helpers_8h.md#ab4ca33b42893a69e295387244ff9ee66)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(spsr)

[ 90](4_2lib__helpers_8h.md#a77716d5dbbee548d5c7864c48efd9929)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(tcr)

[ 91](4_2lib__helpers_8h.md#a90c8f409355b33084a8976c9cf88d957)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(ttbr0)

[ 92](4_2lib__helpers_8h.md#a32582c152b47e0a3119ce4f2421850d9)[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)(vbar)

93

94#if defined(CONFIG\_ARM\_MPU)

95/\* Armv8-R aarch64 mpu registers \*/

96#define mpuir\_el1 S3\_0\_c0\_c0\_4

97#define prselr\_el1 S3\_0\_c6\_c2\_1

98#define prbar\_el1 S3\_0\_c6\_c8\_0

99#define prlar\_el1 S3\_0\_c6\_c8\_1

100

101[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(mpuir\_el1);

102[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(prselr\_el1);

103[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(prbar\_el1);

104[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(prlar\_el1);

105#endif

106

[ 107](4_2lib__helpers_8h.md#aa10827ab07d53a97a2a0eef88a34cdc1)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [enable\_debug\_exceptions](4_2lib__helpers_8h.md#aa10827ab07d53a97a2a0eef88a34cdc1)(void)

108{

109 \_\_asm\_\_ volatile ("msr DAIFClr, %0"

110 :: "i" ([DAIFCLR\_DBG\_BIT](arm64_2cpu_8h.md#afb4bae58d424e6460802949ef0355d21)) : "memory");

111}

112

[ 113](4_2lib__helpers_8h.md#a6124913695b3152818ca0c8338145522)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [disable\_debug\_exceptions](4_2lib__helpers_8h.md#a6124913695b3152818ca0c8338145522)(void)

114{

115 \_\_asm\_\_ volatile ("msr DAIFSet, %0"

116 :: "i" ([DAIFSET\_DBG\_BIT](arm64_2cpu_8h.md#ae8f3edaddcaaf22a1155da424838b326)) : "memory");

117}

118

[ 119](4_2lib__helpers_8h.md#ab6fafccc9d37b2b9af7ec37a4bbfea92)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [enable\_serror\_exceptions](4_2lib__helpers_8h.md#ab6fafccc9d37b2b9af7ec37a4bbfea92)(void)

120{

121 \_\_asm\_\_ volatile ("msr DAIFClr, %0"

122 :: "i" ([DAIFCLR\_ABT\_BIT](arm64_2cpu_8h.md#a21a0f602ba0c8b87cc082e3e13aa5d98)) : "memory");

123}

124

[ 125](4_2lib__helpers_8h.md#a316d3a4385241a3ff7032a8d34067a38)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [disable\_serror\_exceptions](4_2lib__helpers_8h.md#a316d3a4385241a3ff7032a8d34067a38)(void)

126{

127 \_\_asm\_\_ volatile ("msr DAIFSet, %0"

128 :: "i" ([DAIFSET\_ABT\_BIT](arm64_2cpu_8h.md#a4a9605b3286e62a9d878c7cfdccbf6f6)) : "memory");

129}

130

[ 131](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf)(void)

132{

133 \_\_asm\_\_ volatile ("msr DAIFClr, %0"

134 :: "i" ([DAIFCLR\_IRQ\_BIT](arm64_2cpu_8h.md#a6f6ae405bbde72ffef083bca9448269b)) : "memory");

135}

136

[ 137](4_2lib__helpers_8h.md#a86526fa2425a30ae46957d0480a09f25)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [disable\_irq](4_2lib__helpers_8h.md#a86526fa2425a30ae46957d0480a09f25)(void)

138{

139 \_\_asm\_\_ volatile ("msr DAIFSet, %0"

140 :: "i" ([DAIFSET\_IRQ\_BIT](arm64_2cpu_8h.md#a22d4cee27b78fddece088591958ca037)) : "memory");

141}

142

[ 143](4_2lib__helpers_8h.md#acca0372b859951afad2cc70c1ef9742f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [enable\_fiq](4_2lib__helpers_8h.md#acca0372b859951afad2cc70c1ef9742f)(void)

144{

145 \_\_asm\_\_ volatile ("msr DAIFClr, %0"

146 :: "i" ([DAIFCLR\_FIQ\_BIT](arm64_2cpu_8h.md#abf5cf8b639767836af6967f6d07e07b3)) : "memory");

147}

148

[ 149](4_2lib__helpers_8h.md#a971a94499a6e9949d79305c234329a10)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [disable\_fiq](4_2lib__helpers_8h.md#a971a94499a6e9949d79305c234329a10)(void)

150{

151 \_\_asm\_\_ volatile ("msr DAIFSet, %0"

152 :: "i" ([DAIFSET\_FIQ\_BIT](arm64_2cpu_8h.md#a53fb1a3ffce153d445525392fb411687)) : "memory");

153}

154

[ 155](4_2lib__helpers_8h.md#a544cc6885da9c2a5fb66a2a788d2ae41)#define sev() \_\_asm\_\_ volatile("sev" : : : "memory")

[ 156](4_2lib__helpers_8h.md#aa97b536857f20cc5b809240da5c6b0b4)#define wfe() \_\_asm\_\_ volatile("wfe" : : : "memory")

[ 157](4_2lib__helpers_8h.md#a7a7ae42b8fd0fc5548e2bc49d20e14d3)#define wfi() \_\_asm\_\_ volatile("wfi" : : : "memory")

158

[ 159](4_2lib__helpers_8h.md#a666bed8ddc768e8c5b75a1cb2d270df1)static inline bool [is\_el\_implemented](4_2lib__helpers_8h.md#a666bed8ddc768e8c5b75a1cb2d270df1)(unsigned int el)

160{

161 unsigned int shift;

162

163 if (el > 3) {

164 return false;

165 }

166

167 shift = [ID\_AA64PFR0\_EL1\_SHIFT](arm64_2cpu_8h.md#a9add6e194aac9e74e71c2dc2dd025eb7) \* el;

168

169 return ((([read\_id\_aa64pfr0\_el1](4_2lib__helpers_8h.md#a38462e114f3f2c73503e48cf02df81c6)() >> shift) & [ID\_AA64PFR0\_ELX\_MASK](arm64_2cpu_8h.md#ad296dae475a3598559cb5f53d74a62b0)) != 0U);

170}

171

[ 172](4_2lib__helpers_8h.md#a819e9a0d12d5273f526f0485600e7c28)static inline bool [is\_el\_highest\_implemented](4_2lib__helpers_8h.md#a819e9a0d12d5273f526f0485600e7c28)(void)

173{

174 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) el\_highest;

175 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) curr\_el;

176

177 el\_highest = [read\_id\_aa64pfr0\_el1](4_2lib__helpers_8h.md#a38462e114f3f2c73503e48cf02df81c6)() & 0xFFFF;

178 el\_highest = (31U - \_\_builtin\_clz(el\_highest)) / 4;

179

180 curr\_el = [GET\_EL](arm64_2cpu_8h.md#a16a04b233cad3fb65cb16dbeff32f8f2)([read\_currentel](4_2lib__helpers_8h.md#ab8bf450426e6ffd01784e74a89b368e5)());

181

182 if (curr\_el < el\_highest)

183 return false;

184

185 return true;

186}

187

[ 188](4_2lib__helpers_8h.md#aff5c60debe8b01feaf857df6940d9e28)static inline bool [is\_el2\_sec\_supported](4_2lib__helpers_8h.md#aff5c60debe8b01feaf857df6940d9e28)(void)

189{

190 return ((([read\_id\_aa64pfr0\_el1](4_2lib__helpers_8h.md#a38462e114f3f2c73503e48cf02df81c6)() >> [ID\_AA64PFR0\_SEL2\_SHIFT](arm64_2cpu_8h.md#a7ebf5636fdc14822cb8bbe10c7f2e1b4)) &

191 [ID\_AA64PFR0\_SEL2\_MASK](arm64_2cpu_8h.md#a233d4971a3bcb773cfe17e4dbe0ee750)) != 0U);

192}

193

[ 194](4_2lib__helpers_8h.md#af264946ff140207b02cfca1957da610d)static inline bool [is\_in\_secure\_state](4_2lib__helpers_8h.md#af264946ff140207b02cfca1957da610d)(void)

195{

196 /\* We cannot read SCR\_EL3 from EL2 or EL1 \*/

197 return ![IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ARMV8\_A\_NS);

198}

199

200#endif /\* !\_ASMLANGUAGE \*/

201

202#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM64\_LIB\_HELPERS\_H\_ \*/

[disable\_serror\_exceptions](4_2lib__helpers_8h.md#a316d3a4385241a3ff7032a8d34067a38)

static ALWAYS\_INLINE void disable\_serror\_exceptions(void)

**Definition** lib\_helpers.h:125

[read\_id\_aa64pfr0\_el1](4_2lib__helpers_8h.md#a38462e114f3f2c73503e48cf02df81c6)

static ALWAYS\_INLINE uint64\_t read\_id\_aa64pfr0\_el1(void)

**Definition** lib\_helpers.h:70

[disable\_debug\_exceptions](4_2lib__helpers_8h.md#a6124913695b3152818ca0c8338145522)

static ALWAYS\_INLINE void disable\_debug\_exceptions(void)

**Definition** lib\_helpers.h:113

[is\_el\_implemented](4_2lib__helpers_8h.md#a666bed8ddc768e8c5b75a1cb2d270df1)

static bool is\_el\_implemented(unsigned int el)

**Definition** lib\_helpers.h:159

[is\_el\_highest\_implemented](4_2lib__helpers_8h.md#a819e9a0d12d5273f526f0485600e7c28)

static bool is\_el\_highest\_implemented(void)

**Definition** lib\_helpers.h:172

[disable\_irq](4_2lib__helpers_8h.md#a86526fa2425a30ae46957d0480a09f25)

static ALWAYS\_INLINE void disable\_irq(void)

**Definition** lib\_helpers.h:137

[enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf)

static ALWAYS\_INLINE void enable\_irq(void)

**Definition** lib\_helpers.h:131

[disable\_fiq](4_2lib__helpers_8h.md#a971a94499a6e9949d79305c234329a10)

static ALWAYS\_INLINE void disable\_fiq(void)

**Definition** lib\_helpers.h:149

[enable\_debug\_exceptions](4_2lib__helpers_8h.md#aa10827ab07d53a97a2a0eef88a34cdc1)

static ALWAYS\_INLINE void enable\_debug\_exceptions(void)

**Definition** lib\_helpers.h:107

[MAKE\_REG\_HELPER\_EL123](4_2lib__helpers_8h.md#ab0d7628d77ded016e77f75d46717ab5e)

#define MAKE\_REG\_HELPER\_EL123(reg)

**Definition** lib\_helpers.h:51

[enable\_serror\_exceptions](4_2lib__helpers_8h.md#ab6fafccc9d37b2b9af7ec37a4bbfea92)

static ALWAYS\_INLINE void enable\_serror\_exceptions(void)

**Definition** lib\_helpers.h:119

[read\_currentel](4_2lib__helpers_8h.md#ab8bf450426e6ffd01784e74a89b368e5)

static ALWAYS\_INLINE uint64\_t read\_currentel(void)

**Definition** lib\_helpers.h:66

[enable\_fiq](4_2lib__helpers_8h.md#acca0372b859951afad2cc70c1ef9742f)

static ALWAYS\_INLINE void enable\_fiq(void)

**Definition** lib\_helpers.h:143

[is\_in\_secure\_state](4_2lib__helpers_8h.md#af264946ff140207b02cfca1957da610d)

static bool is\_in\_secure\_state(void)

**Definition** lib\_helpers.h:194

[is\_el2\_sec\_supported](4_2lib__helpers_8h.md#aff5c60debe8b01feaf857df6940d9e28)

static bool is\_el2\_sec\_supported(void)

**Definition** lib\_helpers.h:188

[cpu.h](arm64_2cpu_8h.md)

[GET\_EL](arm64_2cpu_8h.md#a16a04b233cad3fb65cb16dbeff32f8f2)

#define GET\_EL(\_mode)

**Definition** cpu.h:95

[DAIFCLR\_ABT\_BIT](arm64_2cpu_8h.md#a21a0f602ba0c8b87cc082e3e13aa5d98)

#define DAIFCLR\_ABT\_BIT

**Definition** cpu.h:20

[DAIFSET\_IRQ\_BIT](arm64_2cpu_8h.md#a22d4cee27b78fddece088591958ca037)

#define DAIFSET\_IRQ\_BIT

**Definition** cpu.h:14

[ID\_AA64PFR0\_SEL2\_MASK](arm64_2cpu_8h.md#a233d4971a3bcb773cfe17e4dbe0ee750)

#define ID\_AA64PFR0\_SEL2\_MASK

**Definition** cpu.h:117

[DAIFSET\_ABT\_BIT](arm64_2cpu_8h.md#a4a9605b3286e62a9d878c7cfdccbf6f6)

#define DAIFSET\_ABT\_BIT

**Definition** cpu.h:15

[DAIFSET\_FIQ\_BIT](arm64_2cpu_8h.md#a53fb1a3ffce153d445525392fb411687)

#define DAIFSET\_FIQ\_BIT

**Definition** cpu.h:13

[DAIFCLR\_IRQ\_BIT](arm64_2cpu_8h.md#a6f6ae405bbde72ffef083bca9448269b)

#define DAIFCLR\_IRQ\_BIT

**Definition** cpu.h:19

[ID\_AA64PFR0\_SEL2\_SHIFT](arm64_2cpu_8h.md#a7ebf5636fdc14822cb8bbe10c7f2e1b4)

#define ID\_AA64PFR0\_SEL2\_SHIFT

**Definition** cpu.h:116

[ID\_AA64PFR0\_EL1\_SHIFT](arm64_2cpu_8h.md#a9add6e194aac9e74e71c2dc2dd025eb7)

#define ID\_AA64PFR0\_EL1\_SHIFT

**Definition** cpu.h:112

[DAIFCLR\_FIQ\_BIT](arm64_2cpu_8h.md#abf5cf8b639767836af6967f6d07e07b3)

#define DAIFCLR\_FIQ\_BIT

**Definition** cpu.h:18

[ID\_AA64PFR0\_ELX\_MASK](arm64_2cpu_8h.md#ad296dae475a3598559cb5f53d74a62b0)

#define ID\_AA64PFR0\_ELX\_MASK

**Definition** cpu.h:115

[DAIFSET\_DBG\_BIT](arm64_2cpu_8h.md#ae8f3edaddcaaf22a1155da424838b326)

#define DAIFSET\_DBG\_BIT

**Definition** cpu.h:16

[DAIFCLR\_DBG\_BIT](arm64_2cpu_8h.md#afb4bae58d424e6460802949ef0355d21)

#define DAIFCLR\_DBG\_BIT

**Definition** cpu.h:21

[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)

#define MAKE\_REG\_HELPER(reg, op1, CRn, CRm, op2)

**Definition** lib\_helpers.h:45

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [lib\_helpers.h](4_2lib__helpers_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
