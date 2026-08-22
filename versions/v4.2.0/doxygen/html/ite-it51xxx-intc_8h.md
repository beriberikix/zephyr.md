---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ite-it51xxx-intc_8h.html
original_path: doxygen/html/ite-it51xxx-intc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-it51xxx-intc.h File Reference

[Go to the source code of this file.](ite-it51xxx-intc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_TYPE\_NONE](#a9290a5f35a4d3514237ba9fb00936859)   0 |
| #define | [IRQ\_TYPE\_EDGE\_RISING](#ac95cadb7e2fafe537f8be5274baa1e75)   1 |
| #define | [IRQ\_TYPE\_EDGE\_FALLING](#aab03b1a63f7cd7f3a43353048655135a)   2 |
| #define | [IRQ\_TYPE\_EDGE\_BOTH](#a377225dde978048e3d918cedba2c125e)   ([IRQ\_TYPE\_EDGE\_FALLING](#aab03b1a63f7cd7f3a43353048655135a) | [IRQ\_TYPE\_EDGE\_RISING](#ac95cadb7e2fafe537f8be5274baa1e75)) |
| #define | [IRQ\_TYPE\_LEVEL\_HIGH](#a82fc9c68723b62cf4071203f54bd321b)   4 |
| #define | [IRQ\_TYPE\_LEVEL\_LOW](#adfb5a6f2364155f99a90fba88ff9a670)   8 |
| #define | [IT51XXX\_IRQ\_WU20](#a1bd9ea3edc79e9584e9bc260bdedf2ab)   1 |
| #define | [IT51XXX\_IRQ\_KBC\_OBE](#aacb758fc7908b24ef63b2ec198522e34)   2 |
| #define | [IT51XXX\_IRQ\_SMB\_D](#a2e0a412bf3d3ca8b8cfef268630f8e03)   4 |
| #define | [IT51XXX\_IRQ\_WKINTD](#a6f59cc673117062961e9b6d625ac6f5f)   5 |
| #define | [IT51XXX\_IRQ\_WU23](#a2fb3c8770a2af10e03c295117335e6c4)   6 |
| #define | [IT51XXX\_IRQ\_SMB\_A](#a48dc8e3c6bdfe08aeea02d81da7dfa63)   9 |
| #define | [IT51XXX\_IRQ\_SMB\_B](#aab9f42d55277e2f5e6090a89ad339906)   10 |
| #define | [IT51XXX\_IRQ\_WU26](#a9e030083506874c6553b807fd7d72ad9)   12 |
| #define | [IT51XXX\_IRQ\_WKINTC](#a18e8b286b05048957bb47f74fb67a364)   13 |
| #define | [IT51XXX\_IRQ\_WU25](#ada00c64e4d7a21a63c4233caaf982c36)   14 |
| #define | [IT51XXX\_IRQ\_SMB\_C](#ae7070e00ef2980b55e8453057954ca93)   16 |
| #define | [IT51XXX\_IRQ\_WU24](#ac79fe3fa0f5d888e67659b2fac11c824)   17 |
| #define | [IT51XXX\_IRQ\_WU22](#acf15edcfe3b3345a23032fefaed27e69)   21 |
| #define | [IT51XXX\_IRQ\_KBC\_IBF](#ae2accc4b4816ee2580cb2802686dc2f6)   24 |
| #define | [IT51XXX\_IRQ\_PMC1\_IBF](#a198b2275166c27e6781d14841ca3ba97)   25 |
| #define | [IT51XXX\_IRQ\_PMC2\_IBF](#acf65f7e32721d9231a565d8131bad770)   27 |
| #define | [IT51XXX\_IRQ\_TIMER1](#ad56cb3d55328f4aaeb96411a912a3347)   30 |
| #define | [IT51XXX\_IRQ\_WU21](#a1900defd3b4a23c2a19c25c113b2d691)   31 |
| #define | [IT51XXX\_IRQ\_SPI](#a07eeb5cc1ae5b73f91ce828cbd9451a8)   37 |
| #define | [IT51XXX\_IRQ\_WU50](#a8d1ddae9ca1a4b7035f19647d1438589)   40 |
| #define | [IT51XXX\_IRQ\_WU51](#a92d027bb989bda813964f17832902b11)   41 |
| #define | [IT51XXX\_IRQ\_WU52](#a731e3e2cfce359c9a2f0040a4a94cbd3)   42 |
| #define | [IT51XXX\_IRQ\_WU53](#abd748c80cea3b56d183c0a9c4f0c3c9a)   43 |
| #define | [IT51XXX\_IRQ\_WU54](#af48dd974da667ab231cdc18f3feaa251)   44 |
| #define | [IT51XXX\_IRQ\_WU55](#a064ae1cc0c5ec0f249fbd2d6e1e0f70f)   45 |
| #define | [IT51XXX\_IRQ\_WU56](#a36f49197d820a024e3ab3684bedc414d)   46 |
| #define | [IT51XXX\_IRQ\_WU57](#a7245dc3295c00844799011c7b34714fc)   47 |
| #define | [IT51XXX\_IRQ\_WU60](#ae8b3f9cd8fa478093f494b7aa2ff5b91)   48 |
| #define | [IT51XXX\_IRQ\_WU61](#ac391efd2f7283026c3d75b4542c05ef1)   49 |
| #define | [IT51XXX\_IRQ\_WU62](#ab8f17a3cbadce21886c20abe75fffc78)   50 |
| #define | [IT51XXX\_IRQ\_WU63](#a9df1dfa62b7e8250e7e6723b7b6ff337)   51 |
| #define | [IT51XXX\_IRQ\_WU64](#a4c3502581103d480d3f053dff872c8ea)   52 |
| #define | [IT51XXX\_IRQ\_WU65](#ac1f10125b96238e29e03c405e62e20a3)   53 |
| #define | [IT51XXX\_IRQ\_WU66](#ae0f32c3f17f670d6ec70e12e89102bb2)   54 |
| #define | [IT51XXX\_IRQ\_WU67](#a4b414ec5990e57faeb8e3b56cec853bc)   55 |
| #define | [IT51XXX\_IRQ\_TIMER2](#a503ec871ea49a5d2e4b96e5effb41da9)   58 |
| #define | [IT51XXX\_IRQ\_WU70](#af8cf4838b02d059e685530ffedf93bfa)   72 |
| #define | [IT51XXX\_IRQ\_WU71](#a9fd08d907faf689ecd778ab62356ea57)   73 |
| #define | [IT51XXX\_IRQ\_WU72](#a4f2ea344998a12cb1180b31d1566c938)   74 |
| #define | [IT51XXX\_IRQ\_WU73](#a64da2ea6e069ab31f161d54fbb6261c9)   75 |
| #define | [IT51XXX\_IRQ\_WU74](#af5d3ea451601aeb1f68770dda46cca65)   76 |
| #define | [IT51XXX\_IRQ\_WU75](#a73a7bc4fa0e4387bba05c432930a038b)   77 |
| #define | [IT51XXX\_IRQ\_WU76](#a8aadaec67ad35044cd3ab33c780e519f)   78 |
| #define | [IT51XXX\_IRQ\_WU77](#a46928ad8b9c916e25a625ab63bdd347f)   79 |
| #define | [IT51XXX\_IRQ\_WU88](#a0cc237123ca5c9e5ee5d2607a1f65cca)   85 |
| #define | [IT51XXX\_IRQ\_WU89](#a3483a35ba697124f99248296a4fea2b2)   86 |
| #define | [IT51XXX\_IRQ\_WU90](#a8628b39b9d4ed06f5f9340ee986192b2)   87 |
| #define | [IT51XXX\_IRQ\_WU80](#a3899296e615d7ec73d2837c082e35e45)   88 |
| #define | [IT51XXX\_IRQ\_WU81](#a594740dd6c46675dc51da4572de9da5e)   89 |
| #define | [IT51XXX\_IRQ\_WU82](#a1833664c1f0542e1e1558309ef515994)   90 |
| #define | [IT51XXX\_IRQ\_WU83](#a6ebed02426d639b288c7e7c1c8c99996)   91 |
| #define | [IT51XXX\_IRQ\_WU84](#aeddeccc8358a4e1beca4bda4bac04e8e)   92 |
| #define | [IT51XXX\_IRQ\_WU85](#a54675f2dfc773de68a0265ffe5403334)   93 |
| #define | [IT51XXX\_IRQ\_WU86](#a4836dc7572b080050825b634b2739646)   94 |
| #define | [IT51XXX\_IRQ\_WU87](#a0eaf7c4c781e015bbf4d1f53fe37f446)   95 |
| #define | [IT51XXX\_IRQ\_WU91](#a5bb04e38d680139a5ce1041b180d2742)   96 |
| #define | [IT51XXX\_IRQ\_WU92](#a225c69b63c8534ef4aca7f8bf57377fa)   97 |
| #define | [IT51XXX\_IRQ\_WU93](#a340aa216839b6dc185618f6615c3dcc2)   98 |
| #define | [IT51XXX\_IRQ\_WU95](#a6409fd59e97542c5ef8bef2db86208f2)   100 |
| #define | [IT51XXX\_IRQ\_WU96](#a3818c0faa999f1d1b967b1c611139d49)   101 |
| #define | [IT51XXX\_IRQ\_WU97](#a8eb5c55cd65680bc525ec13550935cf8)   102 |
| #define | [IT51XXX\_IRQ\_WU98](#ae79e7df40a0e4979ec62927689ac6cb0)   103 |
| #define | [IT51XXX\_IRQ\_WU99](#a321ce88140a01d74cc92918b139fac86)   104 |
| #define | [IT51XXX\_IRQ\_WU100](#a6e06551e06cf220c07c1dd2a77b71a40)   105 |
| #define | [IT51XXX\_IRQ\_WU101](#aeb8d32ab2288e2d6b8ed9373f1004969)   106 |
| #define | [IT51XXX\_IRQ\_WU102](#a21f0556a14699a72814de76f9aab054b)   107 |
| #define | [IT51XXX\_IRQ\_WU103](#a80d91803a44448f1019cab38e9eeb9d0)   108 |
| #define | [IT51XXX\_IRQ\_WU104](#a70286a54519eac7e069a5cd7149b7605)   109 |
| #define | [IT51XXX\_IRQ\_WU105](#a0edf01dcc171ae82f5000d91cb75a325)   110 |
| #define | [IT51XXX\_IRQ\_WU106](#a1e5344c12c111644ec129649ec1bc590)   111 |
| #define | [IT51XXX\_IRQ\_WU107](#aeb45d2b08b983864373a0f55eb22e43d)   112 |
| #define | [IT51XXX\_IRQ\_WU108](#a5aefba5d16ed726483ea6f5d530abee1)   113 |
| #define | [IT51XXX\_IRQ\_WU109](#a1261ef1bdeb49a8829227db86913bb63)   114 |
| #define | [IT51XXX\_IRQ\_WU110](#afdd1fc1548ff42ed4ee71a4cac096740)   115 |
| #define | [IT51XXX\_IRQ\_WU111](#ab579f5814ff928e42ed3ecfff4479c98)   116 |
| #define | [IT51XXX\_IRQ\_WU112](#a8d1263072ff6e203f483db4f4963affb)   117 |
| #define | [IT51XXX\_IRQ\_WU113](#af5c068d30e13d3beae36e43e60f683a0)   118 |
| #define | [IT51XXX\_IRQ\_WU114](#a9e3ceecd8fc68956a9c86235e1c8d31b)   119 |
| #define | [IT51XXX\_IRQ\_WU115](#a1234e873af21343a697bd2f6d6b975ef)   120 |
| #define | [IT51XXX\_IRQ\_WU116](#ac93e38d1a414b44a5a7ec85ee0827006)   121 |
| #define | [IT51XXX\_IRQ\_WU117](#aef5f1d8e172f0454547f338188161670)   122 |
| #define | [IT51XXX\_IRQ\_WU118](#ac424aeac70e9232ee199832c8b8e35fe)   123 |
| #define | [IT51XXX\_IRQ\_WU119](#a3ccd0d5fed12d435960fc757292a291a)   124 |
| #define | [IT51XXX\_IRQ\_WU120](#a886130b549e4a839b3f0228ecbe24d33)   125 |
| #define | [IT51XXX\_IRQ\_WU121](#ad25d4ec41e22d897907646d14d089ac8)   126 |
| #define | [IT51XXX\_IRQ\_WU122](#ad62f6942c45c6775237a65e3fb63890d)   127 |
| #define | [IT51XXX\_IRQ\_WU128](#a2ed1d21bffa4100b329475da7f0b05f5)   128 |
| #define | [IT51XXX\_IRQ\_WU129](#a7abbba0cf4ff18e831d90f5a755e4bf0)   129 |
| #define | [IT51XXX\_IRQ\_WU131](#aa37e21e814b8f03155f5edf183c2ff68)   131 |
| #define | [IT51XXX\_IRQ\_WU132](#a7f8ee82d1a99380bb0c78868d2c7f9ab)   132 |
| #define | [IT51XXX\_IRQ\_WU133](#abab0fcc184a589ba650baddf2150e94b)   133 |
| #define | [IT51XXX\_IRQ\_WU134](#aa384f21424d9c2f0f5ae385367385c90)   134 |
| #define | [IT51XXX\_IRQ\_WU135](#a90e796c4f1fe0d74d456db79407188ff)   135 |
| #define | [IT51XXX\_IRQ\_WU136](#a949522fcdba6424668f214c4fba2b2ac)   136 |
| #define | [IT51XXX\_IRQ\_WU137](#aeeace56eafbaa49befe615e2a4c873f3)   137 |
| #define | [IT51XXX\_IRQ\_WU138](#a6b2c04bdde25754955c9882b97821176)   138 |
| #define | [IT51XXX\_IRQ\_WU139](#abe9d36fd7c3cba5b613c37d1e212a108)   139 |
| #define | [IT51XXX\_IRQ\_WU140](#a0056b7712922f1c825ee5157819e343e)   140 |
| #define | [IT51XXX\_IRQ\_WU141](#afb41c8d686df27c6248cdf2245bb0cb0)   141 |
| #define | [IT51XXX\_IRQ\_WU142](#a241bae65d751d0840e82ec6c01f58900)   142 |
| #define | [IT51XXX\_IRQ\_WU127](#a98a29286e93b44900f6373deed1c1f6b)   148 |
| #define | [IT51XXX\_IRQ\_V\_CMP](#ada04e9ef33341983fba6faa6fcbe4a96)   151 |
| #define | [IT51XXX\_IRQ\_PECI](#abd85b8ba3de11192be938e35d3508e87)   152 |
| #define | [IT51XXX\_IRQ\_ESPI](#a37dc6051af77a724854c527a45dfac68)   153 |
| #define | [IT51XXX\_IRQ\_ESPI\_VW](#adbddb73244678d5fde56eec7479775f4)   154 |
| #define | [IT51XXX\_IRQ\_PCH\_P80](#a8559f80da2518403b5d9472657f82ea0)   155 |
| #define | [IT51XXX\_IRQ\_TIMER3](#a28bcb6addfada56ac81f15e45c7ee3b4)   157 |
| #define | [IT51XXX\_IRQ\_PLL\_CHANGE](#a519c0e8e3f30a9e1af2b64822b07ee13)   159 |
| #define | [IT51XXX\_IRQ\_SMB\_E](#a47d8b8240562c4a2751a91337c9fa305)   160 |
| #define | [IT51XXX\_IRQ\_SMB\_F](#a11f41892c1092f950a4a1e69e1b78a9c)   161 |
| #define | [IT51XXX\_IRQ\_WU40](#a185ad05ef3459010c11695c539126ed1)   163 |
| #define | [IT51XXX\_IRQ\_WU45](#a32688b80aa7e9f4cdc5c56b8454ce833)   166 |
| #define | [IT51XXX\_IRQ\_WU46](#a0826262e2d144ccb3744aa051a49d3bf)   168 |
| #define | [IT51XXX\_IRQ\_WU144](#abc65b0e84172082f67f7f73f966fe93e)   170 |
| #define | [IT51XXX\_IRQ\_WU145](#a5fa5010931782c35ef10dc8aff598496)   171 |
| #define | [IT51XXX\_IRQ\_WU146](#a950d230c0b4cdca84362c94d923cd292)   172 |
| #define | [IT51XXX\_IRQ\_WU147](#a2092b865939507ed7c9deaedb9ca1d1b)   173 |
| #define | [IT51XXX\_IRQ\_TIMER4](#af46c7e6a1396a5758c0acc9ee0b41fd9)   175 |
| #define | [IT51XXX\_IRQ\_WU148](#ab79775b5e3e970bd94e2e80f3918e6ad)   176 |
| #define | [IT51XXX\_IRQ\_WU149](#a24533eae53c79b5d6e2c4d8b6f648c00)   177 |
| #define | [IT51XXX\_IRQ\_WU150](#afbea534e0246c550492d193e9ca449d8)   178 |
| #define | [IT51XXX\_IRQ\_WU151](#a589f55a54a23a30754557f8abc8d98c8)   179 |
| #define | [IT51XXX\_IRQ\_I3C\_M0](#af0379a8a7ee6c496a839d26ff088f86a)   180 |
| #define | [IT51XXX\_IRQ\_I3C\_M1](#a6a311d1c8ed8c0b6f886a0939d973938)   181 |
| #define | [IT51XXX\_IRQ\_I3C\_S0](#a3e77d71c4a44f2891fe0c9aca8d54a68)   182 |
| #define | [IT51XXX\_IRQ\_I3C\_S1](#a6656394e194fe50f39ef6188f7b0d6f2)   183 |
| #define | [IT51XXX\_IRQ\_SMB\_SC](#ac4d39ade3c95ca510c7abb04398a80a0)   203 |
| #define | [IT51XXX\_IRQ\_SMB\_SB](#a2a3f81d5804f14330681b72b8f8364f4)   204 |
| #define | [IT51XXX\_IRQ\_SMB\_SA](#a9073793dfae7154c3a4b7d4313595c60)   205 |
| #define | [IT51XXX\_IRQ\_TIMER1\_DW](#a31679c43c86bbbe8b87c2e64c649e7c8)   207 |
| #define | [IT51XXX\_IRQ\_TIMER2\_DW](#a7ad66cb768137ce97bc38118f66dfa15)   208 |
| #define | [IT51XXX\_IRQ\_TIMER3\_DW](#a6b7e9fbfa177b548a4b06ad6b858b8a6)   209 |
| #define | [IT51XXX\_IRQ\_TIMER4\_DW](#a3a8b1a21fa8f69b9068608f1a41fada2)   210 |
| #define | [IT51XXX\_IRQ\_TIMER5\_DW](#a68c95d448985caf77c240ad680a03afc)   211 |
| #define | [IT51XXX\_IRQ\_TIMER6\_DW](#abba7af2fd3a2a785cf533d3b92ac9ebd)   212 |
| #define | [IT51XXX\_IRQ\_TIMER7\_DW](#a8320ec332457fb8590ce65fb53ff2769)   213 |
| #define | [IT51XXX\_IRQ\_TIMER8\_DW](#ad156f2f74a3441c1fa99d6f24ca17281)   214 |
| #define | [IT51XXX\_IRQ\_PWM\_TACH0](#ab31a3e61f66db774b1cac063fe1d0285)   219 |
| #define | [IT51XXX\_IRQ\_PWM\_TACH1](#acffdacb27fdfbd21158e17eb8edc29fb)   220 |
| #define | [IT51XXX\_IRQ\_PWM\_TACH2](#ab7915c5e0093e966dbabd34a55c80e19)   221 |
| #define | [IT51XXX\_IRQ\_SMB\_G](#aa71190064a261f80fe101e8800432664)   222 |
| #define | [IT51XXX\_IRQ\_SMB\_H](#a8a5b61f307baac7667d007a56789bc81)   223 |
| #define | [IT51XXX\_IRQ\_SMB\_I](#ab02616140905f0e335523993b894a8ed)   224 |

## Macro Definition Documentation

## [◆ ](#a377225dde978048e3d918cedba2c125e)IRQ\_TYPE\_EDGE\_BOTH

| #define IRQ\_TYPE\_EDGE\_BOTH   ([IRQ\_TYPE\_EDGE\_FALLING](#aab03b1a63f7cd7f3a43353048655135a) | [IRQ\_TYPE\_EDGE\_RISING](#ac95cadb7e2fafe537f8be5274baa1e75)) |
| --- |

## [◆ ](#aab03b1a63f7cd7f3a43353048655135a)IRQ\_TYPE\_EDGE\_FALLING

| #define IRQ\_TYPE\_EDGE\_FALLING   2 |
| --- |

## [◆ ](#ac95cadb7e2fafe537f8be5274baa1e75)IRQ\_TYPE\_EDGE\_RISING

| #define IRQ\_TYPE\_EDGE\_RISING   1 |
| --- |

## [◆ ](#a82fc9c68723b62cf4071203f54bd321b)IRQ\_TYPE\_LEVEL\_HIGH

| #define IRQ\_TYPE\_LEVEL\_HIGH   4 |
| --- |

## [◆ ](#adfb5a6f2364155f99a90fba88ff9a670)IRQ\_TYPE\_LEVEL\_LOW

| #define IRQ\_TYPE\_LEVEL\_LOW   8 |
| --- |

## [◆ ](#a9290a5f35a4d3514237ba9fb00936859)IRQ\_TYPE\_NONE

| #define IRQ\_TYPE\_NONE   0 |
| --- |

## [◆ ](#a37dc6051af77a724854c527a45dfac68)IT51XXX\_IRQ\_ESPI

| #define IT51XXX\_IRQ\_ESPI   153 |
| --- |

## [◆ ](#adbddb73244678d5fde56eec7479775f4)IT51XXX\_IRQ\_ESPI\_VW

| #define IT51XXX\_IRQ\_ESPI\_VW   154 |
| --- |

## [◆ ](#af0379a8a7ee6c496a839d26ff088f86a)IT51XXX\_IRQ\_I3C\_M0

| #define IT51XXX\_IRQ\_I3C\_M0   180 |
| --- |

## [◆ ](#a6a311d1c8ed8c0b6f886a0939d973938)IT51XXX\_IRQ\_I3C\_M1

| #define IT51XXX\_IRQ\_I3C\_M1   181 |
| --- |

## [◆ ](#a3e77d71c4a44f2891fe0c9aca8d54a68)IT51XXX\_IRQ\_I3C\_S0

| #define IT51XXX\_IRQ\_I3C\_S0   182 |
| --- |

## [◆ ](#a6656394e194fe50f39ef6188f7b0d6f2)IT51XXX\_IRQ\_I3C\_S1

| #define IT51XXX\_IRQ\_I3C\_S1   183 |
| --- |

## [◆ ](#ae2accc4b4816ee2580cb2802686dc2f6)IT51XXX\_IRQ\_KBC\_IBF

| #define IT51XXX\_IRQ\_KBC\_IBF   24 |
| --- |

## [◆ ](#aacb758fc7908b24ef63b2ec198522e34)IT51XXX\_IRQ\_KBC\_OBE

| #define IT51XXX\_IRQ\_KBC\_OBE   2 |
| --- |

## [◆ ](#a8559f80da2518403b5d9472657f82ea0)IT51XXX\_IRQ\_PCH\_P80

| #define IT51XXX\_IRQ\_PCH\_P80   155 |
| --- |

## [◆ ](#abd85b8ba3de11192be938e35d3508e87)IT51XXX\_IRQ\_PECI

| #define IT51XXX\_IRQ\_PECI   152 |
| --- |

## [◆ ](#a519c0e8e3f30a9e1af2b64822b07ee13)IT51XXX\_IRQ\_PLL\_CHANGE

| #define IT51XXX\_IRQ\_PLL\_CHANGE   159 |
| --- |

## [◆ ](#a198b2275166c27e6781d14841ca3ba97)IT51XXX\_IRQ\_PMC1\_IBF

| #define IT51XXX\_IRQ\_PMC1\_IBF   25 |
| --- |

## [◆ ](#acf65f7e32721d9231a565d8131bad770)IT51XXX\_IRQ\_PMC2\_IBF

| #define IT51XXX\_IRQ\_PMC2\_IBF   27 |
| --- |

## [◆ ](#ab31a3e61f66db774b1cac063fe1d0285)IT51XXX\_IRQ\_PWM\_TACH0

| #define IT51XXX\_IRQ\_PWM\_TACH0   219 |
| --- |

## [◆ ](#acffdacb27fdfbd21158e17eb8edc29fb)IT51XXX\_IRQ\_PWM\_TACH1

| #define IT51XXX\_IRQ\_PWM\_TACH1   220 |
| --- |

## [◆ ](#ab7915c5e0093e966dbabd34a55c80e19)IT51XXX\_IRQ\_PWM\_TACH2

| #define IT51XXX\_IRQ\_PWM\_TACH2   221 |
| --- |

## [◆ ](#a48dc8e3c6bdfe08aeea02d81da7dfa63)IT51XXX\_IRQ\_SMB\_A

| #define IT51XXX\_IRQ\_SMB\_A   9 |
| --- |

## [◆ ](#aab9f42d55277e2f5e6090a89ad339906)IT51XXX\_IRQ\_SMB\_B

| #define IT51XXX\_IRQ\_SMB\_B   10 |
| --- |

## [◆ ](#ae7070e00ef2980b55e8453057954ca93)IT51XXX\_IRQ\_SMB\_C

| #define IT51XXX\_IRQ\_SMB\_C   16 |
| --- |

## [◆ ](#a2e0a412bf3d3ca8b8cfef268630f8e03)IT51XXX\_IRQ\_SMB\_D

| #define IT51XXX\_IRQ\_SMB\_D   4 |
| --- |

## [◆ ](#a47d8b8240562c4a2751a91337c9fa305)IT51XXX\_IRQ\_SMB\_E

| #define IT51XXX\_IRQ\_SMB\_E   160 |
| --- |

## [◆ ](#a11f41892c1092f950a4a1e69e1b78a9c)IT51XXX\_IRQ\_SMB\_F

| #define IT51XXX\_IRQ\_SMB\_F   161 |
| --- |

## [◆ ](#aa71190064a261f80fe101e8800432664)IT51XXX\_IRQ\_SMB\_G

| #define IT51XXX\_IRQ\_SMB\_G   222 |
| --- |

## [◆ ](#a8a5b61f307baac7667d007a56789bc81)IT51XXX\_IRQ\_SMB\_H

| #define IT51XXX\_IRQ\_SMB\_H   223 |
| --- |

## [◆ ](#ab02616140905f0e335523993b894a8ed)IT51XXX\_IRQ\_SMB\_I

| #define IT51XXX\_IRQ\_SMB\_I   224 |
| --- |

## [◆ ](#a9073793dfae7154c3a4b7d4313595c60)IT51XXX\_IRQ\_SMB\_SA

| #define IT51XXX\_IRQ\_SMB\_SA   205 |
| --- |

## [◆ ](#a2a3f81d5804f14330681b72b8f8364f4)IT51XXX\_IRQ\_SMB\_SB

| #define IT51XXX\_IRQ\_SMB\_SB   204 |
| --- |

## [◆ ](#ac4d39ade3c95ca510c7abb04398a80a0)IT51XXX\_IRQ\_SMB\_SC

| #define IT51XXX\_IRQ\_SMB\_SC   203 |
| --- |

## [◆ ](#a07eeb5cc1ae5b73f91ce828cbd9451a8)IT51XXX\_IRQ\_SPI

| #define IT51XXX\_IRQ\_SPI   37 |
| --- |

## [◆ ](#ad56cb3d55328f4aaeb96411a912a3347)IT51XXX\_IRQ\_TIMER1

| #define IT51XXX\_IRQ\_TIMER1   30 |
| --- |

## [◆ ](#a31679c43c86bbbe8b87c2e64c649e7c8)IT51XXX\_IRQ\_TIMER1\_DW

| #define IT51XXX\_IRQ\_TIMER1\_DW   207 |
| --- |

## [◆ ](#a503ec871ea49a5d2e4b96e5effb41da9)IT51XXX\_IRQ\_TIMER2

| #define IT51XXX\_IRQ\_TIMER2   58 |
| --- |

## [◆ ](#a7ad66cb768137ce97bc38118f66dfa15)IT51XXX\_IRQ\_TIMER2\_DW

| #define IT51XXX\_IRQ\_TIMER2\_DW   208 |
| --- |

## [◆ ](#a28bcb6addfada56ac81f15e45c7ee3b4)IT51XXX\_IRQ\_TIMER3

| #define IT51XXX\_IRQ\_TIMER3   157 |
| --- |

## [◆ ](#a6b7e9fbfa177b548a4b06ad6b858b8a6)IT51XXX\_IRQ\_TIMER3\_DW

| #define IT51XXX\_IRQ\_TIMER3\_DW   209 |
| --- |

## [◆ ](#af46c7e6a1396a5758c0acc9ee0b41fd9)IT51XXX\_IRQ\_TIMER4

| #define IT51XXX\_IRQ\_TIMER4   175 |
| --- |

## [◆ ](#a3a8b1a21fa8f69b9068608f1a41fada2)IT51XXX\_IRQ\_TIMER4\_DW

| #define IT51XXX\_IRQ\_TIMER4\_DW   210 |
| --- |

## [◆ ](#a68c95d448985caf77c240ad680a03afc)IT51XXX\_IRQ\_TIMER5\_DW

| #define IT51XXX\_IRQ\_TIMER5\_DW   211 |
| --- |

## [◆ ](#abba7af2fd3a2a785cf533d3b92ac9ebd)IT51XXX\_IRQ\_TIMER6\_DW

| #define IT51XXX\_IRQ\_TIMER6\_DW   212 |
| --- |

## [◆ ](#a8320ec332457fb8590ce65fb53ff2769)IT51XXX\_IRQ\_TIMER7\_DW

| #define IT51XXX\_IRQ\_TIMER7\_DW   213 |
| --- |

## [◆ ](#ad156f2f74a3441c1fa99d6f24ca17281)IT51XXX\_IRQ\_TIMER8\_DW

| #define IT51XXX\_IRQ\_TIMER8\_DW   214 |
| --- |

## [◆ ](#ada04e9ef33341983fba6faa6fcbe4a96)IT51XXX\_IRQ\_V\_CMP

| #define IT51XXX\_IRQ\_V\_CMP   151 |
| --- |

## [◆ ](#a18e8b286b05048957bb47f74fb67a364)IT51XXX\_IRQ\_WKINTC

| #define IT51XXX\_IRQ\_WKINTC   13 |
| --- |

## [◆ ](#a6f59cc673117062961e9b6d625ac6f5f)IT51XXX\_IRQ\_WKINTD

| #define IT51XXX\_IRQ\_WKINTD   5 |
| --- |

## [◆ ](#a6e06551e06cf220c07c1dd2a77b71a40)IT51XXX\_IRQ\_WU100

| #define IT51XXX\_IRQ\_WU100   105 |
| --- |

## [◆ ](#aeb8d32ab2288e2d6b8ed9373f1004969)IT51XXX\_IRQ\_WU101

| #define IT51XXX\_IRQ\_WU101   106 |
| --- |

## [◆ ](#a21f0556a14699a72814de76f9aab054b)IT51XXX\_IRQ\_WU102

| #define IT51XXX\_IRQ\_WU102   107 |
| --- |

## [◆ ](#a80d91803a44448f1019cab38e9eeb9d0)IT51XXX\_IRQ\_WU103

| #define IT51XXX\_IRQ\_WU103   108 |
| --- |

## [◆ ](#a70286a54519eac7e069a5cd7149b7605)IT51XXX\_IRQ\_WU104

| #define IT51XXX\_IRQ\_WU104   109 |
| --- |

## [◆ ](#a0edf01dcc171ae82f5000d91cb75a325)IT51XXX\_IRQ\_WU105

| #define IT51XXX\_IRQ\_WU105   110 |
| --- |

## [◆ ](#a1e5344c12c111644ec129649ec1bc590)IT51XXX\_IRQ\_WU106

| #define IT51XXX\_IRQ\_WU106   111 |
| --- |

## [◆ ](#aeb45d2b08b983864373a0f55eb22e43d)IT51XXX\_IRQ\_WU107

| #define IT51XXX\_IRQ\_WU107   112 |
| --- |

## [◆ ](#a5aefba5d16ed726483ea6f5d530abee1)IT51XXX\_IRQ\_WU108

| #define IT51XXX\_IRQ\_WU108   113 |
| --- |

## [◆ ](#a1261ef1bdeb49a8829227db86913bb63)IT51XXX\_IRQ\_WU109

| #define IT51XXX\_IRQ\_WU109   114 |
| --- |

## [◆ ](#afdd1fc1548ff42ed4ee71a4cac096740)IT51XXX\_IRQ\_WU110

| #define IT51XXX\_IRQ\_WU110   115 |
| --- |

## [◆ ](#ab579f5814ff928e42ed3ecfff4479c98)IT51XXX\_IRQ\_WU111

| #define IT51XXX\_IRQ\_WU111   116 |
| --- |

## [◆ ](#a8d1263072ff6e203f483db4f4963affb)IT51XXX\_IRQ\_WU112

| #define IT51XXX\_IRQ\_WU112   117 |
| --- |

## [◆ ](#af5c068d30e13d3beae36e43e60f683a0)IT51XXX\_IRQ\_WU113

| #define IT51XXX\_IRQ\_WU113   118 |
| --- |

## [◆ ](#a9e3ceecd8fc68956a9c86235e1c8d31b)IT51XXX\_IRQ\_WU114

| #define IT51XXX\_IRQ\_WU114   119 |
| --- |

## [◆ ](#a1234e873af21343a697bd2f6d6b975ef)IT51XXX\_IRQ\_WU115

| #define IT51XXX\_IRQ\_WU115   120 |
| --- |

## [◆ ](#ac93e38d1a414b44a5a7ec85ee0827006)IT51XXX\_IRQ\_WU116

| #define IT51XXX\_IRQ\_WU116   121 |
| --- |

## [◆ ](#aef5f1d8e172f0454547f338188161670)IT51XXX\_IRQ\_WU117

| #define IT51XXX\_IRQ\_WU117   122 |
| --- |

## [◆ ](#ac424aeac70e9232ee199832c8b8e35fe)IT51XXX\_IRQ\_WU118

| #define IT51XXX\_IRQ\_WU118   123 |
| --- |

## [◆ ](#a3ccd0d5fed12d435960fc757292a291a)IT51XXX\_IRQ\_WU119

| #define IT51XXX\_IRQ\_WU119   124 |
| --- |

## [◆ ](#a886130b549e4a839b3f0228ecbe24d33)IT51XXX\_IRQ\_WU120

| #define IT51XXX\_IRQ\_WU120   125 |
| --- |

## [◆ ](#ad25d4ec41e22d897907646d14d089ac8)IT51XXX\_IRQ\_WU121

| #define IT51XXX\_IRQ\_WU121   126 |
| --- |

## [◆ ](#ad62f6942c45c6775237a65e3fb63890d)IT51XXX\_IRQ\_WU122

| #define IT51XXX\_IRQ\_WU122   127 |
| --- |

## [◆ ](#a98a29286e93b44900f6373deed1c1f6b)IT51XXX\_IRQ\_WU127

| #define IT51XXX\_IRQ\_WU127   148 |
| --- |

## [◆ ](#a2ed1d21bffa4100b329475da7f0b05f5)IT51XXX\_IRQ\_WU128

| #define IT51XXX\_IRQ\_WU128   128 |
| --- |

## [◆ ](#a7abbba0cf4ff18e831d90f5a755e4bf0)IT51XXX\_IRQ\_WU129

| #define IT51XXX\_IRQ\_WU129   129 |
| --- |

## [◆ ](#aa37e21e814b8f03155f5edf183c2ff68)IT51XXX\_IRQ\_WU131

| #define IT51XXX\_IRQ\_WU131   131 |
| --- |

## [◆ ](#a7f8ee82d1a99380bb0c78868d2c7f9ab)IT51XXX\_IRQ\_WU132

| #define IT51XXX\_IRQ\_WU132   132 |
| --- |

## [◆ ](#abab0fcc184a589ba650baddf2150e94b)IT51XXX\_IRQ\_WU133

| #define IT51XXX\_IRQ\_WU133   133 |
| --- |

## [◆ ](#aa384f21424d9c2f0f5ae385367385c90)IT51XXX\_IRQ\_WU134

| #define IT51XXX\_IRQ\_WU134   134 |
| --- |

## [◆ ](#a90e796c4f1fe0d74d456db79407188ff)IT51XXX\_IRQ\_WU135

| #define IT51XXX\_IRQ\_WU135   135 |
| --- |

## [◆ ](#a949522fcdba6424668f214c4fba2b2ac)IT51XXX\_IRQ\_WU136

| #define IT51XXX\_IRQ\_WU136   136 |
| --- |

## [◆ ](#aeeace56eafbaa49befe615e2a4c873f3)IT51XXX\_IRQ\_WU137

| #define IT51XXX\_IRQ\_WU137   137 |
| --- |

## [◆ ](#a6b2c04bdde25754955c9882b97821176)IT51XXX\_IRQ\_WU138

| #define IT51XXX\_IRQ\_WU138   138 |
| --- |

## [◆ ](#abe9d36fd7c3cba5b613c37d1e212a108)IT51XXX\_IRQ\_WU139

| #define IT51XXX\_IRQ\_WU139   139 |
| --- |

## [◆ ](#a0056b7712922f1c825ee5157819e343e)IT51XXX\_IRQ\_WU140

| #define IT51XXX\_IRQ\_WU140   140 |
| --- |

## [◆ ](#afb41c8d686df27c6248cdf2245bb0cb0)IT51XXX\_IRQ\_WU141

| #define IT51XXX\_IRQ\_WU141   141 |
| --- |

## [◆ ](#a241bae65d751d0840e82ec6c01f58900)IT51XXX\_IRQ\_WU142

| #define IT51XXX\_IRQ\_WU142   142 |
| --- |

## [◆ ](#abc65b0e84172082f67f7f73f966fe93e)IT51XXX\_IRQ\_WU144

| #define IT51XXX\_IRQ\_WU144   170 |
| --- |

## [◆ ](#a5fa5010931782c35ef10dc8aff598496)IT51XXX\_IRQ\_WU145

| #define IT51XXX\_IRQ\_WU145   171 |
| --- |

## [◆ ](#a950d230c0b4cdca84362c94d923cd292)IT51XXX\_IRQ\_WU146

| #define IT51XXX\_IRQ\_WU146   172 |
| --- |

## [◆ ](#a2092b865939507ed7c9deaedb9ca1d1b)IT51XXX\_IRQ\_WU147

| #define IT51XXX\_IRQ\_WU147   173 |
| --- |

## [◆ ](#ab79775b5e3e970bd94e2e80f3918e6ad)IT51XXX\_IRQ\_WU148

| #define IT51XXX\_IRQ\_WU148   176 |
| --- |

## [◆ ](#a24533eae53c79b5d6e2c4d8b6f648c00)IT51XXX\_IRQ\_WU149

| #define IT51XXX\_IRQ\_WU149   177 |
| --- |

## [◆ ](#afbea534e0246c550492d193e9ca449d8)IT51XXX\_IRQ\_WU150

| #define IT51XXX\_IRQ\_WU150   178 |
| --- |

## [◆ ](#a589f55a54a23a30754557f8abc8d98c8)IT51XXX\_IRQ\_WU151

| #define IT51XXX\_IRQ\_WU151   179 |
| --- |

## [◆ ](#a1bd9ea3edc79e9584e9bc260bdedf2ab)IT51XXX\_IRQ\_WU20

| #define IT51XXX\_IRQ\_WU20   1 |
| --- |

## [◆ ](#a1900defd3b4a23c2a19c25c113b2d691)IT51XXX\_IRQ\_WU21

| #define IT51XXX\_IRQ\_WU21   31 |
| --- |

## [◆ ](#acf15edcfe3b3345a23032fefaed27e69)IT51XXX\_IRQ\_WU22

| #define IT51XXX\_IRQ\_WU22   21 |
| --- |

## [◆ ](#a2fb3c8770a2af10e03c295117335e6c4)IT51XXX\_IRQ\_WU23

| #define IT51XXX\_IRQ\_WU23   6 |
| --- |

## [◆ ](#ac79fe3fa0f5d888e67659b2fac11c824)IT51XXX\_IRQ\_WU24

| #define IT51XXX\_IRQ\_WU24   17 |
| --- |

## [◆ ](#ada00c64e4d7a21a63c4233caaf982c36)IT51XXX\_IRQ\_WU25

| #define IT51XXX\_IRQ\_WU25   14 |
| --- |

## [◆ ](#a9e030083506874c6553b807fd7d72ad9)IT51XXX\_IRQ\_WU26

| #define IT51XXX\_IRQ\_WU26   12 |
| --- |

## [◆ ](#a185ad05ef3459010c11695c539126ed1)IT51XXX\_IRQ\_WU40

| #define IT51XXX\_IRQ\_WU40   163 |
| --- |

## [◆ ](#a32688b80aa7e9f4cdc5c56b8454ce833)IT51XXX\_IRQ\_WU45

| #define IT51XXX\_IRQ\_WU45   166 |
| --- |

## [◆ ](#a0826262e2d144ccb3744aa051a49d3bf)IT51XXX\_IRQ\_WU46

| #define IT51XXX\_IRQ\_WU46   168 |
| --- |

## [◆ ](#a8d1ddae9ca1a4b7035f19647d1438589)IT51XXX\_IRQ\_WU50

| #define IT51XXX\_IRQ\_WU50   40 |
| --- |

## [◆ ](#a92d027bb989bda813964f17832902b11)IT51XXX\_IRQ\_WU51

| #define IT51XXX\_IRQ\_WU51   41 |
| --- |

## [◆ ](#a731e3e2cfce359c9a2f0040a4a94cbd3)IT51XXX\_IRQ\_WU52

| #define IT51XXX\_IRQ\_WU52   42 |
| --- |

## [◆ ](#abd748c80cea3b56d183c0a9c4f0c3c9a)IT51XXX\_IRQ\_WU53

| #define IT51XXX\_IRQ\_WU53   43 |
| --- |

## [◆ ](#af48dd974da667ab231cdc18f3feaa251)IT51XXX\_IRQ\_WU54

| #define IT51XXX\_IRQ\_WU54   44 |
| --- |

## [◆ ](#a064ae1cc0c5ec0f249fbd2d6e1e0f70f)IT51XXX\_IRQ\_WU55

| #define IT51XXX\_IRQ\_WU55   45 |
| --- |

## [◆ ](#a36f49197d820a024e3ab3684bedc414d)IT51XXX\_IRQ\_WU56

| #define IT51XXX\_IRQ\_WU56   46 |
| --- |

## [◆ ](#a7245dc3295c00844799011c7b34714fc)IT51XXX\_IRQ\_WU57

| #define IT51XXX\_IRQ\_WU57   47 |
| --- |

## [◆ ](#ae8b3f9cd8fa478093f494b7aa2ff5b91)IT51XXX\_IRQ\_WU60

| #define IT51XXX\_IRQ\_WU60   48 |
| --- |

## [◆ ](#ac391efd2f7283026c3d75b4542c05ef1)IT51XXX\_IRQ\_WU61

| #define IT51XXX\_IRQ\_WU61   49 |
| --- |

## [◆ ](#ab8f17a3cbadce21886c20abe75fffc78)IT51XXX\_IRQ\_WU62

| #define IT51XXX\_IRQ\_WU62   50 |
| --- |

## [◆ ](#a9df1dfa62b7e8250e7e6723b7b6ff337)IT51XXX\_IRQ\_WU63

| #define IT51XXX\_IRQ\_WU63   51 |
| --- |

## [◆ ](#a4c3502581103d480d3f053dff872c8ea)IT51XXX\_IRQ\_WU64

| #define IT51XXX\_IRQ\_WU64   52 |
| --- |

## [◆ ](#ac1f10125b96238e29e03c405e62e20a3)IT51XXX\_IRQ\_WU65

| #define IT51XXX\_IRQ\_WU65   53 |
| --- |

## [◆ ](#ae0f32c3f17f670d6ec70e12e89102bb2)IT51XXX\_IRQ\_WU66

| #define IT51XXX\_IRQ\_WU66   54 |
| --- |

## [◆ ](#a4b414ec5990e57faeb8e3b56cec853bc)IT51XXX\_IRQ\_WU67

| #define IT51XXX\_IRQ\_WU67   55 |
| --- |

## [◆ ](#af8cf4838b02d059e685530ffedf93bfa)IT51XXX\_IRQ\_WU70

| #define IT51XXX\_IRQ\_WU70   72 |
| --- |

## [◆ ](#a9fd08d907faf689ecd778ab62356ea57)IT51XXX\_IRQ\_WU71

| #define IT51XXX\_IRQ\_WU71   73 |
| --- |

## [◆ ](#a4f2ea344998a12cb1180b31d1566c938)IT51XXX\_IRQ\_WU72

| #define IT51XXX\_IRQ\_WU72   74 |
| --- |

## [◆ ](#a64da2ea6e069ab31f161d54fbb6261c9)IT51XXX\_IRQ\_WU73

| #define IT51XXX\_IRQ\_WU73   75 |
| --- |

## [◆ ](#af5d3ea451601aeb1f68770dda46cca65)IT51XXX\_IRQ\_WU74

| #define IT51XXX\_IRQ\_WU74   76 |
| --- |

## [◆ ](#a73a7bc4fa0e4387bba05c432930a038b)IT51XXX\_IRQ\_WU75

| #define IT51XXX\_IRQ\_WU75   77 |
| --- |

## [◆ ](#a8aadaec67ad35044cd3ab33c780e519f)IT51XXX\_IRQ\_WU76

| #define IT51XXX\_IRQ\_WU76   78 |
| --- |

## [◆ ](#a46928ad8b9c916e25a625ab63bdd347f)IT51XXX\_IRQ\_WU77

| #define IT51XXX\_IRQ\_WU77   79 |
| --- |

## [◆ ](#a3899296e615d7ec73d2837c082e35e45)IT51XXX\_IRQ\_WU80

| #define IT51XXX\_IRQ\_WU80   88 |
| --- |

## [◆ ](#a594740dd6c46675dc51da4572de9da5e)IT51XXX\_IRQ\_WU81

| #define IT51XXX\_IRQ\_WU81   89 |
| --- |

## [◆ ](#a1833664c1f0542e1e1558309ef515994)IT51XXX\_IRQ\_WU82

| #define IT51XXX\_IRQ\_WU82   90 |
| --- |

## [◆ ](#a6ebed02426d639b288c7e7c1c8c99996)IT51XXX\_IRQ\_WU83

| #define IT51XXX\_IRQ\_WU83   91 |
| --- |

## [◆ ](#aeddeccc8358a4e1beca4bda4bac04e8e)IT51XXX\_IRQ\_WU84

| #define IT51XXX\_IRQ\_WU84   92 |
| --- |

## [◆ ](#a54675f2dfc773de68a0265ffe5403334)IT51XXX\_IRQ\_WU85

| #define IT51XXX\_IRQ\_WU85   93 |
| --- |

## [◆ ](#a4836dc7572b080050825b634b2739646)IT51XXX\_IRQ\_WU86

| #define IT51XXX\_IRQ\_WU86   94 |
| --- |

## [◆ ](#a0eaf7c4c781e015bbf4d1f53fe37f446)IT51XXX\_IRQ\_WU87

| #define IT51XXX\_IRQ\_WU87   95 |
| --- |

## [◆ ](#a0cc237123ca5c9e5ee5d2607a1f65cca)IT51XXX\_IRQ\_WU88

| #define IT51XXX\_IRQ\_WU88   85 |
| --- |

## [◆ ](#a3483a35ba697124f99248296a4fea2b2)IT51XXX\_IRQ\_WU89

| #define IT51XXX\_IRQ\_WU89   86 |
| --- |

## [◆ ](#a8628b39b9d4ed06f5f9340ee986192b2)IT51XXX\_IRQ\_WU90

| #define IT51XXX\_IRQ\_WU90   87 |
| --- |

## [◆ ](#a5bb04e38d680139a5ce1041b180d2742)IT51XXX\_IRQ\_WU91

| #define IT51XXX\_IRQ\_WU91   96 |
| --- |

## [◆ ](#a225c69b63c8534ef4aca7f8bf57377fa)IT51XXX\_IRQ\_WU92

| #define IT51XXX\_IRQ\_WU92   97 |
| --- |

## [◆ ](#a340aa216839b6dc185618f6615c3dcc2)IT51XXX\_IRQ\_WU93

| #define IT51XXX\_IRQ\_WU93   98 |
| --- |

## [◆ ](#a6409fd59e97542c5ef8bef2db86208f2)IT51XXX\_IRQ\_WU95

| #define IT51XXX\_IRQ\_WU95   100 |
| --- |

## [◆ ](#a3818c0faa999f1d1b967b1c611139d49)IT51XXX\_IRQ\_WU96

| #define IT51XXX\_IRQ\_WU96   101 |
| --- |

## [◆ ](#a8eb5c55cd65680bc525ec13550935cf8)IT51XXX\_IRQ\_WU97

| #define IT51XXX\_IRQ\_WU97   102 |
| --- |

## [◆ ](#ae79e7df40a0e4979ec62927689ac6cb0)IT51XXX\_IRQ\_WU98

| #define IT51XXX\_IRQ\_WU98   103 |
| --- |

## [◆ ](#a321ce88140a01d74cc92918b139fac86)IT51XXX\_IRQ\_WU99

| #define IT51XXX\_IRQ\_WU99   104 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [ite-it51xxx-intc.h](ite-it51xxx-intc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
