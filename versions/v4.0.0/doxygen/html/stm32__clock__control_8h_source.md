---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32__clock__control_8h_source.html
original_path: doxygen/html/stm32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

30#elif defined(CONFIG\_SOC\_SERIES\_STM32F7X)

31#include <[zephyr/dt-bindings/clock/stm32f7\_clock.h](stm32f7__clock_8h.md)>

32#elif defined(CONFIG\_SOC\_SERIES\_STM32G0X)

33#include <[zephyr/dt-bindings/clock/stm32g0\_clock.h](stm32g0__clock_8h.md)>

34#elif defined(CONFIG\_SOC\_SERIES\_STM32G4X)

35#include <[zephyr/dt-bindings/clock/stm32g4\_clock.h](stm32g4__clock_8h.md)>

36#elif defined(CONFIG\_SOC\_SERIES\_STM32L0X)

37#include <[zephyr/dt-bindings/clock/stm32l0\_clock.h](stm32l0__clock_8h.md)>

38#elif defined(CONFIG\_SOC\_SERIES\_STM32L1X)

39#include <[zephyr/dt-bindings/clock/stm32l1\_clock.h](stm32l1__clock_8h.md)>

40#elif defined(CONFIG\_SOC\_SERIES\_STM32L4X) || \

41 defined(CONFIG\_SOC\_SERIES\_STM32L5X)

42#include <[zephyr/dt-bindings/clock/stm32l4\_clock.h](stm32l4__clock_8h.md)>

43#elif defined(CONFIG\_SOC\_SERIES\_STM32WBX)

44#include <[zephyr/dt-bindings/clock/stm32wb\_clock.h](stm32wb__clock_8h.md)>

45#elif defined(CONFIG\_SOC\_SERIES\_STM32WB0X)

46#include <[zephyr/dt-bindings/clock/stm32wb0\_clock.h](stm32wb0__clock_8h.md)>

47#elif defined(CONFIG\_SOC\_SERIES\_STM32WLX)

48#include <[zephyr/dt-bindings/clock/stm32wl\_clock.h](stm32wl__clock_8h.md)>

49#elif defined(CONFIG\_SOC\_SERIES\_STM32H5X)

50#include <[zephyr/dt-bindings/clock/stm32h5\_clock.h](stm32h5__clock_8h.md)>

51#elif defined(CONFIG\_SOC\_SERIES\_STM32H7X)

52#include <[zephyr/dt-bindings/clock/stm32h7\_clock.h](stm32h7__clock_8h.md)>

53#elif defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

54#include <[zephyr/dt-bindings/clock/stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)>

55#elif defined(CONFIG\_SOC\_SERIES\_STM32U0X)

56#include <[zephyr/dt-bindings/clock/stm32u0\_clock.h](stm32u0__clock_8h.md)>

57#elif defined(CONFIG\_SOC\_SERIES\_STM32U5X)

58#include <[zephyr/dt-bindings/clock/stm32u5\_clock.h](stm32u5__clock_8h.md)>

59#elif defined(CONFIG\_SOC\_SERIES\_STM32WBAX)

60#include <[zephyr/dt-bindings/clock/stm32wba\_clock.h](stm32wba__clock_8h.md)>

61#else

62#include <[zephyr/dt-bindings/clock/stm32\_clock.h](stm32__clock_8h.md)>

63#endif

64

[ 66](stm32__clock__control_8h.md#ad33dc3d92546f9a4162a65a06ac6c673)#define STM32\_CLOCK\_CONTROL\_NODE DT\_NODELABEL(rcc)

67

69

[ 70](stm32__clock__control_8h.md#a38a0117c88924c6e1beca37e6cdea56b)#define STM32\_AHB\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

[ 71](stm32__clock__control_8h.md#a7af7ec37fc9d13d8d3bd6c3193ac8660)#define STM32\_APB1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb1\_prescaler)

[ 72](stm32__clock__control_8h.md#ad82f77d7d85845342bfa613557b1f569)#define STM32\_APB2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb2\_prescaler)

[ 73](stm32__clock__control_8h.md#ad1ffa671b55ad88e624ed9b7c4a22839)#define STM32\_APB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb3\_prescaler)

[ 74](stm32__clock__control_8h.md#aa3510cdd90c9cc8b34933954f6e71caa)#define STM32\_APB5\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb5\_prescaler)

[ 75](stm32__clock__control_8h.md#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)#define STM32\_APB7\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb7\_prescaler)

[ 76](stm32__clock__control_8h.md#afca170bc72a77d8905b6c2ca0cce9e7b)#define STM32\_AHB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

[ 77](stm32__clock__control_8h.md#a3da9fd6fe11ceb8c2225e43eb2556d2d)#define STM32\_AHB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

[ 78](stm32__clock__control_8h.md#aeb1fabf85560ccd6cc1c0bdb34c86ec2)#define STM32\_AHB5\_PRESCALER DT\_PROP\_OR(DT\_NODELABEL(rcc), ahb5\_prescaler, 1)

[ 79](stm32__clock__control_8h.md#a18dc4749249030d371007b5135f5af54)#define STM32\_CPU1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

[ 80](stm32__clock__control_8h.md#a4f1975635dc6244f98263636c44f3942)#define STM32\_CPU2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu2\_prescaler)

81

82#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

83#define STM32\_CORE\_PRESCALER STM32\_AHB\_PRESCALER

84#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

85#define STM32\_CORE\_PRESCALER STM32\_CPU1\_PRESCALER

86#endif

87

88#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

89#define STM32\_FLASH\_PRESCALER STM32\_AHB3\_PRESCALER

90#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

91#define STM32\_FLASH\_PRESCALER STM32\_AHB4\_PRESCALER

92#else

[ 93](stm32__clock__control_8h.md#ac3274b70aee7aff6282eaa77ca819f27)#define STM32\_FLASH\_PRESCALER STM32\_CORE\_PRESCALER

94#endif

95

[ 96](stm32__clock__control_8h.md#a29ef6b98c22a522cde9f7dab5b11ace0)#define STM32\_ADC\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc\_prescaler)

[ 97](stm32__clock__control_8h.md#a35954cadc11af5ee499918be312acf38)#define STM32\_ADC12\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc12\_prescaler)

[ 98](stm32__clock__control_8h.md#a1cae4646086d8f855b72d55fee1483ad)#define STM32\_ADC34\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc34\_prescaler)

99

101#if defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

102#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), dcpre)

103#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

104#define STM32\_PPRE1 DT\_PROP(DT\_NODELABEL(rcc), ppre1)

105#define STM32\_PPRE2 DT\_PROP(DT\_NODELABEL(rcc), ppre2)

106#define STM32\_PPRE4 DT\_PROP(DT\_NODELABEL(rcc), ppre4)

107#define STM32\_PPRE5 DT\_PROP(DT\_NODELABEL(rcc), ppre5)

108#else

[ 109](stm32__clock__control_8h.md#a51967fd4dcf9ec8fe8e7250b5af32c87)#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), d1cpre)

[ 110](stm32__clock__control_8h.md#a035ea0d8259c0f89306c6a7d344705f2)#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

[ 111](stm32__clock__control_8h.md#a844064bd8ccafb5df4bf02748840491d)#define STM32\_D2PPRE1 DT\_PROP(DT\_NODELABEL(rcc), d2ppre1)

[ 112](stm32__clock__control_8h.md#a50394a7e040433c738fc7e9f03b7aff3)#define STM32\_D2PPRE2 DT\_PROP(DT\_NODELABEL(rcc), d2ppre2)

[ 113](stm32__clock__control_8h.md#a02a098a3296751f55ea349faecff7bd5)#define STM32\_D1PPRE DT\_PROP(DT\_NODELABEL(rcc), d1ppre)

[ 114](stm32__clock__control_8h.md#a9dd9b0e8ef84e6ff033a707b2a0ec231)#define STM32\_D3PPRE DT\_PROP(DT\_NODELABEL(rcc), d3ppre)

115#endif /\* CONFIG\_SOC\_SERIES\_STM32H7RSX \*/

116

[ 118](stm32__clock__control_8h.md#aea3d7b8e3adedef5f93cdb38852a8097)#define STM32\_AHB5\_DIV DT\_PROP(DT\_NODELABEL(rcc), ahb5\_div)

119

[ 120](stm32__clock__control_8h.md#ad9bff8a9cfbe0dbe0db73d077cb7a227)#define DT\_RCC\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(rcc))

121

122/\* To enable use of IS\_ENABLED utility macro, these symbols

123 \* should not be defined directly using DT\_SAME\_NODE.

124 \*/

125#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(pll))

126#define STM32\_SYSCLK\_SRC\_PLL 1

127#endif

128#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

129#define STM32\_SYSCLK\_SRC\_HSI 1

130#endif

131#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

132#define STM32\_SYSCLK\_SRC\_HSE 1

133#endif

134#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

135#define STM32\_SYSCLK\_SRC\_MSI 1

136#endif

137#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

138#define STM32\_SYSCLK\_SRC\_MSIS 1

139#endif

140#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

141#define STM32\_SYSCLK\_SRC\_CSI 1

142#endif

143

144

146

147#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f2\_pll\_clock, okay) || \

148 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f4\_pll\_clock, okay) || \

149 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f7\_pll\_clock, okay) || \

150 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g0\_pll\_clock, okay) || \

151 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g4\_pll\_clock, okay) || \

152 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l4\_pll\_clock, okay) || \

153 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u0\_pll\_clock, okay) || \

154 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u5\_pll\_clock, okay) || \

155 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wb\_pll\_clock, okay) || \

156 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wba\_pll\_clock, okay) || \

157 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7\_pll\_clock, okay) || \

158 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7rs\_pll\_clock, okay)

159#define STM32\_PLL\_ENABLED 1

160#define STM32\_PLL\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div\_m)

161#define STM32\_PLL\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul\_n)

162#define STM32\_PLL\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_p)

163#define STM32\_PLL\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_p, 1)

164#define STM32\_PLL\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_q)

165#define STM32\_PLL\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_q, 1)

166#define STM32\_PLL\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_r)

167#define STM32\_PLL\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_r, 1)

168#define STM32\_PLL\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_s)

169#define STM32\_PLL\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_s, 1)

170#define STM32\_PLL\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), fracn)

171#define STM32\_PLL\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll), fracn, 1)

172#endif

173

174#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f4\_plli2s\_clock, okay)

175#define STM32\_PLLI2S\_ENABLED 1

176#define STM32\_PLLI2S\_M\_DIVISOR STM32\_PLL\_M\_DIVISOR

177#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

178#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

179#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

180#endif

181

182#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f412\_plli2s\_clock, okay)

183#define STM32\_PLLI2S\_ENABLED 1

184#define STM32\_PLLI2S\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(plli2s), div\_m)

185#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

186#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

187#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

188#endif

189

190#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32u5\_pll\_clock, okay) || \

191 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7\_pll\_clock, okay) || \

192 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7rs\_pll\_clock, okay)

193#define STM32\_PLL2\_ENABLED 1

194#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

195#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

196#define STM32\_PLL2\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_p)

197#define STM32\_PLL2\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_p, 1)

198#define STM32\_PLL2\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_q)

199#define STM32\_PLL2\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_q, 1)

200#define STM32\_PLL2\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_r)

201#define STM32\_PLL2\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_r, 1)

202#define STM32\_PLL2\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_s)

203#define STM32\_PLL2\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_s, 1)

204#define STM32\_PLL2\_T\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_t)

205#define STM32\_PLL2\_T\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_t, 1)

206#define STM32\_PLL2\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), fracn)

207#define STM32\_PLL2\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll2), fracn, 1)

208#endif

209

210#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7\_pll\_clock, okay) || \

211 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32u5\_pll\_clock, okay) || \

212 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7rs\_pll\_clock, okay)

213#define STM32\_PLL3\_ENABLED 1

214#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

215#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

216#define STM32\_PLL3\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_p)

217#define STM32\_PLL3\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_p, 1)

218#define STM32\_PLL3\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_q)

219#define STM32\_PLL3\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_q, 1)

220#define STM32\_PLL3\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_r)

221#define STM32\_PLL3\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_r, 1)

222#define STM32\_PLL3\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_s)

223#define STM32\_PLL3\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_s, 1)

224#define STM32\_PLL3\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), fracn)

225#define STM32\_PLL3\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll3), fracn, 1)

226#endif

227

228#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f1\_pll\_clock, okay)

229#define STM32\_PLL\_ENABLED 1

230#define STM32\_PLL\_XTPRE DT\_PROP(DT\_NODELABEL(pll), xtpre)

231#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

232#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), usbpre)

233#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f0\_pll\_clock, okay) || \

234 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f100\_pll\_clock, okay) || \

235 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f105\_pll\_clock, okay)

236#define STM32\_PLL\_ENABLED 1

237#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

238#define STM32\_PLL\_PREDIV DT\_PROP(DT\_NODELABEL(pll), prediv)

239#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), otgfspre)

240#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l0\_pll\_clock, okay)

241#define STM32\_PLL\_ENABLED 1

242#define STM32\_PLL\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div)

243#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

244#endif

245

246#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32f105\_pll2\_clock, okay)

247#define STM32\_PLL2\_ENABLED 1

248#define STM32\_PLL2\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul)

249#define STM32\_PLL2\_PREDIV DT\_PROP(DT\_NODELABEL(pll2), prediv)

250#endif

251

253#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll)) && \

254 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), clocks)

255#define DT\_PLL\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll))

256#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

257#define STM32\_PLL\_SRC\_MSI 1

258#endif

259#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

260#define STM32\_PLL\_SRC\_MSIS 1

261#endif

262#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

263#define STM32\_PLL\_SRC\_HSI 1

264#endif

265#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

266#define STM32\_PLL\_SRC\_CSI 1

267#endif

268#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

269#define STM32\_PLL\_SRC\_HSE 1

270#endif

271#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(pll2))

272#define STM32\_PLL\_SRC\_PLL2 1

273#endif

274

275#endif

276

278#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll2)) && \

279 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), clocks)

280#define DT\_PLL2\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll2))

281#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

282#define STM32\_PLL2\_SRC\_MSIS 1

283#endif

284#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

285#define STM32\_PLL2\_SRC\_HSI 1

286#endif

287#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

288#define STM32\_PLL2\_SRC\_HSE 1

289#endif

290

291#endif

292

294#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll3)) && \

295 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), clocks)

296#define DT\_PLL3\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll3))

297#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

298#define STM32\_PLL3\_SRC\_MSIS 1

299#endif

300#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

301#define STM32\_PLL3\_SRC\_HSI 1

302#endif

303#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

304#define STM32\_PLL3\_SRC\_HSE 1

305#endif

306

307#endif

308

309

311

312#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), fixed\_clock, okay)

313#define STM32\_LSE\_ENABLED 1

314#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

315#define STM32\_LSE\_DRIVING 0

316#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

317#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), st\_stm32\_lse\_clock, okay)

318#define STM32\_LSE\_ENABLED 1

319#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

320#define STM32\_LSE\_DRIVING DT\_PROP(DT\_NODELABEL(clk\_lse), driving\_capability)

321#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

322#else

[ 323](stm32__clock__control_8h.md#a05b49e91f478558d33b2b862718758fa)#define STM32\_LSE\_ENABLED 0

[ 324](stm32__clock__control_8h.md#aedfe731de4f32e8dacd027bb115ca0e9)#define STM32\_LSE\_FREQ 0

[ 325](stm32__clock__control_8h.md#aead1c5c5ac685af96410f4883f7e988b)#define STM32\_LSE\_DRIVING 0

[ 326](stm32__clock__control_8h.md#a94745d7699b62ef9e7f8bbfbc6803727)#define STM32\_LSE\_BYPASS 0

327#endif

328

329#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay) || \

330 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32l0\_msi\_clock, okay)

331#define STM32\_MSI\_ENABLED 1

332#define STM32\_MSI\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_range)

333#endif

334

335#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay)

336#define STM32\_MSI\_ENABLED 1

337#define STM32\_MSI\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_pll\_mode)

338#endif

339

340#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msis), st\_stm32u5\_msi\_clock, okay)

341#define STM32\_MSIS\_ENABLED 1

342#define STM32\_MSIS\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_range)

343#define STM32\_MSIS\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_pll\_mode)

344#else

[ 345](stm32__clock__control_8h.md#a1a83a4c9a806689ac963e2ea8b142fda)#define STM32\_MSIS\_ENABLED 0

[ 346](stm32__clock__control_8h.md#a0109485d9cfd70782ce6aff604399330)#define STM32\_MSIS\_RANGE 0

[ 347](stm32__clock__control_8h.md#a02f0311b8e9c41a004ed355aff37a7b3)#define STM32\_MSIS\_PLL\_MODE 0

348#endif

349

350#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msik), st\_stm32u5\_msi\_clock, okay)

351#define STM32\_MSIK\_ENABLED 1

352#define STM32\_MSIK\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_range)

353#define STM32\_MSIK\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_pll\_mode)

354#else

[ 355](stm32__clock__control_8h.md#a379e09d2e380483155b0ef8cc39d490b)#define STM32\_MSIK\_ENABLED 0

[ 356](stm32__clock__control_8h.md#a2fb4bc355d7e69e6b676794d0ab4cbba)#define STM32\_MSIK\_RANGE 0

[ 357](stm32__clock__control_8h.md#a67d63326f5ebe1b249eb56b227aecb29)#define STM32\_MSIK\_PLL\_MODE 0

358#endif

359

360#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_csi), fixed\_clock, okay)

361#define STM32\_CSI\_ENABLED 1

362#define STM32\_CSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_csi), clock\_frequency)

363#else

[ 364](stm32__clock__control_8h.md#a2110dbb73ce08ba40555f1d95b50ce5c)#define STM32\_CSI\_FREQ 0

365#endif

366

367#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi), fixed\_clock, okay)

368#define STM32\_LSI\_ENABLED 1

369#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi), clock\_frequency)

370#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi1), fixed\_clock, okay)

371#define STM32\_LSI\_ENABLED 1

372#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi1), clock\_frequency)

373#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi2), fixed\_clock, okay)

374#define STM32\_LSI\_ENABLED 1

375#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi2), clock\_frequency)

376#else

[ 377](stm32__clock__control_8h.md#ae4ad7f2e4844901d753a91c1ba5c58c5)#define STM32\_LSI\_FREQ 0

378#endif

379

380#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), fixed\_clock, okay)

381#define STM32\_HSI\_DIV\_ENABLED 0

382#define STM32\_HSI\_ENABLED 1

383#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

384#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32h7\_hsi\_clock, okay) \

385 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32g0\_hsi\_clock, okay) \

386 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32c0\_hsi\_clock, okay)

387#define STM32\_HSI\_DIV\_ENABLED 1

388#define STM32\_HSI\_ENABLED 1

389#define STM32\_HSI\_DIVISOR DT\_PROP(DT\_NODELABEL(clk\_hsi), hsi\_div)

390#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

391#else

[ 392](stm32__clock__control_8h.md#aa67c0b4d532b58d78b12d36ae6817912)#define STM32\_HSI\_DIV\_ENABLED 0

[ 393](stm32__clock__control_8h.md#a2cc52c346227b2dfb91e1ab5aeda586c)#define STM32\_HSI\_DIVISOR 1

[ 394](stm32__clock__control_8h.md#af906386de1fde7ab0894971723a0a801)#define STM32\_HSI\_FREQ 0

395#endif

396

397#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), fixed\_clock, okay)

398#define STM32\_HSE\_ENABLED 1

399#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

400#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32\_hse\_clock, okay)

401#define STM32\_HSE\_ENABLED 1

402#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

403#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

404#define STM32\_HSE\_CSS DT\_PROP(DT\_NODELABEL(clk\_hse), css\_enabled)

405#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wl\_hse\_clock, okay)

406#define STM32\_HSE\_ENABLED 1

407#define STM32\_HSE\_TCXO DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_tcxo)

408#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

409#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

410#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wba\_hse\_clock, okay)

411#define STM32\_HSE\_ENABLED 1

412#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

413#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

414#else

[ 415](stm32__clock__control_8h.md#a7c3796ef481224c9e2f7516853677ec9)#define STM32\_HSE\_FREQ 0

416#endif

417

418#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), fixed\_clock, okay)

419#define STM32\_HSI48\_ENABLED 1

420#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

421#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), st\_stm32\_hsi48\_clock, okay)

422#define STM32\_HSI48\_ENABLED 1

423#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

424#define STM32\_HSI48\_CRS\_USB\_SOF DT\_PROP(DT\_NODELABEL(clk\_hsi48), crs\_usb\_sof)

425#endif

426

427#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(perck), st\_stm32\_clock\_mux, okay)

428#define STM32\_CKPER\_ENABLED 1

429#endif

430

432

[ 433](structstm32__pclken.md)struct [stm32\_pclken](structstm32__pclken.md) {

[ 434](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e);

[ 435](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf);

436};

437

439

[ 440](stm32__clock__control_8h.md#aa1b0949b4c58d57dcd2e979320cbed0a)#define STM32\_CLOCK\_INFO(clk\_index, node\_id) \

441 { \

442 .enr = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bits), \

443 .bus = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) \

444 }

[ 445](stm32__clock__control_8h.md#a9eb57b349f41edec11ff52a78015aea9)#define STM32\_DT\_CLOCKS(node\_id) \

446 { \

447 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

448 STM32\_CLOCK\_INFO, (,), node\_id) \

449 }

450

[ 451](stm32__clock__control_8h.md#a693176c2c60364d327aa5768ebfac185)#define STM32\_DT\_INST\_CLOCKS(inst) \

452 STM32\_DT\_CLOCKS(DT\_DRV\_INST(inst))

453

[ 454](stm32__clock__control_8h.md#a38559b31633eca5475b73b8a88df1fcd)#define STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT(inst) DT\_INST\_CLOCKS\_HAS\_IDX(inst, 1) ||

[ 455](stm32__clock__control_8h.md#aac932dfd992b11d479edf2a2d5e8de47)#define STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

456 (DT\_INST\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT) 0)

457

[ 458](stm32__clock__control_8h.md#a8743160d8765b466f8ac6a89efaa9dbc)#define STM32\_DOMAIN\_CLOCK\_SUPPORT(id) DT\_CLOCKS\_HAS\_IDX(DT\_NODELABEL(id), 1) ||

[ 459](stm32__clock__control_8h.md#a7951b8025683529eebdd415d6b65688b)#define STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

460 (DT\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_SUPPORT) 0)

461

463

[ 469](stm32__clock__control_8h.md#aaeece46c7eb50e1f095cc33f9f9c3475)#define STM32\_CLOCK\_REG\_GET(clock) \

470 (((clock) >> STM32\_CLOCK\_REG\_SHIFT) & STM32\_CLOCK\_REG\_MASK)

471

[ 477](stm32__clock__control_8h.md#a311bbc17ae04bf6fb648040255ed9af4)#define STM32\_CLOCK\_SHIFT\_GET(clock) \

478 (((clock) >> STM32\_CLOCK\_SHIFT\_SHIFT) & STM32\_CLOCK\_SHIFT\_MASK)

479

[ 485](stm32__clock__control_8h.md#ad3decf332c88ed6dd0f3deb22fdf559e)#define STM32\_CLOCK\_MASK\_GET(clock) \

486 (((clock) >> STM32\_CLOCK\_MASK\_SHIFT) & STM32\_CLOCK\_MASK\_MASK)

487

[ 493](stm32__clock__control_8h.md#ae4e06e6122c64ab7c4ccfadb4957a029)#define STM32\_CLOCK\_VAL\_GET(clock) \

494 (((clock) >> STM32\_CLOCK\_VAL\_SHIFT) & STM32\_CLOCK\_VAL\_MASK)

495

[ 501](stm32__clock__control_8h.md#aa10147ff5e9b937abef1f11b15d92901)#define STM32\_MCO\_CFGR\_REG\_GET(mco\_cfgr) \

502 (((mco\_cfgr) >> STM32\_MCO\_CFGR\_REG\_SHIFT) & STM32\_MCO\_CFGR\_REG\_MASK)

503

[ 509](stm32__clock__control_8h.md#a018b775433cbe5f53f4161d359d04bb5)#define STM32\_MCO\_CFGR\_SHIFT\_GET(mco\_cfgr) \

510 (((mco\_cfgr) >> STM32\_MCO\_CFGR\_SHIFT\_SHIFT) & STM32\_MCO\_CFGR\_SHIFT\_MASK)

511

[ 517](stm32__clock__control_8h.md#a22fcdb2be5108145090b65a2d90d4146)#define STM32\_MCO\_CFGR\_MASK\_GET(mco\_cfgr) \

518 (((mco\_cfgr) >> STM32\_MCO\_CFGR\_MASK\_SHIFT) & STM32\_MCO\_CFGR\_MASK\_MASK)

519

[ 525](stm32__clock__control_8h.md#a3503338c38db5b0939879395a97e0ac0)#define STM32\_MCO\_CFGR\_VAL\_GET(mco\_cfgr) \

526 (((mco\_cfgr) >> STM32\_MCO\_CFGR\_VAL\_SHIFT) & STM32\_MCO\_CFGR\_VAL\_MASK)

527

528#if defined(STM32\_HSE\_CSS)

537void stm32\_hse\_css\_callback(void);

538#endif

539

540#ifdef CONFIG\_SOC\_SERIES\_STM32WB0X

545typedef void (\*lsi\_update\_cb\_t)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) new\_lsi\_frequency);

546

558int stm32wb0\_register\_lsi\_update\_callback(lsi\_update\_cb\_t cb);

559#endif /\* CONFIG\_SOC\_SERIES\_STM32WB0X \*/

560

561#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[stm32\_clock.h](stm32__clock_8h.md)

[stm32c0\_clock.h](stm32c0__clock_8h.md)

[stm32f0\_clock.h](stm32f0__clock_8h.md)

[stm32f10x\_clock.h](stm32f10x__clock_8h.md)

[stm32f1\_clock.h](stm32f1__clock_8h.md)

[stm32f3\_clock.h](stm32f3__clock_8h.md)

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

[stm32u0\_clock.h](stm32u0__clock_8h.md)

[stm32u5\_clock.h](stm32u5__clock_8h.md)

[stm32wb0\_clock.h](stm32wb0__clock_8h.md)

[stm32wb\_clock.h](stm32wb__clock_8h.md)

[stm32wba\_clock.h](stm32wba__clock_8h.md)

[stm32wl\_clock.h](stm32wl__clock_8h.md)

[stm32\_pclken](structstm32__pclken.md)

Driver structure definition.

**Definition** stm32\_clock\_control.h:433

[stm32\_pclken::bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e)

uint32\_t bus

**Definition** stm32\_clock\_control.h:434

[stm32\_pclken::enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf)

uint32\_t enr

**Definition** stm32\_clock\_control.h:435

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [stm32\_clock\_control.h](stm32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
