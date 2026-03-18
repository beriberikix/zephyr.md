---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2xtensa_2irq_8h_source.html
original_path: doxygen/html/arch_2xtensa_2irq_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

irq.h

[Go to the documentation of this file.](arch_2xtensa_2irq_8h.md)

1/\*

2 \* Copyright (c) 2016 Cadence Design Systems, Inc.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_IRQ\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_IRQ\_H\_

8

9#include <[stdint.h](stdint_8h.md)>

10

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12#include <xtensa/config/core-isa.h>

13

[ 14](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)#define CONFIG\_GEN\_IRQ\_START\_VECTOR 0

15

19

20/\*

21 \* Call this function to enable the specified interrupts.

22 \*

23 \* mask - Bit mask of interrupts to be enabled.

24 \*/

25static inline void z\_xt\_ints\_on(unsigned int mask)

26{

27 int val;

28

29 \_\_asm\_\_ volatile("rsr.intenable %0" : "=r"(val));

30 val |= mask;

31 \_\_asm\_\_ volatile("wsr.intenable %0; rsync" : : "r"(val));

32}

33

34

35/\*

36 \* Call this function to disable the specified interrupts.

37 \*

38 \* mask - Bit mask of interrupts to be disabled.

39 \*/

40static inline void z\_xt\_ints\_off(unsigned int mask)

41{

42 int val;

43

44 \_\_asm\_\_ volatile("rsr.intenable %0" : "=r"(val));

45 val &= ~mask;

46 \_\_asm\_\_ volatile("wsr.intenable %0; rsync" : : "r"(val));

47}

48

49

50/\*

51 \* Call this function to set the specified (s/w) interrupt.

52 \*/

53static inline void z\_xt\_set\_intset(unsigned int arg)

54{

55#if XCHAL\_HAVE\_INTERRUPTS

56 \_\_asm\_\_ volatile("wsr.intset %0; rsync" : : "r"(arg));

57#else

58 ARG\_UNUSED(arg);

59#endif

60}

61

65

66#ifdef CONFIG\_MULTI\_LEVEL\_INTERRUPTS

67

68/\* for \_soc\_irq\_\*() \*/

69#include <soc.h>

70

71#ifdef CONFIG\_2ND\_LEVEL\_INTERRUPTS

72#ifdef CONFIG\_3RD\_LEVEL\_INTERRUPTS

73#define CONFIG\_NUM\_IRQS (XCHAL\_NUM\_INTERRUPTS +\

74 (CONFIG\_NUM\_2ND\_LEVEL\_AGGREGATORS +\

75 CONFIG\_NUM\_3RD\_LEVEL\_AGGREGATORS) \*\

76 CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR)

77#else

78#define CONFIG\_NUM\_IRQS (XCHAL\_NUM\_INTERRUPTS +\

79 CONFIG\_NUM\_2ND\_LEVEL\_AGGREGATORS \*\

80 CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR)

81#endif /\* CONFIG\_3RD\_LEVEL\_INTERRUPTS \*/

82#else

83#define CONFIG\_NUM\_IRQS XCHAL\_NUM\_INTERRUPTS

84#endif /\* CONFIG\_2ND\_LEVEL\_INTERRUPTS \*/

85

86void z\_soc\_irq\_init(void);

87void z\_soc\_irq\_enable(unsigned int irq);

88void z\_soc\_irq\_disable(unsigned int irq);

89int z\_soc\_irq\_is\_enabled(unsigned int irq);

90

91#define arch\_irq\_enable(irq) z\_soc\_irq\_enable(irq)

92#define arch\_irq\_disable(irq) z\_soc\_irq\_disable(irq)

93

94#define arch\_irq\_is\_enabled(irq) z\_soc\_irq\_is\_enabled(irq)

95

96#ifdef CONFIG\_DYNAMIC\_INTERRUPTS

97extern int z\_soc\_irq\_connect\_dynamic(unsigned int irq, unsigned int priority,

98 void (\*routine)(const void \*parameter),

99 const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

100#endif

101

102#else

103

[ 104](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837)#define CONFIG\_NUM\_IRQS XCHAL\_NUM\_INTERRUPTS

105

[ 106](arch_2xtensa_2irq_8h.md#a5ea6488112b97755b13583cd2832c2fa)#define arch\_irq\_enable(irq) xtensa\_irq\_enable(irq)

[ 107](arch_2xtensa_2irq_8h.md#a19b436a206500c3748ad5c32050db241)#define arch\_irq\_disable(irq) xtensa\_irq\_disable(irq)

108

[ 109](arch_2xtensa_2irq_8h.md#ae95daf1bea993f1d03adaf31fc44c369)#define arch\_irq\_is\_enabled(irq) xtensa\_irq\_is\_enabled(irq)

110

111#endif

112

[ 118](arch_2xtensa_2irq_8h.md#a9d6c92219fd2390f777aff106d2eafa9)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [xtensa\_irq\_enable](arch_2xtensa_2irq_8h.md#a9d6c92219fd2390f777aff106d2eafa9)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq)

119{

120 z\_xt\_ints\_on(1 << irq);

121}

122

[ 128](arch_2xtensa_2irq_8h.md#a37d1c0641f471e9492c2493c77327c96)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [xtensa\_irq\_disable](arch_2xtensa_2irq_8h.md#a37d1c0641f471e9492c2493c77327c96)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq)

129{

130 z\_xt\_ints\_off(1 << irq);

131}

132

[ 134](arch_2xtensa_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

135{

136 unsigned int key;

137

138 \_\_asm\_\_ volatile("rsil %0, %1"

139 : "=r"(key) : "i"(XCHAL\_EXCM\_LEVEL) : "memory");

140 return key;

141}

142

[ 144](arch_2xtensa_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(unsigned int key)

145{

146 \_\_asm\_\_ volatile("wsr.ps %0; rsync"

147 :: "r"(key) : "memory");

148}

149

[ 151](arch_2xtensa_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) bool [arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)(unsigned int key)

152{

153 return (key & 0xf) == 0; /\* INTLEVEL field \*/

154}

155

[ 163](arch_2xtensa_2irq_8h.md#ae6e10f2a35e679c41c11700330ce8b7a)extern int [xtensa\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae6e10f2a35e679c41c11700330ce8b7a)(unsigned int irq);

164

165#include <[zephyr/irq.h](irq_8h.md)>

166

167#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_XTENSA\_IRQ\_H\_ \*/

[arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

Disable all interrupts on the local CPU.

**Definition** irq.h:168

[arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** irq.h:176

[arch\_irq\_unlocked](arch_2arc_2v2_2irq_8h.md#adb441b26ed6818fea4ebba6b8853354b)

static ALWAYS\_INLINE bool arch\_irq\_unlocked(unsigned int key)

**Definition** irq.h:181

[xtensa\_irq\_disable](arch_2xtensa_2irq_8h.md#a37d1c0641f471e9492c2493c77327c96)

static ALWAYS\_INLINE void xtensa\_irq\_disable(uint32\_t irq)

Disable interrupt on Xtensa core.

**Definition** irq.h:128

[xtensa\_irq\_enable](arch_2xtensa_2irq_8h.md#a9d6c92219fd2390f777aff106d2eafa9)

static ALWAYS\_INLINE void xtensa\_irq\_enable(uint32\_t irq)

Enable interrupt on Xtensa core.

**Definition** irq.h:118

[xtensa\_irq\_is\_enabled](arch_2xtensa_2irq_8h.md#ae6e10f2a35e679c41c11700330ce8b7a)

int xtensa\_irq\_is\_enabled(unsigned int irq)

Query if an interrupt is enabled on Xtensa core.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[irq.h](irq_8h.md)

Public interface for configuring interrupts.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [irq.h](arch_2xtensa_2irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
