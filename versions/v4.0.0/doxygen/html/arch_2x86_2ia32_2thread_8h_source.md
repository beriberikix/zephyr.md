---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2ia32_2thread_8h_source.html
original_path: doxygen/html/arch_2x86_2ia32_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2x86_2ia32_2thread_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_THREAD\_H\_

20#define ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_THREAD\_H\_

21

29#if defined(CONFIG\_EAGER\_FPU\_SHARING) || defined(CONFIG\_LAZY\_FPU\_SHARING)

30#ifdef CONFIG\_X86\_SSE

31#define FP\_REG\_SET\_ALIGN 16

32#else

33#define FP\_REG\_SET\_ALIGN 4

34#endif

35#else

36/\* Unused, no special alignment requirements, use default alignment for

37 \* char buffers on this arch

38 \*/

[ 39](arch_2x86_2ia32_2thread_8h.md#af99d45d7fb31caf8f4abf9306fb654a3)#define FP\_REG\_SET\_ALIGN 1

40#endif /\* CONFIG\_\*\_FP\_SHARING \*/

41

42/\*

43 \* Bits for \_thread\_arch.flags, see their use in intstub.S et al.

44 \*/

45

[ 46](arch_2x86_2ia32_2thread_8h.md#adb3b8047e5ebfc1305e7616991913818)#define X86\_THREAD\_FLAG\_INT 0x01

[ 47](arch_2x86_2ia32_2thread_8h.md#a01b9d81506f2cacafd8b5c1341d30207)#define X86\_THREAD\_FLAG\_EXC 0x02

[ 48](arch_2x86_2ia32_2thread_8h.md#a9976b965d1010def5c40f40be6930461)#define X86\_THREAD\_FLAG\_ALL (X86\_THREAD\_FLAG\_INT | X86\_THREAD\_FLAG\_EXC)

49

50#ifndef \_ASMLANGUAGE

51#include <[stdint.h](stdint_8h.md)>

52#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h.md)>

53

54/\*

55 \* The following structure defines the set of 'non-volatile' integer registers.

56 \* These registers must be preserved by a called C function. These are the

57 \* only registers that need to be saved/restored when a cooperative context

58 \* switch occurs.

59 \*/

60

61struct \_callee\_saved {

62 unsigned long esp;

63

64 /\*

65 \* The following registers are considered non-volatile, i.e.

66 \* callee-save,

67 \* but their values are pushed onto the stack rather than stored in the

68 \* TCS

69 \* structure:

70 \*

71 \* unsigned long ebp;

72 \* unsigned long ebx;

73 \* unsigned long esi;

74 \* unsigned long edi;

75 \*/

76

77};

78

79typedef struct \_callee\_saved \_callee\_saved\_t;

80

81/\*

82 \* The macros CONFIG\_{LAZY|EAGER}\_FPU\_SHARING shall be set to indicate that the

83 \* saving/restoring of the traditional x87 floating point (and MMX) registers

84 \* are supported by the kernel's context swapping code. The macro

85 \* CONFIG\_X86\_SSE shall \_also\_ be set if saving/restoring of the XMM

86 \* registers is also supported in the kernel's context swapping code.

87 \*/

88

89#if defined(CONFIG\_EAGER\_FPU\_SHARING) || defined(CONFIG\_LAZY\_FPU\_SHARING)

90

91/\* definition of a single x87 (floating point / MMX) register \*/

92

93typedef struct s\_FpReg {

94 unsigned char reg[10]; /\* 80 bits: ST[0-7] \*/

95} tFpReg;

96

97/\*

98 \* The following is the "normal" floating point register save area, or

99 \* more accurately the save area required by the 'fnsave' and 'frstor'

100 \* instructions. The structure matches the layout described in the

101 \* "Intel(r) 64 and IA-32 Architectures Software Developer's Manual

102 \* Volume 1: Basic Architecture": Protected Mode x87 FPU State Image in

103 \* Memory, 32-Bit Format.

104 \*/

105

106typedef struct [s\_FpRegSet](structs__FpRegSet.md) { /\* # of bytes: name of register \*/

107 unsigned short fcw; /\* 2 : x87 FPU control word \*/

108 unsigned short pad1; /\* 2 : N/A \*/

109 unsigned short fsw; /\* 2 : x87 FPU status word \*/

110 unsigned short pad2; /\* 2 : N/A \*/

111 unsigned short ftw; /\* 2 : x87 FPU tag word \*/

112 unsigned short pad3; /\* 2 : N/A \*/

113 unsigned int fpuip; /\* 4 : x87 FPU instruction pointer offset \*/

114 unsigned short cs; /\* 2 : x87 FPU instruction pointer selector \*/

115 unsigned short fop : 11; /\* 2 : x87 FPU opcode \*/

116 unsigned short pad4 : 5; /\* : 5 bits = 00000 \*/

117 unsigned int fpudp; /\* 4 : x87 FPU instr operand ptr offset \*/

118 unsigned short ds; /\* 2 : x87 FPU instr operand ptr selector \*/

119 unsigned short pad5; /\* 2 : N/A \*/

120 tFpReg fpReg[8]; /\* 80 : ST0 -> ST7 \*/

121} [tFpRegSet](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811) \_\_aligned([FP\_REG\_SET\_ALIGN](arch_2x86_2ia32_2thread_8h.md#af99d45d7fb31caf8f4abf9306fb654a3));

122

123#ifdef CONFIG\_X86\_SSE

124

125/\* definition of a single x87 (floating point / MMX) register \*/

126

127typedef struct s\_FpRegEx {

128 unsigned char reg[10]; /\* 80 bits: ST[0-7] or MM[0-7] \*/

129 unsigned char rsrvd[6]; /\* 48 bits: reserved \*/

130} tFpRegEx;

131

132/\* definition of a single XMM register \*/

133

134typedef struct s\_XmmReg {

135 unsigned char reg[16]; /\* 128 bits: XMM[0-7] \*/

136} tXmmReg;

137

138/\*

139 \* The following is the "extended" floating point register save area, or

140 \* more accurately the save area required by the 'fxsave' and 'fxrstor'

141 \* instructions. The structure matches the layout described in the

142 \* "Intel 64 and IA-32 Architectures Software Developer's Manual

143 \* Volume 2A: Instruction Set Reference, A-M", except for the bytes from offset

144 \* 464 to 511 since these "are available to software use. The processor does

145 \* not write to bytes 464:511 of an FXSAVE area".

146 \*

147 \* This structure must be aligned on a 16 byte boundary when the instructions

148 \* fxsave/fxrstor are used to write/read the data to/from the structure.

149 \*/

150

151typedef struct [s\_FpRegSetEx](structs__FpRegSetEx.md) /\* # of bytes: name of register \*/

152{

153 unsigned short fcw; /\* 2 : x87 FPU control word \*/

154 unsigned short fsw; /\* 2 : x87 FPU status word \*/

155 unsigned char ftw; /\* 1 : x87 FPU abridged tag word \*/

156 unsigned char rsrvd0; /\* 1 : reserved \*/

157 unsigned short fop; /\* 2 : x87 FPU opcode \*/

158 unsigned int fpuip; /\* 4 : x87 FPU instruction pointer offset \*/

159 unsigned short cs; /\* 2 : x87 FPU instruction pointer selector \*/

160 unsigned short rsrvd1; /\* 2 : reserved \*/

161 unsigned int fpudp; /\* 4 : x87 FPU instr operand ptr offset \*/

162 unsigned short ds; /\* 2 : x87 FPU instr operand ptr selector \*/

163 unsigned short rsrvd2; /\* 2 : reserved \*/

164 unsigned int mxcsr; /\* 4 : MXCSR register state \*/

165 unsigned int mxcsrMask; /\* 4 : MXCSR register mask \*/

166 tFpRegEx fpReg[8]; /\* 128 : x87 FPU/MMX registers \*/

167 tXmmReg xmmReg[8]; /\* 128 : XMM registers \*/

168 unsigned char rsrvd3[176]; /\* 176 : reserved \*/

169} [tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967) \_\_aligned([FP\_REG\_SET\_ALIGN](arch_2x86_2ia32_2thread_8h.md#af99d45d7fb31caf8f4abf9306fb654a3));

170

171#else /\* CONFIG\_X86\_SSE == 0 \*/

172

173typedef struct [s\_FpRegSetEx](structs__FpRegSetEx.md) {

174} [tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967);

175

176#endif /\* CONFIG\_X86\_SSE == 0 \*/

177

178#else /\* !CONFIG\_LAZY\_FPU\_SHARING && !CONFIG\_EAGER\_FPU\_SHARING \*/

179

180/\* empty floating point register definition \*/

181

[ 182](structs__FpRegSet.md)typedef struct [s\_FpRegSet](structs__FpRegSet.md) {

[ 183](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811)} [tFpRegSet](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811);

184

[ 185](structs__FpRegSetEx.md)typedef struct [s\_FpRegSetEx](structs__FpRegSetEx.md) {

[ 186](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967)} [tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967);

187

188#endif /\* CONFIG\_LAZY\_FPU\_SHARING || CONFIG\_EAGER\_FPU\_SHARING \*/

189

190/\*

191 \* The following structure defines the set of 'volatile' x87 FPU/MMX/SSE

192 \* registers. These registers need not be preserved by a called C function.

193 \* Given that they are not preserved across function calls, they must be

194 \* save/restored (along with s\_coopFloatReg) when a preemptive context

195 \* switch occurs.

196 \*/

197

[ 198](structs__preempFloatReg.md)typedef struct [s\_preempFloatReg](structs__preempFloatReg.md) {

199 union {

200 /\* threads with K\_FP\_REGS utilize this format \*/

[ 201](structs__preempFloatReg.md#a4acaff08c1a51294d7c45e1144491d86) [tFpRegSet](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811) [fpRegs](structs__preempFloatReg.md#a4acaff08c1a51294d7c45e1144491d86);

202 /\* threads with K\_SSE\_REGS utilize this format \*/

[ 203](structs__preempFloatReg.md#a295615b119006e286338175dcb2d2944) [tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967) [fpRegsEx](structs__preempFloatReg.md#a295615b119006e286338175dcb2d2944);

[ 204](structs__preempFloatReg.md#a0974de9441844c906da4b91278ac1d5f) } [floatRegsUnion](structs__preempFloatReg.md#a0974de9441844c906da4b91278ac1d5f);

[ 205](arch_2x86_2ia32_2thread_8h.md#a559de7a9ab93bd874af8fd66a3851d01)} [tPreempFloatReg](arch_2x86_2ia32_2thread_8h.md#a559de7a9ab93bd874af8fd66a3851d01);

206

207/\*

208 \* The thread control structure definition. It contains the

209 \* various fields to manage a \_single\_ thread. The TCS will be aligned

210 \* to the appropriate architecture specific boundary via the

211 \* arch\_new\_thread() call.

212 \*/

213

214struct \_thread\_arch {

215 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flags;

216

217#ifdef CONFIG\_USERSPACE

218#ifndef CONFIG\_X86\_COMMON\_PAGE\_TABLE

219 /\* Physical address of the page tables used by this thread \*/

220 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) ptables;

221#endif /\* CONFIG\_X86\_COMMON\_PAGE\_TABLE \*/

222

223 /\* Initial privilege mode stack pointer when doing a system call.

224 \* Un-set for supervisor threads.

225 \*/

226 char \*psp;

227#endif

228

229#if defined(CONFIG\_LAZY\_FPU\_SHARING)

230 /\*

231 \* Nested exception count to maintain setting of EXC\_ACTIVE flag across

232 \* outermost exception. EXC\_ACTIVE is used by z\_swap() lazy FP

233 \* save/restore and by debug tools.

234 \*/

235 unsigned excNestCount; /\* nested exception count \*/

236#endif /\* CONFIG\_LAZY\_FPU\_SHARING \*/

237

238 [tPreempFloatReg](arch_2x86_2ia32_2thread_8h.md#a559de7a9ab93bd874af8fd66a3851d01) preempFloatReg; /\* volatile float register storage \*/

239};

240

241typedef struct \_thread\_arch \_thread\_arch\_t;

242

243#endif /\* \_ASMLANGUAGE \*/

244

245#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_IA32\_THREAD\_H\_ \*/

[tPreempFloatReg](arch_2x86_2ia32_2thread_8h.md#a559de7a9ab93bd874af8fd66a3851d01)

struct s\_preempFloatReg tPreempFloatReg

[tFpRegSetEx](arch_2x86_2ia32_2thread_8h.md#a9b38503997978c6dbfdb03448cb38967)

struct s\_FpRegSetEx tFpRegSetEx

[tFpRegSet](arch_2x86_2ia32_2thread_8h.md#ac6b7d0ab9f5986eb129f362e4dc39811)

struct s\_FpRegSet tFpRegSet

[FP\_REG\_SET\_ALIGN](arch_2x86_2ia32_2thread_8h.md#af99d45d7fb31caf8f4abf9306fb654a3)

#define FP\_REG\_SET\_ALIGN

Floating point register set alignment.

**Definition** thread.h:39

[mmustructs.h](mmustructs_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[s\_FpRegSetEx](structs__FpRegSetEx.md)

**Definition** thread.h:185

[s\_FpRegSet](structs__FpRegSet.md)

**Definition** thread.h:182

[s\_preempFloatReg](structs__preempFloatReg.md)

**Definition** thread.h:198

[s\_preempFloatReg::floatRegsUnion](structs__preempFloatReg.md#a0974de9441844c906da4b91278ac1d5f)

union s\_preempFloatReg::@037204035261307060351071062147171372006066315006 floatRegsUnion

[s\_preempFloatReg::fpRegsEx](structs__preempFloatReg.md#a295615b119006e286338175dcb2d2944)

tFpRegSetEx fpRegsEx

**Definition** thread.h:203

[s\_preempFloatReg::fpRegs](structs__preempFloatReg.md#a4acaff08c1a51294d7c45e1144491d86)

tFpRegSet fpRegs

**Definition** thread.h:201

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [ia32](dir_b429dacf948f53b894465a48d17dcb95.md)
- [thread.h](arch_2x86_2ia32_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
