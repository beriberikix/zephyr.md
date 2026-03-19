---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nios2_2arch_8h_source.html
original_path: doxygen/html/nios2_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](nios2_2arch_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_ARCH\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_ARCH\_H\_

16

17#include <system.h>

18

19#include <[zephyr/arch/nios2/thread.h](arch_2nios2_2thread_8h.md)>

20#include <[zephyr/arch/nios2/exception.h](nios2_2exception_8h.md)>

21#include <[zephyr/arch/nios2/asm\_inline.h](nios2_2asm__inline_8h.md)>

22#include <[zephyr/arch/common/addr\_types.h](addr__types_8h.md)>

23#include <[zephyr/devicetree.h](devicetree_8h.md)>

24#include <[zephyr/arch/nios2/nios2.h](nios2_8h.md)>

25#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

26#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

27#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

28

[ 29](nios2_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 4

30

31#ifndef \_ASMLANGUAGE

32#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

33#include <[zephyr/irq.h](irq_8h.md)>

34#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

40/\* There is no notion of priority with the Nios II internal interrupt

41 \* controller and no flags are currently supported.

42 \*/

[ 43](nios2_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

44{ \

45 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

46}

47

[ 48](nios2_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

49{

50 unsigned int key, tmp;

51

52 \_\_asm\_\_ volatile (

53 "rdctl %[key], status\n\t"

54 "movi %[tmp], -2\n\t"

55 "and %[tmp], %[key], %[tmp]\n\t"

56 "wrctl status, %[tmp]\n\t"

57 : [key] "=r" (key), [tmp] "=r" (tmp)

58 : : "memory");

59

60 return key;

61}

62

[ 63](nios2_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

64{

65 /\* If the CPU is built without certain features, then

66 \* the only writable bit in the status register is PIE

67 \* in which case we can just write the value stored in key,

68 \* all the other writable bits will be the same.

69 \*

70 \* If not, other stuff could have changed and we need to

71 \* specifically flip just that bit.

72 \*/

73

74#if (ALT\_CPU\_NUM\_OF\_SHADOW\_REG\_SETS > 0) || \

75 (defined ALT\_CPU\_EIC\_PRESENT) || \

76 (defined ALT\_CPU\_MMU\_PRESENT) || \

77 (defined ALT\_CPU\_MPU\_PRESENT)

78 \_\_asm\_\_ volatile (

79 "andi %[key], %[key], 1\n\t"

80 "beq %[key], zero, 1f\n\t"

81 "rdctl %[key], status\n\t"

82 "ori %[key], %[key], 1\n\t"

83 "wrctl status, %[key]\n\t"

84 "1:\n\t"

85 : [key] "+r" (key)

86 : : "memory");

87#else

88 \_\_asm\_\_ volatile (

89 "wrctl status, %[key]"

90 : : [key] "r" (key)

91 : "memory");

92#endif

93}

94

[ 95](nios2_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

96{

97 return key & 1;

98}

99

[ 100](nios2_2arch_8h.md#aa278d630653b33cb339621d725ed295a)void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 101](nios2_2arch_8h.md#a216d692e87bfba955a60f8e570e127df)void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

102

103FUNC\_NORETURN void z\_SysFatalErrorHandler(unsigned int reason,

104 const struct [arch\_esf](structarch__esf.md) \*esf);

105

106FUNC\_NORETURN void z\_NanoFatalErrorHandler(unsigned int reason,

107 const struct [arch\_esf](structarch__esf.md) \*esf);

108

[ 109](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eb)enum [nios2\_exception\_cause](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eb) {

[ 110](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba25e598ae2f7e517970f8f797e4f1b30a) [NIOS2\_EXCEPTION\_UNKNOWN](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba25e598ae2f7e517970f8f797e4f1b30a) = -1,

[ 111](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf6c6a73adf1aa0df7a4d5bf9892423ee) [NIOS2\_EXCEPTION\_RESET](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf6c6a73adf1aa0df7a4d5bf9892423ee) = 0,

[ 112](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba7fc081560604efa925848ed4204b589c) [NIOS2\_EXCEPTION\_CPU\_ONLY\_RESET\_REQUEST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba7fc081560604efa925848ed4204b589c) = 1,

[ 113](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf4d926e02d36e21e78902fc404bbf4f5) [NIOS2\_EXCEPTION\_INTERRUPT](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf4d926e02d36e21e78902fc404bbf4f5) = 2,

[ 114](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaebf7c6f50a51346242135178592fec50) [NIOS2\_EXCEPTION\_TRAP\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaebf7c6f50a51346242135178592fec50) = 3,

[ 115](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebabfc872ef21b65fe5a2dd77833f5daf59) [NIOS2\_EXCEPTION\_UNIMPLEMENTED\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebabfc872ef21b65fe5a2dd77833f5daf59) = 4,

[ 116](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba894eb715964b668ec2d4ed0e32dadb70) [NIOS2\_EXCEPTION\_ILLEGAL\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba894eb715964b668ec2d4ed0e32dadb70) = 5,

[ 117](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae388771d5651cbda528c168fbc2b045f) [NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae388771d5651cbda528c168fbc2b045f) = 6,

[ 118](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad4daa79baaf28b7e57a41ab10c1a056b) [NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad4daa79baaf28b7e57a41ab10c1a056b) = 7,

[ 119](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad831a5dd045c258c7586f33b4af5ca85) [NIOS2\_EXCEPTION\_DIVISION\_ERROR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad831a5dd045c258c7586f33b4af5ca85) = 8,

[ 120](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba9a08eea9bdf84fb5bce9b39126c7f407) [NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST\_ADDR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba9a08eea9bdf84fb5bce9b39126c7f407) = 9,

[ 121](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae6258162d85c0c3b0a780b1e905a2d56) [NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae6258162d85c0c3b0a780b1e905a2d56) = 10,

[ 122](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba732e002953cc38c05f87a6aa61a662bf) [NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba732e002953cc38c05f87a6aa61a662bf) = 11,

[ 123](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba810fce3ab2f5ceb92b6e73e707f1d22e) [NIOS2\_EXCEPTION\_TLB\_MISS](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba810fce3ab2f5ceb92b6e73e707f1d22e) = 12,

[ 124](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae8101069360e03367af48e97e2d689a7) [NIOS2\_EXCEPTION\_TLB\_EXECUTE\_PERM\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae8101069360e03367af48e97e2d689a7) = 13,

[ 125](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad6cf84739e1469a0e8a4ba614d19a18a) [NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad6cf84739e1469a0e8a4ba614d19a18a) = 14,

[ 126](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba32fd876bb736d600090d68f9d5c30055) [NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba32fd876bb736d600090d68f9d5c30055) = 15,

[ 127](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba6403b7c0a411db595de90af57b3ac25a) [NIOS2\_EXCEPTION\_MPU\_INST\_REGION\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba6403b7c0a411db595de90af57b3ac25a) = 16,

[ 128](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebacb7c66d2e8e211b82d74da89d6a1855a) [NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebacb7c66d2e8e211b82d74da89d6a1855a) = 17,

[ 129](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba4cad710f904b74d686b286828a12c006) [NIOS2\_EXCEPTION\_ECC\_TLB\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba4cad710f904b74d686b286828a12c006) = 18,

[ 130](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad2c112e52af6240e77e3cb532d7890a1) [NIOS2\_EXCEPTION\_ECC\_FETCH\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad2c112e52af6240e77e3cb532d7890a1) = 19,

[ 131](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaec6269ebaf6592bc20f2acfee2420a33) [NIOS2\_EXCEPTION\_ECC\_REGISTER\_FILE\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaec6269ebaf6592bc20f2acfee2420a33) = 20,

[ 132](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf5b4a2d54e230de79b36a4ca5d262ca0) [NIOS2\_EXCEPTION\_ECC\_DATA\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf5b4a2d54e230de79b36a4ca5d262ca0) = 21,

[ 133](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba157e694bc9bbae8aa20ef35e94f621b8) [NIOS2\_EXCEPTION\_ECC\_DATA\_CACHE\_WRITEBACK\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba157e694bc9bbae8aa20ef35e94f621b8) = 22

134};

135

136/\* Bitfield indicating which exception cause codes report a valid

137 \* badaddr register. NIOS2\_EXCEPTION\_TLB\_MISS and NIOS2\_EXCEPTION\_ECC\_TLB\_ERR

138 \* are deliberately not included here, you need to check if TLBMISC.D=1

139 \*/

[ 140](nios2_2arch_8h.md#a70ed7e577dcd2644cbd4c4e964736c05)#define NIOS2\_BADADDR\_CAUSE\_MASK \

141 (BIT(NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR) | \

142 BIT(NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR) | \

143 BIT(NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC) | \

144 BIT(NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION) | \

145 BIT(NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION) | \

146 BIT(NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION) | \

147 BIT(NIOS2\_EXCEPTION\_ECC\_DATA\_ERR))

148

149

[ 150](nios2_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

151

[ 152](nios2_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

153{

154 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

155}

156

[ 157](nios2_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

158

[ 159](nios2_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

160{

161 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

162}

163

[ 164](nios2_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

165{

166 \_\_asm\_\_ volatile("nop");

167}

168

169#ifdef \_\_cplusplus

170}

171#endif

172

173#endif /\* \_ASMLANGUAGE \*/

174

175#endif /\* ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_ARCH\_H\_ \*/

[addr\_types.h](addr__types_8h.md)

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[thread.h](arch_2nios2_2thread_8h.md)

Per-arch thread definition.

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[types.h](include_2zephyr_2types_8h.md)

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:63

[arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** arch.h:74

[sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

[sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** arch.h:99

[arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** arch.h:106

[arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** arch.h:87

[nios2\_exception\_cause](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eb)

nios2\_exception\_cause

**Definition** arch.h:109

[NIOS2\_EXCEPTION\_ECC\_DATA\_CACHE\_WRITEBACK\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba157e694bc9bbae8aa20ef35e94f621b8)

@ NIOS2\_EXCEPTION\_ECC\_DATA\_CACHE\_WRITEBACK\_ERR

**Definition** arch.h:133

[NIOS2\_EXCEPTION\_UNKNOWN](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba25e598ae2f7e517970f8f797e4f1b30a)

@ NIOS2\_EXCEPTION\_UNKNOWN

**Definition** arch.h:110

[NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba32fd876bb736d600090d68f9d5c30055)

@ NIOS2\_EXCEPTION\_TLB\_WRITE\_PERM\_VIOLATION

**Definition** arch.h:126

[NIOS2\_EXCEPTION\_ECC\_TLB\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba4cad710f904b74d686b286828a12c006)

@ NIOS2\_EXCEPTION\_ECC\_TLB\_ERR

**Definition** arch.h:129

[NIOS2\_EXCEPTION\_MPU\_INST\_REGION\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba6403b7c0a411db595de90af57b3ac25a)

@ NIOS2\_EXCEPTION\_MPU\_INST\_REGION\_VIOLATION

**Definition** arch.h:127

[NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba732e002953cc38c05f87a6aa61a662bf)

@ NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_DATA\_ADDR

**Definition** arch.h:122

[NIOS2\_EXCEPTION\_CPU\_ONLY\_RESET\_REQUEST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba7fc081560604efa925848ed4204b589c)

@ NIOS2\_EXCEPTION\_CPU\_ONLY\_RESET\_REQUEST

**Definition** arch.h:112

[NIOS2\_EXCEPTION\_TLB\_MISS](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba810fce3ab2f5ceb92b6e73e707f1d22e)

@ NIOS2\_EXCEPTION\_TLB\_MISS

**Definition** arch.h:123

[NIOS2\_EXCEPTION\_ILLEGAL\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba894eb715964b668ec2d4ed0e32dadb70)

@ NIOS2\_EXCEPTION\_ILLEGAL\_INST

**Definition** arch.h:116

[NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST\_ADDR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5eba9a08eea9bdf84fb5bce9b39126c7f407)

@ NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST\_ADDR

**Definition** arch.h:120

[NIOS2\_EXCEPTION\_UNIMPLEMENTED\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebabfc872ef21b65fe5a2dd77833f5daf59)

@ NIOS2\_EXCEPTION\_UNIMPLEMENTED\_INST

**Definition** arch.h:115

[NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebacb7c66d2e8e211b82d74da89d6a1855a)

@ NIOS2\_EXCEPTION\_MPU\_DATA\_REGION\_VIOLATION

**Definition** arch.h:128

[NIOS2\_EXCEPTION\_ECC\_FETCH\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad2c112e52af6240e77e3cb532d7890a1)

@ NIOS2\_EXCEPTION\_ECC\_FETCH\_ERR

**Definition** arch.h:130

[NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad4daa79baaf28b7e57a41ab10c1a056b)

@ NIOS2\_EXCEPTION\_MISALIGNED\_TARGET\_PC

**Definition** arch.h:118

[NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad6cf84739e1469a0e8a4ba614d19a18a)

@ NIOS2\_EXCEPTION\_TLB\_READ\_PERM\_VIOLATION

**Definition** arch.h:125

[NIOS2\_EXCEPTION\_DIVISION\_ERROR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebad831a5dd045c258c7586f33b4af5ca85)

@ NIOS2\_EXCEPTION\_DIVISION\_ERROR

**Definition** arch.h:119

[NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae388771d5651cbda528c168fbc2b045f)

@ NIOS2\_EXCEPTION\_MISALIGNED\_DATA\_ADDR

**Definition** arch.h:117

[NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae6258162d85c0c3b0a780b1e905a2d56)

@ NIOS2\_EXCEPTION\_SUPERVISOR\_ONLY\_INST

**Definition** arch.h:121

[NIOS2\_EXCEPTION\_TLB\_EXECUTE\_PERM\_VIOLATION](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebae8101069360e03367af48e97e2d689a7)

@ NIOS2\_EXCEPTION\_TLB\_EXECUTE\_PERM\_VIOLATION

**Definition** arch.h:124

[NIOS2\_EXCEPTION\_TRAP\_INST](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaebf7c6f50a51346242135178592fec50)

@ NIOS2\_EXCEPTION\_TRAP\_INST

**Definition** arch.h:114

[NIOS2\_EXCEPTION\_ECC\_REGISTER\_FILE\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaec6269ebaf6592bc20f2acfee2420a33)

@ NIOS2\_EXCEPTION\_ECC\_REGISTER\_FILE\_ERR

**Definition** arch.h:131

[NIOS2\_EXCEPTION\_INTERRUPT](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf4d926e02d36e21e78902fc404bbf4f5)

@ NIOS2\_EXCEPTION\_INTERRUPT

**Definition** arch.h:113

[NIOS2\_EXCEPTION\_ECC\_DATA\_ERR](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf5b4a2d54e230de79b36a4ca5d262ca0)

@ NIOS2\_EXCEPTION\_ECC\_DATA\_ERR

**Definition** arch.h:132

[NIOS2\_EXCEPTION\_RESET](nios2_2arch_8h.md#a74caf934553c660658877ace2e17d5ebaf6c6a73adf1aa0df7a4d5bf9892423ee)

@ NIOS2\_EXCEPTION\_RESET

**Definition** arch.h:111

[asm\_inline.h](nios2_2asm__inline_8h.md)

[exception.h](nios2_2exception_8h.md)

[nios2.h](nios2_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:60

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[sys\_io.h](sys_2sys__io_8h.md)

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [arch.h](nios2_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
