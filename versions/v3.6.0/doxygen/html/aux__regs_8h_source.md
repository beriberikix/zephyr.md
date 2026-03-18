---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/aux__regs_8h_source.html
original_path: doxygen/html/aux__regs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aux\_regs.h

[Go to the documentation of this file.](aux__regs_8h.md)

1/\*

2 \* Copyright (c) 2014 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_AUX\_REGS\_H\_

16#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_AUX\_REGS\_H\_

17

18#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

19

20#define \_ARC\_V2\_LP\_START 0x002

21#define \_ARC\_V2\_LP\_END 0x003

22#define \_ARC\_V2\_IDENTITY 0x004

23#define \_ARC\_V2\_SEC\_STAT 0x09

24#define \_ARC\_V2\_STATUS32 0x00a

25#define \_ARC\_V2\_STATUS32\_P0 0x00b

26#define \_ARC\_V2\_USER\_SP 0x00d

27#define \_ARC\_V2\_AUX\_IRQ\_CTRL 0x00e

28#define \_ARC\_V2\_IC\_IVIC 0x010

29#define \_ARC\_V2\_IC\_CTRL 0x011

30#define \_ARC\_V2\_IC\_LIL 0x013

31#define \_ARC\_V2\_IC\_IVIL 0x019

32#define \_ARC\_V2\_IC\_DATA 0x01d

33#define \_ARC\_V2\_TMR0\_COUNT 0x021

34#define \_ARC\_V2\_TMR0\_CONTROL 0x022

35#define \_ARC\_V2\_TMR0\_LIMIT 0x023

36#define \_ARC\_V2\_IRQ\_VECT\_BASE 0x025

37#define \_ARC\_V2\_IRQ\_VECT\_BASE\_S 0x26

38#define \_ARC\_V2\_KERNEL\_SP 0x38

39#define \_ARC\_V2\_SEC\_U\_SP 0x39

40#define \_ARC\_V2\_SEC\_K\_SP 0x3a

41#define \_ARC\_V2\_AUX\_IRQ\_ACT 0x043

42#define \_ARC\_V2\_DC\_IVDC 0x047

43#define \_ARC\_V2\_DC\_CTRL 0x048

44#define \_ARC\_V2\_DC\_LDL 0x049

45#define \_ARC\_V2\_DC\_IVDL 0x04a

46#define \_ARC\_V2\_DC\_FLSH 0x04b

47#define \_ARC\_V2\_DC\_FLDL 0x04c

48#define \_ARC\_V2\_EA\_BUILD 0x065

49#define \_ARC\_V2\_VECBASE\_AC\_BUILD 0x068

50#define \_ARC\_V2\_FP\_BUILD 0x06b

51#define \_ARC\_V2\_DPFP\_BUILD 0x06c

52#define \_ARC\_V2\_MPU\_BUILD 0x06d

53#define \_ARC\_V2\_RF\_BUILD 0x06e

54#define \_ARC\_V2\_MMU\_BUILD 0x06f

55#define \_ARC\_V2\_VECBASE\_BUILD 0x071

56#define \_ARC\_V2\_D\_CACHE\_BUILD 0x072

57#define \_ARC\_V2\_DCCM\_BUILD 0x074

58#define \_ARC\_V2\_TIMER\_BUILD 0x075

59#define \_ARC\_V2\_AP\_BUILD 0x076

60#define \_ARC\_V2\_I\_CACHE\_BUILD 0x077

61#define \_ARC\_V2\_ICCM\_BUILD 0x078

62#define \_ARC\_V2\_MULTIPLY\_BUILD 0x07b

63#define \_ARC\_V2\_SWAP\_BUILD 0x07c

64#define \_ARC\_V2\_NORM\_BUILD 0x07d

65#define \_ARC\_V2\_MINMAX\_BUILD 0x07e

66#define \_ARC\_V2\_BARREL\_BUILD 0x07f

67#define \_ARC\_V2\_ISA\_CONFIG 0x0c1

68#define \_ARC\_V2\_SEP\_BUILD 0x0c7

69#define \_ARC\_V2\_LPB\_BUILD 0x0e9

70#define \_ARC\_V2\_LPB\_CTRL 0x488

71#define \_ARC\_V2\_IRQ\_BUILD 0x0f3

72#define \_ARC\_V2\_PCT\_BUILD 0x0f5

73#define \_ARC\_V2\_CC\_BUILD 0x0f6

74#define \_ARC\_V2\_TMR1\_COUNT 0x100

75#define \_ARC\_V2\_TMR1\_CONTROL 0x101

76#define \_ARC\_V2\_TMR1\_LIMIT 0x102

77#define \_ARC\_V2\_S\_TMR0\_COUNT 0x106

78#define \_ARC\_V2\_S\_TMR0\_CONTROL 0x107

79#define \_ARC\_V2\_S\_TMR0\_LIMIT 0x108

80#define \_ARC\_V2\_S\_TMR1\_COUNT 0x109

81#define \_ARC\_V2\_S\_TMR1\_CONTROL 0x10a

82#define \_ARC\_V2\_S\_TMR1\_LIMIT 0x10b

83#define \_ARC\_V2\_IRQ\_PRIO\_PEND 0x200

84#define \_ARC\_V2\_AUX\_IRQ\_HINT 0x201

85#define \_ARC\_V2\_IRQ\_PRIORITY 0x206

86#define \_ARC\_V2\_USTACK\_TOP 0x260

87#define \_ARC\_V2\_USTACK\_BASE 0x261

88#define \_ARC\_V2\_S\_USTACK\_TOP 0x262

89#define \_ARC\_V2\_S\_USTACK\_BASE 0x263

90#define \_ARC\_V2\_KSTACK\_TOP 0x264

91#define \_ARC\_V2\_KSTACK\_BASE 0x265

92#define \_ARC\_V2\_S\_KSTACK\_TOP 0x266

93#define \_ARC\_V2\_S\_KSTACK\_BASE 0x267

94#define \_ARC\_V2\_NSC\_TABLE\_TOP 0x268

95#define \_ARC\_V2\_NSC\_TABLE\_BASE 0x269

96#define \_ARC\_V2\_JLI\_BASE 0x290

97#define \_ARC\_V2\_LDI\_BASE 0x291

98#define \_ARC\_V2\_EI\_BASE 0x292

99#define \_ARC\_V2\_ERET 0x400

100#define \_ARC\_V2\_ERSTATUS 0x402

101#define \_ARC\_V2\_ECR 0x403

102#define \_ARC\_V2\_EFA 0x404

103#define \_ARC\_V2\_ERSEC\_STAT 0x406

104#define \_ARC\_V2\_ICAUSE 0x40a

105#define \_ARC\_V2\_IRQ\_SELECT 0x40b

106#define \_ARC\_V2\_IRQ\_ENABLE 0x40c

107#define \_ARC\_V2\_IRQ\_TRIGGER 0x40d

108#define \_ARC\_V2\_IRQ\_STATUS 0x40f

109#define \_ARC\_V2\_IRQ\_PULSE\_CANCEL 0x415

110#define \_ARC\_V2\_IRQ\_PENDING 0x416

111#define \_ARC\_V2\_FPU\_CTRL 0x300

112#define \_ARC\_V2\_FPU\_STATUS 0x301

113#define \_ARC\_V2\_FPU\_DPFP1L 0x302

114#define \_ARC\_V2\_FPU\_DPFP1H 0x303

115#define \_ARC\_V2\_FPU\_DPFP2L 0x304

116#define \_ARC\_V2\_FPU\_DPFP2H 0x305

117#define \_ARC\_V2\_MPU\_EN 0x409

118#define \_ARC\_V2\_MPU\_RDB0 0x422

119#define \_ARC\_V2\_MPU\_RDP0 0x423

120#define \_ARC\_V2\_MPU\_INDEX 0x448

121#define \_ARC\_V2\_MPU\_RSTART 0x449

122#define \_ARC\_V2\_MPU\_REND 0x44A

123#define \_ARC\_V2\_MPU\_RPER 0x44B

124#define \_ARC\_V2\_MPU\_PROBE 0x44C

125#define \_ARC\_V2\_ACC0\_GHI 0x583

126#define \_ARC\_V2\_ACC0\_HI 0x582

127#define \_ARC\_V2\_ACC0\_GLO 0x581

128#define \_ARC\_V2\_ACC0\_LO 0x580

129#define \_ARC\_V2\_DSP\_BUILD 0x7A

130#define \_ARC\_V2\_DSP\_CTRL 0x59f

131#define \_ARC\_V2\_DSP\_BFLY0 0x598

132#define \_ARC\_V2\_DSP\_FFT\_CTRL 0x59e

133#define \_ARC\_V2\_AGU\_BUILD 0xcc

134#define \_ARC\_V2\_AGU\_AP0 0x5c0

135#define \_ARC\_V2\_AGU\_AP1 0x5c1

136#define \_ARC\_V2\_AGU\_AP2 0x5c2

137#define \_ARC\_V2\_AGU\_AP3 0x5c3

138#define \_ARC\_V2\_AGU\_AP4 0x5c4

139#define \_ARC\_V2\_AGU\_AP5 0x5c5

140#define \_ARC\_V2\_AGU\_AP6 0x5c6

141#define \_ARC\_V2\_AGU\_AP7 0x5c7

142#define \_ARC\_V2\_AGU\_AP8 0x5c8

143#define \_ARC\_V2\_AGU\_AP9 0x5c9

144#define \_ARC\_V2\_AGU\_AP10 0x5ca

145#define \_ARC\_V2\_AGU\_AP11 0x5cb

146#define \_ARC\_V2\_AGU\_OS0 0x5d0

147#define \_ARC\_V2\_AGU\_OS1 0x5d1

148#define \_ARC\_V2\_AGU\_OS2 0x5d2

149#define \_ARC\_V2\_AGU\_OS3 0x5d3

150#define \_ARC\_V2\_AGU\_OS4 0x5d4

151#define \_ARC\_V2\_AGU\_OS5 0x5d5

152#define \_ARC\_V2\_AGU\_OS6 0x5d6

153#define \_ARC\_V2\_AGU\_OS7 0x5d7

154#define \_ARC\_V2\_AGU\_MOD0 0x5e0

155#define \_ARC\_V2\_AGU\_MOD1 0x5e1

156#define \_ARC\_V2\_AGU\_MOD2 0x5e2

157#define \_ARC\_V2\_AGU\_MOD3 0x5e3

158#define \_ARC\_V2\_AGU\_MOD4 0x5e4

159#define \_ARC\_V2\_AGU\_MOD5 0x5e5

160#define \_ARC\_V2\_AGU\_MOD6 0x5e6

161#define \_ARC\_V2\_AGU\_MOD7 0x5e7

162#define \_ARC\_V2\_AGU\_MOD8 0x5e8

163#define \_ARC\_V2\_AGU\_MOD9 0x5e9

164#define \_ARC\_V2\_AGU\_MOD10 0x5ea

165#define \_ARC\_V2\_AGU\_MOD11 0x5eb

166#define \_ARC\_V2\_AGU\_MOD12 0x5ec

167#define \_ARC\_V2\_AGU\_MOD13 0x5ed

168#define \_ARC\_V2\_AGU\_MOD14 0x5ee

169#define \_ARC\_V2\_AGU\_MOD15 0x5ef

170#define \_ARC\_V2\_AGU\_MOD16 0x5f0

171#define \_ARC\_V2\_AGU\_MOD17 0x5f1

172#define \_ARC\_V2\_AGU\_MOD18 0x5f2

173#define \_ARC\_V2\_AGU\_MOD19 0x5f3

174#define \_ARC\_V2\_AGU\_MOD20 0x5f4

175#define \_ARC\_V2\_AGU\_MOD21 0x5f5

176#define \_ARC\_V2\_AGU\_MOD22 0x5f6

177#define \_ARC\_V2\_AGU\_MOD23 0x5f7

178#define \_ARC\_HW\_PF\_BUILD 0xf70

179#define \_ARC\_HW\_PF\_CTRL 0x4f

180

181/\* \_ARC\_HW\_PF\_CTRL bits \*/

182#define \_ARC\_HW\_PF\_CTRL\_ENABLE BIT(0)

183

184/\* STATUS32/STATUS32\_P0 bits \*/

185#define \_ARC\_V2\_STATUS32\_H (1 << 0)

186#define Z\_ARC\_V2\_STATUS32\_E(x) ((x) << 1)

187#define \_ARC\_V2\_STATUS32\_AE\_BIT 5

188#define \_ARC\_V2\_STATUS32\_AE (1 << \_ARC\_V2\_STATUS32\_AE\_BIT)

189#define \_ARC\_V2\_STATUS32\_DE (1 << 6)

190#define \_ARC\_V2\_STATUS32\_U\_BIT 7

191#define \_ARC\_V2\_STATUS32\_U (1 << \_ARC\_V2\_STATUS32\_U\_BIT)

192#define \_ARC\_V2\_STATUS32\_V (1 << 8)

193#define \_ARC\_V2\_STATUS32\_C (1 << 9)

194#define \_ARC\_V2\_STATUS32\_N (1 << 10)

195#define \_ARC\_V2\_STATUS32\_Z (1 << 11)

196#define \_ARC\_V2\_STATUS32\_L (1 << 12)

197#define \_ARC\_V2\_STATUS32\_DZ\_BIT 13

198#define \_ARC\_V2\_STATUS32\_DZ (1 << \_ARC\_V2\_STATUS32\_DZ\_BIT)

199#define \_ARC\_V2\_STATUS32\_SC\_BIT 14

200#define \_ARC\_V2\_STATUS32\_SC (1 << \_ARC\_V2\_STATUS32\_SC\_BIT)

201#define \_ARC\_V2\_STATUS32\_ES (1 << 15)

202#define \_ARC\_V2\_STATUS32\_RB(x) ((x) << 16)

203#define \_ARC\_V2\_STATUS32\_AD\_BIT 19

204#define \_ARC\_V2\_STATUS32\_AD (1 << \_ARC\_V2\_STATUS32\_AD\_BIT)

205#define \_ARC\_V2\_STATUS32\_US\_BIT 20

206#define \_ARC\_V2\_STATUS32\_US (1 << \_ARC\_V2\_STATUS32\_US\_BIT)

207#define \_ARC\_V2\_STATUS32\_S\_BIT 21

208#define \_ARC\_V2\_STATUS32\_S (1 << \_ARC\_V2\_STATUS32\_US\_BIT)

209#define \_ARC\_V2\_STATUS32\_IE (1 << 31)

210

211/\* SEC\_STAT bits \*/

212#define \_ARC\_V2\_SEC\_STAT\_SSC\_BIT 0

213#define \_ARC\_V2\_SEC\_STAT\_SSC (1 << \_ARC\_V2\_SEC\_STAT\_SSC\_BIT)

214#define \_ARC\_V2\_SEC\_STAT\_NSRT\_BIT 1

215#define \_ARC\_V2\_SEC\_STAT\_NSRT (1 << \_ARC\_V2\_SEC\_STAT\_NSRT\_BIT)

216#define \_ARC\_V2\_SEC\_STAT\_NSRU\_BIT 2

217#define \_ARC\_V2\_SEC\_STAT\_NSRU (1 << \_ARC\_V2\_SEC\_STAT\_NSRU\_BIT)

218#define \_ARC\_V2\_SEC\_STAT\_IRM\_BIT 3

219#define \_ARC\_V2\_SEC\_STAT\_IRM (1 << \_ARC\_V2\_SEC\_STAT\_IRM\_BIT)

220#define \_ARC\_V2\_SEC\_STAT\_SUE\_BIT 4

221#define \_ARC\_V2\_SEC\_STAT\_SUE (1 << \_ARC\_V2\_SEC\_STAT\_SUE\_BIT)

222#define \_ARC\_V2\_SEC\_STAT\_NIC\_BIT 5

223#define \_ARC\_V2\_SEC\_STAT\_NIC (1 << \_ARC\_V2\_SEC\_STAT\_NIC\_BIT)

224

225/\* interrupt related bits \*/

226#define \_ARC\_V2\_IRQ\_PRIORITY\_SECURE 0x100

227

228/\* exception cause register masks \*/

229#define Z\_ARC\_V2\_ECR\_VECTOR(X) ((X & 0xff0000) >> 16)

230#define Z\_ARC\_V2\_ECR\_CODE(X) ((X & 0xff00) >> 8)

231#define Z\_ARC\_V2\_ECR\_PARAMETER(X) (X & 0xff)

232

233#ifndef \_ASMLANGUAGE

234

235#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

236#if defined(\_\_CCAC\_\_)

237

238#define z\_arc\_v2\_aux\_reg\_read(reg) \_lr((volatile uint32\_t)reg)

239#define z\_arc\_v2\_aux\_reg\_write(reg, val) \

240 \_sr((unsigned int)val, (volatile uint32\_t)reg)

241

242#else /\* ! \_\_CCAC\_\_ \*/

243

244#define z\_arc\_v2\_aux\_reg\_read(reg) \_\_builtin\_arc\_lr((volatile uint32\_t)reg)

245#define z\_arc\_v2\_aux\_reg\_write(reg, val) \

246 \_\_builtin\_arc\_sr((unsigned int)val, (volatile uint32\_t)reg)

247

248#endif /\* \_\_CCAC\_\_ \*/

249#endif /\* \_ASMLANGUAGE \*/

250

251#define z\_arc\_v2\_core\_id() \

252 ({ \

253 unsigned int \_\_ret; \

254 \_\_asm\_\_ \_\_volatile\_\_("lr %0, [%1]\n" \

255 "xbfu %0, %0, 0xe8\n" \

256 : "=r"(\_\_ret) \

257 : "i"(\_ARC\_V2\_IDENTITY)); \

258 \_\_ret; \

259 })

260

261#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_AUX\_REGS\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [aux\_regs.h](aux__regs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
