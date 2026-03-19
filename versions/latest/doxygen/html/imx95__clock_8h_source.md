---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/imx95__clock_8h_source.html
original_path: doxygen/html/imx95__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx95\_clock.h

[Go to the documentation of this file.](imx95__clock_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX95\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX95\_CLOCK\_H\_

9

[ 10](imx95__clock_8h.md#a9b7a93883568b4cb2cf3d5423dd15382)#define IMX95\_CLK\_32K 1

[ 11](imx95__clock_8h.md#a50188fa88fc1c2d48d850ba015f40b59)#define IMX95\_CLK\_24M 2

[ 12](imx95__clock_8h.md#a7efab51377f0fe06199fd0ecf716fbdf)#define IMX95\_CLK\_FRO 3

[ 13](imx95__clock_8h.md#ac39c98ecf7bcbcd3a99b12c2503f2cf2)#define IMX95\_CLK\_SYSPLL1\_VCO 4

[ 14](imx95__clock_8h.md#ae3745afcc7b4ed45b1fc0835c813afdd)#define IMX95\_CLK\_SYSPLL1\_PFD0\_UNGATED 5

[ 15](imx95__clock_8h.md#ab26746047d8d3f210098dfeeadbae96a)#define IMX95\_CLK\_SYSPLL1\_PFD0 6

[ 16](imx95__clock_8h.md#a639f6c5cae063999f8b125b96e066e74)#define IMX95\_CLK\_SYSPLL1\_PFD0\_DIV2 7

[ 17](imx95__clock_8h.md#a1a0f15273871d7afee6eec921f33e8c5)#define IMX95\_CLK\_SYSPLL1\_PFD1\_UNGATED 8

[ 18](imx95__clock_8h.md#a22ed1cf87d7966fc1fadffc684a644e9)#define IMX95\_CLK\_SYSPLL1\_PFD1 9

[ 19](imx95__clock_8h.md#a1c671f88f11ddf7edfa27ca2191a8c68)#define IMX95\_CLK\_SYSPLL1\_PFD1\_DIV2 10

[ 20](imx95__clock_8h.md#a29ac83757b5f884cc619dcf008e19fc2)#define IMX95\_CLK\_SYSPLL1\_PFD2\_UNGATED 11

[ 21](imx95__clock_8h.md#a6e23bb04b1ea546600b7b11190030923)#define IMX95\_CLK\_SYSPLL1\_PFD2 12

[ 22](imx95__clock_8h.md#a0439bed47334261f8ee30ab20a4ef15f)#define IMX95\_CLK\_SYSPLL1\_PFD2\_DIV2 13

[ 23](imx95__clock_8h.md#abebadc4aea8ddb29cd14db8840d06543)#define IMX95\_CLK\_AUDIOPLL1\_VCO 14

[ 24](imx95__clock_8h.md#a6360521a2d12efe2ef835708c22e7943)#define IMX95\_CLK\_AUDIOPLL1 15

[ 25](imx95__clock_8h.md#ad1ccae7142f7cae92f5abfaac725e5cc)#define IMX95\_CLK\_AUDIOPLL2\_VCO 16

[ 26](imx95__clock_8h.md#a8001def86799113e3d326051ffaf4647)#define IMX95\_CLK\_AUDIOPLL2 17

[ 27](imx95__clock_8h.md#a5a733a857af74137409cf887d9661254)#define IMX95\_CLK\_VIDEOPLL1\_VCO 18

[ 28](imx95__clock_8h.md#ad2a1434edb64ba5433aef11f544d1859)#define IMX95\_CLK\_VIDEOPLL1 19

[ 29](imx95__clock_8h.md#ac687438f6612c26279c4c98691c401d0)#define IMX95\_CLK\_RESERVED20 20

[ 30](imx95__clock_8h.md#ad49a22358efb0b06476dc3c64cede59b)#define IMX95\_CLK\_RESERVED21 21

[ 31](imx95__clock_8h.md#add1d521f5a1914c4fc20eaa5c4165d1f)#define IMX95\_CLK\_RESERVED22 22

[ 32](imx95__clock_8h.md#a0b0c1ca8fd4b47e659a9e0668c7af452)#define IMX95\_CLK\_RESERVED23 23

[ 33](imx95__clock_8h.md#a1f497ddbc46406a4c940ad114d5bcfea)#define IMX95\_CLK\_ARMPLL\_VCO 24

[ 34](imx95__clock_8h.md#a5fe8c5d32e6903a6b3a039ab4c2d6abf)#define IMX95\_CLK\_ARMPLL\_PFD0\_UNGATED 25

[ 35](imx95__clock_8h.md#ac6824e0992296068db39f93fc0a146c8)#define IMX95\_CLK\_ARMPLL\_PFD0 26

[ 36](imx95__clock_8h.md#a41a8d9a8c1093e732a8fcb390102faa7)#define IMX95\_CLK\_ARMPLL\_PFD1\_UNGATED 27

[ 37](imx95__clock_8h.md#a5380ee5c8d198af1aae96b5d6b2a398d)#define IMX95\_CLK\_ARMPLL\_PFD1 28

[ 38](imx95__clock_8h.md#a4e223d7794eb60dcc81a31971247387e)#define IMX95\_CLK\_ARMPLL\_PFD2\_UNGATED 29

[ 39](imx95__clock_8h.md#ae5628a72f1fcfc4b0e1035e741a9bbf3)#define IMX95\_CLK\_ARMPLL\_PFD2 30

[ 40](imx95__clock_8h.md#a04f223bbca0b96450b7aeb5de1ea55ee)#define IMX95\_CLK\_ARMPLL\_PFD3\_UNGATED 31

[ 41](imx95__clock_8h.md#a876ff18330c760a8c960011c179f832e)#define IMX95\_CLK\_ARMPLL\_PFD3 32

[ 42](imx95__clock_8h.md#a8db3aba1c1722a3ed16a5450bd8b417f)#define IMX95\_CLK\_DRAMPLL\_VCO 33

[ 43](imx95__clock_8h.md#a025f75b9c34c46d8fac5fc04e3bdef5c)#define IMX95\_CLK\_DRAMPLL 34

[ 44](imx95__clock_8h.md#a3c45a888f5231c1c1333dba4156c705a)#define IMX95\_CLK\_HSIOPLL\_VCO 35

[ 45](imx95__clock_8h.md#a2dca92af9fe947f2d45d6450e526ae21)#define IMX95\_CLK\_HSIOPLL 36

[ 46](imx95__clock_8h.md#a1c1b4f20c705ae9325728eb413aa2be8)#define IMX95\_CLK\_LDBPLL\_VCO 37

[ 47](imx95__clock_8h.md#a4fac68429d60d6641173125f406046b9)#define IMX95\_CLK\_LDBPLL 38

[ 48](imx95__clock_8h.md#a9a49891a24cefe3652dffb0e92b0a312)#define IMX95\_CLK\_EXT1 39

[ 49](imx95__clock_8h.md#a87f05b646d2432c8cce8a9d439086307)#define IMX95\_CLK\_EXT2 40

50

[ 51](imx95__clock_8h.md#a48935720ce23759a6b1824b70073a6e7)#define IMX95\_CCM\_NUM\_CLK\_SRC 41

52

[ 53](imx95__clock_8h.md#ac3dad59139f69f7838a21fe829d5c23f)#define IMX95\_CLK\_ADC (IMX95\_CCM\_NUM\_CLK\_SRC + 0)

[ 54](imx95__clock_8h.md#ab16ac4da8c60535446c3a7e87ddfcb6f)#define IMX95\_CLK\_TMU (IMX95\_CCM\_NUM\_CLK\_SRC + 1)

[ 55](imx95__clock_8h.md#a14dcbbdcd2016d0f513a54ba945f898e)#define IMX95\_CLK\_BUSAON (IMX95\_CCM\_NUM\_CLK\_SRC + 2)

[ 56](imx95__clock_8h.md#ace6c1fc4e24b54762fe6644b47ec0548)#define IMX95\_CLK\_CAN1 (IMX95\_CCM\_NUM\_CLK\_SRC + 3)

[ 57](imx95__clock_8h.md#a5e5e1926cc0b28a24cfcaec8434f0eaf)#define IMX95\_CLK\_I3C1 (IMX95\_CCM\_NUM\_CLK\_SRC + 4)

[ 58](imx95__clock_8h.md#a8dd784dacbe71ba5e6f7eed6a38b9397)#define IMX95\_CLK\_I3C1SLOW (IMX95\_CCM\_NUM\_CLK\_SRC + 5)

[ 59](imx95__clock_8h.md#a26950c20cc46aa070792fe79621d3e66)#define IMX95\_CLK\_LPI2C1 (IMX95\_CCM\_NUM\_CLK\_SRC + 6)

[ 60](imx95__clock_8h.md#a4100e4afcbcf832db0904508f6e4ab82)#define IMX95\_CLK\_LPI2C2 (IMX95\_CCM\_NUM\_CLK\_SRC + 7)

[ 61](imx95__clock_8h.md#add133d1c064166a2f17cd22500e8306d)#define IMX95\_CLK\_LPSPI1 (IMX95\_CCM\_NUM\_CLK\_SRC + 8)

[ 62](imx95__clock_8h.md#aeb62a62483ef9530d3d6248d098114e1)#define IMX95\_CLK\_LPSPI2 (IMX95\_CCM\_NUM\_CLK\_SRC + 9)

[ 63](imx95__clock_8h.md#aca5a1e4b7d771ae8c60b5fa644134656)#define IMX95\_CLK\_LPTMR1 (IMX95\_CCM\_NUM\_CLK\_SRC + 10)

[ 64](imx95__clock_8h.md#ad8972c6a9ef18fa14a4675aacb0a3bda)#define IMX95\_CLK\_LPUART1 (IMX95\_CCM\_NUM\_CLK\_SRC + 11)

[ 65](imx95__clock_8h.md#a3ded16e9f23e46bde058469bafa54fdc)#define IMX95\_CLK\_LPUART2 (IMX95\_CCM\_NUM\_CLK\_SRC + 12)

[ 66](imx95__clock_8h.md#a19d1490500bd20be349a617baecb589a)#define IMX95\_CLK\_M33 (IMX95\_CCM\_NUM\_CLK\_SRC + 13)

[ 67](imx95__clock_8h.md#ab7503b76b01a60422dde7679581ee53f)#define IMX95\_CLK\_M33SYSTICK (IMX95\_CCM\_NUM\_CLK\_SRC + 14)

[ 68](imx95__clock_8h.md#abe2ee50fa44e196420814f32e0412084)#define IMX95\_CLK\_MQS1 (IMX95\_CCM\_NUM\_CLK\_SRC + 15)

[ 69](imx95__clock_8h.md#aa4d7068eec9ac85fa8bd041a4deeb292)#define IMX95\_CLK\_PDM (IMX95\_CCM\_NUM\_CLK\_SRC + 16)

[ 70](imx95__clock_8h.md#a7b0df640d992e18c3dd9de9fa8dce73c)#define IMX95\_CLK\_SAI1 (IMX95\_CCM\_NUM\_CLK\_SRC + 17)

[ 71](imx95__clock_8h.md#aec589270076706a36ff7dcc0967afb09)#define IMX95\_CLK\_SENTINEL (IMX95\_CCM\_NUM\_CLK\_SRC + 18)

[ 72](imx95__clock_8h.md#a6d0ed1aa172d45c4977c9213762c37de)#define IMX95\_CLK\_TPM2 (IMX95\_CCM\_NUM\_CLK\_SRC + 19)

[ 73](imx95__clock_8h.md#a32100013dc0ede7af510aa576d51a5fe)#define IMX95\_CLK\_TSTMR1 (IMX95\_CCM\_NUM\_CLK\_SRC + 20)

[ 74](imx95__clock_8h.md#aa6dfb3ea7a7b06ad7e32e44097b4ff63)#define IMX95\_CLK\_CAMAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 21)

[ 75](imx95__clock_8h.md#ae5635a0f77ba667af8b793e04e70dc8c)#define IMX95\_CLK\_CAMAXI (IMX95\_CCM\_NUM\_CLK\_SRC + 22)

[ 76](imx95__clock_8h.md#a55921f0998568d8cc755f52323514afb)#define IMX95\_CLK\_CAMCM0 (IMX95\_CCM\_NUM\_CLK\_SRC + 23)

[ 77](imx95__clock_8h.md#acdf74a0dd94e3968b82fbbdd6d7ea2f7)#define IMX95\_CLK\_CAMISI (IMX95\_CCM\_NUM\_CLK\_SRC + 24)

[ 78](imx95__clock_8h.md#a976ffb49e7fdaf80988eb356d4db1c93)#define IMX95\_CLK\_MIPIPHYCFG (IMX95\_CCM\_NUM\_CLK\_SRC + 25)

[ 79](imx95__clock_8h.md#a8594724a101ae1c4da668e5289ca4fd0)#define IMX95\_CLK\_MIPIPHYPLLBYPASS (IMX95\_CCM\_NUM\_CLK\_SRC + 26)

[ 80](imx95__clock_8h.md#a5764e912b985633e61c89627306e8c2d)#define IMX95\_CLK\_MIPIPHYPLLREF (IMX95\_CCM\_NUM\_CLK\_SRC + 27)

[ 81](imx95__clock_8h.md#a5fca62080a438890412845e2f011698e)#define IMX95\_CLK\_MIPITESTBYTE (IMX95\_CCM\_NUM\_CLK\_SRC + 28)

[ 82](imx95__clock_8h.md#a56d88258ba89195b026cf704134880cc)#define IMX95\_CLK\_A55 (IMX95\_CCM\_NUM\_CLK\_SRC + 29)

[ 83](imx95__clock_8h.md#ad31c0d84b478943b8e87e6ce33e66b16)#define IMX95\_CLK\_A55MTRBUS (IMX95\_CCM\_NUM\_CLK\_SRC + 30)

[ 84](imx95__clock_8h.md#af58b21cdca480df1e2f1aacd79c905ec)#define IMX95\_CLK\_A55PERIPH (IMX95\_CCM\_NUM\_CLK\_SRC + 31)

[ 85](imx95__clock_8h.md#a4a6e074d72f5a2fa32956da0369c4bbf)#define IMX95\_CLK\_DRAMALT (IMX95\_CCM\_NUM\_CLK\_SRC + 32)

[ 86](imx95__clock_8h.md#a6f873149adc683d4642760d270de0fd8)#define IMX95\_CLK\_DRAMAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 33)

[ 87](imx95__clock_8h.md#a4261fc63f0cd9c985e032965bf28b00c)#define IMX95\_CLK\_DISPAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 34)

[ 88](imx95__clock_8h.md#a399eadfc95c65c7b2af73837e562c565)#define IMX95\_CLK\_DISPAXI (IMX95\_CCM\_NUM\_CLK\_SRC + 35)

[ 89](imx95__clock_8h.md#a632b6d13b8d4ae3c05aaa7ea031858b1)#define IMX95\_CLK\_DISPDP (IMX95\_CCM\_NUM\_CLK\_SRC + 36)

[ 90](imx95__clock_8h.md#a2ced89227e852d09b774a26fa51bcd27)#define IMX95\_CLK\_DISPOCRAM (IMX95\_CCM\_NUM\_CLK\_SRC + 37)

[ 91](imx95__clock_8h.md#a28c0e25ba1597aa611cd45c1275ae2b0)#define IMX95\_CLK\_DISPUSB31 (IMX95\_CCM\_NUM\_CLK\_SRC + 38)

[ 92](imx95__clock_8h.md#a2987bc135c5799deea9458fd9d4c800c)#define IMX95\_CLK\_DISP1PIX (IMX95\_CCM\_NUM\_CLK\_SRC + 39)

[ 93](imx95__clock_8h.md#a315f6c4f07135be89aab0a578a9f294c)#define IMX95\_CLK\_DISP2PIX (IMX95\_CCM\_NUM\_CLK\_SRC + 40)

[ 94](imx95__clock_8h.md#a3e5f2878e3c7d35db3d47d07d4af15b4)#define IMX95\_CLK\_DISP3PIX (IMX95\_CCM\_NUM\_CLK\_SRC + 41)

[ 95](imx95__clock_8h.md#a1198b0b28897c91a7772f35b542b36ad)#define IMX95\_CLK\_GPUAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 42)

[ 96](imx95__clock_8h.md#a30cdba4628e6b94ff88a71471c14ef72)#define IMX95\_CLK\_GPU (IMX95\_CCM\_NUM\_CLK\_SRC + 43)

[ 97](imx95__clock_8h.md#a6b944b0dca2375ee33b515c6091f8583)#define IMX95\_CLK\_HSIOACSCAN480M (IMX95\_CCM\_NUM\_CLK\_SRC + 44)

[ 98](imx95__clock_8h.md#a45edde4cf4df7004edf9e1e2b783a667)#define IMX95\_CLK\_HSIOACSCAN80M (IMX95\_CCM\_NUM\_CLK\_SRC + 45)

[ 99](imx95__clock_8h.md#ab6b35af924e424df86f8a113d0f983fb)#define IMX95\_CLK\_HSIO (IMX95\_CCM\_NUM\_CLK\_SRC + 46)

[ 100](imx95__clock_8h.md#a50e39bed2228cf0ef4b4031613e3b4cf)#define IMX95\_CLK\_HSIOPCIEAUX (IMX95\_CCM\_NUM\_CLK\_SRC + 47)

[ 101](imx95__clock_8h.md#ad85e7278719127b827fa797b3c753320)#define IMX95\_CLK\_HSIOPCIETEST160M (IMX95\_CCM\_NUM\_CLK\_SRC + 48)

[ 102](imx95__clock_8h.md#a0e19d77e4dbf5e93ab9ba272d5961cd7)#define IMX95\_CLK\_HSIOPCIETEST400M (IMX95\_CCM\_NUM\_CLK\_SRC + 49)

[ 103](imx95__clock_8h.md#a9c5a5b2f7bfe6235b148c35767dcd592)#define IMX95\_CLK\_HSIOPCIETEST500M (IMX95\_CCM\_NUM\_CLK\_SRC + 50)

[ 104](imx95__clock_8h.md#a3cc32aefd925642c82c2274c361d5310)#define IMX95\_CLK\_HSIOUSBTEST50M (IMX95\_CCM\_NUM\_CLK\_SRC + 51)

[ 105](imx95__clock_8h.md#a07da64e5baefc91a5827a4d757ff085e)#define IMX95\_CLK\_HSIOUSBTEST60M (IMX95\_CCM\_NUM\_CLK\_SRC + 52)

[ 106](imx95__clock_8h.md#afc1e1a1daa92656be092d253a182e33b)#define IMX95\_CLK\_BUSM7 (IMX95\_CCM\_NUM\_CLK\_SRC + 53)

[ 107](imx95__clock_8h.md#a5adefbba53cf5bc3fcacec63897fb19c)#define IMX95\_CLK\_M7 (IMX95\_CCM\_NUM\_CLK\_SRC + 54)

[ 108](imx95__clock_8h.md#a266fd71db83f0daef8747aa60b1e6b50)#define IMX95\_CLK\_M7SYSTICK (IMX95\_CCM\_NUM\_CLK\_SRC + 55)

[ 109](imx95__clock_8h.md#a61c81f4d72e1ec5d63b5a3dc4f06457f)#define IMX95\_CLK\_BUSNETCMIX (IMX95\_CCM\_NUM\_CLK\_SRC + 56)

[ 110](imx95__clock_8h.md#a17f3aa440ee4d83387b02bb9cb65f336)#define IMX95\_CLK\_ENET (IMX95\_CCM\_NUM\_CLK\_SRC + 57)

[ 111](imx95__clock_8h.md#aecf1b5b67163853a97116704137f2e8e)#define IMX95\_CLK\_ENETPHYTEST200M (IMX95\_CCM\_NUM\_CLK\_SRC + 58)

[ 112](imx95__clock_8h.md#aeebde7fc608e18fc7fb4c0b444fbb603)#define IMX95\_CLK\_ENETPHYTEST500M (IMX95\_CCM\_NUM\_CLK\_SRC + 59)

[ 113](imx95__clock_8h.md#a4842b46fa07e43945cd0e28fe828b47c)#define IMX95\_CLK\_ENETPHYTEST667M (IMX95\_CCM\_NUM\_CLK\_SRC + 60)

[ 114](imx95__clock_8h.md#a5d3964c90afe897038ee74763a27d836)#define IMX95\_CLK\_ENETREF (IMX95\_CCM\_NUM\_CLK\_SRC + 61)

[ 115](imx95__clock_8h.md#adbca39599f265e95d10c59b83c42ef19)#define IMX95\_CLK\_ENETTIMER1 (IMX95\_CCM\_NUM\_CLK\_SRC + 62)

[ 116](imx95__clock_8h.md#ae3c58c0d05e06b5f8e7a5e4c87334227)#define IMX95\_CLK\_MQS2 (IMX95\_CCM\_NUM\_CLK\_SRC + 63)

[ 117](imx95__clock_8h.md#a740addcece917bd64bebc5b929797964)#define IMX95\_CLK\_SAI2 (IMX95\_CCM\_NUM\_CLK\_SRC + 64)

[ 118](imx95__clock_8h.md#ac949c05475f80694d5073afd0b110e2a)#define IMX95\_CLK\_NOCAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 65)

[ 119](imx95__clock_8h.md#a64e5aea357605df3be1f7e0199c9146b)#define IMX95\_CLK\_NOC (IMX95\_CCM\_NUM\_CLK\_SRC + 66)

[ 120](imx95__clock_8h.md#a4859a8be753eb018f3c5f86019da20a4)#define IMX95\_CLK\_NPUAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 67)

[ 121](imx95__clock_8h.md#aa99cecc3e20d32b9cb029a85f2bcd5d0)#define IMX95\_CLK\_NPU (IMX95\_CCM\_NUM\_CLK\_SRC + 68)

[ 122](imx95__clock_8h.md#a1f8b7c26a7148f30f125c6440984f386)#define IMX95\_CLK\_CCMCKO1 (IMX95\_CCM\_NUM\_CLK\_SRC + 69)

[ 123](imx95__clock_8h.md#a560b27d42f2e2e9f1a911d95b8fbb864)#define IMX95\_CLK\_CCMCKO2 (IMX95\_CCM\_NUM\_CLK\_SRC + 70)

[ 124](imx95__clock_8h.md#aad0b7ac5f78bf79b20d8ec33db9ac287)#define IMX95\_CLK\_CCMCKO3 (IMX95\_CCM\_NUM\_CLK\_SRC + 71)

[ 125](imx95__clock_8h.md#a2ab428cfb446fe4fa4b3be907d00b280)#define IMX95\_CLK\_CCMCKO4 (IMX95\_CCM\_NUM\_CLK\_SRC + 72)

[ 126](imx95__clock_8h.md#ab04e4b927f331996ab7961dbd7a8cf01)#define IMX95\_CLK\_VPUAPB (IMX95\_CCM\_NUM\_CLK\_SRC + 73)

[ 127](imx95__clock_8h.md#a5739f4a0f592e8ca6c633064a81108d9)#define IMX95\_CLK\_VPU (IMX95\_CCM\_NUM\_CLK\_SRC + 74)

[ 128](imx95__clock_8h.md#a2c20fbf047824bc4094d959973786094)#define IMX95\_CLK\_VPUDSP (IMX95\_CCM\_NUM\_CLK\_SRC + 75)

[ 129](imx95__clock_8h.md#a50b2766b744f29c72870d35362f20479)#define IMX95\_CLK\_VPUJPEG (IMX95\_CCM\_NUM\_CLK\_SRC + 76)

[ 130](imx95__clock_8h.md#acc81585761073fe3879893cdda064210)#define IMX95\_CLK\_AUDIOXCVR (IMX95\_CCM\_NUM\_CLK\_SRC + 77)

[ 131](imx95__clock_8h.md#abed81dab2c6d3315efb3d6bf95cc5e21)#define IMX95\_CLK\_BUSWAKEUP (IMX95\_CCM\_NUM\_CLK\_SRC + 78)

[ 132](imx95__clock_8h.md#adad77e80d08aa66faa13fb627c74290c)#define IMX95\_CLK\_CAN2 (IMX95\_CCM\_NUM\_CLK\_SRC + 79)

[ 133](imx95__clock_8h.md#ae2dff47e47984165851a4508077e42aa)#define IMX95\_CLK\_CAN3 (IMX95\_CCM\_NUM\_CLK\_SRC + 80)

[ 134](imx95__clock_8h.md#a8ac89293f6a2596b08ccbd862c87c903)#define IMX95\_CLK\_CAN4 (IMX95\_CCM\_NUM\_CLK\_SRC + 81)

[ 135](imx95__clock_8h.md#a6e2a116260b9b80324c9cfd7785209ed)#define IMX95\_CLK\_CAN5 (IMX95\_CCM\_NUM\_CLK\_SRC + 82)

[ 136](imx95__clock_8h.md#a55e880b0d82413761ba6968868d6be76)#define IMX95\_CLK\_FLEXIO1 (IMX95\_CCM\_NUM\_CLK\_SRC + 83)

[ 137](imx95__clock_8h.md#af62ed9830128e77709fe96088acb52c7)#define IMX95\_CLK\_FLEXIO2 (IMX95\_CCM\_NUM\_CLK\_SRC + 84)

[ 138](imx95__clock_8h.md#ad94aabe5b00f807bb7fd59afd5922add)#define IMX95\_CLK\_FLEXSPI1 (IMX95\_CCM\_NUM\_CLK\_SRC + 85)

[ 139](imx95__clock_8h.md#a43d24cba72b5fe94e0063ff590fdeb9d)#define IMX95\_CLK\_I3C2 (IMX95\_CCM\_NUM\_CLK\_SRC + 86)

[ 140](imx95__clock_8h.md#a59b501711a550287a99667a526ad607d)#define IMX95\_CLK\_I3C2SLOW (IMX95\_CCM\_NUM\_CLK\_SRC + 87)

[ 141](imx95__clock_8h.md#a6da662191259a81b881c91b0e16c7cf2)#define IMX95\_CLK\_LPI2C3 (IMX95\_CCM\_NUM\_CLK\_SRC + 88)

[ 142](imx95__clock_8h.md#a01dee85ab8d5fd1cfe722d92ec9d73d1)#define IMX95\_CLK\_LPI2C4 (IMX95\_CCM\_NUM\_CLK\_SRC + 89)

[ 143](imx95__clock_8h.md#ae24702dc4b730186676fa509227df3a8)#define IMX95\_CLK\_LPI2C5 (IMX95\_CCM\_NUM\_CLK\_SRC + 90)

[ 144](imx95__clock_8h.md#ab3db8caa4c62bd519802a6593b617621)#define IMX95\_CLK\_LPI2C6 (IMX95\_CCM\_NUM\_CLK\_SRC + 91)

[ 145](imx95__clock_8h.md#a3972c80cc32d41746646346aac4a1ef8)#define IMX95\_CLK\_LPI2C7 (IMX95\_CCM\_NUM\_CLK\_SRC + 92)

[ 146](imx95__clock_8h.md#adf0381fbc0f8ad09c25491f6802831ec)#define IMX95\_CLK\_LPI2C8 (IMX95\_CCM\_NUM\_CLK\_SRC + 93)

[ 147](imx95__clock_8h.md#a0c7eaa75cf79285b1c967aa86bbd6741)#define IMX95\_CLK\_LPSPI3 (IMX95\_CCM\_NUM\_CLK\_SRC + 94)

[ 148](imx95__clock_8h.md#a72eadac6ee125e7d30b76c24403688c0)#define IMX95\_CLK\_LPSPI4 (IMX95\_CCM\_NUM\_CLK\_SRC + 95)

[ 149](imx95__clock_8h.md#abb4e9ab3dd0c2869c51262e0e320d74a)#define IMX95\_CLK\_LPSPI5 (IMX95\_CCM\_NUM\_CLK\_SRC + 96)

[ 150](imx95__clock_8h.md#a116ebabcd0b2d393c75978717530cd81)#define IMX95\_CLK\_LPSPI6 (IMX95\_CCM\_NUM\_CLK\_SRC + 97)

[ 151](imx95__clock_8h.md#a2cc9b2f408ad9f818b1bb9eb65b21c82)#define IMX95\_CLK\_LPSPI7 (IMX95\_CCM\_NUM\_CLK\_SRC + 98)

[ 152](imx95__clock_8h.md#ac05c5abf43e260583f8f9f4687efb7b5)#define IMX95\_CLK\_LPSPI8 (IMX95\_CCM\_NUM\_CLK\_SRC + 99)

[ 153](imx95__clock_8h.md#a2eb94707de9472b8166eda5107fb892d)#define IMX95\_CLK\_LPTMR2 (IMX95\_CCM\_NUM\_CLK\_SRC + 100)

[ 154](imx95__clock_8h.md#abf97f301a9366661e4943cee8c8f8d20)#define IMX95\_CLK\_LPUART3 (IMX95\_CCM\_NUM\_CLK\_SRC + 101)

[ 155](imx95__clock_8h.md#aaf917f13283998726b50f5854eff6751)#define IMX95\_CLK\_LPUART4 (IMX95\_CCM\_NUM\_CLK\_SRC + 102)

[ 156](imx95__clock_8h.md#aca2ed853e09b232f9fb8d8a8415c8ac7)#define IMX95\_CLK\_LPUART5 (IMX95\_CCM\_NUM\_CLK\_SRC + 103)

[ 157](imx95__clock_8h.md#a002d22573b1f1f53b5135aea73e90680)#define IMX95\_CLK\_LPUART6 (IMX95\_CCM\_NUM\_CLK\_SRC + 104)

[ 158](imx95__clock_8h.md#a555150002e6ac4296c05bf966f1a5a06)#define IMX95\_CLK\_LPUART7 (IMX95\_CCM\_NUM\_CLK\_SRC + 105)

[ 159](imx95__clock_8h.md#ab96c8a0f9f030fd3b69af009f8149ca9)#define IMX95\_CLK\_LPUART8 (IMX95\_CCM\_NUM\_CLK\_SRC + 106)

[ 160](imx95__clock_8h.md#a59823aaf1d01bbbd5f614953c1016b36)#define IMX95\_CLK\_SAI3 (IMX95\_CCM\_NUM\_CLK\_SRC + 107)

[ 161](imx95__clock_8h.md#ac43962d4dacf3575265dd39b78c6b5f8)#define IMX95\_CLK\_SAI4 (IMX95\_CCM\_NUM\_CLK\_SRC + 108)

[ 162](imx95__clock_8h.md#a25b33aab4a80f05eb693e131e89493ae)#define IMX95\_CLK\_SAI5 (IMX95\_CCM\_NUM\_CLK\_SRC + 109)

[ 163](imx95__clock_8h.md#aeed0022cc9045d09c67c72535ff5aa0c)#define IMX95\_CLK\_SPDIF (IMX95\_CCM\_NUM\_CLK\_SRC + 110)

[ 164](imx95__clock_8h.md#a181cbd339a6ae460b8a63a2e534bb668)#define IMX95\_CLK\_SWOTRACE (IMX95\_CCM\_NUM\_CLK\_SRC + 111)

[ 165](imx95__clock_8h.md#af32af5545dbe718560a9e9986c73bf84)#define IMX95\_CLK\_TPM4 (IMX95\_CCM\_NUM\_CLK\_SRC + 112)

[ 166](imx95__clock_8h.md#a29e1ad802f92043feefec90485edaea3)#define IMX95\_CLK\_TPM5 (IMX95\_CCM\_NUM\_CLK\_SRC + 113)

[ 167](imx95__clock_8h.md#ad9e526e52d258b1a151fcdc9b73cd96e)#define IMX95\_CLK\_TPM6 (IMX95\_CCM\_NUM\_CLK\_SRC + 114)

[ 168](imx95__clock_8h.md#a1d38f97caec2031358407acfc4efe754)#define IMX95\_CLK\_TSTMR2 (IMX95\_CCM\_NUM\_CLK\_SRC + 115)

[ 169](imx95__clock_8h.md#a7ddf6970dfcd8442e840626702c79032)#define IMX95\_CLK\_USBPHYBURUNIN (IMX95\_CCM\_NUM\_CLK\_SRC + 116)

[ 170](imx95__clock_8h.md#af11fdfa2a2602284ca23879bffdde3f2)#define IMX95\_CLK\_USDHC1 (IMX95\_CCM\_NUM\_CLK\_SRC + 117)

[ 171](imx95__clock_8h.md#a8f952271170567680942e072a01547c1)#define IMX95\_CLK\_USDHC2 (IMX95\_CCM\_NUM\_CLK\_SRC + 118)

[ 172](imx95__clock_8h.md#a77536097a0d07bd60084dfc299180c75)#define IMX95\_CLK\_USDHC3 (IMX95\_CCM\_NUM\_CLK\_SRC + 119)

[ 173](imx95__clock_8h.md#aa3408a3c717291a9b825e05ddb23cd71)#define IMX95\_CLK\_V2XPK (IMX95\_CCM\_NUM\_CLK\_SRC + 120)

[ 174](imx95__clock_8h.md#a4a181ed9fc6864c82fb38bf917e92d06)#define IMX95\_CLK\_WAKEUPAXI (IMX95\_CCM\_NUM\_CLK\_SRC + 121)

[ 175](imx95__clock_8h.md#ac8a0b85fd44d1ddd6f056714d5883e18)#define IMX95\_CLK\_XSPISLVROOT (IMX95\_CCM\_NUM\_CLK\_SRC + 122)

176

177#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_IMX95\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [imx95\_clock.h](imx95__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
