---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2xtensa_2gdbstub_8h_source.html
original_path: doxygen/html/arch_2xtensa_2gdbstub_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdbstub.h

[Go to the documentation of this file.](arch_2xtensa_2gdbstub_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[inttypes.h](inttypes_8h.md)>

8

9#ifndef ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_GDBSTUB\_SYS\_H\_

10#define ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_GDBSTUB\_SYS\_H\_

11

12#ifdef CONFIG\_GDBSTUB

13

[ 14](arch_2xtensa_2gdbstub_8h.md#a6d8520d58f7d4a35a8d747a2ea2b8b2e)#define XTREG\_GRP\_MASK 0x0F00

[ 15](arch_2xtensa_2gdbstub_8h.md#a6c4b0ec6ff50d409949b3eb675101fa9)#define XTREG\_GRP\_GENERAL 0x0000

[ 16](arch_2xtensa_2gdbstub_8h.md#a4ce12c698d17a8e67b11392362a2a7b8)#define XTREG\_GRP\_ADDR 0x0100

[ 17](arch_2xtensa_2gdbstub_8h.md#a9cebc8c3e734ccb3997757018014b3e3)#define XTREG\_GRP\_SPECIAL 0x0200

[ 18](arch_2xtensa_2gdbstub_8h.md#a1b75ea49d7031c3d9b334dcf636727ca)#define XTREG\_GRP\_USER 0x0300

19

[ 37](structxtensa__register.md)struct [xtensa\_register](structxtensa__register.md) {

[ 39](structxtensa__register.md#a58afab24c5b54d15dcd36ebcdf0e750d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [val](structxtensa__register.md#a58afab24c5b54d15dcd36ebcdf0e750d);

40

[ 42](structxtensa__register.md#a7c2a71ffd07ce4b17c9d8bab43536670) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [idx](structxtensa__register.md#a7c2a71ffd07ce4b17c9d8bab43536670);

43

[ 45](structxtensa__register.md#a4b0b68c1c0b8401cb7f7fdc8ef653844) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [byte\_size](structxtensa__register.md#a4b0b68c1c0b8401cb7f7fdc8ef653844);

46

[ 48](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [regno](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2);

49

[ 54](structxtensa__register.md#aa0a1af384d561e5a33819d64b475bdbb) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [gpkt\_offset](structxtensa__register.md#aa0a1af384d561e5a33819d64b475bdbb);

55

[ 60](structxtensa__register.md#ae2daef15a43d111728d559cb68adee37) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [stack\_offset](structxtensa__register.md#ae2daef15a43d111728d559cb68adee37);

61

[ 63](structxtensa__register.md#a8ec99f010bc979cb4f7736fda9786c7b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [seqno](structxtensa__register.md#a8ec99f010bc979cb4f7736fda9786c7b);

64

[ 69](structxtensa__register.md#aaf92daddc205651cba3aa07d08afbf16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_read\_only](structxtensa__register.md#aaf92daddc205651cba3aa07d08afbf16):1;

70};

71

72/\* Due to Xtensa SoCs being highly configurable,

73 \* the register files between SoCs are not identical.

74 \*

75 \* This means generic registers can, sometimes, have

76 \* different offsets from start of register files

77 \* needed to communicate with GDB.

78 \*

79 \* Therefore, it is better to defer to the SoC layer

80 \* for proper support for GDB.

81 \*/

82#include <gdbstub/soc.h>

83

87struct [gdb\_ctx](structgdb__ctx.md) {

89 unsigned int [exception](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999);

90

[ 92](structgdb__ctx.md#adb06cbd2bc9f322d692f8a73fb18e99d) struct [xtensa\_register](structxtensa__register.md) \*[regs](structgdb__ctx.md#adb06cbd2bc9f322d692f8a73fb18e99d);

93

[ 95](structgdb__ctx.md#a2eb775bca1b96ddfa495620d0a19788d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_regs](structgdb__ctx.md#a2eb775bca1b96ddfa495620d0a19788d);

96

[ 98](structgdb__ctx.md#ac040960f884c235a3b27820d49d30161) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [seqno](structgdb__ctx.md#ac040960f884c235a3b27820d49d30161);

99

[ 101](structgdb__ctx.md#ac4930a460dc63c823b4e8e13e925c067) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [a0\_idx](structgdb__ctx.md#ac4930a460dc63c823b4e8e13e925c067);

102

[ 104](structgdb__ctx.md#ae73c7bcb4e501c9f28308838f0923cd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ar\_idx](structgdb__ctx.md#ae73c7bcb4e501c9f28308838f0923cd0);

105

[ 107](structgdb__ctx.md#a4094f8ee5045ee6ca97fb256b0a93a41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [wb\_idx](structgdb__ctx.md#a4094f8ee5045ee6ca97fb256b0a93a41);

108};

109

[ 116](arch_2xtensa_2gdbstub_8h.md#a60984092197e67f37d85bc8819b97f65)static inline bool [gdb\_xtensa\_is\_logical\_addr\_reg](arch_2xtensa_2gdbstub_8h.md#a60984092197e67f37d85bc8819b97f65)(struct [xtensa\_register](structxtensa__register.md) \*reg)

117{

118 if (reg->[regno](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2) < 16) {

119 return true;

120 } else {

121 return false;

122 }

123}

124

[ 131](arch_2xtensa_2gdbstub_8h.md#a1c2969ce9537bb9adca02a37a4a887c5)static inline bool [gdb\_xtensa\_is\_address\_reg](arch_2xtensa_2gdbstub_8h.md#a1c2969ce9537bb9adca02a37a4a887c5)(struct [xtensa\_register](structxtensa__register.md) \*reg)

132{

133 if ((reg->[regno](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2) & [XTREG\_GRP\_MASK](arch_2xtensa_2gdbstub_8h.md#a6d8520d58f7d4a35a8d747a2ea2b8b2e)) == [XTREG\_GRP\_ADDR](arch_2xtensa_2gdbstub_8h.md#a4ce12c698d17a8e67b11392362a2a7b8)) {

134 return true;

135 } else {

136 return false;

137 }

138}

139

[ 147](arch_2xtensa_2gdbstub_8h.md#a65288d340838b80be483b62e00be3afa)static inline bool [gdb\_xtensa\_is\_special\_reg](arch_2xtensa_2gdbstub_8h.md#a65288d340838b80be483b62e00be3afa)(struct [xtensa\_register](structxtensa__register.md) \*reg)

148{

149 if ((reg->[regno](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2) & [XTREG\_GRP\_MASK](arch_2xtensa_2gdbstub_8h.md#a6d8520d58f7d4a35a8d747a2ea2b8b2e)) == [XTREG\_GRP\_SPECIAL](arch_2xtensa_2gdbstub_8h.md#a9cebc8c3e734ccb3997757018014b3e3)) {

150 return true;

151 } else {

152 return false;

153 }

154}

155

[ 163](arch_2xtensa_2gdbstub_8h.md#ae2cdfe587c68d6e606df46a646343ae7)static inline bool [gdb\_xtensa\_is\_user\_reg](arch_2xtensa_2gdbstub_8h.md#ae2cdfe587c68d6e606df46a646343ae7)(struct [xtensa\_register](structxtensa__register.md) \*reg)

164{

165 if ((reg->[regno](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2) & [XTREG\_GRP\_MASK](arch_2xtensa_2gdbstub_8h.md#a6d8520d58f7d4a35a8d747a2ea2b8b2e)) == [XTREG\_GRP\_USER](arch_2xtensa_2gdbstub_8h.md#a1b75ea49d7031c3d9b334dcf636727ca)) {

166 return true;

167 } else {

168 return false;

169 }

170}

171

172#endif /\* CONFIG\_GDBSTUB \*/

173

174#endif /\* ZEPHYR\_INCLUDE\_ARCH\_XTENSA\_GDBSTUB\_SYS\_H\_ \*/

[XTREG\_GRP\_USER](arch_2xtensa_2gdbstub_8h.md#a1b75ea49d7031c3d9b334dcf636727ca)

#define XTREG\_GRP\_USER

**Definition** gdbstub.h:18

[gdb\_xtensa\_is\_address\_reg](arch_2xtensa_2gdbstub_8h.md#a1c2969ce9537bb9adca02a37a4a887c5)

static bool gdb\_xtensa\_is\_address\_reg(struct xtensa\_register \*reg)

Test if the register is a address register (AR0 - AR31/AR63).

**Definition** gdbstub.h:131

[XTREG\_GRP\_ADDR](arch_2xtensa_2gdbstub_8h.md#a4ce12c698d17a8e67b11392362a2a7b8)

#define XTREG\_GRP\_ADDR

**Definition** gdbstub.h:16

[gdb\_xtensa\_is\_logical\_addr\_reg](arch_2xtensa_2gdbstub_8h.md#a60984092197e67f37d85bc8819b97f65)

static bool gdb\_xtensa\_is\_logical\_addr\_reg(struct xtensa\_register \*reg)

Test if the register is a logical address register (A0 - A15).

**Definition** gdbstub.h:116

[gdb\_xtensa\_is\_special\_reg](arch_2xtensa_2gdbstub_8h.md#a65288d340838b80be483b62e00be3afa)

static bool gdb\_xtensa\_is\_special\_reg(struct xtensa\_register \*reg)

Test if the register is a special register that needs to be accessed via RSR/WSR.

**Definition** gdbstub.h:147

[XTREG\_GRP\_MASK](arch_2xtensa_2gdbstub_8h.md#a6d8520d58f7d4a35a8d747a2ea2b8b2e)

#define XTREG\_GRP\_MASK

**Definition** gdbstub.h:14

[XTREG\_GRP\_SPECIAL](arch_2xtensa_2gdbstub_8h.md#a9cebc8c3e734ccb3997757018014b3e3)

#define XTREG\_GRP\_SPECIAL

**Definition** gdbstub.h:17

[gdb\_xtensa\_is\_user\_reg](arch_2xtensa_2gdbstub_8h.md#ae2cdfe587c68d6e606df46a646343ae7)

static bool gdb\_xtensa\_is\_user\_reg(struct xtensa\_register \*reg)

Test if the register is a user register that needs to be accessed via RUR/WUR.

**Definition** gdbstub.h:163

[inttypes.h](inttypes_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[gdb\_ctx](structgdb__ctx.md)

Architecture specific GDB context.

**Definition** gdbstub.h:61

[gdb\_ctx::num\_regs](structgdb__ctx.md#a2eb775bca1b96ddfa495620d0a19788d)

uint8\_t num\_regs

Number of registers.

**Definition** gdbstub.h:95

[gdb\_ctx::wb\_idx](structgdb__ctx.md#a4094f8ee5045ee6ca97fb256b0a93a41)

uint8\_t wb\_idx

Index in register descriptions of WINDOWBASE register.

**Definition** gdbstub.h:107

[gdb\_ctx::seqno](structgdb__ctx.md#ac040960f884c235a3b27820d49d30161)

uint8\_t seqno

Sequence number.

**Definition** gdbstub.h:98

[gdb\_ctx::a0\_idx](structgdb__ctx.md#ac4930a460dc63c823b4e8e13e925c067)

uint8\_t a0\_idx

Index in register descriptions of A0 register.

**Definition** gdbstub.h:101

[gdb\_ctx::regs](structgdb__ctx.md#adb06cbd2bc9f322d692f8a73fb18e99d)

struct xtensa\_register \* regs

Register descriptions.

**Definition** gdbstub.h:92

[gdb\_ctx::exception](structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999)

unsigned int exception

Exception reason.

**Definition** gdbstub.h:63

[gdb\_ctx::ar\_idx](structgdb__ctx.md#ae73c7bcb4e501c9f28308838f0923cd0)

uint8\_t ar\_idx

Index in register descriptions of AR0 register.

**Definition** gdbstub.h:104

[xtensa\_register](structxtensa__register.md)

Register description for GDB stub.

**Definition** gdbstub.h:37

[xtensa\_register::byte\_size](structxtensa__register.md#a4b0b68c1c0b8401cb7f7fdc8ef653844)

uint8\_t byte\_size

Size of register.

**Definition** gdbstub.h:45

[xtensa\_register::val](structxtensa__register.md#a58afab24c5b54d15dcd36ebcdf0e750d)

uint32\_t val

Register value.

**Definition** gdbstub.h:39

[xtensa\_register::idx](structxtensa__register.md#a7c2a71ffd07ce4b17c9d8bab43536670)

uint8\_t idx

GDB register index (for p/P packets).

**Definition** gdbstub.h:42

[xtensa\_register::seqno](structxtensa__register.md#a8ec99f010bc979cb4f7736fda9786c7b)

uint8\_t seqno

Sequence number.

**Definition** gdbstub.h:63

[xtensa\_register::regno](structxtensa__register.md#a9c85b2544da4849db91f5a70e75630f2)

uint16\_t regno

Xtensa register number.

**Definition** gdbstub.h:48

[xtensa\_register::gpkt\_offset](structxtensa__register.md#aa0a1af384d561e5a33819d64b475bdbb)

int16\_t gpkt\_offset

Offset of this register in GDB G-packet.

**Definition** gdbstub.h:54

[xtensa\_register::is\_read\_only](structxtensa__register.md#aaf92daddc205651cba3aa07d08afbf16)

uint8\_t is\_read\_only

Set to 1 if register should not be written to during debugging.

**Definition** gdbstub.h:69

[xtensa\_register::stack\_offset](structxtensa__register.md#ae2daef15a43d111728d559cb68adee37)

int8\_t stack\_offset

Offset of saved register in stack frame.

**Definition** gdbstub.h:60

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [gdbstub.h](arch_2xtensa_2gdbstub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
