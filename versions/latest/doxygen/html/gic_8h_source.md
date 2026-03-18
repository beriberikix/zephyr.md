---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gic_8h_source.html
original_path: doxygen/html/gic_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gic.h

[Go to the documentation of this file.](gic_8h.md)

1/\*

2 \* Copyright (c) 2019 Stephanos Ioannidis <root@stephanos.io>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GIC\_H\_

17#define ZEPHYR\_INCLUDE\_DRIVERS\_GIC\_H\_

18

19/\*

20 \* GIC Register Interface Base Addresses

21 \*/

22

[ 23](gic_8h.md#adb371115c787d786755ca23eedc6a651)#define GIC\_DIST\_BASE DT\_REG\_ADDR\_BY\_IDX(DT\_INST(0, arm\_gic), 0)

[ 24](gic_8h.md#a855f96fbf6e3c5645d7e4d610eb98664)#define GIC\_CPU\_BASE DT\_REG\_ADDR\_BY\_IDX(DT\_INST(0, arm\_gic), 1)

25

26/\*

27 \* GIC Distributor Interface

28 \*/

29

30/\*

31 \* 0x000 Distributor Control Register

32 \* v1 ICDDCR

33 \* v2/v3 GICD\_CTLR

34 \*/

[ 35](gic_8h.md#a00f17ebce4b31e38e18375340fdf3826)#define GICD\_CTLR (GIC\_DIST\_BASE + 0x0)

36

37/\*

38 \* 0x004 Interrupt Controller Type Register

39 \* v1 ICDICTR

40 \* v2/v3 GICD\_TYPER

41 \*/

[ 42](gic_8h.md#a1b97217a477f13f173ff4a22c0aeeef6)#define GICD\_TYPER (GIC\_DIST\_BASE + 0x4)

43

44/\*

45 \* 0x008 Distributor Implementer Identification Register

46 \* v1 ICDIIDR

47 \* v2/v3 GICD\_IIDR

48 \*/

[ 49](gic_8h.md#a88abd454e14abb10903e32cc83649e07)#define GICD\_IIDR (GIC\_DIST\_BASE + 0x8)

50

51/\*

52 \* 0x080 Interrupt Group Registers

53 \* v1 ICDISRn

54 \* v2/v3 GICD\_IGROUPRn

55 \*/

[ 56](gic_8h.md#a1080fbe96176a41ccf2bd2387ff0db63)#define GICD\_IGROUPRn (GIC\_DIST\_BASE + 0x80)

57

58/\*

59 \* 0x100 Interrupt Set-Enable Registers

60 \* v1 ICDISERn

61 \* v2/v3 GICD\_ISENABLERn

62 \*/

[ 63](gic_8h.md#a310ab6442912860cc32c4728323aa77d)#define GICD\_ISENABLERn (GIC\_DIST\_BASE + 0x100)

64

65/\*

66 \* 0x180 Interrupt Clear-Enable Registers

67 \* v1 ICDICERn

68 \* v2/v3 GICD\_ICENABLERn

69 \*/

[ 70](gic_8h.md#a5c3d3ec71773c06de84fae6e9a4e0a09)#define GICD\_ICENABLERn (GIC\_DIST\_BASE + 0x180)

71

72/\*

73 \* 0x200 Interrupt Set-Pending Registers

74 \* v1 ICDISPRn

75 \* v2/v3 GICD\_ISPENDRn

76 \*/

[ 77](gic_8h.md#a6f6edc1558ef636d46f09b68b7abe025)#define GICD\_ISPENDRn (GIC\_DIST\_BASE + 0x200)

78

79/\*

80 \* 0x280 Interrupt Clear-Pending Registers

81 \* v1 ICDICPRn

82 \* v2/v3 GICD\_ICPENDRn

83 \*/

[ 84](gic_8h.md#aeb43e488b1b2f321aa04973b92f55fde)#define GICD\_ICPENDRn (GIC\_DIST\_BASE + 0x280)

85

86/\*

87 \* 0x300 Interrupt Set-Active Registers

88 \* v1 ICDABRn

89 \* v2/v3 GICD\_ISACTIVERn

90 \*/

[ 91](gic_8h.md#a166410e3d61c7b967df532db8b541bf6)#define GICD\_ISACTIVERn (GIC\_DIST\_BASE + 0x300)

92

93#if CONFIG\_GIC\_VER >= 2

94/\*

95 \* 0x380 Interrupt Clear-Active Registers

96 \* v2/v3 GICD\_ICACTIVERn

97 \*/

98#define GICD\_ICACTIVERn (GIC\_DIST\_BASE + 0x380)

99#endif

100

101/\*

102 \* 0x400 Interrupt Priority Registers

103 \* v1 ICDIPRn

104 \* v2/v3 GICD\_IPRIORITYRn

105 \*/

[ 106](gic_8h.md#ac55442a1b5748b8fcc46a9630ecf1645)#define GICD\_IPRIORITYRn (GIC\_DIST\_BASE + 0x400)

107

108/\*

109 \* 0x800 Interrupt Processor Targets Registers

110 \* v1 ICDIPTRn

111 \* v2/v3 GICD\_ITARGETSRn

112 \*/

[ 113](gic_8h.md#a9b05ed54bb00c209d8774edea5368d5d)#define GICD\_ITARGETSRn (GIC\_DIST\_BASE + 0x800)

114

115/\*

116 \* 0xC00 Interrupt Configuration Registers

117 \* v1 ICDICRn

118 \* v2/v3 GICD\_ICFGRn

119 \*/

[ 120](gic_8h.md#a4683149b0af23adbf4b1c149be5d9fe5)#define GICD\_ICFGRn (GIC\_DIST\_BASE + 0xc00)

121

122/\*

123 \* 0xF00 Software Generated Interrupt Register

124 \* v1 ICDSGIR

125 \* v2/v3 GICD\_SGIR

126 \*/

[ 127](gic_8h.md#a5125b5f77951f0e882e002aac406beec)#define GICD\_SGIR (GIC\_DIST\_BASE + 0xf00)

128

129/\*

130 \* GIC CPU Interface

131 \*/

132

133#if CONFIG\_GIC\_VER <= 2

134

135/\*

136 \* 0x0000 CPU Interface Control Register

137 \* v1 ICCICR

138 \* v2/v3 GICC\_CTLR

139 \*/

[ 140](gic_8h.md#a11871e15a62cbfcc1e54f3dd2ce21e74)#define GICC\_CTLR (GIC\_CPU\_BASE + 0x0)

141

142/\*

143 \* 0x0004 Interrupt Priority Mask Register

144 \* v1 ICCPMR

145 \* v2/v3 GICC\_PMR

146 \*/

[ 147](gic_8h.md#a8d72b8216b091c1d148b5812bc46e7d4)#define GICC\_PMR (GIC\_CPU\_BASE + 0x4)

148

149/\*

150 \* 0x0008 Binary Point Register

151 \* v1 ICCBPR

152 \* v2/v3 GICC\_BPR

153 \*/

[ 154](gic_8h.md#acef579bca73eb22cc132808fcfede353)#define GICC\_BPR (GIC\_CPU\_BASE + 0x8)

155

156/\*

157 \* 0x000C Interrupt Acknowledge Register

158 \* v1 ICCIAR

159 \* v2/v3 GICC\_IAR

160 \*/

[ 161](gic_8h.md#a61672c3cde5301e076793c2ad904cdb9)#define GICC\_IAR (GIC\_CPU\_BASE + 0xc)

162

163/\*

164 \* 0x0010 End of Interrupt Register

165 \* v1 ICCEOIR

166 \* v2/v3 GICC\_EOIR

167 \*/

[ 168](gic_8h.md#af92519fe60b0cf2183a6100bea15dd43)#define GICC\_EOIR (GIC\_CPU\_BASE + 0x10)

169

170

171/\*

172 \* Helper Constants

173 \*/

174

175/\* GICC\_CTLR \*/

[ 176](gic_8h.md#a518810ec411ebf4fb128a86c3e256333)#define GICC\_CTLR\_ENABLEGRP0 BIT(0)

[ 177](gic_8h.md#a692e86e4ede5319e7480a358fe75172b)#define GICC\_CTLR\_ENABLEGRP1 BIT(1)

178

[ 179](gic_8h.md#ad3403f63efc5ce1dc9f257602f2ff0ae)#define GICC\_CTLR\_ENABLE\_MASK (GICC\_CTLR\_ENABLEGRP0 | GICC\_CTLR\_ENABLEGRP1)

180

181#if defined(CONFIG\_GIC\_V2)

182

183#define GICC\_CTLR\_FIQBYPDISGRP0 BIT(5)

184#define GICC\_CTLR\_IRQBYPDISGRP0 BIT(6)

185#define GICC\_CTLR\_FIQBYPDISGRP1 BIT(7)

186#define GICC\_CTLR\_IRQBYPDISGRP1 BIT(8)

187

188#define GICC\_CTLR\_BYPASS\_MASK (GICC\_CTLR\_FIQBYPDISGRP0 | \

189 GICC\_CTLR\_IRQBYPDISGRP1 | \

190 GICC\_CTLR\_FIQBYPDISGRP1 | \

191 GICC\_CTLR\_IRQBYPDISGRP1)

192

193#endif /\* CONFIG\_GIC\_V2 \*/

194

195/\* GICD\_SGIR \*/

[ 196](gic_8h.md#abb0a8279fd1bafe13b5b79ec7aeb3f90)#define GICD\_SGIR\_TGTFILT(x) ((x) << 24)

[ 197](gic_8h.md#a907207ff57799c57a6b84a928738d205)#define GICD\_SGIR\_TGTFILT\_CPULIST GICD\_SGIR\_TGTFILT(0b00)

[ 198](gic_8h.md#a64b98ce10603ac8cb7bb356fa162a344)#define GICD\_SGIR\_TGTFILT\_ALLBUTREQ GICD\_SGIR\_TGTFILT(0b01)

[ 199](gic_8h.md#ae759ef6f311a7279db5e7ccd68c80863)#define GICD\_SGIR\_TGTFILT\_REQONLY GICD\_SGIR\_TGTFILT(0b10)

200

[ 201](gic_8h.md#a4dff39b6ec90ed14dea04fdd25abc1ce)#define GICD\_SGIR\_CPULIST(x) ((x) << 16)

[ 202](gic_8h.md#a124b8c93f6902e9166447dd735f5dc1a)#define GICD\_SGIR\_CPULIST\_CPU(n) GICD\_SGIR\_CPULIST(BIT(n))

[ 203](gic_8h.md#a011479af47f54dfc94330092191aaac5)#define GICD\_SGIR\_CPULIST\_MASK 0xff

204

[ 205](gic_8h.md#a041824e4a8176f8bbbdac5bafe06fae7)#define GICD\_SGIR\_NSATT BIT(15)

206

[ 207](gic_8h.md#ae388207ec492448a22511cee6dcecedc)#define GICD\_SGIR\_SGIINTID(x) (x)

208

209#endif /\* CONFIG\_GIC\_VER <= 2 \*/

210

211

212/\* GICD\_ICFGR \*/

[ 213](gic_8h.md#a44b5b4941c426cd73350eeea005beb8a)#define GICD\_ICFGR\_MASK BIT\_MASK(2)

[ 214](gic_8h.md#a11ed86dd29db285527ff4474958ade81)#define GICD\_ICFGR\_TYPE BIT(1)

215

216/\* GICD\_TYPER.ITLinesNumber 0:4 \*/

[ 217](gic_8h.md#a74cbf9f2c19fb1a09f8936958b02503a)#define GICD\_TYPER\_ITLINESNUM\_MASK 0x1f

218

219/\* GICD\_TYPER.IDbits \*/

[ 220](gic_8h.md#a62397b69dbb93be1a404d14c195cdb2f)#define GICD\_TYPER\_IDBITS(typer) ((((typer) >> 19) & 0x1f) + 1)

221

222/\*

223 \* Common Helper Constants

224 \*/

[ 225](gic_8h.md#a87acbf5e0124561ba231e95cca1bbc7a)#define GIC\_SGI\_INT\_BASE 0

[ 226](gic_8h.md#a63bca268593477e8c0b6bc58aa3ee85c)#define GIC\_PPI\_INT\_BASE 16

227

[ 228](gic_8h.md#a9bb04de2bd1f9d4e304ecdbea6a63a85)#define GIC\_IS\_SGI(intid) (((intid) >= GIC\_SGI\_INT\_BASE) && \

229 ((intid) < GIC\_PPI\_INT\_BASE))

230

231

[ 232](gic_8h.md#ad9e9ba1264c9e57922cc0b8ad2e4dfba)#define GIC\_SPI\_INT\_BASE 32

233

[ 234](gic_8h.md#a1deeb13c2ac681cb120c06b18dee2b91)#define GIC\_SPI\_MAX\_INTID 1019

235

[ 236](gic_8h.md#aa2672b14cfaa1a943bf1633e208ba288)#define GIC\_IS\_SPI(intid) (((intid) >= GIC\_SPI\_INT\_BASE) && \

237 ((intid) <= GIC\_SPI\_MAX\_INTID))

238

[ 239](gic_8h.md#aed0af65dd3212045aeb0906d2d937ad5)#define GIC\_NUM\_INTR\_PER\_REG 32

240

[ 241](gic_8h.md#ad563564c4794a65475474fd8c19f7b41)#define GIC\_NUM\_CFG\_PER\_REG 16

242

[ 243](gic_8h.md#abb00f7fda87b16903a1fbcdd85d660bf)#define GIC\_NUM\_PRI\_PER\_REG 4

244

245/\* GIC idle priority : value '0xff' will allow all interrupts \*/

[ 246](gic_8h.md#ae29667ceb670f4fabfc442350e8d4152)#define GIC\_IDLE\_PRIO 0xff

247

248/\* Priority levels 0:255 \*/

[ 249](gic_8h.md#aaa5afc14eff8f002060b52030783cc47)#define GIC\_PRI\_MASK 0xff

250

251/\*

252 \* '0xa0'is used to initialize each interrupt default priority.

253 \* This is an arbitrary value in current context.

254 \* Any value '0x80' to '0xff' will work for both NS and S state.

255 \* The values of individual interrupt and default has to be chosen

256 \* carefully if PMR and BPR based nesting and preemption has to be done.

257 \*/

[ 258](gic_8h.md#a94e122b157b3e50259581bd1d2f319a1)#define GIC\_INT\_DEF\_PRI\_X4 0xa0a0a0a0

259

260/\* GIC special interrupt id \*/

[ 261](gic_8h.md#a6ac20d04f13472d5dd915197af39aaf3)#define GIC\_INTID\_SPURIOUS 1023

262

263/\* Fixme: update from platform specific define or dt \*/

[ 264](gic_8h.md#a24a62a86eb885f9f47e8bfdc430e8292)#define GIC\_NUM\_CPU\_IF CONFIG\_MP\_MAX\_NUM\_CPUS

265

266#ifndef \_ASMLANGUAGE

267

268#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

269#include <[zephyr/device.h](device_8h.md)>

270

271/\*

272 \* GIC Driver Interface Functions

273 \*/

274

[ 280](gic_8h.md#a585b5b22a16dab6999ab94dae30f4e71)void [arm\_gic\_irq\_enable](gic_8h.md#a585b5b22a16dab6999ab94dae30f4e71)(unsigned int irq);

281

[ 287](gic_8h.md#a3f5ec5c6b16fbac66cd02459d6045742)void [arm\_gic\_irq\_disable](gic_8h.md#a3f5ec5c6b16fbac66cd02459d6045742)(unsigned int irq);

288

[ 295](gic_8h.md#acfa77cdcf46cad1181476bc3b974b58e)bool [arm\_gic\_irq\_is\_enabled](gic_8h.md#acfa77cdcf46cad1181476bc3b974b58e)(unsigned int irq);

296

[ 303](gic_8h.md#ad0cc0929cc6e0336448d45ebd27a45bd)bool [arm\_gic\_irq\_is\_pending](gic_8h.md#ad0cc0929cc6e0336448d45ebd27a45bd)(unsigned int irq);

304

[ 310](gic_8h.md#a2980cdb020c9d8a886bf9d4fd485121b)void [arm\_gic\_irq\_clear\_pending](gic_8h.md#a2980cdb020c9d8a886bf9d4fd485121b)(unsigned int irq);

311

[ 319](gic_8h.md#ad5eb3fc988f7077dc9600e62d768b076)void [arm\_gic\_irq\_set\_priority](gic_8h.md#ad5eb3fc988f7077dc9600e62d768b076)(

320 unsigned int irq, unsigned int prio, unsigned int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

321

[ 327](gic_8h.md#ae545623722c1b45fda2b58155f3fd0ed)unsigned int [arm\_gic\_get\_active](gic_8h.md#ae545623722c1b45fda2b58155f3fd0ed)(void);

328

[ 334](gic_8h.md#a4bfb597ef68cc7f83d86ba52e099e3b4)void [arm\_gic\_eoi](gic_8h.md#a4bfb597ef68cc7f83d86ba52e099e3b4)(unsigned int irq);

335

336#ifdef CONFIG\_SMP

[ 340](gic_8h.md#a3c2d3adf07e2d48bdf863d8142a685aa)void [arm\_gic\_secondary\_init](gic_8h.md#a3c2d3adf07e2d48bdf863d8142a685aa)(void);

341#endif

342

[ 351](gic_8h.md#a08291705f002f01687cf507abbb410dc)void [gic\_raise\_sgi](gic_8h.md#a08291705f002f01687cf507abbb410dc)(unsigned int sgi\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) target\_aff,

352 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) target\_list);

353

354#endif /\* !\_ASMLANGUAGE \*/

355

356#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GIC\_H\_ \*/

[device.h](device_8h.md)

[gic\_raise\_sgi](gic_8h.md#a08291705f002f01687cf507abbb410dc)

void gic\_raise\_sgi(unsigned int sgi\_id, uint64\_t target\_aff, uint16\_t target\_list)

raise SGI to target cores

[arm\_gic\_irq\_clear\_pending](gic_8h.md#a2980cdb020c9d8a886bf9d4fd485121b)

void arm\_gic\_irq\_clear\_pending(unsigned int irq)

Clear the pending irq.

[arm\_gic\_secondary\_init](gic_8h.md#a3c2d3adf07e2d48bdf863d8142a685aa)

void arm\_gic\_secondary\_init(void)

Initialize GIC of secondary cores.

[arm\_gic\_irq\_disable](gic_8h.md#a3f5ec5c6b16fbac66cd02459d6045742)

void arm\_gic\_irq\_disable(unsigned int irq)

Disable interrupt.

[arm\_gic\_eoi](gic_8h.md#a4bfb597ef68cc7f83d86ba52e099e3b4)

void arm\_gic\_eoi(unsigned int irq)

Signal end-of-interrupt.

[arm\_gic\_irq\_enable](gic_8h.md#a585b5b22a16dab6999ab94dae30f4e71)

void arm\_gic\_irq\_enable(unsigned int irq)

Enable interrupt.

[arm\_gic\_irq\_is\_enabled](gic_8h.md#acfa77cdcf46cad1181476bc3b974b58e)

bool arm\_gic\_irq\_is\_enabled(unsigned int irq)

Check if an interrupt is enabled.

[arm\_gic\_irq\_is\_pending](gic_8h.md#ad0cc0929cc6e0336448d45ebd27a45bd)

bool arm\_gic\_irq\_is\_pending(unsigned int irq)

Check if an interrupt is pending.

[arm\_gic\_irq\_set\_priority](gic_8h.md#ad5eb3fc988f7077dc9600e62d768b076)

void arm\_gic\_irq\_set\_priority(unsigned int irq, unsigned int prio, unsigned int flags)

Set interrupt priority.

[arm\_gic\_get\_active](gic_8h.md#ae545623722c1b45fda2b58155f3fd0ed)

unsigned int arm\_gic\_get\_active(void)

Get active interrupt ID.

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gic.h](gic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
