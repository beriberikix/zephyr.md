---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/silabs-adc_8h.html
original_path: doxygen/html/silabs-adc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

silabs-adc.h File Reference

[Go to the source code of this file.](silabs-adc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IADC\_INPUT\_GND](#a9079872ea673c06f1b5a230b03bf20be)   0x0 |
| #define | [IADC\_INPUT\_AVDD](#a75e46fbc6e20324b32fe8be3e0256e78)   0x10 |
| #define | [IADC\_INPUT\_IOVDD](#a9652ed876e1e1c70c78989a3c8fe2c5a)   0x11 |
| #define | [IADC\_INPUT\_VBAT](#a1d95665004651be5690df6514963c998)   0x12 |
| #define | [IADC\_INPUT\_DVDD](#a62218ff41ed9f715432ce73f5051ebc8)   0x14 |
| #define | [IADC\_INPUT\_DECOUPLE](#acb7877862a52d4615163a3b0920965bc)   0x17 |
| #define | [IADC\_INPUT\_DAC0](#a6a40ee65efc6fa504d0e6072d3884b95)   0x20 |
| #define | [IADC\_INPUT\_DAC1](#a1865e9caafa9bd81462a90c416f3dd31)   0x20 |
| #define | [IADC\_INPUT\_AIN0](#a1e1fd182523dec625a3b22a63a6842f8)   0x40 |
| #define | [IADC\_INPUT\_AIN1](#a3eb2b55b9c28781a2b9dcdca470fcd48)   0x40 |
| #define | [IADC\_INPUT\_AIN2](#a2e79855494312988073fef58f43c3418)   0x50 |
| #define | [IADC\_INPUT\_AIN3](#a52508deb9e959478d067ff6a55489952)   0x50 |
| #define | [IADC\_INPUT\_PA0](#ae01eb7dc9f88a360e6c97e3dfdde539f)   0x80 |
| #define | [IADC\_INPUT\_PA1](#a6ffc4a2461f826f78eaefdf11ec00c6f)   0x81 |
| #define | [IADC\_INPUT\_PA2](#a0a4818ce30f117dcfe00f2f3c36ee29e)   0x82 |
| #define | [IADC\_INPUT\_PA3](#ab14c513d6cd0e0d9a1690726b0ba74ab)   0x83 |
| #define | [IADC\_INPUT\_PA4](#afede8e08309862ee0ef7a50430e6e142)   0x84 |
| #define | [IADC\_INPUT\_PA5](#acb8e8533e447869d108d517b264bfae0)   0x85 |
| #define | [IADC\_INPUT\_PA6](#ab8c553e8e3e8a378e3b2ce1327026077)   0x86 |
| #define | [IADC\_INPUT\_PA7](#ade7fc9d6fc81a6d8acda0c74c6827fa2)   0x87 |
| #define | [IADC\_INPUT\_PA8](#a11338173315ccdc6d646e11db4502c35)   0x88 |
| #define | [IADC\_INPUT\_PA9](#ac1c3c9b80108b2a907a84895c0d32c7b)   0x89 |
| #define | [IADC\_INPUT\_PA10](#ac7ca251cbeca7fbbb12dbb1908754f05)   0x8a |
| #define | [IADC\_INPUT\_PA11](#aa68136120c51941db7200354ecfbed61)   0x8b |
| #define | [IADC\_INPUT\_PA12](#aaa2927d1af01d105467d9881b3f450e7)   0x8c |
| #define | [IADC\_INPUT\_PA13](#ab7ce2f74294a5bc46038254386fa1a61)   0x8d |
| #define | [IADC\_INPUT\_PA14](#a15de625ff8ec01d61f75a16e64891a36)   0x8e |
| #define | [IADC\_INPUT\_PA15](#a8ac4ba4b0ac3c7d2fc330b65c89e8d5b)   0x8f |
| #define | [IADC\_INPUT\_PB0](#aa6694af6e25f57a2146dbaca259d733b)   0x90 |
| #define | [IADC\_INPUT\_PB1](#a157a18d5e9f0646a884e58ed4a16971e)   0x91 |
| #define | [IADC\_INPUT\_PB2](#a003bb5c9f7590feb9706aae237932af2)   0x92 |
| #define | [IADC\_INPUT\_PB3](#ad7857d33939eb403f39b6dbeef17db7a)   0x93 |
| #define | [IADC\_INPUT\_PB4](#a620d251d1dbe7829a17ca8a8f3a52313)   0x94 |
| #define | [IADC\_INPUT\_PB5](#a7d149889e0b481c61cb5dbba978686dc)   0x95 |
| #define | [IADC\_INPUT\_PB6](#a84bf6e5f5b04182470c99a950db489ee)   0x96 |
| #define | [IADC\_INPUT\_PB7](#afa0ee61b1f99a2d3b73e5ff542cfe847)   0x97 |
| #define | [IADC\_INPUT\_PB8](#a419af9002216fd569e572a7f7a0d86b4)   0x98 |
| #define | [IADC\_INPUT\_PB9](#ab26fa11eb4f135c0979be193b5fdb2a2)   0x99 |
| #define | [IADC\_INPUT\_PB10](#ab8cc977d0451ab50f91513db1a1b286c)   0x9a |
| #define | [IADC\_INPUT\_PB11](#a65cbdacf5bc04e257ff59e8ff103a1bb)   0x9b |
| #define | [IADC\_INPUT\_PB12](#a181c6efb18e6f1f8e88f895c9c06a2bb)   0x9c |
| #define | [IADC\_INPUT\_PB13](#aaa44c54bf4a5e2f639b452b91ec760e1)   0x9d |
| #define | [IADC\_INPUT\_PB14](#a3404f935df4a0150d5fa2450b48db1b9)   0x9e |
| #define | [IADC\_INPUT\_PB15](#a0d95e53263e6f9d81d3c8943a2528bba)   0x9f |
| #define | [IADC\_INPUT\_PC0](#a77e8660bcbab59fdd002aa47b8e3b995)   0xa0 |
| #define | [IADC\_INPUT\_PC1](#a391aa1ccf0f182e27bf0aa7aabf3e205)   0xa1 |
| #define | [IADC\_INPUT\_PC2](#ae8cf398da121239f7ba8f1ceccef6a18)   0xa2 |
| #define | [IADC\_INPUT\_PC3](#a406447621d396d998877810b645d65af)   0xa3 |
| #define | [IADC\_INPUT\_PC4](#afeb58f1db5c0b4da7b8c2b0a1bdb9ecc)   0xa4 |
| #define | [IADC\_INPUT\_PC5](#ac2907ed9ec541dcae0d81c407b441049)   0xa5 |
| #define | [IADC\_INPUT\_PC6](#a9fecac8f1471f9436b4441c21ebd07f4)   0xa6 |
| #define | [IADC\_INPUT\_PC7](#a401929f4fbf5f82d128b22212710f4e2)   0xa7 |
| #define | [IADC\_INPUT\_PC8](#ac410e6eac0e8d73fe06eda7df9ac20d9)   0xa8 |
| #define | [IADC\_INPUT\_PC9](#acd2469da9e3eef7dfebed6a07e3af30d)   0xa9 |
| #define | [IADC\_INPUT\_PC10](#ac37c781befe71ce9077ac307b16a222a)   0xaa |
| #define | [IADC\_INPUT\_PC11](#a59b4a6d1af4626b77bc75068cd4aac15)   0xab |
| #define | [IADC\_INPUT\_PC12](#a72e630578e8f563c58b44bb91d7aecdf)   0xac |
| #define | [IADC\_INPUT\_PC13](#a497a9d0ea97dfc8b5b78f1a5ee6828f3)   0xad |
| #define | [IADC\_INPUT\_PC14](#a054b25a920bb2c69a279cf8abd4ceb3d)   0xae |
| #define | [IADC\_INPUT\_PC15](#a83092d0164d57b876977faef4dd37691)   0xaf |
| #define | [IADC\_INPUT\_PD0](#ae6f84fc8b9d449f4a50db9c4fbbe90e5)   0xb0 |
| #define | [IADC\_INPUT\_PD1](#a8f923038d52f9c3e398ce48e4f9bb5fa)   0xb1 |
| #define | [IADC\_INPUT\_PD2](#a0236011d3ec6581f8b6b3a1815cdab98)   0xb2 |
| #define | [IADC\_INPUT\_PD3](#a1b845cdb16de1228f1b315a8e6b1b362)   0xb3 |
| #define | [IADC\_INPUT\_PD4](#a678a9a11a20ef8f8d02983f8320cf992)   0xb4 |
| #define | [IADC\_INPUT\_PD5](#a1e5e52ee545dc7bbecb6a9d3c2375081)   0xb5 |
| #define | [IADC\_INPUT\_PD6](#a8a4444973af60ea0f50d24126056f781)   0xb6 |
| #define | [IADC\_INPUT\_PD7](#a6bb8b5c7df7b11e5904025070aff65f9)   0xb7 |
| #define | [IADC\_INPUT\_PD8](#acf84c4ad299b0989f675d45e7004f7d9)   0xb8 |
| #define | [IADC\_INPUT\_PD9](#a92b2b775b202733da79af6d4108017eb)   0xb9 |
| #define | [IADC\_INPUT\_PD10](#a13f8688b6615f2ea98a384205e642948)   0xba |
| #define | [IADC\_INPUT\_PD11](#afaec243c4edb30f9b91e8f7a2f1aeb55)   0xbb |
| #define | [IADC\_INPUT\_PD12](#afce1e43a5b1a7b1673f527efc7bbaf28)   0xbc |
| #define | [IADC\_INPUT\_PD13](#adb93e82ea442465566000dd175d503f1)   0xbd |
| #define | [IADC\_INPUT\_PD14](#a58a43a78414fefa7577f5d377873054c)   0xbe |
| #define | [IADC\_INPUT\_PD15](#acf87bf9d9c95a05ea5e9b3359ec64396)   0xbf |

## Macro Definition Documentation

## [◆ ](#a1e1fd182523dec625a3b22a63a6842f8)IADC\_INPUT\_AIN0

| #define IADC\_INPUT\_AIN0   0x40 |
| --- |

## [◆ ](#a3eb2b55b9c28781a2b9dcdca470fcd48)IADC\_INPUT\_AIN1

| #define IADC\_INPUT\_AIN1   0x40 |
| --- |

## [◆ ](#a2e79855494312988073fef58f43c3418)IADC\_INPUT\_AIN2

| #define IADC\_INPUT\_AIN2   0x50 |
| --- |

## [◆ ](#a52508deb9e959478d067ff6a55489952)IADC\_INPUT\_AIN3

| #define IADC\_INPUT\_AIN3   0x50 |
| --- |

## [◆ ](#a75e46fbc6e20324b32fe8be3e0256e78)IADC\_INPUT\_AVDD

| #define IADC\_INPUT\_AVDD   0x10 |
| --- |

## [◆ ](#a6a40ee65efc6fa504d0e6072d3884b95)IADC\_INPUT\_DAC0

| #define IADC\_INPUT\_DAC0   0x20 |
| --- |

## [◆ ](#a1865e9caafa9bd81462a90c416f3dd31)IADC\_INPUT\_DAC1

| #define IADC\_INPUT\_DAC1   0x20 |
| --- |

## [◆ ](#acb7877862a52d4615163a3b0920965bc)IADC\_INPUT\_DECOUPLE

| #define IADC\_INPUT\_DECOUPLE   0x17 |
| --- |

## [◆ ](#a62218ff41ed9f715432ce73f5051ebc8)IADC\_INPUT\_DVDD

| #define IADC\_INPUT\_DVDD   0x14 |
| --- |

## [◆ ](#a9079872ea673c06f1b5a230b03bf20be)IADC\_INPUT\_GND

| #define IADC\_INPUT\_GND   0x0 |
| --- |

## [◆ ](#a9652ed876e1e1c70c78989a3c8fe2c5a)IADC\_INPUT\_IOVDD

| #define IADC\_INPUT\_IOVDD   0x11 |
| --- |

## [◆ ](#ae01eb7dc9f88a360e6c97e3dfdde539f)IADC\_INPUT\_PA0

| #define IADC\_INPUT\_PA0   0x80 |
| --- |

## [◆ ](#a6ffc4a2461f826f78eaefdf11ec00c6f)IADC\_INPUT\_PA1

| #define IADC\_INPUT\_PA1   0x81 |
| --- |

## [◆ ](#ac7ca251cbeca7fbbb12dbb1908754f05)IADC\_INPUT\_PA10

| #define IADC\_INPUT\_PA10   0x8a |
| --- |

## [◆ ](#aa68136120c51941db7200354ecfbed61)IADC\_INPUT\_PA11

| #define IADC\_INPUT\_PA11   0x8b |
| --- |

## [◆ ](#aaa2927d1af01d105467d9881b3f450e7)IADC\_INPUT\_PA12

| #define IADC\_INPUT\_PA12   0x8c |
| --- |

## [◆ ](#ab7ce2f74294a5bc46038254386fa1a61)IADC\_INPUT\_PA13

| #define IADC\_INPUT\_PA13   0x8d |
| --- |

## [◆ ](#a15de625ff8ec01d61f75a16e64891a36)IADC\_INPUT\_PA14

| #define IADC\_INPUT\_PA14   0x8e |
| --- |

## [◆ ](#a8ac4ba4b0ac3c7d2fc330b65c89e8d5b)IADC\_INPUT\_PA15

| #define IADC\_INPUT\_PA15   0x8f |
| --- |

## [◆ ](#a0a4818ce30f117dcfe00f2f3c36ee29e)IADC\_INPUT\_PA2

| #define IADC\_INPUT\_PA2   0x82 |
| --- |

## [◆ ](#ab14c513d6cd0e0d9a1690726b0ba74ab)IADC\_INPUT\_PA3

| #define IADC\_INPUT\_PA3   0x83 |
| --- |

## [◆ ](#afede8e08309862ee0ef7a50430e6e142)IADC\_INPUT\_PA4

| #define IADC\_INPUT\_PA4   0x84 |
| --- |

## [◆ ](#acb8e8533e447869d108d517b264bfae0)IADC\_INPUT\_PA5

| #define IADC\_INPUT\_PA5   0x85 |
| --- |

## [◆ ](#ab8c553e8e3e8a378e3b2ce1327026077)IADC\_INPUT\_PA6

| #define IADC\_INPUT\_PA6   0x86 |
| --- |

## [◆ ](#ade7fc9d6fc81a6d8acda0c74c6827fa2)IADC\_INPUT\_PA7

| #define IADC\_INPUT\_PA7   0x87 |
| --- |

## [◆ ](#a11338173315ccdc6d646e11db4502c35)IADC\_INPUT\_PA8

| #define IADC\_INPUT\_PA8   0x88 |
| --- |

## [◆ ](#ac1c3c9b80108b2a907a84895c0d32c7b)IADC\_INPUT\_PA9

| #define IADC\_INPUT\_PA9   0x89 |
| --- |

## [◆ ](#aa6694af6e25f57a2146dbaca259d733b)IADC\_INPUT\_PB0

| #define IADC\_INPUT\_PB0   0x90 |
| --- |

## [◆ ](#a157a18d5e9f0646a884e58ed4a16971e)IADC\_INPUT\_PB1

| #define IADC\_INPUT\_PB1   0x91 |
| --- |

## [◆ ](#ab8cc977d0451ab50f91513db1a1b286c)IADC\_INPUT\_PB10

| #define IADC\_INPUT\_PB10   0x9a |
| --- |

## [◆ ](#a65cbdacf5bc04e257ff59e8ff103a1bb)IADC\_INPUT\_PB11

| #define IADC\_INPUT\_PB11   0x9b |
| --- |

## [◆ ](#a181c6efb18e6f1f8e88f895c9c06a2bb)IADC\_INPUT\_PB12

| #define IADC\_INPUT\_PB12   0x9c |
| --- |

## [◆ ](#aaa44c54bf4a5e2f639b452b91ec760e1)IADC\_INPUT\_PB13

| #define IADC\_INPUT\_PB13   0x9d |
| --- |

## [◆ ](#a3404f935df4a0150d5fa2450b48db1b9)IADC\_INPUT\_PB14

| #define IADC\_INPUT\_PB14   0x9e |
| --- |

## [◆ ](#a0d95e53263e6f9d81d3c8943a2528bba)IADC\_INPUT\_PB15

| #define IADC\_INPUT\_PB15   0x9f |
| --- |

## [◆ ](#a003bb5c9f7590feb9706aae237932af2)IADC\_INPUT\_PB2

| #define IADC\_INPUT\_PB2   0x92 |
| --- |

## [◆ ](#ad7857d33939eb403f39b6dbeef17db7a)IADC\_INPUT\_PB3

| #define IADC\_INPUT\_PB3   0x93 |
| --- |

## [◆ ](#a620d251d1dbe7829a17ca8a8f3a52313)IADC\_INPUT\_PB4

| #define IADC\_INPUT\_PB4   0x94 |
| --- |

## [◆ ](#a7d149889e0b481c61cb5dbba978686dc)IADC\_INPUT\_PB5

| #define IADC\_INPUT\_PB5   0x95 |
| --- |

## [◆ ](#a84bf6e5f5b04182470c99a950db489ee)IADC\_INPUT\_PB6

| #define IADC\_INPUT\_PB6   0x96 |
| --- |

## [◆ ](#afa0ee61b1f99a2d3b73e5ff542cfe847)IADC\_INPUT\_PB7

| #define IADC\_INPUT\_PB7   0x97 |
| --- |

## [◆ ](#a419af9002216fd569e572a7f7a0d86b4)IADC\_INPUT\_PB8

| #define IADC\_INPUT\_PB8   0x98 |
| --- |

## [◆ ](#ab26fa11eb4f135c0979be193b5fdb2a2)IADC\_INPUT\_PB9

| #define IADC\_INPUT\_PB9   0x99 |
| --- |

## [◆ ](#a77e8660bcbab59fdd002aa47b8e3b995)IADC\_INPUT\_PC0

| #define IADC\_INPUT\_PC0   0xa0 |
| --- |

## [◆ ](#a391aa1ccf0f182e27bf0aa7aabf3e205)IADC\_INPUT\_PC1

| #define IADC\_INPUT\_PC1   0xa1 |
| --- |

## [◆ ](#ac37c781befe71ce9077ac307b16a222a)IADC\_INPUT\_PC10

| #define IADC\_INPUT\_PC10   0xaa |
| --- |

## [◆ ](#a59b4a6d1af4626b77bc75068cd4aac15)IADC\_INPUT\_PC11

| #define IADC\_INPUT\_PC11   0xab |
| --- |

## [◆ ](#a72e630578e8f563c58b44bb91d7aecdf)IADC\_INPUT\_PC12

| #define IADC\_INPUT\_PC12   0xac |
| --- |

## [◆ ](#a497a9d0ea97dfc8b5b78f1a5ee6828f3)IADC\_INPUT\_PC13

| #define IADC\_INPUT\_PC13   0xad |
| --- |

## [◆ ](#a054b25a920bb2c69a279cf8abd4ceb3d)IADC\_INPUT\_PC14

| #define IADC\_INPUT\_PC14   0xae |
| --- |

## [◆ ](#a83092d0164d57b876977faef4dd37691)IADC\_INPUT\_PC15

| #define IADC\_INPUT\_PC15   0xaf |
| --- |

## [◆ ](#ae8cf398da121239f7ba8f1ceccef6a18)IADC\_INPUT\_PC2

| #define IADC\_INPUT\_PC2   0xa2 |
| --- |

## [◆ ](#a406447621d396d998877810b645d65af)IADC\_INPUT\_PC3

| #define IADC\_INPUT\_PC3   0xa3 |
| --- |

## [◆ ](#afeb58f1db5c0b4da7b8c2b0a1bdb9ecc)IADC\_INPUT\_PC4

| #define IADC\_INPUT\_PC4   0xa4 |
| --- |

## [◆ ](#ac2907ed9ec541dcae0d81c407b441049)IADC\_INPUT\_PC5

| #define IADC\_INPUT\_PC5   0xa5 |
| --- |

## [◆ ](#a9fecac8f1471f9436b4441c21ebd07f4)IADC\_INPUT\_PC6

| #define IADC\_INPUT\_PC6   0xa6 |
| --- |

## [◆ ](#a401929f4fbf5f82d128b22212710f4e2)IADC\_INPUT\_PC7

| #define IADC\_INPUT\_PC7   0xa7 |
| --- |

## [◆ ](#ac410e6eac0e8d73fe06eda7df9ac20d9)IADC\_INPUT\_PC8

| #define IADC\_INPUT\_PC8   0xa8 |
| --- |

## [◆ ](#acd2469da9e3eef7dfebed6a07e3af30d)IADC\_INPUT\_PC9

| #define IADC\_INPUT\_PC9   0xa9 |
| --- |

## [◆ ](#ae6f84fc8b9d449f4a50db9c4fbbe90e5)IADC\_INPUT\_PD0

| #define IADC\_INPUT\_PD0   0xb0 |
| --- |

## [◆ ](#a8f923038d52f9c3e398ce48e4f9bb5fa)IADC\_INPUT\_PD1

| #define IADC\_INPUT\_PD1   0xb1 |
| --- |

## [◆ ](#a13f8688b6615f2ea98a384205e642948)IADC\_INPUT\_PD10

| #define IADC\_INPUT\_PD10   0xba |
| --- |

## [◆ ](#afaec243c4edb30f9b91e8f7a2f1aeb55)IADC\_INPUT\_PD11

| #define IADC\_INPUT\_PD11   0xbb |
| --- |

## [◆ ](#afce1e43a5b1a7b1673f527efc7bbaf28)IADC\_INPUT\_PD12

| #define IADC\_INPUT\_PD12   0xbc |
| --- |

## [◆ ](#adb93e82ea442465566000dd175d503f1)IADC\_INPUT\_PD13

| #define IADC\_INPUT\_PD13   0xbd |
| --- |

## [◆ ](#a58a43a78414fefa7577f5d377873054c)IADC\_INPUT\_PD14

| #define IADC\_INPUT\_PD14   0xbe |
| --- |

## [◆ ](#acf87bf9d9c95a05ea5e9b3359ec64396)IADC\_INPUT\_PD15

| #define IADC\_INPUT\_PD15   0xbf |
| --- |

## [◆ ](#a0236011d3ec6581f8b6b3a1815cdab98)IADC\_INPUT\_PD2

| #define IADC\_INPUT\_PD2   0xb2 |
| --- |

## [◆ ](#a1b845cdb16de1228f1b315a8e6b1b362)IADC\_INPUT\_PD3

| #define IADC\_INPUT\_PD3   0xb3 |
| --- |

## [◆ ](#a678a9a11a20ef8f8d02983f8320cf992)IADC\_INPUT\_PD4

| #define IADC\_INPUT\_PD4   0xb4 |
| --- |

## [◆ ](#a1e5e52ee545dc7bbecb6a9d3c2375081)IADC\_INPUT\_PD5

| #define IADC\_INPUT\_PD5   0xb5 |
| --- |

## [◆ ](#a8a4444973af60ea0f50d24126056f781)IADC\_INPUT\_PD6

| #define IADC\_INPUT\_PD6   0xb6 |
| --- |

## [◆ ](#a6bb8b5c7df7b11e5904025070aff65f9)IADC\_INPUT\_PD7

| #define IADC\_INPUT\_PD7   0xb7 |
| --- |

## [◆ ](#acf84c4ad299b0989f675d45e7004f7d9)IADC\_INPUT\_PD8

| #define IADC\_INPUT\_PD8   0xb8 |
| --- |

## [◆ ](#a92b2b775b202733da79af6d4108017eb)IADC\_INPUT\_PD9

| #define IADC\_INPUT\_PD9   0xb9 |
| --- |

## [◆ ](#a1d95665004651be5690df6514963c998)IADC\_INPUT\_VBAT

| #define IADC\_INPUT\_VBAT   0x12 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [silabs-adc.h](silabs-adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
