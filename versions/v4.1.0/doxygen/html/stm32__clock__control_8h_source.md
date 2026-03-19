---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32__clock__control_8h_source.html
original_path: doxygen/html/stm32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

44#elif defined(CONFIG\_SOC\_SERIES\_STM32WBX)

45#include <[zephyr/dt-bindings/clock/stm32wb\_clock.h](stm32wb__clock_8h.md)>

46#elif defined(CONFIG\_SOC\_SERIES\_STM32WB0X)

47#include <[zephyr/dt-bindings/clock/stm32wb0\_clock.h](stm32wb0__clock_8h.md)>

48#elif defined(CONFIG\_SOC\_SERIES\_STM32WLX)

49#include <[zephyr/dt-bindings/clock/stm32wl\_clock.h](stm32wl__clock_8h.md)>

50#elif defined(CONFIG\_SOC\_SERIES\_STM32H5X)

51#include <[zephyr/dt-bindings/clock/stm32h5\_clock.h](stm32h5__clock_8h.md)>

52#elif defined(CONFIG\_SOC\_SERIES\_STM32H7X)

53#include <[zephyr/dt-bindings/clock/stm32h7\_clock.h](stm32h7__clock_8h.md)>

54#elif defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

55#include <[zephyr/dt-bindings/clock/stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)>

56#elif defined(CONFIG\_SOC\_SERIES\_STM32N6X)

57#include <[zephyr/dt-bindings/clock/stm32n6\_clock.h](stm32n6__clock_8h.md)>

58#elif defined(CONFIG\_SOC\_SERIES\_STM32U0X)

59#include <[zephyr/dt-bindings/clock/stm32u0\_clock.h](stm32u0__clock_8h.md)>

60#elif defined(CONFIG\_SOC\_SERIES\_STM32U5X)

61#include <[zephyr/dt-bindings/clock/stm32u5\_clock.h](stm32u5__clock_8h.md)>

62#elif defined(CONFIG\_SOC\_SERIES\_STM32WBAX)

63#include <[zephyr/dt-bindings/clock/stm32wba\_clock.h](stm32wba__clock_8h.md)>

64#else

65#include <[zephyr/dt-bindings/clock/stm32\_clock.h](stm32__clock_8h.md)>

66#endif

67

[ 69](stm32__clock__control_8h.md#ad33dc3d92546f9a4162a65a06ac6c673)#define STM32\_CLOCK\_CONTROL\_NODE DT\_NODELABEL(rcc)

70

72

[ 73](stm32__clock__control_8h.md#a38a0117c88924c6e1beca37e6cdea56b)#define STM32\_AHB\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

[ 74](stm32__clock__control_8h.md#a7af7ec37fc9d13d8d3bd6c3193ac8660)#define STM32\_APB1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb1\_prescaler)

[ 75](stm32__clock__control_8h.md#ad82f77d7d85845342bfa613557b1f569)#define STM32\_APB2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb2\_prescaler)

[ 76](stm32__clock__control_8h.md#ad1ffa671b55ad88e624ed9b7c4a22839)#define STM32\_APB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb3\_prescaler)

[ 77](stm32__clock__control_8h.md#adf8be1edd443c074679ad6b2ae7d19ed)#define STM32\_APB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb4\_prescaler)

[ 78](stm32__clock__control_8h.md#aa3510cdd90c9cc8b34933954f6e71caa)#define STM32\_APB5\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb5\_prescaler)

[ 79](stm32__clock__control_8h.md#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)#define STM32\_APB7\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb7\_prescaler)

[ 80](stm32__clock__control_8h.md#afca170bc72a77d8905b6c2ca0cce9e7b)#define STM32\_AHB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

[ 81](stm32__clock__control_8h.md#a3da9fd6fe11ceb8c2225e43eb2556d2d)#define STM32\_AHB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

[ 82](stm32__clock__control_8h.md#aeb1fabf85560ccd6cc1c0bdb34c86ec2)#define STM32\_AHB5\_PRESCALER DT\_PROP\_OR(DT\_NODELABEL(rcc), ahb5\_prescaler, 1)

[ 83](stm32__clock__control_8h.md#a18dc4749249030d371007b5135f5af54)#define STM32\_CPU1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

[ 84](stm32__clock__control_8h.md#a4f1975635dc6244f98263636c44f3942)#define STM32\_CPU2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu2\_prescaler)

85

86#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

87#define STM32\_CORE\_PRESCALER STM32\_AHB\_PRESCALER

88#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

89#define STM32\_CORE\_PRESCALER STM32\_CPU1\_PRESCALER

90#endif

91

92#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

93#define STM32\_FLASH\_PRESCALER STM32\_AHB3\_PRESCALER

94#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

95#define STM32\_FLASH\_PRESCALER STM32\_AHB4\_PRESCALER

96#else

[ 97](stm32__clock__control_8h.md#ac3274b70aee7aff6282eaa77ca819f27)#define STM32\_FLASH\_PRESCALER STM32\_CORE\_PRESCALER

98#endif

99

[ 100](stm32__clock__control_8h.md#a29ef6b98c22a522cde9f7dab5b11ace0)#define STM32\_ADC\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc\_prescaler)

[ 101](stm32__clock__control_8h.md#a35954cadc11af5ee499918be312acf38)#define STM32\_ADC12\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc12\_prescaler)

[ 102](stm32__clock__control_8h.md#a1cae4646086d8f855b72d55fee1483ad)#define STM32\_ADC34\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc34\_prescaler)

103

105#if defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

106#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), dcpre)

107#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

108#define STM32\_PPRE1 DT\_PROP(DT\_NODELABEL(rcc), ppre1)

109#define STM32\_PPRE2 DT\_PROP(DT\_NODELABEL(rcc), ppre2)

110#define STM32\_PPRE4 DT\_PROP(DT\_NODELABEL(rcc), ppre4)

111#define STM32\_PPRE5 DT\_PROP(DT\_NODELABEL(rcc), ppre5)

112#else

[ 113](stm32__clock__control_8h.md#a51967fd4dcf9ec8fe8e7250b5af32c87)#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), d1cpre)

[ 114](stm32__clock__control_8h.md#a035ea0d8259c0f89306c6a7d344705f2)#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

[ 115](stm32__clock__control_8h.md#a844064bd8ccafb5df4bf02748840491d)#define STM32\_D2PPRE1 DT\_PROP(DT\_NODELABEL(rcc), d2ppre1)

[ 116](stm32__clock__control_8h.md#a50394a7e040433c738fc7e9f03b7aff3)#define STM32\_D2PPRE2 DT\_PROP(DT\_NODELABEL(rcc), d2ppre2)

[ 117](stm32__clock__control_8h.md#a02a098a3296751f55ea349faecff7bd5)#define STM32\_D1PPRE DT\_PROP(DT\_NODELABEL(rcc), d1ppre)

[ 118](stm32__clock__control_8h.md#a9dd9b0e8ef84e6ff033a707b2a0ec231)#define STM32\_D3PPRE DT\_PROP(DT\_NODELABEL(rcc), d3ppre)

119#endif /\* CONFIG\_SOC\_SERIES\_STM32H7RSX \*/

120

[ 122](stm32__clock__control_8h.md#aea3d7b8e3adedef5f93cdb38852a8097)#define STM32\_AHB5\_DIV DT\_PROP(DT\_NODELABEL(rcc), ahb5\_div)

123

[ 124](stm32__clock__control_8h.md#ad9bff8a9cfbe0dbe0db73d077cb7a227)#define DT\_RCC\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(rcc))

125

126/\* To enable use of IS\_ENABLED utility macro, these symbols

127 \* should not be defined directly using DT\_SAME\_NODE.

128 \*/

129#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(pll))

130#define STM32\_SYSCLK\_SRC\_PLL 1

131#endif

132#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

133#define STM32\_SYSCLK\_SRC\_HSI 1

134#endif

135#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

136#define STM32\_SYSCLK\_SRC\_HSE 1

137#endif

138#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

139#define STM32\_SYSCLK\_SRC\_MSI 1

140#endif

141#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

142#define STM32\_SYSCLK\_SRC\_MSIS 1

143#endif

144#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

145#define STM32\_SYSCLK\_SRC\_CSI 1

146#endif

147#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(ic2))

148#define STM32\_SYSCLK\_SRC\_IC2 1

149#endif

150

151

153

154#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f2\_pll\_clock, okay) || \

155 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f4\_pll\_clock, okay) || \

156 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f7\_pll\_clock, okay) || \

157 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g0\_pll\_clock, okay) || \

158 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g4\_pll\_clock, okay) || \

159 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l4\_pll\_clock, okay) || \

160 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u0\_pll\_clock, okay) || \

161 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u5\_pll\_clock, okay) || \

162 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wb\_pll\_clock, okay) || \

163 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wba\_pll\_clock, okay) || \

164 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7\_pll\_clock, okay) || \

165 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7rs\_pll\_clock, okay)

166#define STM32\_PLL\_ENABLED 1

167#define STM32\_PLL\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div\_m)

168#define STM32\_PLL\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul\_n)

169#define STM32\_PLL\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_p)

170#define STM32\_PLL\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_p, 1)

171#define STM32\_PLL\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_q)

172#define STM32\_PLL\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_q, 1)

173#define STM32\_PLL\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_r)

174#define STM32\_PLL\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_r, 1)

175#define STM32\_PLL\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_s)

176#define STM32\_PLL\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_s, 1)

177#define STM32\_PLL\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), fracn)

178#define STM32\_PLL\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll), fracn, 1)

179#endif

180

181#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f4\_plli2s\_clock, okay)

182#define STM32\_PLLI2S\_ENABLED 1

183#define STM32\_PLLI2S\_M\_DIVISOR STM32\_PLL\_M\_DIVISOR

184#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

185#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

186#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

187#endif

188

189#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f411\_plli2s\_clock, okay)

190#define STM32\_PLLI2S\_ENABLED 1

191#define STM32\_PLLI2S\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(plli2s), div\_m)

192#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

193#define STM32\_PLLI2S\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_q)

194#define STM32\_PLLI2S\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_q, 1)

195#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

196#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

197#endif

198

199#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32u5\_pll\_clock, okay) || \

200 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7\_pll\_clock, okay) || \

201 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7rs\_pll\_clock, okay)

202#define STM32\_PLL2\_ENABLED 1

203#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

204#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

205#define STM32\_PLL2\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_p)

206#define STM32\_PLL2\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_p, 1)

207#define STM32\_PLL2\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_q)

208#define STM32\_PLL2\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_q, 1)

209#define STM32\_PLL2\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_r)

210#define STM32\_PLL2\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_r, 1)

211#define STM32\_PLL2\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_s)

212#define STM32\_PLL2\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_s, 1)

213#define STM32\_PLL2\_T\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_t)

214#define STM32\_PLL2\_T\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_t, 1)

215#define STM32\_PLL2\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), fracn)

216#define STM32\_PLL2\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll2), fracn, 1)

217#endif

218

219#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7\_pll\_clock, okay) || \

220 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32u5\_pll\_clock, okay) || \

221 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7rs\_pll\_clock, okay)

222#define STM32\_PLL3\_ENABLED 1

223#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

224#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

225#define STM32\_PLL3\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_p)

226#define STM32\_PLL3\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_p, 1)

227#define STM32\_PLL3\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_q)

228#define STM32\_PLL3\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_q, 1)

229#define STM32\_PLL3\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_r)

230#define STM32\_PLL3\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_r, 1)

231#define STM32\_PLL3\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_s)

232#define STM32\_PLL3\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_s, 1)

233#define STM32\_PLL3\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), fracn)

234#define STM32\_PLL3\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll3), fracn, 1)

235#endif

236

237#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f1\_pll\_clock, okay)

238#define STM32\_PLL\_ENABLED 1

239#define STM32\_PLL\_XTPRE DT\_PROP(DT\_NODELABEL(pll), xtpre)

240#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

241#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), usbpre)

242#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f0\_pll\_clock, okay) || \

243 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f100\_pll\_clock, okay) || \

244 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f105\_pll\_clock, okay)

245#define STM32\_PLL\_ENABLED 1

246#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

247#define STM32\_PLL\_PREDIV DT\_PROP(DT\_NODELABEL(pll), prediv)

248#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), otgfspre)

249#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l0\_pll\_clock, okay)

250#define STM32\_PLL\_ENABLED 1

251#define STM32\_PLL\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div)

252#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

253#endif

254

255#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32f105\_pll2\_clock, okay)

256#define STM32\_PLL2\_ENABLED 1

257#define STM32\_PLL2\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul)

258#define STM32\_PLL2\_PREDIV DT\_PROP(DT\_NODELABEL(pll2), prediv)

259#endif

260

261#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll1), st\_stm32n6\_pll\_clock, okay)

262#define STM32\_PLL1\_ENABLED 1

263#define STM32\_PLL1\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll1), div\_m)

264#define STM32\_PLL1\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll1), mul\_n)

265#define STM32\_PLL1\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll1), div\_p1)

266#define STM32\_PLL1\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll1), div\_p2)

267#endif

268

269#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32n6\_pll\_clock, okay)

270#define STM32\_PLL2\_ENABLED 1

271#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

272#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

273#define STM32\_PLL2\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_p1)

274#define STM32\_PLL2\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_p2)

275#endif

276

277#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32n6\_pll\_clock, okay)

278#define STM32\_PLL3\_ENABLED 1

279#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

280#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

281#define STM32\_PLL3\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_p1)

282#define STM32\_PLL3\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_p2)

283#endif

284

285#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll4), st\_stm32n6\_pll\_clock, okay)

286#define STM32\_PLL4\_ENABLED 1

287#define STM32\_PLL4\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_m)

288#define STM32\_PLL4\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll4), mul\_n)

289#define STM32\_PLL4\_P1\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_p1)

290#define STM32\_PLL4\_P2\_DIVISOR DT\_PROP(DT\_NODELABEL(pll4), div\_p2)

291#endif

292

294#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll)) && \

295 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), clocks)

296#define DT\_PLL\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll))

297#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

298#define STM32\_PLL\_SRC\_MSI 1

299#endif

300#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

301#define STM32\_PLL\_SRC\_MSIS 1

302#endif

303#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

304#define STM32\_PLL\_SRC\_HSI 1

305#endif

306#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

307#define STM32\_PLL\_SRC\_CSI 1

308#endif

309#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

310#define STM32\_PLL\_SRC\_HSE 1

311#endif

312#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(pll2))

313#define STM32\_PLL\_SRC\_PLL2 1

314#endif

315

316#endif

317

319#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll2)) && \

320 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), clocks)

321#define DT\_PLL2\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll2))

322#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

323#define STM32\_PLL2\_SRC\_MSI 1

324#endif

325#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

326#define STM32\_PLL2\_SRC\_MSIS 1

327#endif

328#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

329#define STM32\_PLL2\_SRC\_HSI 1

330#endif

331#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

332#define STM32\_PLL2\_SRC\_HSE 1

333#endif

334

335#endif

336

338#if DT\_NODE\_HAS\_STATUS\_OKAY(DT\_NODELABEL(pll3)) && \

339 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), clocks)

340#define DT\_PLL3\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll3))

341#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

342#define STM32\_PLL3\_SRC\_MSI 1

343#endif

344#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

345#define STM32\_PLL3\_SRC\_MSIS 1

346#endif

347#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

348#define STM32\_PLL3\_SRC\_HSI 1

349#endif

350#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

351#define STM32\_PLL3\_SRC\_HSE 1

352#endif

353

354#endif

355

357#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll4), okay) && \

358 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll4), clocks)

359#define DT\_PLL4\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll4))

360#if DT\_SAME\_NODE(DT\_PLL4\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

361#define STM32\_PLL4\_SRC\_MSI 1

362#endif

363#if DT\_SAME\_NODE(DT\_PLL4\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

364#define STM32\_PLL4\_SRC\_HSI 1

365#endif

366#if DT\_SAME\_NODE(DT\_PLL4\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

367#define STM32\_PLL4\_SRC\_HSE 1

368#endif

369

370#endif

371

372

374

375#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), fixed\_clock, okay)

376#define STM32\_LSE\_ENABLED 1

377#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

378#define STM32\_LSE\_DRIVING 0

379#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

380#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), st\_stm32\_lse\_clock, okay)

381#define STM32\_LSE\_ENABLED 1

382#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

383#define STM32\_LSE\_DRIVING DT\_PROP(DT\_NODELABEL(clk\_lse), driving\_capability)

384#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

385#else

[ 386](stm32__clock__control_8h.md#a05b49e91f478558d33b2b862718758fa)#define STM32\_LSE\_ENABLED 0

[ 387](stm32__clock__control_8h.md#aedfe731de4f32e8dacd027bb115ca0e9)#define STM32\_LSE\_FREQ 0

[ 388](stm32__clock__control_8h.md#aead1c5c5ac685af96410f4883f7e988b)#define STM32\_LSE\_DRIVING 0

[ 389](stm32__clock__control_8h.md#a94745d7699b62ef9e7f8bbfbc6803727)#define STM32\_LSE\_BYPASS 0

390#endif

391

392#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay) || \

393 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32l0\_msi\_clock, okay)

394#define STM32\_MSI\_ENABLED 1

395#define STM32\_MSI\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_range)

396#endif

397

398#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay)

399#define STM32\_MSI\_ENABLED 1

400#define STM32\_MSI\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_pll\_mode)

401#endif

402

403#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msis), st\_stm32u5\_msi\_clock, okay)

404#define STM32\_MSIS\_ENABLED 1

405#define STM32\_MSIS\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_range)

406#define STM32\_MSIS\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_pll\_mode)

407#else

[ 408](stm32__clock__control_8h.md#a1a83a4c9a806689ac963e2ea8b142fda)#define STM32\_MSIS\_ENABLED 0

[ 409](stm32__clock__control_8h.md#a0109485d9cfd70782ce6aff604399330)#define STM32\_MSIS\_RANGE 0

[ 410](stm32__clock__control_8h.md#a02f0311b8e9c41a004ed355aff37a7b3)#define STM32\_MSIS\_PLL\_MODE 0

411#endif

412

413#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msik), st\_stm32u5\_msi\_clock, okay)

414#define STM32\_MSIK\_ENABLED 1

415#define STM32\_MSIK\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_range)

416#define STM32\_MSIK\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_pll\_mode)

417#else

[ 418](stm32__clock__control_8h.md#a379e09d2e380483155b0ef8cc39d490b)#define STM32\_MSIK\_ENABLED 0

[ 419](stm32__clock__control_8h.md#a2fb4bc355d7e69e6b676794d0ab4cbba)#define STM32\_MSIK\_RANGE 0

[ 420](stm32__clock__control_8h.md#a67d63326f5ebe1b249eb56b227aecb29)#define STM32\_MSIK\_PLL\_MODE 0

421#endif

422

423#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_csi), fixed\_clock, okay)

424#define STM32\_CSI\_ENABLED 1

425#define STM32\_CSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_csi), clock\_frequency)

426#else

[ 427](stm32__clock__control_8h.md#a2110dbb73ce08ba40555f1d95b50ce5c)#define STM32\_CSI\_FREQ 0

428#endif

429

430#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi), fixed\_clock, okay)

431#define STM32\_LSI\_ENABLED 1

432#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi), clock\_frequency)

433#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi1), fixed\_clock, okay)

434#define STM32\_LSI\_ENABLED 1

435#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi1), clock\_frequency)

436#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi2), fixed\_clock, okay)

437#define STM32\_LSI\_ENABLED 1

438#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi2), clock\_frequency)

439#else

[ 440](stm32__clock__control_8h.md#ae4ad7f2e4844901d753a91c1ba5c58c5)#define STM32\_LSI\_FREQ 0

441#endif

442

443#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), fixed\_clock, okay)

444#define STM32\_HSI\_DIV\_ENABLED 0

445#define STM32\_HSI\_ENABLED 1

446#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

447#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32h7\_hsi\_clock, okay) \

448 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32g0\_hsi\_clock, okay) \

449 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32c0\_hsi\_clock, okay)

450#define STM32\_HSI\_DIV\_ENABLED 1

451#define STM32\_HSI\_ENABLED 1

452#define STM32\_HSI\_DIVISOR DT\_PROP(DT\_NODELABEL(clk\_hsi), hsi\_div)

453#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

454#else

[ 455](stm32__clock__control_8h.md#aa67c0b4d532b58d78b12d36ae6817912)#define STM32\_HSI\_DIV\_ENABLED 0

[ 456](stm32__clock__control_8h.md#a2cc52c346227b2dfb91e1ab5aeda586c)#define STM32\_HSI\_DIVISOR 1

[ 457](stm32__clock__control_8h.md#af906386de1fde7ab0894971723a0a801)#define STM32\_HSI\_FREQ 0

458#endif

459

460#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), fixed\_clock, okay)

461#define STM32\_HSE\_ENABLED 1

462#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

463#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32\_hse\_clock, okay)

464#define STM32\_HSE\_ENABLED 1

465#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

466#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

467#define STM32\_HSE\_CSS DT\_PROP(DT\_NODELABEL(clk\_hse), css\_enabled)

468#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wl\_hse\_clock, okay)

469#define STM32\_HSE\_ENABLED 1

470#define STM32\_HSE\_TCXO DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_tcxo)

471#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

472#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

473#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wba\_hse\_clock, okay)

474#define STM32\_HSE\_ENABLED 1

475#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

476#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

477#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32n6\_hse\_clock, okay)

478#define STM32\_HSE\_ENABLED 1

479#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

480#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

481#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

482#else

[ 483](stm32__clock__control_8h.md#a7c3796ef481224c9e2f7516853677ec9)#define STM32\_HSE\_FREQ 0

484#endif

485

486#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), fixed\_clock, okay)

487#define STM32\_HSI48\_ENABLED 1

488#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

489#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), st\_stm32\_hsi48\_clock, okay)

490#define STM32\_HSI48\_ENABLED 1

491#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

492#define STM32\_HSI48\_CRS\_USB\_SOF DT\_PROP(DT\_NODELABEL(clk\_hsi48), crs\_usb\_sof)

493#endif

494

495#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(perck), st\_stm32\_clock\_mux, okay)

496#define STM32\_CKPER\_ENABLED 1

497#endif

498

499#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(cpusw), st\_stm32\_clock\_mux, okay)

500#define STM32\_CPUSW\_ENABLED 1

501#endif

502

503#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic1), st\_stm32n6\_ic\_clock\_mux, okay)

504#define STM32\_IC1\_ENABLED 1

505#define STM32\_IC1\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic1), pll\_src)

506#define STM32\_IC1\_DIV DT\_PROP(DT\_NODELABEL(ic1), ic\_div)

507#endif

508

509#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic2), st\_stm32n6\_ic\_clock\_mux, okay)

510#define STM32\_IC2\_ENABLED 1

511#define STM32\_IC2\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic2), pll\_src)

512#define STM32\_IC2\_DIV DT\_PROP(DT\_NODELABEL(ic2), ic\_div)

513#endif

514

515#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic3), st\_stm32n6\_ic\_clock\_mux, okay)

516#define STM32\_IC3\_ENABLED 1

517#define STM32\_IC3\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic3), pll\_src)

518#define STM32\_IC3\_DIV DT\_PROP(DT\_NODELABEL(ic3), ic\_div)

519#endif

520

521#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic4), st\_stm32n6\_ic\_clock\_mux, okay)

522#define STM32\_IC4\_ENABLED 1

523#define STM32\_IC4\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic4), pll\_src)

524#define STM32\_IC4\_DIV DT\_PROP(DT\_NODELABEL(ic4), ic\_div)

525#endif

526

527#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic5), st\_stm32n6\_ic\_clock\_mux, okay)

528#define STM32\_IC5\_ENABLED 1

529#define STM32\_IC5\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic5), pll\_src)

530#define STM32\_IC5\_DIV DT\_PROP(DT\_NODELABEL(ic5), ic\_div)

531#endif

532

533#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic6), st\_stm32n6\_ic\_clock\_mux, okay)

534#define STM32\_IC6\_ENABLED 1

535#define STM32\_IC6\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic6), pll\_src)

536#define STM32\_IC6\_DIV DT\_PROP(DT\_NODELABEL(ic6), ic\_div)

537#endif

538

539#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic7), st\_stm32n6\_ic\_clock\_mux, okay)

540#define STM32\_IC7\_ENABLED 1

541#define STM32\_IC7\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic7), pll\_src)

542#define STM32\_IC7\_DIV DT\_PROP(DT\_NODELABEL(ic7), ic\_div)

543#endif

544

545#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic8), st\_stm32n6\_ic\_clock\_mux, okay)

546#define STM32\_IC8\_ENABLED 1

547#define STM32\_IC8\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic8), pll\_src)

548#define STM32\_IC8\_DIV DT\_PROP(DT\_NODELABEL(ic8), ic\_div)

549#endif

550

551#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic9), st\_stm32n6\_ic\_clock\_mux, okay)

552#define STM32\_IC9\_ENABLED 1

553#define STM32\_IC9\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic9), pll\_src)

554#define STM32\_IC9\_DIV DT\_PROP(DT\_NODELABEL(ic9), ic\_div)

555#endif

556

557#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic10), st\_stm32n6\_ic\_clock\_mux, okay)

558#define STM32\_IC10\_ENABLED 1

559#define STM32\_IC10\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic10), pll\_src)

560#define STM32\_IC10\_DIV DT\_PROP(DT\_NODELABEL(ic10), ic\_div)

561#endif

562

563#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic11), st\_stm32n6\_ic\_clock\_mux, okay)

564#define STM32\_IC11\_ENABLED 1

565#define STM32\_IC11\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic11), pll\_src)

566#define STM32\_IC11\_DIV DT\_PROP(DT\_NODELABEL(ic11), ic\_div)

567#endif

568

569#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic12), st\_stm32n6\_ic\_clock\_mux, okay)

570#define STM32\_IC12\_ENABLED 1

571#define STM32\_IC12\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic12), pll\_src)

572#define STM32\_IC12\_DIV DT\_PROP(DT\_NODELABEL(ic12), ic\_div)

573#endif

574

575#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic13), st\_stm32n6\_ic\_clock\_mux, okay)

576#define STM32\_IC13\_ENABLED 1

577#define STM32\_IC13\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic13), pll\_src)

578#define STM32\_IC13\_DIV DT\_PROP(DT\_NODELABEL(ic13), ic\_div)

579#endif

580

581#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic14), st\_stm32n6\_ic\_clock\_mux, okay)

582#define STM32\_IC14\_ENABLED 1

583#define STM32\_IC14\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic14), pll\_src)

584#define STM32\_IC14\_DIV DT\_PROP(DT\_NODELABEL(ic14), ic\_div)

585#endif

586

587#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic15), st\_stm32n6\_ic\_clock\_mux, okay)

588#define STM32\_IC15\_ENABLED 1

589#define STM32\_IC15\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic15), pll\_src)

590#define STM32\_IC15\_DIV DT\_PROP(DT\_NODELABEL(ic15), ic\_div)

591#endif

592

593#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic16), st\_stm32n6\_ic\_clock\_mux, okay)

594#define STM32\_IC16\_ENABLED 1

595#define STM32\_IC16\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic16), pll\_src)

596#define STM32\_IC16\_DIV DT\_PROP(DT\_NODELABEL(ic16), ic\_div)

597#endif

598

599#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic17), st\_stm32n6\_ic\_clock\_mux, okay)

600#define STM32\_IC17\_ENABLED 1

601#define STM32\_IC17\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic17), pll\_src)

602#define STM32\_IC17\_DIV DT\_PROP(DT\_NODELABEL(ic17), ic\_div)

603#endif

604

605#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic18), st\_stm32n6\_ic\_clock\_mux, okay)

606#define STM32\_IC18\_ENABLED 1

607#define STM32\_IC18\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic18), pll\_src)

608#define STM32\_IC18\_DIV DT\_PROP(DT\_NODELABEL(ic18), ic\_div)

609#endif

610

611#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic19), st\_stm32n6\_ic\_clock\_mux, okay)

612#define STM32\_IC19\_ENABLED 1

613#define STM32\_IC19\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic19), pll\_src)

614#define STM32\_IC19\_DIV DT\_PROP(DT\_NODELABEL(ic19), ic\_div)

615#endif

616

617#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(ic20), st\_stm32n6\_ic\_clock\_mux, okay)

618#define STM32\_IC20\_ENABLED 1

619#define STM32\_IC20\_PLL\_SRC DT\_PROP(DT\_NODELABEL(ic20), pll\_src)

620#define STM32\_IC20\_DIV DT\_PROP(DT\_NODELABEL(ic20), ic\_div)

621#endif

622

624

[ 625](structstm32__pclken.md)struct [stm32\_pclken](structstm32__pclken.md) {

[ 626](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) : [STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0);

[ 627](structstm32__pclken.md#a38e8d02b1a7117115e7fa0405ed10cc4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [div](structstm32__pclken.md#a38e8d02b1a7117115e7fa0405ed10cc4) : (32 - [STM32\_CLOCK\_DIV\_SHIFT](stm32__clock_8h.md#a208c97071646d6a363fa8abcd44908f0));

[ 628](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf);

629};

630

632

[ 633](stm32__clock__control_8h.md#aa1b0949b4c58d57dcd2e979320cbed0a)#define STM32\_CLOCK\_INFO(clk\_index, node\_id) \

634 { \

635 .enr = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bits), \

636 .bus = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) & \

637 GENMASK(STM32\_CLOCK\_DIV\_SHIFT - 1, 0), \

638 .div = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) >> \

639 STM32\_CLOCK\_DIV\_SHIFT, \

640 }

[ 641](stm32__clock__control_8h.md#a9eb57b349f41edec11ff52a78015aea9)#define STM32\_DT\_CLOCKS(node\_id) \

642 { \

643 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

644 STM32\_CLOCK\_INFO, (,), node\_id) \

645 }

646

[ 647](stm32__clock__control_8h.md#a693176c2c60364d327aa5768ebfac185)#define STM32\_DT\_INST\_CLOCKS(inst) \

648 STM32\_DT\_CLOCKS(DT\_DRV\_INST(inst))

649

[ 650](stm32__clock__control_8h.md#a38559b31633eca5475b73b8a88df1fcd)#define STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT(inst) DT\_INST\_CLOCKS\_HAS\_IDX(inst, 1) ||

[ 651](stm32__clock__control_8h.md#aac932dfd992b11d479edf2a2d5e8de47)#define STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

652 (DT\_INST\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT) 0)

653

[ 654](stm32__clock__control_8h.md#a8743160d8765b466f8ac6a89efaa9dbc)#define STM32\_DOMAIN\_CLOCK\_SUPPORT(id) DT\_CLOCKS\_HAS\_IDX(DT\_NODELABEL(id), 1) ||

[ 655](stm32__clock__control_8h.md#a7951b8025683529eebdd415d6b65688b)#define STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

656 (DT\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_SUPPORT) 0)

657

659

[ 665](stm32__clock__control_8h.md#a932d2b05943fc3511f0ad82f4e10c98a)#define STM32\_DT\_CLKSEL\_REG\_GET(clock) \

666 (((clock) >> STM32\_DT\_CLKSEL\_REG\_SHIFT) & STM32\_DT\_CLKSEL\_REG\_MASK)

667

[ 673](stm32__clock__control_8h.md#a721bbde6ed4c76019fba67677e359c05)#define STM32\_DT\_CLKSEL\_SHIFT\_GET(clock) \

674 (((clock) >> STM32\_DT\_CLKSEL\_SHIFT\_SHIFT) & STM32\_DT\_CLKSEL\_SHIFT\_MASK)

675

[ 681](stm32__clock__control_8h.md#ad2c6955f07a96ff6ffecf2b1b267de2c)#define STM32\_DT\_CLKSEL\_MASK\_GET(clock) \

682 (((clock) >> STM32\_DT\_CLKSEL\_MASK\_SHIFT) & STM32\_DT\_CLKSEL\_MASK\_MASK)

683

[ 689](stm32__clock__control_8h.md#aecf915cbdbf64d743b6ccb020a905abe)#define STM32\_DT\_CLKSEL\_VAL\_GET(clock) \

690 (((clock) >> STM32\_DT\_CLKSEL\_VAL\_SHIFT) & STM32\_DT\_CLKSEL\_VAL\_MASK)

691

692#if defined(STM32\_HSE\_CSS)

701void stm32\_hse\_css\_callback(void);

702#endif

703

704#ifdef CONFIG\_SOC\_SERIES\_STM32WB0X

709typedef void (\*lsi\_update\_cb\_t)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) new\_lsi\_frequency);

710

722int stm32wb0\_register\_lsi\_update\_callback(lsi\_update\_cb\_t cb);

723#endif /\* CONFIG\_SOC\_SERIES\_STM32WB0X \*/

724

725#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_ \*/

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

[stm32n6\_clock.h](stm32n6__clock_8h.md)

[stm32u0\_clock.h](stm32u0__clock_8h.md)

[stm32u5\_clock.h](stm32u5__clock_8h.md)

[stm32wb0\_clock.h](stm32wb0__clock_8h.md)

[stm32wb\_clock.h](stm32wb__clock_8h.md)

[stm32wba\_clock.h](stm32wba__clock_8h.md)

[stm32wl\_clock.h](stm32wl__clock_8h.md)

[stm32\_pclken](structstm32__pclken.md)

Driver structure definition.

**Definition** stm32\_clock\_control.h:625

[stm32\_pclken::div](structstm32__pclken.md#a38e8d02b1a7117115e7fa0405ed10cc4)

uint32\_t div

**Definition** stm32\_clock\_control.h:627

[stm32\_pclken::bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e)

uint32\_t bus

**Definition** stm32\_clock\_control.h:626

[stm32\_pclken::enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf)

uint32\_t enr

**Definition** stm32\_clock\_control.h:628

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [stm32\_clock\_control.h](stm32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
