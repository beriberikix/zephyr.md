---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2intel64_2thread_8h_source.html
original_path: doxygen/html/arch_2x86_2intel64_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2x86_2intel64_2thread_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_THREAD\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_THREAD\_H\_

8

[ 9](arch_2x86_2intel64_2thread_8h.md#a9976b965d1010def5c40f40be6930461)#define X86\_THREAD\_FLAG\_ALL 0x01 /\* \_thread\_arch.flags: entire state saved \*/

10

11/\*

12 \* GDT selectors - these must agree with the GDT layout in locore.S.

13 \*/

14

[ 15](arch_2x86_2intel64_2thread_8h.md#a53141d432cd6d04e0e47c12fa796886c)#define X86\_KERNEL\_CS\_32 0x08 /\* 32-bit kernel code \*/

[ 16](arch_2x86_2intel64_2thread_8h.md#a71032cef700766c2d1d8661ba26228d1)#define X86\_KERNEL\_DS\_32 0x10 /\* 32-bit kernel data \*/

[ 17](arch_2x86_2intel64_2thread_8h.md#a86a201d2fee57e06985202e366797cee)#define X86\_KERNEL\_CS 0x18 /\* 64-bit kernel code \*/

[ 18](arch_2x86_2intel64_2thread_8h.md#aec469f2b32038a8968280fa8aa7b9eeb)#define X86\_KERNEL\_DS 0x20 /\* 64-bit kernel data \*/

[ 19](arch_2x86_2intel64_2thread_8h.md#a346cd512e6426a7142790ffc5d8cbbc4)#define X86\_USER\_CS\_32 0x28 /\* 32-bit user data (unused) \*/

[ 20](arch_2x86_2intel64_2thread_8h.md#a5ee9fd539d1fa910dd924bb391566a74)#define X86\_USER\_DS 0x30 /\* 64-bit user mode data \*/

[ 21](arch_2x86_2intel64_2thread_8h.md#a4e231b18c27e74b82d7a1021784cb65d)#define X86\_USER\_CS 0x38 /\* 64-bit user mode code \*/

22

23/\* Value programmed into bits 63:32 of STAR MSR with proper segment

24 \* descriptors for implementing user mode with syscall/sysret

25 \*/

[ 26](arch_2x86_2intel64_2thread_8h.md#a878f72d5fdb7380968713ef35fa86899)#define X86\_STAR\_UPPER ((X86\_USER\_CS\_32 << 16) | X86\_KERNEL\_CS)

27

[ 28](arch_2x86_2intel64_2thread_8h.md#ae5e8af7e75778451925d9a94322c39ab)#define X86\_KERNEL\_CPU0\_TR 0x40 /\* 64-bit task state segment \*/

[ 29](arch_2x86_2intel64_2thread_8h.md#a3f7c36aa07ea09dfaedc41d50339d563)#define X86\_KERNEL\_CPU1\_TR 0x50 /\* 64-bit task state segment \*/

[ 30](arch_2x86_2intel64_2thread_8h.md#ad706983ae625a525a0ff4d4b5e6f9df4)#define X86\_KERNEL\_CPU2\_TR 0x60 /\* 64-bit task state segment \*/

[ 31](arch_2x86_2intel64_2thread_8h.md#a04c092d0b318251a296a9ed64f7b1fa5)#define X86\_KERNEL\_CPU3\_TR 0x70 /\* 64-bit task state segment \*/

32

33/\*

34 \* Some SSE definitions. Ideally these will ultimately be shared with 32-bit.

35 \*/

36

[ 37](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)#define X86\_FXSAVE\_SIZE 512 /\* size and alignment of buffer ... \*/

[ 38](arch_2x86_2intel64_2thread_8h.md#a7a6607831b2b148ce38e7715907ef31c)#define X86\_FXSAVE\_ALIGN 16 /\* ... for FXSAVE/FXRSTOR ops \*/

39

40/\* MXCSR Control and Status Register for SIMD floating-point operations.

41 \* Set default value 1F80H according to the Intel(R) 64 and IA-32 Manual.

42 \* Disable denormals-are-zeros mode.

43 \*/

[ 44](arch_2x86_2intel64_2thread_8h.md#a1a95e6241909317576dea666aa1959c9)#define X86\_MXCSR\_SANE 0x1f80

45

46#ifndef \_ASMLANGUAGE

47

48#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

49#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h.md)>

50

51/\*

52 \* 64-bit Task State Segment. One defined per CPU.

53 \*/

54

[ 55](structx86__tss64.md)struct [x86\_tss64](structx86__tss64.md) {

56 /\*

57 \* Architecturally-defined portion. It is somewhat tedious to

58 \* enumerate each member specifically (rather than using arrays)

59 \* but we need to get (some of) their offsets from assembly.

60 \*/

61

[ 62](structx86__tss64.md#a3ff44c512471f9cc2c4c6646d238857b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved0](structx86__tss64.md#a3ff44c512471f9cc2c4c6646d238857b)[4];

63

[ 64](structx86__tss64.md#ab6a7bd042da10b4540ac2f208df12dc6) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rsp0](structx86__tss64.md#ab6a7bd042da10b4540ac2f208df12dc6); /\* privileged stacks \*/

[ 65](structx86__tss64.md#a3480fa4dbb902b1432877367643caa67) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rsp1](structx86__tss64.md#a3480fa4dbb902b1432877367643caa67);

[ 66](structx86__tss64.md#aa57637fcc7fb8d3c3aaba20a904dad8c) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [rsp2](structx86__tss64.md#aa57637fcc7fb8d3c3aaba20a904dad8c);

67

[ 68](structx86__tss64.md#acf57e387decb430168f62d02e185b481) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structx86__tss64.md#acf57e387decb430168f62d02e185b481)[8];

69

[ 70](structx86__tss64.md#aad1ee7a792e1d84ffbd450aeb2f512c6) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist1](structx86__tss64.md#aad1ee7a792e1d84ffbd450aeb2f512c6); /\* interrupt stacks \*/

[ 71](structx86__tss64.md#a104c0c491e7d42742b971e620c7413c4) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist2](structx86__tss64.md#a104c0c491e7d42742b971e620c7413c4);

[ 72](structx86__tss64.md#a6967793f8c50fff0fe45fe3be89213e0) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist3](structx86__tss64.md#a6967793f8c50fff0fe45fe3be89213e0);

[ 73](structx86__tss64.md#a5c1639407277f12412aef9a36f62f7f8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist4](structx86__tss64.md#a5c1639407277f12412aef9a36f62f7f8);

[ 74](structx86__tss64.md#ac028c09a272d34ac66cde1556f5b95cb) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist5](structx86__tss64.md#ac028c09a272d34ac66cde1556f5b95cb);

[ 75](structx86__tss64.md#a2a5dba1c1f8a16f42ff83ce4d34f1873) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist6](structx86__tss64.md#a2a5dba1c1f8a16f42ff83ce4d34f1873);

[ 76](structx86__tss64.md#a652e42fc803a5176f4e1c46588c70204) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [ist7](structx86__tss64.md#a652e42fc803a5176f4e1c46588c70204);

77

[ 78](structx86__tss64.md#a44383c388151792d34b34d331df8fc4e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved1](structx86__tss64.md#a44383c388151792d34b34d331df8fc4e)[10];

79

[ 80](structx86__tss64.md#ac83f83b8b8a399ac988911b75d3e66d3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iomapb](structx86__tss64.md#ac83f83b8b8a399ac988911b75d3e66d3); /\* offset to I/O base \*/

81

82 /\*

83 \* Zephyr specific portion. Stash per-CPU data here for convenience.

84 \*/

85

[ 86](structx86__tss64.md#a34157a050bb727f67286482e6d0c34dd) struct \_cpu \*[cpu](structx86__tss64.md#a34157a050bb727f67286482e6d0c34dd);

87#ifdef CONFIG\_USERSPACE

88 /\* Privilege mode stack pointer value when doing a system call \*/

[ 89](structx86__tss64.md#a959e976899cdcff13cfafba8514489f5) char \*[psp](structx86__tss64.md#a959e976899cdcff13cfafba8514489f5);

90

91 /\* Storage area for user mode stack pointer when doing a syscall \*/

[ 92](structx86__tss64.md#afe97afae56793aae5ed3ba35f4b06143) char \*[usp](structx86__tss64.md#afe97afae56793aae5ed3ba35f4b06143);

93#endif /\* CONFIG\_USERSPACE \*/

94} \_\_packed \_\_aligned(8);

95

[ 96](arch_2x86_2intel64_2thread_8h.md#af11b6454439f03e21b92bceff9ed7f00)typedef struct [x86\_tss64](structx86__tss64.md) [x86\_tss64\_t](arch_2x86_2intel64_2thread_8h.md#af11b6454439f03e21b92bceff9ed7f00);

97

98/\*

99 \* The \_callee\_saved registers are unconditionally saved/restored across

100 \* context switches; the \_thread\_arch registers are only preserved when

101 \* the thread is interrupted. \_arch\_thread.flags tells \_\_resume when to

102 \* cheat and only restore the first set. For more details see locore.S.

103 \*/

104

105struct \_callee\_saved {

106 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rsp;

107 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rbx;

108 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rbp;

109 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r12;

110 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r13;

111 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r14;

112 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r15;

113 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rip;

114 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rflags;

115};

116

117typedef struct \_callee\_saved \_callee\_saved\_t;

118

119struct \_thread\_arch {

120 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flags;

121

122#ifdef CONFIG\_USERSPACE

123#ifndef CONFIG\_X86\_COMMON\_PAGE\_TABLE

124 /\* Physical address of the page tables used by this thread \*/

125 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) ptables;

126#endif /\* CONFIG\_X86\_COMMON\_PAGE\_TABLE \*/

127

128 /\* Initial privilege mode stack pointer when doing a system call.

129 \* Un-set for supervisor threads.

130 \*/

131 char \*psp;

132

133 /\* SS and CS selectors for this thread when restoring context \*/

134 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ss;

135 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cs;

136#endif

137

138 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rax;

139 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rcx;

140 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rdx;

141 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rsi;

142 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) rdi;

143 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r8;

144 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r9;

145 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r10;

146 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r11;

147 char \_\_aligned([X86\_FXSAVE\_ALIGN](arch_2x86_2intel64_2thread_8h.md#a7a6607831b2b148ce38e7715907ef31c)) sse[[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)];

148};

149

150typedef struct \_thread\_arch \_thread\_arch\_t;

151

152#endif /\* \_ASMLANGUAGE \*/

153

154#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL64\_THREAD\_H\_ \*/

[X86\_FXSAVE\_ALIGN](arch_2x86_2intel64_2thread_8h.md#a7a6607831b2b148ce38e7715907ef31c)

#define X86\_FXSAVE\_ALIGN

**Definition** thread.h:38

[X86\_FXSAVE\_SIZE](arch_2x86_2intel64_2thread_8h.md#ace21a6c2662fc989b5a51a2ebb53d129)

#define X86\_FXSAVE\_SIZE

**Definition** thread.h:37

[x86\_tss64\_t](arch_2x86_2intel64_2thread_8h.md#af11b6454439f03e21b92bceff9ed7f00)

struct x86\_tss64 x86\_tss64\_t

**Definition** thread.h:96

[types.h](include_2zephyr_2types_8h.md)

[mmustructs.h](mmustructs_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[x86\_tss64](structx86__tss64.md)

**Definition** thread.h:55

[x86\_tss64::ist2](structx86__tss64.md#a104c0c491e7d42742b971e620c7413c4)

uint64\_t ist2

**Definition** thread.h:71

[x86\_tss64::ist6](structx86__tss64.md#a2a5dba1c1f8a16f42ff83ce4d34f1873)

uint64\_t ist6

**Definition** thread.h:75

[x86\_tss64::cpu](structx86__tss64.md#a34157a050bb727f67286482e6d0c34dd)

struct \_cpu \* cpu

**Definition** thread.h:86

[x86\_tss64::rsp1](structx86__tss64.md#a3480fa4dbb902b1432877367643caa67)

uint64\_t rsp1

**Definition** thread.h:65

[x86\_tss64::reserved0](structx86__tss64.md#a3ff44c512471f9cc2c4c6646d238857b)

uint8\_t reserved0[4]

**Definition** thread.h:62

[x86\_tss64::reserved1](structx86__tss64.md#a44383c388151792d34b34d331df8fc4e)

uint8\_t reserved1[10]

**Definition** thread.h:78

[x86\_tss64::ist4](structx86__tss64.md#a5c1639407277f12412aef9a36f62f7f8)

uint64\_t ist4

**Definition** thread.h:73

[x86\_tss64::ist7](structx86__tss64.md#a652e42fc803a5176f4e1c46588c70204)

uint64\_t ist7

**Definition** thread.h:76

[x86\_tss64::ist3](structx86__tss64.md#a6967793f8c50fff0fe45fe3be89213e0)

uint64\_t ist3

**Definition** thread.h:72

[x86\_tss64::psp](structx86__tss64.md#a959e976899cdcff13cfafba8514489f5)

char \* psp

**Definition** thread.h:89

[x86\_tss64::rsp2](structx86__tss64.md#aa57637fcc7fb8d3c3aaba20a904dad8c)

uint64\_t rsp2

**Definition** thread.h:66

[x86\_tss64::ist1](structx86__tss64.md#aad1ee7a792e1d84ffbd450aeb2f512c6)

uint64\_t ist1

**Definition** thread.h:70

[x86\_tss64::rsp0](structx86__tss64.md#ab6a7bd042da10b4540ac2f208df12dc6)

uint64\_t rsp0

**Definition** thread.h:64

[x86\_tss64::ist5](structx86__tss64.md#ac028c09a272d34ac66cde1556f5b95cb)

uint64\_t ist5

**Definition** thread.h:74

[x86\_tss64::iomapb](structx86__tss64.md#ac83f83b8b8a399ac988911b75d3e66d3)

uint16\_t iomapb

**Definition** thread.h:80

[x86\_tss64::reserved](structx86__tss64.md#acf57e387decb430168f62d02e185b481)

uint8\_t reserved[8]

**Definition** thread.h:68

[x86\_tss64::usp](structx86__tss64.md#afe97afae56793aae5ed3ba35f4b06143)

char \* usp

**Definition** thread.h:92

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel64](dir_1abf87bed33eaf4508c3178cbd4d6168.md)
- [thread.h](arch_2x86_2intel64_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
