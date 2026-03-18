---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32__clock__control_8h_source.html
original_path: doxygen/html/stm32__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

47#elif defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

48#include <[zephyr/dt-bindings/clock/stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)>

49#elif defined(CONFIG\_SOC\_SERIES\_STM32U5X)

50#include <[zephyr/dt-bindings/clock/stm32u5\_clock.h](stm32u5__clock_8h.md)>

51#elif defined(CONFIG\_SOC\_SERIES\_STM32WBAX)

52#include <[zephyr/dt-bindings/clock/stm32wba\_clock.h](stm32wba__clock_8h.md)>

53#else

54#include <[zephyr/dt-bindings/clock/stm32\_clock.h](stm32__clock_8h.md)>

55#endif

56

[ 58](stm32__clock__control_8h.md#ad33dc3d92546f9a4162a65a06ac6c673)#define STM32\_CLOCK\_CONTROL\_NODE DT\_NODELABEL(rcc)

59

61

[ 62](stm32__clock__control_8h.md#a38a0117c88924c6e1beca37e6cdea56b)#define STM32\_AHB\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

[ 63](stm32__clock__control_8h.md#a7af7ec37fc9d13d8d3bd6c3193ac8660)#define STM32\_APB1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb1\_prescaler)

[ 64](stm32__clock__control_8h.md#ad82f77d7d85845342bfa613557b1f569)#define STM32\_APB2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb2\_prescaler)

[ 65](stm32__clock__control_8h.md#ad1ffa671b55ad88e624ed9b7c4a22839)#define STM32\_APB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb3\_prescaler)

[ 66](stm32__clock__control_8h.md#aa3510cdd90c9cc8b34933954f6e71caa)#define STM32\_APB5\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb5\_prescaler)

[ 67](stm32__clock__control_8h.md#a5b3ff33cd4a1ac4c8acfbe1ca921b9c3)#define STM32\_APB7\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), apb7\_prescaler)

[ 68](stm32__clock__control_8h.md#afca170bc72a77d8905b6c2ca0cce9e7b)#define STM32\_AHB3\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

[ 69](stm32__clock__control_8h.md#a3da9fd6fe11ceb8c2225e43eb2556d2d)#define STM32\_AHB4\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

[ 70](stm32__clock__control_8h.md#aeb1fabf85560ccd6cc1c0bdb34c86ec2)#define STM32\_AHB5\_PRESCALER DT\_PROP\_OR(DT\_NODELABEL(rcc), ahb5\_prescaler, 1)

[ 71](stm32__clock__control_8h.md#a18dc4749249030d371007b5135f5af54)#define STM32\_CPU1\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

[ 72](stm32__clock__control_8h.md#a4f1975635dc6244f98263636c44f3942)#define STM32\_CPU2\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), cpu2\_prescaler)

73

74#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb\_prescaler)

75#define STM32\_CORE\_PRESCALER STM32\_AHB\_PRESCALER

76#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), cpu1\_prescaler)

77#define STM32\_CORE\_PRESCALER STM32\_CPU1\_PRESCALER

78#endif

79

80#if DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb3\_prescaler)

81#define STM32\_FLASH\_PRESCALER STM32\_AHB3\_PRESCALER

82#elif DT\_NODE\_HAS\_PROP(DT\_NODELABEL(rcc), ahb4\_prescaler)

83#define STM32\_FLASH\_PRESCALER STM32\_AHB4\_PRESCALER

84#else

[ 85](stm32__clock__control_8h.md#ac3274b70aee7aff6282eaa77ca819f27)#define STM32\_FLASH\_PRESCALER STM32\_CORE\_PRESCALER

86#endif

87

[ 88](stm32__clock__control_8h.md#a29ef6b98c22a522cde9f7dab5b11ace0)#define STM32\_ADC\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc\_prescaler)

[ 89](stm32__clock__control_8h.md#a35954cadc11af5ee499918be312acf38)#define STM32\_ADC12\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc12\_prescaler)

[ 90](stm32__clock__control_8h.md#a1cae4646086d8f855b72d55fee1483ad)#define STM32\_ADC34\_PRESCALER DT\_PROP(DT\_NODELABEL(rcc), adc34\_prescaler)

91

93#if defined(CONFIG\_SOC\_SERIES\_STM32H7RSX)

94#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), dcpre)

95#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

96#define STM32\_PPRE1 DT\_PROP(DT\_NODELABEL(rcc), ppre1)

97#define STM32\_PPRE2 DT\_PROP(DT\_NODELABEL(rcc), ppre2)

98#define STM32\_PPRE4 DT\_PROP(DT\_NODELABEL(rcc), ppre4)

99#define STM32\_PPRE5 DT\_PROP(DT\_NODELABEL(rcc), ppre5)

100#else

[ 101](stm32__clock__control_8h.md#a51967fd4dcf9ec8fe8e7250b5af32c87)#define STM32\_D1CPRE DT\_PROP(DT\_NODELABEL(rcc), d1cpre)

[ 102](stm32__clock__control_8h.md#a035ea0d8259c0f89306c6a7d344705f2)#define STM32\_HPRE DT\_PROP(DT\_NODELABEL(rcc), hpre)

[ 103](stm32__clock__control_8h.md#a844064bd8ccafb5df4bf02748840491d)#define STM32\_D2PPRE1 DT\_PROP(DT\_NODELABEL(rcc), d2ppre1)

[ 104](stm32__clock__control_8h.md#a50394a7e040433c738fc7e9f03b7aff3)#define STM32\_D2PPRE2 DT\_PROP(DT\_NODELABEL(rcc), d2ppre2)

[ 105](stm32__clock__control_8h.md#a02a098a3296751f55ea349faecff7bd5)#define STM32\_D1PPRE DT\_PROP(DT\_NODELABEL(rcc), d1ppre)

[ 106](stm32__clock__control_8h.md#a9dd9b0e8ef84e6ff033a707b2a0ec231)#define STM32\_D3PPRE DT\_PROP(DT\_NODELABEL(rcc), d3ppre)

107#endif /\* CONFIG\_SOC\_SERIES\_STM32H7RSX \*/

108

[ 110](stm32__clock__control_8h.md#aea3d7b8e3adedef5f93cdb38852a8097)#define STM32\_AHB5\_DIV DT\_PROP(DT\_NODELABEL(rcc), ahb5\_div)

111

[ 112](stm32__clock__control_8h.md#ad9bff8a9cfbe0dbe0db73d077cb7a227)#define DT\_RCC\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(rcc))

113

114/\* To enable use of IS\_ENABLED utility macro, these symbols

115 \* should not be defined directly using DT\_SAME\_NODE.

116 \*/

117#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(pll))

118#define STM32\_SYSCLK\_SRC\_PLL 1

119#endif

120#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

121#define STM32\_SYSCLK\_SRC\_HSI 1

122#endif

123#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

124#define STM32\_SYSCLK\_SRC\_HSE 1

125#endif

126#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

127#define STM32\_SYSCLK\_SRC\_MSI 1

128#endif

129#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

130#define STM32\_SYSCLK\_SRC\_MSIS 1

131#endif

132#if DT\_SAME\_NODE(DT\_RCC\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

133#define STM32\_SYSCLK\_SRC\_CSI 1

134#endif

135

136

138

139#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f2\_pll\_clock, okay) || \

140 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f4\_pll\_clock, okay) || \

141 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f7\_pll\_clock, okay) || \

142 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g0\_pll\_clock, okay) || \

143 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32g4\_pll\_clock, okay) || \

144 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l4\_pll\_clock, okay) || \

145 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32u5\_pll\_clock, okay) || \

146 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wb\_pll\_clock, okay) || \

147 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32wba\_pll\_clock, okay) || \

148 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7\_pll\_clock, okay) || \

149 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32h7rs\_pll\_clock, okay)

150#define STM32\_PLL\_ENABLED 1

151#define STM32\_PLL\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div\_m)

152#define STM32\_PLL\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul\_n)

153#define STM32\_PLL\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_p)

154#define STM32\_PLL\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_p, 1)

155#define STM32\_PLL\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_q)

156#define STM32\_PLL\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_q, 1)

157#define STM32\_PLL\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_r)

158#define STM32\_PLL\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_r, 1)

159#define STM32\_PLL\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), div\_s)

160#define STM32\_PLL\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll), div\_s, 1)

161#define STM32\_PLL\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), fracn)

162#define STM32\_PLL\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll), fracn, 1)

163#endif

164

165#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f4\_plli2s\_clock, okay)

166#define STM32\_PLLI2S\_ENABLED 1

167#define STM32\_PLLI2S\_M\_DIVISOR STM32\_PLL\_M\_DIVISOR

168#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

169#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

170#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

171#endif

172

173#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(plli2s), st\_stm32f412\_plli2s\_clock, okay)

174#define STM32\_PLLI2S\_ENABLED 1

175#define STM32\_PLLI2S\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(plli2s), div\_m)

176#define STM32\_PLLI2S\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(plli2s), mul\_n)

177#define STM32\_PLLI2S\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(plli2s), div\_r)

178#define STM32\_PLLI2S\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(plli2s), div\_r, 1)

179#endif

180

181#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32u5\_pll\_clock, okay) || \

182 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7\_pll\_clock, okay) || \

183 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32h7rs\_pll\_clock, okay)

184#define STM32\_PLL2\_ENABLED 1

185#define STM32\_PLL2\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll2), div\_m)

186#define STM32\_PLL2\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul\_n)

187#define STM32\_PLL2\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_p)

188#define STM32\_PLL2\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_p, 1)

189#define STM32\_PLL2\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_q)

190#define STM32\_PLL2\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_q, 1)

191#define STM32\_PLL2\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_r)

192#define STM32\_PLL2\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_r, 1)

193#define STM32\_PLL2\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_s)

194#define STM32\_PLL2\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_s, 1)

195#define STM32\_PLL2\_T\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), div\_t)

196#define STM32\_PLL2\_T\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll2), div\_t, 1)

197#define STM32\_PLL2\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), fracn)

198#define STM32\_PLL2\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll2), fracn, 1)

199#endif

200

201#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7\_pll\_clock, okay) || \

202 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32u5\_pll\_clock, okay) || \

203 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll3), st\_stm32h7rs\_pll\_clock, okay)

204#define STM32\_PLL3\_ENABLED 1

205#define STM32\_PLL3\_M\_DIVISOR DT\_PROP(DT\_NODELABEL(pll3), div\_m)

206#define STM32\_PLL3\_N\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll3), mul\_n)

207#define STM32\_PLL3\_P\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_p)

208#define STM32\_PLL3\_P\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_p, 1)

209#define STM32\_PLL3\_Q\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_q)

210#define STM32\_PLL3\_Q\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_q, 1)

211#define STM32\_PLL3\_R\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_r)

212#define STM32\_PLL3\_R\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_r, 1)

213#define STM32\_PLL3\_S\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), div\_s)

214#define STM32\_PLL3\_S\_DIVISOR DT\_PROP\_OR(DT\_NODELABEL(pll3), div\_s, 1)

215#define STM32\_PLL3\_FRACN\_ENABLED DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), fracn)

216#define STM32\_PLL3\_FRACN\_VALUE DT\_PROP\_OR(DT\_NODELABEL(pll3), fracn, 1)

217#endif

218

219#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f1\_pll\_clock, okay)

220#define STM32\_PLL\_ENABLED 1

221#define STM32\_PLL\_XTPRE DT\_PROP(DT\_NODELABEL(pll), xtpre)

222#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

223#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), usbpre)

224#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f0\_pll\_clock, okay) || \

225 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f100\_pll\_clock, okay) || \

226 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32f105\_pll\_clock, okay)

227#define STM32\_PLL\_ENABLED 1

228#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

229#define STM32\_PLL\_PREDIV DT\_PROP(DT\_NODELABEL(pll), prediv)

230#define STM32\_PLL\_USBPRE DT\_PROP(DT\_NODELABEL(pll), otgfspre)

231#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll), st\_stm32l0\_pll\_clock, okay)

232#define STM32\_PLL\_ENABLED 1

233#define STM32\_PLL\_DIVISOR DT\_PROP(DT\_NODELABEL(pll), div)

234#define STM32\_PLL\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll), mul)

235#endif

236

237#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(pll2), st\_stm32f105\_pll2\_clock, okay)

238#define STM32\_PLL2\_ENABLED 1

239#define STM32\_PLL2\_MULTIPLIER DT\_PROP(DT\_NODELABEL(pll2), mul)

240#define STM32\_PLL2\_PREDIV DT\_PROP(DT\_NODELABEL(pll2), prediv)

241#endif

242

244#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll), okay) && \

245 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll), clocks)

246#define DT\_PLL\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll))

247#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msi))

248#define STM32\_PLL\_SRC\_MSI 1

249#endif

250#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

251#define STM32\_PLL\_SRC\_MSIS 1

252#endif

253#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

254#define STM32\_PLL\_SRC\_HSI 1

255#endif

256#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_csi))

257#define STM32\_PLL\_SRC\_CSI 1

258#endif

259#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

260#define STM32\_PLL\_SRC\_HSE 1

261#endif

262#if DT\_SAME\_NODE(DT\_PLL\_CLOCKS\_CTRL, DT\_NODELABEL(pll2))

263#define STM32\_PLL\_SRC\_PLL2 1

264#endif

265

266#endif

267

269#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll2), okay) && \

270 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll2), clocks)

271#define DT\_PLL2\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll2))

272#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

273#define STM32\_PLL2\_SRC\_MSIS 1

274#endif

275#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

276#define STM32\_PLL2\_SRC\_HSI 1

277#endif

278#if DT\_SAME\_NODE(DT\_PLL2\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

279#define STM32\_PLL2\_SRC\_HSE 1

280#endif

281

282#endif

283

285#if DT\_NODE\_HAS\_STATUS(DT\_NODELABEL(pll3), okay) && \

286 DT\_NODE\_HAS\_PROP(DT\_NODELABEL(pll3), clocks)

287#define DT\_PLL3\_CLOCKS\_CTRL DT\_CLOCKS\_CTLR(DT\_NODELABEL(pll3))

288#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_msis))

289#define STM32\_PLL3\_SRC\_MSIS 1

290#endif

291#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hsi))

292#define STM32\_PLL3\_SRC\_HSI 1

293#endif

294#if DT\_SAME\_NODE(DT\_PLL3\_CLOCKS\_CTRL, DT\_NODELABEL(clk\_hse))

295#define STM32\_PLL3\_SRC\_HSE 1

296#endif

297

298#endif

299

300

302

303#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), fixed\_clock, okay)

304#define STM32\_LSE\_ENABLED 1

305#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

306#define STM32\_LSE\_DRIVING 0

307#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

308#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lse), st\_stm32\_lse\_clock, okay)

309#define STM32\_LSE\_ENABLED 1

310#define STM32\_LSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lse), clock\_frequency)

311#define STM32\_LSE\_DRIVING DT\_PROP(DT\_NODELABEL(clk\_lse), driving\_capability)

312#define STM32\_LSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_lse), lse\_bypass)

313#else

[ 314](stm32__clock__control_8h.md#a05b49e91f478558d33b2b862718758fa)#define STM32\_LSE\_ENABLED 0

[ 315](stm32__clock__control_8h.md#aedfe731de4f32e8dacd027bb115ca0e9)#define STM32\_LSE\_FREQ 0

[ 316](stm32__clock__control_8h.md#aead1c5c5ac685af96410f4883f7e988b)#define STM32\_LSE\_DRIVING 0

[ 317](stm32__clock__control_8h.md#a94745d7699b62ef9e7f8bbfbc6803727)#define STM32\_LSE\_BYPASS 0

318#endif

319

320#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay) || \

321 DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32l0\_msi\_clock, okay)

322#define STM32\_MSI\_ENABLED 1

323#define STM32\_MSI\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_range)

324#endif

325

326#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msi), st\_stm32\_msi\_clock, okay)

327#define STM32\_MSI\_ENABLED 1

328#define STM32\_MSI\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msi), msi\_pll\_mode)

329#endif

330

331#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msis), st\_stm32u5\_msi\_clock, okay)

332#define STM32\_MSIS\_ENABLED 1

333#define STM32\_MSIS\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_range)

334#define STM32\_MSIS\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msis), msi\_pll\_mode)

335#else

[ 336](stm32__clock__control_8h.md#a1a83a4c9a806689ac963e2ea8b142fda)#define STM32\_MSIS\_ENABLED 0

[ 337](stm32__clock__control_8h.md#a0109485d9cfd70782ce6aff604399330)#define STM32\_MSIS\_RANGE 0

[ 338](stm32__clock__control_8h.md#a02f0311b8e9c41a004ed355aff37a7b3)#define STM32\_MSIS\_PLL\_MODE 0

339#endif

340

341#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_msik), st\_stm32u5\_msi\_clock, okay)

342#define STM32\_MSIK\_ENABLED 1

343#define STM32\_MSIK\_RANGE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_range)

344#define STM32\_MSIK\_PLL\_MODE DT\_PROP(DT\_NODELABEL(clk\_msik), msi\_pll\_mode)

345#else

[ 346](stm32__clock__control_8h.md#a379e09d2e380483155b0ef8cc39d490b)#define STM32\_MSIK\_ENABLED 0

[ 347](stm32__clock__control_8h.md#a2fb4bc355d7e69e6b676794d0ab4cbba)#define STM32\_MSIK\_RANGE 0

[ 348](stm32__clock__control_8h.md#a67d63326f5ebe1b249eb56b227aecb29)#define STM32\_MSIK\_PLL\_MODE 0

349#endif

350

351#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_csi), fixed\_clock, okay)

352#define STM32\_CSI\_ENABLED 1

353#define STM32\_CSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_csi), clock\_frequency)

354#else

[ 355](stm32__clock__control_8h.md#a2110dbb73ce08ba40555f1d95b50ce5c)#define STM32\_CSI\_FREQ 0

356#endif

357

358#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi), fixed\_clock, okay)

359#define STM32\_LSI\_ENABLED 1

360#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi), clock\_frequency)

361#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi1), fixed\_clock, okay)

362#define STM32\_LSI\_ENABLED 1

363#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi1), clock\_frequency)

364#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_lsi2), fixed\_clock, okay)

365#define STM32\_LSI\_ENABLED 1

366#define STM32\_LSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_lsi2), clock\_frequency)

367#else

[ 368](stm32__clock__control_8h.md#ae4ad7f2e4844901d753a91c1ba5c58c5)#define STM32\_LSI\_FREQ 0

369#endif

370

371#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), fixed\_clock, okay)

372#define STM32\_HSI\_DIV\_ENABLED 0

373#define STM32\_HSI\_ENABLED 1

374#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

375#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32h7\_hsi\_clock, okay) \

376 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32g0\_hsi\_clock, okay) \

377 || DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi), st\_stm32c0\_hsi\_clock, okay)

378#define STM32\_HSI\_DIV\_ENABLED 1

379#define STM32\_HSI\_ENABLED 1

380#define STM32\_HSI\_DIVISOR DT\_PROP(DT\_NODELABEL(clk\_hsi), hsi\_div)

381#define STM32\_HSI\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi), clock\_frequency)

382#else

[ 383](stm32__clock__control_8h.md#aa67c0b4d532b58d78b12d36ae6817912)#define STM32\_HSI\_DIV\_ENABLED 0

[ 384](stm32__clock__control_8h.md#a2cc52c346227b2dfb91e1ab5aeda586c)#define STM32\_HSI\_DIVISOR 1

[ 385](stm32__clock__control_8h.md#af906386de1fde7ab0894971723a0a801)#define STM32\_HSI\_FREQ 0

386#endif

387

388#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), fixed\_clock, okay)

389#define STM32\_HSE\_ENABLED 1

390#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

391#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32\_hse\_clock, okay)

392#define STM32\_HSE\_ENABLED 1

393#define STM32\_HSE\_BYPASS DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_bypass)

394#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

395#define STM32\_HSE\_CSS DT\_PROP(DT\_NODELABEL(clk\_hse), css\_enabled)

396#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wl\_hse\_clock, okay)

397#define STM32\_HSE\_ENABLED 1

398#define STM32\_HSE\_TCXO DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_tcxo)

399#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

400#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

401#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hse), st\_stm32wba\_hse\_clock, okay)

402#define STM32\_HSE\_ENABLED 1

403#define STM32\_HSE\_DIV2 DT\_PROP(DT\_NODELABEL(clk\_hse), hse\_div2)

404#define STM32\_HSE\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hse), clock\_frequency)

405#else

[ 406](stm32__clock__control_8h.md#a7c3796ef481224c9e2f7516853677ec9)#define STM32\_HSE\_FREQ 0

407#endif

408

409#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), fixed\_clock, okay)

410#define STM32\_HSI48\_ENABLED 1

411#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

412#elif DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(clk\_hsi48), st\_stm32\_hsi48\_clock, okay)

413#define STM32\_HSI48\_ENABLED 1

414#define STM32\_HSI48\_FREQ DT\_PROP(DT\_NODELABEL(clk\_hsi48), clock\_frequency)

415#define STM32\_HSI48\_CRS\_USB\_SOF DT\_PROP(DT\_NODELABEL(clk\_hsi48), crs\_usb\_sof)

416#endif

417

418#if DT\_NODE\_HAS\_COMPAT\_STATUS(DT\_NODELABEL(perck), st\_stm32\_clock\_mux, okay)

419#define STM32\_CKPER\_ENABLED 1

420#endif

421

423

[ 424](structstm32__pclken.md)struct [stm32\_pclken](structstm32__pclken.md) {

[ 425](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e);

[ 426](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf);

427};

428

430

[ 431](stm32__clock__control_8h.md#aa1b0949b4c58d57dcd2e979320cbed0a)#define STM32\_CLOCK\_INFO(clk\_index, node\_id) \

432 { \

433 .enr = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bits), \

434 .bus = DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, clk\_index, bus) \

435 }

[ 436](stm32__clock__control_8h.md#a9eb57b349f41edec11ff52a78015aea9)#define STM32\_DT\_CLOCKS(node\_id) \

437 { \

438 LISTIFY(DT\_NUM\_CLOCKS(node\_id), \

439 STM32\_CLOCK\_INFO, (,), node\_id) \

440 }

441

[ 442](stm32__clock__control_8h.md#a693176c2c60364d327aa5768ebfac185)#define STM32\_DT\_INST\_CLOCKS(inst) \

443 STM32\_DT\_CLOCKS(DT\_DRV\_INST(inst))

444

[ 445](stm32__clock__control_8h.md#a38559b31633eca5475b73b8a88df1fcd)#define STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT(inst) DT\_INST\_CLOCKS\_HAS\_IDX(inst, 1) ||

[ 446](stm32__clock__control_8h.md#aac932dfd992b11d479edf2a2d5e8de47)#define STM32\_DT\_INST\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

447 (DT\_INST\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_INST\_SUPPORT) 0)

448

[ 449](stm32__clock__control_8h.md#a8743160d8765b466f8ac6a89efaa9dbc)#define STM32\_DOMAIN\_CLOCK\_SUPPORT(id) DT\_CLOCKS\_HAS\_IDX(DT\_NODELABEL(id), 1) ||

[ 450](stm32__clock__control_8h.md#a7951b8025683529eebdd415d6b65688b)#define STM32\_DT\_DEV\_DOMAIN\_CLOCK\_SUPPORT \

451 (DT\_FOREACH\_STATUS\_OKAY(STM32\_DOMAIN\_CLOCK\_SUPPORT) 0)

452

454

[ 460](stm32__clock__control_8h.md#aaeece46c7eb50e1f095cc33f9f9c3475)#define STM32\_CLOCK\_REG\_GET(clock) \

461 (((clock) >> STM32\_CLOCK\_REG\_SHIFT) & STM32\_CLOCK\_REG\_MASK)

462

[ 468](stm32__clock__control_8h.md#a311bbc17ae04bf6fb648040255ed9af4)#define STM32\_CLOCK\_SHIFT\_GET(clock) \

469 (((clock) >> STM32\_CLOCK\_SHIFT\_SHIFT) & STM32\_CLOCK\_SHIFT\_MASK)

470

[ 476](stm32__clock__control_8h.md#ad3decf332c88ed6dd0f3deb22fdf559e)#define STM32\_CLOCK\_MASK\_GET(clock) \

477 (((clock) >> STM32\_CLOCK\_MASK\_SHIFT) & STM32\_CLOCK\_MASK\_MASK)

478

[ 484](stm32__clock__control_8h.md#ae4e06e6122c64ab7c4ccfadb4957a029)#define STM32\_CLOCK\_VAL\_GET(clock) \

485 (((clock) >> STM32\_CLOCK\_VAL\_SHIFT) & STM32\_CLOCK\_VAL\_MASK)

486

487#if defined(STM32\_HSE\_CSS)

496void stm32\_hse\_css\_callback(void);

497#endif

498

499#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_STM32\_CLOCK\_CONTROL\_H\_ \*/

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

[stm32h7rs\_clock.h](stm32h7rs__clock_8h.md)

[stm32l0\_clock.h](stm32l0__clock_8h.md)

[stm32l1\_clock.h](stm32l1__clock_8h.md)

[stm32l4\_clock.h](stm32l4__clock_8h.md)

[stm32u5\_clock.h](stm32u5__clock_8h.md)

[stm32wb\_clock.h](stm32wb__clock_8h.md)

[stm32wba\_clock.h](stm32wba__clock_8h.md)

[stm32wl\_clock.h](stm32wl__clock_8h.md)

[stm32\_pclken](structstm32__pclken.md)

Driver structure definition.

**Definition** stm32\_clock\_control.h:424

[stm32\_pclken::bus](structstm32__pclken.md#a511b195a13a653c1ff664a41ef791f8e)

uint32\_t bus

**Definition** stm32\_clock\_control.h:425

[stm32\_pclken::enr](structstm32__pclken.md#a907fb7b42699bff79625e4332714eadf)

uint32\_t enr

**Definition** stm32\_clock\_control.h:426

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [stm32\_clock\_control.h](stm32__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
