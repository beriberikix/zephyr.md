---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32__clock__control_8h_source.html
original_path: doxygen/html/stm32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_clock\_control.h

[Go to the documentation of this file.](stm32__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2016 Open-RnD Sp. z o.o.

3 \* Copyright (c) 2016 BayLibre, SAS

4 \* Copyright (c) 2017-2022 Linaro Limited.

5 \* Copyright (c) 2017 RnDity Sp. z o.o.

6 \* Copyright (c) 2023 STMicroelectronics

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_

11#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_

12

13#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

14

15#if defined(CONFIG\_SOC\_SERIES\_STM32C0X)

16#include <[zephyr/dt-bindings/clock/stm32c0\_clock.h](stm32c0__clock_8h.md)>

17#elif defined(CONFIG\_SOC\_SERIES\_STM32F0X)

18#include <[zephyr/dt-bindings/clock/stm32f0\_clock.h](stm32f0__clock_8h.md)>

19#elif defined(CONFIG\_SOC\_SERIES\_STM32F1X)

20#include <[zephyr/dt-bindings/clock/stm32f1\_clock.h](stm32f1__clock_8h.md)>

21#elif defined(CONFIG\_SOC\_SERIES\_STM32F3X)

22#include <[zephyr/dt-bindings/clock/stm32f3\_clock.h](stm32f3__clock_8h.md)>

23#elif defined(CONFIG\_SOC\_SERIES\_STM32F2X) || \

24 defined(CONFIG\_SOC\_SERIES\_STM32F4X)

25#include <[zephyr/dt-bindings/clock/stm32f4\_clock.h](stm32f4__clock_8h.md)>

26#elif defined(CONFIG\_SOC\_SERIES\_STM32F7X)

27#include <[zephyr/dt-bindings/clock/stm32f7\_clock.h](stm32f7__clock_8h.md)>

28#elif defined(CONFIG\_SOC\_SERIES\_STM32G0X)

29#include <[zephyr/dt-bindings/clock/stm32g0\_clock.h](stm32g0__clock_8h.md)>

30#elif defined(CONFIG\_SOC\_SERIES\_STM32G4X)

31#include <[zephyr/dt-bindings/clock/stm32g4\_clock.h](stm32g4__clock_8h.md)>

32#elif defined(CONFIG\_SOC\_SERIES\_STM32L0X)

33#include <[zephyr/dt-bindings/clock/stm32l0\_clock.h](stm32l0__clock_8h.md)>

34#elif defined(CONFIG\_SOC\_SERIES\_STM32L1X)

35#include <[zephyr/dt-bindings/clock/stm32l1\_clock.h](stm32l1__clock_8h.md)>

36#elif defined(CONFIG\_SOC\_SERIES\_STM32L4X) || \

37 defined(CONFIG\_SOC\_SERIES\_STM32L5X)

38#include <[zephyr/dt-bindings/clock/stm32l4\_clock.h](stm32l4__clock_8h.md)>

39#elif defined(CONFIG\_SOC\_SERIES\_STM32WBX)

40#include <[zephyr/dt-bindings/clock/stm32wb\_clock.h](stm32wb__clock_8h.md)>

41#elif defined(CONFIG\_SOC\_SERIES\_STM32WLX)

42#include <[zephyr/dt-bindings/clock/stm32wl\_clock.h](stm32wl__clock_8h.md)>

43#elif defined(CONFIG\_SOC\_SERIES\_STM32H5X)

44#include <[zephyr/dt-bindings/clock/stm32h5\_clock.h](stm32h5__clock_8h.md)>

45#elif defined(CONFIG\_SOC\_SERIES\_STM32H7X)

46#include <[zephyr/dt-bindings/clock/stm32h7\_clock.h](stm32h7__clock_8h.md)>

47#elif defined(CONFIG\_SOC\_SERIES\_STM32U5X)

48#include <[zephyr/dt-bindings/clock/stm32u5\_clock.h](stm32u5__clock_8h.md)>

49#elif defined(CONFIG\_SOC\_SERIES\_STM32WBAX)

50#include <[zephyr/dt-bindings/clock/stm32wba\_clock.h](stm32wba__clock_8h.md)>

51#else

52#include <[zephyr/dt-bindings/clock/stm32\_clock.h](stm32__clock_8h.md)>

53#endif

54

[ 56](stm32__clock__control_8h.md#ad33dc3d92546f9a4162a65a06ac6c673)#define STM32\_CLOCK\_CONTROL\_NODE DT\_NODELABEL(rcc)

57

59

[ 60](stm32__clock__control_8h.md#a38a0117c88924c6e1beca37e6cdea56b)#define STM32\_AHB\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

[ 61](stm32__clock__control_8h.md#a7af7ec37fc9d13d8d3bd6c3193ac8660)#define STM32\_APB1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb1\_prescaler)

[ 62](stm32__clock__control_8h.md#ad82f77d7d85845342bfa613557b1f569)#define STM32\_APB2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb2\_prescaler)

[ 63](stm32__clock__control_8h.md#ad1ffa671b55ad88e624ed9b7c4a22839)#define STM32\_APB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb3\_prescaler)

[ 64](stm32__clock__control_8h.md#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)#define STM32\_APB7\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb7\_prescaler)

[ 65](stm32__clock__control_8h.md#afca170bc72a77d8905b6c2ca0cce9e7b)#define STM32\_AHB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

[ 66](stm32__clock__control_8h.md#a3da9fd6fe11ceb8c2225e43eb2556d2d)#define STM32\_AHB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

[ 67](stm32__clock__control_8h.md#aeb1fabf85560ccd6cc1c0bdb34c86ec2)#define STM32\_AHB5\_PRESCALER DT\_PROP\_OR(DT\_NODELABEL(rcc), ahb5\_prescaler, 1)

[ 68](stm32__clock__control_8h.md#a18dc4749249030d371007b5135f5af54)#define STM32\_CPU1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

[ 69](stm32__clock__control_8h.md#a4f1975635dc6244f98263636c44f3942)#define STM32\_CPU2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu2\_prescaler)

70

71#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

72#define STM32\_CORE\_PRESCALER STM32\_AHB\_PRESCALER

73#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

74#define STM32\_CORE\_PRESCALER STM32\_CPU1\_PRESCALER

75#endif

76

77#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

78#define STM32\_FLASH\_PRESCALER STM32\_AHB3\_PRESCALER

79#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

80#define STM32\_FLASH\_PRESCALER STM32\_AHB4\_PRESCALER

81#else

[ 82](stm32__clock__control_8h.md#ac3274b70aee7aff6282eaa77ca819f27)#define STM32\_FLASH\_PRESCALER STM32\_CORE\_PRESCALER

83#endif

84

[ 85](stm32__clock__control_8h.md#a29ef6b98c22a522cde9f7dab5b11ace0)#define STM32\_ADC\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc\_prescaler)

[ 86](stm32__clock__control_8h.md#a35954cadc11af5ee499918be312acf38)#define STM32\_ADC12\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc12\_prescaler)

[ 87](stm32__clock__control_8h.md#a1cae4646086d8f855b72d55fee1483ad)#define STM32\_ADC34\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc34\_prescaler)

88

[ 90](stm32__clock__control_8h.md#a51967fd4dcf9ec8fe8e7250b5af32c87)#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), d1cpre)

[ 91](stm32__clock__control_8h.md#a035ea0d8259c0f89306c6a7d344705f2)#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

[ 92](stm32__clock__control_8h.md#a844064bd8ccafb5df4bf02748840491d)#define STM32\_D2PPRE1 DT\_PROP(DT\_NODELABEL(rcc), d2ppre1)

[ 93](stm32__clock__control_8h.md#a50394a7e040433c738fc7e9f03b7aff3)#define STM32\_D2PPRE2 DT\_PROP(DT\_NODELABEL(rcc), d2ppre2)

[ 94](stm32__clock__control_8h.md#a02a098a3296751f55ea349faecff7bd5)#define STM32\_D1PPRE DT\_PROP(DT\_NODELABEL(rcc), d1ppre)

[ 95](stm32__clock__control_8h.md#a9dd9b0e8ef84e6ff033a707b2a0ec231)#define STM32\_D3PPRE DT\_PROP(DT\_NODELABEL(rcc), d3ppre)

96

[ 98](stm32__clock__control_8h.md#aea3d7b8e3adedef5f93cdb38852a8097)#define STM32\_AHB5\_DIV DT\_PROP(DT\_NODELABEL(rcc), ahb5\_div)

99

[ 100](stm32__clock__control_8h.md#ad9bff8a9cfbe0dbe0db73d077cb7a227)#define DT\_RCC\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(rcc))

101

102/\* To enable use of IS\_ENABLED utility macro, these symbols

103 \* should not be defined directly using DT\_SAME\_NODE.

104 \*/

105#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(pll))

106#define STM32\_SYSCLK\_SRC\_PLL 1

107#endif

108#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

109#define STM32\_SYSCLK\_SRC\_HSI 1

110#endif

111#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

112#define STM32\_SYSCLK\_SRC\_HSE 1

113#endif

114#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

115#define STM32\_SYSCLK\_SRC\_MSI 1

116#endif

117#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

118#define STM32\_SYSCLK\_SRC\_MSIS 1

119#endif

120#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

121#define STM32\_SYSCLK\_SRC\_CSI 1

122#endif

123

124

126

127#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f2\_pll\_clock, okay) || \

128 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f4\_pll\_clock, okay) || \

129 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f7\_pll\_clock, okay) || \

130 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g0\_pll\_clock, okay) || \

131 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g4\_pll\_clock, okay) || \

132 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l4\_pll\_clock, okay) || \

133 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u5\_pll\_clock, okay) || \

134 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wb\_pll\_clock, okay) || \

135 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wba\_pll\_clock, okay) || \

136 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7\_pll\_clock, okay)

137#define STM32\_PLL\_ENABLED 1

138#define STM32\_PLL\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div\_m)

139#define STM32\_PLL\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul\_n)

140#define STM32\_PLL\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_p)

141#define STM32\_PLL\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_p, 1)

142#define STM32\_PLL\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_q)

143#define STM32\_PLL\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_q, 1)

144#define STM32\_PLL\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_r)

145#define STM32\_PLL\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_r, 1)

146#define STM32\_PLL\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), fracn)

147#define STM32\_PLL\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll), fracn, 1)

148#endif

149

150#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f4\_plli2s\_clock, okay)

151#define STM32\_PLLI2S\_ENABLED 1

152#define STM32\_PLLI2S\_M\_DIVISOR STM32\_PLL\_M\_DIVISOR

153#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

154#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

155#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

156#endif

157

158#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f412\_plli2s\_clock, okay)

159#define STM32\_PLLI2S\_ENABLED 1

160#define STM32\_PLLI2S\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(plli2s), div\_m)

161#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

162#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

163#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

164#endif

165

166#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32u5\_pll\_clock, okay) || \

167 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7\_pll\_clock, okay)

168#define STM32\_PLL2\_ENABLED 1

169#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

170#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

171#define STM32\_PLL2\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_p)

172#define STM32\_PLL2\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_p, 1)

173#define STM32\_PLL2\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_q)

174#define STM32\_PLL2\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_q, 1)

175#define STM32\_PLL2\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_r)

176#define STM32\_PLL2\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_r, 1)

177#define STM32\_PLL2\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), fracn)

178#define STM32\_PLL2\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll2), fracn, 1)

179#endif

180

181#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7\_pll\_clock, okay) || \

182 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32u5\_pll\_clock, okay)

183#define STM32\_PLL3\_ENABLED 1

184#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

185#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

186#define STM32\_PLL3\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_p)

187#define STM32\_PLL3\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_p, 1)

188#define STM32\_PLL3\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_q)

189#define STM32\_PLL3\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_q, 1)

190#define STM32\_PLL3\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_r)

191#define STM32\_PLL3\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_r, 1)

192#define STM32\_PLL3\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), fracn)

193#define STM32\_PLL3\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll3), fracn, 1)

194#endif

195

196#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f1\_pll\_clock, okay)

197#define STM32\_PLL\_ENABLED 1

198#define STM32\_PLL\_XTPRE DT\_PROP(DT\_NODELABEL(pll), xtpre)

199#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

200#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), usbpre)

201#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f0\_pll\_clock, okay) || \

202 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f100\_pll\_clock, okay) || \

203 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f105\_pll\_clock, okay)

204#define STM32\_PLL\_ENABLED 1

205#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

206#define STM32\_PLL\_PREDIV DT\_PROP(DT\_NODELABEL(pll), prediv)

207#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), otgfspre)

208#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l0\_pll\_clock, okay)

209#define STM32\_PLL\_ENABLED 1

210#define STM32\_PLL\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div)

211#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

212#endif

213

214#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32f105\_pll2\_clock, okay)

215#define STM32\_PLL2\_ENABLED 1

216#define STM32\_PLL2\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul)

217#define STM32\_PLL2\_PREDIV DT\_PROP(DT\_NODELABEL(pll2), prediv)

218#endif

219

221#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll), okay) && \

222 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), clocks)

223#define DT\_PLL\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll))

224#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

225#define STM32\_PLL\_SRC\_MSI 1

226#endif

227#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

228#define STM32\_PLL\_SRC\_MSIS 1

229#endif

230#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

231#define STM32\_PLL\_SRC\_HSI 1

232#endif

233#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

234#define STM32\_PLL\_SRC\_CSI 1

235#endif

236#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

237#define STM32\_PLL\_SRC\_HSE 1

238#endif

239#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(pll2))

240#define STM32\_PLL\_SRC\_PLL2 1

241#endif

242

243#endif

244

246#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll2), okay) && \

247 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), clocks)

248#define DT\_PLL2\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll2))

249#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

250#define STM32\_PLL2\_SRC\_MSIS 1

251#endif

252#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

253#define STM32\_PLL2\_SRC\_HSI 1

254#endif

255#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

256#define STM32\_PLL2\_SRC\_HSE 1

257#endif

258

259#endif

260

262#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll3), okay) && \

263 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), clocks)

264#define DT\_PLL3\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll3))

265#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

266#define STM32\_PLL3\_SRC\_MSIS 1

267#endif

268#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

269#define STM32\_PLL3\_SRC\_HSI 1

270#endif

271#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

272#define STM32\_PLL3\_SRC\_HSE 1

273#endif

274

275#endif

276

277

279

280#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), fixed\_clock, okay)

281#define STM32\_LSE\_ENABLED 1

282#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

283#define STM32\_LSE\_DRIVING 0

284#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

285#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), st\_stm32\_lse\_clock, okay)

286#define STM32\_LSE\_ENABLED 1

287#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

288#define STM32\_LSE\_DRIVING DT\_PROP(DT\_NODELABEL(clk\_lse), driving\_capability)

289#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

290#else

[ 291](stm32__clock__control_8h.md#a05b49e91f478558d33b2b862718758fa)#define STM32\_LSE\_ENABLED 0

[ 292](stm32__clock__control_8h.md#aedfe731de4f32e8dacd027bb115ca0e9)#define STM32\_LSE\_FREQ 0

[ 293](stm32__clock__control_8h.md#aead1c5c5ac685af96410f4883f7e988b)#define STM32\_LSE\_DRIVING 0

[ 294](stm32__clock__control_8h.md#a94745d7699b62ef9e7f8bbfbc6803727)#define STM32\_LSE\_BYPASS 0

295#endif

296

297#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay) || \

298 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32l0\_msi\_clock, okay)

299#define STM32\_MSI\_ENABLED 1

300#define STM32\_MSI\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_range)

301#endif

302

303#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay)

304#define STM32\_MSI\_ENABLED 1

305#define STM32\_MSI\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_pll\_mode)

306#endif

307

308#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msis), st\_stm32u5\_msi\_clock, okay)

309#define STM32\_MSIS\_ENABLED 1

310#define STM32\_MSIS\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_range)

311#define STM32\_MSIS\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_pll\_mode)

312#else

[ 313](stm32__clock__control_8h.md#a1a83a4c9a806689ac963e2ea8b142fda)#define STM32\_MSIS\_ENABLED 0

[ 314](stm32__clock__control_8h.md#a0109485d9cfd70782ce6aff604399330)#define STM32\_MSIS\_RANGE 0

[ 315](stm32__clock__control_8h.md#a02f0311b8e9c41a004ed355aff37a7b3)#define STM32\_MSIS\_PLL\_MODE 0

316#endif

317

318#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msik), st\_stm32u5\_msi\_clock, okay)

319#define STM32\_MSIK\_ENABLED 1

320#define STM32\_MSIK\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_range)

321#define STM32\_MSIK\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_pll\_mode)

322#else

[ 323](stm32__clock__control_8h.md#a379e09d2e380483155b0ef8cc39d490b)#define STM32\_MSIK\_ENABLED 0

[ 324](stm32__clock__control_8h.md#a2fb4bc355d7e69e6b676794d0ab4cbba)#define STM32\_MSIK\_RANGE 0

[ 325](stm32__clock__control_8h.md#a67d63326f5ebe1b249eb56b227aecb29)#define STM32\_MSIK\_PLL\_MODE 0

326#endif

327

328#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_csi), fixed\_clock, okay)

329#define STM32\_CSI\_ENABLED 1

330#define STM32\_CSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_csi), clock\_frequency)

331#else

[ 332](stm32__clock__control_8h.md#a2110dbb73ce08ba40555f1d95b50ce5c)#define STM32\_CSI\_FREQ 0

333#endif

334

335#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi), fixed\_clock, okay)

336#define STM32\_LSI\_ENABLED 1

337#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi), clock\_frequency)

338#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi1), fixed\_clock, okay)

339#define STM32\_LSI\_ENABLED 1

340#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi1), clock\_frequency)

341#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi2), fixed\_clock, okay)

342#define STM32\_LSI\_ENABLED 1

343#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi2), clock\_frequency)

344#else

[ 345](stm32__clock__control_8h.md#ae4ad7f2e4844901d753a91c1ba5c58c5)#define STM32\_LSI\_FREQ 0

346#endif

347

348#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), fixed\_clock, okay)

349#define STM32\_HSI\_DIV\_ENABLED 0

350#define STM32\_HSI\_ENABLED 1

351#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

352#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32h7\_hsi\_clock, okay) \

353 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32g0\_hsi\_clock, okay) \

354 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32c0\_hsi\_clock, okay)

355#define STM32\_HSI\_DIV\_ENABLED 1

356#define STM32\_HSI\_ENABLED 1

357#define STM32\_HSI\_DIVISOR DT\_PROP(DT\_NODELABEL(clk\_hsi), hsi\_div)

358#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

359#else

[ 360](stm32__clock__control_8h.md#aa67c0b4d532b58d78b12d36ae6817912)#define STM32\_HSI\_DIV\_ENABLED 0

[ 361](stm32__clock__control_8h.md#a2cc52c346227b2dfb91e1ab5aeda586c)#define STM32\_HSI\_DIVISOR 1

[ 362](stm32__clock__control_8h.md#af906386de1fde7ab0894971723a0a801)#define STM32\_HSI\_FREQ 0

363#endif

364

365#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), fixed\_clock, okay)

366#define STM32\_HSE\_ENABLED 1

367#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

368#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32\_hse\_clock, okay)

369#define STM32\_HSE\_ENABLED 1

370#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

371#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

372#define STM32\_HSE\_CSS DT\_PROP(DT\_NODELABEL(clk\_hse), css\_enabled)

373#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wl\_hse\_clock, okay)

374#define STM32\_HSE\_ENABLED 1

375#define STM32\_HSE\_TCXO DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_tcxo)

376#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

377#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

378#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wba\_hse\_clock, okay)

379#define STM32\_HSE\_ENABLED 1

380#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

381#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

382#else

[ 383](stm32__clock__control_8h.md#a7c3796ef481224c9e2f7516853677ec9)#define STM32\_HSE\_FREQ 0

384#endif

385

386#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), fixed\_clock, okay)

387#define STM32\_HSI48\_ENABLED 1

388#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

389#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), st\_stm32\_hsi48\_clock, okay)

390#define STM32\_HSI48\_ENABLED 1

391#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

392#define STM32\_HSI48\_CRS\_USB\_SOF DT\_PROP(DT\_NODELABEL(clk\_hsi48), crs\_usb\_sof)

393#endif

394

395#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(perck), st\_stm32\_clock\_mux, okay)

396#define STM32\_CKPER\_ENABLED 1

397#endif

398

400

[ 401](structstm32__pclken.md)struct [stm32\_pclken](structstm32__pclken.md) {

[ 402](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e);

[ 403](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf);

404};

405

407

[ 408](stm32__clock__control_8h.md#aa1b0949b4c58d57dcd2e979320cbed0a)#define STM32\_CLOCK\_INFO(clk\_index, node\_id) \

409 { \

410 .enr = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bits), \

411 .bus = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) \

412 }

[ 413](stm32__clock__control_8h.md#a9eb57b349f41edec11ff52a78015aea9)#define STM32\_DT\_CLOCKS(node\_id) \

414 { \

415 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

416 STM32\_CLOCK\_INFO, (,), node\_id) \

417 }

418

[ 419](stm32__clock__control_8h.md#a693176c2c60364d327aa5768ebfac185)#define STM32\_DT\_INST\_CLOCKS(inst) \

420 STM32\_DT\_CLOCKS(DT\_DRV\_INST(inst))

421

[ 422](stm32__clock__control_8h.md#a38559b31633eca5475b73b8a88df1fcd)#define STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT(inst) DT\_INST\_CLOCKS\_HAS\_IDX(inst, 1) ||

[ 423](stm32__clock__control_8h.md#aac932dfd992b11d479edf2a2d5e8de47)#define STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

424 (DT\_INST\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT) 0)

425

[ 426](stm32__clock__control_8h.md#a8743160d8765b466f8ac6a89efaa9dbc)#define STM32\_DOMAIN\_CLOCK\_SUPPORT(id) DT\_CLOCKS\_HAS\_IDX(DT\_NODELABEL(id), 1) ||

[ 427](stm32__clock__control_8h.md#a7951b8025683529eebdd415d6b65688b)#define STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

428 (DT\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_SUPPORT) 0)

429

431

[ 437](stm32__clock__control_8h.md#aaeece46c7eb50e1f095cc33f9f9c3475)#define STM32\_CLOCK\_REG\_GET(clock) \

438 (((clock) >> STM32\_CLOCK\_REG\_SHIFT) & STM32\_CLOCK\_REG\_MASK)

439

[ 445](stm32__clock__control_8h.md#a311bbc17ae04bf6fb648040255ed9af4)#define STM32\_CLOCK\_SHIFT\_GET(clock) \

446 (((clock) >> STM32\_CLOCK\_SHIFT\_SHIFT) & STM32\_CLOCK\_SHIFT\_MASK)

447

[ 453](stm32__clock__control_8h.md#ad3decf332c88ed6dd0f3deb22fdf559e)#define STM32\_CLOCK\_MASK\_GET(clock) \

454 (((clock) >> STM32\_CLOCK\_MASK\_SHIFT) & STM32\_CLOCK\_MASK\_MASK)

455

[ 461](stm32__clock__control_8h.md#ae4e06e6122c64ab7c4ccfadb4957a029)#define STM32\_CLOCK\_VAL\_GET(clock) \

462 (((clock) >> STM32\_CLOCK\_VAL\_SHIFT) & STM32\_CLOCK\_VAL\_MASK)

463

464#if defined(STM32\_HSE\_CSS)

473void stm32\_hse\_css\_callback(void);

474#endif

475

476#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stm32\_clock.h](stm32__clock_8h.md)

[stm32c0\_clock.h](stm32c0__clock_8h.md)

[stm32f0\_clock.h](stm32f0__clock_8h.md)

[stm32f1\_clock.h](stm32f1__clock_8h.md)

[stm32f3\_clock.h](stm32f3__clock_8h.md)

[stm32f4\_clock.h](stm32f4__clock_8h.md)

[stm32f7\_clock.h](stm32f7__clock_8h.md)

[stm32g0\_clock.h](stm32g0__clock_8h.md)

[stm32g4\_clock.h](stm32g4__clock_8h.md)

[stm32h5\_clock.h](stm32h5__clock_8h.md)

[stm32h7\_clock.h](stm32h7__clock_8h.md)

[stm32l0\_clock.h](stm32l0__clock_8h.md)

[stm32l1\_clock.h](stm32l1__clock_8h.md)

[stm32l4\_clock.h](stm32l4__clock_8h.md)

[stm32u5\_clock.h](stm32u5__clock_8h.md)

[stm32wb\_clock.h](stm32wb__clock_8h.md)

[stm32wba\_clock.h](stm32wba__clock_8h.md)

[stm32wl\_clock.h](stm32wl__clock_8h.md)

[stm32\_pclken](structstm32__pclken.md)

Driver structure definition.

**Definition** stm32\_clock\_control.h:401

[stm32\_pclken::bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e)

uint32\_t bus

**Definition** stm32\_clock\_control.h:402

[stm32\_pclken::enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf)

uint32\_t enr

**Definition** stm32\_clock\_control.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [stm32\_clock\_control.h](stm32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
