---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/renesas-ra-icu_8h.html
original_path: doxygen/html/renesas-ra-icu_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-ra-icu.h File Reference

[Go to the source code of this file.](renesas-ra-icu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RA\_ICU\_IRQ\_UNSPECIFIED](#a05110d1b8cd06173ab331cc65dba40ca)   (-1) |
| #define | [RA\_ICU\_PORT\_IRQ0](#abf57ee5d814699230bd42c83a0c9045f)   (1 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ1](#a9634f70b2e7ba85d94f3c89eb508f0a3)   (2 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ2](#a9eec5e02aabf9da25e519b2d049dce29)   (3 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ3](#a5ca72014b0ef6093a8830cd3134fcb96)   (4 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ4](#a511eea99c1c288b58cd90d3992d27821)   (5 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ5](#a212fd596f370048148443973191c85a2)   (6 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ6](#a26aae8a3213343658ca725de656f4c4b)   (7 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ7](#a4dd558196b883fa869bae172b9c462fd)   (8 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ8](#a0df06e9ce6a74ffefc4f16cf7fdab1ed)   (9 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ9](#ac6d5188afe5ce472a4f1c6791383af63)   (10 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ10](#a6960edc44b4e2fa6559b1b082d84cff7)   (11 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ11](#aca393b0ad400cedbaa54587fae03e7ef)   (12 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ12](#a3ed88347b1d60d0821bca20d3ad30ab5)   (13 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ14](#a62d4ea9916be89bc354b25196a352eea)   (15 << 8) |
| #define | [RA\_ICU\_PORT\_IRQ15](#a61305c00d1a5290fa26b8b77139422df)   (16 << 8) |
| #define | [RA\_ICU\_DMAC0\_INT](#a1f5e98c5b3754bc664f726bb3f8eff80)   (17 << 8) |
| #define | [RA\_ICU\_DMAC1\_INT](#a65aaf583aba9ec0d15d4e3a9dc5bf962)   (18 << 8) |
| #define | [RA\_ICU\_DMAC2\_INT](#a9a5349120699c42ef7d23a2e307a5324)   (19 << 8) |
| #define | [RA\_ICU\_DMAC3\_INT](#a36710517138f90ce4e4913f516047d7d)   (20 << 8) |
| #define | [RA\_ICU\_DTC\_COMPLETE](#a8c8fca9a760f02455fe7d90bac6c59c5)   (21 << 8) |
| #define | [RA\_ICU\_ICU\_SNZCANCEL](#a1db1ccfa4a07b33291452bdf0d0e06c3)   (23 << 8) |
| #define | [RA\_ICU\_FCU\_FRDYI](#a845de92915d21ffc33db540565827e49)   (24 << 8) |
| #define | [RA\_ICU\_LVD\_LVD1](#a8f553978cc2639473df512776c5ac917)   (25 << 8) |
| #define | [RA\_ICU\_LVD\_LVD2](#a9021c40306177306d8358c7007b712ea)   (26 << 8) |
| #define | [RA\_ICU\_VBATT\_LVD](#acd4f7fbf1bfe48dd9aabc291c251069c)   (27 << 8) |
| #define | [RA\_ICU\_MOSC\_STOP](#a3a95d0e49b745378a08f5af9d8bd076c)   (28 << 8) |
| #define | [RA\_ICU\_SYSTEM\_SNZREQ](#aa329c9eade412d1d927ddc3cb2bdd308)   (29 << 8) |
| #define | [RA\_ICU\_AGT0\_AGTI](#a8f042698b7657f7bb85b53bba35dd6ff)   (30 << 8) |
| #define | [RA\_ICU\_AGT0\_AGTCMAI](#a49d3eaf32dc91c8c5db05f5adcb87e28)   (31 << 8) |
| #define | [RA\_ICU\_AGT0\_AGTCMBI](#aaeb79083b13936e4aa383a6abcdc00cc)   (32 << 8) |
| #define | [RA\_ICU\_AGT1\_AGTI](#acb788091f2ea8609dbcca283ea171d51)   (33 << 8) |
| #define | [RA\_ICU\_AGT1\_AGTCMAI](#a439cfa6642b3de3cc0904c05296949a0)   (34 << 8) |
| #define | [RA\_ICU\_AGT1\_AGTCMBI](#a9e4326fe84596abb9d413a3e2257de21)   (35 << 8) |
| #define | [RA\_ICU\_IWDT\_NMIUNDF](#adab3ccfa14dc248d70aff5c0f6d8ae96)   (36 << 8) |
| #define | [RA\_ICU\_WDT\_NMIUNDF](#ae862b2d094199f06502027841cfc2d8e)   (37 << 8) |
| #define | [RA\_ICU\_RTC\_ALM](#a122d35809141c4c5e6259f2c28393843)   (38 << 8) |
| #define | [RA\_ICU\_RTC\_PRD](#a7603e4b50fa1de24cf62e56a33174cdb)   (39 << 8) |
| #define | [RA\_ICU\_RTC\_CUP](#ab577778d03f2b84cd0495f475c972a8b)   (40 << 8) |
| #define | [RA\_ICU\_ADC140\_ADI](#af81839a1eccd377d8bec1ba756b7f240)   (41 << 8) |
| #define | [RA\_ICU\_ADC140\_GBADI](#a2c77dc5905fa294db9a873818956bb7e)   (42 << 8) |
| #define | [RA\_ICU\_ADC140\_CMPAI](#ae6ba80b0342805166e3275636f96a975)   (43 << 8) |
| #define | [RA\_ICU\_ADC140\_CMPBI](#ae8e3a49399174a9dcbd5cfa00eaa0397)   (44 << 8) |
| #define | [RA\_ICU\_ADC140\_WCMPM](#a22a1f2bb28aa14c479a32acb5ecc3593)   (45 << 8) |
| #define | [RA\_ICU\_ADC140\_WCMPUM](#a772e4cd1e6e2cc9d8fb2c849920e23de)   (46 << 8) |
| #define | [RA\_ICU\_ACMP\_LP0](#a7fcb585a4700afa50378c7227de7f76a)   (47 << 8) |
| #define | [RA\_ICU\_ACMP\_LP1](#a7c95589a42b3f455782383bf45120492)   (48 << 8) |
| #define | [RA\_ICU\_USBFS\_D0FIFO](#af1d44243752a66eaca69e2da756057c1)   (49 << 8) |
| #define | [RA\_ICU\_USBFS\_D1FIFO](#af91ab097f8dac586dbfbb94608248a55)   (50 << 8) |
| #define | [RA\_ICU\_USBFS\_USBI](#ad29c8fff1390a867d5b8329c8b277ef6)   (51 << 8) |
| #define | [RA\_ICU\_USBFS\_USBR](#aedfde20ed81105ab5ec6fc9f15ec8e05)   (52 << 8) |
| #define | [RA\_ICU\_IIC0\_RXI](#a36fcacb08859f5c03b1c5e57f60002be)   (53 << 8) |
| #define | [RA\_ICU\_IIC0\_TXI](#ad89e311e2b73a95f8538b0d1c58cab93)   (54 << 8) |
| #define | [RA\_ICU\_IIC0\_TEI](#ac112865a71e86e2c205825ca7023e2ef)   (55 << 8) |
| #define | [RA\_ICU\_IIC0\_EEI](#a02980d44ee8e6fb0001e3b96de901524)   (56 << 8) |
| #define | [RA\_ICU\_IIC0\_WUI](#a5b64f6a82170b0fb2eddc4550eaf2d30)   (57 << 8) |
| #define | [RA\_ICU\_IIC1\_RXI](#a0e3646e3fc840a741143396c21247bf1)   (58 << 8) |
| #define | [RA\_ICU\_IIC1\_TXI](#a89ace514ee8a7e2e853d1404693fbbaf)   (59 << 8) |
| #define | [RA\_ICU\_IIC1\_TEI](#a655efa3abcf88cdf9a317e4a08ede63a)   (60 << 8) |
| #define | [RA\_ICU\_IIC1\_EEI](#afeb973bf4a990c5f638633fc065b4ffc)   (61 << 8) |
| #define | [RA\_ICU\_SSIE0\_SSITXI](#a7fdce8fba57936a4b41d8f07e6526ea6)   (62 << 8) |
| #define | [RA\_ICU\_SSIE0\_SSIRXI](#a3c629d8751df452f69a2e1861e8792c9)   (63 << 8) |
| #define | [RA\_ICU\_SSIE0\_SSIF](#ab93ca169682fe4d055e672751b41a8fe)   (65 << 8) |
| #define | [RA\_ICU\_CTSU\_CTSUWR](#a6ea92496fd64a00934aa691f6a8bc22a)   (66 << 8) |
| #define | [RA\_ICU\_CTSU\_CTSURD](#af6898ba11c76bed1c4a0cdad76d20ba3)   (67 << 8) |
| #define | [RA\_ICU\_CTSU\_CTSUFN](#a84a6402b4e036f93bd812bbd56d26e1d)   (68 << 8) |
| #define | [RA\_ICU\_KEY\_INTKR](#a5f1e16c4b2a19230646186990d5ceacd)   (69 << 8) |
| #define | [RA\_ICU\_DOC\_DOPCI](#a683d069333136f5fbb24c17663af7ecd)   (70 << 8) |
| #define | [RA\_ICU\_CAC\_FERRI](#a27b05f6c9ced35cc791814be2274b6e1)   (71 << 8) |
| #define | [RA\_ICU\_CAC\_MENDI](#abe8540dffaa7fde4a769c5dcb6e88909)   (72 << 8) |
| #define | [RA\_ICU\_CAC\_OVFI](#a393048af8bba53b9a30b0709ef176f2a)   (73 << 8) |
| #define | [RA\_ICU\_CAN0\_ERS](#acdbaa104552cbf233bde53efcd1eb005)   (74 << 8) |
| #define | [RA\_ICU\_CAN0\_RXF](#afbf4bb3cd92d0754da30052533109d09)   (75 << 8) |
| #define | [RA\_ICU\_CAN0\_TXF](#a90a9552c83ab601ab085fc4899093627)   (76 << 8) |
| #define | [RA\_ICU\_CAN0\_RXM](#a772e4f5126a0a9d21921d9628cb62f0c)   (77 << 8) |
| #define | [RA\_ICU\_CAN0\_TXM](#a69ed346adc7bf2b5eff1fe0b19c1747b)   (78 << 8) |
| #define | [RA\_ICU\_IOPORT\_GROUP1](#a22f873ffc10db62978e25cf7d91d3871)   (70 << 8) |
| #define | [RA\_ICU\_IOPORT\_GROUP2](#a15906c3be13ddcf6142b9ee5a4eee25c)   (80 << 8) |
| #define | [RA\_ICU\_IOPORT\_GROUP3](#ad4c9cc57137570f05a1d337b2ae2a40b)   (81 << 8) |
| #define | [RA\_ICU\_IOPORT\_GROUP4](#a66b119c3f07b02d5fd7f6c667a2a408c)   (82 << 8) |
| #define | [RA\_ICU\_ELC\_SWEVT0](#a3af6611275a7fcd09cabfd0789ba38ca)   (83 << 8) |
| #define | [RA\_ICU\_ELC\_SWEVT1](#a8bdb43684613ad8c8662a125eca60e88)   (84 << 8) |
| #define | [RA\_ICU\_POEG\_GROUP0](#a6f1dbea7bc004de5b363f718a026251a)   (85 << 8) |
| #define | [RA\_ICU\_POEG\_GROUP1](#a49c84bfba6c3a22c2beb4322f5a43ead)   (86 << 8) |
| #define | [RA\_ICU\_GPT0\_CCMPA](#abc960a973e57c866f160f9ec7b9ba92d)   (87 << 8) |
| #define | [RA\_ICU\_GPT0\_CCMPB](#aa24f48cfaff3ecb195a81dfbbc1a8b78)   (88 << 8) |
| #define | [RA\_ICU\_GPT0\_CMPC](#a92bbd691fb8021f89ff409d8dd2bc653)   (89 << 8) |
| #define | [RA\_ICU\_GPT0\_CMPD](#a6bceb7c84c56badb633723ca8056eb3c)   (90 << 8) |
| #define | [RA\_ICU\_GPT0\_CMPE](#a70c1174ad19f3d3b1208eab7b1d3bf94)   (91 << 8) |
| #define | [RA\_ICU\_GPT0\_CMPF](#aff592612f2ab1ca87cb74814747a457b)   (92 << 8) |
| #define | [RA\_ICU\_GPT0\_OVF](#a724fe9773b21feefc24f15ee8a7e58f9)   (93 << 8) |
| #define | [RA\_ICU\_GPT0\_UDF](#ae84d498abac538c678c3d3583b778ae1)   (94 << 8) |
| #define | [RA\_ICU\_GPT1\_CCMPA](#a4c2b5872a30a00e6e94a6e31058512aa)   (95 << 8) |
| #define | [RA\_ICU\_GPT1\_CCMPB](#ab7ed649d7b620d85f65df75ecd4cf112)   (96 << 8) |
| #define | [RA\_ICU\_GPT1\_CMPC](#adafca2329b13ea0598597d83ede55ba9)   (97 << 8) |
| #define | [RA\_ICU\_GPT1\_CMPD](#a91342b289d3727ef64a1a6f8e098b0fb)   (98 << 8) |
| #define | [RA\_ICU\_GPT1\_CMPE](#a2a51c5ae4b499d23bb87b1a01f0513b2)   (99 << 8) |
| #define | [RA\_ICU\_GPT1\_CMPF](#a3c7c41ee806c4abcff1968c9fc601c73)   (100 << 8) |
| #define | [RA\_ICU\_GPT1\_OVF](#a82d9c4f0ed875b67729a14923208ace6)   (101 << 8) |
| #define | [RA\_ICU\_GPT1\_UDF](#abc03ccf50583476ff2198506c963882c)   (102 << 8) |
| #define | [RA\_ICU\_GPT2\_CCMPA](#a3c1cdae0a2e19b36058958513d0c47b5)   (103 << 8) |
| #define | [RA\_ICU\_GPT2\_CCMPB](#a73efa0bffff7edd948fa160be1740961)   (104 << 8) |
| #define | [RA\_ICU\_GPT2\_CMPC](#af5400a5a3e095ed3aab7a9e9f1c2c4fe)   (105 << 8) |
| #define | [RA\_ICU\_GPT2\_CMPD](#a632b9ddbb69194a961a5fdb30ee30cb0)   (106 << 8) |
| #define | [RA\_ICU\_GPT2\_CMPE](#ab4e9a907952811b6a3d77b135f74f1f2)   (107 << 8) |
| #define | [RA\_ICU\_GPT2\_CMPF](#a19247d60bdb100a170560411d68220c3)   (108 << 8) |
| #define | [RA\_ICU\_GPT2\_OVF](#a1b61ab091de6164e3229a0b2f0784a2c)   (109 << 8) |
| #define | [RA\_ICU\_GPT2\_UDF](#a03da6b6d658b9257c9482a061e0f3e86)   (110 << 8) |
| #define | [RA\_ICU\_GPT3\_CCMPA](#ad2a6b2bedeaa09018440a386ac9e55fe)   (111 << 8) |
| #define | [RA\_ICU\_GPT3\_CCMPB](#aa10c6893d943765961d1563ac7927c67)   (112 << 8) |
| #define | [RA\_ICU\_GPT3\_CMPC](#a29c110a19c26c80cbfc9d7c72dfdc46a)   (113 << 8) |
| #define | [RA\_ICU\_GPT3\_CMPD](#a2edafdee7cc1ae27ac7e89b865268ecc)   (114 << 8) |
| #define | [RA\_ICU\_GPT3\_CMPE](#a737fb57923cf539e0b394a611f2d479d)   (115 << 8) |
| #define | [RA\_ICU\_GPT3\_CMPF](#a0dd13cf66a2ac04dfc5cd04b9458134d)   (116 << 8) |
| #define | [RA\_ICU\_GPT3\_OVF](#a09e1e85f40470f97445d1e3466467e78)   (117 << 8) |
| #define | [RA\_ICU\_GPT3\_UDF](#a6401f68679d59e7d2f823d578aa0d09f)   (118 << 8) |
| #define | [RA\_ICU\_GPT4\_CCMPA](#a5b0f20bffc3b8c81c73f0bff4db482e8)   (119 << 8) |
| #define | [RA\_ICU\_GPT4\_CCMPB](#a3915190ef9d6fee52b5ea974cd108958)   (120 << 8) |
| #define | [RA\_ICU\_GPT4\_CMPC](#a59d23b8099170bf5d39a9e24a6e307cd)   (121 << 8) |
| #define | [RA\_ICU\_GPT4\_CMPD](#a77d2439b91c1531a6b036402c48bdc7d)   (122 << 8) |
| #define | [RA\_ICU\_GPT4\_CMPE](#a65cbe53562c584f9501864ca9f0dd9ee)   (123 << 8) |
| #define | [RA\_ICU\_GPT4\_CMPF](#a42c387bb9ecae74d8309cc27d23cc366)   (124 << 8) |
| #define | [RA\_ICU\_GPT4\_OVF](#a69a5adc8d3fff2a9e3a17ef111373f45)   (125 << 8) |
| #define | [RA\_ICU\_GPT4\_UDF](#a9fbab3d4d84307d4c6fa3e2da498fc97)   (126 << 8) |
| #define | [RA\_ICU\_GPT5\_CCMPA](#a1181773ea55d7e8ca49175eb3cbd1b67)   (127 << 8) |
| #define | [RA\_ICU\_GPT5\_CCMPB](#ab5aaec7beca98b625897c6246fe53a4f)   (128 << 8) |
| #define | [RA\_ICU\_GPT5\_CMPC](#ae5de70de6f59d17e541f3b1a8bca1ad4)   (129 << 8) |
| #define | [RA\_ICU\_GPT5\_CMPD](#aa7e171c4c28d42bb48752969467c9486)   (130 << 8) |
| #define | [RA\_ICU\_GPT5\_CMPE](#aa97f1ade56929682c09cd961911ea35f)   (131 << 8) |
| #define | [RA\_ICU\_GPT5\_CMPF](#a6c4830109db82d102493b0d6f35665e5)   (132 << 8) |
| #define | [RA\_ICU\_GPT5\_OVF](#a3e78e11631c69002b851c8b7f954cdda)   (133 << 8) |
| #define | [RA\_ICU\_GPT5\_UDF](#a0214d5b3f38cb748811ef43ae0b05e2f)   (134 << 8) |
| #define | [RA\_ICU\_GPT6\_CCMPA](#a88d9c955eb32f5d3aebe899e03390937)   (135 << 8) |
| #define | [RA\_ICU\_GPT6\_CCMPB](#a0b3302db1a324dc8e3db15f7a36ba1f7)   (136 << 8) |
| #define | [RA\_ICU\_GPT6\_CMPC](#a77c8895f454cd23bde726778796faeb0)   (137 << 8) |
| #define | [RA\_ICU\_GPT6\_CMPD](#a8937da2cd2623c81d36e37606aa2e8e1)   (138 << 8) |
| #define | [RA\_ICU\_GPT6\_CMPE](#a74b47ae49e1f7cb0e9953c22e4eeebb6)   (139 << 8) |
| #define | [RA\_ICU\_GPT6\_CMPF](#acf2e84915ff1e285370c8c51edef80fa)   (140 << 8) |
| #define | [RA\_ICU\_GPT6\_OVF](#abfa5bc932c09df993e155cbe26a64ab4)   (141 << 8) |
| #define | [RA\_ICU\_GPT6\_UDF](#ac28fa43dc4bafc56337b03cdd7dacbd4)   (142 << 8) |
| #define | [RA\_ICU\_GPT7\_CCMPA](#a62d15d5533793ed893ac6c51c99dc74e)   (143 << 8) |
| #define | [RA\_ICU\_GPT7\_CCMPB](#a05ba7f7c2f0bc8dd79020f09f0775049)   (144 << 8) |
| #define | [RA\_ICU\_GPT7\_CMPC](#a5b7cd277641a1a884c8425dd3d1e220e)   (145 << 8) |
| #define | [RA\_ICU\_GPT7\_CMPD](#ac746f2a933a3d6d8a05c9c6aa91a4bec)   (146 << 8) |
| #define | [RA\_ICU\_GPT7\_CMPE](#ae18586a96dec4ddbb4f01effde6b075b)   (147 << 8) |
| #define | [RA\_ICU\_GPT7\_CMPF](#a2f2fdeabeb0be60b77c8d126b9739466)   (148 << 8) |
| #define | [RA\_ICU\_GPT7\_OVF](#a5c7d09aea9a7a77661ac381e6a9905c5)   (149 << 8) |
| #define | [RA\_ICU\_GPT7\_UDF](#a55b989dad215d7dda3a68625c21e09e3)   (150 << 8) |
| #define | [RA\_ICU\_GPT\_UVWEDGE](#aed9fa36a8d62f5352ba6f15977021fad)   (151 << 8) |
| #define | [RA\_ICU\_SCI0\_RXI](#a40c3c9c05e5ad1bb7e87b0432ebff904)   (152 << 8) |
| #define | [RA\_ICU\_SCI0\_TXI](#a57ba91d0e16e044377c25eb42de3fc49)   (153 << 8) |
| #define | [RA\_ICU\_SCI0\_TEI](#ac653e1d2f57daa4f68d36cc597e9e602)   (154 << 8) |
| #define | [RA\_ICU\_SCI0\_ERI](#a4ffde15659be77a80b168566f3bac05f)   (155 << 8) |
| #define | [RA\_ICU\_SCI0\_AM](#a182ca7456f2165f1eee38fd3098be08d)   (156 << 8) |
| #define | [RA\_ICU\_SCI0\_RXI\_OR\_ERI](#ac7e0ddd146fd63b5201e4ad9954f1c37)   (157 << 8) |
| #define | [RA\_ICU\_SCI1\_RXI](#a2f21bbc5eab47e5f5147433eb7b72933)   (158 << 8) |
| #define | [RA\_ICU\_SCI1\_TXI](#abf7bc3870a83a7a77ae602d564c87ca7)   (159 << 8) |
| #define | [RA\_ICU\_SCI1\_TEI](#aec719867c9e414e0ca1605919724686a)   (160 << 8) |
| #define | [RA\_ICU\_SCI1\_ERI](#abb21ea5f21401509523b588ba8b2ef13)   (161 << 8) |
| #define | [RA\_ICU\_SCI1\_AM](#add15456ded38a18a65695ecbce3b5260)   (162 << 8) |
| #define | [RA\_ICU\_SCI2\_RXI](#af0804956b3eed5d26bbde37e6e357344)   (163 << 8) |
| #define | [RA\_ICU\_SCI2\_TXI](#ac1f3bfddffdebbb101bc0359cd6cab49)   (164 << 8) |
| #define | [RA\_ICU\_SCI2\_TEI](#ab7d61b58fb61724a0233a1b639583e6e)   (165 << 8) |
| #define | [RA\_ICU\_SCI2\_ERI](#a47ee241b2d274073589caa6927560086)   (166 << 8) |
| #define | [RA\_ICU\_SCI2\_AM](#a2e4b682b2dd6b98aab4a2f75efab13fc)   (167 << 8) |
| #define | [RA\_ICU\_SCI9\_RXI](#ab884249dba2c79f8db45c3103d0d226d)   (168 << 8) |
| #define | [RA\_ICU\_SCI9\_TXI](#a4a346c13f597718642232c2a34e72500)   (169 << 8) |
| #define | [RA\_ICU\_SCI9\_TEI](#af5bd5bd5bf54e8419f11991b802971d5)   (170 << 8) |
| #define | [RA\_ICU\_SCI9\_ERI](#a0747a5eef57cfc36ba79eb507600ddcb)   (171 << 8) |
| #define | [RA\_ICU\_SCI9\_AM](#ad6392ad85038f9351ec08a15bb64f48a)   (172 << 8) |
| #define | [RA\_ICU\_SPI0\_SPRI](#a40180b3f1bf6709fa0ee4c0bea7e1aab)   (173 << 8) |
| #define | [RA\_ICU\_SPI0\_SPTI](#a19e62564a5b29f7489e44477d1ff9ceb)   (174 << 8) |
| #define | [RA\_ICU\_SPI0\_SPII](#a8542542186b2ccddd35d3ea42346c2cc)   (175 << 8) |
| #define | [RA\_ICU\_SPI0\_SPEI](#a2157ac9a24687c1908d7cc61d4a01c8c)   (176 << 8) |
| #define | [RA\_ICU\_SPI0\_SPTEND](#a86c91cfc649778ecd66c8b758cb12889)   (177 << 8) |
| #define | [RA\_ICU\_SPI1\_SPRI](#ac6b192a749d09b44078e14e1dd2764a9)   (178 << 8) |
| #define | [RA\_ICU\_SPI1\_SPTI](#ade2108762cd0b9d5f0667feda347e1fa)   (179 << 8) |
| #define | [RA\_ICU\_SPI1\_SPII](#a5cd3019eb2a3ba3628c128ddb913caac)   (180 << 8) |
| #define | [RA\_ICU\_SPI1\_SPEI](#acaafc80142dfa897c6bf279b486790a8)   (181 << 8) |
| #define | [RA\_ICU\_SPI1\_SPTEND](#a3222b0bbdbcc58b5e7ce141a9c4dc3f1)   (182 << 8) |

## Macro Definition Documentation

## [◆ ](#a7fcb585a4700afa50378c7227de7f76a)RA\_ICU\_ACMP\_LP0

| #define RA\_ICU\_ACMP\_LP0   (47 << 8) |
| --- |

## [◆ ](#a7c95589a42b3f455782383bf45120492)RA\_ICU\_ACMP\_LP1

| #define RA\_ICU\_ACMP\_LP1   (48 << 8) |
| --- |

## [◆ ](#af81839a1eccd377d8bec1ba756b7f240)RA\_ICU\_ADC140\_ADI

| #define RA\_ICU\_ADC140\_ADI   (41 << 8) |
| --- |

## [◆ ](#ae6ba80b0342805166e3275636f96a975)RA\_ICU\_ADC140\_CMPAI

| #define RA\_ICU\_ADC140\_CMPAI   (43 << 8) |
| --- |

## [◆ ](#ae8e3a49399174a9dcbd5cfa00eaa0397)RA\_ICU\_ADC140\_CMPBI

| #define RA\_ICU\_ADC140\_CMPBI   (44 << 8) |
| --- |

## [◆ ](#a2c77dc5905fa294db9a873818956bb7e)RA\_ICU\_ADC140\_GBADI

| #define RA\_ICU\_ADC140\_GBADI   (42 << 8) |
| --- |

## [◆ ](#a22a1f2bb28aa14c479a32acb5ecc3593)RA\_ICU\_ADC140\_WCMPM

| #define RA\_ICU\_ADC140\_WCMPM   (45 << 8) |
| --- |

## [◆ ](#a772e4cd1e6e2cc9d8fb2c849920e23de)RA\_ICU\_ADC140\_WCMPUM

| #define RA\_ICU\_ADC140\_WCMPUM   (46 << 8) |
| --- |

## [◆ ](#a49d3eaf32dc91c8c5db05f5adcb87e28)RA\_ICU\_AGT0\_AGTCMAI

| #define RA\_ICU\_AGT0\_AGTCMAI   (31 << 8) |
| --- |

## [◆ ](#aaeb79083b13936e4aa383a6abcdc00cc)RA\_ICU\_AGT0\_AGTCMBI

| #define RA\_ICU\_AGT0\_AGTCMBI   (32 << 8) |
| --- |

## [◆ ](#a8f042698b7657f7bb85b53bba35dd6ff)RA\_ICU\_AGT0\_AGTI

| #define RA\_ICU\_AGT0\_AGTI   (30 << 8) |
| --- |

## [◆ ](#a439cfa6642b3de3cc0904c05296949a0)RA\_ICU\_AGT1\_AGTCMAI

| #define RA\_ICU\_AGT1\_AGTCMAI   (34 << 8) |
| --- |

## [◆ ](#a9e4326fe84596abb9d413a3e2257de21)RA\_ICU\_AGT1\_AGTCMBI

| #define RA\_ICU\_AGT1\_AGTCMBI   (35 << 8) |
| --- |

## [◆ ](#acb788091f2ea8609dbcca283ea171d51)RA\_ICU\_AGT1\_AGTI

| #define RA\_ICU\_AGT1\_AGTI   (33 << 8) |
| --- |

## [◆ ](#a27b05f6c9ced35cc791814be2274b6e1)RA\_ICU\_CAC\_FERRI

| #define RA\_ICU\_CAC\_FERRI   (71 << 8) |
| --- |

## [◆ ](#abe8540dffaa7fde4a769c5dcb6e88909)RA\_ICU\_CAC\_MENDI

| #define RA\_ICU\_CAC\_MENDI   (72 << 8) |
| --- |

## [◆ ](#a393048af8bba53b9a30b0709ef176f2a)RA\_ICU\_CAC\_OVFI

| #define RA\_ICU\_CAC\_OVFI   (73 << 8) |
| --- |

## [◆ ](#acdbaa104552cbf233bde53efcd1eb005)RA\_ICU\_CAN0\_ERS

| #define RA\_ICU\_CAN0\_ERS   (74 << 8) |
| --- |

## [◆ ](#afbf4bb3cd92d0754da30052533109d09)RA\_ICU\_CAN0\_RXF

| #define RA\_ICU\_CAN0\_RXF   (75 << 8) |
| --- |

## [◆ ](#a772e4f5126a0a9d21921d9628cb62f0c)RA\_ICU\_CAN0\_RXM

| #define RA\_ICU\_CAN0\_RXM   (77 << 8) |
| --- |

## [◆ ](#a90a9552c83ab601ab085fc4899093627)RA\_ICU\_CAN0\_TXF

| #define RA\_ICU\_CAN0\_TXF   (76 << 8) |
| --- |

## [◆ ](#a69ed346adc7bf2b5eff1fe0b19c1747b)RA\_ICU\_CAN0\_TXM

| #define RA\_ICU\_CAN0\_TXM   (78 << 8) |
| --- |

## [◆ ](#a84a6402b4e036f93bd812bbd56d26e1d)RA\_ICU\_CTSU\_CTSUFN

| #define RA\_ICU\_CTSU\_CTSUFN   (68 << 8) |
| --- |

## [◆ ](#af6898ba11c76bed1c4a0cdad76d20ba3)RA\_ICU\_CTSU\_CTSURD

| #define RA\_ICU\_CTSU\_CTSURD   (67 << 8) |
| --- |

## [◆ ](#a6ea92496fd64a00934aa691f6a8bc22a)RA\_ICU\_CTSU\_CTSUWR

| #define RA\_ICU\_CTSU\_CTSUWR   (66 << 8) |
| --- |

## [◆ ](#a1f5e98c5b3754bc664f726bb3f8eff80)RA\_ICU\_DMAC0\_INT

| #define RA\_ICU\_DMAC0\_INT   (17 << 8) |
| --- |

## [◆ ](#a65aaf583aba9ec0d15d4e3a9dc5bf962)RA\_ICU\_DMAC1\_INT

| #define RA\_ICU\_DMAC1\_INT   (18 << 8) |
| --- |

## [◆ ](#a9a5349120699c42ef7d23a2e307a5324)RA\_ICU\_DMAC2\_INT

| #define RA\_ICU\_DMAC2\_INT   (19 << 8) |
| --- |

## [◆ ](#a36710517138f90ce4e4913f516047d7d)RA\_ICU\_DMAC3\_INT

| #define RA\_ICU\_DMAC3\_INT   (20 << 8) |
| --- |

## [◆ ](#a683d069333136f5fbb24c17663af7ecd)RA\_ICU\_DOC\_DOPCI

| #define RA\_ICU\_DOC\_DOPCI   (70 << 8) |
| --- |

## [◆ ](#a8c8fca9a760f02455fe7d90bac6c59c5)RA\_ICU\_DTC\_COMPLETE

| #define RA\_ICU\_DTC\_COMPLETE   (21 << 8) |
| --- |

## [◆ ](#a3af6611275a7fcd09cabfd0789ba38ca)RA\_ICU\_ELC\_SWEVT0

| #define RA\_ICU\_ELC\_SWEVT0   (83 << 8) |
| --- |

## [◆ ](#a8bdb43684613ad8c8662a125eca60e88)RA\_ICU\_ELC\_SWEVT1

| #define RA\_ICU\_ELC\_SWEVT1   (84 << 8) |
| --- |

## [◆ ](#a845de92915d21ffc33db540565827e49)RA\_ICU\_FCU\_FRDYI

| #define RA\_ICU\_FCU\_FRDYI   (24 << 8) |
| --- |

## [◆ ](#abc960a973e57c866f160f9ec7b9ba92d)RA\_ICU\_GPT0\_CCMPA

| #define RA\_ICU\_GPT0\_CCMPA   (87 << 8) |
| --- |

## [◆ ](#aa24f48cfaff3ecb195a81dfbbc1a8b78)RA\_ICU\_GPT0\_CCMPB

| #define RA\_ICU\_GPT0\_CCMPB   (88 << 8) |
| --- |

## [◆ ](#a92bbd691fb8021f89ff409d8dd2bc653)RA\_ICU\_GPT0\_CMPC

| #define RA\_ICU\_GPT0\_CMPC   (89 << 8) |
| --- |

## [◆ ](#a6bceb7c84c56badb633723ca8056eb3c)RA\_ICU\_GPT0\_CMPD

| #define RA\_ICU\_GPT0\_CMPD   (90 << 8) |
| --- |

## [◆ ](#a70c1174ad19f3d3b1208eab7b1d3bf94)RA\_ICU\_GPT0\_CMPE

| #define RA\_ICU\_GPT0\_CMPE   (91 << 8) |
| --- |

## [◆ ](#aff592612f2ab1ca87cb74814747a457b)RA\_ICU\_GPT0\_CMPF

| #define RA\_ICU\_GPT0\_CMPF   (92 << 8) |
| --- |

## [◆ ](#a724fe9773b21feefc24f15ee8a7e58f9)RA\_ICU\_GPT0\_OVF

| #define RA\_ICU\_GPT0\_OVF   (93 << 8) |
| --- |

## [◆ ](#ae84d498abac538c678c3d3583b778ae1)RA\_ICU\_GPT0\_UDF

| #define RA\_ICU\_GPT0\_UDF   (94 << 8) |
| --- |

## [◆ ](#a4c2b5872a30a00e6e94a6e31058512aa)RA\_ICU\_GPT1\_CCMPA

| #define RA\_ICU\_GPT1\_CCMPA   (95 << 8) |
| --- |

## [◆ ](#ab7ed649d7b620d85f65df75ecd4cf112)RA\_ICU\_GPT1\_CCMPB

| #define RA\_ICU\_GPT1\_CCMPB   (96 << 8) |
| --- |

## [◆ ](#adafca2329b13ea0598597d83ede55ba9)RA\_ICU\_GPT1\_CMPC

| #define RA\_ICU\_GPT1\_CMPC   (97 << 8) |
| --- |

## [◆ ](#a91342b289d3727ef64a1a6f8e098b0fb)RA\_ICU\_GPT1\_CMPD

| #define RA\_ICU\_GPT1\_CMPD   (98 << 8) |
| --- |

## [◆ ](#a2a51c5ae4b499d23bb87b1a01f0513b2)RA\_ICU\_GPT1\_CMPE

| #define RA\_ICU\_GPT1\_CMPE   (99 << 8) |
| --- |

## [◆ ](#a3c7c41ee806c4abcff1968c9fc601c73)RA\_ICU\_GPT1\_CMPF

| #define RA\_ICU\_GPT1\_CMPF   (100 << 8) |
| --- |

## [◆ ](#a82d9c4f0ed875b67729a14923208ace6)RA\_ICU\_GPT1\_OVF

| #define RA\_ICU\_GPT1\_OVF   (101 << 8) |
| --- |

## [◆ ](#abc03ccf50583476ff2198506c963882c)RA\_ICU\_GPT1\_UDF

| #define RA\_ICU\_GPT1\_UDF   (102 << 8) |
| --- |

## [◆ ](#a3c1cdae0a2e19b36058958513d0c47b5)RA\_ICU\_GPT2\_CCMPA

| #define RA\_ICU\_GPT2\_CCMPA   (103 << 8) |
| --- |

## [◆ ](#a73efa0bffff7edd948fa160be1740961)RA\_ICU\_GPT2\_CCMPB

| #define RA\_ICU\_GPT2\_CCMPB   (104 << 8) |
| --- |

## [◆ ](#af5400a5a3e095ed3aab7a9e9f1c2c4fe)RA\_ICU\_GPT2\_CMPC

| #define RA\_ICU\_GPT2\_CMPC   (105 << 8) |
| --- |

## [◆ ](#a632b9ddbb69194a961a5fdb30ee30cb0)RA\_ICU\_GPT2\_CMPD

| #define RA\_ICU\_GPT2\_CMPD   (106 << 8) |
| --- |

## [◆ ](#ab4e9a907952811b6a3d77b135f74f1f2)RA\_ICU\_GPT2\_CMPE

| #define RA\_ICU\_GPT2\_CMPE   (107 << 8) |
| --- |

## [◆ ](#a19247d60bdb100a170560411d68220c3)RA\_ICU\_GPT2\_CMPF

| #define RA\_ICU\_GPT2\_CMPF   (108 << 8) |
| --- |

## [◆ ](#a1b61ab091de6164e3229a0b2f0784a2c)RA\_ICU\_GPT2\_OVF

| #define RA\_ICU\_GPT2\_OVF   (109 << 8) |
| --- |

## [◆ ](#a03da6b6d658b9257c9482a061e0f3e86)RA\_ICU\_GPT2\_UDF

| #define RA\_ICU\_GPT2\_UDF   (110 << 8) |
| --- |

## [◆ ](#ad2a6b2bedeaa09018440a386ac9e55fe)RA\_ICU\_GPT3\_CCMPA

| #define RA\_ICU\_GPT3\_CCMPA   (111 << 8) |
| --- |

## [◆ ](#aa10c6893d943765961d1563ac7927c67)RA\_ICU\_GPT3\_CCMPB

| #define RA\_ICU\_GPT3\_CCMPB   (112 << 8) |
| --- |

## [◆ ](#a29c110a19c26c80cbfc9d7c72dfdc46a)RA\_ICU\_GPT3\_CMPC

| #define RA\_ICU\_GPT3\_CMPC   (113 << 8) |
| --- |

## [◆ ](#a2edafdee7cc1ae27ac7e89b865268ecc)RA\_ICU\_GPT3\_CMPD

| #define RA\_ICU\_GPT3\_CMPD   (114 << 8) |
| --- |

## [◆ ](#a737fb57923cf539e0b394a611f2d479d)RA\_ICU\_GPT3\_CMPE

| #define RA\_ICU\_GPT3\_CMPE   (115 << 8) |
| --- |

## [◆ ](#a0dd13cf66a2ac04dfc5cd04b9458134d)RA\_ICU\_GPT3\_CMPF

| #define RA\_ICU\_GPT3\_CMPF   (116 << 8) |
| --- |

## [◆ ](#a09e1e85f40470f97445d1e3466467e78)RA\_ICU\_GPT3\_OVF

| #define RA\_ICU\_GPT3\_OVF   (117 << 8) |
| --- |

## [◆ ](#a6401f68679d59e7d2f823d578aa0d09f)RA\_ICU\_GPT3\_UDF

| #define RA\_ICU\_GPT3\_UDF   (118 << 8) |
| --- |

## [◆ ](#a5b0f20bffc3b8c81c73f0bff4db482e8)RA\_ICU\_GPT4\_CCMPA

| #define RA\_ICU\_GPT4\_CCMPA   (119 << 8) |
| --- |

## [◆ ](#a3915190ef9d6fee52b5ea974cd108958)RA\_ICU\_GPT4\_CCMPB

| #define RA\_ICU\_GPT4\_CCMPB   (120 << 8) |
| --- |

## [◆ ](#a59d23b8099170bf5d39a9e24a6e307cd)RA\_ICU\_GPT4\_CMPC

| #define RA\_ICU\_GPT4\_CMPC   (121 << 8) |
| --- |

## [◆ ](#a77d2439b91c1531a6b036402c48bdc7d)RA\_ICU\_GPT4\_CMPD

| #define RA\_ICU\_GPT4\_CMPD   (122 << 8) |
| --- |

## [◆ ](#a65cbe53562c584f9501864ca9f0dd9ee)RA\_ICU\_GPT4\_CMPE

| #define RA\_ICU\_GPT4\_CMPE   (123 << 8) |
| --- |

## [◆ ](#a42c387bb9ecae74d8309cc27d23cc366)RA\_ICU\_GPT4\_CMPF

| #define RA\_ICU\_GPT4\_CMPF   (124 << 8) |
| --- |

## [◆ ](#a69a5adc8d3fff2a9e3a17ef111373f45)RA\_ICU\_GPT4\_OVF

| #define RA\_ICU\_GPT4\_OVF   (125 << 8) |
| --- |

## [◆ ](#a9fbab3d4d84307d4c6fa3e2da498fc97)RA\_ICU\_GPT4\_UDF

| #define RA\_ICU\_GPT4\_UDF   (126 << 8) |
| --- |

## [◆ ](#a1181773ea55d7e8ca49175eb3cbd1b67)RA\_ICU\_GPT5\_CCMPA

| #define RA\_ICU\_GPT5\_CCMPA   (127 << 8) |
| --- |

## [◆ ](#ab5aaec7beca98b625897c6246fe53a4f)RA\_ICU\_GPT5\_CCMPB

| #define RA\_ICU\_GPT5\_CCMPB   (128 << 8) |
| --- |

## [◆ ](#ae5de70de6f59d17e541f3b1a8bca1ad4)RA\_ICU\_GPT5\_CMPC

| #define RA\_ICU\_GPT5\_CMPC   (129 << 8) |
| --- |

## [◆ ](#aa7e171c4c28d42bb48752969467c9486)RA\_ICU\_GPT5\_CMPD

| #define RA\_ICU\_GPT5\_CMPD   (130 << 8) |
| --- |

## [◆ ](#aa97f1ade56929682c09cd961911ea35f)RA\_ICU\_GPT5\_CMPE

| #define RA\_ICU\_GPT5\_CMPE   (131 << 8) |
| --- |

## [◆ ](#a6c4830109db82d102493b0d6f35665e5)RA\_ICU\_GPT5\_CMPF

| #define RA\_ICU\_GPT5\_CMPF   (132 << 8) |
| --- |

## [◆ ](#a3e78e11631c69002b851c8b7f954cdda)RA\_ICU\_GPT5\_OVF

| #define RA\_ICU\_GPT5\_OVF   (133 << 8) |
| --- |

## [◆ ](#a0214d5b3f38cb748811ef43ae0b05e2f)RA\_ICU\_GPT5\_UDF

| #define RA\_ICU\_GPT5\_UDF   (134 << 8) |
| --- |

## [◆ ](#a88d9c955eb32f5d3aebe899e03390937)RA\_ICU\_GPT6\_CCMPA

| #define RA\_ICU\_GPT6\_CCMPA   (135 << 8) |
| --- |

## [◆ ](#a0b3302db1a324dc8e3db15f7a36ba1f7)RA\_ICU\_GPT6\_CCMPB

| #define RA\_ICU\_GPT6\_CCMPB   (136 << 8) |
| --- |

## [◆ ](#a77c8895f454cd23bde726778796faeb0)RA\_ICU\_GPT6\_CMPC

| #define RA\_ICU\_GPT6\_CMPC   (137 << 8) |
| --- |

## [◆ ](#a8937da2cd2623c81d36e37606aa2e8e1)RA\_ICU\_GPT6\_CMPD

| #define RA\_ICU\_GPT6\_CMPD   (138 << 8) |
| --- |

## [◆ ](#a74b47ae49e1f7cb0e9953c22e4eeebb6)RA\_ICU\_GPT6\_CMPE

| #define RA\_ICU\_GPT6\_CMPE   (139 << 8) |
| --- |

## [◆ ](#acf2e84915ff1e285370c8c51edef80fa)RA\_ICU\_GPT6\_CMPF

| #define RA\_ICU\_GPT6\_CMPF   (140 << 8) |
| --- |

## [◆ ](#abfa5bc932c09df993e155cbe26a64ab4)RA\_ICU\_GPT6\_OVF

| #define RA\_ICU\_GPT6\_OVF   (141 << 8) |
| --- |

## [◆ ](#ac28fa43dc4bafc56337b03cdd7dacbd4)RA\_ICU\_GPT6\_UDF

| #define RA\_ICU\_GPT6\_UDF   (142 << 8) |
| --- |

## [◆ ](#a62d15d5533793ed893ac6c51c99dc74e)RA\_ICU\_GPT7\_CCMPA

| #define RA\_ICU\_GPT7\_CCMPA   (143 << 8) |
| --- |

## [◆ ](#a05ba7f7c2f0bc8dd79020f09f0775049)RA\_ICU\_GPT7\_CCMPB

| #define RA\_ICU\_GPT7\_CCMPB   (144 << 8) |
| --- |

## [◆ ](#a5b7cd277641a1a884c8425dd3d1e220e)RA\_ICU\_GPT7\_CMPC

| #define RA\_ICU\_GPT7\_CMPC   (145 << 8) |
| --- |

## [◆ ](#ac746f2a933a3d6d8a05c9c6aa91a4bec)RA\_ICU\_GPT7\_CMPD

| #define RA\_ICU\_GPT7\_CMPD   (146 << 8) |
| --- |

## [◆ ](#ae18586a96dec4ddbb4f01effde6b075b)RA\_ICU\_GPT7\_CMPE

| #define RA\_ICU\_GPT7\_CMPE   (147 << 8) |
| --- |

## [◆ ](#a2f2fdeabeb0be60b77c8d126b9739466)RA\_ICU\_GPT7\_CMPF

| #define RA\_ICU\_GPT7\_CMPF   (148 << 8) |
| --- |

## [◆ ](#a5c7d09aea9a7a77661ac381e6a9905c5)RA\_ICU\_GPT7\_OVF

| #define RA\_ICU\_GPT7\_OVF   (149 << 8) |
| --- |

## [◆ ](#a55b989dad215d7dda3a68625c21e09e3)RA\_ICU\_GPT7\_UDF

| #define RA\_ICU\_GPT7\_UDF   (150 << 8) |
| --- |

## [◆ ](#aed9fa36a8d62f5352ba6f15977021fad)RA\_ICU\_GPT\_UVWEDGE

| #define RA\_ICU\_GPT\_UVWEDGE   (151 << 8) |
| --- |

## [◆ ](#a1db1ccfa4a07b33291452bdf0d0e06c3)RA\_ICU\_ICU\_SNZCANCEL

| #define RA\_ICU\_ICU\_SNZCANCEL   (23 << 8) |
| --- |

## [◆ ](#a02980d44ee8e6fb0001e3b96de901524)RA\_ICU\_IIC0\_EEI

| #define RA\_ICU\_IIC0\_EEI   (56 << 8) |
| --- |

## [◆ ](#a36fcacb08859f5c03b1c5e57f60002be)RA\_ICU\_IIC0\_RXI

| #define RA\_ICU\_IIC0\_RXI   (53 << 8) |
| --- |

## [◆ ](#ac112865a71e86e2c205825ca7023e2ef)RA\_ICU\_IIC0\_TEI

| #define RA\_ICU\_IIC0\_TEI   (55 << 8) |
| --- |

## [◆ ](#ad89e311e2b73a95f8538b0d1c58cab93)RA\_ICU\_IIC0\_TXI

| #define RA\_ICU\_IIC0\_TXI   (54 << 8) |
| --- |

## [◆ ](#a5b64f6a82170b0fb2eddc4550eaf2d30)RA\_ICU\_IIC0\_WUI

| #define RA\_ICU\_IIC0\_WUI   (57 << 8) |
| --- |

## [◆ ](#afeb973bf4a990c5f638633fc065b4ffc)RA\_ICU\_IIC1\_EEI

| #define RA\_ICU\_IIC1\_EEI   (61 << 8) |
| --- |

## [◆ ](#a0e3646e3fc840a741143396c21247bf1)RA\_ICU\_IIC1\_RXI

| #define RA\_ICU\_IIC1\_RXI   (58 << 8) |
| --- |

## [◆ ](#a655efa3abcf88cdf9a317e4a08ede63a)RA\_ICU\_IIC1\_TEI

| #define RA\_ICU\_IIC1\_TEI   (60 << 8) |
| --- |

## [◆ ](#a89ace514ee8a7e2e853d1404693fbbaf)RA\_ICU\_IIC1\_TXI

| #define RA\_ICU\_IIC1\_TXI   (59 << 8) |
| --- |

## [◆ ](#a22f873ffc10db62978e25cf7d91d3871)RA\_ICU\_IOPORT\_GROUP1

| #define RA\_ICU\_IOPORT\_GROUP1   (70 << 8) |
| --- |

## [◆ ](#a15906c3be13ddcf6142b9ee5a4eee25c)RA\_ICU\_IOPORT\_GROUP2

| #define RA\_ICU\_IOPORT\_GROUP2   (80 << 8) |
| --- |

## [◆ ](#ad4c9cc57137570f05a1d337b2ae2a40b)RA\_ICU\_IOPORT\_GROUP3

| #define RA\_ICU\_IOPORT\_GROUP3   (81 << 8) |
| --- |

## [◆ ](#a66b119c3f07b02d5fd7f6c667a2a408c)RA\_ICU\_IOPORT\_GROUP4

| #define RA\_ICU\_IOPORT\_GROUP4   (82 << 8) |
| --- |

## [◆ ](#a05110d1b8cd06173ab331cc65dba40ca)RA\_ICU\_IRQ\_UNSPECIFIED

| #define RA\_ICU\_IRQ\_UNSPECIFIED   (-1) |
| --- |

## [◆ ](#adab3ccfa14dc248d70aff5c0f6d8ae96)RA\_ICU\_IWDT\_NMIUNDF

| #define RA\_ICU\_IWDT\_NMIUNDF   (36 << 8) |
| --- |

## [◆ ](#a5f1e16c4b2a19230646186990d5ceacd)RA\_ICU\_KEY\_INTKR

| #define RA\_ICU\_KEY\_INTKR   (69 << 8) |
| --- |

## [◆ ](#a8f553978cc2639473df512776c5ac917)RA\_ICU\_LVD\_LVD1

| #define RA\_ICU\_LVD\_LVD1   (25 << 8) |
| --- |

## [◆ ](#a9021c40306177306d8358c7007b712ea)RA\_ICU\_LVD\_LVD2

| #define RA\_ICU\_LVD\_LVD2   (26 << 8) |
| --- |

## [◆ ](#a3a95d0e49b745378a08f5af9d8bd076c)RA\_ICU\_MOSC\_STOP

| #define RA\_ICU\_MOSC\_STOP   (28 << 8) |
| --- |

## [◆ ](#a6f1dbea7bc004de5b363f718a026251a)RA\_ICU\_POEG\_GROUP0

| #define RA\_ICU\_POEG\_GROUP0   (85 << 8) |
| --- |

## [◆ ](#a49c84bfba6c3a22c2beb4322f5a43ead)RA\_ICU\_POEG\_GROUP1

| #define RA\_ICU\_POEG\_GROUP1   (86 << 8) |
| --- |

## [◆ ](#abf57ee5d814699230bd42c83a0c9045f)RA\_ICU\_PORT\_IRQ0

| #define RA\_ICU\_PORT\_IRQ0   (1 << 8) |
| --- |

## [◆ ](#a9634f70b2e7ba85d94f3c89eb508f0a3)RA\_ICU\_PORT\_IRQ1

| #define RA\_ICU\_PORT\_IRQ1   (2 << 8) |
| --- |

## [◆ ](#a6960edc44b4e2fa6559b1b082d84cff7)RA\_ICU\_PORT\_IRQ10

| #define RA\_ICU\_PORT\_IRQ10   (11 << 8) |
| --- |

## [◆ ](#aca393b0ad400cedbaa54587fae03e7ef)RA\_ICU\_PORT\_IRQ11

| #define RA\_ICU\_PORT\_IRQ11   (12 << 8) |
| --- |

## [◆ ](#a3ed88347b1d60d0821bca20d3ad30ab5)RA\_ICU\_PORT\_IRQ12

| #define RA\_ICU\_PORT\_IRQ12   (13 << 8) |
| --- |

## [◆ ](#a62d4ea9916be89bc354b25196a352eea)RA\_ICU\_PORT\_IRQ14

| #define RA\_ICU\_PORT\_IRQ14   (15 << 8) |
| --- |

## [◆ ](#a61305c00d1a5290fa26b8b77139422df)RA\_ICU\_PORT\_IRQ15

| #define RA\_ICU\_PORT\_IRQ15   (16 << 8) |
| --- |

## [◆ ](#a9eec5e02aabf9da25e519b2d049dce29)RA\_ICU\_PORT\_IRQ2

| #define RA\_ICU\_PORT\_IRQ2   (3 << 8) |
| --- |

## [◆ ](#a5ca72014b0ef6093a8830cd3134fcb96)RA\_ICU\_PORT\_IRQ3

| #define RA\_ICU\_PORT\_IRQ3   (4 << 8) |
| --- |

## [◆ ](#a511eea99c1c288b58cd90d3992d27821)RA\_ICU\_PORT\_IRQ4

| #define RA\_ICU\_PORT\_IRQ4   (5 << 8) |
| --- |

## [◆ ](#a212fd596f370048148443973191c85a2)RA\_ICU\_PORT\_IRQ5

| #define RA\_ICU\_PORT\_IRQ5   (6 << 8) |
| --- |

## [◆ ](#a26aae8a3213343658ca725de656f4c4b)RA\_ICU\_PORT\_IRQ6

| #define RA\_ICU\_PORT\_IRQ6   (7 << 8) |
| --- |

## [◆ ](#a4dd558196b883fa869bae172b9c462fd)RA\_ICU\_PORT\_IRQ7

| #define RA\_ICU\_PORT\_IRQ7   (8 << 8) |
| --- |

## [◆ ](#a0df06e9ce6a74ffefc4f16cf7fdab1ed)RA\_ICU\_PORT\_IRQ8

| #define RA\_ICU\_PORT\_IRQ8   (9 << 8) |
| --- |

## [◆ ](#ac6d5188afe5ce472a4f1c6791383af63)RA\_ICU\_PORT\_IRQ9

| #define RA\_ICU\_PORT\_IRQ9   (10 << 8) |
| --- |

## [◆ ](#a122d35809141c4c5e6259f2c28393843)RA\_ICU\_RTC\_ALM

| #define RA\_ICU\_RTC\_ALM   (38 << 8) |
| --- |

## [◆ ](#ab577778d03f2b84cd0495f475c972a8b)RA\_ICU\_RTC\_CUP

| #define RA\_ICU\_RTC\_CUP   (40 << 8) |
| --- |

## [◆ ](#a7603e4b50fa1de24cf62e56a33174cdb)RA\_ICU\_RTC\_PRD

| #define RA\_ICU\_RTC\_PRD   (39 << 8) |
| --- |

## [◆ ](#a182ca7456f2165f1eee38fd3098be08d)RA\_ICU\_SCI0\_AM

| #define RA\_ICU\_SCI0\_AM   (156 << 8) |
| --- |

## [◆ ](#a4ffde15659be77a80b168566f3bac05f)RA\_ICU\_SCI0\_ERI

| #define RA\_ICU\_SCI0\_ERI   (155 << 8) |
| --- |

## [◆ ](#a40c3c9c05e5ad1bb7e87b0432ebff904)RA\_ICU\_SCI0\_RXI

| #define RA\_ICU\_SCI0\_RXI   (152 << 8) |
| --- |

## [◆ ](#ac7e0ddd146fd63b5201e4ad9954f1c37)RA\_ICU\_SCI0\_RXI\_OR\_ERI

| #define RA\_ICU\_SCI0\_RXI\_OR\_ERI   (157 << 8) |
| --- |

## [◆ ](#ac653e1d2f57daa4f68d36cc597e9e602)RA\_ICU\_SCI0\_TEI

| #define RA\_ICU\_SCI0\_TEI   (154 << 8) |
| --- |

## [◆ ](#a57ba91d0e16e044377c25eb42de3fc49)RA\_ICU\_SCI0\_TXI

| #define RA\_ICU\_SCI0\_TXI   (153 << 8) |
| --- |

## [◆ ](#add15456ded38a18a65695ecbce3b5260)RA\_ICU\_SCI1\_AM

| #define RA\_ICU\_SCI1\_AM   (162 << 8) |
| --- |

## [◆ ](#abb21ea5f21401509523b588ba8b2ef13)RA\_ICU\_SCI1\_ERI

| #define RA\_ICU\_SCI1\_ERI   (161 << 8) |
| --- |

## [◆ ](#a2f21bbc5eab47e5f5147433eb7b72933)RA\_ICU\_SCI1\_RXI

| #define RA\_ICU\_SCI1\_RXI   (158 << 8) |
| --- |

## [◆ ](#aec719867c9e414e0ca1605919724686a)RA\_ICU\_SCI1\_TEI

| #define RA\_ICU\_SCI1\_TEI   (160 << 8) |
| --- |

## [◆ ](#abf7bc3870a83a7a77ae602d564c87ca7)RA\_ICU\_SCI1\_TXI

| #define RA\_ICU\_SCI1\_TXI   (159 << 8) |
| --- |

## [◆ ](#a2e4b682b2dd6b98aab4a2f75efab13fc)RA\_ICU\_SCI2\_AM

| #define RA\_ICU\_SCI2\_AM   (167 << 8) |
| --- |

## [◆ ](#a47ee241b2d274073589caa6927560086)RA\_ICU\_SCI2\_ERI

| #define RA\_ICU\_SCI2\_ERI   (166 << 8) |
| --- |

## [◆ ](#af0804956b3eed5d26bbde37e6e357344)RA\_ICU\_SCI2\_RXI

| #define RA\_ICU\_SCI2\_RXI   (163 << 8) |
| --- |

## [◆ ](#ab7d61b58fb61724a0233a1b639583e6e)RA\_ICU\_SCI2\_TEI

| #define RA\_ICU\_SCI2\_TEI   (165 << 8) |
| --- |

## [◆ ](#ac1f3bfddffdebbb101bc0359cd6cab49)RA\_ICU\_SCI2\_TXI

| #define RA\_ICU\_SCI2\_TXI   (164 << 8) |
| --- |

## [◆ ](#ad6392ad85038f9351ec08a15bb64f48a)RA\_ICU\_SCI9\_AM

| #define RA\_ICU\_SCI9\_AM   (172 << 8) |
| --- |

## [◆ ](#a0747a5eef57cfc36ba79eb507600ddcb)RA\_ICU\_SCI9\_ERI

| #define RA\_ICU\_SCI9\_ERI   (171 << 8) |
| --- |

## [◆ ](#ab884249dba2c79f8db45c3103d0d226d)RA\_ICU\_SCI9\_RXI

| #define RA\_ICU\_SCI9\_RXI   (168 << 8) |
| --- |

## [◆ ](#af5bd5bd5bf54e8419f11991b802971d5)RA\_ICU\_SCI9\_TEI

| #define RA\_ICU\_SCI9\_TEI   (170 << 8) |
| --- |

## [◆ ](#a4a346c13f597718642232c2a34e72500)RA\_ICU\_SCI9\_TXI

| #define RA\_ICU\_SCI9\_TXI   (169 << 8) |
| --- |

## [◆ ](#a2157ac9a24687c1908d7cc61d4a01c8c)RA\_ICU\_SPI0\_SPEI

| #define RA\_ICU\_SPI0\_SPEI   (176 << 8) |
| --- |

## [◆ ](#a8542542186b2ccddd35d3ea42346c2cc)RA\_ICU\_SPI0\_SPII

| #define RA\_ICU\_SPI0\_SPII   (175 << 8) |
| --- |

## [◆ ](#a40180b3f1bf6709fa0ee4c0bea7e1aab)RA\_ICU\_SPI0\_SPRI

| #define RA\_ICU\_SPI0\_SPRI   (173 << 8) |
| --- |

## [◆ ](#a86c91cfc649778ecd66c8b758cb12889)RA\_ICU\_SPI0\_SPTEND

| #define RA\_ICU\_SPI0\_SPTEND   (177 << 8) |
| --- |

## [◆ ](#a19e62564a5b29f7489e44477d1ff9ceb)RA\_ICU\_SPI0\_SPTI

| #define RA\_ICU\_SPI0\_SPTI   (174 << 8) |
| --- |

## [◆ ](#acaafc80142dfa897c6bf279b486790a8)RA\_ICU\_SPI1\_SPEI

| #define RA\_ICU\_SPI1\_SPEI   (181 << 8) |
| --- |

## [◆ ](#a5cd3019eb2a3ba3628c128ddb913caac)RA\_ICU\_SPI1\_SPII

| #define RA\_ICU\_SPI1\_SPII   (180 << 8) |
| --- |

## [◆ ](#ac6b192a749d09b44078e14e1dd2764a9)RA\_ICU\_SPI1\_SPRI

| #define RA\_ICU\_SPI1\_SPRI   (178 << 8) |
| --- |

## [◆ ](#a3222b0bbdbcc58b5e7ce141a9c4dc3f1)RA\_ICU\_SPI1\_SPTEND

| #define RA\_ICU\_SPI1\_SPTEND   (182 << 8) |
| --- |

## [◆ ](#ade2108762cd0b9d5f0667feda347e1fa)RA\_ICU\_SPI1\_SPTI

| #define RA\_ICU\_SPI1\_SPTI   (179 << 8) |
| --- |

## [◆ ](#ab93ca169682fe4d055e672751b41a8fe)RA\_ICU\_SSIE0\_SSIF

| #define RA\_ICU\_SSIE0\_SSIF   (65 << 8) |
| --- |

## [◆ ](#a3c629d8751df452f69a2e1861e8792c9)RA\_ICU\_SSIE0\_SSIRXI

| #define RA\_ICU\_SSIE0\_SSIRXI   (63 << 8) |
| --- |

## [◆ ](#a7fdce8fba57936a4b41d8f07e6526ea6)RA\_ICU\_SSIE0\_SSITXI

| #define RA\_ICU\_SSIE0\_SSITXI   (62 << 8) |
| --- |

## [◆ ](#aa329c9eade412d1d927ddc3cb2bdd308)RA\_ICU\_SYSTEM\_SNZREQ

| #define RA\_ICU\_SYSTEM\_SNZREQ   (29 << 8) |
| --- |

## [◆ ](#af1d44243752a66eaca69e2da756057c1)RA\_ICU\_USBFS\_D0FIFO

| #define RA\_ICU\_USBFS\_D0FIFO   (49 << 8) |
| --- |

## [◆ ](#af91ab097f8dac586dbfbb94608248a55)RA\_ICU\_USBFS\_D1FIFO

| #define RA\_ICU\_USBFS\_D1FIFO   (50 << 8) |
| --- |

## [◆ ](#ad29c8fff1390a867d5b8329c8b277ef6)RA\_ICU\_USBFS\_USBI

| #define RA\_ICU\_USBFS\_USBI   (51 << 8) |
| --- |

## [◆ ](#aedfde20ed81105ab5ec6fc9f15ec8e05)RA\_ICU\_USBFS\_USBR

| #define RA\_ICU\_USBFS\_USBR   (52 << 8) |
| --- |

## [◆ ](#acd4f7fbf1bfe48dd9aabc291c251069c)RA\_ICU\_VBATT\_LVD

| #define RA\_ICU\_VBATT\_LVD   (27 << 8) |
| --- |

## [◆ ](#ae862b2d094199f06502027841cfc2d8e)RA\_ICU\_WDT\_NMIUNDF

| #define RA\_ICU\_WDT\_NMIUNDF   (37 << 8) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [renesas-ra-icu.h](renesas-ra-icu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
