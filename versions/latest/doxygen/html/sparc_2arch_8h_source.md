---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sparc_2arch_8h_source.html
original_path: doxygen/html/sparc_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](sparc_2arch_8h.md)

1/\*

2 \* Copyright (c) 2019-2020 Cobham Gaisler AB

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_

16

17#include <[zephyr/arch/sparc/thread.h](arch_2sparc_2thread_8h.md)>

18#include <[zephyr/arch/sparc/sparc.h](sparc_8h.md)>

19#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

20#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

21#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

22

23#include <[zephyr/irq.h](irq_8h.md)>

24#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

25#include <soc.h>

26#include <[zephyr/devicetree.h](devicetree_8h.md)>

27

28/\* stacks, for SPARC architecture stack shall be 8byte-aligned \*/

[ 29](sparc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 8

30

31/\*

32 \* Software trap numbers.

33 \* Assembly usage: "ta SPARC\_SW\_TRAP\_<TYPE>"

34 \*/

[ 35](sparc_2arch_8h.md#af489f2ab54555e99f7e0351e95bdadda)#define SPARC\_SW\_TRAP\_FLUSH\_WINDOWS 0x03

[ 36](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)#define SPARC\_SW\_TRAP\_SET\_PIL 0x09

[ 37](sparc_2arch_8h.md#a2e78f31907142407cf66518f840ca5e9)#define SPARC\_SW\_TRAP\_EXCEPT 0x0F

38

39#ifndef \_ASMLANGUAGE

40#include <[zephyr/sys/util.h](util_8h.md)>

41

42#ifdef \_\_cplusplus

43extern "C" {

44#endif

45

[ 46](sparc_2arch_8h.md#a49668abaf6448b75881e21c6a7d4aac6)#define STACK\_ROUND\_UP(x) ROUND\_UP(x, ARCH\_STACK\_PTR\_ALIGN)

47

48/\*

49 \* SOC specific function to translate from processor interrupt request level

50 \* (1..15) to logical interrupt source number. For example by probing the

51 \* interrupt controller.

52 \*/

53int z\_sparc\_int\_get\_source(int irl);

54void z\_irq\_spurious(const void \*unused);

55

56

[ 57](sparc_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

58 { \

59 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

60 }

61

62

63static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int z\_sparc\_set\_pil\_inline(unsigned int newpil)

64{

65 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) oldpil \_\_asm\_\_ ("o0") = newpil;

66

67 \_\_asm\_\_ volatile (

68 "ta %1\nnop\n" :

69 "=r" (oldpil) :

70 "i" ([SPARC\_SW\_TRAP\_SET\_PIL](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)), "r" (oldpil) :

71 "memory"

72 );

73 return oldpil;

74}

75

[ 76](sparc_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

77{

78 return z\_sparc\_set\_pil\_inline(15);

79}

80

[ 81](sparc_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

82{

83 z\_sparc\_set\_pil\_inline(key);

84}

85

[ 86](sparc_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

87{

88 return key == 0;

89}

90

[ 91](sparc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

92{

93 \_\_asm\_\_ volatile ("nop");

94}

95

[ 96](sparc_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

97

[ 98](sparc_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

99{

100 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

101}

102

[ 103](sparc_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

104

[ 105](sparc_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

106{

107 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

108}

109

110struct \_\_esf {

111 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) out[8];

112 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) global[8];

113 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psr;

114 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pc;

115 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) npc;

116 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wim;

117 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tbr;

118 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) y;

119};

120

121typedef struct \_\_esf z\_arch\_esf\_t;

122

[ 123](sparc_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) \

124do { \

125 register uint32\_t \_g1 \_\_asm\_\_("g1") = reason\_p; \

126 \

127 \_\_asm\_\_ volatile ( \

128 "ta %[vector]\n\t" \

129 : \

130 : [vector] "i" (SPARC\_SW\_TRAP\_EXCEPT), "r" (\_g1) \

131 : "memory" \

132 ); \

133 CODE\_UNREACHABLE; \

134} while (false)

135

136#ifdef \_\_cplusplus

137}

138#endif

139

140#endif /\*\_ASMLANGUAGE \*/

141

142#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[sys\_io.h](arch_2common_2sys__io_8h.md)

[thread.h](arch_2sparc_2thread_8h.md)

Per-arch thread definition.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

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

[SPARC\_SW\_TRAP\_SET\_PIL](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)

#define SPARC\_SW\_TRAP\_SET\_PIL

**Definition** arch.h:36

[sparc.h](sparc_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[sys\_bitops.h](sys__bitops_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [arch.h](sparc_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
