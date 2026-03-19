---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sparc_2arch_8h_source.html
original_path: doxygen/html/sparc_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

17#include <[zephyr/arch/sparc/exception.h](sparc_2exception_8h.md)>

18#include <[zephyr/arch/sparc/thread.h](arch_2sparc_2thread_8h.md)>

19#include <[zephyr/arch/sparc/sparc.h](sparc_8h.md)>

20#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

21#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

22#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

23

24#include <[zephyr/irq.h](irq_8h.md)>

25#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

26#include <soc.h>

27#include <[zephyr/devicetree.h](devicetree_8h.md)>

28

29/\* stacks, for SPARC architecture stack shall be 8byte-aligned \*/

[ 30](sparc_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 8

31

32/\*

33 \* Software trap numbers.

34 \* Assembly usage: "ta SPARC\_SW\_TRAP\_<TYPE>"

35 \*/

[ 36](sparc_2arch_8h.md#af489f2ab54555e99f7e0351e95bdadda)#define SPARC\_SW\_TRAP\_FLUSH\_WINDOWS 0x03

[ 37](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)#define SPARC\_SW\_TRAP\_SET\_PIL 0x09

[ 38](sparc_2arch_8h.md#a2e78f31907142407cf66518f840ca5e9)#define SPARC\_SW\_TRAP\_EXCEPT 0x0F

39

40#ifndef \_ASMLANGUAGE

41#include <[zephyr/sys/util.h](sys_2util_8h.md)>

42

43#ifdef \_\_cplusplus

44extern "C" {

45#endif

46

[ 47](sparc_2arch_8h.md#a49668abaf6448b75881e21c6a7d4aac6)#define STACK\_ROUND\_UP(x) ROUND\_UP(x, ARCH\_STACK\_PTR\_ALIGN)

48

49/\*

50 \* SOC specific function to translate from processor interrupt request level

51 \* (1..15) to logical interrupt source number. For example by probing the

52 \* interrupt controller.

53 \*/

54int z\_sparc\_int\_get\_source(int irl);

55void z\_irq\_spurious(const void \*unused);

56

57

[ 58](sparc_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

59 { \

60 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

61 }

62

63

64static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int z\_sparc\_set\_pil\_inline(unsigned int newpil)

65{

66 register [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) oldpil \_\_asm\_\_ ("o0") = newpil;

67

68 \_\_asm\_\_ volatile (

69 "ta %1\nnop\n" :

70 "=r" (oldpil) :

71 "i" ([SPARC\_SW\_TRAP\_SET\_PIL](sparc_2arch_8h.md#a0db46ead17cf040d99fa5adc10aa1274)), "r" (oldpil) :

72 "memory"

73 );

74 return oldpil;

75}

76

[ 77](sparc_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

78{

79 return z\_sparc\_set\_pil\_inline(15);

80}

81

[ 82](sparc_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

83{

84 z\_sparc\_set\_pil\_inline(key);

85}

86

[ 87](sparc_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

88{

89 return key == 0;

90}

91

[ 92](sparc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

93{

94 \_\_asm\_\_ volatile ("nop");

95}

96

[ 97](sparc_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

98

[ 99](sparc_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

100{

101 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

102}

103

[ 104](sparc_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

105

[ 106](sparc_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

107{

108 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

109}

110

[ 111](sparc_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) \

112do { \

113 register uint32\_t \_g1 \_\_asm\_\_("g1") = reason\_p; \

114 \

115 \_\_asm\_\_ volatile ( \

116 "ta %[vector]\n\t" \

117 : \

118 : [vector] "i" (SPARC\_SW\_TRAP\_EXCEPT), "r" (\_g1) \

119 : "memory" \

120 ); \

121 CODE\_UNREACHABLE; \

122} while (false)

123

124#ifdef \_\_cplusplus

125}

126#endif

127

128#endif /\*\_ASMLANGUAGE \*/

129

130#endif /\* ZEPHYR\_INCLUDE\_ARCH\_SPARC\_ARCH\_H\_ \*/

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

**Definition** common.h:129

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

**Definition** arch.h:37

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
