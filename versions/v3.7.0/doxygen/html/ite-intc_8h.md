---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ite-intc_8h.html
original_path: doxygen/html/ite-intc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ite-intc.h File Reference

[Go to the source code of this file.](ite-intc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IRQ\_TYPE\_NONE](#a9290a5f35a4d3514237ba9fb00936859)   0 |
| #define | [IRQ\_TYPE\_EDGE\_RISING](#ac95cadb7e2fafe537f8be5274baa1e75)   1 |
| #define | [IRQ\_TYPE\_EDGE\_FALLING](#aab03b1a63f7cd7f3a43353048655135a)   2 |
| #define | [IRQ\_TYPE\_EDGE\_BOTH](#a377225dde978048e3d918cedba2c125e)   ([IRQ\_TYPE\_EDGE\_FALLING](#aab03b1a63f7cd7f3a43353048655135a) | [IRQ\_TYPE\_EDGE\_RISING](#ac95cadb7e2fafe537f8be5274baa1e75)) |
| #define | [IRQ\_TYPE\_LEVEL\_HIGH](#a82fc9c68723b62cf4071203f54bd321b)   4 |
| #define | [IRQ\_TYPE\_LEVEL\_LOW](#adfb5a6f2364155f99a90fba88ff9a670)   8 |
| #define | [IT8XXX2\_IRQ\_WU20](#a51865a04eb03d3a3f1239cbbf547fb45)   1 |
| #define | [IT8XXX2\_IRQ\_KBC\_OBE](#a164c6994b9ec0e6caeb2d22f26bb3193)   2 |
| #define | [IT8XXX2\_IRQ\_SMB\_D](#a3ade9064122702f975e5bb8c152af253)   4 |
| #define | [IT8XXX2\_IRQ\_WKINTD](#acdc62901f3913707a381ef90b0c022d3)   5 |
| #define | [IT8XXX2\_IRQ\_WU23](#af40e775e4a526303b9dab46161e0583b)   6 |
| #define | [IT8XXX2\_IRQ\_SMB\_A](#afeffdbf074bfea151dd7e95938303943)   9 |
| #define | [IT8XXX2\_IRQ\_SMB\_B](#ab92e5222303c3b72fe058e4678c3baa0)   10 |
| #define | [IT8XXX2\_IRQ\_WU26](#a08515d08e3080bdc2f2cd42c492dbbc2)   12 |
| #define | [IT8XXX2\_IRQ\_WKINTC](#a4e6257f4cdb53d2603777c6f2bbf1e89)   13 |
| #define | [IT8XXX2\_IRQ\_WU25](#a24a0259fb6961ae91da26b9fcb985db5)   14 |
| #define | [IT8XXX2\_IRQ\_SMB\_C](#a8347f8b954afdde767f221a07a7c6359)   16 |
| #define | [IT8XXX2\_IRQ\_WU24](#a1a5ed099e4ee92fa257a542244d9d410)   17 |
| #define | [IT8XXX2\_IRQ\_WU22](#a7cbf470dc0aef8cce66946b3dfd05117)   21 |
| #define | [IT8XXX2\_IRQ\_USB](#ac585dd5e3a928bf6080d1d5fb879b686)   23 |
| #define | [IT8XXX2\_IRQ\_KBC\_IBF](#ad192bc4d6eb374f6f1b6a3435a0de475)   24 |
| #define | [IT8XXX2\_IRQ\_PMC1\_IBF](#ace6032a2b393b2e9f82e17bc4f682507)   25 |
| #define | [IT8XXX2\_IRQ\_PMC2\_IBF](#af54f7abd8fd110352dbd932665169797)   27 |
| #define | [IT8XXX2\_IRQ\_TIMER1](#a9353a04daccd2da837b226e098045e65)   30 |
| #define | [IT8XXX2\_IRQ\_WU21](#aa8e07837f14e38d727ad423d8fd3be26)   31 |
| #define | [IT8XXX2\_IRQ\_WU50](#afc0033cac685e369c1e643508ac8d3a9)   40 |
| #define | [IT8XXX2\_IRQ\_WU51](#aaafc18df1262db451a0a4d443143d5a5)   41 |
| #define | [IT8XXX2\_IRQ\_WU52](#a9f1574d93a73a24b560e5d8f6ed639d7)   42 |
| #define | [IT8XXX2\_IRQ\_WU53](#ad45cafb41e8199d89fc14bbf1ef1c1fb)   43 |
| #define | [IT8XXX2\_IRQ\_WU54](#ac246e8f65786a75c9aba1ec5a4204fe5)   44 |
| #define | [IT8XXX2\_IRQ\_WU55](#a794890994a7a1df4171874e24f8f7500)   45 |
| #define | [IT8XXX2\_IRQ\_WU56](#aa553be72aa49dc4c669ad4976d934f9f)   46 |
| #define | [IT8XXX2\_IRQ\_WU57](#ab97cc00122c848c10d37a9397e7bea66)   47 |
| #define | [IT8XXX2\_IRQ\_WU60](#ad5aa387daa4a4c9889bce14af424a32f)   48 |
| #define | [IT8XXX2\_IRQ\_WU61](#adbb8b156e28763763936f1744091ef16)   49 |
| #define | [IT8XXX2\_IRQ\_WU62](#a323fbf7a864a4fe8d2dc5ccbeb257294)   50 |
| #define | [IT8XXX2\_IRQ\_WU63](#a43ebabf29257d1e9e34c7ec9940bf886)   51 |
| #define | [IT8XXX2\_IRQ\_WU64](#a7b36f3167661f548b2be26fdb2699a99)   52 |
| #define | [IT8XXX2\_IRQ\_WU65](#a450e550d3c955cb85963c40fe9c3ef79)   53 |
| #define | [IT8XXX2\_IRQ\_WU66](#a63347ec51db69184846a4e14a1368709)   54 |
| #define | [IT8XXX2\_IRQ\_WU67](#ad8cb0227c71b5173566a483f7190b454)   55 |
| #define | [IT8XXX2\_IRQ\_TIMER2](#a44a71af10fc4eebb3a9e6fd14fa03fa4)   58 |
| #define | [IT8XXX2\_IRQ\_WU70](#a8cb33d3f882ed2cd523795a688fa1363)   72 |
| #define | [IT8XXX2\_IRQ\_WU71](#a9303a03c624d9edf842ee268f6d4f4a0)   73 |
| #define | [IT8XXX2\_IRQ\_WU72](#a260e57b5abf3538854ce49a08c8a1d5b)   74 |
| #define | [IT8XXX2\_IRQ\_WU73](#ac6e77697033c09657877ae7646c2dbd5)   75 |
| #define | [IT8XXX2\_IRQ\_WU74](#ad15f96abc4101a0bfed25d348e9bb8dd)   76 |
| #define | [IT8XXX2\_IRQ\_WU75](#a8127b5a3d89eb80919888400b77d6df9)   77 |
| #define | [IT8XXX2\_IRQ\_WU76](#a5431a28b59009ad6cfe89df880f26b74)   78 |
| #define | [IT8XXX2\_IRQ\_WU77](#a85638058bef305cf3c72275a74a8a8f5)   79 |
| #define | [IT8XXX2\_IRQ\_TIMER8](#a62568d6b0f25a658c16cb5c809f92c6f)   80 |
| #define | [IT8XXX2\_IRQ\_WU88](#a9d62ad86c7c15e13b962a5c0f17e0810)   85 |
| #define | [IT8XXX2\_IRQ\_WU89](#a6b34b4de0fad04f9d3c577eff9a74aed)   86 |
| #define | [IT8XXX2\_IRQ\_WU90](#ae29e4e29bdb8920d352a85f1eb97bc09)   87 |
| #define | [IT8XXX2\_IRQ\_WU80](#a12dd29667cd356607e7f31b52ea906ea)   88 |
| #define | [IT8XXX2\_IRQ\_WU81](#ade0f819076b8cc26f63a33772507899a)   89 |
| #define | [IT8XXX2\_IRQ\_WU82](#a232053c3ff1a86e4afbfc332599ed711)   90 |
| #define | [IT8XXX2\_IRQ\_WU83](#ae4a1972e35689df1db714b52d71dc140)   91 |
| #define | [IT8XXX2\_IRQ\_WU84](#a2257ffbbd8f9a0ce446548bffc3d311c)   92 |
| #define | [IT8XXX2\_IRQ\_WU85](#a8268491bc0032a66991d9a8d3a3d285c)   93 |
| #define | [IT8XXX2\_IRQ\_WU86](#ab7ce72297a86bb34bd9025599c81dd49)   94 |
| #define | [IT8XXX2\_IRQ\_WU87](#a7517e75de3795b5cd482d8adb607c991)   95 |
| #define | [IT8XXX2\_IRQ\_WU91](#a5d3cac73994a065201a17ab4725d962a)   96 |
| #define | [IT8XXX2\_IRQ\_WU92](#af5f92032cb97b198ba36c7b428d011ae)   97 |
| #define | [IT8XXX2\_IRQ\_WU93](#afae6ea7e844d0bbd809cc683b354883c)   98 |
| #define | [IT8XXX2\_IRQ\_WU94](#a690f5f5f6f300b24cd907122df15b420)   99 |
| #define | [IT8XXX2\_IRQ\_WU95](#ace32741abf9552cd60a092f747e8b9e6)   100 |
| #define | [IT8XXX2\_IRQ\_WU96](#a21f8e8cd3ef74b5a716344c90e0e39b4)   101 |
| #define | [IT8XXX2\_IRQ\_WU97](#ac4170451fb1cb5d5e7e8d6e075fd8fce)   102 |
| #define | [IT8XXX2\_IRQ\_WU98](#a29555f549f89915491439c9399eed39f)   103 |
| #define | [IT8XXX2\_IRQ\_WU99](#a26aaeadedf73d5c5bd42c9dff56a8059)   104 |
| #define | [IT8XXX2\_IRQ\_WU100](#afed48a97b31e7fae176ddcd0f15b1df8)   105 |
| #define | [IT8XXX2\_IRQ\_WU101](#a4ea9ccbd6fec3c479aeabfe3d95fb9a1)   106 |
| #define | [IT8XXX2\_IRQ\_WU102](#a347772eb009d923d6bf26e7be1130fd1)   107 |
| #define | [IT8XXX2\_IRQ\_WU103](#ae8048263f8ab7a039d9043186dd3b21c)   108 |
| #define | [IT8XXX2\_IRQ\_WU104](#a3b545fc9e5b2725734cc9d8705ab33c6)   109 |
| #define | [IT8XXX2\_IRQ\_WU105](#a8494842c802337e212ac3591cd90318d)   110 |
| #define | [IT8XXX2\_IRQ\_WU106](#aed3fd2392932c82eb7c237540778c1dc)   111 |
| #define | [IT8XXX2\_IRQ\_WU107](#ae905883b0d64273279320febb80474e4)   112 |
| #define | [IT8XXX2\_IRQ\_WU108](#af5890809f076a19af7bdb019761b2fd5)   113 |
| #define | [IT8XXX2\_IRQ\_WU109](#a486bb418458778885e38df9d9f7e3400)   114 |
| #define | [IT8XXX2\_IRQ\_WU110](#af15907cee51085a38d191005d4902294)   115 |
| #define | [IT8XXX2\_IRQ\_WU111](#aefe25a9621334783ec285b065ef60c14)   116 |
| #define | [IT8XXX2\_IRQ\_WU112](#a0500748e035b1be53ac925949239222b)   117 |
| #define | [IT8XXX2\_IRQ\_WU113](#a3cfd6fbf8f81d2f06da7349136150a3f)   118 |
| #define | [IT8XXX2\_IRQ\_WU114](#aa548093ad9515794dd05254ab44c1aa1)   119 |
| #define | [IT8XXX2\_IRQ\_WU115](#aaf4e01822d4db393a3d232903568f732)   120 |
| #define | [IT8XXX2\_IRQ\_WU116](#a8d06b3da3354bf3e0386fddb076eedd6)   121 |
| #define | [IT8XXX2\_IRQ\_WU117](#af8e6a237bb5517104d1cfaea5ea83013)   122 |
| #define | [IT8XXX2\_IRQ\_WU118](#a929368b200b099b7c3559297f7eec93f)   123 |
| #define | [IT8XXX2\_IRQ\_WU119](#aea0d15b7466a70f369e793744d8879ed)   124 |
| #define | [IT8XXX2\_IRQ\_WU120](#aa999701f32ffeb7a896e439d402d7c20)   125 |
| #define | [IT8XXX2\_IRQ\_WU121](#ae6b5cbc9a7be8e266b234e2ae1236c5a)   126 |
| #define | [IT8XXX2\_IRQ\_WU122](#a0cc7e45df4a646a50533f18829fb9823)   127 |
| #define | [IT8XXX2\_IRQ\_WU128](#aae2ba10f26caf6eeb4cfe9c70e7b51d4)   128 |
| #define | [IT8XXX2\_IRQ\_WU129](#aa36107db62047a7ba38a0aa3c091f993)   129 |
| #define | [IT8XXX2\_IRQ\_WU130](#a070e81200de0c2fe7ba6c6a67eb702aa)   130 |
| #define | [IT8XXX2\_IRQ\_WU131](#a2733ffe35eb8a3361ba329417dd8313e)   131 |
| #define | [IT8XXX2\_IRQ\_WU132](#a4898c89604f929459ffe7c599fc8fa7b)   132 |
| #define | [IT8XXX2\_IRQ\_WU133](#a4e85ab9e4d017c90b79139ba61fdd5d1)   133 |
| #define | [IT8XXX2\_IRQ\_WU134](#af396686ee5e9c1f7c54f191b054c108f)   134 |
| #define | [IT8XXX2\_IRQ\_WU135](#a90c3033b6daf309fcfe73bb39b3b252f)   135 |
| #define | [IT8XXX2\_IRQ\_WU136](#aff0e5b1d4946deb68d6ed1d7420e42bb)   136 |
| #define | [IT8XXX2\_IRQ\_WU137](#a3943e3914e2e6c62ab3f5b28c2a1a4e8)   137 |
| #define | [IT8XXX2\_IRQ\_WU138](#a817f4b3d15ff7469f5d347d4cc87c1e4)   138 |
| #define | [IT8XXX2\_IRQ\_WU139](#a7eae741560ddaf972a9ac99826dde9fb)   139 |
| #define | [IT8XXX2\_IRQ\_WU140](#aaed275701462369166e099fa6415a69e)   140 |
| #define | [IT8XXX2\_IRQ\_WU141](#a986e35a0b6cecdbae29e269f40f4d648)   141 |
| #define | [IT8XXX2\_IRQ\_WU142](#a360d9aa8caa04a319d4c4fe92efdc7c9)   142 |
| #define | [IT8XXX2\_IRQ\_WU143](#aeb435671c9894e01c8babae68e6858d2)   143 |
| #define | [IT8XXX2\_IRQ\_WU123](#a988dbab9684233c89ca0d1ff90ff4caa)   144 |
| #define | [IT8XXX2\_IRQ\_WU124](#a0673f35476eb2f3ea3905ffed7055e7f)   145 |
| #define | [IT8XXX2\_IRQ\_WU125](#a6acd52b3400d5e352cae94dba3eeaca0)   146 |
| #define | [IT8XXX2\_IRQ\_WU126](#a0441a32e61afd7254a9fa2edb510d4a1)   147 |
| #define | [IT8XXX2\_IRQ\_V\_CMP](#aed5301127cb8b90f9831b244c8085b79)   151 |
| #define | [IT8XXX2\_IRQ\_SMB\_E](#aea5518cddba14665f9f7a2acf7b704a7)   152 |
| #define | [IT8XXX2\_IRQ\_SMB\_F](#a0b9b660f99ccc836f3cd1c5aaa66476b)   153 |
| #define | [IT8XXX2\_IRQ\_TIMER3](#a90092bccc13f1a9523ade25d2fa49c1f)   155 |
| #define | [IT8XXX2\_IRQ\_TIMER4](#a2e5c4330798c3a376bb7453660f2e01b)   156 |
| #define | [IT8XXX2\_IRQ\_TIMER5](#af61ec5638b3f691d9def15a71d8a82ac)   157 |
| #define | [IT8XXX2\_IRQ\_TIMER6](#a01203154d769bc5bbf1bd7cf5e42ebdf)   158 |
| #define | [IT8XXX2\_IRQ\_TIMER7](#a369c990acee73d8dcbedc3e462070581)   159 |
| #define | [IT8XXX2\_IRQ\_ESPI](#aaf76ad2c103888e4cfa104b463f3ba25)   162 |
| #define | [IT8XXX2\_IRQ\_ESPI\_VW](#a3589b7e407cbe43552ce47552844f09f)   163 |
| #define | [IT8XXX2\_IRQ\_PCH\_P80](#a77a329b843c2709461188b236e7e9f5a)   164 |
| #define | [IT8XXX2\_IRQ\_USBPD0](#a3693e6b88579d604942052a0e588eb85)   165 |
| #define | [IT8XXX2\_IRQ\_USBPD1](#ab17c137bc7f8d5439ac5c2b204cf14e3)   166 |
| #define | [IT8XXX2\_IRQ\_USBPD2](#aae96e204b6c6e6be344ee7f2377006c1)   174 |
| #define | [IT8XXX2\_IRQ\_WU40](#a7aa1ecddba7071219cca6a145cb53969)   176 |
| #define | [IT8XXX2\_IRQ\_WU45](#a95c762f9c661f278894d43420370e948)   177 |
| #define | [IT8XXX2\_IRQ\_WU46](#a041acf5b855e1d3e99e1b7e82c6e57bc)   178 |
| #define | [IT8XXX2\_IRQ\_WU144](#a42eb93ef740173eb2277669957abefaa)   179 |
| #define | [IT8XXX2\_IRQ\_WU145](#a429966f42f4484049a98cdf7e962aa04)   180 |
| #define | [IT8XXX2\_IRQ\_WU146](#a0668648aa708375b7a50fb7ffb2a4e42)   181 |
| #define | [IT8XXX2\_IRQ\_WU147](#a6cc3170056313309ed7b29c088d92737)   182 |
| #define | [IT8XXX2\_IRQ\_WU148](#accbe84f26e4bd5fd48f8a1803ad7c3b6)   183 |
| #define | [IT8XXX2\_IRQ\_WU149](#a46404fb07e0693bcfa6be6dd8375aa6d)   184 |
| #define | [IT8XXX2\_IRQ\_WU150](#a8394d2a1eecd8958ed10b198cb0d33fe)   185 |
| #define | [IT8XXX2\_IRQ\_COUNT](#a39332381696855007ce3af2164bb449d)   ([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) + 1) |

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

## [◆ ](#a39332381696855007ce3af2164bb449d)IT8XXX2\_IRQ\_COUNT

| #define IT8XXX2\_IRQ\_COUNT   ([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) + 1) |
| --- |

## [◆ ](#aaf76ad2c103888e4cfa104b463f3ba25)IT8XXX2\_IRQ\_ESPI

| #define IT8XXX2\_IRQ\_ESPI   162 |
| --- |

## [◆ ](#a3589b7e407cbe43552ce47552844f09f)IT8XXX2\_IRQ\_ESPI\_VW

| #define IT8XXX2\_IRQ\_ESPI\_VW   163 |
| --- |

## [◆ ](#ad192bc4d6eb374f6f1b6a3435a0de475)IT8XXX2\_IRQ\_KBC\_IBF

| #define IT8XXX2\_IRQ\_KBC\_IBF   24 |
| --- |

## [◆ ](#a164c6994b9ec0e6caeb2d22f26bb3193)IT8XXX2\_IRQ\_KBC\_OBE

| #define IT8XXX2\_IRQ\_KBC\_OBE   2 |
| --- |

## [◆ ](#a77a329b843c2709461188b236e7e9f5a)IT8XXX2\_IRQ\_PCH\_P80

| #define IT8XXX2\_IRQ\_PCH\_P80   164 |
| --- |

## [◆ ](#ace6032a2b393b2e9f82e17bc4f682507)IT8XXX2\_IRQ\_PMC1\_IBF

| #define IT8XXX2\_IRQ\_PMC1\_IBF   25 |
| --- |

## [◆ ](#af54f7abd8fd110352dbd932665169797)IT8XXX2\_IRQ\_PMC2\_IBF

| #define IT8XXX2\_IRQ\_PMC2\_IBF   27 |
| --- |

## [◆ ](#afeffdbf074bfea151dd7e95938303943)IT8XXX2\_IRQ\_SMB\_A

| #define IT8XXX2\_IRQ\_SMB\_A   9 |
| --- |

## [◆ ](#ab92e5222303c3b72fe058e4678c3baa0)IT8XXX2\_IRQ\_SMB\_B

| #define IT8XXX2\_IRQ\_SMB\_B   10 |
| --- |

## [◆ ](#a8347f8b954afdde767f221a07a7c6359)IT8XXX2\_IRQ\_SMB\_C

| #define IT8XXX2\_IRQ\_SMB\_C   16 |
| --- |

## [◆ ](#a3ade9064122702f975e5bb8c152af253)IT8XXX2\_IRQ\_SMB\_D

| #define IT8XXX2\_IRQ\_SMB\_D   4 |
| --- |

## [◆ ](#aea5518cddba14665f9f7a2acf7b704a7)IT8XXX2\_IRQ\_SMB\_E

| #define IT8XXX2\_IRQ\_SMB\_E   152 |
| --- |

## [◆ ](#a0b9b660f99ccc836f3cd1c5aaa66476b)IT8XXX2\_IRQ\_SMB\_F

| #define IT8XXX2\_IRQ\_SMB\_F   153 |
| --- |

## [◆ ](#a9353a04daccd2da837b226e098045e65)IT8XXX2\_IRQ\_TIMER1

| #define IT8XXX2\_IRQ\_TIMER1   30 |
| --- |

## [◆ ](#a44a71af10fc4eebb3a9e6fd14fa03fa4)IT8XXX2\_IRQ\_TIMER2

| #define IT8XXX2\_IRQ\_TIMER2   58 |
| --- |

## [◆ ](#a90092bccc13f1a9523ade25d2fa49c1f)IT8XXX2\_IRQ\_TIMER3

| #define IT8XXX2\_IRQ\_TIMER3   155 |
| --- |

## [◆ ](#a2e5c4330798c3a376bb7453660f2e01b)IT8XXX2\_IRQ\_TIMER4

| #define IT8XXX2\_IRQ\_TIMER4   156 |
| --- |

## [◆ ](#af61ec5638b3f691d9def15a71d8a82ac)IT8XXX2\_IRQ\_TIMER5

| #define IT8XXX2\_IRQ\_TIMER5   157 |
| --- |

## [◆ ](#a01203154d769bc5bbf1bd7cf5e42ebdf)IT8XXX2\_IRQ\_TIMER6

| #define IT8XXX2\_IRQ\_TIMER6   158 |
| --- |

## [◆ ](#a369c990acee73d8dcbedc3e462070581)IT8XXX2\_IRQ\_TIMER7

| #define IT8XXX2\_IRQ\_TIMER7   159 |
| --- |

## [◆ ](#a62568d6b0f25a658c16cb5c809f92c6f)IT8XXX2\_IRQ\_TIMER8

| #define IT8XXX2\_IRQ\_TIMER8   80 |
| --- |

## [◆ ](#ac585dd5e3a928bf6080d1d5fb879b686)IT8XXX2\_IRQ\_USB

| #define IT8XXX2\_IRQ\_USB   23 |
| --- |

## [◆ ](#a3693e6b88579d604942052a0e588eb85)IT8XXX2\_IRQ\_USBPD0

| #define IT8XXX2\_IRQ\_USBPD0   165 |
| --- |

## [◆ ](#ab17c137bc7f8d5439ac5c2b204cf14e3)IT8XXX2\_IRQ\_USBPD1

| #define IT8XXX2\_IRQ\_USBPD1   166 |
| --- |

## [◆ ](#aae96e204b6c6e6be344ee7f2377006c1)IT8XXX2\_IRQ\_USBPD2

| #define IT8XXX2\_IRQ\_USBPD2   174 |
| --- |

## [◆ ](#aed5301127cb8b90f9831b244c8085b79)IT8XXX2\_IRQ\_V\_CMP

| #define IT8XXX2\_IRQ\_V\_CMP   151 |
| --- |

## [◆ ](#a4e6257f4cdb53d2603777c6f2bbf1e89)IT8XXX2\_IRQ\_WKINTC

| #define IT8XXX2\_IRQ\_WKINTC   13 |
| --- |

## [◆ ](#acdc62901f3913707a381ef90b0c022d3)IT8XXX2\_IRQ\_WKINTD

| #define IT8XXX2\_IRQ\_WKINTD   5 |
| --- |

## [◆ ](#afed48a97b31e7fae176ddcd0f15b1df8)IT8XXX2\_IRQ\_WU100

| #define IT8XXX2\_IRQ\_WU100   105 |
| --- |

## [◆ ](#a4ea9ccbd6fec3c479aeabfe3d95fb9a1)IT8XXX2\_IRQ\_WU101

| #define IT8XXX2\_IRQ\_WU101   106 |
| --- |

## [◆ ](#a347772eb009d923d6bf26e7be1130fd1)IT8XXX2\_IRQ\_WU102

| #define IT8XXX2\_IRQ\_WU102   107 |
| --- |

## [◆ ](#ae8048263f8ab7a039d9043186dd3b21c)IT8XXX2\_IRQ\_WU103

| #define IT8XXX2\_IRQ\_WU103   108 |
| --- |

## [◆ ](#a3b545fc9e5b2725734cc9d8705ab33c6)IT8XXX2\_IRQ\_WU104

| #define IT8XXX2\_IRQ\_WU104   109 |
| --- |

## [◆ ](#a8494842c802337e212ac3591cd90318d)IT8XXX2\_IRQ\_WU105

| #define IT8XXX2\_IRQ\_WU105   110 |
| --- |

## [◆ ](#aed3fd2392932c82eb7c237540778c1dc)IT8XXX2\_IRQ\_WU106

| #define IT8XXX2\_IRQ\_WU106   111 |
| --- |

## [◆ ](#ae905883b0d64273279320febb80474e4)IT8XXX2\_IRQ\_WU107

| #define IT8XXX2\_IRQ\_WU107   112 |
| --- |

## [◆ ](#af5890809f076a19af7bdb019761b2fd5)IT8XXX2\_IRQ\_WU108

| #define IT8XXX2\_IRQ\_WU108   113 |
| --- |

## [◆ ](#a486bb418458778885e38df9d9f7e3400)IT8XXX2\_IRQ\_WU109

| #define IT8XXX2\_IRQ\_WU109   114 |
| --- |

## [◆ ](#af15907cee51085a38d191005d4902294)IT8XXX2\_IRQ\_WU110

| #define IT8XXX2\_IRQ\_WU110   115 |
| --- |

## [◆ ](#aefe25a9621334783ec285b065ef60c14)IT8XXX2\_IRQ\_WU111

| #define IT8XXX2\_IRQ\_WU111   116 |
| --- |

## [◆ ](#a0500748e035b1be53ac925949239222b)IT8XXX2\_IRQ\_WU112

| #define IT8XXX2\_IRQ\_WU112   117 |
| --- |

## [◆ ](#a3cfd6fbf8f81d2f06da7349136150a3f)IT8XXX2\_IRQ\_WU113

| #define IT8XXX2\_IRQ\_WU113   118 |
| --- |

## [◆ ](#aa548093ad9515794dd05254ab44c1aa1)IT8XXX2\_IRQ\_WU114

| #define IT8XXX2\_IRQ\_WU114   119 |
| --- |

## [◆ ](#aaf4e01822d4db393a3d232903568f732)IT8XXX2\_IRQ\_WU115

| #define IT8XXX2\_IRQ\_WU115   120 |
| --- |

## [◆ ](#a8d06b3da3354bf3e0386fddb076eedd6)IT8XXX2\_IRQ\_WU116

| #define IT8XXX2\_IRQ\_WU116   121 |
| --- |

## [◆ ](#af8e6a237bb5517104d1cfaea5ea83013)IT8XXX2\_IRQ\_WU117

| #define IT8XXX2\_IRQ\_WU117   122 |
| --- |

## [◆ ](#a929368b200b099b7c3559297f7eec93f)IT8XXX2\_IRQ\_WU118

| #define IT8XXX2\_IRQ\_WU118   123 |
| --- |

## [◆ ](#aea0d15b7466a70f369e793744d8879ed)IT8XXX2\_IRQ\_WU119

| #define IT8XXX2\_IRQ\_WU119   124 |
| --- |

## [◆ ](#aa999701f32ffeb7a896e439d402d7c20)IT8XXX2\_IRQ\_WU120

| #define IT8XXX2\_IRQ\_WU120   125 |
| --- |

## [◆ ](#ae6b5cbc9a7be8e266b234e2ae1236c5a)IT8XXX2\_IRQ\_WU121

| #define IT8XXX2\_IRQ\_WU121   126 |
| --- |

## [◆ ](#a0cc7e45df4a646a50533f18829fb9823)IT8XXX2\_IRQ\_WU122

| #define IT8XXX2\_IRQ\_WU122   127 |
| --- |

## [◆ ](#a988dbab9684233c89ca0d1ff90ff4caa)IT8XXX2\_IRQ\_WU123

| #define IT8XXX2\_IRQ\_WU123   144 |
| --- |

## [◆ ](#a0673f35476eb2f3ea3905ffed7055e7f)IT8XXX2\_IRQ\_WU124

| #define IT8XXX2\_IRQ\_WU124   145 |
| --- |

## [◆ ](#a6acd52b3400d5e352cae94dba3eeaca0)IT8XXX2\_IRQ\_WU125

| #define IT8XXX2\_IRQ\_WU125   146 |
| --- |

## [◆ ](#a0441a32e61afd7254a9fa2edb510d4a1)IT8XXX2\_IRQ\_WU126

| #define IT8XXX2\_IRQ\_WU126   147 |
| --- |

## [◆ ](#aae2ba10f26caf6eeb4cfe9c70e7b51d4)IT8XXX2\_IRQ\_WU128

| #define IT8XXX2\_IRQ\_WU128   128 |
| --- |

## [◆ ](#aa36107db62047a7ba38a0aa3c091f993)IT8XXX2\_IRQ\_WU129

| #define IT8XXX2\_IRQ\_WU129   129 |
| --- |

## [◆ ](#a070e81200de0c2fe7ba6c6a67eb702aa)IT8XXX2\_IRQ\_WU130

| #define IT8XXX2\_IRQ\_WU130   130 |
| --- |

## [◆ ](#a2733ffe35eb8a3361ba329417dd8313e)IT8XXX2\_IRQ\_WU131

| #define IT8XXX2\_IRQ\_WU131   131 |
| --- |

## [◆ ](#a4898c89604f929459ffe7c599fc8fa7b)IT8XXX2\_IRQ\_WU132

| #define IT8XXX2\_IRQ\_WU132   132 |
| --- |

## [◆ ](#a4e85ab9e4d017c90b79139ba61fdd5d1)IT8XXX2\_IRQ\_WU133

| #define IT8XXX2\_IRQ\_WU133   133 |
| --- |

## [◆ ](#af396686ee5e9c1f7c54f191b054c108f)IT8XXX2\_IRQ\_WU134

| #define IT8XXX2\_IRQ\_WU134   134 |
| --- |

## [◆ ](#a90c3033b6daf309fcfe73bb39b3b252f)IT8XXX2\_IRQ\_WU135

| #define IT8XXX2\_IRQ\_WU135   135 |
| --- |

## [◆ ](#aff0e5b1d4946deb68d6ed1d7420e42bb)IT8XXX2\_IRQ\_WU136

| #define IT8XXX2\_IRQ\_WU136   136 |
| --- |

## [◆ ](#a3943e3914e2e6c62ab3f5b28c2a1a4e8)IT8XXX2\_IRQ\_WU137

| #define IT8XXX2\_IRQ\_WU137   137 |
| --- |

## [◆ ](#a817f4b3d15ff7469f5d347d4cc87c1e4)IT8XXX2\_IRQ\_WU138

| #define IT8XXX2\_IRQ\_WU138   138 |
| --- |

## [◆ ](#a7eae741560ddaf972a9ac99826dde9fb)IT8XXX2\_IRQ\_WU139

| #define IT8XXX2\_IRQ\_WU139   139 |
| --- |

## [◆ ](#aaed275701462369166e099fa6415a69e)IT8XXX2\_IRQ\_WU140

| #define IT8XXX2\_IRQ\_WU140   140 |
| --- |

## [◆ ](#a986e35a0b6cecdbae29e269f40f4d648)IT8XXX2\_IRQ\_WU141

| #define IT8XXX2\_IRQ\_WU141   141 |
| --- |

## [◆ ](#a360d9aa8caa04a319d4c4fe92efdc7c9)IT8XXX2\_IRQ\_WU142

| #define IT8XXX2\_IRQ\_WU142   142 |
| --- |

## [◆ ](#aeb435671c9894e01c8babae68e6858d2)IT8XXX2\_IRQ\_WU143

| #define IT8XXX2\_IRQ\_WU143   143 |
| --- |

## [◆ ](#a42eb93ef740173eb2277669957abefaa)IT8XXX2\_IRQ\_WU144

| #define IT8XXX2\_IRQ\_WU144   179 |
| --- |

## [◆ ](#a429966f42f4484049a98cdf7e962aa04)IT8XXX2\_IRQ\_WU145

| #define IT8XXX2\_IRQ\_WU145   180 |
| --- |

## [◆ ](#a0668648aa708375b7a50fb7ffb2a4e42)IT8XXX2\_IRQ\_WU146

| #define IT8XXX2\_IRQ\_WU146   181 |
| --- |

## [◆ ](#a6cc3170056313309ed7b29c088d92737)IT8XXX2\_IRQ\_WU147

| #define IT8XXX2\_IRQ\_WU147   182 |
| --- |

## [◆ ](#accbe84f26e4bd5fd48f8a1803ad7c3b6)IT8XXX2\_IRQ\_WU148

| #define IT8XXX2\_IRQ\_WU148   183 |
| --- |

## [◆ ](#a46404fb07e0693bcfa6be6dd8375aa6d)IT8XXX2\_IRQ\_WU149

| #define IT8XXX2\_IRQ\_WU149   184 |
| --- |

## [◆ ](#a8394d2a1eecd8958ed10b198cb0d33fe)IT8XXX2\_IRQ\_WU150

| #define IT8XXX2\_IRQ\_WU150   185 |
| --- |

## [◆ ](#a51865a04eb03d3a3f1239cbbf547fb45)IT8XXX2\_IRQ\_WU20

| #define IT8XXX2\_IRQ\_WU20   1 |
| --- |

## [◆ ](#aa8e07837f14e38d727ad423d8fd3be26)IT8XXX2\_IRQ\_WU21

| #define IT8XXX2\_IRQ\_WU21   31 |
| --- |

## [◆ ](#a7cbf470dc0aef8cce66946b3dfd05117)IT8XXX2\_IRQ\_WU22

| #define IT8XXX2\_IRQ\_WU22   21 |
| --- |

## [◆ ](#af40e775e4a526303b9dab46161e0583b)IT8XXX2\_IRQ\_WU23

| #define IT8XXX2\_IRQ\_WU23   6 |
| --- |

## [◆ ](#a1a5ed099e4ee92fa257a542244d9d410)IT8XXX2\_IRQ\_WU24

| #define IT8XXX2\_IRQ\_WU24   17 |
| --- |

## [◆ ](#a24a0259fb6961ae91da26b9fcb985db5)IT8XXX2\_IRQ\_WU25

| #define IT8XXX2\_IRQ\_WU25   14 |
| --- |

## [◆ ](#a08515d08e3080bdc2f2cd42c492dbbc2)IT8XXX2\_IRQ\_WU26

| #define IT8XXX2\_IRQ\_WU26   12 |
| --- |

## [◆ ](#a7aa1ecddba7071219cca6a145cb53969)IT8XXX2\_IRQ\_WU40

| #define IT8XXX2\_IRQ\_WU40   176 |
| --- |

## [◆ ](#a95c762f9c661f278894d43420370e948)IT8XXX2\_IRQ\_WU45

| #define IT8XXX2\_IRQ\_WU45   177 |
| --- |

## [◆ ](#a041acf5b855e1d3e99e1b7e82c6e57bc)IT8XXX2\_IRQ\_WU46

| #define IT8XXX2\_IRQ\_WU46   178 |
| --- |

## [◆ ](#afc0033cac685e369c1e643508ac8d3a9)IT8XXX2\_IRQ\_WU50

| #define IT8XXX2\_IRQ\_WU50   40 |
| --- |

## [◆ ](#aaafc18df1262db451a0a4d443143d5a5)IT8XXX2\_IRQ\_WU51

| #define IT8XXX2\_IRQ\_WU51   41 |
| --- |

## [◆ ](#a9f1574d93a73a24b560e5d8f6ed639d7)IT8XXX2\_IRQ\_WU52

| #define IT8XXX2\_IRQ\_WU52   42 |
| --- |

## [◆ ](#ad45cafb41e8199d89fc14bbf1ef1c1fb)IT8XXX2\_IRQ\_WU53

| #define IT8XXX2\_IRQ\_WU53   43 |
| --- |

## [◆ ](#ac246e8f65786a75c9aba1ec5a4204fe5)IT8XXX2\_IRQ\_WU54

| #define IT8XXX2\_IRQ\_WU54   44 |
| --- |

## [◆ ](#a794890994a7a1df4171874e24f8f7500)IT8XXX2\_IRQ\_WU55

| #define IT8XXX2\_IRQ\_WU55   45 |
| --- |

## [◆ ](#aa553be72aa49dc4c669ad4976d934f9f)IT8XXX2\_IRQ\_WU56

| #define IT8XXX2\_IRQ\_WU56   46 |
| --- |

## [◆ ](#ab97cc00122c848c10d37a9397e7bea66)IT8XXX2\_IRQ\_WU57

| #define IT8XXX2\_IRQ\_WU57   47 |
| --- |

## [◆ ](#ad5aa387daa4a4c9889bce14af424a32f)IT8XXX2\_IRQ\_WU60

| #define IT8XXX2\_IRQ\_WU60   48 |
| --- |

## [◆ ](#adbb8b156e28763763936f1744091ef16)IT8XXX2\_IRQ\_WU61

| #define IT8XXX2\_IRQ\_WU61   49 |
| --- |

## [◆ ](#a323fbf7a864a4fe8d2dc5ccbeb257294)IT8XXX2\_IRQ\_WU62

| #define IT8XXX2\_IRQ\_WU62   50 |
| --- |

## [◆ ](#a43ebabf29257d1e9e34c7ec9940bf886)IT8XXX2\_IRQ\_WU63

| #define IT8XXX2\_IRQ\_WU63   51 |
| --- |

## [◆ ](#a7b36f3167661f548b2be26fdb2699a99)IT8XXX2\_IRQ\_WU64

| #define IT8XXX2\_IRQ\_WU64   52 |
| --- |

## [◆ ](#a450e550d3c955cb85963c40fe9c3ef79)IT8XXX2\_IRQ\_WU65

| #define IT8XXX2\_IRQ\_WU65   53 |
| --- |

## [◆ ](#a63347ec51db69184846a4e14a1368709)IT8XXX2\_IRQ\_WU66

| #define IT8XXX2\_IRQ\_WU66   54 |
| --- |

## [◆ ](#ad8cb0227c71b5173566a483f7190b454)IT8XXX2\_IRQ\_WU67

| #define IT8XXX2\_IRQ\_WU67   55 |
| --- |

## [◆ ](#a8cb33d3f882ed2cd523795a688fa1363)IT8XXX2\_IRQ\_WU70

| #define IT8XXX2\_IRQ\_WU70   72 |
| --- |

## [◆ ](#a9303a03c624d9edf842ee268f6d4f4a0)IT8XXX2\_IRQ\_WU71

| #define IT8XXX2\_IRQ\_WU71   73 |
| --- |

## [◆ ](#a260e57b5abf3538854ce49a08c8a1d5b)IT8XXX2\_IRQ\_WU72

| #define IT8XXX2\_IRQ\_WU72   74 |
| --- |

## [◆ ](#ac6e77697033c09657877ae7646c2dbd5)IT8XXX2\_IRQ\_WU73

| #define IT8XXX2\_IRQ\_WU73   75 |
| --- |

## [◆ ](#ad15f96abc4101a0bfed25d348e9bb8dd)IT8XXX2\_IRQ\_WU74

| #define IT8XXX2\_IRQ\_WU74   76 |
| --- |

## [◆ ](#a8127b5a3d89eb80919888400b77d6df9)IT8XXX2\_IRQ\_WU75

| #define IT8XXX2\_IRQ\_WU75   77 |
| --- |

## [◆ ](#a5431a28b59009ad6cfe89df880f26b74)IT8XXX2\_IRQ\_WU76

| #define IT8XXX2\_IRQ\_WU76   78 |
| --- |

## [◆ ](#a85638058bef305cf3c72275a74a8a8f5)IT8XXX2\_IRQ\_WU77

| #define IT8XXX2\_IRQ\_WU77   79 |
| --- |

## [◆ ](#a12dd29667cd356607e7f31b52ea906ea)IT8XXX2\_IRQ\_WU80

| #define IT8XXX2\_IRQ\_WU80   88 |
| --- |

## [◆ ](#ade0f819076b8cc26f63a33772507899a)IT8XXX2\_IRQ\_WU81

| #define IT8XXX2\_IRQ\_WU81   89 |
| --- |

## [◆ ](#a232053c3ff1a86e4afbfc332599ed711)IT8XXX2\_IRQ\_WU82

| #define IT8XXX2\_IRQ\_WU82   90 |
| --- |

## [◆ ](#ae4a1972e35689df1db714b52d71dc140)IT8XXX2\_IRQ\_WU83

| #define IT8XXX2\_IRQ\_WU83   91 |
| --- |

## [◆ ](#a2257ffbbd8f9a0ce446548bffc3d311c)IT8XXX2\_IRQ\_WU84

| #define IT8XXX2\_IRQ\_WU84   92 |
| --- |

## [◆ ](#a8268491bc0032a66991d9a8d3a3d285c)IT8XXX2\_IRQ\_WU85

| #define IT8XXX2\_IRQ\_WU85   93 |
| --- |

## [◆ ](#ab7ce72297a86bb34bd9025599c81dd49)IT8XXX2\_IRQ\_WU86

| #define IT8XXX2\_IRQ\_WU86   94 |
| --- |

## [◆ ](#a7517e75de3795b5cd482d8adb607c991)IT8XXX2\_IRQ\_WU87

| #define IT8XXX2\_IRQ\_WU87   95 |
| --- |

## [◆ ](#a9d62ad86c7c15e13b962a5c0f17e0810)IT8XXX2\_IRQ\_WU88

| #define IT8XXX2\_IRQ\_WU88   85 |
| --- |

## [◆ ](#a6b34b4de0fad04f9d3c577eff9a74aed)IT8XXX2\_IRQ\_WU89

| #define IT8XXX2\_IRQ\_WU89   86 |
| --- |

## [◆ ](#ae29e4e29bdb8920d352a85f1eb97bc09)IT8XXX2\_IRQ\_WU90

| #define IT8XXX2\_IRQ\_WU90   87 |
| --- |

## [◆ ](#a5d3cac73994a065201a17ab4725d962a)IT8XXX2\_IRQ\_WU91

| #define IT8XXX2\_IRQ\_WU91   96 |
| --- |

## [◆ ](#af5f92032cb97b198ba36c7b428d011ae)IT8XXX2\_IRQ\_WU92

| #define IT8XXX2\_IRQ\_WU92   97 |
| --- |

## [◆ ](#afae6ea7e844d0bbd809cc683b354883c)IT8XXX2\_IRQ\_WU93

| #define IT8XXX2\_IRQ\_WU93   98 |
| --- |

## [◆ ](#a690f5f5f6f300b24cd907122df15b420)IT8XXX2\_IRQ\_WU94

| #define IT8XXX2\_IRQ\_WU94   99 |
| --- |

## [◆ ](#ace32741abf9552cd60a092f747e8b9e6)IT8XXX2\_IRQ\_WU95

| #define IT8XXX2\_IRQ\_WU95   100 |
| --- |

## [◆ ](#a21f8e8cd3ef74b5a716344c90e0e39b4)IT8XXX2\_IRQ\_WU96

| #define IT8XXX2\_IRQ\_WU96   101 |
| --- |

## [◆ ](#ac4170451fb1cb5d5e7e8d6e075fd8fce)IT8XXX2\_IRQ\_WU97

| #define IT8XXX2\_IRQ\_WU97   102 |
| --- |

## [◆ ](#a29555f549f89915491439c9399eed39f)IT8XXX2\_IRQ\_WU98

| #define IT8XXX2\_IRQ\_WU98   103 |
| --- |

## [◆ ](#a26aaeadedf73d5c5bd42c9dff56a8059)IT8XXX2\_IRQ\_WU99

| #define IT8XXX2\_IRQ\_WU99   104 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [ite-intc.h](ite-intc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
