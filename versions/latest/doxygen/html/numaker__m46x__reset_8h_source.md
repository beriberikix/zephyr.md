---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/numaker__m46x__reset_8h_source.html
original_path: doxygen/html/numaker__m46x__reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker\_m46x\_reset.h

[Go to the documentation of this file.](numaker__m46x__reset_8h.md)

1/\*

2 \* Copyright (c) 2023 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NUMAKER\_M46X\_RESET\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NUMAKER\_M46X\_RESET\_H

9

10/\* Beginning of M460 BSP sys\_reg.h reset module copy \*/

11

[ 12](numaker__m46x__reset_8h.md#aa14c6b9502ce50a8fba24c661032fee5)#define NUMAKER\_SYS\_IPRST0\_PDMA0RST\_Pos (2)

13

[ 14](numaker__m46x__reset_8h.md#a374d55f19e4ec1bb4ff6f6a080129b5b)#define NUMAKER\_SYS\_IPRST0\_EBIRST\_Pos (3)

15

[ 16](numaker__m46x__reset_8h.md#aa7476dd238924462ee26481c6b506f43)#define NUMAKER\_SYS\_IPRST0\_EMAC0RST\_Pos (5)

17

[ 18](numaker__m46x__reset_8h.md#a228ff84206969b7417687dfd66ed759e)#define NUMAKER\_SYS\_IPRST0\_SDH0RST\_Pos (6)

19

[ 20](numaker__m46x__reset_8h.md#abcf3717a5f0b65fc57afa4be8892882c)#define NUMAKER\_SYS\_IPRST0\_CRCRST\_Pos (7)

21

[ 22](numaker__m46x__reset_8h.md#af75fe0a9f9328e7d9426528770709813)#define NUMAKER\_SYS\_IPRST0\_CCAPRST\_Pos (8)

23

[ 24](numaker__m46x__reset_8h.md#aa128ef2acd6d85d3462b2e06505d4430)#define NUMAKER\_SYS\_IPRST0\_HSUSBDRST\_Pos (10)

25

[ 26](numaker__m46x__reset_8h.md#aa3e5d215a7b3d35f798d0c6261420fbb)#define NUMAKER\_SYS\_IPRST0\_HBIRST\_Pos (11)

27

[ 28](numaker__m46x__reset_8h.md#a98ecd3a2da3fd9c188c41f9a7bd2fa83)#define NUMAKER\_SYS\_IPRST0\_CRPTRST\_Pos (12)

29

[ 30](numaker__m46x__reset_8h.md#a00456383a1f8e045fd1a9af21450e8e7)#define NUMAKER\_SYS\_IPRST0\_KSRST\_Pos (13)

31

[ 32](numaker__m46x__reset_8h.md#a60e4e9f5a10982b52d0a586076d3f22f)#define NUMAKER\_SYS\_IPRST0\_SPIMRST\_Pos (14)

33

[ 34](numaker__m46x__reset_8h.md#a3b17c51b64df68e545ac7a1cb3840f3c)#define NUMAKER\_SYS\_IPRST0\_HSUSBHRST\_Pos (16)

35

[ 36](numaker__m46x__reset_8h.md#a838b537ba745222a9646113fcfeb29b6)#define NUMAKER\_SYS\_IPRST0\_SDH1RST\_Pos (17)

37

[ 38](numaker__m46x__reset_8h.md#a9ae42d3fcc4825eefa61ba69f8b8986e)#define NUMAKER\_SYS\_IPRST0\_PDMA1RST\_Pos (18)

39

[ 40](numaker__m46x__reset_8h.md#a95e3fc29e0e6e14522cbe297f45d8b4c)#define NUMAKER\_SYS\_IPRST0\_CANFD0RST\_Pos (20)

41

[ 42](numaker__m46x__reset_8h.md#a2c9fce995130a5237a92638f412e9c60)#define NUMAKER\_SYS\_IPRST0\_CANFD1RST\_Pos (21)

43

[ 44](numaker__m46x__reset_8h.md#a8a83be67140cb8ad215ce7356db2720b)#define NUMAKER\_SYS\_IPRST0\_CANFD2RST\_Pos (22)

45

[ 46](numaker__m46x__reset_8h.md#abdc862980795ce67f2e8705ae0ff42d7)#define NUMAKER\_SYS\_IPRST0\_CANFD3RST\_Pos (23)

47

[ 48](numaker__m46x__reset_8h.md#aa071a0cf4e53dbee5f9c0767da90c1c6)#define NUMAKER\_SYS\_IPRST0\_BMCRST\_Pos (28)

49

[ 50](numaker__m46x__reset_8h.md#a17f475cd001509b810d438e8cde77605)#define NUMAKER\_SYS\_IPRST1\_GPIORST\_Pos (1)

51

[ 52](numaker__m46x__reset_8h.md#aa8719c5979eb8194be0e6d312a9a528e)#define NUMAKER\_SYS\_IPRST1\_TMR0RST\_Pos (2)

53

[ 54](numaker__m46x__reset_8h.md#afd318f4349aff436604236cad97753e2)#define NUMAKER\_SYS\_IPRST1\_TMR1RST\_Pos (3)

55

[ 56](numaker__m46x__reset_8h.md#afeab0c010d4d35c53b5ece3319ce328e)#define NUMAKER\_SYS\_IPRST1\_TMR2RST\_Pos (4)

57

[ 58](numaker__m46x__reset_8h.md#ad7833f4354228b049b78b2e4644ea4a3)#define NUMAKER\_SYS\_IPRST1\_TMR3RST\_Pos (5)

59

[ 60](numaker__m46x__reset_8h.md#a9aa3dc7b6208b672128fbbdf25e28cc6)#define NUMAKER\_SYS\_IPRST1\_ACMP01RST\_Pos (7)

61

[ 62](numaker__m46x__reset_8h.md#a2cff9027643b934115b0dd0832fd56fd)#define NUMAKER\_SYS\_IPRST1\_I2C0RST\_Pos (8)

63

[ 64](numaker__m46x__reset_8h.md#a0f1b077a7b2ce36ca745354942f49120)#define NUMAKER\_SYS\_IPRST1\_I2C1RST\_Pos (9)

65

[ 66](numaker__m46x__reset_8h.md#a140bf4cd4c34d2eee5a5596ec7c2f40d)#define NUMAKER\_SYS\_IPRST1\_I2C2RST\_Pos (10)

67

[ 68](numaker__m46x__reset_8h.md#a6e29d396a308b5083304d21987fe5f19)#define NUMAKER\_SYS\_IPRST1\_I2C3RST\_Pos (11)

69

[ 70](numaker__m46x__reset_8h.md#a6d6486c98c5a5339122b65f78d3043f9)#define NUMAKER\_SYS\_IPRST1\_QSPI0RST\_Pos (12)

71

[ 72](numaker__m46x__reset_8h.md#a3a116c61ff635f11e9e5f4067f4dc042)#define NUMAKER\_SYS\_IPRST1\_SPI0RST\_Pos (13)

73

[ 74](numaker__m46x__reset_8h.md#a460befdbc00ee70ca095a1948105166c)#define NUMAKER\_SYS\_IPRST1\_SPI1RST\_Pos (14)

75

[ 76](numaker__m46x__reset_8h.md#ad9502dd9b6bf78d9f84620ed8d58e90a)#define NUMAKER\_SYS\_IPRST1\_SPI2RST\_Pos (15)

77

[ 78](numaker__m46x__reset_8h.md#acda143dd3b9594065068f04586570ccc)#define NUMAKER\_SYS\_IPRST1\_UART0RST\_Pos (16)

79

[ 80](numaker__m46x__reset_8h.md#a773461c6a35be084ee878a4ae7030ff8)#define NUMAKER\_SYS\_IPRST1\_UART1RST\_Pos (17)

81

[ 82](numaker__m46x__reset_8h.md#a84125fa75be52211802fb9ebca59f4f7)#define NUMAKER\_SYS\_IPRST1\_UART2RST\_Pos (18)

83

[ 84](numaker__m46x__reset_8h.md#af85ed27d6c54961fdbf408ff0d7653de)#define NUMAKER\_SYS\_IPRST1\_UART3RST\_Pos (19)

85

[ 86](numaker__m46x__reset_8h.md#ab5123d96fb9b07ecb4adda8cd945ba5f)#define NUMAKER\_SYS\_IPRST1\_UART4RST\_Pos (20)

87

[ 88](numaker__m46x__reset_8h.md#a0e6a6bb72ff1015815d010ec0860a963)#define NUMAKER\_SYS\_IPRST1\_UART5RST\_Pos (21)

89

[ 90](numaker__m46x__reset_8h.md#a0ea375ad611313a86c5e49c22011c67a)#define NUMAKER\_SYS\_IPRST1\_UART6RST\_Pos (22)

91

[ 92](numaker__m46x__reset_8h.md#ad3e76d7febcd8cea501a7fe14bf2cf47)#define NUMAKER\_SYS\_IPRST1\_UART7RST\_Pos (23)

93

[ 94](numaker__m46x__reset_8h.md#a81487344ea224a53b57e8c6246fef1b4)#define NUMAKER\_SYS\_IPRST1\_OTGRST\_Pos (26)

95

[ 96](numaker__m46x__reset_8h.md#a93ea373b16e2292f1e0d24482974d7c3)#define NUMAKER\_SYS\_IPRST1\_USBDRST\_Pos (27)

97

[ 98](numaker__m46x__reset_8h.md#abd4a68bada9ec9b229a679554628d720)#define NUMAKER\_SYS\_IPRST1\_EADC0RST\_Pos (28)

99

[ 100](numaker__m46x__reset_8h.md#abe78c9ae1c7d1b090827c31ee2c2bd4b)#define NUMAKER\_SYS\_IPRST1\_I2S0RST\_Pos (29)

101

[ 102](numaker__m46x__reset_8h.md#a5eebf9721505308d82ac2208a6c41983)#define NUMAKER\_SYS\_IPRST1\_HSOTGRST\_Pos (30)

103

[ 104](numaker__m46x__reset_8h.md#a93ccfac0f0de8cc332c26727d71b5051)#define NUMAKER\_SYS\_IPRST1\_TRNGRST\_Pos (31)

105

[ 106](numaker__m46x__reset_8h.md#ac108b395e62293d1ff2d92308a55a722)#define NUMAKER\_SYS\_IPRST2\_SC0RST\_Pos (0)

107

[ 108](numaker__m46x__reset_8h.md#a82e2bfd16943789f3eb36dcd6afe5cbd)#define NUMAKER\_SYS\_IPRST2\_SC1RST\_Pos (1)

109

[ 110](numaker__m46x__reset_8h.md#a2d363f890d96e9fcd3a2f847ef0c7121)#define NUMAKER\_SYS\_IPRST2\_SC2RST\_Pos (2)

111

[ 112](numaker__m46x__reset_8h.md#a89def60dbbb6b4d8ecd699a96d8d754f)#define NUMAKER\_SYS\_IPRST2\_I2C4RST\_Pos (3)

113

[ 114](numaker__m46x__reset_8h.md#a80178616a75bf895b0a38ba44ba54d0b)#define NUMAKER\_SYS\_IPRST2\_QSPI1RST\_Pos (4)

115

[ 116](numaker__m46x__reset_8h.md#aa47fffab39f26dd28b2d9801a1f2306d)#define NUMAKER\_SYS\_IPRST2\_SPI3RST\_Pos (6)

117

[ 118](numaker__m46x__reset_8h.md#a621cb2a73e175103b22901b7e0bd69dc)#define NUMAKER\_SYS\_IPRST2\_SPI4RST\_Pos (7)

119

[ 120](numaker__m46x__reset_8h.md#a927b7a5fcd4f3701e14c95ebe175c91a)#define NUMAKER\_SYS\_IPRST2\_USCI0RST\_Pos (8)

121

[ 122](numaker__m46x__reset_8h.md#aaf8c4d5b99560f8e6979f39ef9ac0572)#define NUMAKER\_SYS\_IPRST2\_PSIORST\_Pos (10)

123

[ 124](numaker__m46x__reset_8h.md#ad229d483e0120d911cf56a2a2b2279ae)#define NUMAKER\_SYS\_IPRST2\_DACRST\_Pos (12)

125

[ 126](numaker__m46x__reset_8h.md#a443248596e273131afff1e2b68b92eab)#define NUMAKER\_SYS\_IPRST2\_ECAP2RST\_Pos (13)

127

[ 128](numaker__m46x__reset_8h.md#ac894c9afeb7981a6e00fc09971252078)#define NUMAKER\_SYS\_IPRST2\_ECAP3RST\_Pos (14)

129

[ 130](numaker__m46x__reset_8h.md#a6d438436bd07d45684cc78d6fca18048)#define NUMAKER\_SYS\_IPRST2\_EPWM0RST\_Pos (16)

131

[ 132](numaker__m46x__reset_8h.md#ac38f0a648912c798d3b9216269af3594)#define NUMAKER\_SYS\_IPRST2\_EPWM1RST\_Pos (17)

133

[ 134](numaker__m46x__reset_8h.md#adb6f3192b3df778a296c07495132b6e7)#define NUMAKER\_SYS\_IPRST2\_BPWM0RST\_Pos (18)

135

[ 136](numaker__m46x__reset_8h.md#a4f18e2c27235651b49c7d40a936fa6d5)#define NUMAKER\_SYS\_IPRST2\_BPWM1RST\_Pos (19)

137

[ 138](numaker__m46x__reset_8h.md#a7b4a4715c395fc8912c9468748954695)#define NUMAKER\_SYS\_IPRST2\_EQEI2RST\_Pos (20)

139

[ 140](numaker__m46x__reset_8h.md#ab4f0e95b00560f63d0bcaf1ae6803216)#define NUMAKER\_SYS\_IPRST2\_EQEI3RST\_Pos (21)

141

[ 142](numaker__m46x__reset_8h.md#ab38f815f1486f551d0d448e0a99670cc)#define NUMAKER\_SYS\_IPRST2\_EQEI0RST\_Pos (22)

143

[ 144](numaker__m46x__reset_8h.md#aa33f02894ffff71676ecddf3d39aae08)#define NUMAKER\_SYS\_IPRST2\_EQEI1RST\_Pos (23)

145

[ 146](numaker__m46x__reset_8h.md#aade8ffd96da178454da6b3325bd31227)#define NUMAKER\_SYS\_IPRST2\_ECAP0RST\_Pos (26)

147

[ 148](numaker__m46x__reset_8h.md#ab2cadf6ec318868cdfbfd478d1225468)#define NUMAKER\_SYS\_IPRST2\_ECAP1RST\_Pos (27)

149

[ 150](numaker__m46x__reset_8h.md#a710145caf48d7020223eca8cab05d18a)#define NUMAKER\_SYS\_IPRST2\_I2S1RST\_Pos (29)

151

[ 152](numaker__m46x__reset_8h.md#a6285ab1379959b9960b37d887789bd5d)#define NUMAKER\_SYS\_IPRST2\_EADC1RST\_Pos (31)

153

[ 154](numaker__m46x__reset_8h.md#ac15246169e029bfd56e95c5ff79fd042)#define NUMAKER\_SYS\_IPRST3\_KPIRST\_Pos (0)

155

[ 156](numaker__m46x__reset_8h.md#a3baa32da44621bf50f44c519ccbb6be8)#define NUMAKER\_SYS\_IPRST3\_EADC2RST\_Pos (6)

157

[ 158](numaker__m46x__reset_8h.md#a54a03c6ae788b23a19de9d48bb50a792)#define NUMAKER\_SYS\_IPRST3\_ACMP23RST\_Pos (7)

159

[ 160](numaker__m46x__reset_8h.md#ac5a7c67f4371c8ba5ff5e5138e9ad8bf)#define NUMAKER\_SYS\_IPRST3\_SPI5RST\_Pos (8)

161

[ 162](numaker__m46x__reset_8h.md#ab80f88918ae9e3f4115b7350edee255f)#define NUMAKER\_SYS\_IPRST3\_SPI6RST\_Pos (9)

163

[ 164](numaker__m46x__reset_8h.md#a8fec9bbce9ff84347467b4b33507425a)#define NUMAKER\_SYS\_IPRST3\_SPI7RST\_Pos (10)

165

[ 166](numaker__m46x__reset_8h.md#a40bdcc4efd41c9a615eade873f3f46b2)#define NUMAKER\_SYS\_IPRST3\_SPI8RST\_Pos (11)

167

[ 168](numaker__m46x__reset_8h.md#aa015a4bba4f8a7ff99e4039f477bc63f)#define NUMAKER\_SYS\_IPRST3\_SPI9RST\_Pos (12)

169

[ 170](numaker__m46x__reset_8h.md#af6774dab68735fe66f165bb66a6ee092)#define NUMAKER\_SYS\_IPRST3\_SPI10RST\_Pos (13)

171

[ 172](numaker__m46x__reset_8h.md#a975862229a1426ae8b2c7bcc045ed8c8)#define NUMAKER\_SYS\_IPRST3\_UART8RST\_Pos (16)

173

[ 174](numaker__m46x__reset_8h.md#a9b7371eeb9f40864b22bbf4d8945f6ac)#define NUMAKER\_SYS\_IPRST3\_UART9RST\_Pos (17)

175

176/\* End of M460 BSP sys\_reg.h reset module copy \*/

177

178/\* Beginning of M460 BSP sys.h reset module copy \*/

179

180/\*---------------------------------------------------------------------

181 \* Module Reset Control Resister constant definitions.

182 \*---------------------------------------------------------------------

183 \*/

[ 184](numaker__m46x__reset_8h.md#a2ec945f466041bba124cd635cc6667dc)#define NUMAKER\_PDMA0\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_PDMA0RST\_Pos)

[ 185](numaker__m46x__reset_8h.md#a4de27d07239c747bdae9e173c6abfd17)#define NUMAKER\_EBI\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_EBIRST\_Pos)

[ 186](numaker__m46x__reset_8h.md#a3b1865a84d0278666b2aa69a6ed15de7)#define NUMAKER\_EMAC0\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_EMAC0RST\_Pos)

[ 187](numaker__m46x__reset_8h.md#aff9c7a29e100810a67057224174fb0ba)#define NUMAKER\_SDH0\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_SDH0RST\_Pos)

[ 188](numaker__m46x__reset_8h.md#a9e10d08e25bcce46419e595468ee2140)#define NUMAKER\_CRC\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CRCRST\_Pos)

[ 189](numaker__m46x__reset_8h.md#a7eaaeb46b33e91cf1372fcddc7f856e4)#define NUMAKER\_CCAP\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CCAPRST\_Pos)

[ 190](numaker__m46x__reset_8h.md#a7a9f80ff06b42845eb7fc21800e200ce)#define NUMAKER\_HSUSBD\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_HSUSBDRST\_Pos)

[ 191](numaker__m46x__reset_8h.md#ad0c541f516a939275d74297596a03c7f)#define NUMAKER\_HBI\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_HBIRST\_Pos)

[ 192](numaker__m46x__reset_8h.md#a53316015ee2c28580760707b597382f7)#define NUMAKER\_CRPT\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CRPTRST\_Pos)

[ 193](numaker__m46x__reset_8h.md#a8d447a640e42fede5cc51033c2c61c2d)#define NUMAKER\_KS\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_KSRST\_Pos)

[ 194](numaker__m46x__reset_8h.md#a90aa0e7587a1b4ad7aa7c58065723e24)#define NUMAKER\_SPIM\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_SPIMRST\_Pos)

[ 195](numaker__m46x__reset_8h.md#aa0e56c0249450798639c6395a1594e88)#define NUMAKER\_HSUSBH\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_HSUSBHRST\_Pos)

[ 196](numaker__m46x__reset_8h.md#a81c59151bff5d15bdbb116ec2790a3b6)#define NUMAKER\_SDH1\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_SDH1RST\_Pos)

[ 197](numaker__m46x__reset_8h.md#a30f10524f2e8321564df3116ca3de24f)#define NUMAKER\_PDMA1\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_PDMA1RST\_Pos)

[ 198](numaker__m46x__reset_8h.md#a37c923029e0439dd6b1c449fc81c40f4)#define NUMAKER\_CANFD0\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CANFD0RST\_Pos)

[ 199](numaker__m46x__reset_8h.md#aa3cde3062807637c383a6a11affbace6)#define NUMAKER\_CANFD1\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CANFD1RST\_Pos)

[ 200](numaker__m46x__reset_8h.md#abd2303639e2ddc97f23cd0e9a77ae0c1)#define NUMAKER\_CANFD2\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CANFD2RST\_Pos)

[ 201](numaker__m46x__reset_8h.md#ae045c7f803c1e66748a671d9ed90c5a3)#define NUMAKER\_CANFD3\_RST ((0UL << 24) | NUMAKER\_SYS\_IPRST0\_CANFD3RST\_Pos)

202

[ 203](numaker__m46x__reset_8h.md#a78b715193110ab7029d220d288132bb6)#define NUMAKER\_GPIO\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_GPIORST\_Pos)

[ 204](numaker__m46x__reset_8h.md#af5659ce27a84e17aeeb50cd2edb423c7)#define NUMAKER\_TMR0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_TMR0RST\_Pos)

[ 205](numaker__m46x__reset_8h.md#a7a8501e84864c5810d9e03e2c261bcd4)#define NUMAKER\_TMR1\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_TMR1RST\_Pos)

[ 206](numaker__m46x__reset_8h.md#a0e7f53329931eab01b15ba09d0b1b2a4)#define NUMAKER\_TMR2\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_TMR2RST\_Pos)

[ 207](numaker__m46x__reset_8h.md#a8e77d7bfed00350408e6d1cfe010a366)#define NUMAKER\_TMR3\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_TMR3RST\_Pos)

[ 208](numaker__m46x__reset_8h.md#a16163237a6cbb88ef60dd465b137b0c3)#define NUMAKER\_ACMP01\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_ACMP01RST\_Pos)

[ 209](numaker__m46x__reset_8h.md#a59c61b565df006bfff587f3468c7c0c6)#define NUMAKER\_I2C0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_I2C0RST\_Pos)

[ 210](numaker__m46x__reset_8h.md#ad7061d30f5fffad6396f499c4e703f30)#define NUMAKER\_I2C1\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_I2C1RST\_Pos)

[ 211](numaker__m46x__reset_8h.md#abee67c7820c016fa124e6a6d96451ac9)#define NUMAKER\_I2C2\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_I2C2RST\_Pos)

[ 212](numaker__m46x__reset_8h.md#a6395be9706c311db84f3563382d52482)#define NUMAKER\_I2C3\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_I2C3RST\_Pos)

[ 213](numaker__m46x__reset_8h.md#ad95c0f26b66c02b0d76ada07e4a8ae4f)#define NUMAKER\_QSPI0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_QSPI0RST\_Pos)

[ 214](numaker__m46x__reset_8h.md#ac26b4c587af3877bab01d38fa51fae2c)#define NUMAKER\_SPI0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_SPI0RST\_Pos)

[ 215](numaker__m46x__reset_8h.md#a6ed8951e79509205becde2782955edc3)#define NUMAKER\_SPI1\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_SPI1RST\_Pos)

[ 216](numaker__m46x__reset_8h.md#aea94605fb578f4e80084db8c24700173)#define NUMAKER\_SPI2\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_SPI2RST\_Pos)

[ 217](numaker__m46x__reset_8h.md#a0ca6e29af1512259983d74592d86c8ac)#define NUMAKER\_UART0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART0RST\_Pos)

[ 218](numaker__m46x__reset_8h.md#a855263435d644be9a655aafaa6997e57)#define NUMAKER\_UART1\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART1RST\_Pos)

[ 219](numaker__m46x__reset_8h.md#acc518471fe73a842b39a56a6c2a3d208)#define NUMAKER\_UART2\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART2RST\_Pos)

[ 220](numaker__m46x__reset_8h.md#a451f38258887da534ee5c75e6dfcc28a)#define NUMAKER\_UART3\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART3RST\_Pos)

[ 221](numaker__m46x__reset_8h.md#a74a3f05297b2014947e13c9e8fd7fd14)#define NUMAKER\_UART4\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART4RST\_Pos)

[ 222](numaker__m46x__reset_8h.md#a83b12f8d7cc1822080bb088730033c5d)#define NUMAKER\_UART5\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART5RST\_Pos)

[ 223](numaker__m46x__reset_8h.md#a42e7f4a4a1f585df59b03928f1b95b11)#define NUMAKER\_UART6\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART6RST\_Pos)

[ 224](numaker__m46x__reset_8h.md#aa4f97772ca5218ae52d2105e722db6fc)#define NUMAKER\_UART7\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_UART7RST\_Pos)

[ 225](numaker__m46x__reset_8h.md#a93cde8c56f474777ba4fe7ff47fe8f14)#define NUMAKER\_OTG\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_OTGRST\_Pos)

[ 226](numaker__m46x__reset_8h.md#a1a74ded775d85a498a044529857c5826)#define NUMAKER\_USBD\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_USBDRST\_Pos)

[ 227](numaker__m46x__reset_8h.md#abfb255d99741ffe50d400a09b8a80787)#define NUMAKER\_EADC0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_EADC0RST\_Pos)

[ 228](numaker__m46x__reset_8h.md#a03ef0de3b74746a046ecb95a3a67d118)#define NUMAKER\_I2S0\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_I2S0RST\_Pos)

[ 229](numaker__m46x__reset_8h.md#a15039533325b936d624688eba49fa195)#define NUMAKER\_HSOTG\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_HSOTGRST\_Pos)

[ 230](numaker__m46x__reset_8h.md#a7d1dca0f73d12f8cad5d4fb3941e9a34)#define NUMAKER\_TRNG\_RST ((4UL << 24) | NUMAKER\_SYS\_IPRST1\_TRNGRST\_Pos)

231

[ 232](numaker__m46x__reset_8h.md#a245990b674440f81d430747866a4b361)#define NUMAKER\_SC0\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_SC0RST\_Pos)

[ 233](numaker__m46x__reset_8h.md#abd5924e1da2047c5f03d57c153f4e347)#define NUMAKER\_SC1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_SC1RST\_Pos)

[ 234](numaker__m46x__reset_8h.md#a59744aefc103b03a7a913082cecbbfdf)#define NUMAKER\_SC2\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_SC2RST\_Pos)

[ 235](numaker__m46x__reset_8h.md#a19253588c50f22717fcc85342a1d6953)#define NUMAKER\_I2C4\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_I2C4RST\_Pos)

[ 236](numaker__m46x__reset_8h.md#af974026a64f61a9f99f83ae3f6512b11)#define NUMAKER\_QSPI1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_QSPI1RST\_Pos)

[ 237](numaker__m46x__reset_8h.md#a62670f2e3ed7a343b0d8338cf18484ce)#define NUMAKER\_SPI3\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_SPI3RST\_Pos)

[ 238](numaker__m46x__reset_8h.md#a1ebef886aa8911b2faa3031faeeb872c)#define NUMAKER\_SPI4\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_SPI4RST\_Pos)

[ 239](numaker__m46x__reset_8h.md#ab7e650d5582aa2f623f075c5b2c2dce5)#define NUMAKER\_USCI0\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_USCI0RST\_Pos)

[ 240](numaker__m46x__reset_8h.md#a01d5fab6c29b3716a89971f528f4eaaa)#define NUMAKER\_PSIO\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_PSIORST\_Pos)

[ 241](numaker__m46x__reset_8h.md#aa244c6cee2327a190b27856b83446913)#define NUMAKER\_DAC\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_DACRST\_Pos)

[ 242](numaker__m46x__reset_8h.md#ac7fcfa9b1c8e15744d413acb643202f7)#define NUMAKER\_EPWM0\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EPWM0RST\_Pos)

[ 243](numaker__m46x__reset_8h.md#a529ccc59cc243788d18e63f519cfe5c7)#define NUMAKER\_EPWM1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EPWM1RST\_Pos)

[ 244](numaker__m46x__reset_8h.md#acc414db67e10f45e8a24d29175ee233d)#define NUMAKER\_BPWM0\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_BPWM0RST\_Pos)

[ 245](numaker__m46x__reset_8h.md#a8fb8d5dd324e35f28c6a26bb0d0b170e)#define NUMAKER\_BPWM1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_BPWM1RST\_Pos)

[ 246](numaker__m46x__reset_8h.md#aaa793688d87486488dca737c346bfc8d)#define NUMAKER\_EQEI0\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EQEI0RST\_Pos)

[ 247](numaker__m46x__reset_8h.md#af1b3595e1191835a0a3a35b6a1949c2a)#define NUMAKER\_EQEI1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EQEI1RST\_Pos)

[ 248](numaker__m46x__reset_8h.md#a61b8b9e037b37b3dc3ed37edd60dc50a)#define NUMAKER\_EQEI2\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EQEI2RST\_Pos)

[ 249](numaker__m46x__reset_8h.md#abc7ed91549dae87975100a50a88d2bff)#define NUMAKER\_EQEI3\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EQEI3RST\_Pos)

[ 250](numaker__m46x__reset_8h.md#a423d4739b6f1c7092608a2fb1eef4909)#define NUMAKER\_ECAP0\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_ECAP0RST\_Pos)

[ 251](numaker__m46x__reset_8h.md#ae8be7edf8c201921491a45aef91cc565)#define NUMAKER\_ECAP1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_ECAP1RST\_Pos)

[ 252](numaker__m46x__reset_8h.md#ae05bc356cec6067442e574af9c1e47db)#define NUMAKER\_ECAP2\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_ECAP2RST\_Pos)

[ 253](numaker__m46x__reset_8h.md#ab7c2a8a97a8250ed95c021515abe1e8b)#define NUMAKER\_ECAP3\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_ECAP3RST\_Pos)

[ 254](numaker__m46x__reset_8h.md#a44c2a01d3538f6cc8e7b5085d9b97acd)#define NUMAKER\_I2S1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_I2S1RST\_Pos)

[ 255](numaker__m46x__reset_8h.md#a871ce18fa9048621659df0295f294a7c)#define NUMAKER\_EADC1\_RST ((8UL << 24) | NUMAKER\_SYS\_IPRST2\_EADC1RST\_Pos)

256

[ 257](numaker__m46x__reset_8h.md#af7c4f0dfde6c7860bf6d7044dcc17f4c)#define NUMAKER\_KPI\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_KPIRST\_Pos)

[ 258](numaker__m46x__reset_8h.md#ae7e962c1d85a1adc401ee40246f01f3b)#define NUMAKER\_EADC2\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_EADC2RST\_Pos)

[ 259](numaker__m46x__reset_8h.md#ad147e483d60833d8ae5d24f6a713c028)#define NUMAKER\_ACMP23\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_ACMP23RST\_Pos)

[ 260](numaker__m46x__reset_8h.md#a1bb081ae3dfbf7e810ed9b48482f7e8b)#define NUMAKER\_SPI5\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_SPI5RST\_Pos)

[ 261](numaker__m46x__reset_8h.md#a2fc81466d5d6885fb6d71768469ca281)#define NUMAKER\_SPI6\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_SPI6RST\_Pos)

[ 262](numaker__m46x__reset_8h.md#a290eaa04c3906d7997066d62ec5093d7)#define NUMAKER\_SPI7\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_SPI7RST\_Pos)

[ 263](numaker__m46x__reset_8h.md#a47e03830fc7aa97cfcecd650174697b6)#define NUMAKER\_SPI8\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_SPI8RST\_Pos)

[ 264](numaker__m46x__reset_8h.md#a1682fd48569227082fef66d973893d7a)#define NUMAKER\_SPI9\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_SPI9RST\_Pos)

[ 265](numaker__m46x__reset_8h.md#a39989e15be7179b07216514970969bf0)#define NUMAKER\_SPI10\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_SPI10RST\_Pos)

[ 266](numaker__m46x__reset_8h.md#adb20e898d770ace2319ede3852216566)#define NUMAKER\_UART8\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_UART8RST\_Pos)

[ 267](numaker__m46x__reset_8h.md#ac9e61e7657c7973bbc1c735abf5e2b45)#define NUMAKER\_UART9\_RST ((0x18UL << 24) | NUMAKER\_SYS\_IPRST3\_UART9RST\_Pos)

268

269/\* End of M460 BSP sys.h reset module copy \*/

270

271#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [numaker\_m46x\_reset.h](numaker__m46x__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
