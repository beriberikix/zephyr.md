---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel_2internal_2mm_8h_source.html
original_path: doxygen/html/kernel_2internal_2mm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm.h

[Go to the documentation of this file.](kernel_2internal_2mm_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_KERNEL\_INTERNAL\_MM\_H

8#define ZEPHYR\_INCLUDE\_KERNEL\_INTERNAL\_MM\_H

9

10#include <[zephyr/sys/util.h](util_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12

18

19/\*

20 \* This is the offset to subtract from a virtual address mapped in the

21 \* kernel's permanent mapping of RAM, to obtain its physical address.

22 \*

23 \* virt\_addr = phys\_addr + Z\_MEM\_VM\_OFFSET

24 \*

25 \* This only works for virtual addresses within the interval

26 \* [CONFIG\_KERNEL\_VM\_BASE, CONFIG\_KERNEL\_VM\_BASE + (CONFIG\_SRAM\_SIZE \* 1024)).

27 \*

28 \* These macros are intended for assembly, linker code, and static initializers.

29 \* Use with care.

30 \*

31 \* Note that when demand paging is active, these will only work with page

32 \* frames that are pinned to their virtual mapping at boot.

33 \*

34 \* TODO: This will likely need to move to an arch API or need additional

35 \* constraints defined.

36 \*/

37#ifdef CONFIG\_MMU

38#define Z\_MEM\_VM\_OFFSET ((CONFIG\_KERNEL\_VM\_BASE + CONFIG\_KERNEL\_VM\_OFFSET) - \

39 (CONFIG\_SRAM\_BASE\_ADDRESS + CONFIG\_SRAM\_OFFSET))

40#else

41#define Z\_MEM\_VM\_OFFSET 0

42#endif

43

44#define Z\_MEM\_PHYS\_ADDR(virt) ((virt) - Z\_MEM\_VM\_OFFSET)

45#define Z\_MEM\_VIRT\_ADDR(phys) ((phys) + Z\_MEM\_VM\_OFFSET)

46

47#if Z\_MEM\_VM\_OFFSET != 0

48#define Z\_VM\_KERNEL 1

49#ifdef CONFIG\_XIP

50#error "XIP and a virtual memory kernel are not allowed"

51#endif

52#endif

53

54#ifndef \_ASMLANGUAGE

55#include <[stdint.h](stdint_8h.md)>

56#include <stddef.h>

57#include <[inttypes.h](inttypes_8h.md)>

58#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

59#include <[zephyr/sys/mem\_manage.h](mem__manage_8h.md)>

60

61/\* Just like Z\_MEM\_PHYS\_ADDR() but with type safety and assertions \*/

62static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) z\_mem\_phys\_addr(void \*virt)

63{

64 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))virt;

65

66#if defined(CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK)

67 \_\_ASSERT([sys\_mm\_is\_virt\_addr\_in\_range](group__memory__management.md#ga1a4b707eae142c8f871a198b865e3d16)(virt),

68 "address %p not in permanent mappings", virt);

69#elif defined(CONFIG\_MMU)

70 \_\_ASSERT(

71#if CONFIG\_KERNEL\_VM\_BASE != 0

72 (addr >= CONFIG\_KERNEL\_VM\_BASE) &&

73#endif

74#if (CONFIG\_KERNEL\_VM\_BASE + CONFIG\_KERNEL\_VM\_SIZE) != 0

75 (addr < (CONFIG\_KERNEL\_VM\_BASE +

76 (CONFIG\_KERNEL\_VM\_SIZE))),

77#else

78 false,

79#endif

80 "address %p not in permanent mappings", virt);

81#else

82 /\* Should be identity-mapped \*/

83 \_\_ASSERT(

84#if CONFIG\_SRAM\_BASE\_ADDRESS != 0

85 (addr >= CONFIG\_SRAM\_BASE\_ADDRESS) &&

86#endif

87#if (CONFIG\_SRAM\_BASE\_ADDRESS + (CONFIG\_SRAM\_SIZE \* 1024UL)) != 0

88 (addr < (CONFIG\_SRAM\_BASE\_ADDRESS +

89 (CONFIG\_SRAM\_SIZE \* 1024UL))),

90#else

91 false,

92#endif

93 "physical address 0x%lx not in RAM",

94 (unsigned long)addr);

95#endif /\* CONFIG\_MMU \*/

96

97 /\* TODO add assertion that this page is pinned to boot mapping,

98 \* the above checks won't be sufficient with demand paging

99 \*/

100

101 return Z\_MEM\_PHYS\_ADDR(addr);

102}

103

104/\* Just like Z\_MEM\_VIRT\_ADDR() but with type safety and assertions \*/

105static inline void \*z\_mem\_virt\_addr([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys)

106{

107#if defined(CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK)

108 \_\_ASSERT([sys\_mm\_is\_phys\_addr\_in\_range](group__memory__management.md#gaef71defc60c1d898d5ece56c6826a2e1)(phys),

109 "physical address 0x%lx not in RAM", (unsigned long)phys);

110#else

111 \_\_ASSERT(

112#if CONFIG\_SRAM\_BASE\_ADDRESS != 0

113 (phys >= CONFIG\_SRAM\_BASE\_ADDRESS) &&

114#endif

115#if (CONFIG\_SRAM\_BASE\_ADDRESS + (CONFIG\_SRAM\_SIZE \* 1024UL)) != 0

116 (phys < (CONFIG\_SRAM\_BASE\_ADDRESS +

117 (CONFIG\_SRAM\_SIZE \* 1024UL))),

118#else

119 false,

120#endif

121 "physical address 0x%lx not in RAM", (unsigned long)phys);

122#endif

123

124 /\* TODO add assertion that this page frame is pinned to boot mapping,

125 \* the above check won't be sufficient with demand paging

126 \*/

127

128 return (void \*)Z\_MEM\_VIRT\_ADDR(phys);

129}

130

131#ifdef \_\_cplusplus

132extern "C" {

133#endif

134

176void z\_phys\_map([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*virt\_ptr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, size\_t size,

177 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

178

206void z\_phys\_unmap([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*virt, size\_t size);

207

208#ifdef \_\_cplusplus

209}

210#endif

211

213

214#endif /\* !\_ASMLANGUAGE \*/

215#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_INTERNAL\_MM\_H \*/

[\_\_assert.h](____assert_8h.md)

[sys\_mm\_is\_virt\_addr\_in\_range](group__memory__management.md#ga1a4b707eae142c8f871a198b865e3d16)

bool sys\_mm\_is\_virt\_addr\_in\_range(void \*virt)

Check if a virtual address is within range of virtual memory.

[sys\_mm\_is\_phys\_addr\_in\_range](group__memory__management.md#gaef71defc60c1d898d5ece56c6826a2e1)

bool sys\_mm\_is\_phys\_addr\_in\_range(uintptr\_t phys)

Check if a physical address is within range of physical memory.

[inttypes.h](inttypes_8h.md)

[mem\_manage.h](mem__manage_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [internal](dir_5a28aaecc3642d39af859931377173ec.md)
- [mm.h](kernel_2internal_2mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
