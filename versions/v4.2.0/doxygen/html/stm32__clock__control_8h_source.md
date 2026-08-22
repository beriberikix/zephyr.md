---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stm32__clock__control_8h_source.html
original_path: doxygen/html/stm32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

20#if defined(CONFIG\_SOC\_STM32F10X\_CONNECTIVITY\_LINE\_DEVICE)

21#include <[zephyr/dt-bindings/clock/stm32f10x\_clock.h](stm32f10x__clock_8h.md)>

22#else

23#include <[zephyr/dt-bindings/clock/stm32f1\_clock.h](stm32f1__clock_8h.md)>

24#endif

25#elif defined(CONFIG\_SOC\_SERIES\_STM32F3X)

26#include <[zephyr/dt-bindings/clock/stm32f3\_clock.h](stm32f3__clock_8h.md)>

27#elif defined(CONFIG\_SOC\_SERIES\_STM32F2X) || \

28 defined(CONFIG\_SOC\_SERIES\_STM32F4X)

29#include <[zephyr/dt-bindings/clock/stm32f4\_clock.h](stm32f4__clock_8h.md)>

30#include <[zephyr/dt-bindings/clock/stm32f410\_clock.h](stm32f410__clock_8h.md)>

31#elif defined(CONFIG\_SOC\_SERIES\_STM32F7X)

32#include <[zephyr/dt-bindings/clock/stm32f7\_clock.h](stm32f7__clock_8h.md)>

33#elif defined(CONFIG\_SOC\_SERIES\_STM32G0X)

34#include <[zephyr/dt-bindings/clock/stm32g0\_clock.h](stm32g0__clock_8h.md)>

35#elif defined(CONFIG\_SOC\_SERIES\_STM32G4X)

36#include <[zephyr/dt-bindings/clock/stm32g4\_clock.h](stm32g4__clock_8h.md)>

37#elif defined(CONFIG\_SOC\_SERIES\_STM32L0X)

38#include <[zephyr/dt-bindings/clock/stm32l0\_clock.h](stm32l0__clock_8h.md)>

39#elif defined(CONFIG\_SOC\_SERIES\_STM32L1X)

40#include <[zephyr/dt-bindings/clock/stm32l1\_clock.h](stm32l1__clock_8h.md)>

41#elif defined(CONFIG\_SOC\_SERIES\_STM32L4X) || \

42 defined(CONFIG\_SOC\_SERIES\_STM32L5X)

43#include <[zephyr/dt-bindings/clock/stm32l4\_clock.h](stm32l4__clock_8h.md)>

44#elif defined(CONFIG\_SOC\_SERIES\_STM32MP2X)

45#include <[zephyr/dt-bindings/clock/stm32mp2\_clock.h](stm32mp2__clock_8h.md)>

46#elif defined(CONFIG\_SOC\_SERIES\_STM32WBX)

47#include <[zephyr/dt-bindings/clock/stm32wb\_clock.h](stm32wb__clock_8h.md)>

48#elif defined(CONFIG\_SOC\_SERIES\_STM32WB0X)

49#include <[zephyr/dt-bindings/clock/stm32wb0\_clock.h](stm32wb0__clock_8h.md)>

50#elif defined(CONFIG\_SOC\_SERIES\_STM32WLX)

51#include <[zephyr/dt-bindings/clock/stm32wl\_clock.h](stm32wl__clock_8h.md)>

52#elif defined(CONFIG\_SOC\_SERIES\_STM32H5X)

53#include <[zephyr/dt-bindings/clock/stm32h5\_clock.h](stm32h5__clock_8h.md)>

54#elif defined(CONFIG\_SOC\_SERIES\_STM32H7X)

55#include <[zephyr/dt-bindings/clock/stm32h7\_clock.h](stm32h7__clock_8h.md)>

56#elif defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

57#include <[zephyr/dt-bindings/clock/stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)>

58#elif defined(CONFIG\_SOC\_SERIES\_STM32MP13X)

59#include <[zephyr/dt-bindings/clock/stm32mp13\_clock.h](stm32mp13__clock_8h.md)>

60#elif defined(CONFIG\_SOC\_SERIES\_STM32N6X)

61#include <[zephyr/dt-bindings/clock/stm32n6\_clock.h](stm32n6__clock_8h.md)>

62#elif defined(CONFIG\_SOC\_SERIES\_STM32U0X)

63#include <[zephyr/dt-bindings/clock/stm32u0\_clock.h](stm32u0__clock_8h.md)>

64#elif defined(CONFIG\_SOC\_SERIES\_STM32U3X)

65#include <[zephyr/dt-bindings/clock/stm32u3\_clock.h](stm32u3__clock_8h.md)>

66#elif defined(CONFIG\_SOC\_SERIES\_STM32U5X)

67#include <[zephyr/dt-bindings/clock/stm32u5\_clock.h](stm32u5__clock_8h.md)>

68#elif defined(CONFIG\_SOC\_SERIES\_STM32WBAX)

69#include <[zephyr/dt-bindings/clock/stm32wba\_clock.h](stm32wba__clock_8h.md)>

70#else

71#include <[zephyr/dt-bindings/clock/stm32\_clock.h](stm32__clock_8h.md)>

72#endif

73

[ 75](stm32__clock__control_8h.md#ad33dc3d92546f9a4162a65a06ac6c673)#define STM32\_CLOCK\_CONTROL\_NODE DT\_NODELABEL(rcc)

76

78

[ 79](stm32__clock__control_8h.md#a38a0117c88924c6e1beca37e6cdea56b)#define STM32\_AHB\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

[ 80](stm32__clock__control_8h.md#a7af7ec37fc9d13d8d3bd6c3193ac8660)#define STM32\_APB1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb1\_prescaler)

[ 81](stm32__clock__control_8h.md#ad82f77d7d85845342bfa613557b1f569)#define STM32\_APB2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb2\_prescaler)

[ 82](stm32__clock__control_8h.md#ad1ffa671b55ad88e624ed9b7c4a22839)#define STM32\_APB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb3\_prescaler)

[ 83](stm32__clock__control_8h.md#adf8be1edd443c074679ad6b2ae7d19ed)#define STM32\_APB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb4\_prescaler)

[ 84](stm32__clock__control_8h.md#aa3510cdd90c9cc8b34933954f6e71caa)#define STM32\_APB5\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb5\_prescaler)

[ 85](stm32__clock__control_8h.md#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)#define STM32\_APB7\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb7\_prescaler)

[ 86](stm32__clock__control_8h.md#afca170bc72a77d8905b6c2ca0cce9e7b)#define STM32\_AHB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

[ 87](stm32__clock__control_8h.md#a3da9fd6fe11ceb8c2225e43eb2556d2d)#define STM32\_AHB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

[ 88](stm32__clock__control_8h.md#aeb1fabf85560ccd6cc1c0bdb34c86ec2)#define STM32\_AHB5\_PRESCALER DT\_PROP\_OR(DT\_NODELABEL(rcc), ahb5\_prescaler, 1)

[ 89](stm32__clock__control_8h.md#a18dc4749249030d371007b5135f5af54)#define STM32\_CPU1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

[ 90](stm32__clock__control_8h.md#a4f1975635dc6244f98263636c44f3942)#define STM32\_CPU2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu2\_prescaler)

91

92#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

93#define STM32\_CORE\_PRESCALER STM32\_AHB\_PRESCALER

94#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

95#define STM32\_CORE\_PRESCALER STM32\_CPU1\_PRESCALER

96#endif

97

98#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

99#define STM32\_FLASH\_PRESCALER STM32\_AHB3\_PRESCALER

100#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

101#define STM32\_FLASH\_PRESCALER STM32\_AHB4\_PRESCALER

102#else

[ 103](stm32__clock__control_8h.md#ac3274b70aee7aff6282eaa77ca819f27)#define STM32\_FLASH\_PRESCALER STM32\_CORE\_PRESCALER

104#endif

105

[ 106](stm32__clock__control_8h.md#a29ef6b98c22a522cde9f7dab5b11ace0)#define STM32\_ADC\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc\_prescaler)

[ 107](stm32__clock__control_8h.md#a35954cadc11af5ee499918be312acf38)#define STM32\_ADC12\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc12\_prescaler)

[ 108](stm32__clock__control_8h.md#a1cae4646086d8f855b72d55fee1483ad)#define STM32\_ADC34\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc34\_prescaler)

109

111#if defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

112#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), dcpre)

113#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

114#define STM32\_PPRE1 DT\_PROP(DT\_NODELABEL(rcc), ppre1)

115#define STM32\_PPRE2 DT\_PROP(DT\_NODELABEL(rcc), ppre2)

116#define STM32\_PPRE4 DT\_PROP(DT\_NODELABEL(rcc), ppre4)

117#define STM32\_PPRE5 DT\_PROP(DT\_NODELABEL(rcc), ppre5)

118#else

[ 119](stm32__clock__control_8h.md#a51967fd4dcf9ec8fe8e7250b5af32c87)#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), d1cpre)

[ 120](stm32__clock__control_8h.md#a035ea0d8259c0f89306c6a7d344705f2)#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

[ 121](stm32__clock__control_8h.md#a844064bd8ccafb5df4bf02748840491d)#define STM32\_D2PPRE1 DT\_PROP(DT\_NODELABEL(rcc), d2ppre1)

[ 122](stm32__clock__control_8h.md#a50394a7e040433c738fc7e9f03b7aff3)#define STM32\_D2PPRE2 DT\_PROP(DT\_NODELABEL(rcc), d2ppre2)

[ 123](stm32__clock__control_8h.md#a02a098a3296751f55ea349faecff7bd5)#define STM32\_D1PPRE DT\_PROP(DT\_NODELABEL(rcc), d1ppre)

[ 124](stm32__clock__control_8h.md#a9dd9b0e8ef84e6ff033a707b2a0ec231)#define STM32\_D3PPRE DT\_PROP(DT\_NODELABEL(rcc), d3ppre)

125#endif /\* CONFIG\_SOC\_SERIES\_STM32H7RSX \*/

126

[ 128](stm32__clock__control_8h.md#aea3d7b8e3adedef5f93cdb38852a8097)#define STM32\_AHB5\_DIV DT\_PROP(DT\_NODELABEL(rcc), ahb5\_div)

129

[ 130](stm32__clock__control_8h.md#ad9bff8a9cfbe0dbe0db73d077cb7a227)#define DT\_RCC\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(rcc))

131

132/\* To enable use of IS\_ENABLED utility macro, these symbols

133 \* should not be defined directly using DT\_SAME\_NODE.

134 \*/

135#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(pll))

136#define STM32\_SYSCLK\_SRC\_PLL 1

137#endif

138#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

139#define STM32\_SYSCLK\_SRC\_HSI 1

140#endif

141#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

142#define STM32\_SYSCLK\_SRC\_HSE 1

143#endif

144#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

145#define STM32\_SYSCLK\_SRC\_MSI 1

146#endif

147#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

148#define STM32\_SYSCLK\_SRC\_MSIS 1

149#endif

150#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

151#define STM32\_SYSCLK\_SRC\_CSI 1

152#endif

153#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(ic2))

154#define STM32\_SYSCLK\_SRC\_IC2 1

155#endif

156

157#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(rcc), st\_stm32n6\_rcc, okay)

158#if (DT\_SAME\_NODE(DT\_CLOCKS\_CTLR\_BY\_IDX(DT\_NODELABEL(cpusw), 0), DT\_NODELABEL(rcc)))

159#if (DT\_CLOCKS\_CELL\_BY\_IDX(DT\_NODELABEL(cpusw), 0, bus) == STM32\_SRC\_HSI)

160#define STM32\_CPUCLK\_SRC\_HSI 1

161#elif (DT\_CLOCKS\_CELL\_BY\_IDX(DT\_NODELABEL(cpusw), 0, bus) == STM32\_SRC\_MSI)

162#define STM32\_CPUCLK\_SRC\_MSI 1

163#elif (DT\_CLOCKS\_CELL\_BY\_IDX(DT\_NODELABEL(cpusw), 0, bus) == STM32\_SRC\_HSE)

164#define STM32\_CPUCLK\_SRC\_HSE 1

165#elif (DT\_CLOCKS\_CELL\_BY\_IDX(DT\_NODELABEL(cpusw), 0, bus) == STM32\_SRC\_IC1)

166#define STM32\_CPUCLK\_SRC\_IC1 1

167#endif

168#endif /\* cpusw clk source is rcc \*/

169

170#define STM32\_TIMG\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), timg\_prescaler)

171#endif /\* rcc node compatible st\_stm32n6\_rcc and okay \*/

172

174

175#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f2\_pll\_clock, okay) || \

176 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f4\_pll\_clock, okay) || \

177 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f7\_pll\_clock, okay) || \

178 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g0\_pll\_clock, okay) || \

179 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g4\_pll\_clock, okay) || \

180 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l4\_pll\_clock, okay) || \

181 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u0\_pll\_clock, okay) || \

182 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u5\_pll\_clock, okay) || \

183 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wb\_pll\_clock, okay) || \

184 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wba\_pll\_clock, okay) || \

185 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7\_pll\_clock, okay) || \

186 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7rs\_pll\_clock, okay) || \

187 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32mp13\_pll\_clock, okay)

188#define STM32\_PLL\_ENABLED 1

189#define STM32\_PLL\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div\_m)

190#define STM32\_PLL\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul\_n)

191#define STM32\_PLL\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_p)

192#define STM32\_PLL\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_p, 1)

193#define STM32\_PLL\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_q)

194#define STM32\_PLL\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_q, 1)

195#define STM32\_PLL\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_r)

196#define STM32\_PLL\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_r, 1)

197#define STM32\_PLL\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_s)

198#define STM32\_PLL\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_s, 1)

199#define STM32\_PLL\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), fracn)

200#define STM32\_PLL\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll), fracn, 1)

201#endif

202

203#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f4\_plli2s\_clock, okay)

204#define STM32\_PLLI2S\_ENABLED 1

205#define STM32\_PLLI2S\_M\_DIVISOR STM32\_PLL\_M\_DIVISOR

206#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

207#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

208#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

209#endif

210

211#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f411\_plli2s\_clock, okay)

212#define STM32\_PLLI2S\_ENABLED 1

213#define STM32\_PLLI2S\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(plli2s), div\_m)

214#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

215#define STM32\_PLLI2S\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_q)

216#define STM32\_PLLI2S\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_q, 1)

217#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

218#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

219#endif

220

221#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32u5\_pll\_clock, okay) || \

222 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7\_pll\_clock, okay) || \

223 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7rs\_pll\_clock, okay) || \

224 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32mp13\_pll\_clock, okay)

225#define STM32\_PLL2\_ENABLED 1

226#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

227#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

228#define STM32\_PLL2\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_p)

229#define STM32\_PLL2\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_p, 1)

230#define STM32\_PLL2\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_q)

231#define STM32\_PLL2\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_q, 1)

232#define STM32\_PLL2\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_r)

233#define STM32\_PLL2\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_r, 1)

234#define STM32\_PLL2\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_s)

235#define STM32\_PLL2\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_s, 1)

236#define STM32\_PLL2\_T\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_t)

237#define STM32\_PLL2\_T\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_t, 1)

238#define STM32\_PLL2\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), fracn)

239#define STM32\_PLL2\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll2), fracn, 1)

240#endif

241

242#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7\_pll\_clock, okay) || \

243 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32u5\_pll\_clock, okay) || \

244 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7rs\_pll\_clock, okay) || \

245 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32mp13\_pll\_clock, okay)

246#define STM32\_PLL3\_ENABLED 1

247#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

248#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

249#define STM32\_PLL3\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_p)

250#define STM32\_PLL3\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_p, 1)

251#define STM32\_PLL3\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_q)

252#define STM32\_PLL3\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_q, 1)

253#define STM32\_PLL3\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_r)

254#define STM32\_PLL3\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_r, 1)

255#define STM32\_PLL3\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_s)

256#define STM32\_PLL3\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_s, 1)

257#define STM32\_PLL3\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), fracn)

258#define STM32\_PLL3\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll3), fracn, 1)

259#endif

260

261#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll4), st\_stm32mp13\_pll\_clock, okay)

262#define STM32\_PLL4\_ENABLED 1

263#define STM32\_PLL4\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_m)

264#define STM32\_PLL4\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll4), mul\_n)

265#define STM32\_PLL4\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll4), div\_p)

266#define STM32\_PLL4\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll4), div\_p, 1)

267#define STM32\_PLL4\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll4), div\_q)

268#define STM32\_PLL4\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll4), div\_q, 1)

269#define STM32\_PLL4\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll4), div\_r)

270#define STM32\_PLL4\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll4), div\_r, 1)

271#define STM32\_PLL4\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll4), fracn)

272#define STM32\_PLL4\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll4), fracn, 1)

273#endif

274

275#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f1\_pll\_clock, okay)

276#define STM32\_PLL\_ENABLED 1

277#define STM32\_PLL\_XTPRE DT\_PROP(DT\_NODELABEL(pll), xtpre)

278#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

279#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), usbpre)

280#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f0\_pll\_clock, okay) || \

281 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f100\_pll\_clock, okay) || \

282 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f105\_pll\_clock, okay)

283#define STM32\_PLL\_ENABLED 1

284#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

285#define STM32\_PLL\_PREDIV DT\_PROP(DT\_NODELABEL(pll), prediv)

286#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), otgfspre)

287#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l0\_pll\_clock, okay)

288#define STM32\_PLL\_ENABLED 1

289#define STM32\_PLL\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div)

290#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

291#endif

292

293#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32f105\_pll2\_clock, okay)

294#define STM32\_PLL2\_ENABLED 1

295#define STM32\_PLL2\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul)

296#define STM32\_PLL2\_PREDIV DT\_PROP(DT\_NODELABEL(pll2), prediv)

297#endif

298

299#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll1), st\_stm32n6\_pll\_clock, okay)

300#define STM32\_PLL1\_ENABLED 1

301#define STM32\_PLL1\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll1), div\_m)

302#define STM32\_PLL1\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll1), mul\_n)

303#define STM32\_PLL1\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll1), div\_p1)

304#define STM32\_PLL1\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll1), div\_p2)

305#endif

306

307#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32n6\_pll\_clock, okay)

308#define STM32\_PLL2\_ENABLED 1

309#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

310#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

311#define STM32\_PLL2\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_p1)

312#define STM32\_PLL2\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_p2)

313#endif

314

315#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32n6\_pll\_clock, okay)

316#define STM32\_PLL3\_ENABLED 1

317#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

318#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

319#define STM32\_PLL3\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_p1)

320#define STM32\_PLL3\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_p2)

321#endif

322

323#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll4), st\_stm32n6\_pll\_clock, okay)

324#define STM32\_PLL4\_ENABLED 1

325#define STM32\_PLL4\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_m)

326#define STM32\_PLL4\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll4), mul\_n)

327#define STM32\_PLL4\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_p1)

328#define STM32\_PLL4\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_p2)

329#endif

330

332#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll)) && \

333 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), clocks)

334#define DT\_PLL\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll))

335#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

336#define STM32\_PLL\_SRC\_MSI 1

337#endif

338#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

339#define STM32\_PLL\_SRC\_MSIS 1

340#endif

341#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

342#define STM32\_PLL\_SRC\_HSI 1

343#endif

344#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

345#define STM32\_PLL\_SRC\_CSI 1

346#endif

347#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

348#define STM32\_PLL\_SRC\_HSE 1

349#endif

350#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(pll2))

351#define STM32\_PLL\_SRC\_PLL2 1

352#endif

353

354#endif

355

357#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll2)) && \

358 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), clocks)

359#define DT\_PLL2\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll2))

360#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

361#define STM32\_PLL2\_SRC\_MSI 1

362#endif

363#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

364#define STM32\_PLL2\_SRC\_MSIS 1

365#endif

366#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

367#define STM32\_PLL2\_SRC\_HSI 1

368#endif

369#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

370#define STM32\_PLL2\_SRC\_HSE 1

371#endif

372

373#endif

374

376#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll3)) && \

377 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), clocks)

378#define DT\_PLL3\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll3))

379#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

380#define STM32\_PLL3\_SRC\_MSI 1

381#endif

382#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

383#define STM32\_PLL3\_SRC\_MSIS 1

384#endif

385#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

386#define STM32\_PLL3\_SRC\_HSI 1

387#endif

388#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

389#define STM32\_PLL3\_SRC\_HSE 1

390#endif

391

392#endif

393

395#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll4), okay) && \

396 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll4), clocks)

397#define DT\_PLL4\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll4))

398#if DT\_SAME\_NODE(DT\_PLL4\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

399#define STM32\_PLL4\_SRC\_MSI 1

400#endif

401#if DT\_SAME\_NODE(DT\_PLL4\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

402#define STM32\_PLL4\_SRC\_HSI 1

403#endif

404#if DT\_SAME\_NODE(DT\_PLL4\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

405#define STM32\_PLL4\_SRC\_HSE 1

406#endif

407

408#endif

409

410

412

413#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), fixed\_clock, okay)

414#define STM32\_LSE\_ENABLED 1

415#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

416#define STM32\_LSE\_DRIVING 0

417#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

418#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), st\_stm32\_lse\_clock, okay)

419#define STM32\_LSE\_ENABLED 1

420#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

421#define STM32\_LSE\_DRIVING DT\_PROP(DT\_NODELABEL(clk\_lse), driving\_capability)

422#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

423#else

[ 424](stm32__clock__control_8h.md#a05b49e91f478558d33b2b862718758fa)#define STM32\_LSE\_ENABLED 0

[ 425](stm32__clock__control_8h.md#aedfe731de4f32e8dacd027bb115ca0e9)#define STM32\_LSE\_FREQ 0

[ 426](stm32__clock__control_8h.md#aead1c5c5ac685af96410f4883f7e988b)#define STM32\_LSE\_DRIVING 0

[ 427](stm32__clock__control_8h.md#a94745d7699b62ef9e7f8bbfbc6803727)#define STM32\_LSE\_BYPASS 0

428#endif

429

430#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay) || \

431 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32l0\_msi\_clock, okay)

432#define STM32\_MSI\_ENABLED 1

433#define STM32\_MSI\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_range)

434#endif

435

436#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay)

437#define STM32\_MSI\_ENABLED 1

438#define STM32\_MSI\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_pll\_mode)

439#endif

440

441#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msis), st\_stm32u5\_msi\_clock, okay) || \

442 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msis), st\_stm32u3\_msi\_clock, okay)

443#define STM32\_MSIS\_ENABLED 1

444#define STM32\_MSIS\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_range)

445#define STM32\_MSIS\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_pll\_mode)

446#else

[ 447](stm32__clock__control_8h.md#a1a83a4c9a806689ac963e2ea8b142fda)#define STM32\_MSIS\_ENABLED 0

[ 448](stm32__clock__control_8h.md#a0109485d9cfd70782ce6aff604399330)#define STM32\_MSIS\_RANGE 0

[ 449](stm32__clock__control_8h.md#a02f0311b8e9c41a004ed355aff37a7b3)#define STM32\_MSIS\_PLL\_MODE 0

450#endif

451

452#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msik), st\_stm32u5\_msi\_clock, okay) || \

453 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msik), st\_stm32u3\_msi\_clock, okay)

454#define STM32\_MSIK\_ENABLED 1

455#define STM32\_MSIK\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_range)

456#define STM32\_MSIK\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_pll\_mode)

457#else

[ 458](stm32__clock__control_8h.md#a379e09d2e380483155b0ef8cc39d490b)#define STM32\_MSIK\_ENABLED 0

[ 459](stm32__clock__control_8h.md#a2fb4bc355d7e69e6b676794d0ab4cbba)#define STM32\_MSIK\_RANGE 0

[ 460](stm32__clock__control_8h.md#a67d63326f5ebe1b249eb56b227aecb29)#define STM32\_MSIK\_PLL\_MODE 0

461#endif

462

463#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_csi), fixed\_clock, okay)

464#define STM32\_CSI\_ENABLED 1

465#define STM32\_CSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_csi), clock\_frequency)

466#else

[ 467](stm32__clock__control_8h.md#a2110dbb73ce08ba40555f1d95b50ce5c)#define STM32\_CSI\_FREQ 0

468#endif

469

470#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi), fixed\_clock, okay)

471#define STM32\_LSI\_ENABLED 1

472#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi), clock\_frequency)

473#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi1), fixed\_clock, okay)

474#define STM32\_LSI\_ENABLED 1

475#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi1), clock\_frequency)

476#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi2), fixed\_clock, okay)

477#define STM32\_LSI\_ENABLED 1

478#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi2), clock\_frequency)

479#else

[ 480](stm32__clock__control_8h.md#ae4ad7f2e4844901d753a91c1ba5c58c5)#define STM32\_LSI\_FREQ 0

481#endif

482

483#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), fixed\_clock, okay)

484#define STM32\_HSI\_DIV\_ENABLED 0

485#define STM32\_HSI\_ENABLED 1

486#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

487#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32h7\_hsi\_clock, okay) \

488 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32g0\_hsi\_clock, okay) \

489 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32c0\_hsi\_clock, okay) \

490 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32n6\_hsi\_clock, okay)

491#define STM32\_HSI\_DIV\_ENABLED 1

492#define STM32\_HSI\_ENABLED 1

493#define STM32\_HSI\_DIVISOR DT\_PROP(DT\_NODELABEL(clk\_hsi), hsi\_div)

494#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

495#else

[ 496](stm32__clock__control_8h.md#aa67c0b4d532b58d78b12d36ae6817912)#define STM32\_HSI\_DIV\_ENABLED 0

[ 497](stm32__clock__control_8h.md#a2cc52c346227b2dfb91e1ab5aeda586c)#define STM32\_HSI\_DIVISOR 1

[ 498](stm32__clock__control_8h.md#af906386de1fde7ab0894971723a0a801)#define STM32\_HSI\_FREQ 0

499#endif

500

501#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), fixed\_clock, okay)

502#define STM32\_HSE\_ENABLED 1

503#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

504#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32\_hse\_clock, okay)

505#define STM32\_HSE\_ENABLED 1

506#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

507#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

508#define STM32\_HSE\_CSS DT\_PROP(DT\_NODELABEL(clk\_hse), css\_enabled)

509#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wl\_hse\_clock, okay)

510#define STM32\_HSE\_ENABLED 1

511#define STM32\_HSE\_TCXO DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_tcxo)

512#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

513#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

514#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wba\_hse\_clock, okay)

515#define STM32\_HSE\_ENABLED 1

516#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

517#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

518#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32n6\_hse\_clock, okay)

519#define STM32\_HSE\_ENABLED 1

520#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

521#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

522#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

523#else

[ 524](stm32__clock__control_8h.md#a7c3796ef481224c9e2f7516853677ec9)#define STM32\_HSE\_FREQ 0

525#endif

526

527#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), fixed\_clock, okay)

528#define STM32\_HSI48\_ENABLED 1

529#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

530#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), st\_stm32\_hsi48\_clock, okay)

531#define STM32\_HSI48\_ENABLED 1

532#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

533#define STM32\_HSI48\_CRS\_USB\_SOF DT\_PROP(DT\_NODELABEL(clk\_hsi48), crs\_usb\_sof)

534#endif

535

536#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(perck), st\_stm32\_clock\_mux, okay)

537#define STM32\_CKPER\_ENABLED 1

538#endif

539

540#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(cpusw), st\_stm32\_clock\_mux, okay)

541#define STM32\_CPUSW\_ENABLED 1

542#endif

543

544#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic1), st\_stm32n6\_ic\_clock\_mux, okay)

545#define STM32\_IC1\_ENABLED 1

546#define STM32\_IC1\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic1), pll\_src)

547#define STM32\_IC1\_DIV DT\_PROP(DT\_NODELABEL(ic1), ic\_div)

548#endif

549

550#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic2), st\_stm32n6\_ic\_clock\_mux, okay)

551#define STM32\_IC2\_ENABLED 1

552#define STM32\_IC2\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic2), pll\_src)

553#define STM32\_IC2\_DIV DT\_PROP(DT\_NODELABEL(ic2), ic\_div)

554#endif

555

556#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic3), st\_stm32n6\_ic\_clock\_mux, okay)

557#define STM32\_IC3\_ENABLED 1

558#define STM32\_IC3\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic3), pll\_src)

559#define STM32\_IC3\_DIV DT\_PROP(DT\_NODELABEL(ic3), ic\_div)

560#endif

561

562#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic4), st\_stm32n6\_ic\_clock\_mux, okay)

563#define STM32\_IC4\_ENABLED 1

564#define STM32\_IC4\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic4), pll\_src)

565#define STM32\_IC4\_DIV DT\_PROP(DT\_NODELABEL(ic4), ic\_div)

566#endif

567

568#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic5), st\_stm32n6\_ic\_clock\_mux, okay)

569#define STM32\_IC5\_ENABLED 1

570#define STM32\_IC5\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic5), pll\_src)

571#define STM32\_IC5\_DIV DT\_PROP(DT\_NODELABEL(ic5), ic\_div)

572#endif

573

574#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic6), st\_stm32n6\_ic\_clock\_mux, okay)

575#define STM32\_IC6\_ENABLED 1

576#define STM32\_IC6\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic6), pll\_src)

577#define STM32\_IC6\_DIV DT\_PROP(DT\_NODELABEL(ic6), ic\_div)

578#endif

579

580#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic7), st\_stm32n6\_ic\_clock\_mux, okay)

581#define STM32\_IC7\_ENABLED 1

582#define STM32\_IC7\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic7), pll\_src)

583#define STM32\_IC7\_DIV DT\_PROP(DT\_NODELABEL(ic7), ic\_div)

584#endif

585

586#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic8), st\_stm32n6\_ic\_clock\_mux, okay)

587#define STM32\_IC8\_ENABLED 1

588#define STM32\_IC8\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic8), pll\_src)

589#define STM32\_IC8\_DIV DT\_PROP(DT\_NODELABEL(ic8), ic\_div)

590#endif

591

592#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic9), st\_stm32n6\_ic\_clock\_mux, okay)

593#define STM32\_IC9\_ENABLED 1

594#define STM32\_IC9\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic9), pll\_src)

595#define STM32\_IC9\_DIV DT\_PROP(DT\_NODELABEL(ic9), ic\_div)

596#endif

597

598#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic10), st\_stm32n6\_ic\_clock\_mux, okay)

599#define STM32\_IC10\_ENABLED 1

600#define STM32\_IC10\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic10), pll\_src)

601#define STM32\_IC10\_DIV DT\_PROP(DT\_NODELABEL(ic10), ic\_div)

602#endif

603

604#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic11), st\_stm32n6\_ic\_clock\_mux, okay)

605#define STM32\_IC11\_ENABLED 1

606#define STM32\_IC11\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic11), pll\_src)

607#define STM32\_IC11\_DIV DT\_PROP(DT\_NODELABEL(ic11), ic\_div)

608#endif

609

610#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic12), st\_stm32n6\_ic\_clock\_mux, okay)

611#define STM32\_IC12\_ENABLED 1

612#define STM32\_IC12\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic12), pll\_src)

613#define STM32\_IC12\_DIV DT\_PROP(DT\_NODELABEL(ic12), ic\_div)

614#endif

615

616#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic13), st\_stm32n6\_ic\_clock\_mux, okay)

617#define STM32\_IC13\_ENABLED 1

618#define STM32\_IC13\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic13), pll\_src)

619#define STM32\_IC13\_DIV DT\_PROP(DT\_NODELABEL(ic13), ic\_div)

620#endif

621

622#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic14), st\_stm32n6\_ic\_clock\_mux, okay)

623#define STM32\_IC14\_ENABLED 1

624#define STM32\_IC14\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic14), pll\_src)

625#define STM32\_IC14\_DIV DT\_PROP(DT\_NODELABEL(ic14), ic\_div)

626#endif

627

628#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic15), st\_stm32n6\_ic\_clock\_mux, okay)

629#define STM32\_IC15\_ENABLED 1

630#define STM32\_IC15\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic15), pll\_src)

631#define STM32\_IC15\_DIV DT\_PROP(DT\_NODELABEL(ic15), ic\_div)

632#endif

633

634#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic16), st\_stm32n6\_ic\_clock\_mux, okay)

635#define STM32\_IC16\_ENABLED 1

636#define STM32\_IC16\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic16), pll\_src)

637#define STM32\_IC16\_DIV DT\_PROP(DT\_NODELABEL(ic16), ic\_div)

638#endif

639

640#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic17), st\_stm32n6\_ic\_clock\_mux, okay)

641#define STM32\_IC17\_ENABLED 1

642#define STM32\_IC17\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic17), pll\_src)

643#define STM32\_IC17\_DIV DT\_PROP(DT\_NODELABEL(ic17), ic\_div)

644#endif

645

646#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic18), st\_stm32n6\_ic\_clock\_mux, okay)

647#define STM32\_IC18\_ENABLED 1

648#define STM32\_IC18\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic18), pll\_src)

649#define STM32\_IC18\_DIV DT\_PROP(DT\_NODELABEL(ic18), ic\_div)

650#endif

651

652#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic19), st\_stm32n6\_ic\_clock\_mux, okay)

653#define STM32\_IC19\_ENABLED 1

654#define STM32\_IC19\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic19), pll\_src)

655#define STM32\_IC19\_DIV DT\_PROP(DT\_NODELABEL(ic19), ic\_div)

656#endif

657

658#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic20), st\_stm32n6\_ic\_clock\_mux, okay)

659#define STM32\_IC20\_ENABLED 1

660#define STM32\_IC20\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic20), pll\_src)

661#define STM32\_IC20\_DIV DT\_PROP(DT\_NODELABEL(ic20), ic\_div)

662#endif

663

665

[ 666](structstm32__pclken.md)struct [stm32\_pclken](structstm32__pclken.md) {

[ 667](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) : [STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0);

[ 668](structstm32__pclken.md#a38e8d02b1a7117115e7fa0405ed10cc4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [div](structstm32__pclken.md#a38e8d02b1a7117115e7fa0405ed10cc4) : (32 - [STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0));

[ 669](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf);

670};

671

673

[ 674](stm32__clock__control_8h.md#aa1b0949b4c58d57dcd2e979320cbed0a)#define STM32\_CLOCK\_INFO(clk\_index, node\_id) \

675 { \

676 .enr = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bits), \

677 .bus = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) & \

678 GENMASK(STM32\_CLOCK\_DIV\_SHIFT - 1, 0), \

679 .div = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) >> \

680 STM32\_CLOCK\_DIV\_SHIFT, \

681 }

[ 682](stm32__clock__control_8h.md#a9eb57b349f41edec11ff52a78015aea9)#define STM32\_DT\_CLOCKS(node\_id) \

683 { \

684 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

685 STM32\_CLOCK\_INFO, (,), node\_id) \

686 }

687

[ 688](stm32__clock__control_8h.md#a693176c2c60364d327aa5768ebfac185)#define STM32\_DT\_INST\_CLOCKS(inst) \

689 STM32\_DT\_CLOCKS(DT\_DRV\_INST(inst))

690

[ 691](stm32__clock__control_8h.md#a38559b31633eca5475b73b8a88df1fcd)#define STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT(inst) DT\_INST\_CLOCKS\_HAS\_IDX(inst, 1) ||

[ 692](stm32__clock__control_8h.md#aac932dfd992b11d479edf2a2d5e8de47)#define STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

693 (DT\_INST\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT) 0)

694

[ 695](stm32__clock__control_8h.md#a8743160d8765b466f8ac6a89efaa9dbc)#define STM32\_DOMAIN\_CLOCK\_SUPPORT(id) DT\_CLOCKS\_HAS\_IDX(DT\_NODELABEL(id), 1) ||

[ 696](stm32__clock__control_8h.md#a7951b8025683529eebdd415d6b65688b)#define STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

697 (DT\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_SUPPORT) 0)

698

700

[ 706](stm32__clock__control_8h.md#a932d2b05943fc3511f0ad82f4e10c98a)#define STM32\_DT\_CLKSEL\_REG\_GET(clock) \

707 (((clock) >> STM32\_DT\_CLKSEL\_REG\_SHIFT) & STM32\_DT\_CLKSEL\_REG\_MASK)

708

[ 714](stm32__clock__control_8h.md#a721bbde6ed4c76019fba67677e359c05)#define STM32\_DT\_CLKSEL\_SHIFT\_GET(clock) \

715 (((clock) >> STM32\_DT\_CLKSEL\_SHIFT\_SHIFT) & STM32\_DT\_CLKSEL\_SHIFT\_MASK)

716

[ 722](stm32__clock__control_8h.md#ad2c6955f07a96ff6ffecf2b1b267de2c)#define STM32\_DT\_CLKSEL\_MASK\_GET(clock) \

723 (((clock) >> STM32\_DT\_CLKSEL\_MASK\_SHIFT) & STM32\_DT\_CLKSEL\_MASK\_MASK)

724

[ 730](stm32__clock__control_8h.md#aecf915cbdbf64d743b6ccb020a905abe)#define STM32\_DT\_CLKSEL\_VAL\_GET(clock) \

731 (((clock) >> STM32\_DT\_CLKSEL\_VAL\_SHIFT) & STM32\_DT\_CLKSEL\_VAL\_MASK)

732

733#if defined(STM32\_HSE\_CSS)

742void stm32\_hse\_css\_callback(void);

743#endif

744

745#ifdef CONFIG\_SOC\_SERIES\_STM32WB0X

750typedef void (\*lsi\_update\_cb\_t)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) new\_lsi\_frequency);

751

763int stm32wb0\_register\_lsi\_update\_callback(lsi\_update\_cb\_t cb);

764#endif /\* CONFIG\_SOC\_SERIES\_STM32WB0X \*/

765

766#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stm32\_clock.h](stm32__clock_8h.md)

[STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0)

#define STM32\_CLOCK\_DIV\_SHIFT

**Definition** stm32\_clock.h:27

[stm32c0\_clock.h](stm32c0__clock_8h.md)

[stm32f0\_clock.h](stm32f0__clock_8h.md)

[stm32f10x\_clock.h](stm32f10x__clock_8h.md)

[stm32f1\_clock.h](stm32f1__clock_8h.md)

[stm32f3\_clock.h](stm32f3__clock_8h.md)

[stm32f410\_clock.h](stm32f410__clock_8h.md)

[stm32f4\_clock.h](stm32f4__clock_8h.md)

[stm32f7\_clock.h](stm32f7__clock_8h.md)

[stm32g0\_clock.h](stm32g0__clock_8h.md)

[stm32g4\_clock.h](stm32g4__clock_8h.md)

[stm32h5\_clock.h](stm32h5__clock_8h.md)

[stm32h7\_clock.h](stm32h7__clock_8h.md)

[stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)

[stm32l0\_clock.h](stm32l0__clock_8h.md)

[stm32l1\_clock.h](stm32l1__clock_8h.md)

[stm32l4\_clock.h](stm32l4__clock_8h.md)

[stm32mp13\_clock.h](stm32mp13__clock_8h.md)

[stm32mp2\_clock.h](stm32mp2__clock_8h.md)

[stm32n6\_clock.h](stm32n6__clock_8h.md)

[stm32u0\_clock.h](stm32u0__clock_8h.md)

[stm32u3\_clock.h](stm32u3__clock_8h.md)

[stm32u5\_clock.h](stm32u5__clock_8h.md)

[stm32wb0\_clock.h](stm32wb0__clock_8h.md)

[stm32wb\_clock.h](stm32wb__clock_8h.md)

[stm32wba\_clock.h](stm32wba__clock_8h.md)

[stm32wl\_clock.h](stm32wl__clock_8h.md)

[stm32\_pclken](structstm32__pclken.md)

Driver structure definition.

**Definition** stm32\_clock\_control.h:666

[stm32\_pclken::div](structstm32__pclken.md#a38e8d02b1a7117115e7fa0405ed10cc4)

uint32\_t div

**Definition** stm32\_clock\_control.h:668

[stm32\_pclken::bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e)

uint32\_t bus

**Definition** stm32\_clock\_control.h:667

[stm32\_pclken::enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf)

uint32\_t enr

**Definition** stm32\_clock\_control.h:669

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [stm32\_clock\_control.h](stm32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
