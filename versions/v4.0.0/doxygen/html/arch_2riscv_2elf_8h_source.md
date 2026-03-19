---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2riscv_2elf_8h_source.html
original_path: doxygen/html/arch_2riscv_2elf_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf.h

[Go to the documentation of this file.](arch_2riscv_2elf_8h.md)

1

8/\*

9 \* Copyright (c) 2024 CISPA Helmholtz Center for Information Security gGmbH

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13#ifndef ZEPHYR\_ARCH\_RISCV\_ELF\_H

14#define ZEPHYR\_ARCH\_RISCV\_ELF\_H

15

16#include <[stdint.h](stdint_8h.md)>

17#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

27

28#define R\_RISCV\_NONE 0

29#define R\_RISCV\_32 1

30#define R\_RISCV\_64 2

31#define R\_RISCV\_RELATIVE 3

32#define R\_RISCV\_COPY 4

33#define R\_RISCV\_JUMP\_SLOT 5

34#define R\_RISCV\_TLS\_DTPMOD32 6

35#define R\_RISCV\_TLS\_DTPMOD64 7

36#define R\_RISCV\_TLS\_DTPREL32 8

37#define R\_RISCV\_TLS\_DTPREL64 9

38#define R\_RISCV\_TLS\_TPREL32 10

39#define R\_RISCV\_TLS\_TPREL64 11

40#define R\_RISCV\_TLSDESC 12

41/\* 13-15 reserved \*/

42#define R\_RISCV\_BRANCH 16

43#define R\_RISCV\_JAL 17

44#define R\_RISCV\_CALL 18

45#define R\_RISCV\_CALL\_PLT 19

46#define R\_RISCV\_GOT\_HI20 20

47#define R\_RISCV\_TLS\_GOT\_HI20 21

48#define R\_RISCV\_TLS\_GD\_HI20 22

49#define R\_RISCV\_PCREL\_HI20 23

50#define R\_RISCV\_PCREL\_LO12\_I 24

51#define R\_RISCV\_PCREL\_LO12\_S 25

52#define R\_RISCV\_HI20 26

53#define R\_RISCV\_LO12\_I 27

54#define R\_RISCV\_LO12\_S 28

55#define R\_RISCV\_TPREL\_HI20 29

56#define R\_RISCV\_TPREL\_LO12\_I 30

57#define R\_RISCV\_TPREL\_LO12\_S 31

58#define R\_RISCV\_TPREL\_ADD 32

59#define R\_RISCV\_ADD8 33

60#define R\_RISCV\_ADD16 34

61#define R\_RISCV\_ADD32 35

62#define R\_RISCV\_ADD64 36

63#define R\_RISCV\_SUB8 37

64#define R\_RISCV\_SUB16 38

65#define R\_RISCV\_SUB32 39

66#define R\_RISCV\_SUB64 40

67#define R\_RISCV\_GOT32\_PCREL 41

68/\* 42 reserved \*/

69#define R\_RISCV\_ALIGN 43

70/\* next two refer to compressed instructions \*/

71#define R\_RISCV\_RVC\_BRANCH 44

72#define R\_RISCV\_RVC\_JUMP 45

73/\* 46-50 reserved \*/

74#define R\_RISCV\_RELAX 51

75#define R\_RISCV\_SUB6 52

76#define R\_RISCV\_SET6 53

77#define R\_RISCV\_SET8 54

78#define R\_RISCV\_SET16 55

79#define R\_RISCV\_SET32 56

80#define R\_RISCV\_32\_PCREL 57

81#define R\_RISCV\_IRELATIVE 58

82#define R\_RISCV\_PLT32 59

83#define R\_RISCV\_SET\_ULEB128 60

84#define R\_RISCV\_SUB\_ULEB128 61

85#define R\_RISCV\_TLSDESC\_HI20 62

86#define R\_RISCV\_TLSDESC\_LOAD\_LO12 63

87#define R\_RISCV\_TLSDESC\_ADD\_LO12 64

88#define R\_RISCV\_TLSDESC\_CALL 65

89/\* 66-190 reserved \*/

90#define R\_RISCV\_VENDOR 191

91/\* 192-255 reserved \*/

93

98#if defined(CONFIG\_64BIT)

99typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) r\_riscv\_wordclass\_t;

100#else

101typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) r\_riscv\_wordclass\_t;

102#endif

104

[ 110](arch_2riscv_2elf_8h.md#a373699c920d9ff459a0ae2bedf4b71d6)#define R\_RISCV\_IMM8\_GET\_BIT(imm8, bit) (((imm8) & BIT(bit)) >> (bit))

111

[ 118](arch_2riscv_2elf_8h.md#a1657a470d96458e5abdbfc08a31a92c7)#define R\_RISCV\_BTYPE\_IMM8\_MASK(imm8) \

119 ((R\_RISCV\_IMM8\_GET\_BIT(imm8, 12) << 31) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 10) << 30) | \

120 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 9) << 29) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 8) << 28) | \

121 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 7) << 27) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 6) << 26) | \

122 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 5) << 25) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 4) << 11) | \

123 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 3) << 10) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 2) << 9) | \

124 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 1) << 8) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 11) << 7))

125

[ 132](arch_2riscv_2elf_8h.md#a209ba3c784b15adc41b10b35299e43e1)#define R\_RISCV\_JTYPE\_IMM8\_MASK(imm8) \

133 ((R\_RISCV\_IMM8\_GET\_BIT(imm8, 20) << 31) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 10) << 30) | \

134 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 9) << 29) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 8) << 28) | \

135 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 7) << 27) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 6) << 26) | \

136 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 5) << 25) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 4) << 24) | \

137 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 3) << 23) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 2) << 22) | \

138 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 1) << 21) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 11) << 20) | \

139 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 19) << 19) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 18) << 18) | \

140 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 17) << 17) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 16) << 16) | \

141 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 15) << 15) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 14) << 14) | \

142 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 13) << 13) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 12) << 12))

143

[ 149](arch_2riscv_2elf_8h.md#a449d28e8da3f67e6d95df42d5e578aa3)#define R\_RISCV\_STYPE\_IMM8\_MASK(imm8) \

150 ((R\_RISCV\_IMM8\_GET\_BIT(imm8, 11) << 31) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 10) << 30) | \

151 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 9) << 29) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 8) << 28) | \

152 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 7) << 27) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 6) << 26) | \

153 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 5) << 25) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 4) << 11) | \

154 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 3) << 10) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 2) << 9) | \

155 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 1) << 8) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 0) << 7))

156

[ 163](arch_2riscv_2elf_8h.md#a67eef921ccb1b3f70b69d263916ad05d)#define R\_RISCV\_CJTYPE\_IMM8\_MASK(imm8) \

164 ((R\_RISCV\_IMM8\_GET\_BIT(imm8, 11) << 12) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 4) << 11) | \

165 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 9) << 10) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 8) << 9) | \

166 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 10) << 8) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 6) << 7) | \

167 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 7) << 6) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 3) << 5) | \

168 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 2) << 4) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 1) << 3) | \

169 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 5) << 2))

170

[ 177](arch_2riscv_2elf_8h.md#ad5c9a275a624f9ed623d6e88dd53bea3)#define R\_RISCV\_CBTYPE\_IMM8\_MASK(imm8) \

178 ((R\_RISCV\_IMM8\_GET\_BIT(imm8, 8) << 12) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 4) << 11) | \

179 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 3) << 10) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 7) << 6) | \

180 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 6) << 5) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 2) << 4) | \

181 (R\_RISCV\_IMM8\_GET\_BIT(imm8, 1) << 3) | (R\_RISCV\_IMM8\_GET\_BIT(imm8, 5) << 2))

182

[ 188](arch_2riscv_2elf_8h.md#a4919535698f6a4b050504669116665b5)#define R\_RISCV\_CLEAR\_BTYPE\_IMM8(operand) ((operand) & ~R\_RISCV\_BTYPE\_IMM8\_MASK((uint32\_t) -1))

189

[ 196](arch_2riscv_2elf_8h.md#ab34a701190e589da67afae289afde4a7)#define R\_RISCV\_SET\_BTYPE\_IMM8(operand, imm8) \

197 ((R\_RISCV\_CLEAR\_BTYPE\_IMM8(operand)) | R\_RISCV\_BTYPE\_IMM8\_MASK(imm8))

198

[ 204](arch_2riscv_2elf_8h.md#abcc19e420bb224cc8a6a159ee7b26cc2)#define R\_RISCV\_CLEAR\_JTYPE\_IMM8(operand) ((operand) & ~R\_RISCV\_JTYPE\_IMM8\_MASK((uint32\_t) -1))

205

[ 212](arch_2riscv_2elf_8h.md#a754fb9008bc4a39ad34409a757af3510)#define R\_RISCV\_SET\_JTYPE\_IMM8(operand, imm8) \

213 ((R\_RISCV\_CLEAR\_JTYPE\_IMM8(operand)) | R\_RISCV\_JTYPE\_IMM8\_MASK(imm8))

214

[ 220](arch_2riscv_2elf_8h.md#a4ed514a3b1d163d2fe3732c6b0a5a941)#define R\_RISCV\_CLEAR\_STYPE\_IMM8(operand) ((operand) & ~R\_RISCV\_STYPE\_IMM8\_MASK((uint32\_t) -1))

221

[ 228](arch_2riscv_2elf_8h.md#af5471257051b3eff985a1a87cc2dbd5f)#define R\_RISCV\_SET\_STYPE\_IMM8(operand, imm8) \

229 ((R\_RISCV\_CLEAR\_STYPE\_IMM8(operand)) | R\_RISCV\_STYPE\_IMM8\_MASK(imm8))

230

[ 236](arch_2riscv_2elf_8h.md#a965e0f3fcf5faad9ed08381596ac8168)#define R\_RISCV\_CLEAR\_CJTYPE\_IMM8(operand) ((operand) & ~R\_RISCV\_CJTYPE\_IMM8\_MASK((uint32\_t) -1))

237

[ 244](arch_2riscv_2elf_8h.md#a2989a3ea88a01998dd50ed5a9af40450)#define R\_RISCV\_SET\_CJTYPE\_IMM8(operand, imm8) \

245 ((R\_RISCV\_CLEAR\_CJTYPE\_IMM8(operand)) | R\_RISCV\_CJTYPE\_IMM8\_MASK(imm8))

246

[ 252](arch_2riscv_2elf_8h.md#ac79d3798e643d0fd2d703749a3618fe6)#define R\_RISCV\_CLEAR\_CBTYPE\_IMM8(operand) ((operand) & ~R\_RISCV\_CBTYPE\_IMM8\_MASK((uint32\_t) -1))

253

[ 260](arch_2riscv_2elf_8h.md#addf30bebbf4783ff29f2fe5b99e8d02c)#define R\_RISCV\_SET\_CBTYPE\_IMM8(operand, imm8) \

261 ((R\_RISCV\_CLEAR\_CBTYPE\_IMM8(operand)) | R\_RISCV\_CBTYPE\_IMM8\_MASK(imm8))

262

[ 268](arch_2riscv_2elf_8h.md#a498b4a66bc5450871c5752847e813fc5)#define R\_RISCV\_CLEAR\_UTYPE\_IMM8(operand) ((operand) & ~(0xFFFFF000))

269

[ 276](arch_2riscv_2elf_8h.md#a00222ee6cf155a01e6c541dec88045c3)#define R\_RISCV\_SET\_UTYPE\_IMM8(operand, imm8) \

277 ((R\_RISCV\_CLEAR\_UTYPE\_IMM8(operand)) | ((imm8) & 0xFFFFF000))

278

[ 284](arch_2riscv_2elf_8h.md#a5fc196fd73b38a25fbbc31e2225097f4)#define R\_RISCV\_CLEAR\_ITYPE\_IMM8(operand) ((operand) & ~(0xFFF00000))

285

[ 292](arch_2riscv_2elf_8h.md#a56821bda8f04f5c3596a83c77738b208)#define R\_RISCV\_SET\_ITYPE\_IMM8(operand, imm8) ((R\_RISCV\_CLEAR\_ITYPE\_IMM8(operand)) | ((imm8) << 20))

293

294#ifdef \_\_cplusplus

295}

296#endif

297

298#endif /\* ZEPHYR\_ARCH\_RISCV\_ELF\_H \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [elf.h](arch_2riscv_2elf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
