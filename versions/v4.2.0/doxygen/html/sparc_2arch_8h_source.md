---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/sparc_2arch_8h_source.html
original_path: doxygen/html/sparc_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_

18

19#include <[zephyr/arch/sparc/exception.h](sparc_2exception_8h.md)>

20#include <[zephyr/arch/sparc/thread.h](arch_2sparc_2thread_8h.md)>

21#include <[zephyr/arch/sparc/sparc.h](sparc_8h.md)>

22#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

23#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

24#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

25

26#include <[zephyr/irq.h](irq_8h.md)>

27#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

28#include <soc.h>

29#include <[zephyr/devicetree.h](devicetree_8h.md)>

30

31/\* stacks, for SPARC architecture stack shall be 8byte-aligned \*/

[ 32](sparc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 8

33

34/\*

35 \* Software trap numbers.

36 \* Assembly usage: "ta SPARC\_SW\_TRAP\_<TYPE>"

37 \*/

[ 38](sparc_2arch_8h.md#af489f2ab54555e99f7e0351e95bdadda)#define SPARC\_SW\_TRAP\_FLUSH\_WINDOWS 0x03

[ 39](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)#define SPARC\_SW\_TRAP\_SET\_PIL 0x09

[ 40](sparc_2arch_8h.md#a2e78f31907142407cf66518f840ca5e9)#define SPARC\_SW\_TRAP\_EXCEPT 0x0F

41

42#ifndef \_ASMLANGUAGE

43#include <[zephyr/sys/util.h](sys_2util_8h.md)>

44

45#ifdef \_\_cplusplus

46extern "C" {

47#endif

48

[ 49](sparc_2arch_8h.md#a49668abaf6448b75881e21c6a7d4aac6)#define STACK\_ROUND\_UP(x) ROUND\_UP(x, ARCH\_STACK\_PTR\_ALIGN)

50

51/\*

52 \* SOC specific function to translate from processor interrupt request level

53 \* (1..15) to logical interrupt source number. For example by probing the

54 \* interrupt controller.

55 \*/

56int z\_sparc\_int\_get\_source(int irl);

57void z\_irq\_spurious(const void \*unused);

58

59

[ 60](sparc_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

61 { \

62 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

63 }

64

65

66static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int z\_sparc\_set\_pil\_inline(unsigned int newpil)

67{

68 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) oldpil \_\_asm\_\_ ("o0") = newpil;

69

70 \_\_asm\_\_ volatile (

71 "ta %1\nnop\n" :

72 "=r" (oldpil) :

73 "i" ([SPARC\_SW\_TRAP\_SET\_PIL](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)), "r" (oldpil) :

74 "memory"

75 );

76 return oldpil;

77}

78

[ 79](sparc_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

80{

81 return z\_sparc\_set\_pil\_inline(15);

82}

83

[ 84](sparc_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

85{

86 z\_sparc\_set\_pil\_inline(key);

87}

88

[ 89](sparc_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

90{

91 return key == 0;

92}

93

[ 94](sparc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

95{

96 \_\_asm\_\_ volatile ("nop");

97}

98

[ 99](sparc_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

100

[ 101](sparc_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

102{

103 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

104}

105

[ 106](sparc_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

107

[ 108](sparc_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

109{

110 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

111}

112

[ 113](sparc_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) \

114do { \

115 register uint32\_t \_g1 \_\_asm\_\_("g1") = reason\_p; \

116 \

117 \_\_asm\_\_ volatile ( \

118 "ta %[vector]\n\t" \

119 : \

120 : [vector] "i" (SPARC\_SW\_TRAP\_EXCEPT), "r" (\_g1) \

121 : "memory" \

122 ); \

123 CODE\_UNREACHABLE; \

124} while (false)

125

126#ifdef \_\_cplusplus

127}

128#endif

129

130#endif /\*\_ASMLANGUAGE \*/

131

132#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[sys\_io.h](arch_2common_2sys__io_8h.md)

[thread.h](arch_2sparc_2thread_8h.md)

Per-arch thread definition.

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:72

[arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** arch.h:83

[sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)

uint64\_t sys\_clock\_cycle\_get\_64(void)

[sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)

uint32\_t sys\_clock\_cycle\_get\_32(void)

[arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)

static uint32\_t arch\_k\_cycle\_get\_32(void)

**Definition** arch.h:108

[arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)

static uint64\_t arch\_k\_cycle\_get\_64(void)

**Definition** arch.h:115

[arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** arch.h:96

[SPARC\_SW\_TRAP\_SET\_PIL](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)

#define SPARC\_SW\_TRAP\_SET\_PIL

**Definition** arch.h:39

[exception.h](sparc_2exception_8h.md)

[sparc.h](sparc_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [sparc](dir_0b6b538994b3c7630127059eac21a61b.md)
- [arch.h](sparc_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
