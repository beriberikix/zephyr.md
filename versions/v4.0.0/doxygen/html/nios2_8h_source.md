---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nios2_8h_source.html
original_path: doxygen/html/nios2_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nios2.h

[Go to the documentation of this file.](nios2_8h.md)

1#ifndef ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_NIOS2\_H\_

2#define ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_NIOS2\_H\_

3

4/\* SPDX-License-Identifier: Xnet \*/

5

6/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

7\* \*

8\* License Agreement \*

9\* \*

10\* Copyright (c) 2008 Altera Corporation, San Jose, California, USA. \*

11\* All rights reserved. \*

12\* \*

13\* Permission is hereby granted, free of charge, to any person obtaining a \*

14\* copy of this software and associated documentation files (the "Software"), \*

15\* to deal in the Software without restriction, including without limitation \*

16\* the rights to use, copy, modify, merge, publish, distribute, sublicense, \*

17\* and/or sell copies of the Software, and to permit persons to whom the \*

18\* Software is furnished to do so, subject to the following conditions: \*

19\* \*

20\* The above copyright notice and this permission notice shall be included in \*

21\* all copies or substantial portions of the Software. \*

22\* \*

23\* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \*

24\* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, \*

25\* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \*

26\* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER \*

27\* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING \*

28\* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER \*

29\* DEALINGS IN THE SOFTWARE. \*

30\* \*

31\* This agreement shall be governed in all respects by the laws of the State \*

32\* of California and by the laws of the United States of America. \*

33\* \*

34\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

35

36/\*

37 \* This header provides processor specific macros for accessing the Nios2

38 \* control registers.

39 \*/

40

41#ifdef \_\_cplusplus

42extern "C"

43{

44#endif /\* \_\_cplusplus \*/

45

46/\*

47 \* Number of available IRQs in internal interrupt controller.

48 \*/

[ 49](nios2_8h.md#abd1039763ffe41f4858f7089cee25e9f)#define NIOS2\_NIRQ 32

50

51/\* Size in bits of registers \*/

[ 52](nios2_8h.md#aa0323188efb3e001c8a3b601fa1bb08e)#define SYSTEM\_BUS\_WIDTH 32

53

54#ifndef \_ASMLANGUAGE

55

56#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

57#include <[zephyr/arch/cpu.h](cpu_8h.md)>

58#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

59

60/\*

61 \* Functions for accessing select Nios II general-purpose registers.

62 \*/

63

64/\* ET (Exception Temporary) register \*/

65static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_nios2\_read\_et(void)

66{

67 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) et;

68

69 \_\_asm\_\_("mov %0, et" : "=r" (et));

70 return et;

71}

72

73static inline void \_nios2\_write\_et([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) et)

74{

75 \_\_asm\_\_ volatile("mov et, %z0" : : "rM" (et));

76}

77

78static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_nios2\_read\_sp(void)

79{

80 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sp;

81

82 \_\_asm\_\_("mov %0, sp" : "=r" (sp));

83 return sp;

84}

85

86/\*

87 \* Functions for useful processor instructions.

88 \*/

89static inline void z\_nios2\_break(void)

90{

91 \_\_asm\_\_ volatile("break");

92}

93

94static inline void \_nios2\_report\_stack\_overflow(void)

95{

96 \_\_asm\_\_ volatile("break 3");

97}

98

99/\*

100 \* Low-level cache management functions

101 \*/

102static inline void \_nios2\_dcache\_addr\_flush(void \*addr)

103{

104 \_\_asm\_\_ volatile ("flushda (%0)" :: "r" (addr));

105}

106

107static inline void z\_nios2\_dcache\_flush([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset)

108{

109 \_\_asm\_\_ volatile ("flushd (%0)" :: "r" (offset));

110}

111

112static inline void z\_nios2\_icache\_flush([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset)

113{

114 \_\_asm\_\_ volatile ("flushi %0" :: "r" (offset));

115}

116

117static inline void z\_nios2\_pipeline\_flush(void)

118{

119 \_\_asm\_\_ volatile ("flushp");

120}

121

122/\*

123 \* Functions for reading/writing control registers

124 \*/

125

[ 126](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2f)enum [nios2\_creg](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2f) {

[ 127](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa8e0fb22c87be14a31c2d3f64efaf8b92) [NIOS2\_CR\_STATUS](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa8e0fb22c87be14a31c2d3f64efaf8b92) = 0,

[ 128](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa0417a233c3bf681454e0c97814dbf32f) [NIOS2\_CR\_ESTATUS](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa0417a233c3bf681454e0c97814dbf32f) = 1,

[ 129](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa527f50f60249c16dcabd132a735b0335) [NIOS2\_CR\_BSTATUS](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa527f50f60249c16dcabd132a735b0335) = 2,

[ 130](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2faeed3b1c7ff5162091c82eec1922be6c5) [NIOS2\_CR\_IENABLE](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2faeed3b1c7ff5162091c82eec1922be6c5) = 3,

[ 131](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa4b6bfeae632d1f5bf221e8ea7ea73e48) [NIOS2\_CR\_IPENDING](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa4b6bfeae632d1f5bf221e8ea7ea73e48) = 4,

[ 132](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fae5a32e84061fe9bbe971bd24c3639b67) [NIOS2\_CR\_CPUID](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fae5a32e84061fe9bbe971bd24c3639b67) = 5,

133 /\* 6 is reserved \*/

[ 134](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fabb628ed2209bf2cb481d26489dd1e204) [NIOS2\_CR\_EXCEPTION](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fabb628ed2209bf2cb481d26489dd1e204) = 7,

[ 135](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2faeb379228ac9ab02fec0a3270406cb1f6) [NIOS2\_CR\_PTEADDR](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2faeb379228ac9ab02fec0a3270406cb1f6) = 8,

[ 136](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa30075c9bffc1d0d668b84004765c3f6c) [NIOS2\_CR\_TLBACC](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa30075c9bffc1d0d668b84004765c3f6c) = 9,

[ 137](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa5a900dc4216e5f7fa49fb5cf55afa944) [NIOS2\_CR\_TLBMISC](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa5a900dc4216e5f7fa49fb5cf55afa944) = 10,

[ 138](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fac80afd710bef0a395759d717015b2fc3) [NIOS2\_CR\_ECCINJ](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fac80afd710bef0a395759d717015b2fc3) = 11,

[ 139](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa52f4b7c8799260803a32ab28bda4114f) [NIOS2\_CR\_BADADDR](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa52f4b7c8799260803a32ab28bda4114f) = 12,

[ 140](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa72cdf2254fb79551473d3d7e3f5f2240) [NIOS2\_CR\_CONFIG](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa72cdf2254fb79551473d3d7e3f5f2240) = 13,

[ 141](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa995dbc36a07c3a237bb1ec24f5834f1c) [NIOS2\_CR\_MPUBASE](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa995dbc36a07c3a237bb1ec24f5834f1c) = 14,

[ 142](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa2009d9955a6be9351fc1f10c2e76f3b9) [NIOS2\_CR\_MPUACC](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa2009d9955a6be9351fc1f10c2e76f3b9) = 15

143};

144

145/\* XXX I would prefer to define these as static inline functions for

146 \* type checking purposes. However if -O0 is used (i.e. CONFIG\_DEBUG is on)

147 \* we get errors "Control register number must be in range 0-31 for

148 \* \_\_builtin\_rdctl" with the following code:

149 \*

150 \* static inline uint32\_t z\_nios2\_creg\_read(enum nios2\_creg reg)

151 \* {

152 \* return \_\_builtin\_rdctl(reg);

153 \* }

154 \*

155 \* This compiles just fine with -Os.

156 \*/

157#define z\_nios2\_creg\_read(reg) \_\_builtin\_rdctl(reg)

158#define z\_nios2\_creg\_write(reg, val) \_\_builtin\_wrctl(reg, val)

159

160#define z\_nios2\_get\_register\_address(base, regnum) \

161 ((void \*)(((uint8\_t \*)base) + ((regnum) \* (SYSTEM\_BUS\_WIDTH / 8))))

162

163static inline void \_nios2\_reg\_write(void \*base, int regnum, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

164{

165 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(data,

166 ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0))z\_nios2\_get\_register\_address(base, regnum));

167}

168

169static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_nios2\_reg\_read(void \*base, int regnum)

170{

171 return [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0))z\_nios2\_get\_register\_address(base, regnum));

172}

173

174#endif /\* \_ASMLANGUAGE \*/

175

176/\*

177 \* Nios II control registers that are always present

178 \*/

[ 179](nios2_8h.md#ad34427532598ae3ebfa7d23d3b17b608)#define NIOS2\_STATUS status

[ 180](nios2_8h.md#a7d034056f9e1737521bfb86e1bc4f0ab)#define NIOS2\_ESTATUS estatus

[ 181](nios2_8h.md#a72ca6b7521fd2cf19726fa51f3346c36)#define NIOS2\_BSTATUS bstatus

[ 182](nios2_8h.md#ace4053c902157cae6da788ad0f822e35)#define NIOS2\_IENABLE ienable

[ 183](nios2_8h.md#a531b545c2314222d0cd5cf83e3df451c)#define NIOS2\_IPENDING ipending

[ 184](nios2_8h.md#a7908bed7102290cfa768b95539b6125f)#define NIOS2\_CPUID cpuid

185

186/\*

187 \* Bit masks & offsets for Nios II control registers.

188 \* The presence and size of a field is sometimes dependent on the Nios II

189 \* configuration. Bit masks for every possible field and the maximum size of

190 \* that field are defined.

191 \*

192 \* All bit-masks are expressed relative to the position

193 \* of the data with a register. To read data that is LSB-

194 \* aligned, the register read data should be masked, then

195 \* right-shifted by the designated "OFST" macro value. The

196 \* opposite should be used for register writes when starting

197 \* with LSB-aligned data.

198 \*/

199

200/\* STATUS, ESTATUS, BSTATUS, and SSTATUS registers \*/

[ 201](nios2_8h.md#ab72a90fc3af428ec4aeabaecd009be0e)#define NIOS2\_STATUS\_PIE\_MSK (0x00000001)

[ 202](nios2_8h.md#a802439d6552d752804a47e843ea03b62)#define NIOS2\_STATUS\_PIE\_OFST (0)

[ 203](nios2_8h.md#a8b4290b0e9594bcbaf2dd399f37303f8)#define NIOS2\_STATUS\_U\_MSK (0x00000002)

[ 204](nios2_8h.md#a7bea56bb0028e97c89d03a424372e0a7)#define NIOS2\_STATUS\_U\_OFST (1)

[ 205](nios2_8h.md#a64888be8f301859fc55000100d8b262c)#define NIOS2\_STATUS\_EH\_MSK (0x00000004)

[ 206](nios2_8h.md#acb2607282fef918f3617104e8265c6bf)#define NIOS2\_STATUS\_EH\_OFST (2)

[ 207](nios2_8h.md#a9cffcdafe76226a1ead22925e42eb2a1)#define NIOS2\_STATUS\_IH\_MSK (0x00000008)

[ 208](nios2_8h.md#a377f98e7303a4f6a206337b46bcf4f7b)#define NIOS2\_STATUS\_IH\_OFST (3)

[ 209](nios2_8h.md#ae7b58cda92c4f6f6c83a9e2daeffdfdf)#define NIOS2\_STATUS\_IL\_MSK (0x000003f0)

[ 210](nios2_8h.md#ad084220bf77c1d9d039851729cc30df3)#define NIOS2\_STATUS\_IL\_OFST (4)

[ 211](nios2_8h.md#adb909a5a4a6624d47ecc4fcb1099d1a9)#define NIOS2\_STATUS\_CRS\_MSK (0x0000fc00)

[ 212](nios2_8h.md#a8ffd44e86e548dc548c6768f29d198b1)#define NIOS2\_STATUS\_CRS\_OFST (10)

[ 213](nios2_8h.md#a50383173c2fe598509f261ff1ba62c3c)#define NIOS2\_STATUS\_PRS\_MSK (0x003f0000)

[ 214](nios2_8h.md#a5d847db40d631480824d77a1909434bc)#define NIOS2\_STATUS\_PRS\_OFST (16)

[ 215](nios2_8h.md#a6152da1c59926c2740dcb9fbdfd3e96c)#define NIOS2\_STATUS\_NMI\_MSK (0x00400000)

[ 216](nios2_8h.md#a53e628ac5b14ac1bd602d12537915d9c)#define NIOS2\_STATUS\_NMI\_OFST (22)

[ 217](nios2_8h.md#aa65e3c7cd868e0409f30b4efb3293339)#define NIOS2\_STATUS\_RSIE\_MSK (0x00800000)

[ 218](nios2_8h.md#a643fb9a1fe3b029060a1c4f7882d248c)#define NIOS2\_STATUS\_RSIE\_OFST (23)

[ 219](nios2_8h.md#a5bc9644ac75f8d2f5d1527b472fa0267)#define NIOS2\_STATUS\_SRS\_MSK (0x80000000)

[ 220](nios2_8h.md#a24b97dd63c602153a21059a16f151049)#define NIOS2\_STATUS\_SRS\_OFST (31)

221

222/\* EXCEPTION register \*/

[ 223](nios2_8h.md#aa3e05815adb290916e9f699af8c9cc11)#define NIOS2\_EXCEPTION\_REG\_CAUSE\_MASK (0x0000007c)

[ 224](nios2_8h.md#a56440808e259123a40ee625b56935ff6)#define NIOS2\_EXCEPTION\_REG\_CAUSE\_OFST (2)

[ 225](nios2_8h.md#af92a59cccea64fe57ac9f31472b505c2)#define NIOS2\_EXCEPTION\_REG\_ECCFTL\_MASK (0x80000000)

[ 226](nios2_8h.md#a3e139dfdf9769941b7cdc7532adb16b6)#define NIOS2\_EXCEPTION\_REG\_ECCFTL\_OFST (31)

227

228/\* PTEADDR (Page Table Entry Address) register \*/

[ 229](nios2_8h.md#a7951dcf273cf91c0ff273439c0e9bc46)#define NIOS2\_PTEADDR\_REG\_VPN\_OFST 2

[ 230](nios2_8h.md#a473e4f978c7ae3de98ebe43ea7307e4c)#define NIOS2\_PTEADDR\_REG\_VPN\_MASK 0x3ffffc

[ 231](nios2_8h.md#ab58258e4324fae75fc4cf820f9749450)#define NIOS2\_PTEADDR\_REG\_PTBASE\_OFST 22

[ 232](nios2_8h.md#a5b3660b428fd05bc7c1fb3c79bd46ca8)#define NIOS2\_PTEADDR\_REG\_PTBASE\_MASK 0xffc00000

233

234/\* TLBACC (TLB Access) register \*/

[ 235](nios2_8h.md#aa2626f669c60df1ecb656b39790847d1)#define NIOS2\_TLBACC\_REG\_PFN\_OFST 0

[ 236](nios2_8h.md#a618dbc07c36700ac72bcf71ec2c9e472)#define NIOS2\_TLBACC\_REG\_PFN\_MASK 0xfffff

[ 237](nios2_8h.md#a7d2cbd8522d1f327751def5fe969a0d5)#define NIOS2\_TLBACC\_REG\_G\_OFST 20

[ 238](nios2_8h.md#a59243aa4438becd0aa22f9d022861cbb)#define NIOS2\_TLBACC\_REG\_G\_MASK 0x100000

[ 239](nios2_8h.md#aed7fc5ea18365cdcc92c4414bd037d69)#define NIOS2\_TLBACC\_REG\_X\_OFST 21

[ 240](nios2_8h.md#ac0cfd0ae9e54cf7f7d54a803fdf71faa)#define NIOS2\_TLBACC\_REG\_X\_MASK 0x200000

[ 241](nios2_8h.md#a1d3410fc7a0bc76840af4246331b236d)#define NIOS2\_TLBACC\_REG\_W\_OFST 22

[ 242](nios2_8h.md#a26dc8b860a460dadc26e209711ac17de)#define NIOS2\_TLBACC\_REG\_W\_MASK 0x400000

[ 243](nios2_8h.md#a57105c85d09fe71a6377cac532cbdcf8)#define NIOS2\_TLBACC\_REG\_R\_OFST 23

[ 244](nios2_8h.md#a423c56dc6145ad454db34fe3cff783bd)#define NIOS2\_TLBACC\_REG\_R\_MASK 0x800000

[ 245](nios2_8h.md#a8209191a81108ad3b1e559b5e7306338)#define NIOS2\_TLBACC\_REG\_C\_OFST 24

[ 246](nios2_8h.md#a0265f8c890ac3241e45c9e56d53c0b97)#define NIOS2\_TLBACC\_REG\_C\_MASK 0x1000000

[ 247](nios2_8h.md#acbae5d01bfdd37c7a6c7ac6ca2481150)#define NIOS2\_TLBACC\_REG\_IG\_OFST 25

[ 248](nios2_8h.md#abd7e700149da6c2050c7ba53707548c6)#define NIOS2\_TLBACC\_REG\_IG\_MASK 0xfe000000

249

250/\* TLBMISC (TLB Miscellaneous) register \*/

[ 251](nios2_8h.md#a72a4d1d3ac512d48b6500da227b76cd0)#define NIOS2\_TLBMISC\_REG\_D\_OFST 0

[ 252](nios2_8h.md#a8b926d1b8892800379a644fef17ff4bb)#define NIOS2\_TLBMISC\_REG\_D\_MASK 0x1

[ 253](nios2_8h.md#a9f585c28956fda2e6dc63736e6bee3f1)#define NIOS2\_TLBMISC\_REG\_PERM\_OFST 1

[ 254](nios2_8h.md#a4a58e8570b24ecb7b71b8702d8c1317f)#define NIOS2\_TLBMISC\_REG\_PERM\_MASK 0x2

[ 255](nios2_8h.md#ac1ed4797945f0d4f0389ee6dc19b3204)#define NIOS2\_TLBMISC\_REG\_BAD\_OFST 2

[ 256](nios2_8h.md#a09fca40b1c134863ffa5844b31dc2650)#define NIOS2\_TLBMISC\_REG\_BAD\_MASK 0x4

[ 257](nios2_8h.md#a42aa5b5cd42993c02ba9f389324c3f1d)#define NIOS2\_TLBMISC\_REG\_DBL\_OFST 3

[ 258](nios2_8h.md#a82864e33892d9a6e78128b8ff360111c)#define NIOS2\_TLBMISC\_REG\_DBL\_MASK 0x8

[ 259](nios2_8h.md#ad5993cca0d86a22a70b7f3c601cdb2d9)#define NIOS2\_TLBMISC\_REG\_PID\_OFST 4

[ 260](nios2_8h.md#a7d222030def1685e9b138e4ea6728f5f)#define NIOS2\_TLBMISC\_REG\_PID\_MASK 0x3fff0

[ 261](nios2_8h.md#aa0d37e372460c06c388e7aa8abc9139d)#define NIOS2\_TLBMISC\_REG\_WE\_OFST 18

[ 262](nios2_8h.md#ae826f4ca026ae8e7a40de7111fca8bd3)#define NIOS2\_TLBMISC\_REG\_WE\_MASK 0x40000

[ 263](nios2_8h.md#a4220564107aa0292cc8a5d6278265a0f)#define NIOS2\_TLBMISC\_REG\_RD\_OFST 19

[ 264](nios2_8h.md#a28ef7da32e52d2e6a612a0401293bdaa)#define NIOS2\_TLBMISC\_REG\_RD\_MASK 0x80000

[ 265](nios2_8h.md#a2a25ef0819415b9aad86533c2f0652d3)#define NIOS2\_TLBMISC\_REG\_WAY\_OFST 20

[ 266](nios2_8h.md#a2cde4fb21fc83dba1302f4a30bdc6285)#define NIOS2\_TLBMISC\_REG\_WAY\_MASK 0xf00000

[ 267](nios2_8h.md#a6540f242a1ea685971a2c56e12c70c90)#define NIOS2\_TLBMISC\_REG\_EE\_OFST 24

[ 268](nios2_8h.md#ac44e54325b10fd9f19228e99b918544e)#define NIOS2\_TLBMISC\_REG\_EE\_MASK 0x1000000

269

270/\* ECCINJ (ECC Inject) register \*/

[ 271](nios2_8h.md#a3d6ff301573c5c32d4757d5c9c7c1c4c)#define NIOS2\_ECCINJ\_REG\_RF\_OFST 0

[ 272](nios2_8h.md#aa552377c26a733ee06cdfe4d29629d0c)#define NIOS2\_ECCINJ\_REG\_RF\_MASK 0x3

[ 273](nios2_8h.md#aec97f89cb19b0a19362e388fa2109e49)#define NIOS2\_ECCINJ\_REG\_ICTAG\_OFST 2

[ 274](nios2_8h.md#a3e74b0836d561ba277e36e5c553c63ec)#define NIOS2\_ECCINJ\_REG\_ICTAG\_MASK 0xc

[ 275](nios2_8h.md#a3ad741eb57d73fec34f186cc2fca501f)#define NIOS2\_ECCINJ\_REG\_ICDAT\_OFST 4

[ 276](nios2_8h.md#a302b3dd0abfd5101f2c1553a0042e183)#define NIOS2\_ECCINJ\_REG\_ICDAT\_MASK 0x30

[ 277](nios2_8h.md#aa311766055005a3ae3413313c2c09f03)#define NIOS2\_ECCINJ\_REG\_DCTAG\_OFST 6

[ 278](nios2_8h.md#a9eae44ac92ed480ca14544185b5b4bb7)#define NIOS2\_ECCINJ\_REG\_DCTAG\_MASK 0xc0

[ 279](nios2_8h.md#a5a21fbe075b71529d9449f7be4c2a03d)#define NIOS2\_ECCINJ\_REG\_DCDAT\_OFST 8

[ 280](nios2_8h.md#a96ec304e617f5493262ddbcee81ee974)#define NIOS2\_ECCINJ\_REG\_DCDAT\_MASK 0x300

[ 281](nios2_8h.md#a57d39dfc531b4ab6142d8069c071bcda)#define NIOS2\_ECCINJ\_REG\_TLB\_OFST 10

[ 282](nios2_8h.md#ae33e5765611a8913dce76cb3812b0ba1)#define NIOS2\_ECCINJ\_REG\_TLB\_MASK 0xc00

[ 283](nios2_8h.md#ae5a07059d27510eb67f030591c4ed972)#define NIOS2\_ECCINJ\_REG\_DTCM0\_OFST 12

[ 284](nios2_8h.md#a6b04faeba914f397cf08709e40e01405)#define NIOS2\_ECCINJ\_REG\_DTCM0\_MASK 0x3000

[ 285](nios2_8h.md#a2dbd1ef78197bff459745fc5979c6f94)#define NIOS2\_ECCINJ\_REG\_DTCM1\_OFST 14

[ 286](nios2_8h.md#a853512204d550f915d04858dc3f4bebf)#define NIOS2\_ECCINJ\_REG\_DTCM1\_MASK 0xc000

[ 287](nios2_8h.md#aa2175b16f4045fb8911ad53bea651d7a)#define NIOS2\_ECCINJ\_REG\_DTCM2\_OFST 16

[ 288](nios2_8h.md#a73bd69e433a866f0e12efd72ce1c56d3)#define NIOS2\_ECCINJ\_REG\_DTCM2\_MASK 0x30000

[ 289](nios2_8h.md#abc8e7cc4ae8223b33616c5dee424e149)#define NIOS2\_ECCINJ\_REG\_DTCM3\_OFST 18

[ 290](nios2_8h.md#a304454b8f0792f85a95a7972e20040f2)#define NIOS2\_ECCINJ\_REG\_DTCM3\_MASK 0xc0000

291

292/\* CONFIG register \*/

[ 293](nios2_8h.md#a631239a3b9b48af3970d3a8efc116e2d)#define NIOS2\_CONFIG\_REG\_PE\_MASK (0x00000001)

[ 294](nios2_8h.md#a1eaee9129af2e1b54bab839400f029fd)#define NIOS2\_CONFIG\_REG\_PE\_OFST (0)

[ 295](nios2_8h.md#abaad2f10821ddd584d451648103eeaaa)#define NIOS2\_CONFIG\_REG\_ANI\_MASK (0x00000002)

[ 296](nios2_8h.md#a2015a0e32c6f6a0e9ea20c088c07a9c8)#define NIOS2\_CONFIG\_REG\_ANI\_OFST (1)

[ 297](nios2_8h.md#a70b4a9c7154bc9db7eca3b7fee101274)#define NIOS2\_CONFIG\_REG\_ECCEN\_MASK (0x00000004)

[ 298](nios2_8h.md#a37b273e6347f687c09345e20b3a0bcca)#define NIOS2\_CONFIG\_REG\_ECCEN\_OFST (2)

[ 299](nios2_8h.md#a3f37846c7a3285733875d98e527c8737)#define NIOS2\_CONFIG\_REG\_ECCEXC\_MASK (0x00000008)

[ 300](nios2_8h.md#a3997b20b47cd6120b5c2a813008030ef)#define NIOS2\_CONFIG\_REG\_ECCEXC\_OFST (3)

301

302/\* MPUBASE (MPU Base Address) Register \*/

[ 303](nios2_8h.md#a0cc7dd3fc32c21c67ae115c5c84e14fa)#define NIOS2\_MPUBASE\_D\_MASK (0x00000001)

[ 304](nios2_8h.md#a9ec3f5a0c0f778017a3013ef1094c910)#define NIOS2\_MPUBASE\_D\_OFST (0)

[ 305](nios2_8h.md#a6b1e1e8fc7a0d87eef65d760664002aa)#define NIOS2\_MPUBASE\_INDEX\_MASK (0x0000003e)

[ 306](nios2_8h.md#a46a88b78e0e8fc790984976f806b677d)#define NIOS2\_MPUBASE\_INDEX\_OFST (1)

[ 307](nios2_8h.md#acd0cc782bd29cac75c4bd0f30407e3e7)#define NIOS2\_MPUBASE\_BASE\_ADDR\_MASK (0xffffffc0)

[ 308](nios2_8h.md#a6e6758f1584275c132bc897aa9fbc140)#define NIOS2\_MPUBASE\_BASE\_ADDR\_OFST (6)

309

310/\* MPUACC (MPU Access) Register \*/

[ 311](nios2_8h.md#a40b536937f0ebf231d08b1e1b8348cc2)#define NIOS2\_MPUACC\_LIMIT\_MASK (0xffffffc0)

[ 312](nios2_8h.md#a5bd84a46c3b6bb33f66e4f0a44d1823c)#define NIOS2\_MPUACC\_LIMIT\_OFST (6)

[ 313](nios2_8h.md#ae81675d911ca2c34da95b24f7158c4e0)#define NIOS2\_MPUACC\_MASK\_MASK (0xffffffc0)

[ 314](nios2_8h.md#a1d4be3f49cdaef1f58e88a8a5c854fc7)#define NIOS2\_MPUACC\_MASK\_OFST (6)

[ 315](nios2_8h.md#aa22a5a4fe42cb02a6ec97c90665472d1)#define NIOS2\_MPUACC\_C\_MASK (0x00000020)

[ 316](nios2_8h.md#a878e4e5d4a30f0ffa1a13412ac3d632c)#define NIOS2\_MPUACC\_C\_OFST (5)

[ 317](nios2_8h.md#a5d9ba76e47ae29b02fa6d4dfe54a4826)#define NIOS2\_MPUACC\_PERM\_MASK (0x0000001c)

[ 318](nios2_8h.md#a36e8385c8c83bc5a25a2a07746bb9f1b)#define NIOS2\_MPUACC\_PERM\_OFST (2)

[ 319](nios2_8h.md#a24c0c5678a5a7ba9caabcb19ca6acfc0)#define NIOS2\_MPUACC\_RD\_MASK (0x00000002)

[ 320](nios2_8h.md#a066005379b28b72b5b38227b0e55e693)#define NIOS2\_MPUACC\_RD\_OFST (1)

[ 321](nios2_8h.md#a7b26c566bb8094eaefe661b504164dce)#define NIOS2\_MPUACC\_WR\_MASK (0x00000001)

[ 322](nios2_8h.md#a4c849d299cc5c64ae4c92925e1a2e370)#define NIOS2\_MPUACC\_WR\_OFST (0)

323

324#ifdef \_\_cplusplus

325}

326#endif /\* \_\_cplusplus \*/

327

328#endif /\* ZEPHYR\_INCLUDE\_ARCH\_NIOS2\_NIOS2\_H\_ \*/

[cpu.h](cpu_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[nios2\_creg](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2f)

nios2\_creg

**Definition** nios2.h:126

[NIOS2\_CR\_ESTATUS](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa0417a233c3bf681454e0c97814dbf32f)

@ NIOS2\_CR\_ESTATUS

**Definition** nios2.h:128

[NIOS2\_CR\_MPUACC](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa2009d9955a6be9351fc1f10c2e76f3b9)

@ NIOS2\_CR\_MPUACC

**Definition** nios2.h:142

[NIOS2\_CR\_TLBACC](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa30075c9bffc1d0d668b84004765c3f6c)

@ NIOS2\_CR\_TLBACC

**Definition** nios2.h:136

[NIOS2\_CR\_IPENDING](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa4b6bfeae632d1f5bf221e8ea7ea73e48)

@ NIOS2\_CR\_IPENDING

**Definition** nios2.h:131

[NIOS2\_CR\_BSTATUS](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa527f50f60249c16dcabd132a735b0335)

@ NIOS2\_CR\_BSTATUS

**Definition** nios2.h:129

[NIOS2\_CR\_BADADDR](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa52f4b7c8799260803a32ab28bda4114f)

@ NIOS2\_CR\_BADADDR

**Definition** nios2.h:139

[NIOS2\_CR\_TLBMISC](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa5a900dc4216e5f7fa49fb5cf55afa944)

@ NIOS2\_CR\_TLBMISC

**Definition** nios2.h:137

[NIOS2\_CR\_CONFIG](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa72cdf2254fb79551473d3d7e3f5f2240)

@ NIOS2\_CR\_CONFIG

**Definition** nios2.h:140

[NIOS2\_CR\_STATUS](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa8e0fb22c87be14a31c2d3f64efaf8b92)

@ NIOS2\_CR\_STATUS

**Definition** nios2.h:127

[NIOS2\_CR\_MPUBASE](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fa995dbc36a07c3a237bb1ec24f5834f1c)

@ NIOS2\_CR\_MPUBASE

**Definition** nios2.h:141

[NIOS2\_CR\_EXCEPTION](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fabb628ed2209bf2cb481d26489dd1e204)

@ NIOS2\_CR\_EXCEPTION

**Definition** nios2.h:134

[NIOS2\_CR\_ECCINJ](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fac80afd710bef0a395759d717015b2fc3)

@ NIOS2\_CR\_ECCINJ

**Definition** nios2.h:138

[NIOS2\_CR\_CPUID](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2fae5a32e84061fe9bbe971bd24c3639b67)

@ NIOS2\_CR\_CPUID

**Definition** nios2.h:132

[NIOS2\_CR\_PTEADDR](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2faeb379228ac9ab02fec0a3270406cb1f6)

@ NIOS2\_CR\_PTEADDR

**Definition** nios2.h:135

[NIOS2\_CR\_IENABLE](nios2_8h.md#a1e2bfd6bfafde4459019e76f73aecd2faeed3b1c7ff5162091c82eec1922be6c5)

@ NIOS2\_CR\_IENABLE

**Definition** nios2.h:130

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:70

[sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)

static ALWAYS\_INLINE uint32\_t sys\_read32(mem\_addr\_t addr)

**Definition** sys-io-common.h:59

[sys\_io.h](sys_2sys__io_8h.md)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [nios2.h](nios2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
