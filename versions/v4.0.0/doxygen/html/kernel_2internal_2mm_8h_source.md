---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/kernel_2internal_2mm_8h_source.html
original_path: doxygen/html/kernel_2internal_2mm_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12

18

40#ifdef CONFIG\_MMU

[ 41](group__kernel__mm__internal__apis.md#gae9f618604758a034b52509c0377d1bdb)#define K\_MEM\_VIRT\_OFFSET ((CONFIG\_KERNEL\_VM\_BASE + CONFIG\_KERNEL\_VM\_OFFSET) - \

42 (CONFIG\_SRAM\_BASE\_ADDRESS + CONFIG\_SRAM\_OFFSET))

43#else

44#define K\_MEM\_VIRT\_OFFSET 0

45#endif /\* CONFIG\_MMU \*/

46

[ 56](group__kernel__mm__internal__apis.md#ga49b13f5f43530952220fb223c3d56d3c)#define K\_MEM\_PHYS\_ADDR(virt) ((virt) - K\_MEM\_VIRT\_OFFSET)

57

[ 67](group__kernel__mm__internal__apis.md#ga850451db4842595d8d96e85a087e8964)#define K\_MEM\_VIRT\_ADDR(phys) ((phys) + K\_MEM\_VIRT\_OFFSET)

68

69#if K\_MEM\_VIRT\_OFFSET != 0

73#define K\_MEM\_IS\_VM\_KERNEL 1

74#ifdef CONFIG\_XIP

75#error "XIP and a virtual memory kernel are not allowed"

76#endif

77#endif

78

79#ifndef \_ASMLANGUAGE

80#include <[stdint.h](stdint_8h.md)>

81#include <stddef.h>

82#include <[inttypes.h](inttypes_8h.md)>

83#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

84#include <[zephyr/sys/mem\_manage.h](mem__manage_8h.md)>

85

[ 97](group__kernel__mm__internal__apis.md#gadc2d4d6258059524eaba2ff139c2f9ff)static inline [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [k\_mem\_phys\_addr](group__kernel__mm__internal__apis.md#gadc2d4d6258059524eaba2ff139c2f9ff)(void \*virt)

98{

99 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) addr = ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))virt;

100

101#if defined(CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK)

102 \_\_ASSERT([sys\_mm\_is\_virt\_addr\_in\_range](group__memory__management.md#ga1a4b707eae142c8f871a198b865e3d16)(virt),

103 "address %p not in permanent mappings", virt);

104#elif defined(CONFIG\_MMU)

105 \_\_ASSERT(

106#if CONFIG\_KERNEL\_VM\_BASE != 0

107 (addr >= CONFIG\_KERNEL\_VM\_BASE) &&

108#endif /\* CONFIG\_KERNEL\_VM\_BASE != 0 \*/

109#if (CONFIG\_KERNEL\_VM\_BASE + CONFIG\_KERNEL\_VM\_SIZE) != 0

110 (addr < (CONFIG\_KERNEL\_VM\_BASE +

111 (CONFIG\_KERNEL\_VM\_SIZE))),

112#else

113 false,

114#endif /\* CONFIG\_KERNEL\_VM\_BASE + CONFIG\_KERNEL\_VM\_SIZE != 0 \*/

115 "address %p not in permanent mappings", virt);

116#else

117 /\* Should be identity-mapped \*/

118 \_\_ASSERT(

119#if CONFIG\_SRAM\_BASE\_ADDRESS != 0

120 (addr >= CONFIG\_SRAM\_BASE\_ADDRESS) &&

121#endif /\* CONFIG\_SRAM\_BASE\_ADDRESS != 0 \*/

122#if (CONFIG\_SRAM\_BASE\_ADDRESS + (CONFIG\_SRAM\_SIZE \* 1024UL)) != 0

123 (addr < (CONFIG\_SRAM\_BASE\_ADDRESS +

124 (CONFIG\_SRAM\_SIZE \* 1024UL))),

125#else

126 false,

127#endif /\* (CONFIG\_SRAM\_BASE\_ADDRESS + (CONFIG\_SRAM\_SIZE \* 1024UL)) != 0 \*/

128 "physical address 0x%lx not in RAM",

129 (unsigned long)addr);

130#endif /\* CONFIG\_MMU \*/

131

132 /\* TODO add assertion that this page is pinned to boot mapping,

133 \* the above checks won't be sufficient with demand paging

134 \*/

135

136 return [K\_MEM\_PHYS\_ADDR](group__kernel__mm__internal__apis.md#ga49b13f5f43530952220fb223c3d56d3c)(addr);

137}

138

[ 150](group__kernel__mm__internal__apis.md#gaed8dccb2a3c15daff9d2e5b4d49f782a)static inline void \*[k\_mem\_virt\_addr](group__kernel__mm__internal__apis.md#gaed8dccb2a3c15daff9d2e5b4d49f782a)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys)

151{

152#if defined(CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK)

153 \_\_ASSERT([sys\_mm\_is\_phys\_addr\_in\_range](group__memory__management.md#gaef71defc60c1d898d5ece56c6826a2e1)(phys),

154 "physical address 0x%lx not in RAM", (unsigned long)phys);

155#else

156 \_\_ASSERT(

157#if CONFIG\_SRAM\_BASE\_ADDRESS != 0

158 (phys >= CONFIG\_SRAM\_BASE\_ADDRESS) &&

159#endif /\* CONFIG\_SRAM\_BASE\_ADDRESS != 0 \*/

160#if (CONFIG\_SRAM\_BASE\_ADDRESS + (CONFIG\_SRAM\_SIZE \* 1024UL)) != 0

161 (phys < (CONFIG\_SRAM\_BASE\_ADDRESS +

162 (CONFIG\_SRAM\_SIZE \* 1024UL))),

163#else

164 false,

165#endif /\* (CONFIG\_SRAM\_BASE\_ADDRESS + (CONFIG\_SRAM\_SIZE \* 1024UL)) != 0 \*/

166 "physical address 0x%lx not in RAM", (unsigned long)phys);

167#endif /\* CONFIG\_KERNEL\_VM\_USE\_CUSTOM\_MEM\_RANGE\_CHECK \*/

168

169 /\* TODO add assertion that this page frame is pinned to boot mapping,

170 \* the above check won't be sufficient with demand paging

171 \*/

172

173 return (void \*)[K\_MEM\_VIRT\_ADDR](group__kernel__mm__internal__apis.md#ga850451db4842595d8d96e85a087e8964)(phys);

174}

175

176#ifdef \_\_cplusplus

177extern "C" {

178#endif

179

[ 224](group__kernel__mm__internal__apis.md#gaa2c52222198f4c7362c183e1397a4e5c)void [k\_mem\_map\_phys\_bare](group__kernel__mm__internal__apis.md#gaa2c52222198f4c7362c183e1397a4e5c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*virt\_ptr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, size\_t size,

225 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

226

[ 254](group__kernel__mm__internal__apis.md#gae713c4eb253302d06f758f87503cf5dd)void [k\_mem\_unmap\_phys\_bare](group__kernel__mm__internal__apis.md#gae713c4eb253302d06f758f87503cf5dd)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*virt, size\_t size);

255

[ 304](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c)void \*[k\_mem\_map\_phys\_guard](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys, size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), bool is\_anon);

305

[ 324](group__kernel__mm__internal__apis.md#gaca476fbacb86815edd4898b13ecf5120)void [k\_mem\_unmap\_phys\_guard](group__kernel__mm__internal__apis.md#gaca476fbacb86815edd4898b13ecf5120)(void \*addr, size\_t size, bool is\_anon);

325

326#ifdef \_\_cplusplus

327}

328#endif

329

331

332#endif /\* !\_ASMLANGUAGE \*/

333#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_INTERNAL\_MM\_H \*/

[\_\_assert.h](____assert_8h.md)

[k\_mem\_map\_phys\_guard](group__kernel__mm__internal__apis.md#ga2aeab99cba24ac3fd9479dbd421f6c5c)

void \* k\_mem\_map\_phys\_guard(uintptr\_t phys, size\_t size, uint32\_t flags, bool is\_anon)

Map memory into virtual address space with guard pages.

[K\_MEM\_PHYS\_ADDR](group__kernel__mm__internal__apis.md#ga49b13f5f43530952220fb223c3d56d3c)

#define K\_MEM\_PHYS\_ADDR(virt)

Get physical address from virtual address.

**Definition** mm.h:56

[K\_MEM\_VIRT\_ADDR](group__kernel__mm__internal__apis.md#ga850451db4842595d8d96e85a087e8964)

#define K\_MEM\_VIRT\_ADDR(phys)

Get virtual address from physical address.

**Definition** mm.h:67

[k\_mem\_map\_phys\_bare](group__kernel__mm__internal__apis.md#gaa2c52222198f4c7362c183e1397a4e5c)

void k\_mem\_map\_phys\_bare(uint8\_t \*\*virt\_ptr, uintptr\_t phys, size\_t size, uint32\_t flags)

Map a physical memory region into the kernel's virtual address space.

[k\_mem\_unmap\_phys\_guard](group__kernel__mm__internal__apis.md#gaca476fbacb86815edd4898b13ecf5120)

void k\_mem\_unmap\_phys\_guard(void \*addr, size\_t size, bool is\_anon)

Un-map memory mapped via k\_mem\_map\_phys\_guard().

[k\_mem\_phys\_addr](group__kernel__mm__internal__apis.md#gadc2d4d6258059524eaba2ff139c2f9ff)

static uintptr\_t k\_mem\_phys\_addr(void \*virt)

Get physical address from virtual address.

**Definition** mm.h:97

[k\_mem\_unmap\_phys\_bare](group__kernel__mm__internal__apis.md#gae713c4eb253302d06f758f87503cf5dd)

void k\_mem\_unmap\_phys\_bare(uint8\_t \*virt, size\_t size)

Unmap a virtual memory region from kernel's virtual address space.

[k\_mem\_virt\_addr](group__kernel__mm__internal__apis.md#gaed8dccb2a3c15daff9d2e5b4d49f782a)

static void \* k\_mem\_virt\_addr(uintptr\_t phys)

Get virtual address from physical address.

**Definition** mm.h:150

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

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [internal](dir_5a28aaecc3642d39af859931377173ec.md)
- [mm.h](kernel_2internal_2mm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
