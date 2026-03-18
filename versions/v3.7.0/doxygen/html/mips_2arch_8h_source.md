---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mips_2arch_8h_source.html
original_path: doxygen/html/mips_2arch_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](mips_2arch_8h.md)

1/\*

2 \* Copyright (c) 2020 Antony Pavlov <antonynpavlov@gmail.com>

3 \*

4 \* based on include/arch/sparc/arch.h

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_MIPS\_ARCH\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_MIPS\_ARCH\_H\_

11

12#include <[zephyr/arch/mips/thread.h](arch_2mips_2thread_8h.md)>

13#include <[zephyr/arch/mips/exception.h](mips_2exception_8h.md)>

14#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

15#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

16#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

17

18#include <[zephyr/irq.h](irq_8h.md)>

19#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

20#include <[zephyr/devicetree.h](devicetree_8h.md)>

21#include <mips/mipsregs.h>

22

[ 23](mips_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 16

24

[ 25](mips_2arch_8h.md#a19279c7228621d3232e740aa69de27c3)#define OP\_LOADREG lw

[ 26](mips_2arch_8h.md#ab32daf0cef581b53f3553876d4db2714)#define OP\_STOREREG sw

27

[ 28](mips_2arch_8h.md#a26b87470892333da53ff3ecfb4d9226d)#define CP0\_STATUS\_DEF\_RESTORE (ST0\_EXL | ST0\_IE)

29

30#ifndef \_ASMLANGUAGE

31#include <[zephyr/sys/util.h](util_8h.md)>

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

[ 37](mips_2arch_8h.md#a49668abaf6448b75881e21c6a7d4aac6)#define STACK\_ROUND\_UP(x) ROUND\_UP(x, ARCH\_STACK\_PTR\_ALIGN)

38

[ 39](mips_2arch_8h.md#aa278d630653b33cb339621d725ed295a)void [arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)(unsigned int irq);

[ 40](mips_2arch_8h.md#a216d692e87bfba955a60f8e570e127df)void [arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)(unsigned int irq);

[ 41](mips_2arch_8h.md#a3bd8e963a124421bb372dab4bdc6cd83)int [arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)(unsigned int irq);

42void z\_irq\_spurious(const void \*unused);

43

57

[ 58](mips_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

59 { \

60 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

61 }

62

[ 63](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

64{

65 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status = read\_c0\_status();

66

67 if (status & ST0\_IE) {

68 write\_c0\_status(status & ~ST0\_IE);

69 return 1;

70 }

71 return 0;

72}

73

[ 74](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

75{

76 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) status = read\_c0\_status();

77

78 if (key) {

79 status |= ST0\_IE;

80 } else {

81 status &= ~ST0\_IE;

82 }

83

84 write\_c0\_status(status);

85}

86

[ 87](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

88{

89 return key != 0;

90}

91

[ 92](mips_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)(void)

93{

94 \_\_asm\_\_ volatile ("nop");

95}

96

[ 97](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)(void);

98

[ 99](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_k\_cycle\_get\_32](mips_2arch_8h.md#a9ee9f897ec750957de45bf8d43349d5e)(void)

100{

101 return [sys\_clock\_cycle\_get\_32](mips_2arch_8h.md#a42dcd1878309a82246dbfa26510f868a)();

102}

103

[ 104](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)extern [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)(void);

105

[ 106](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [arch\_k\_cycle\_get\_64](mips_2arch_8h.md#acc1ed8d949f694a1d39e389334caf971)(void)

107{

108 return [sys\_clock\_cycle\_get\_64](mips_2arch_8h.md#a25328a181bd0229ef5110c15e8452fc1)();

109}

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* \_ASMLANGUAGE \*/

116

117#endif /\* ZEPHYR\_INCLUDE\_ARCH\_MIPS\_ARCH\_H\_ \*/

[arch\_nop](arc_2arch_8h.md#a0af98dc5138e02248173c30b8f07210f)

static ALWAYS\_INLINE void arch\_nop(void)

**Definition** arch.h:348

[sys\_io.h](arch_2common_2sys__io_8h.md)

[thread.h](arch_2mips_2thread_8h.md)

Per-arch thread definition.

[arch\_irq\_disable](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)

#define arch\_irq\_disable(irq)

**Definition** irq.h:107

[arch\_irq\_enable](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)

#define arch\_irq\_enable(irq)

**Definition** irq.h:106

[arch\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)

#define arch\_irq\_is\_enabled(irq)

**Definition** irq.h:109

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

[exception.h](mips_2exception_8h.md)

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
- [mips](dir_fc8c8ea71cc5b300c3fa15bb05243853.md)
- [arch.h](mips_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
