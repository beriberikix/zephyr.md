---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/x86_2intel64_2arch_8h_source.html
original_path: doxygen/html/x86_2intel64_2arch_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h

[Go to the documentation of this file.](x86_2intel64_2arch_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corp.

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

13

14#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_ARCH\_H\_

15#define ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_ARCH\_H\_

16

17#include <[zephyr/arch/x86/intel64/exception.h](x86_2intel64_2exception_8h.md)>

18#include <[zephyr/arch/x86/intel64/thread.h](arch_2x86_2intel64_2thread_8h.md)>

19#include <[zephyr/arch/x86/thread\_stack.h](arch_2x86_2thread__stack_8h.md)>

20#if defined(CONFIG\_PCIE) && !defined(\_ASMLANGUAGE)

21#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

22#endif

23

24#if CONFIG\_ISR\_STACK\_SIZE != (CONFIG\_ISR\_SUBSTACK\_SIZE \* CONFIG\_ISR\_DEPTH)

25#error "Check ISR stack configuration (CONFIG\_ISR\_\*)"

26#endif

27

28#if CONFIG\_ISR\_SUBSTACK\_SIZE % ARCH\_STACK\_PTR\_ALIGN

29#error "CONFIG\_ISR\_SUBSTACK\_SIZE must be a multiple of 16"

30#endif

31

32#ifndef \_ASMLANGUAGE

33

[ 34](x86_2intel64_2arch_8h.md#aed9cf591fb95242f161e6fc8719cf3e3)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [sys\_write64](x86_2intel64_2arch_8h.md#aed9cf591fb95242f161e6fc8719cf3e3)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

35{

36 \_\_asm\_\_ volatile("movq %0, %1"

37 :

38 : "r"(data), "m" (\*(volatile [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)

39 ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

40 : "memory");

41}

42

[ 43](x86_2intel64_2arch_8h.md#a7ba6099642d909c50219d174c35f6a94)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_read64](x86_2intel64_2arch_8h.md#a7ba6099642d909c50219d174c35f6a94)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr)

44{

45 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret;

46

47 \_\_asm\_\_ volatile("movq %1, %0"

48 : "=r"(ret)

49 : "m" (\*(volatile [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) addr)

50 : "memory");

51

52 return ret;

53}

54

[ 55](x86_2intel64_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) unsigned int [arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)(void)

56{

57 unsigned long key;

58

59 \_\_asm\_\_ volatile ("pushfq; cli; popq %0" : "=g" (key) : : "memory");

60

61 return (unsigned int) key;

62}

63

[ 64](x86_2intel64_2arch_8h.md#a8d3604770d7735d229e7d2fef4ff590a)#define ARCH\_EXCEPT(reason\_p) do { \

65 \_\_asm\_\_ volatile( \

66 "movq %[reason], %%rax\n\t" \

67 "int $32\n\t" \

68 : \

69 : [reason] "i" (reason\_p)); \

70 CODE\_UNREACHABLE; /\* LCOV\_EXCL\_LINE \*/ \

71} while (false)

72

73#ifdef CONFIG\_PCIE

74#define X86\_RESERVE\_IRQ(irq\_p, name) \

75 static TYPE\_SECTION\_ITERABLE(uint8\_t, name, irq\_alloc, name) = irq\_p

76#else

[ 77](x86_2intel64_2arch_8h.md#a7b93ddbf458746ef3d189dfd10888077)#define X86\_RESERVE\_IRQ(irq\_p, name)

78#endif

79

80#endif /\* \_ASMLANGUAGE \*/

81

82/\*

83 \* All Intel64 interrupts are dynamically connected.

84 \*/

85

[ 86](x86_2intel64_2arch_8h.md#accdf8a59e00ac1c1fcedc18b78be4b8a)#define ARCH\_IRQ\_CONNECT(irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) \

87 X86\_RESERVE\_IRQ(irq\_p, \_CONCAT(\_irq\_alloc\_fixed, \_\_COUNTER\_\_)); \

88 arch\_irq\_connect\_dynamic(irq\_p, priority\_p, \

89 (void (\*)(const void \*))isr\_p, \

90 isr\_param\_p, flags\_p)

91

92#ifdef CONFIG\_PCIE

93

94#define ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

95 isr\_p, isr\_param\_p, flags\_p) \

96 X86\_RESERVE\_IRQ(irq\_p, \_CONCAT(\_irq\_alloc\_fixed, \_\_COUNTER\_\_)); \

97 pcie\_connect\_dynamic\_irq(bdf\_p, irq\_p, priority\_p, \

98 (void (\*)(const void \*))isr\_p, \

99 isr\_param\_p, flags\_p)

100

101#endif /\* CONFIG\_PCIE \*/

102

103/\*

104 \* Thread object needs to be 16-byte aligned.

105 \*/

[ 106](x86_2intel64_2arch_8h.md#ad0a10d482624ef8d91859f5bcdc2f647)#define ARCH\_DYNAMIC\_OBJ\_K\_THREAD\_ALIGNMENT 16

107

108#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_ARCH\_H\_ \*/

[thread.h](arch_2x86_2intel64_2thread_8h.md)

[thread\_stack.h](arch_2x86_2thread__stack_8h.md)

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[arch\_irq\_lock](mips_2arch_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

**Definition** arch.h:72

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[sys\_read64](x86_2intel64_2arch_8h.md#a7ba6099642d909c50219d174c35f6a94)

static ALWAYS\_INLINE uint64\_t sys\_read64(mm\_reg\_t addr)

**Definition** arch.h:43

[sys\_write64](x86_2intel64_2arch_8h.md#aed9cf591fb95242f161e6fc8719cf3e3)

static ALWAYS\_INLINE void sys\_write64(uint64\_t data, mm\_reg\_t addr)

**Definition** arch.h:34

[exception.h](x86_2intel64_2exception_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [arch.h](x86_2intel64_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
