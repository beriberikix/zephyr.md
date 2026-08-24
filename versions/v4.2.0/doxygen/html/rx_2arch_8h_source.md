---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rx_2arch_8h_source.html
original_path: doxygen/html/rx_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](rx_2arch_8h.md)

1/\*

2 \* Copyright (c) 2021 KT-Elektronik, Klaucke und Partner GmbH

3 \* Copyright (c) 2024 Renesas Electronics Corporation

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_ARCH\_RX\_ARCH\_H\_

17#define ZEPHYR\_INCLUDE\_ARCH\_RX\_ARCH\_H\_

18

19/\* Add include for DTS generated information \*/

20#include <[zephyr/arch/rx/exception.h](rx_2exception_8h.md)>

21#include <[zephyr/devicetree.h](devicetree_8h.md)>

22

23#include <[zephyr/arch/rx/thread.h](arch_2rx_2thread_8h.md)>

24#include <[zephyr/arch/rx/misc.h](rx_2misc_8h.md)>

25#include <[zephyr/arch/rx/arch\_inlines.h](rx_2arch__inlines_8h.md)>

26#include <[zephyr/arch/rx/error.h](include_2zephyr_2arch_2rx_2error_8h.md)>

27#include <[zephyr/arch/common/sys\_bitops.h](sys__bitops_8h.md)>

28#include <[zephyr/arch/common/sys\_io.h](arch_2common_2sys__io_8h.md)>

29#include <[zephyr/arch/common/ffs.h](ffs_8h.md)>

30#include <[zephyr/sw\_isr\_table.h](sw__isr__table_8h.md)>

31#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

32#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

33#include <[zephyr/sys/util.h](sys_2util_8h.md)>

34#include <[zephyr/irq.h](irq_8h.md)>

35

[ 36](rx_2arch_8h.md#af0f8ad93611d93cd0626914837e761d3)#define ARCH\_STACK\_PTR\_ALIGN 4

37

38#ifndef \_ASMLANGUAGE

39

40#ifdef \_\_cplusplus

41extern "C" {

42#endif

43

[ 44](rx_2arch_8h.md#a1e07bd4d6286e062b88f8e5c839b1daa)#define REG(addr) \*((uint8\_t \*)(addr))

45

46/\* isr for undefined interrupts (results in a fatal error) \*/

47void z\_irq\_spurious(const void \*unused);

48/\* internal routine documented in C file, needed by IRQ\_CONNECT() macro \*/

49extern void z\_irq\_priority\_set([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

50

51/\* Z\_ISR\_DECLARE will populate the .intList section with the interrupt's

52 \* parameters, which will then be used by gen\_irq\_tables.py to create

53 \* the vector table and the software ISR table. This is all done at

54 \* build-time.

55 \*

56 \* We additionally set the priority in the interrupt controller at

57 \* runtime.

58 \*/

[ 59](rx_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

60 { \

61 Z\_ISR\_DECLARE(irq\_p, 0, isr\_p, isr\_param\_p); \

62 z\_irq\_priority\_set(irq\_p, priority\_p, flags\_p); \

63 }

64

65#if CONFIG\_TRACING\_ISR

66#define ARCH\_ISR\_DIRECT\_HEADER() \

67 { \

68 \_kernel.cpus[0].nested++; \

69 sys\_trace\_isr\_enter(); \

70 }

71#else

[ 72](rx_2arch_8h.md#a6c6d57983c066fe8ab21a78f86f7adb3)#define ARCH\_ISR\_DIRECT\_HEADER() \

73 { \

74 \_kernel.cpus[0].nested++; \

75 }

76#endif

77

78#if CONFIG\_TRACING\_ISR

79#define ARCH\_ISR\_DIRECT\_FOOTER(check\_reschedule) \

80 { \

81 if (IS\_ENABLED(CONFIG\_STACK\_SENTINEL)) { \

82 z\_check\_stack\_sentinel(); \

83 } \

84 sys\_trace\_isr\_exit(); \

85 irq\_lock(); \

86 if (check\_reschedule && \_kernel.cpus[0].nested == 1) { \

87 if (\_kernel.cpus->current->base.prio >= 0 || \

88 CONFIG\_NUM\_METAIRQ\_PRIORITIES > 0) { \

89 if (\_kernel.ready\_q.cache != \_kernel.cpus->current) { \

90 z\_rx\_irq\_exit(); \

91 } \

92 } \

93 } \

94 \_kernel.cpus[0].nested--; \

95 }

96#else

[ 97](rx_2arch_8h.md#ae95db3ae6bb31cc46eb6f500341ad974)#define ARCH\_ISR\_DIRECT\_FOOTER(check\_reschedule) \

98 { \

99 if (IS\_ENABLED(CONFIG\_STACK\_SENTINEL)) { \

100 z\_check\_stack\_sentinel(); \

101 } \

102 irq\_lock(); \

103 if (check\_reschedule && \_kernel.cpus[0].nested == 1) { \

104 if (\_kernel.cpus->current->base.prio >= 0 || \

105 CONFIG\_NUM\_METAIRQ\_PRIORITIES > 0) { \

106 if (\_kernel.ready\_q.cache != \_kernel.cpus->current) { \

107 z\_rx\_irq\_exit(); \

108 } \

109 } \

110 } \

111 \_kernel.cpus[0].nested--; \

112 }

113#endif

114

[ 115](rx_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

116{

117 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) key;

118 /\* deactivate interrupts by clearing the PSW-i flag \*/

119 \_\_asm\_\_ volatile("MVFC psw, %0\n"

120 "CLRPSW i"

121 : "=r"(key)

122 :

123 : "cc");

124 /\* return the value of the i-flag before clearing

125 \* if irqs were locked already, it was 0 and calling

126 \* arch\_irq\_unlock(key) will not actually unlock irqs, as this was a

127 \* nested irq lock

128 \*/

129 return key & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16);

130}

131

[ 132](rx_2arch_8h.md#aa2b2745d8e99b8730b44805f4d3bbf05)static inline void [arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

133{

134 if (key != 0) {

135 /\* re-activate interrupts by setting the PSW i-flag\*/

136 \_\_asm\_\_ volatile("SETPSW i" ::: "cc");

137 }

138}

139

[ 140](rx_2arch_8h.md#a1b827afafc622d412962f568b78726dc)static inline bool [arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

141{

142 return key != 0;

143}

144

[ 145](rx_2arch_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) \_cpu\_t \*[arch\_curr\_cpu](rx_2arch_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)(void)

146{

147 return &\_kernel.cpus[0];

148}

149

150#ifdef \_\_cplusplus

151}

152#endif

153

154#endif /\* !\_ASMLANGUAGE \*/

155

156#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RX\_ARCH\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[sys\_io.h](arch_2common_2sys__io_8h.md)

[thread.h](arch_2rx_2thread_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[ffs.h](ffs_8h.md)

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[error.h](include_2zephyr_2arch_2rx_2error_8h.md)

Renesas RX arch public error handling.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[kernel\_structs.h](kernel__structs_8h.md)

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:72

[arch\_irq\_unlock](mips_2arch_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** arch.h:83

[arch\_irq\_unlocked](mips_2arch_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** arch.h:96

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[arch\_curr\_cpu](rx_2arch_8h.md#a3e8a7515c0c3b8de5a037ce5997c73b0)

static ALWAYS\_INLINE \_cpu\_t \* arch\_curr\_cpu(void)

**Definition** arch.h:145

[arch\_inlines.h](rx_2arch__inlines_8h.md)

[exception.h](rx_2exception_8h.md)

[misc.h](rx_2misc_8h.md)

Renesas RX public kernel miscellaneous.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sw\_isr\_table.h](sw__isr__table_8h.md)

Software-managed ISR table.

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_bitops.h](sys__bitops_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [rx](dir_eb52b7f9d95392aedf108916f743bdaf.md)
- [arch.h](rx_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
