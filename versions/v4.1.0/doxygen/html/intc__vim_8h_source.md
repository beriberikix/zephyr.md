---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__vim_8h_source.html
original_path: doxygen/html/intc__vim_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_vim.h

[Go to the documentation of this file.](intc__vim_8h.md)

1/\* Copyright (C) 2023 BeagleBoard.org Foundation

2 \* Copyright (C) 2023 S Prashanth

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_INTC\_VIM\_H\_

8#define ZEPHYR\_DRIVERS\_INTC\_VIM\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/devicetree.h](devicetree_8h.md)>

13#include <[zephyr/dt-bindings/interrupt-controller/ti-vim.h](ti-vim_8h.md)>

14#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

15

[ 16](intc__vim_8h.md#a6b442dccdb4e254cac43abd28c0a724d)#define VIM\_BASE\_ADDR DT\_REG\_ADDR(DT\_INST(0, ti\_vim))

17

[ 18](intc__vim_8h.md#af3def9f38617688929e29eec9651c64b)#define VIM\_MAX\_IRQ\_PER\_GROUP (32)

[ 19](intc__vim_8h.md#a2520b3f68146858942723fe295c0dae4)#define VIM\_MAX\_GROUP\_NUM ((uint32\_t)(CONFIG\_NUM\_IRQS / VIM\_MAX\_IRQ\_PER\_GROUP))

20

[ 21](intc__vim_8h.md#a2bbbdbfa2a3dd00d1bd54d5c804220c1)#define VIM\_GET\_IRQ\_GROUP\_NUM(n) ((uint32\_t)((n) / VIM\_MAX\_IRQ\_PER\_GROUP))

[ 22](intc__vim_8h.md#a765f1dd48172c22f4fb9cb5eb2c0ecfc)#define VIM\_GET\_IRQ\_BIT\_NUM(n) ((uint32\_t)((n) % VIM\_MAX\_IRQ\_PER\_GROUP))

23

[ 24](intc__vim_8h.md#aba7671d7f7dee14d87f7feff8a3451f7)#define VIM\_PRI\_INT\_MAX (15)

25

[ 26](intc__vim_8h.md#a378ef153f705928fff529e02838d50af)#define VIM\_PID (VIM\_BASE\_ADDR + 0x0000)

[ 27](intc__vim_8h.md#adf312872ea552e35a0e9fed4ef69ae11)#define VIM\_INFO (VIM\_BASE\_ADDR + 0x0004)

[ 28](intc__vim_8h.md#ab4ee6967e7149c07a2690978e7a2f97b)#define VIM\_PRIIRQ (VIM\_BASE\_ADDR + 0x0008)

[ 29](intc__vim_8h.md#a17ea1cd9d06d003bbc094bffbefb47c4)#define VIM\_PRIFIQ (VIM\_BASE\_ADDR + 0x000C)

[ 30](intc__vim_8h.md#a7bcbdd8241d466014361b13baf43d81b)#define VIM\_IRQGSTS (VIM\_BASE\_ADDR + 0x0010)

[ 31](intc__vim_8h.md#a6c2b44a4cabf058542f9663f48d1bc07)#define VIM\_FIQGSTS (VIM\_BASE\_ADDR + 0x0014)

[ 32](intc__vim_8h.md#a893a5e8467a3e5417272dedc098e42b5)#define VIM\_IRQVEC (VIM\_BASE\_ADDR + 0x0018)

[ 33](intc__vim_8h.md#aba9caef8adb052c353f54679b95f4001)#define VIM\_FIQVEC (VIM\_BASE\_ADDR + 0x001C)

[ 34](intc__vim_8h.md#a814d881a2f50b7b47ab25084f59587f5)#define VIM\_ACTIRQ (VIM\_BASE\_ADDR + 0x0020)

[ 35](intc__vim_8h.md#a48bda38b33fc5dfc695dfdbe627f4984)#define VIM\_ACTFIQ (VIM\_BASE\_ADDR + 0x0024)

[ 36](intc__vim_8h.md#ac77876e0bfdd3a9382e28728d9e2ebd3)#define VIM\_DEDVEC (VIM\_BASE\_ADDR + 0x0030)

37

[ 38](intc__vim_8h.md#a0b86c01e8e3844c71a74380c2392a847)#define VIM\_RAW(n) (VIM\_BASE\_ADDR + (0x400) + ((n) \* 0x20))

[ 39](intc__vim_8h.md#ae714f8162f5840ab2eb655d48c92ac99)#define VIM\_STS(n) (VIM\_BASE\_ADDR + (0x404) + ((n) \* 0x20))

[ 40](intc__vim_8h.md#a0d2b404f0483d09a32b6a4914cd660ef)#define VIM\_INTR\_EN\_SET(n) (VIM\_BASE\_ADDR + (0x408) + ((n) \* 0x20))

[ 41](intc__vim_8h.md#a313eefa1e7b90c3988c8d15c1dfb2aae)#define VIM\_INTR\_EN\_CLR(n) (VIM\_BASE\_ADDR + (0x40c) + ((n) \* 0x20))

[ 42](intc__vim_8h.md#a6a07b16389503e1131e9b46e84545c4e)#define VIM\_IRQSTS(n) (VIM\_BASE\_ADDR + (0x410) + ((n) \* 0x20))

[ 43](intc__vim_8h.md#ac20f6ab045eb4c7193c94252d4ee26a5)#define VIM\_FIQSTS(n) (VIM\_BASE\_ADDR + (0x414) + ((n) \* 0x20))

[ 44](intc__vim_8h.md#adbf1801e1f7dfa45f19f20e91ccbf1e2)#define VIM\_INTMAP(n) (VIM\_BASE\_ADDR + (0x418) + ((n) \* 0x20))

[ 45](intc__vim_8h.md#a28965b8d5ed95f9bd0322e95d41aa65c)#define VIM\_INTTYPE(n) (VIM\_BASE\_ADDR + (0x41c) + ((n) \* 0x20))

[ 46](intc__vim_8h.md#ad7c36f8650ff847544a550a31235193b)#define VIM\_PRI\_INT(n) (VIM\_BASE\_ADDR + (0x1000) + ((n) \* 0x4))

[ 47](intc__vim_8h.md#abb38d6437a3f25c193c2506fe97cf89c)#define VIM\_VEC\_INT(n) (VIM\_BASE\_ADDR + (0x2000) + ((n) \* 0x4))

48

49/\* RAW \*/

50

[ 51](intc__vim_8h.md#acd62766b3379b5baf178a33b6ff3d905)#define VIM\_GRP\_RAW\_STS\_MASK (BIT\_MASK(32))

[ 52](intc__vim_8h.md#ad28eafc29daa6e59de34e62f1493cfca)#define VIM\_GRP\_RAW\_STS\_SHIFT (0x00000000U)

[ 53](intc__vim_8h.md#aa82ed994598088a4a39bf628d78dc747)#define VIM\_GRP\_RAW\_STS\_RESETVAL (0x00000000U)

[ 54](intc__vim_8h.md#a2842ee6521e5115eb85dd2b591aebd9b)#define VIM\_GRP\_RAW\_STS\_MAX (BIT\_MASK(32))

55

[ 56](intc__vim_8h.md#a4817d3ad8ab3b557b19882b272d67d1b)#define VIM\_GRP\_RAW\_RESETVAL (0x00000000U)

57

58/\* STS \*/

59

[ 60](intc__vim_8h.md#a7f4d55def9ac847ff1c2f6739f09a636)#define VIM\_GRP\_STS\_MSK\_MASK (BIT\_MASK(32))

[ 61](intc__vim_8h.md#a79f980ac35a193b154853fd35aa8bcaf)#define VIM\_GRP\_STS\_MSK\_SHIFT (0x00000000U)

[ 62](intc__vim_8h.md#aec03c90df4149318acb41f1feacd4392)#define VIM\_GRP\_STS\_MSK\_RESETVAL (0x00000000U)

[ 63](intc__vim_8h.md#a1c452655a919216d7ba809d96e1b0287)#define VIM\_GRP\_STS\_MSK\_MAX (BIT\_MASK(32))

64

[ 65](intc__vim_8h.md#a229308ab7f2cd16ce15cbe0dd8c0197b)#define VIM\_GRP\_STS\_RESETVAL (0x00000000U)

66

67/\* INTR\_EN\_SET \*/

68

[ 69](intc__vim_8h.md#a339c2737a2eb9180b78305a058b6aa90)#define VIM\_GRP\_INTR\_EN\_SET\_MSK\_MASK (BIT\_MASK(32))

[ 70](intc__vim_8h.md#a9c5eb8d20f8de659ca970cd69c4cd193)#define VIM\_GRP\_INTR\_EN\_SET\_MSK\_SHIFT (0x00000000U)

[ 71](intc__vim_8h.md#a81eb2356267a972232177b893bc41fb7)#define VIM\_GRP\_INTR\_EN\_SET\_MSK\_RESETVAL (0x00000000U)

[ 72](intc__vim_8h.md#a61e07bf8b299223d8d4767aaa2e718b2)#define VIM\_GRP\_INTR\_EN\_SET\_MSK\_MAX (BIT\_MASK(32))

73

[ 74](intc__vim_8h.md#a23b0f2ce857795c9e6c6faf35f124d02)#define VIM\_GRP\_INTR\_EN\_SET\_RESETVAL (0x00000000U)

75

76/\* INTR\_EN\_CLR \*/

77

[ 78](intc__vim_8h.md#a5b0397e530cdcc0ae4f88796a9ef86ef)#define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MASK (BIT\_MASK(32))

[ 79](intc__vim_8h.md#ae3fde9d57f6e6328a7f88f6889d91c3a)#define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_SHIFT (0x00000000U)

[ 80](intc__vim_8h.md#a5617ad614b65e9341c5f9b4a3405fce6)#define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_RESETVAL (0x00000000U)

[ 81](intc__vim_8h.md#a1af7c911da646796d1091c4da9f45bf9)#define VIM\_GRP\_INTR\_EN\_CLR\_MSK\_MAX (BIT\_MASK(32))

82

[ 83](intc__vim_8h.md#a1113d705a90dd04e9af1999c37f9cb8e)#define VIM\_GRP\_INTR\_EN\_CLR\_RESETVAL (0x00000000U)

84

85/\* IRQSTS \*/

86

[ 87](intc__vim_8h.md#a13abe76418c094499d537b7fad5a171c)#define VIM\_GRP\_IRQSTS\_MSK\_MASK (BIT\_MASK(32))

[ 88](intc__vim_8h.md#a24299da38556f543de8e12ff36a81d38)#define VIM\_GRP\_IRQSTS\_MSK\_SHIFT (0x00000000U)

[ 89](intc__vim_8h.md#ac4d5bf5d6ee09462f4254a12db2bad44)#define VIM\_GRP\_IRQSTS\_MSK\_RESETVAL (0x00000000U)

[ 90](intc__vim_8h.md#aa3a16c92d1f55aff8a9b750990a7daf1)#define VIM\_GRP\_IRQSTS\_MSK\_MAX (BIT\_MASK(32))

91

[ 92](intc__vim_8h.md#a308a20f9e29c85ece314a6a005b6a4dd)#define VIM\_GRP\_IRQSTS\_RESETVAL (0x00000000U)

93

94/\* FIQSTS \*/

95

[ 96](intc__vim_8h.md#a374962357620f5b6ea7f3938158f52c9)#define VIM\_GRP\_FIQSTS\_MSK\_MASK (BIT\_MASK(32))

[ 97](intc__vim_8h.md#a3b5c2839ef08c51d8163048023bec7bc)#define VIM\_GRP\_FIQSTS\_MSK\_SHIFT (0x00000000U)

[ 98](intc__vim_8h.md#a75f2aa2343da1e6f1577189911c685ce)#define VIM\_GRP\_FIQSTS\_MSK\_RESETVAL (0x00000000U)

[ 99](intc__vim_8h.md#a7698addaef1b0850b538b508762da567)#define VIM\_GRP\_FIQSTS\_MSK\_MAX (BIT\_MASK(32))

100

[ 101](intc__vim_8h.md#aff2481d09e0ed29c7206d28c098a0d14)#define VIM\_GRP\_FIQSTS\_RESETVAL (0x00000000U)

102

103/\* INTMAP \*/

104

[ 105](intc__vim_8h.md#a0259713478ab1f5930d1b303450d9b72)#define VIM\_GRP\_INTMAP\_MSK\_MASK (BIT\_MASK(32))

[ 106](intc__vim_8h.md#aea4c913d99500c4b3cb1c60b5b514c2f)#define VIM\_GRP\_INTMAP\_MSK\_SHIFT (0x00000000U)

[ 107](intc__vim_8h.md#ac5d9e9e42d0c203c22a357ccec802c72)#define VIM\_GRP\_INTMAP\_MSK\_RESETVAL (0x00000000U)

[ 108](intc__vim_8h.md#ad64d7f6045a420d2ed78f6bb0446294f)#define VIM\_GRP\_INTMAP\_MSK\_MAX (BIT\_MASK(32))

109

[ 110](intc__vim_8h.md#a104e9c67c35b9656d451efbe5045cb78)#define VIM\_GRP\_INTMAP\_RESETVAL (0x00000000U)

111

112/\* INTTYPE \*/

113

[ 114](intc__vim_8h.md#a29cdb963486249ff8d87c1bf4ceeeb74)#define VIM\_GRP\_INTTYPE\_MSK\_MASK (BIT\_MASK(32))

[ 115](intc__vim_8h.md#a6c1cd189c9e5426b8a79b97b1f860753)#define VIM\_GRP\_INTTYPE\_MSK\_SHIFT (0x00000000U)

[ 116](intc__vim_8h.md#a5d3443ac8213a8c02c364c9e6f37690c)#define VIM\_GRP\_INTTYPE\_MSK\_RESETVAL (0x00000000U)

[ 117](intc__vim_8h.md#a37f2063ecf4acdd91ab16a8941a9c51c)#define VIM\_GRP\_INTTYPE\_MSK\_MAX (BIT\_MASK(32))

118

[ 119](intc__vim_8h.md#a35adc119bb4371fe8cf7070336935720)#define VIM\_GRP\_INTTYPE\_RESETVAL (0x00000000U)

120

121/\* INT \*/

122

[ 123](intc__vim_8h.md#a996fc01313c3b05b298f32b7691a0ba1)#define VIM\_PRI\_INT\_VAL\_MASK (BIT\_MASK(4))

[ 124](intc__vim_8h.md#ad9d91c69c20c243578aea8028d4635a2)#define VIM\_PRI\_INT\_VAL\_SHIFT (0x00000000U)

[ 125](intc__vim_8h.md#a413968f03758ca53b005bfe7c5e3023b)#define VIM\_PRI\_INT\_VAL\_RESETVAL (BIT\_MASK(4))

[ 126](intc__vim_8h.md#af8297a7ca4b4b0cddb3703312fb858bb)#define VIM\_PRI\_INT\_VAL\_MAX (BIT\_MASK(4))

127

[ 128](intc__vim_8h.md#a72fa57b55ef32e7c7db63932c28d65da)#define VIM\_PRI\_INT\_RESETVAL (BIT\_MASK(4))

129

130/\* INT \*/

131

[ 132](intc__vim_8h.md#a8076a54316cec3fc0de52079bd4cd598)#define VIM\_VEC\_INT\_VAL\_MASK (0xFFFFFFFCU)

[ 133](intc__vim_8h.md#a3024d3c80cdc3db66954fa83541ca389)#define VIM\_VEC\_INT\_VAL\_SHIFT (0x00000002U)

[ 134](intc__vim_8h.md#a3dd1401816579e5d07876b87b34e2177)#define VIM\_VEC\_INT\_VAL\_RESETVAL (0x00000000U)

[ 135](intc__vim_8h.md#a769edf746fb1ef704f85bfdee55fb136)#define VIM\_VEC\_INT\_VAL\_MAX (BIT\_MASK(30))

136

[ 137](intc__vim_8h.md#a16bd2873cba17ebd29acd3aeb58b2df4)#define VIM\_VEC\_INT\_RESETVAL (0x00000000U)

138

139/\* INFO \*/

140

[ 141](intc__vim_8h.md#adeba4e94c9d68665820fd13483d24b85)#define VIM\_INFO\_INTERRUPTS\_MASK (BIT\_MASK(11))

[ 142](intc__vim_8h.md#ace1cb4b9d2de191575a9bba21882a025)#define VIM\_INFO\_INTERRUPTS\_SHIFT (0x00000000U)

[ 143](intc__vim_8h.md#ad37820d3013c0ed4867a7235ee16444f)#define VIM\_INFO\_INTERRUPTS\_RESETVAL (0x00000400U)

[ 144](intc__vim_8h.md#aca715ba5a23516302a6c1a648fbbdeea)#define VIM\_INFO\_INTERRUPTS\_MAX (BIT\_MASK(11))

145

[ 146](intc__vim_8h.md#a3fc8c50f54bc3a158dbfef51fb96ee5b)#define VIM\_INFO\_RESETVAL (0x00000400U)

147

148/\* PRIIRQ \*/

149

[ 150](intc__vim_8h.md#a4d4d0d285eabeccb6418c442a7b3453b)#define VIM\_PRIIRQ\_VALID\_MASK (0x80000000U)

[ 151](intc__vim_8h.md#acaca01cbd74088f455f8345472424339)#define VIM\_PRIIRQ\_VALID\_SHIFT (BIT\_MASK(5))

[ 152](intc__vim_8h.md#a7026e741d660e4d893ac1457c12ef827)#define VIM\_PRIIRQ\_VALID\_RESETVAL (0x00000000U)

[ 153](intc__vim_8h.md#aacbd1281fb54586fa48c6ed3d49d62cd)#define VIM\_PRIIRQ\_VALID\_MAX (0x00000001U)

154

[ 155](intc__vim_8h.md#adc2729dd6329da29bac1ac4942003f7d)#define VIM\_PRIIRQ\_VALID\_VAL\_TRUE (0x1U)

[ 156](intc__vim_8h.md#a0966b95628413d1efdf9e572783865bd)#define VIM\_PRIIRQ\_VALID\_VAL\_FALSE (0x0U)

157

[ 158](intc__vim_8h.md#ad952cdc46228507194a3b19baf6d71e7)#define VIM\_PRIIRQ\_PRI\_MASK (0x000F0000U)

[ 159](intc__vim_8h.md#a31ed4fa3d085d39863d0da6b657ca0df)#define VIM\_PRIIRQ\_PRI\_SHIFT (0x00000010U)

[ 160](intc__vim_8h.md#a810037874c898a7c0f738096406b9148)#define VIM\_PRIIRQ\_PRI\_RESETVAL (0x00000000U)

[ 161](intc__vim_8h.md#ac3f1624d169a99edb836f3a3ba82acfa)#define VIM\_PRIIRQ\_PRI\_MAX (BIT\_MASK(4))

162

[ 163](intc__vim_8h.md#a236930837a36a72e4b29f81175537543)#define VIM\_PRIIRQ\_NUM\_MASK (BIT\_MASK(10))

[ 164](intc__vim_8h.md#ac7956ab58b6223b8e511892ff35d9375)#define VIM\_PRIIRQ\_NUM\_SHIFT (0x00000000U)

[ 165](intc__vim_8h.md#a4376b256f168336b45108b8255a0f92f)#define VIM\_PRIIRQ\_NUM\_RESETVAL (0x00000000U)

[ 166](intc__vim_8h.md#a610e6f20d550a0cc5e90f31f7ce9f065)#define VIM\_PRIIRQ\_NUM\_MAX (BIT\_MASK(10))

167

[ 168](intc__vim_8h.md#a13826544f2e9cd4ce4164b62d8e82d7e)#define VIM\_PRIIRQ\_RESETVAL (0x00000000U)

169

170/\* PRIFIQ \*/

171

[ 172](intc__vim_8h.md#aba90d57af70816d9b58dc8851f6da004)#define VIM\_PRIFIQ\_VALID\_MASK (0x80000000U)

[ 173](intc__vim_8h.md#a3c93252a9eae445243cd8a9c39d79f82)#define VIM\_PRIFIQ\_VALID\_SHIFT (BIT\_MASK(5))

[ 174](intc__vim_8h.md#a322fe75f392fb162f1c04330990ed2d7)#define VIM\_PRIFIQ\_VALID\_RESETVAL (0x00000000U)

[ 175](intc__vim_8h.md#ac8173b6b098e38ea9eebbf79e8f8a1da)#define VIM\_PRIFIQ\_VALID\_MAX (0x00000001U)

176

[ 177](intc__vim_8h.md#ac5ced3000f18ecfc7fc5ea07e3473f78)#define VIM\_PRIFIQ\_VALID\_VAL\_TRUE (0x1U)

[ 178](intc__vim_8h.md#a6bdf3d9847f3ccad759874bb5b09cfb4)#define VIM\_PRIFIQ\_VALID\_VAL\_FALSE (0x0U)

179

[ 180](intc__vim_8h.md#a6de77b9058d6b58314097adebe045a86)#define VIM\_PRIFIQ\_PRI\_MASK (0x000F0000U)

[ 181](intc__vim_8h.md#a3d61188f8ce9b07ac1bcb708c0a28619)#define VIM\_PRIFIQ\_PRI\_SHIFT (0x00000010U)

[ 182](intc__vim_8h.md#aa810609b09640d548c56bdfb09b9868c)#define VIM\_PRIFIQ\_PRI\_RESETVAL (0x00000000U)

[ 183](intc__vim_8h.md#a67922050c7eb81575c1b7b1e227b6839)#define VIM\_PRIFIQ\_PRI\_MAX (BIT\_MASK(4))

184

[ 185](intc__vim_8h.md#aad509ed553a5e15f893390481ac739fa)#define VIM\_PRIFIQ\_NUM\_MASK (BIT\_MASK(10))

[ 186](intc__vim_8h.md#af8b15089bdd21a468168c1d5e8fc7dad)#define VIM\_PRIFIQ\_NUM\_SHIFT (0x00000000U)

[ 187](intc__vim_8h.md#a608c0a95598b701c377351bdab275df4)#define VIM\_PRIFIQ\_NUM\_RESETVAL (0x00000000U)

[ 188](intc__vim_8h.md#ac27797438659455e527d82e9fb586b5a)#define VIM\_PRIFIQ\_NUM\_MAX (BIT\_MASK(10))

189

[ 190](intc__vim_8h.md#adf127d9e139beb74e65b88741d82013a)#define VIM\_PRIFIQ\_RESETVAL (0x00000000U)

191

192/\* IRQGSTS \*/

193

[ 194](intc__vim_8h.md#a4497e08f4d565ace708e50c84f0f51b6)#define VIM\_IRQGSTS\_STS\_MASK (BIT\_MASK(32))

[ 195](intc__vim_8h.md#a03180f0120311298a518f8f109fa2dee)#define VIM\_IRQGSTS\_STS\_SHIFT (0x00000000U)

[ 196](intc__vim_8h.md#af7d810589915de14ab7cff616fdb0b5f)#define VIM\_IRQGSTS\_STS\_RESETVAL (0x00000000U)

[ 197](intc__vim_8h.md#a82828e470cbcd1df782ed463c61ecfee)#define VIM\_IRQGSTS\_STS\_MAX (BIT\_MASK(32))

198

[ 199](intc__vim_8h.md#a674113c74daca28dc3a3777cf2a33917)#define VIM\_IRQGSTS\_RESETVAL (0x00000000U)

200

201/\* FIQGSTS \*/

202

[ 203](intc__vim_8h.md#a4047a2f3c251c623a7bb4f03e2c80aa9)#define VIM\_FIQGSTS\_STS\_MASK (BIT\_MASK(32))

[ 204](intc__vim_8h.md#a0cf8b2290a847eccb9206368c36d84d3)#define VIM\_FIQGSTS\_STS\_SHIFT (0x00000000U)

[ 205](intc__vim_8h.md#ac814862811ec1cf1d1e240c03fa5220a)#define VIM\_FIQGSTS\_STS\_RESETVAL (0x00000000U)

[ 206](intc__vim_8h.md#a06d51cb097cedabe76ab25fb2336be2b)#define VIM\_FIQGSTS\_STS\_MAX (BIT\_MASK(32))

207

[ 208](intc__vim_8h.md#ada89357c38ffaa43681b7e874aaddd6a)#define VIM\_FIQGSTS\_RESETVAL (0x00000000U)

209

210/\* IRQVEC \*/

211

[ 212](intc__vim_8h.md#a854706bcbaeb0764d2dac7a325734b20)#define VIM\_IRQVEC\_ADDR\_MASK (0xFFFFFFFCU)

[ 213](intc__vim_8h.md#a692248d3c771837c934b2057573511f7)#define VIM\_IRQVEC\_ADDR\_SHIFT (0x00000002U)

[ 214](intc__vim_8h.md#ad0643477818df3a01ec0aad56be04cb1)#define VIM\_IRQVEC\_ADDR\_RESETVAL (0x00000000U)

[ 215](intc__vim_8h.md#abb959b8bcc866cc955ae998ae62a2feb)#define VIM\_IRQVEC\_ADDR\_MAX (BIT\_MASK(30))

216

[ 217](intc__vim_8h.md#a5c92254c2655c9a73f13eba43e50a398)#define VIM\_IRQVEC\_RESETVAL (0x00000000U)

218

219/\* FIQVEC \*/

220

[ 221](intc__vim_8h.md#a88ff3e766b092657a21fdf7ae2e93564)#define VIM\_FIQVEC\_ADDR\_MASK (0xFFFFFFFCU)

[ 222](intc__vim_8h.md#a0db8828c7c1b359335220d80cf6fcb6f)#define VIM\_FIQVEC\_ADDR\_SHIFT (0x00000002U)

[ 223](intc__vim_8h.md#a5694973ce948cb75ec95b457b58544a5)#define VIM\_FIQVEC\_ADDR\_RESETVAL (0x00000000U)

[ 224](intc__vim_8h.md#a9e15f36e9494b3f69bbf49d962c38590)#define VIM\_FIQVEC\_ADDR\_MAX (BIT\_MASK(30))

225

[ 226](intc__vim_8h.md#a972fd2da90560b549d4eacc367643367)#define VIM\_FIQVEC\_RESETVAL (0x00000000U)

227

228/\* ACTIRQ \*/

229

[ 230](intc__vim_8h.md#a9740e75023b8bf6ddc87f2aabc234a5c)#define VIM\_ACTIRQ\_VALID\_MASK (0x80000000U)

[ 231](intc__vim_8h.md#ab80c58ab4e04413ec1108ab4899758e4)#define VIM\_ACTIRQ\_VALID\_SHIFT (BIT\_MASK(5))

[ 232](intc__vim_8h.md#ad41b0eebaa403614473d6d91b3c54708)#define VIM\_ACTIRQ\_VALID\_RESETVAL (0x00000000U)

[ 233](intc__vim_8h.md#a8c0cf47b8dca0ed71e45a0d2cf791cf9)#define VIM\_ACTIRQ\_VALID\_MAX (0x00000001U)

234

[ 235](intc__vim_8h.md#a67149d8156c8c49e50ffd974ff541be8)#define VIM\_ACTIRQ\_VALID\_VAL\_TRUE (0x1U)

[ 236](intc__vim_8h.md#a4755bb481e7b635fb78a1ed1645fd65f)#define VIM\_ACTIRQ\_VALID\_VAL\_FALSE (0x0U)

237

[ 238](intc__vim_8h.md#aa67330dfd1a07514b6aefb175688f6a2)#define VIM\_ACTIRQ\_PRI\_MASK (0x000F0000U)

[ 239](intc__vim_8h.md#aa7f7b505e9f67ef073b27eecfd2e24dd)#define VIM\_ACTIRQ\_PRI\_SHIFT (0x00000010U)

[ 240](intc__vim_8h.md#a407ec18db62cdab6fc03e2e91d8f7a48)#define VIM\_ACTIRQ\_PRI\_RESETVAL (0x00000000U)

[ 241](intc__vim_8h.md#af5af969746c802c3fcc54624cc8fc1c5)#define VIM\_ACTIRQ\_PRI\_MAX (BIT\_MASK(4))

242

[ 243](intc__vim_8h.md#af37fe4204363b131433c08e144b706c0)#define VIM\_ACTIRQ\_NUM\_MASK (BIT\_MASK(10))

[ 244](intc__vim_8h.md#a1fb7025bd77510c4aa4735205a5e0119)#define VIM\_ACTIRQ\_NUM\_SHIFT (0x00000000U)

[ 245](intc__vim_8h.md#a891dc381e24ccef01b7ddc3004e68f72)#define VIM\_ACTIRQ\_NUM\_RESETVAL (0x00000000U)

[ 246](intc__vim_8h.md#ac1e4050ca8a6f725df77e3066fb75577)#define VIM\_ACTIRQ\_NUM\_MAX (BIT\_MASK(10))

247

[ 248](intc__vim_8h.md#afe3be53299ab4dd7f158cb887d2a71af)#define VIM\_ACTIRQ\_RESETVAL (0x00000000U)

249

250/\* ACTFIQ \*/

251

[ 252](intc__vim_8h.md#a5f654648e1fceddc473017f5c69ebfde)#define VIM\_ACTFIQ\_VALID\_MASK (0x80000000U)

[ 253](intc__vim_8h.md#a8891923ca180a27349b5ac4c50b75624)#define VIM\_ACTFIQ\_VALID\_SHIFT (BIT\_MASK(5))

[ 254](intc__vim_8h.md#adde70d87d3232e8cebd56058a0ba11c0)#define VIM\_ACTFIQ\_VALID\_RESETVAL (0x00000000U)

[ 255](intc__vim_8h.md#a4c3805e9372e278fa041f29b1cc79be0)#define VIM\_ACTFIQ\_VALID\_MAX (0x00000001U)

256

[ 257](intc__vim_8h.md#a89a2a0626470f6d4efe41ea9790d6dfb)#define VIM\_ACTFIQ\_VALID\_VAL\_TRUE (0x1U)

[ 258](intc__vim_8h.md#ad931b8267aa9895fb907f83b9bcab0a8)#define VIM\_ACTFIQ\_VALID\_VAL\_FALSE (0x0U)

259

[ 260](intc__vim_8h.md#a53c9c40d87a7f364b61a6e2f626ec289)#define VIM\_ACTFIQ\_PRI\_MASK (0x000F0000U)

[ 261](intc__vim_8h.md#afd741827c49d9ab22ef4982061e48867)#define VIM\_ACTFIQ\_PRI\_SHIFT (0x00000010U)

[ 262](intc__vim_8h.md#a51ccd75970e116bac2e1a35c6de1170f)#define VIM\_ACTFIQ\_PRI\_RESETVAL (0x00000000U)

[ 263](intc__vim_8h.md#a22d18ac005433d054a6a15dff39c6e68)#define VIM\_ACTFIQ\_PRI\_MAX (BIT\_MASK(4))

264

[ 265](intc__vim_8h.md#a6245859896c6fcaf000ce56a04d30d5f)#define VIM\_ACTFIQ\_NUM\_MASK (BIT\_MASK(10))

[ 266](intc__vim_8h.md#adc5bba8d5dd9a72a6db1b5ed51145159)#define VIM\_ACTFIQ\_NUM\_SHIFT (0x00000000U)

[ 267](intc__vim_8h.md#a09b7e2ffd6b9e526bb3088a421e5efc4)#define VIM\_ACTFIQ\_NUM\_RESETVAL (0x00000000U)

[ 268](intc__vim_8h.md#a6e1d51c6b92462e9789ba0dcc2d3bd53)#define VIM\_ACTFIQ\_NUM\_MAX (BIT\_MASK(10))

269

[ 270](intc__vim_8h.md#a29431d2fd28113d56f66531593876580)#define VIM\_ACTFIQ\_RESETVAL (0x00000000U)

271

272/\* DEDVEC \*/

273

[ 274](intc__vim_8h.md#a29b50c725ad2f701fb0c324f178579fb)#define VIM\_DEDVEC\_ADDR\_MASK (0xFFFFFFFCU)

[ 275](intc__vim_8h.md#aa2d21a760a0307ad49b55880652ad2de)#define VIM\_DEDVEC\_ADDR\_SHIFT (0x00000002U)

[ 276](intc__vim_8h.md#a549218cf3d2c3031ad08a2c2cc0138b0)#define VIM\_DEDVEC\_ADDR\_RESETVAL (0x00000000U)

[ 277](intc__vim_8h.md#a4d3ae5e999ff96654cd472211788f203)#define VIM\_DEDVEC\_ADDR\_MAX (BIT\_MASK(30))

278

[ 279](intc__vim_8h.md#a8245d6946648411610d113a2c85a9e91)#define VIM\_DEDVEC\_RESETVAL (0x00000000U)

280

281/\*

282 \* VIM Driver Interface Functions

283 \*/

284

290unsigned int z\_vim\_irq\_get\_active(void);

291

297void z\_vim\_irq\_eoi(unsigned int irq);

298

302void z\_vim\_irq\_init(void);

303

311void z\_vim\_irq\_priority\_set(unsigned int irq, unsigned int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

312

318void z\_vim\_irq\_enable(unsigned int irq);

319

325void z\_vim\_irq\_disable(unsigned int irq);

326

335int z\_vim\_irq\_is\_enabled(unsigned int irq);

336

342void z\_vim\_arm\_enter\_irq(int irq);

343

344#endif /\* ZEPHYR\_DRIVERS\_INTC\_VIM\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[ti-vim.h](ti-vim_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_vim.h](intc__vim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
