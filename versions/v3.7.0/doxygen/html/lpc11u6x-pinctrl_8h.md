---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/lpc11u6x-pinctrl_8h.html
original_path: doxygen/html/lpc11u6x-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lpc11u6x-pinctrl.h File Reference

[Go to the source code of this file.](lpc11u6x-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IOCON\_FUNC0](#ab08f72eae45dd5656aeca24c346c8626)   0 |
|  | Pin control register for standard digital I/O pins: |
| #define | [IOCON\_FUNC1](#ab6449233bd56957c684b9ad694606e3a)   1 |
| #define | [IOCON\_FUNC2](#a43ebb7abf055ce2491fbba5ef72f6fc7)   2 |
| #define | [IOCON\_FUNC3](#ace4708e511b3aa9c352600604331bec0)   3 |
| #define | [IOCON\_FUNC4](#ac621b96a2bd1ee57a83ff1af98287a8d)   4 |
| #define | [IOCON\_FUNC5](#a0f9630599f40a3f96a5887c7e65508a9)   5 |
| #define | [IOCON\_MODE\_INACT](#afc593aafe607c88c52864ecb7586ffe9)   (0 << 3) /\* No pull resistor. \*/ |
| #define | [IOCON\_MODE\_PULLDOWN](#a270261df49234519bfd09e076dfcec6c)   (1 << 3) /\* Enable pull-down resistor. \*/ |
| #define | [IOCON\_MODE\_PULLUP](#ad8fe947d8e7076d6cec01a5b30261141)   (2 << 3) /\* Enable Pull-up resistor. \*/ |
| #define | [IOCON\_MODE\_REPEATER](#a53d705841cc362c6f43ffc1370d71726)   (3 << 3) /\* Repeater mode. \*/ |
| #define | [IOCON\_HYS\_EN](#afb7c408ac1f52b7b7e46fde3061fe0b7)   (1 << 5) /\* Enable hysteresis. \*/ |
| #define | [IOCON\_INV\_EN](#ae1fd1faa316f6c3108b499928f8c9922)   (1 << 6) /\* Invert input polarity. \*/ |
| #define | [IOCON\_ADMODE\_EN](#a9a3d4f3e281c382f795b9a769073d4e4)   (0 << 7) /\* Enable analog input mode. \*/ |
| #define | [IOCON\_DIGMODE\_EN](#a516e9d9bc7b1f3aaefd9d09c6ece74d2)   (1 << 7) /\* Enable digital I/O mode. \*/ |
| #define | [IOCON\_FILTR\_DIS](#a5a141a4fd02a8a7204cb251e1815b2ff)   (1 << 8) /\* Disable noise filtering. \*/ |
| #define | [IOCON\_SFI2C\_EN](#aa7dd24866523506919c8f3fa7a8614a8)   (0 << 8) /\* I2C standard mode / Fast-mode. \*/ |
| #define | [IOCON\_STDI2C\_EN](#a897f505b779e01014e235f1d73745787)   (1 << 8) /\* GPIO functionality. \*/ |
| #define | [IOCON\_FASTI2C\_EN](#a5454c9c23da82b9db63d63866d054989)   (2 << 8) /\* I2C Fast-mode Plus. \*/ |
| #define | [IOCON\_OPENDRAIN\_EN](#a226b54f672e61a7a2d2893d9ef8cbc9c)   (1 << 10) /\* Enable [open](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b)-drain mode. \*/ |
| #define | [IOCON\_S\_MODE\_0CLK](#a05f3ba263e98d5ee980f1604e5bb901c)   (0 << 11) /\* No input filter. \*/ |
| #define | [IOCON\_S\_MODE\_1CLK](#a7148355cde16d13476362ff1c1bc1668)   (1 << 11) |
| #define | [IOCON\_S\_MODE\_2CLK](#a87827c87941a76ce73118c65afb439f5)   (2 << 11) |
| #define | [IOCON\_S\_MODE\_3CLK](#a54dba7082ab18b6a15eea0a87c119a71)   (3 << 11) |
| #define | [IOCON\_CLKDIV0](#a32dad85c69cde862614f7dc694de25e1)   (0 << 13) |
| #define | [IOCON\_CLKDIV1](#a9cf0243a32cce57e52c3b3931979a0c4)   (1 << 13) |
| #define | [IOCON\_CLKDIV2](#a05aed1b2f2679b3bb56a1bdc08e032a1)   (2 << 13) |
| #define | [IOCON\_CLKDIV3](#a96b9d2b722278cdc733ddec36aca82b8)   (3 << 13) |
| #define | [IOCON\_CLKDIV4](#a293173c3047155fd78ba45a0f4e464f5)   (4 << 13) |
| #define | [IOCON\_CLKDIV5](#aecba1dab2a9cb8c19052ab56c7efbc6d)   (5 << 13) |
| #define | [IOCON\_CLKDIV6](#a25f5cc1afc44889d9e77b62923135411)   (6 << 13) |
| #define | [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(offset, type, mux) |
| #define | [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba)   0x0 |
| #define | [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb)   0x1 |
| #define | [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)   0x2 |
| #define | [RESET\_PIO0\_0](#abd7869399ab5c12219c1d7e06885e391)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(0, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_0 \*/ |
| #define | [PIO0\_0\_PIO0\_0](#aa1d6732f64540461cae792821ac7b2d6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(0, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_0 \*/ |
| #define | [PIO0\_1\_PIO0\_1](#ab44c7ff7f772892dbb66149d8064ba04)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_1 \*/ |
| #define | [CLKOUT\_PIO0\_1](#a4d2452db92940671b276775adec24700)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_1 \*/ |
| #define | [CT32B0\_MAT2\_PIO0\_1](#aa6fbfccc166375429d6c720684686a24)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_1 \*/ |
| #define | [USB\_FTOGGLE\_PIO0\_1](#a827fea9b1eb5d3d16dbb1f95bd06b40e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_1 \*/ |
| #define | [PIO0\_2\_PIO0\_2](#ab5a06c37a003d97135fc0da7c9949f60)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_2 \*/ |
| #define | [SSP0\_SSEL\_PIO0\_2](#a883806b472afb21f170006c620fe2b2d)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_2 \*/ |
| #define | [CT16B0\_CAP0\_PIO0\_2](#a2c44ad39551919eaf469137d3d37f78b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_2 \*/ |
| #define | [R\_0\_PIO0\_2](#a497b4217421b6854a707201765ff12a8)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_2 \*/ |
| #define | [PIO0\_3\_PIO0\_3](#a89f6d1689c8672f14033a31543ced43a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(3, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_3 \*/ |
| #define | [USB\_VBUS\_PIO0\_3](#a410001d990fb8424e9f6d75f6a7f2c67)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(3, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_3 \*/ |
| #define | [R\_1\_PIO0\_3](#a54242b6862e052d7d1c2ee998b6d3927)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(3, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_3 \*/ |
| #define | [PIO0\_4\_PIO0\_4](#a017c42b9bbbacfbbd9310b3f1a918a66)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(4, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 0) /\* PIO0\_4 \*/ |
| #define | [I2C0\_SCL\_PIO0\_4](#af03e2705d8630f60521f853e9b4b1d61)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(4, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 1) /\* PIO0\_4 \*/ |
| #define | [R\_2\_PIO0\_4](#ab0e34b062fd26c27d29891c77d8542a0)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(4, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 2) /\* PIO0\_4 \*/ |
| #define | [PIO0\_5\_PIO0\_5](#aa0fe8d6e7a4f69dd54980143f92df7ab)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(5, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 0) /\* PIO0\_5 \*/ |
| #define | [I2C0\_SDA\_PIO0\_5](#a7a30f5f10c3c59925e18d0526fa94431)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(5, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 1) /\* PIO0\_5 \*/ |
| #define | [R\_3\_PIO0\_5](#a372339383fc7d4d6e70965b744c10e48)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(5, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 2) /\* PIO0\_5 \*/ |
| #define | [PIO0\_6\_PIO0\_6](#a50ab17a232562ebc41deb8238de35f20)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_6 \*/ |
| #define | [R\_PIO0\_6](#a0d784ee93461dd2f05beeb7c9cfa46b7)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_6 \*/ |
| #define | [SSP0\_SCK\_PIO0\_6](#a632c9844b7638e69f8846b845dce32f7)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_6 \*/ |
| #define | [R\_4\_PIO0\_6](#a49f11eb792f5b0a7ecf80aeaa82291e2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_6 \*/ |
| #define | [PIO0\_7\_PIO0\_7](#a95b8cc1a76a6097556568f4554bf4e3f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_7 \*/ |
| #define | [U0\_CTS\_PIO0\_7](#aad418e1711b045ea50806d464c92fbcf)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_7 \*/ |
| #define | [R\_5\_PIO0\_7](#aea308935da9604f8bdfea4d58959e518)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_7 \*/ |
| #define | [I2C1\_SCL\_PIO0\_7](#a747ec67e7cb403d747b9f57429b71983)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_7 \*/ |
| #define | [PIO0\_8\_PIO0\_8](#a9e4b255125ef44e2de5c77743b4010ee)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_8 \*/ |
| #define | [SSP0\_MISO\_PIO0\_8](#a1d448d4e7bfeed79bc6e3fb14947afa7)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_8 \*/ |
| #define | [CT16B0\_MAT0\_PIO0\_8](#ad3f05ac410ca8c36aa81a57b635c1bb5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_8 \*/ |
| #define | [R\_6\_PIO0\_8](#a8feac8b8845786a001a5dedbd2c749cd)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_8 \*/ |
| #define | [PIO0\_9\_PIO0\_9](#a0db63ca26d440f3bc24a48d39fbfcc4b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_9 \*/ |
| #define | [SSP0\_MOSI\_PIO0\_9](#af1a1f4c533ae4806d692aff574334ebf)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_9 \*/ |
| #define | [CT16B0\_MAT1\_PIO0\_9](#a8f50532277b4b0b30b926e1f67a31cf1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_9 \*/ |
| #define | [R\_7\_PIO0\_9](#add1b38cd0b4e6b4557b5feeb39df424e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_9 \*/ |
| #define | [SWCLK\_PIO0\_10](#a9694c0dc682d5d6be38b963226aaef3c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_10 \*/ |
| #define | [PIO0\_10\_PIO0\_10](#a0b09489a89b80784605cddcc430914d6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_10 \*/ |
| #define | [SSP0\_SCK\_PIO0\_10](#ad68005dc04bde783a05f6c47da6dc4ef)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_10 \*/ |
| #define | [CT16B0\_MAT2\_PIO0\_10](#adca5657fc469b0f579f7a42f94ca5261)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_10 \*/ |
| #define | [TDI\_PIO0\_11](#afbfb770c4372aadbdb6f5c18d399e17e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_11 \*/ |
| #define | [PIO0\_11\_PIO0\_11](#a157b55ccf1883066cc9217629366b809)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_11 \*/ |
| #define | [ADC\_9\_PIO0\_11](#abfeca937f748f0b54ee4178c072ed1f5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_11 \*/ |
| #define | [CT32B0\_MAT3\_PIO0\_11](#a005db7665d634e68c56b59a3cb5b456d)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_11 \*/ |
| #define | [U1\_RTS\_PIO0\_11](#aaa87da84c9da4433539b55b513ab932b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_11 \*/ |
| #define | [U1\_SCLK\_PIO0\_11](#a3c5e8df87f093df6858f6ceb7e33e5ec)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 5) /\* PIO0\_11 \*/ |
| #define | [TMS\_PIO0\_12](#a8e608b93b683519cda35d166e08ab587)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_12 \*/ |
| #define | [PIO0\_12\_PIO0\_12](#ab4b3327e260eccbcccf80f0c1904ac56)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_12 \*/ |
| #define | [ADC\_8\_PIO0\_12](#ae9f30a9545a11701304231e5efb707a5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_12 \*/ |
| #define | [CT32B1\_CAP0\_PIO0\_12](#a7b28030377332811f795cd1462bf631f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_12 \*/ |
| #define | [U1\_CTS\_PIO0\_12](#ac58b55301756d90dcbfac6264df577b2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_12 \*/ |
| #define | [PIO0\_12\_PIO0\_12](#a51f64447bf880601691ffe859d0f1964)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 5) /\* PIO0\_12 \*/ |
| #define | [TDO\_PIO0\_13](#ace1983c57935ab76096a42fa0d9af286)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_13 \*/ |
| #define | [PIO0\_13\_PIO0\_13](#af1f156f6bca42a308c3d154ce6033f5a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_13 \*/ |
| #define | [ADC\_7\_PIO0\_13](#a706b80599c77ce5212b2359187d3fab1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_13 \*/ |
| #define | [CT32B1\_MAT0\_PIO0\_13](#af55d0700864a68532d8b253344160ebf)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_13 \*/ |
| #define | [U1\_RXD\_PIO0\_13](#a3eb45ad4dd10da96ed90153ef3b53665)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_13 \*/ |
| #define | [PIO0\_13\_PIO0\_13](#a8d40f087b829a11db51c16ab2181995c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 5) /\* PIO0\_13 \*/ |
| #define | [TRST\_PIO0\_14](#ad8c652abc5c8558f9312bd0ea201d7fc)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_14 \*/ |
| #define | [PIO0\_14\_PIO0\_14](#a692e4e1765be1cbca9897691a6bfbc39)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_14 \*/ |
| #define | [ADC\_6\_PIO0\_14](#ae6c3bb89b08367707e91bb00d3f55da5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_14 \*/ |
| #define | [CT32B1\_MAT1\_PIO0\_14](#acc4bcbd80fa3306bfa4ab8a4d3023c34)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_14 \*/ |
| #define | [U1\_TXD\_PIO0\_14](#a567bb0593686aa6552e868caeb623532)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_14 \*/ |
| #define | [SWDIO\_PIO0\_15](#a0b65345797054d59564518f73eee1602)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_15 \*/ |
| #define | [PIO0\_15\_PIO0\_15](#a59a92f1c63f7eb548a19f555cfe0208e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_15 \*/ |
| #define | [ADC\_3\_PIO0\_15](#af92fd1b534c099ad808403a199cad8a0)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_15 \*/ |
| #define | [CT32B1\_MAT2\_PIO0\_15](#ac5ed12914616e50cac147b251291d3f6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_15 \*/ |
| #define | [WAKEUP\_PIO0\_16](#a285bf9c6e5c1b7bfc8ada6ececbe466e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_16 \*/ |
| #define | [PIO0\_16\_PIO0\_16](#aa4a10249e5ee8e04ce01f62864476727)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_16 \*/ |
| #define | [ADC\_2\_PIO0\_16](#a21eeb0732f5d35d747f63db3eac9cfad)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_16 \*/ |
| #define | [CT32B1\_MAT3\_PIO0\_16](#a26ecf5bab459bde9bbb64ff5a019b09a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_16 \*/ |
| #define | [R\_8\_PIO0\_16](#a58df208f71b6efffed28bbabddf45f41)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_16 \*/ |
| #define | [PIO0\_17\_PIO0\_17](#a34451e215c47228b8337d0aed0c2c929)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_17 \*/ |
| #define | [U0\_RTS\_PIO0\_17](#ad946bbd06292183b7bdcd8db7d93d980)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_17 \*/ |
| #define | [CT32B0\_CAP0\_PIO0\_17](#afa844a06c34eb41b114b49aac65d5eb1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_17 \*/ |
| #define | [U0\_SCLK\_PIO0\_17](#a5f911210bf444c31df578680aa92ba9e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_17 \*/ |
| #define | [PIO0\_18\_PIO0\_18](#a87d216855b3f78407343517d639cd75c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(18, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_18 \*/ |
| #define | [U0\_RXD\_PIO0\_18](#a22d6493688b04414c7dc732d43f4c0f2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(18, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_18 \*/ |
| #define | [CT32B0\_MAT0\_PIO0\_18](#a099d0dca10dd8ac2762ac340473a798b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(18, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_18 \*/ |
| #define | [PIO0\_19\_PIO0\_19](#a83757ba41e5c8ff4a04384a6f59550e1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(19, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_19 \*/ |
| #define | [U0\_TXD\_PIO0\_19](#a602172b5fe5dde4f7064ea152914e3b4)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(19, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_19 \*/ |
| #define | [CT32B0\_MAT1\_PIO0\_19](#a579df8a29d7f50a93ae328c1aec9385a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(19, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_19 \*/ |
| #define | [PIO0\_20\_PIO0\_20](#a28a9784674717e3617070ed87923a1f1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(20, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_20 \*/ |
| #define | [CT16B1\_CAP0\_PIO0\_20](#aa7942f15263a5a5c36bd4513da5223c2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(20, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_20 \*/ |
| #define | [U2\_RXD\_PIO0\_20](#a9fc4de327d564720e61a338e4a5d3b5b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(20, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_20 \*/ |
| #define | [PIO0\_21\_PIO0\_21](#abfb5b6fa233853dc18ed899fa4418b1b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(21, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_21 \*/ |
| #define | [CT16B1\_MAT0\_PIO0\_21](#a91549c703ace01d5e5cd3f5477ec156e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(21, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_21 \*/ |
| #define | [SSP1\_MOSI\_PIO0\_21](#aaec77c9670e3e88d00641020ec0d47d6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(21, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_21 \*/ |
| #define | [PIO0\_22\_PIO0\_22](#a9df3dda1a040239ee21e73c813659ccd)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_22 \*/ |
| #define | [ADC\_11\_PIO0\_22](#aafede8fcd15e8bfe236e95c9a7b49b96)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_22 \*/ |
| #define | [CT16B1\_CAP1\_PIO0\_22](#a2630aa1a98d13baf6f04f78f005bf704)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_22 \*/ |
| #define | [SSP1\_MISO\_PIO0\_22](#a783a183d806cac03c7db41096bae4272)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_22 \*/ |
| #define | [PIO0\_23\_PIO0\_23](#a07878c04e96b6472f26d3760a42ac212)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_23 \*/ |
| #define | [ADC\_1\_PIO0\_23](#ab00e7a1a150e2e1c9b45d86c850a4a0b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_23 \*/ |
| #define | [R\_9\_PIO0\_23](#ab0d0d78534d6cc1d4cee77b3eee84114)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_23 \*/ |
| #define | [U0\_RI\_PIO0\_23](#a1b2efba93021237e6fd7e3e276fef4e5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_23 \*/ |
| #define | [SSP1\_SSEL\_PIO0\_23](#a0a3ad1a37c02adc62dbae966523e6d4c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_23 \*/ |
| #define | [PIO1\_0\_PIO1\_0](#ac68053b619744fbf1c1f17f7b08cf580)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_0 \*/ |
| #define | [CT32B1\_MAT0\_PIO1\_0](#a5ee6340e6fe3b732b6d49bbef6c90155)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_0 \*/ |
| #define | [R\_10\_PIO1\_0](#a1ac3960333408442de9bd74e694595de)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_0 \*/ |
| #define | [U2\_TXD\_PIO1\_0](#a4319b4d5227cd2a7ff75de78a422a870)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_0 \*/ |
| #define | [PIO1\_1\_PIO1\_1](#a299fee16f12cef2f585e132548ba3b72)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_1 \*/ |
| #define | [CT32B1\_MAT1\_PIO1\_1](#afb61298e6db2c507f6090a86566edc91)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_1 \*/ |
| #define | [R\_11\_PIO1\_1](#aaae95bceef30b054294e7a7eed2d68a4)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_1 \*/ |
| #define | [U0\_DTR\_PIO1\_1](#a7a17c6326f865f7eee09ec236ce12216)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_1 \*/ |
| #define | [PIO1\_2\_PIO1\_2](#a5265479414c8dd9845e6aa5213eda99e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_2 \*/ |
| #define | [CT32B1\_MAT2\_PIO1\_2](#ab158e092af2c6ad056cc6f4d298c1951)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_2 \*/ |
| #define | [R\_12\_PIO1\_2](#ac7bd9d42184bd9175925b2e789d4e0f8)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_2 \*/ |
| #define | [U1\_RXD\_PIO1\_2](#a4af77ea4a454643946504e10d249edcc)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_2 \*/ |
| #define | [PIO1\_3\_PIO1\_3](#a2d403da5360929eed6c833567c415fe5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_3 \*/ |
| #define | [CT32B1\_MAT3\_PIO1\_3](#a7edf5d0d95f5fa253b03ccc77447ed9a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_3 \*/ |
| #define | [R\_13\_PIO1\_3](#a1f35a5b9268e09e3ff279d0d7b27e8d9)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_3 \*/ |
| #define | [I2C1\_SDA\_PIO1\_3](#ae63879080611307c152e569946e7a7ae)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_3 \*/ |
| #define | [ADC\_5\_PIO1\_3](#ac4f0bd23dfc3f744220cadb6949d4e1f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO1\_3 \*/ |
| #define | [PIO1\_4\_PIO1\_4](#aecf77d09221ba70819899708b4ad74a8)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_4 \*/ |
| #define | [CT32B1\_CAP0\_PIO1\_4](#a54bfd60ff58b0148b6848f8b2982442e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_4 \*/ |
| #define | [R\_14\_PIO1\_4](#aaba8b00d104b3163f0c7cee32b91cf1e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_4 \*/ |
| #define | [U0\_DSR\_PIO1\_4](#a0a7cdf5fa1cae307725c7cf8742cc599)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_4 \*/ |
| #define | [PIO1\_5\_PIO1\_5](#ab070530de6c3105054206c5a526f5730)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_5 \*/ |
| #define | [CT32B1\_CAP1\_PIO1\_5](#a1ab5d0cd48d5ade99b0a6e4fc8bc9f68)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_5 \*/ |
| #define | [R\_15\_PIO1\_5](#adcccebfaed3f6f65e12a4052ff04fdcd)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_5 \*/ |
| #define | [U0\_DCD\_PIO1\_5](#a0abbdcaf023079f9181f260779ced50e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_5 \*/ |
| #define | [PIO1\_6\_PIO1\_6](#af6b1804a5aefa54e7a3c4dba33394805)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_6 \*/ |
| #define | [R\_16\_PIO1\_6](#a9f77fd7bcd00d7bc4e179cb3c3db622e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_6 \*/ |
| #define | [U2\_RXD\_PIO1\_6](#a48ac3c0096037bbe64d92b2d2b0e621f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_6 \*/ |
| #define | [CT32B0\_CAP1\_PIO1\_6](#a01c2a127b550f1c904cf747a2351c006)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_6 \*/ |
| #define | [PIO1\_7\_PIO1\_7](#ab77050cd6c5323ede0c6ce3f52f4f83e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_7 \*/ |
| #define | [R\_17\_PIO1\_7](#a2478b21ed3999f9fb27e1ddcc555383f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_7 \*/ |
| #define | [U2\_CTS\_PIO1\_7](#a23bb3cc2ede010588651fede510df3db)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_7 \*/ |
| #define | [CT16B1\_CAP0\_PIO1\_7](#a6673a36d9b33d563295063f73c466b58)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_7 \*/ |
| #define | [PIO1\_8\_PIO1\_8](#a5eb361e081a52918777d89f61c0a26fa)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_8 \*/ |
| #define | [R\_18\_PIO1\_8](#a01a390f0311638bc09569b06839fb7dd)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_8 \*/ |
| #define | [U1\_TXD\_PIO1\_8](#a253fad10b49809895c3f27ec3e51a567)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_8 \*/ |
| #define | [CT16B0\_CAP0\_PIO1\_8](#a598b61d037bfcacc335bf0996a477843)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_8 \*/ |
| #define | [PIO1\_9\_PIO1\_9](#a75ab800970f73ac0177aaf8139ba8739)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_9 \*/ |
| #define | [U0\_CTS\_PIO1\_9](#a5ec91d14ec34a2080c1d857e1fd6f572)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_9 \*/ |
| #define | [CT16B1\_MAT1\_PIO1\_9](#a9db77081025e9907d1d90cf993d8a028)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_9 \*/ |
| #define | [ADC\_0\_PIO1\_9](#a03ce0c70811dc7195ee48649532f2ebd)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_9 \*/ |
| #define | [PIO1\_10\_PIO1\_10](#a037f6a357a5bbea0dc0cb9902c94c846)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_10 \*/ |
| #define | [U2\_RTS\_PIO1\_10](#a2f2957c1a43d63106ce2d61678103f62)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_10 \*/ |
| #define | [U2\_SCLK\_PIO1\_10](#ac7236d26fd68c0be4b0f80e7ac6614cd)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_10 \*/ |
| #define | [CT16B1\_MAT0\_PIO1\_10](#abd7606b5f7f902397d6c2ab8fedfd2b3)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_10 \*/ |
| #define | [PIO1\_11\_PIO1\_11](#a97b3bfd02acef68ffc82952e49bd03fe)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_11 \*/ |
| #define | [I2C1\_SCL\_PIO1\_11](#abd5321e5d55560fb0927e8a26027d001)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_11 \*/ |
| #define | [CT16B0\_MAT2\_PIO1\_11](#ad0ae914ba48296f972618dee04cc6490)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_11 \*/ |
| #define | [U0\_RI\_PIO1\_11](#aa43f68879f82d124e3d1da1b1a4bee16)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_11 \*/ |
| #define | [PIO1\_12\_PIO1\_12](#a896bd464fd196266a8862fde369e899b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_12 \*/ |
| #define | [SSP0\_MOSI\_PIO1\_12](#a0bc3c1d34d0bc7a92543edd4e743905f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_12 \*/ |
| #define | [CT16B0\_MAT1\_PIO1\_12](#a5b8fcd82c3feca9ed3dfbd2f905b4a74)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_12 \*/ |
| #define | [R\_21\_PIO1\_12](#abe8e17586c29617e61a2671408e84637)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_12 \*/ |
| #define | [PIO1\_13\_PIO1\_13](#ad2d3d8b8bb3a17fab2dc03850b9934e6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_13 \*/ |
| #define | [U1\_CTS\_PIO1\_13](#ad00e6299050aceda961b3b6af7a78f79)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_13 \*/ |
| #define | [SCT0\_OUT3\_PIO1\_13](#a504a57a6c6e3014ed4df4320736c7713)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_13 \*/ |
| #define | [R\_22\_PIO1\_13](#a8613dd791e9ddf76c84d12c9f25f31ed)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_13 \*/ |
| #define | [PIO1\_14\_PIO1\_14](#aec627d88659627216048116352084463)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_14 \*/ |
| #define | [I2C1\_SDA\_PIO1\_14](#aa478831aabf3f70f44dc83be779f29df)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_14 \*/ |
| #define | [CT32B1\_MAT2\_PIO1\_14](#a7e9fefa7d3b24bcf91c2af8143934e1b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_14 \*/ |
| #define | [R\_23\_PIO1\_14](#a75b2a3bdcdc904bce2ed4641fd77d36f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_14 \*/ |
| #define | [PIO1\_15\_PIO1\_15](#ad430442be04fb9768354a29392aa3150)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_15 \*/ |
| #define | [SSP0\_SSEL\_PIO1\_15](#acc0fec039c618cf46e788bfb6f651cfe)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_15 \*/ |
| #define | [CT32B1\_MAT3\_PIO1\_15](#af960ef8b39ccd08fbe57d0fb2808507a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_15 \*/ |
| #define | [R\_24\_PIO1\_15](#a31607e58141be4451603b21142dc2b78)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_15 \*/ |
| #define | [PIO1\_16\_PIO1\_16](#a890647261f0d13600177b8da109e7f80)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_16 \*/ |
| #define | [SSP0\_MISO\_PIO1\_16](#adb527bbcf8d059c9bfccdf29f3ac4aa5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_16 \*/ |
| #define | [CT16B0\_MAT0\_PIO1\_16](#acead3031fd80d06b2f87cf0ad8e9e8e2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_16 \*/ |
| #define | [R\_25\_PIO1\_16](#afbf96bb8cc6cf2f8f56ac0f48de55a9d)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_16 \*/ |
| #define | [PIO1\_17\_PIO1\_17](#ab7c4014e4c5aff2215d00bfbfcdca7c6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_17 \*/ |
| #define | [CT16B0\_CAP2\_PIO1\_17](#a27237240e4f0c84be58ac4a40915b30b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_17 \*/ |
| #define | [U0\_RXD\_PIO1\_17](#a974de383ed91f1e80b6e67ab95f627d3)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_17 \*/ |
| #define | [R\_26\_PIO1\_17](#a485ea3b9fe56406e22a835ad8101ca2a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_17 \*/ |
| #define | [PIO1\_18\_PIO1\_18](#abd5742cad3a656c0cca0a02ec6b41acf)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_18 \*/ |
| #define | [CT16B1\_CAP1\_PIO1\_18](#af2925353ca8342deac5cc6c47623b40c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_18 \*/ |
| #define | [U0\_TXD\_PIO1\_18](#a15cb6f2cf2ca2ba9b04b54b490e2c88b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_18 \*/ |
| #define | [R\_27\_PIO1\_18](#a7a373b17b448fdd55c2b0b4e88750d38)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_18 \*/ |
| #define | [PIO1\_19\_PIO1\_19](#ae56e1309f5dfaff815c892ef0e1ed2b9)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_19 \*/ |
| #define | [U2\_CTS\_PIO1\_19](#a14b9435d73cf7890108f3f7e929154e7)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_19 \*/ |
| #define | [SCT0\_OUT0\_PIO1\_19](#ac19819cd774abe2a0597247136804d2e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_19 \*/ |
| #define | [R\_28\_PIO1\_19](#a1a87c8b465b4539dee7d82dcf0067d5b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_19 \*/ |
| #define | [PIO1\_20\_PIO1\_20](#adea5f43202f54b478043589ea1d4b1e1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_20 \*/ |
| #define | [U0\_DSR\_PIO1\_20](#a3ed819b62c0253666670f98230fb6194)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_20 \*/ |
| #define | [SSP1\_SCK\_PIO1\_20](#af998519da9f4ffd89b606b0261f95a1e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_20 \*/ |
| #define | [CT16B0\_MAT0\_PIO1\_20](#a55e45a077e426ae5e06508b66d899c4c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_20 \*/ |
| #define | [PIO1\_21\_PIO1\_21](#a0c6805b1f84117dee5e66f091818d9ca)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_21 \*/ |
| #define | [U0\_DCD\_PIO1\_21](#aaf239310ed5db40a24ca15cc7f48ed2b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_21 \*/ |
| #define | [SSP1\_MISO\_PIO1\_21](#af44b09e3f6bf4ac86fae8f257a0620c6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_21 \*/ |
| #define | [CT16B0\_CAP1\_PIO1\_21](#a1ef21fd46fa25d46c8eb7b8881f4b08c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_21 \*/ |
| #define | [PIO1\_22\_PIO1\_22](#a689cbb1bd742d803a7d512f5be6c4cfb)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_22 \*/ |
| #define | [SSP1\_MOSI\_PIO1\_22](#aa39927fc00dacde807c16c4044fa62b5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_22 \*/ |
| #define | [CT32B1\_CAP1\_PIO1\_22](#a39a31d62e31f796e3a54f43056577675)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_22 \*/ |
| #define | [ADC\_4\_PIO1\_22](#a9686cbbd0389bec5c771f2776f05cde7)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_22 \*/ |
| #define | [R\_29\_PIO1\_22](#adfbe0b94e760582fccaa92f88f41d1f4)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO1\_22 \*/ |
| #define | [PIO1\_23\_PIO1\_23](#ab15b87098dc679562fcd0eb74aa8c761)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_23 \*/ |
| #define | [CT16B1\_MAT1\_PIO1\_23](#aa168a44ff47701e1e090bc95de4b4601)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_23 \*/ |
| #define | [SSP1\_SSEL\_PIO1\_23](#a241d8f9f8546f68c66e490a4f42951ca)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_23 \*/ |
| #define | [U2\_TXD\_PIO1\_23](#adbafcde4cb5f052835ed790774e91a67)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_23 \*/ |
| #define | [PIO1\_24\_PIO1\_24](#a86877f01c21462c697dcdf1163ef2057)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(48, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_24 \*/ |
| #define | [CT32B0\_MAT0\_PIO1\_24](#aa5758ecd3938aa9210fad9e6a291fb54)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(48, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_24 \*/ |
| #define | [I2C1\_SDA\_PIO1\_24](#ae7f01370d20cb64565a5e0d17190f11c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(48, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_24 \*/ |
| #define | [PIO1\_25\_PIO1\_25](#ad1f94b842d9d03ecfd95521ad4fc50ef)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_25 \*/ |
| #define | [U2\_RTS\_PIO1\_25](#afc6ec4baef4bad621e4d62ae945a1163)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_25 \*/ |
| #define | [U2\_SCLK\_PIO1\_25](#a784ceb0c6b7772018f082fcd508cba4f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_25 \*/ |
| #define | [SCT0\_IN0\_PIO1\_25](#add2cbf06dc14447e4661ce8a3de45f2f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_25 \*/ |
| #define | [R\_30\_PIO1\_25](#a387b44f72acc4eb20b382da8f076d195)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 4) /\* PIO1\_25 \*/ |
| #define | [PIO1\_26\_PIO1\_26](#a6b8c76bf4eb6a9e621363bbd7862a3c5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_26 \*/ |
| #define | [CT32B0\_MAT2\_PIO1\_26](#a1733e97cfa0bb66c7717450596b0cfea)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_26 \*/ |
| #define | [U0\_RXD\_PIO1\_26](#a3cc2c9440f957296aa32d4636b2d6130)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_26 \*/ |
| #define | [R\_19\_PIO1\_26](#ab0411bc0f8b6654e0f7bb8259cb47e7e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_26 \*/ |
| #define | [PIO1\_27\_PIO1\_27](#ac22ea9cd9fdb0dcf4125628fd41ad4e2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_27 \*/ |
| #define | [CT32B0\_MAT3\_PIO1\_27](#ac2a89c71d21325e0e64cd8a3d8c4ebdc)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_27 \*/ |
| #define | [U0\_TXD\_PIO1\_27](#aef4522554340d95f52f21f6896d121c6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_27 \*/ |
| #define | [R\_20\_PIO1\_27](#a629bba740c1f829a7401dbe6972b155e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_27 \*/ |
| #define | [SSP1\_SCK\_PIO1\_27](#adc98f945f54727aa26fb4bb5acccb1b2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 4) /\* PIO1\_27 \*/ |
| #define | [PIO1\_28\_PIO1\_28](#ae45e38efb89456519fd29191d1bfd41e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_28 \*/ |
| #define | [CT32B0\_CAP0\_PIO1\_28](#acbc5db1dfeb27c0e9e9c37760876aa7f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_28 \*/ |
| #define | [U0\_SCLK\_PIO1\_28](#a2eb7dfc050a7afad6630db88a430ffa4)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_28 \*/ |
| #define | [U0\_RTS\_PIO1\_28](#a030246ec2f49c51f0ea088ed565d0f6d)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_28 \*/ |
| #define | [PIO1\_29\_PIO1\_29](#a07775fe074a265e8594cc0f1bc3c4553)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_29 \*/ |
| #define | [SSP0\_SCK\_PIO1\_29](#afa406dcc3b4ce8853b38782aaee8b34c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_29 \*/ |
| #define | [CT32B0\_CAP1\_PIO1\_29](#a8c9a3e151294c9fab0c8ef47d0f0e4fe)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_29 \*/ |
| #define | [U0\_DTRn\_PIO1\_29](#affc255b3a5b093927b05ec78056090fa)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_29 \*/ |
| #define | [ADC\_10\_PIO1\_29](#a15dfb4021a3db0723c8918d89840f569)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO1\_29 \*/ |
| #define | [PIO1\_30\_PIO1\_30](#a0452698f8cda9677cc606f6e8386f0c5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_30 \*/ |
| #define | [I2C1\_SCL\_PIO1\_30](#a8edcf1fdf2dd40db40fc0e3bb226c868)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_30 \*/ |
| #define | [SCT0\_IN3\_PIO1\_30](#a92bceca4249eed78de2037929325bc58)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_30 \*/ |
| #define | [R\_31\_PIO1\_30](#a85192c0b77e70e515a9165852d221208)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_30 \*/ |
| #define | [PIO1\_31\_PIO1\_31](#ae459ff2b755df0e5a22378e59fb1ccbc)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(55, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_31 \*/ |
| #define | [PIO2\_0\_PIO2\_0](#a5fafd0c519a03d1f678c7f1c6c3b34ed)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(60, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO2\_0 \*/ |
| #define | [XTALIN\_PIO2\_0](#a5f3bfb1721c59d5800bcdf187dbddeb1)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(60, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO2\_0 \*/ |
| #define | [PIO2\_1\_PIO2\_1](#ab18db336e17b21d3e1864f47fbfe211b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(61, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO2\_1 \*/ |
| #define | [XTALOUT\_PIO2\_1](#a8c1b112e94052158ccefdda7c023d9e0)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(61, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO2\_1 \*/ |
| #define | [PIO2\_2\_PIO2\_2](#a5ee88fb076ffc8f05c54ffa403976fa4)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_2 \*/ |
| #define | [U3\_RTS\_PIO2\_2](#aa079f73f9150780aabd8e2cc2325c465)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_2 \*/ |
| #define | [U3\_SCLK\_PIO2\_2](#ab257d298276dc7d42c7c4ccfbde4b2fe)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_2 \*/ |
| #define | [SCT0\_OUT1\_PIO2\_2](#adf678074b20d6e433bd2d9e9fb13681e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO2\_2 \*/ |
| #define | [PIO2\_3\_PIO2\_3](#ab76b9f2a58719e0cbd557e5b3019861d)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(64, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_3 \*/ |
| #define | [U3\_RXD\_PIO2\_3](#a330a0f6bb26f2a8d1881433d42251d88)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(64, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_3 \*/ |
| #define | [CT32B0\_MAT1\_PIO2\_3](#a54da6ec8f7f08351101969ebdbc6d7f9)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(64, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_3 \*/ |
| #define | [PIO2\_4\_PIO2\_4](#aec83c87cf4c5c7a6cd72370978c5f3ab)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(65, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_4 \*/ |
| #define | [U3\_TXD\_PIO2\_4](#a69efa41cce2c5e868b790df9bb2f2fe5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(65, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_4 \*/ |
| #define | [CT32B0\_MAT2\_PIO2\_4](#a42c6c88c505fdd8101ff9abaa61c7896)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(65, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_4 \*/ |
| #define | [PIO2\_5\_PIO2\_5](#abd48058e2c15f74525c6354cf245db73)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(66, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_5 \*/ |
| #define | [U3\_CTS\_PIO2\_5](#a478a19515c027a5282b061de7a201317)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(66, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_5 \*/ |
| #define | [SCT0\_IN1\_PIO2\_5](#a73d3caf803f8a4df930c63cf4fe3f37c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(66, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_5 \*/ |
| #define | [PIO2\_6\_PIO2\_6](#a180b0de4ca0603c2e171c869a52f7580)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_6 \*/ |
| #define | [U1\_RTS\_PIO2\_6](#ab9a1ba400672c6486a0f8647164a1397)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_6 \*/ |
| #define | [U1\_SCLK\_PIO2\_6](#a3885a451ceef59f37c8cb470aa3c23d0)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_6 \*/ |
| #define | [SCT0\_IN2\_PIO2\_6](#ae14001bfffc9a00d61caf9647a3527f0)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO2\_6 \*/ |
| #define | [PIO2\_7\_PIO2\_7](#a7e1cd4171f323202a5b67bb1e9363732)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(68, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_7 \*/ |
| #define | [SSP0\_SCK\_PIO2\_7](#a6f00dd7928fb37ed72b08f0ce57ee03c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(68, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_7 \*/ |
| #define | [SCT0\_OUT2\_PIO2\_7](#a41199c507951e02ae2aad6b1b94a2aa5)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(68, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_7 \*/ |
| #define | [PIO2\_8\_PIO2\_8](#aa423ccac69367faeaee101c4ca4d411a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(69, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_8 \*/ |
| #define | [SCT1\_IN0\_PIO2\_8](#af4e4c1f8972faff68d459b159c385dd2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(69, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_8 \*/ |
| #define | [PIO2\_9\_PIO2\_9](#aa849da24aea3e3d29c43cc8f7264b434)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(70, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_9 \*/ |
| #define | [SCT1\_IN1\_PIO2\_9](#afd99a1f94ac011c63fbb8a9a9db511da)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(70, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_9 \*/ |
| #define | [PIO2\_10\_PIO2\_10](#a2471788decdf2d9119ca1245ddc77981)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(71, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_10 \*/ |
| #define | [U4\_RTS\_PIO2\_10](#a531b7e88f7193b4ce754081685e6d23f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(71, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_10 \*/ |
| #define | [U4\_SCLK\_PIO2\_10](#a34a74c9cc41c9839ee54dccf1aaa9ad7)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(71, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_10 \*/ |
| #define | [PIO2\_11\_PIO2\_11](#a25f558f2d23c6a973da481216a331047)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(72, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_11 \*/ |
| #define | [U4\_RXD\_PIO2\_11](#aaabe5ad6b984f52723df7c958e043cd2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(72, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_11 \*/ |
| #define | [PIO2\_12\_PIO2\_12](#a55b8398b79ab94885c5b1a266cc96b67)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(73, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_12 \*/ |
| #define | [U4\_TXD\_PIO2\_12](#aa676078e9cc9a7dbb114e9e39bbdee07)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(73, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_12 \*/ |
| #define | [PIO2\_13\_PIO2\_13](#aad0ffb60a10d384eec0c88137e9f5049)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(74, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_13 \*/ |
| #define | [U4\_CTS\_PIO2\_13](#a2481a40bdab053f1d25e6fd4daeb90cc)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(74, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_13 \*/ |
| #define | [PIO2\_14\_PIO2\_14](#a4d600902f1f7cfa6d6d7a15dad9fa47e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(75, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_14 \*/ |
| #define | [SCT1\_IN2\_PIO2\_14](#a372dcaa75ccd7aea049ae958f41e9332)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(75, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_14 \*/ |
| #define | [PIO2\_15\_PIO2\_15](#a4247567257584b93a079dde0636a8d82)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(76, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_15 \*/ |
| #define | [SCT1\_IN3\_PIO2\_15](#ad4ea56df396ac4cab517d5bd7b735f5c)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(76, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_15 \*/ |
| #define | [PIO2\_16\_PIO2\_16](#a68ae2af37b444a788e82cbdd59a9518e)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(77, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_16 \*/ |
| #define | [SCT1\_OUT0\_PIO2\_16](#affe7ba3bec6cfd4b2bba3533ea8cbd66)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(77, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_16 \*/ |
| #define | [PIO2\_17\_PIO2\_17](#aafd4249d51198bee34d7f03275b70bc6)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(78, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_17 \*/ |
| #define | [SCT1\_OUT1\_PIO2\_17](#a2e3304361cf9766f08c764fac50ef9bc)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(78, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_17 \*/ |
| #define | [PIO2\_18\_PIO2\_18](#ab01949c5d3a85a0acb2266d7c4e71b8a)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(79, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_18 \*/ |
| #define | [SCT1\_OUT2\_PIO2\_18](#af2c8a7e95a4a2f63e1f86ed9aa83a76f)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(79, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_18 \*/ |
| #define | [PIO2\_19\_PIO2\_19](#a10046d3d553609d2e46568d31bcbd22b)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(80, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_19 \*/ |
| #define | [SCT1\_OUT3\_PIO2\_19](#a89409cbd5a036dd7ff5c5a868eef4521)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(80, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_19 \*/ |
| #define | [PIO2\_20\_PIO2\_20](#a379470de275ec9e879c6a7da55dc81e2)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(81, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_20 \*/ |
| #define | [PIO2\_21\_PIO2\_21](#a8cc6a3d1353183ec7277fbb88a405961)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(82, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_21 \*/ |
| #define | [PIO2\_22\_PIO2\_22](#a12640000bfec871e24fff6deaa5cdd08)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(83, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_22 \*/ |
| #define | [PIO2\_23\_PIO2\_23](#ab78b84af5278ada6d4c31bbc85928899)   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(84, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_23 \*/ |

## Macro Definition Documentation

## [◆ ](#a03ce0c70811dc7195ee48649532f2ebd)ADC\_0\_PIO1\_9

| #define ADC\_0\_PIO1\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_9 \*/ |
| --- |

## [◆ ](#a15dfb4021a3db0723c8918d89840f569)ADC\_10\_PIO1\_29

| #define ADC\_10\_PIO1\_29   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO1\_29 \*/ |
| --- |

## [◆ ](#aafede8fcd15e8bfe236e95c9a7b49b96)ADC\_11\_PIO0\_22

| #define ADC\_11\_PIO0\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_22 \*/ |
| --- |

## [◆ ](#ab00e7a1a150e2e1c9b45d86c850a4a0b)ADC\_1\_PIO0\_23

| #define ADC\_1\_PIO0\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_23 \*/ |
| --- |

## [◆ ](#a21eeb0732f5d35d747f63db3eac9cfad)ADC\_2\_PIO0\_16

| #define ADC\_2\_PIO0\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_16 \*/ |
| --- |

## [◆ ](#af92fd1b534c099ad808403a199cad8a0)ADC\_3\_PIO0\_15

| #define ADC\_3\_PIO0\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_15 \*/ |
| --- |

## [◆ ](#a9686cbbd0389bec5c771f2776f05cde7)ADC\_4\_PIO1\_22

| #define ADC\_4\_PIO1\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_22 \*/ |
| --- |

## [◆ ](#ac4f0bd23dfc3f744220cadb6949d4e1f)ADC\_5\_PIO1\_3

| #define ADC\_5\_PIO1\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO1\_3 \*/ |
| --- |

## [◆ ](#ae6c3bb89b08367707e91bb00d3f55da5)ADC\_6\_PIO0\_14

| #define ADC\_6\_PIO0\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_14 \*/ |
| --- |

## [◆ ](#a706b80599c77ce5212b2359187d3fab1)ADC\_7\_PIO0\_13

| #define ADC\_7\_PIO0\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_13 \*/ |
| --- |

## [◆ ](#ae9f30a9545a11701304231e5efb707a5)ADC\_8\_PIO0\_12

| #define ADC\_8\_PIO0\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_12 \*/ |
| --- |

## [◆ ](#abfeca937f748f0b54ee4178c072ed1f5)ADC\_9\_PIO0\_11

| #define ADC\_9\_PIO0\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_11 \*/ |
| --- |

## [◆ ](#a4d2452db92940671b276775adec24700)CLKOUT\_PIO0\_1

| #define CLKOUT\_PIO0\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_1 \*/ |
| --- |

## [◆ ](#a2c44ad39551919eaf469137d3d37f78b)CT16B0\_CAP0\_PIO0\_2

| #define CT16B0\_CAP0\_PIO0\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_2 \*/ |
| --- |

## [◆ ](#a598b61d037bfcacc335bf0996a477843)CT16B0\_CAP0\_PIO1\_8

| #define CT16B0\_CAP0\_PIO1\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_8 \*/ |
| --- |

## [◆ ](#a1ef21fd46fa25d46c8eb7b8881f4b08c)CT16B0\_CAP1\_PIO1\_21

| #define CT16B0\_CAP1\_PIO1\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_21 \*/ |
| --- |

## [◆ ](#a27237240e4f0c84be58ac4a40915b30b)CT16B0\_CAP2\_PIO1\_17

| #define CT16B0\_CAP2\_PIO1\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_17 \*/ |
| --- |

## [◆ ](#ad3f05ac410ca8c36aa81a57b635c1bb5)CT16B0\_MAT0\_PIO0\_8

| #define CT16B0\_MAT0\_PIO0\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_8 \*/ |
| --- |

## [◆ ](#acead3031fd80d06b2f87cf0ad8e9e8e2)CT16B0\_MAT0\_PIO1\_16

| #define CT16B0\_MAT0\_PIO1\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_16 \*/ |
| --- |

## [◆ ](#a55e45a077e426ae5e06508b66d899c4c)CT16B0\_MAT0\_PIO1\_20

| #define CT16B0\_MAT0\_PIO1\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_20 \*/ |
| --- |

## [◆ ](#a8f50532277b4b0b30b926e1f67a31cf1)CT16B0\_MAT1\_PIO0\_9

| #define CT16B0\_MAT1\_PIO0\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_9 \*/ |
| --- |

## [◆ ](#a5b8fcd82c3feca9ed3dfbd2f905b4a74)CT16B0\_MAT1\_PIO1\_12

| #define CT16B0\_MAT1\_PIO1\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_12 \*/ |
| --- |

## [◆ ](#adca5657fc469b0f579f7a42f94ca5261)CT16B0\_MAT2\_PIO0\_10

| #define CT16B0\_MAT2\_PIO0\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_10 \*/ |
| --- |

## [◆ ](#ad0ae914ba48296f972618dee04cc6490)CT16B0\_MAT2\_PIO1\_11

| #define CT16B0\_MAT2\_PIO1\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_11 \*/ |
| --- |

## [◆ ](#aa7942f15263a5a5c36bd4513da5223c2)CT16B1\_CAP0\_PIO0\_20

| #define CT16B1\_CAP0\_PIO0\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(20, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_20 \*/ |
| --- |

## [◆ ](#a6673a36d9b33d563295063f73c466b58)CT16B1\_CAP0\_PIO1\_7

| #define CT16B1\_CAP0\_PIO1\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_7 \*/ |
| --- |

## [◆ ](#a2630aa1a98d13baf6f04f78f005bf704)CT16B1\_CAP1\_PIO0\_22

| #define CT16B1\_CAP1\_PIO0\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_22 \*/ |
| --- |

## [◆ ](#af2925353ca8342deac5cc6c47623b40c)CT16B1\_CAP1\_PIO1\_18

| #define CT16B1\_CAP1\_PIO1\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_18 \*/ |
| --- |

## [◆ ](#a91549c703ace01d5e5cd3f5477ec156e)CT16B1\_MAT0\_PIO0\_21

| #define CT16B1\_MAT0\_PIO0\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(21, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_21 \*/ |
| --- |

## [◆ ](#abd7606b5f7f902397d6c2ab8fedfd2b3)CT16B1\_MAT0\_PIO1\_10

| #define CT16B1\_MAT0\_PIO1\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_10 \*/ |
| --- |

## [◆ ](#aa168a44ff47701e1e090bc95de4b4601)CT16B1\_MAT1\_PIO1\_23

| #define CT16B1\_MAT1\_PIO1\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_23 \*/ |
| --- |

## [◆ ](#a9db77081025e9907d1d90cf993d8a028)CT16B1\_MAT1\_PIO1\_9

| #define CT16B1\_MAT1\_PIO1\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_9 \*/ |
| --- |

## [◆ ](#afa844a06c34eb41b114b49aac65d5eb1)CT32B0\_CAP0\_PIO0\_17

| #define CT32B0\_CAP0\_PIO0\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_17 \*/ |
| --- |

## [◆ ](#acbc5db1dfeb27c0e9e9c37760876aa7f)CT32B0\_CAP0\_PIO1\_28

| #define CT32B0\_CAP0\_PIO1\_28   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_28 \*/ |
| --- |

## [◆ ](#a8c9a3e151294c9fab0c8ef47d0f0e4fe)CT32B0\_CAP1\_PIO1\_29

| #define CT32B0\_CAP1\_PIO1\_29   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_29 \*/ |
| --- |

## [◆ ](#a01c2a127b550f1c904cf747a2351c006)CT32B0\_CAP1\_PIO1\_6

| #define CT32B0\_CAP1\_PIO1\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_6 \*/ |
| --- |

## [◆ ](#a099d0dca10dd8ac2762ac340473a798b)CT32B0\_MAT0\_PIO0\_18

| #define CT32B0\_MAT0\_PIO0\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(18, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_18 \*/ |
| --- |

## [◆ ](#aa5758ecd3938aa9210fad9e6a291fb54)CT32B0\_MAT0\_PIO1\_24

| #define CT32B0\_MAT0\_PIO1\_24   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(48, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_24 \*/ |
| --- |

## [◆ ](#a579df8a29d7f50a93ae328c1aec9385a)CT32B0\_MAT1\_PIO0\_19

| #define CT32B0\_MAT1\_PIO0\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(19, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_19 \*/ |
| --- |

## [◆ ](#a54da6ec8f7f08351101969ebdbc6d7f9)CT32B0\_MAT1\_PIO2\_3

| #define CT32B0\_MAT1\_PIO2\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(64, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_3 \*/ |
| --- |

## [◆ ](#aa6fbfccc166375429d6c720684686a24)CT32B0\_MAT2\_PIO0\_1

| #define CT32B0\_MAT2\_PIO0\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_1 \*/ |
| --- |

## [◆ ](#a1733e97cfa0bb66c7717450596b0cfea)CT32B0\_MAT2\_PIO1\_26

| #define CT32B0\_MAT2\_PIO1\_26   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_26 \*/ |
| --- |

## [◆ ](#a42c6c88c505fdd8101ff9abaa61c7896)CT32B0\_MAT2\_PIO2\_4

| #define CT32B0\_MAT2\_PIO2\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(65, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_4 \*/ |
| --- |

## [◆ ](#a005db7665d634e68c56b59a3cb5b456d)CT32B0\_MAT3\_PIO0\_11

| #define CT32B0\_MAT3\_PIO0\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_11 \*/ |
| --- |

## [◆ ](#ac2a89c71d21325e0e64cd8a3d8c4ebdc)CT32B0\_MAT3\_PIO1\_27

| #define CT32B0\_MAT3\_PIO1\_27   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_27 \*/ |
| --- |

## [◆ ](#a7b28030377332811f795cd1462bf631f)CT32B1\_CAP0\_PIO0\_12

| #define CT32B1\_CAP0\_PIO0\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_12 \*/ |
| --- |

## [◆ ](#a54bfd60ff58b0148b6848f8b2982442e)CT32B1\_CAP0\_PIO1\_4

| #define CT32B1\_CAP0\_PIO1\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_4 \*/ |
| --- |

## [◆ ](#a39a31d62e31f796e3a54f43056577675)CT32B1\_CAP1\_PIO1\_22

| #define CT32B1\_CAP1\_PIO1\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_22 \*/ |
| --- |

## [◆ ](#a1ab5d0cd48d5ade99b0a6e4fc8bc9f68)CT32B1\_CAP1\_PIO1\_5

| #define CT32B1\_CAP1\_PIO1\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_5 \*/ |
| --- |

## [◆ ](#af55d0700864a68532d8b253344160ebf)CT32B1\_MAT0\_PIO0\_13

| #define CT32B1\_MAT0\_PIO0\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_13 \*/ |
| --- |

## [◆ ](#a5ee6340e6fe3b732b6d49bbef6c90155)CT32B1\_MAT0\_PIO1\_0

| #define CT32B1\_MAT0\_PIO1\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_0 \*/ |
| --- |

## [◆ ](#acc4bcbd80fa3306bfa4ab8a4d3023c34)CT32B1\_MAT1\_PIO0\_14

| #define CT32B1\_MAT1\_PIO0\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_14 \*/ |
| --- |

## [◆ ](#afb61298e6db2c507f6090a86566edc91)CT32B1\_MAT1\_PIO1\_1

| #define CT32B1\_MAT1\_PIO1\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_1 \*/ |
| --- |

## [◆ ](#ac5ed12914616e50cac147b251291d3f6)CT32B1\_MAT2\_PIO0\_15

| #define CT32B1\_MAT2\_PIO0\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_15 \*/ |
| --- |

## [◆ ](#a7e9fefa7d3b24bcf91c2af8143934e1b)CT32B1\_MAT2\_PIO1\_14

| #define CT32B1\_MAT2\_PIO1\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_14 \*/ |
| --- |

## [◆ ](#ab158e092af2c6ad056cc6f4d298c1951)CT32B1\_MAT2\_PIO1\_2

| #define CT32B1\_MAT2\_PIO1\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_2 \*/ |
| --- |

## [◆ ](#a26ecf5bab459bde9bbb64ff5a019b09a)CT32B1\_MAT3\_PIO0\_16

| #define CT32B1\_MAT3\_PIO0\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_16 \*/ |
| --- |

## [◆ ](#af960ef8b39ccd08fbe57d0fb2808507a)CT32B1\_MAT3\_PIO1\_15

| #define CT32B1\_MAT3\_PIO1\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_15 \*/ |
| --- |

## [◆ ](#a7edf5d0d95f5fa253b03ccc77447ed9a)CT32B1\_MAT3\_PIO1\_3

| #define CT32B1\_MAT3\_PIO1\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_3 \*/ |
| --- |

## [◆ ](#af03e2705d8630f60521f853e9b4b1d61)I2C0\_SCL\_PIO0\_4

| #define I2C0\_SCL\_PIO0\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(4, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 1) /\* PIO0\_4 \*/ |
| --- |

## [◆ ](#a7a30f5f10c3c59925e18d0526fa94431)I2C0\_SDA\_PIO0\_5

| #define I2C0\_SDA\_PIO0\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(5, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 1) /\* PIO0\_5 \*/ |
| --- |

## [◆ ](#a747ec67e7cb403d747b9f57429b71983)I2C1\_SCL\_PIO0\_7

| #define I2C1\_SCL\_PIO0\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_7 \*/ |
| --- |

## [◆ ](#abd5321e5d55560fb0927e8a26027d001)I2C1\_SCL\_PIO1\_11

| #define I2C1\_SCL\_PIO1\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_11 \*/ |
| --- |

## [◆ ](#a8edcf1fdf2dd40db40fc0e3bb226c868)I2C1\_SCL\_PIO1\_30

| #define I2C1\_SCL\_PIO1\_30   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_30 \*/ |
| --- |

## [◆ ](#aa478831aabf3f70f44dc83be779f29df)I2C1\_SDA\_PIO1\_14

| #define I2C1\_SDA\_PIO1\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_14 \*/ |
| --- |

## [◆ ](#ae7f01370d20cb64565a5e0d17190f11c)I2C1\_SDA\_PIO1\_24

| #define I2C1\_SDA\_PIO1\_24   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(48, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_24 \*/ |
| --- |

## [◆ ](#ae63879080611307c152e569946e7a7ae)I2C1\_SDA\_PIO1\_3

| #define I2C1\_SDA\_PIO1\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_3 \*/ |
| --- |

## [◆ ](#a9a3d4f3e281c382f795b9a769073d4e4)IOCON\_ADMODE\_EN

| #define IOCON\_ADMODE\_EN   (0 << 7) /\* Enable analog input mode. \*/ |
| --- |

## [◆ ](#a32dad85c69cde862614f7dc694de25e1)IOCON\_CLKDIV0

| #define IOCON\_CLKDIV0   (0 << 13) |
| --- |

## [◆ ](#a9cf0243a32cce57e52c3b3931979a0c4)IOCON\_CLKDIV1

| #define IOCON\_CLKDIV1   (1 << 13) |
| --- |

## [◆ ](#a05aed1b2f2679b3bb56a1bdc08e032a1)IOCON\_CLKDIV2

| #define IOCON\_CLKDIV2   (2 << 13) |
| --- |

## [◆ ](#a96b9d2b722278cdc733ddec36aca82b8)IOCON\_CLKDIV3

| #define IOCON\_CLKDIV3   (3 << 13) |
| --- |

## [◆ ](#a293173c3047155fd78ba45a0f4e464f5)IOCON\_CLKDIV4

| #define IOCON\_CLKDIV4   (4 << 13) |
| --- |

## [◆ ](#aecba1dab2a9cb8c19052ab56c7efbc6d)IOCON\_CLKDIV5

| #define IOCON\_CLKDIV5   (5 << 13) |
| --- |

## [◆ ](#a25f5cc1afc44889d9e77b62923135411)IOCON\_CLKDIV6

| #define IOCON\_CLKDIV6   (6 << 13) |
| --- |

## [◆ ](#a516e9d9bc7b1f3aaefd9d09c6ece74d2)IOCON\_DIGMODE\_EN

| #define IOCON\_DIGMODE\_EN   (1 << 7) /\* Enable digital I/O mode. \*/ |
| --- |

## [◆ ](#a5454c9c23da82b9db63d63866d054989)IOCON\_FASTI2C\_EN

| #define IOCON\_FASTI2C\_EN   (2 << 8) /\* I2C Fast-mode Plus. \*/ |
| --- |

## [◆ ](#a5a141a4fd02a8a7204cb251e1815b2ff)IOCON\_FILTR\_DIS

| #define IOCON\_FILTR\_DIS   (1 << 8) /\* Disable noise filtering. \*/ |
| --- |

## [◆ ](#ab08f72eae45dd5656aeca24c346c8626)IOCON\_FUNC0

| #define IOCON\_FUNC0   0 |
| --- |

Pin control register for standard digital I/O pins:

[0:2] function. [3:4] mode. [5] hysteresis. [6] invert input. [7:9] reserved. [10] open-drain mode. [11:12] digital filter sample mode. [13:15] clock divisor. [16:31] reserved.

Control registers for digital/analog I/O pins:

[0:2] function. [3:4] mode. [5] hysteresis. [6] invert input. [7] analog mode. [8] input glitch filter. [9] reserved. [10] open-drain mode. [11:12] digital filter sample mode. [13:15] clock divisor. [16:31] reserved.

Control registers for open-drain I/O pins (I2C):

[0:2] function. [3:7] reserved. [8:9] I2C mode. [10] reserved. [11:12] digital filter sample mode. [13:15] clock divisor. [16:31] reserved.

## [◆ ](#ab6449233bd56957c684b9ad694606e3a)IOCON\_FUNC1

| #define IOCON\_FUNC1   1 |
| --- |

## [◆ ](#a43ebb7abf055ce2491fbba5ef72f6fc7)IOCON\_FUNC2

| #define IOCON\_FUNC2   2 |
| --- |

## [◆ ](#ace4708e511b3aa9c352600604331bec0)IOCON\_FUNC3

| #define IOCON\_FUNC3   3 |
| --- |

## [◆ ](#ac621b96a2bd1ee57a83ff1af98287a8d)IOCON\_FUNC4

| #define IOCON\_FUNC4   4 |
| --- |

## [◆ ](#a0f9630599f40a3f96a5887c7e65508a9)IOCON\_FUNC5

| #define IOCON\_FUNC5   5 |
| --- |

## [◆ ](#afb7c408ac1f52b7b7e46fde3061fe0b7)IOCON\_HYS\_EN

| #define IOCON\_HYS\_EN   (1 << 5) /\* Enable hysteresis. \*/ |
| --- |

## [◆ ](#ae1fd1faa316f6c3108b499928f8c9922)IOCON\_INV\_EN

| #define IOCON\_INV\_EN   (1 << 6) /\* Invert input polarity. \*/ |
| --- |

## [◆ ](#afc593aafe607c88c52864ecb7586ffe9)IOCON\_MODE\_INACT

| #define IOCON\_MODE\_INACT   (0 << 3) /\* No pull resistor. \*/ |
| --- |

## [◆ ](#a270261df49234519bfd09e076dfcec6c)IOCON\_MODE\_PULLDOWN

| #define IOCON\_MODE\_PULLDOWN   (1 << 3) /\* Enable pull-down resistor. \*/ |
| --- |

## [◆ ](#ad8fe947d8e7076d6cec01a5b30261141)IOCON\_MODE\_PULLUP

| #define IOCON\_MODE\_PULLUP   (2 << 3) /\* Enable Pull-up resistor. \*/ |
| --- |

## [◆ ](#a53d705841cc362c6f43ffc1370d71726)IOCON\_MODE\_REPEATER

| #define IOCON\_MODE\_REPEATER   (3 << 3) /\* Repeater mode. \*/ |
| --- |

## [◆ ](#a3c281dcff389739802d68c2fc59d608e)IOCON\_MUX

| #define IOCON\_MUX | ( |  | *offset*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *mux* ) |

**Value:**

(((offset & 0xFFF) << 20) | \

(((type) & 0x3) << 18) | \

(((mux) & 0xF) << 0))

## [◆ ](#a226b54f672e61a7a2d2893d9ef8cbc9c)IOCON\_OPENDRAIN\_EN

| #define IOCON\_OPENDRAIN\_EN   (1 << 10) /\* Enable [open](fcntl_8h.md#ac843f2e35e60c3bbf1da47d84306f29b)-drain mode. \*/ |
| --- |

## [◆ ](#a05f3ba263e98d5ee980f1604e5bb901c)IOCON\_S\_MODE\_0CLK

| #define IOCON\_S\_MODE\_0CLK   (0 << 11) /\* No input filter. \*/ |
| --- |

## [◆ ](#a7148355cde16d13476362ff1c1bc1668)IOCON\_S\_MODE\_1CLK

| #define IOCON\_S\_MODE\_1CLK   (1 << 11) |
| --- |

## [◆ ](#a87827c87941a76ce73118c65afb439f5)IOCON\_S\_MODE\_2CLK

| #define IOCON\_S\_MODE\_2CLK   (2 << 11) |
| --- |

## [◆ ](#a54dba7082ab18b6a15eea0a87c119a71)IOCON\_S\_MODE\_3CLK

| #define IOCON\_S\_MODE\_3CLK   (3 << 11) |
| --- |

## [◆ ](#aa7dd24866523506919c8f3fa7a8614a8)IOCON\_SFI2C\_EN

| #define IOCON\_SFI2C\_EN   (0 << 8) /\* I2C standard mode / Fast-mode. \*/ |
| --- |

## [◆ ](#a897f505b779e01014e235f1d73745787)IOCON\_STDI2C\_EN

| #define IOCON\_STDI2C\_EN   (1 << 8) /\* GPIO functionality. \*/ |
| --- |

## [◆ ](#afd7386a10a00b7f0cfbb44d6ceb66df3)IOCON\_TYPE\_A

| #define IOCON\_TYPE\_A   0x2 |
| --- |

## [◆ ](#a9ae60793668890cd0dc2117dc64f02ba)IOCON\_TYPE\_D

| #define IOCON\_TYPE\_D   0x0 |
| --- |

## [◆ ](#a6c16820a5170feb2c133f82216318bbb)IOCON\_TYPE\_I

| #define IOCON\_TYPE\_I   0x1 |
| --- |

## [◆ ](#aa1d6732f64540461cae792821ac7b2d6)PIO0\_0\_PIO0\_0

| #define PIO0\_0\_PIO0\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(0, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_0 \*/ |
| --- |

## [◆ ](#a0b09489a89b80784605cddcc430914d6)PIO0\_10\_PIO0\_10

| #define PIO0\_10\_PIO0\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_10 \*/ |
| --- |

## [◆ ](#a157b55ccf1883066cc9217629366b809)PIO0\_11\_PIO0\_11

| #define PIO0\_11\_PIO0\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_11 \*/ |
| --- |

## [◆ ](#a51f64447bf880601691ffe859d0f1964)PIO0\_12\_PIO0\_12 [1/2]

| #define PIO0\_12\_PIO0\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 5) /\* PIO0\_12 \*/ |
| --- |

## [◆ ](#ab4b3327e260eccbcccf80f0c1904ac56)PIO0\_12\_PIO0\_12 [2/2]

| #define PIO0\_12\_PIO0\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_12 \*/ |
| --- |

## [◆ ](#a8d40f087b829a11db51c16ab2181995c)PIO0\_13\_PIO0\_13 [1/2]

| #define PIO0\_13\_PIO0\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 5) /\* PIO0\_13 \*/ |
| --- |

## [◆ ](#af1f156f6bca42a308c3d154ce6033f5a)PIO0\_13\_PIO0\_13 [2/2]

| #define PIO0\_13\_PIO0\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_13 \*/ |
| --- |

## [◆ ](#a692e4e1765be1cbca9897691a6bfbc39)PIO0\_14\_PIO0\_14

| #define PIO0\_14\_PIO0\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_14 \*/ |
| --- |

## [◆ ](#a59a92f1c63f7eb548a19f555cfe0208e)PIO0\_15\_PIO0\_15

| #define PIO0\_15\_PIO0\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_15 \*/ |
| --- |

## [◆ ](#aa4a10249e5ee8e04ce01f62864476727)PIO0\_16\_PIO0\_16

| #define PIO0\_16\_PIO0\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO0\_16 \*/ |
| --- |

## [◆ ](#a34451e215c47228b8337d0aed0c2c929)PIO0\_17\_PIO0\_17

| #define PIO0\_17\_PIO0\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_17 \*/ |
| --- |

## [◆ ](#a87d216855b3f78407343517d639cd75c)PIO0\_18\_PIO0\_18

| #define PIO0\_18\_PIO0\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(18, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_18 \*/ |
| --- |

## [◆ ](#a83757ba41e5c8ff4a04384a6f59550e1)PIO0\_19\_PIO0\_19

| #define PIO0\_19\_PIO0\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(19, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_19 \*/ |
| --- |

## [◆ ](#ab44c7ff7f772892dbb66149d8064ba04)PIO0\_1\_PIO0\_1

| #define PIO0\_1\_PIO0\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_1 \*/ |
| --- |

## [◆ ](#a28a9784674717e3617070ed87923a1f1)PIO0\_20\_PIO0\_20

| #define PIO0\_20\_PIO0\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(20, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_20 \*/ |
| --- |

## [◆ ](#abfb5b6fa233853dc18ed899fa4418b1b)PIO0\_21\_PIO0\_21

| #define PIO0\_21\_PIO0\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(21, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_21 \*/ |
| --- |

## [◆ ](#a9df3dda1a040239ee21e73c813659ccd)PIO0\_22\_PIO0\_22

| #define PIO0\_22\_PIO0\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_22 \*/ |
| --- |

## [◆ ](#a07878c04e96b6472f26d3760a42ac212)PIO0\_23\_PIO0\_23

| #define PIO0\_23\_PIO0\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_23 \*/ |
| --- |

## [◆ ](#ab5a06c37a003d97135fc0da7c9949f60)PIO0\_2\_PIO0\_2

| #define PIO0\_2\_PIO0\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_2 \*/ |
| --- |

## [◆ ](#a89f6d1689c8672f14033a31543ced43a)PIO0\_3\_PIO0\_3

| #define PIO0\_3\_PIO0\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(3, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_3 \*/ |
| --- |

## [◆ ](#a017c42b9bbbacfbbd9310b3f1a918a66)PIO0\_4\_PIO0\_4

| #define PIO0\_4\_PIO0\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(4, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 0) /\* PIO0\_4 \*/ |
| --- |

## [◆ ](#aa0fe8d6e7a4f69dd54980143f92df7ab)PIO0\_5\_PIO0\_5

| #define PIO0\_5\_PIO0\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(5, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 0) /\* PIO0\_5 \*/ |
| --- |

## [◆ ](#a50ab17a232562ebc41deb8238de35f20)PIO0\_6\_PIO0\_6

| #define PIO0\_6\_PIO0\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_6 \*/ |
| --- |

## [◆ ](#a95b8cc1a76a6097556568f4554bf4e3f)PIO0\_7\_PIO0\_7

| #define PIO0\_7\_PIO0\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_7 \*/ |
| --- |

## [◆ ](#a9e4b255125ef44e2de5c77743b4010ee)PIO0\_8\_PIO0\_8

| #define PIO0\_8\_PIO0\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_8 \*/ |
| --- |

## [◆ ](#a0db63ca26d440f3bc24a48d39fbfcc4b)PIO0\_9\_PIO0\_9

| #define PIO0\_9\_PIO0\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_9 \*/ |
| --- |

## [◆ ](#ac68053b619744fbf1c1f17f7b08cf580)PIO1\_0\_PIO1\_0

| #define PIO1\_0\_PIO1\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_0 \*/ |
| --- |

## [◆ ](#a037f6a357a5bbea0dc0cb9902c94c846)PIO1\_10\_PIO1\_10

| #define PIO1\_10\_PIO1\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_10 \*/ |
| --- |

## [◆ ](#a97b3bfd02acef68ffc82952e49bd03fe)PIO1\_11\_PIO1\_11

| #define PIO1\_11\_PIO1\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_11 \*/ |
| --- |

## [◆ ](#a896bd464fd196266a8862fde369e899b)PIO1\_12\_PIO1\_12

| #define PIO1\_12\_PIO1\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_12 \*/ |
| --- |

## [◆ ](#ad2d3d8b8bb3a17fab2dc03850b9934e6)PIO1\_13\_PIO1\_13

| #define PIO1\_13\_PIO1\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_13 \*/ |
| --- |

## [◆ ](#aec627d88659627216048116352084463)PIO1\_14\_PIO1\_14

| #define PIO1\_14\_PIO1\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_14 \*/ |
| --- |

## [◆ ](#ad430442be04fb9768354a29392aa3150)PIO1\_15\_PIO1\_15

| #define PIO1\_15\_PIO1\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_15 \*/ |
| --- |

## [◆ ](#a890647261f0d13600177b8da109e7f80)PIO1\_16\_PIO1\_16

| #define PIO1\_16\_PIO1\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_16 \*/ |
| --- |

## [◆ ](#ab7c4014e4c5aff2215d00bfbfcdca7c6)PIO1\_17\_PIO1\_17

| #define PIO1\_17\_PIO1\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_17 \*/ |
| --- |

## [◆ ](#abd5742cad3a656c0cca0a02ec6b41acf)PIO1\_18\_PIO1\_18

| #define PIO1\_18\_PIO1\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_18 \*/ |
| --- |

## [◆ ](#ae56e1309f5dfaff815c892ef0e1ed2b9)PIO1\_19\_PIO1\_19

| #define PIO1\_19\_PIO1\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_19 \*/ |
| --- |

## [◆ ](#a299fee16f12cef2f585e132548ba3b72)PIO1\_1\_PIO1\_1

| #define PIO1\_1\_PIO1\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_1 \*/ |
| --- |

## [◆ ](#adea5f43202f54b478043589ea1d4b1e1)PIO1\_20\_PIO1\_20

| #define PIO1\_20\_PIO1\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_20 \*/ |
| --- |

## [◆ ](#a0c6805b1f84117dee5e66f091818d9ca)PIO1\_21\_PIO1\_21

| #define PIO1\_21\_PIO1\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_21 \*/ |
| --- |

## [◆ ](#a689cbb1bd742d803a7d512f5be6c4cfb)PIO1\_22\_PIO1\_22

| #define PIO1\_22\_PIO1\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_22 \*/ |
| --- |

## [◆ ](#ab15b87098dc679562fcd0eb74aa8c761)PIO1\_23\_PIO1\_23

| #define PIO1\_23\_PIO1\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_23 \*/ |
| --- |

## [◆ ](#a86877f01c21462c697dcdf1163ef2057)PIO1\_24\_PIO1\_24

| #define PIO1\_24\_PIO1\_24   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(48, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_24 \*/ |
| --- |

## [◆ ](#ad1f94b842d9d03ecfd95521ad4fc50ef)PIO1\_25\_PIO1\_25

| #define PIO1\_25\_PIO1\_25   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_25 \*/ |
| --- |

## [◆ ](#a6b8c76bf4eb6a9e621363bbd7862a3c5)PIO1\_26\_PIO1\_26

| #define PIO1\_26\_PIO1\_26   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_26 \*/ |
| --- |

## [◆ ](#ac22ea9cd9fdb0dcf4125628fd41ad4e2)PIO1\_27\_PIO1\_27

| #define PIO1\_27\_PIO1\_27   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_27 \*/ |
| --- |

## [◆ ](#ae45e38efb89456519fd29191d1bfd41e)PIO1\_28\_PIO1\_28

| #define PIO1\_28\_PIO1\_28   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_28 \*/ |
| --- |

## [◆ ](#a07775fe074a265e8594cc0f1bc3c4553)PIO1\_29\_PIO1\_29

| #define PIO1\_29\_PIO1\_29   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_29 \*/ |
| --- |

## [◆ ](#a5265479414c8dd9845e6aa5213eda99e)PIO1\_2\_PIO1\_2

| #define PIO1\_2\_PIO1\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_2 \*/ |
| --- |

## [◆ ](#a0452698f8cda9677cc606f6e8386f0c5)PIO1\_30\_PIO1\_30

| #define PIO1\_30\_PIO1\_30   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_30 \*/ |
| --- |

## [◆ ](#ae459ff2b755df0e5a22378e59fb1ccbc)PIO1\_31\_PIO1\_31

| #define PIO1\_31\_PIO1\_31   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(55, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_31 \*/ |
| --- |

## [◆ ](#a2d403da5360929eed6c833567c415fe5)PIO1\_3\_PIO1\_3

| #define PIO1\_3\_PIO1\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_3 \*/ |
| --- |

## [◆ ](#aecf77d09221ba70819899708b4ad74a8)PIO1\_4\_PIO1\_4

| #define PIO1\_4\_PIO1\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_4 \*/ |
| --- |

## [◆ ](#ab070530de6c3105054206c5a526f5730)PIO1\_5\_PIO1\_5

| #define PIO1\_5\_PIO1\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_5 \*/ |
| --- |

## [◆ ](#af6b1804a5aefa54e7a3c4dba33394805)PIO1\_6\_PIO1\_6

| #define PIO1\_6\_PIO1\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_6 \*/ |
| --- |

## [◆ ](#ab77050cd6c5323ede0c6ce3f52f4f83e)PIO1\_7\_PIO1\_7

| #define PIO1\_7\_PIO1\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_7 \*/ |
| --- |

## [◆ ](#a5eb361e081a52918777d89f61c0a26fa)PIO1\_8\_PIO1\_8

| #define PIO1\_8\_PIO1\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO1\_8 \*/ |
| --- |

## [◆ ](#a75ab800970f73ac0177aaf8139ba8739)PIO1\_9\_PIO1\_9

| #define PIO1\_9\_PIO1\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO1\_9 \*/ |
| --- |

## [◆ ](#a5fafd0c519a03d1f678c7f1c6c3b34ed)PIO2\_0\_PIO2\_0

| #define PIO2\_0\_PIO2\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(60, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO2\_0 \*/ |
| --- |

## [◆ ](#a2471788decdf2d9119ca1245ddc77981)PIO2\_10\_PIO2\_10

| #define PIO2\_10\_PIO2\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(71, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_10 \*/ |
| --- |

## [◆ ](#a25f558f2d23c6a973da481216a331047)PIO2\_11\_PIO2\_11

| #define PIO2\_11\_PIO2\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(72, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_11 \*/ |
| --- |

## [◆ ](#a55b8398b79ab94885c5b1a266cc96b67)PIO2\_12\_PIO2\_12

| #define PIO2\_12\_PIO2\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(73, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_12 \*/ |
| --- |

## [◆ ](#aad0ffb60a10d384eec0c88137e9f5049)PIO2\_13\_PIO2\_13

| #define PIO2\_13\_PIO2\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(74, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_13 \*/ |
| --- |

## [◆ ](#a4d600902f1f7cfa6d6d7a15dad9fa47e)PIO2\_14\_PIO2\_14

| #define PIO2\_14\_PIO2\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(75, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_14 \*/ |
| --- |

## [◆ ](#a4247567257584b93a079dde0636a8d82)PIO2\_15\_PIO2\_15

| #define PIO2\_15\_PIO2\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(76, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_15 \*/ |
| --- |

## [◆ ](#a68ae2af37b444a788e82cbdd59a9518e)PIO2\_16\_PIO2\_16

| #define PIO2\_16\_PIO2\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(77, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_16 \*/ |
| --- |

## [◆ ](#aafd4249d51198bee34d7f03275b70bc6)PIO2\_17\_PIO2\_17

| #define PIO2\_17\_PIO2\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(78, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_17 \*/ |
| --- |

## [◆ ](#ab01949c5d3a85a0acb2266d7c4e71b8a)PIO2\_18\_PIO2\_18

| #define PIO2\_18\_PIO2\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(79, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_18 \*/ |
| --- |

## [◆ ](#a10046d3d553609d2e46568d31bcbd22b)PIO2\_19\_PIO2\_19

| #define PIO2\_19\_PIO2\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(80, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_19 \*/ |
| --- |

## [◆ ](#ab18db336e17b21d3e1864f47fbfe211b)PIO2\_1\_PIO2\_1

| #define PIO2\_1\_PIO2\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(61, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO2\_1 \*/ |
| --- |

## [◆ ](#a379470de275ec9e879c6a7da55dc81e2)PIO2\_20\_PIO2\_20

| #define PIO2\_20\_PIO2\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(81, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_20 \*/ |
| --- |

## [◆ ](#a8cc6a3d1353183ec7277fbb88a405961)PIO2\_21\_PIO2\_21

| #define PIO2\_21\_PIO2\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(82, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_21 \*/ |
| --- |

## [◆ ](#a12640000bfec871e24fff6deaa5cdd08)PIO2\_22\_PIO2\_22

| #define PIO2\_22\_PIO2\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(83, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_22 \*/ |
| --- |

## [◆ ](#ab78b84af5278ada6d4c31bbc85928899)PIO2\_23\_PIO2\_23

| #define PIO2\_23\_PIO2\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(84, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_23 \*/ |
| --- |

## [◆ ](#a5ee88fb076ffc8f05c54ffa403976fa4)PIO2\_2\_PIO2\_2

| #define PIO2\_2\_PIO2\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_2 \*/ |
| --- |

## [◆ ](#ab76b9f2a58719e0cbd557e5b3019861d)PIO2\_3\_PIO2\_3

| #define PIO2\_3\_PIO2\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(64, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_3 \*/ |
| --- |

## [◆ ](#aec83c87cf4c5c7a6cd72370978c5f3ab)PIO2\_4\_PIO2\_4

| #define PIO2\_4\_PIO2\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(65, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_4 \*/ |
| --- |

## [◆ ](#abd48058e2c15f74525c6354cf245db73)PIO2\_5\_PIO2\_5

| #define PIO2\_5\_PIO2\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(66, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_5 \*/ |
| --- |

## [◆ ](#a180b0de4ca0603c2e171c869a52f7580)PIO2\_6\_PIO2\_6

| #define PIO2\_6\_PIO2\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_6 \*/ |
| --- |

## [◆ ](#a7e1cd4171f323202a5b67bb1e9363732)PIO2\_7\_PIO2\_7

| #define PIO2\_7\_PIO2\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(68, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_7 \*/ |
| --- |

## [◆ ](#aa423ccac69367faeaee101c4ca4d411a)PIO2\_8\_PIO2\_8

| #define PIO2\_8\_PIO2\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(69, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_8 \*/ |
| --- |

## [◆ ](#aa849da24aea3e3d29c43cc8f7264b434)PIO2\_9\_PIO2\_9

| #define PIO2\_9\_PIO2\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(70, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO2\_9 \*/ |
| --- |

## [◆ ](#a497b4217421b6854a707201765ff12a8)R\_0\_PIO0\_2

| #define R\_0\_PIO0\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_2 \*/ |
| --- |

## [◆ ](#a1ac3960333408442de9bd74e694595de)R\_10\_PIO1\_0

| #define R\_10\_PIO1\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_0 \*/ |
| --- |

## [◆ ](#aaae95bceef30b054294e7a7eed2d68a4)R\_11\_PIO1\_1

| #define R\_11\_PIO1\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_1 \*/ |
| --- |

## [◆ ](#ac7bd9d42184bd9175925b2e789d4e0f8)R\_12\_PIO1\_2

| #define R\_12\_PIO1\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_2 \*/ |
| --- |

## [◆ ](#a1f35a5b9268e09e3ff279d0d7b27e8d9)R\_13\_PIO1\_3

| #define R\_13\_PIO1\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(27, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO1\_3 \*/ |
| --- |

## [◆ ](#aaba8b00d104b3163f0c7cee32b91cf1e)R\_14\_PIO1\_4

| #define R\_14\_PIO1\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_4 \*/ |
| --- |

## [◆ ](#adcccebfaed3f6f65e12a4052ff04fdcd)R\_15\_PIO1\_5

| #define R\_15\_PIO1\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_5 \*/ |
| --- |

## [◆ ](#a9f77fd7bcd00d7bc4e179cb3c3db622e)R\_16\_PIO1\_6

| #define R\_16\_PIO1\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_6 \*/ |
| --- |

## [◆ ](#a2478b21ed3999f9fb27e1ddcc555383f)R\_17\_PIO1\_7

| #define R\_17\_PIO1\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_7 \*/ |
| --- |

## [◆ ](#a01a390f0311638bc09569b06839fb7dd)R\_18\_PIO1\_8

| #define R\_18\_PIO1\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_8 \*/ |
| --- |

## [◆ ](#ab0411bc0f8b6654e0f7bb8259cb47e7e)R\_19\_PIO1\_26

| #define R\_19\_PIO1\_26   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_26 \*/ |
| --- |

## [◆ ](#a54242b6862e052d7d1c2ee998b6d3927)R\_1\_PIO0\_3

| #define R\_1\_PIO0\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(3, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_3 \*/ |
| --- |

## [◆ ](#a629bba740c1f829a7401dbe6972b155e)R\_20\_PIO1\_27

| #define R\_20\_PIO1\_27   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_27 \*/ |
| --- |

## [◆ ](#abe8e17586c29617e61a2671408e84637)R\_21\_PIO1\_12

| #define R\_21\_PIO1\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_12 \*/ |
| --- |

## [◆ ](#a8613dd791e9ddf76c84d12c9f25f31ed)R\_22\_PIO1\_13

| #define R\_22\_PIO1\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_13 \*/ |
| --- |

## [◆ ](#a75b2a3bdcdc904bce2ed4641fd77d36f)R\_23\_PIO1\_14

| #define R\_23\_PIO1\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(38, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_14 \*/ |
| --- |

## [◆ ](#a31607e58141be4451603b21142dc2b78)R\_24\_PIO1\_15

| #define R\_24\_PIO1\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_15 \*/ |
| --- |

## [◆ ](#afbf96bb8cc6cf2f8f56ac0f48de55a9d)R\_25\_PIO1\_16

| #define R\_25\_PIO1\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_16 \*/ |
| --- |

## [◆ ](#a485ea3b9fe56406e22a835ad8101ca2a)R\_26\_PIO1\_17

| #define R\_26\_PIO1\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_17 \*/ |
| --- |

## [◆ ](#a7a373b17b448fdd55c2b0b4e88750d38)R\_27\_PIO1\_18

| #define R\_27\_PIO1\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_18 \*/ |
| --- |

## [◆ ](#a1a87c8b465b4539dee7d82dcf0067d5b)R\_28\_PIO1\_19

| #define R\_28\_PIO1\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_19 \*/ |
| --- |

## [◆ ](#adfbe0b94e760582fccaa92f88f41d1f4)R\_29\_PIO1\_22

| #define R\_29\_PIO1\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO1\_22 \*/ |
| --- |

## [◆ ](#ab0e34b062fd26c27d29891c77d8542a0)R\_2\_PIO0\_4

| #define R\_2\_PIO0\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(4, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 2) /\* PIO0\_4 \*/ |
| --- |

## [◆ ](#a387b44f72acc4eb20b382da8f076d195)R\_30\_PIO1\_25

| #define R\_30\_PIO1\_25   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 4) /\* PIO1\_25 \*/ |
| --- |

## [◆ ](#a85192c0b77e70e515a9165852d221208)R\_31\_PIO1\_30

| #define R\_31\_PIO1\_30   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_30 \*/ |
| --- |

## [◆ ](#a372339383fc7d4d6e70965b744c10e48)R\_3\_PIO0\_5

| #define R\_3\_PIO0\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(5, [IOCON\_TYPE\_I](#a6c16820a5170feb2c133f82216318bbb), 2) /\* PIO0\_5 \*/ |
| --- |

## [◆ ](#a49f11eb792f5b0a7ecf80aeaa82291e2)R\_4\_PIO0\_6

| #define R\_4\_PIO0\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_6 \*/ |
| --- |

## [◆ ](#aea308935da9604f8bdfea4d58959e518)R\_5\_PIO0\_7

| #define R\_5\_PIO0\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_7 \*/ |
| --- |

## [◆ ](#a8feac8b8845786a001a5dedbd2c749cd)R\_6\_PIO0\_8

| #define R\_6\_PIO0\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_8 \*/ |
| --- |

## [◆ ](#add1b38cd0b4e6b4557b5feeb39df424e)R\_7\_PIO0\_9

| #define R\_7\_PIO0\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_9 \*/ |
| --- |

## [◆ ](#a58df208f71b6efffed28bbabddf45f41)R\_8\_PIO0\_16

| #define R\_8\_PIO0\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_16 \*/ |
| --- |

## [◆ ](#ab0d0d78534d6cc1d4cee77b3eee84114)R\_9\_PIO0\_23

| #define R\_9\_PIO0\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 2) /\* PIO0\_23 \*/ |
| --- |

## [◆ ](#a0d784ee93461dd2f05beeb7c9cfa46b7)R\_PIO0\_6

| #define R\_PIO0\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_6 \*/ |
| --- |

## [◆ ](#abd7869399ab5c12219c1d7e06885e391)RESET\_PIO0\_0

| #define RESET\_PIO0\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(0, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_0 \*/ |
| --- |

## [◆ ](#add2cbf06dc14447e4661ce8a3de45f2f)SCT0\_IN0\_PIO1\_25

| #define SCT0\_IN0\_PIO1\_25   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_25 \*/ |
| --- |

## [◆ ](#a73d3caf803f8a4df930c63cf4fe3f37c)SCT0\_IN1\_PIO2\_5

| #define SCT0\_IN1\_PIO2\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(66, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_5 \*/ |
| --- |

## [◆ ](#ae14001bfffc9a00d61caf9647a3527f0)SCT0\_IN2\_PIO2\_6

| #define SCT0\_IN2\_PIO2\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO2\_6 \*/ |
| --- |

## [◆ ](#a92bceca4249eed78de2037929325bc58)SCT0\_IN3\_PIO1\_30

| #define SCT0\_IN3\_PIO1\_30   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(54, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_30 \*/ |
| --- |

## [◆ ](#ac19819cd774abe2a0597247136804d2e)SCT0\_OUT0\_PIO1\_19

| #define SCT0\_OUT0\_PIO1\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_19 \*/ |
| --- |

## [◆ ](#adf678074b20d6e433bd2d9e9fb13681e)SCT0\_OUT1\_PIO2\_2

| #define SCT0\_OUT1\_PIO2\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO2\_2 \*/ |
| --- |

## [◆ ](#a41199c507951e02ae2aad6b1b94a2aa5)SCT0\_OUT2\_PIO2\_7

| #define SCT0\_OUT2\_PIO2\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(68, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_7 \*/ |
| --- |

## [◆ ](#a504a57a6c6e3014ed4df4320736c7713)SCT0\_OUT3\_PIO1\_13

| #define SCT0\_OUT3\_PIO1\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_13 \*/ |
| --- |

## [◆ ](#af4e4c1f8972faff68d459b159c385dd2)SCT1\_IN0\_PIO2\_8

| #define SCT1\_IN0\_PIO2\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(69, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_8 \*/ |
| --- |

## [◆ ](#afd99a1f94ac011c63fbb8a9a9db511da)SCT1\_IN1\_PIO2\_9

| #define SCT1\_IN1\_PIO2\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(70, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_9 \*/ |
| --- |

## [◆ ](#a372dcaa75ccd7aea049ae958f41e9332)SCT1\_IN2\_PIO2\_14

| #define SCT1\_IN2\_PIO2\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(75, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_14 \*/ |
| --- |

## [◆ ](#ad4ea56df396ac4cab517d5bd7b735f5c)SCT1\_IN3\_PIO2\_15

| #define SCT1\_IN3\_PIO2\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(76, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_15 \*/ |
| --- |

## [◆ ](#affe7ba3bec6cfd4b2bba3533ea8cbd66)SCT1\_OUT0\_PIO2\_16

| #define SCT1\_OUT0\_PIO2\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(77, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_16 \*/ |
| --- |

## [◆ ](#a2e3304361cf9766f08c764fac50ef9bc)SCT1\_OUT1\_PIO2\_17

| #define SCT1\_OUT1\_PIO2\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(78, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_17 \*/ |
| --- |

## [◆ ](#af2c8a7e95a4a2f63e1f86ed9aa83a76f)SCT1\_OUT2\_PIO2\_18

| #define SCT1\_OUT2\_PIO2\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(79, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_18 \*/ |
| --- |

## [◆ ](#a89409cbd5a036dd7ff5c5a868eef4521)SCT1\_OUT3\_PIO2\_19

| #define SCT1\_OUT3\_PIO2\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(80, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_19 \*/ |
| --- |

## [◆ ](#a1d448d4e7bfeed79bc6e3fb14947afa7)SSP0\_MISO\_PIO0\_8

| #define SSP0\_MISO\_PIO0\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(8, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_8 \*/ |
| --- |

## [◆ ](#adb527bbcf8d059c9bfccdf29f3ac4aa5)SSP0\_MISO\_PIO1\_16

| #define SSP0\_MISO\_PIO1\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(40, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_16 \*/ |
| --- |

## [◆ ](#af1a1f4c533ae4806d692aff574334ebf)SSP0\_MOSI\_PIO0\_9

| #define SSP0\_MOSI\_PIO0\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(9, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_9 \*/ |
| --- |

## [◆ ](#a0bc3c1d34d0bc7a92543edd4e743905f)SSP0\_MOSI\_PIO1\_12

| #define SSP0\_MOSI\_PIO1\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(36, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_12 \*/ |
| --- |

## [◆ ](#ad68005dc04bde783a05f6c47da6dc4ef)SSP0\_SCK\_PIO0\_10

| #define SSP0\_SCK\_PIO0\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_10 \*/ |
| --- |

## [◆ ](#a632c9844b7638e69f8846b845dce32f7)SSP0\_SCK\_PIO0\_6

| #define SSP0\_SCK\_PIO0\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(6, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_6 \*/ |
| --- |

## [◆ ](#afa406dcc3b4ce8853b38782aaee8b34c)SSP0\_SCK\_PIO1\_29

| #define SSP0\_SCK\_PIO1\_29   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_29 \*/ |
| --- |

## [◆ ](#a6f00dd7928fb37ed72b08f0ce57ee03c)SSP0\_SCK\_PIO2\_7

| #define SSP0\_SCK\_PIO2\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(68, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_7 \*/ |
| --- |

## [◆ ](#a883806b472afb21f170006c620fe2b2d)SSP0\_SSEL\_PIO0\_2

| #define SSP0\_SSEL\_PIO0\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(2, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_2 \*/ |
| --- |

## [◆ ](#acc0fec039c618cf46e788bfb6f651cfe)SSP0\_SSEL\_PIO1\_15

| #define SSP0\_SSEL\_PIO1\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(39, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_15 \*/ |
| --- |

## [◆ ](#a783a183d806cac03c7db41096bae4272)SSP1\_MISO\_PIO0\_22

| #define SSP1\_MISO\_PIO0\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(22, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_22 \*/ |
| --- |

## [◆ ](#af44b09e3f6bf4ac86fae8f257a0620c6)SSP1\_MISO\_PIO1\_21

| #define SSP1\_MISO\_PIO1\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_21 \*/ |
| --- |

## [◆ ](#aaec77c9670e3e88d00641020ec0d47d6)SSP1\_MOSI\_PIO0\_21

| #define SSP1\_MOSI\_PIO0\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(21, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_21 \*/ |
| --- |

## [◆ ](#aa39927fc00dacde807c16c4044fa62b5)SSP1\_MOSI\_PIO1\_22

| #define SSP1\_MOSI\_PIO1\_22   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(46, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_22 \*/ |
| --- |

## [◆ ](#af998519da9f4ffd89b606b0261f95a1e)SSP1\_SCK\_PIO1\_20

| #define SSP1\_SCK\_PIO1\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_20 \*/ |
| --- |

## [◆ ](#adc98f945f54727aa26fb4bb5acccb1b2)SSP1\_SCK\_PIO1\_27

| #define SSP1\_SCK\_PIO1\_27   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 4) /\* PIO1\_27 \*/ |
| --- |

## [◆ ](#a0a3ad1a37c02adc62dbae966523e6d4c)SSP1\_SSEL\_PIO0\_23

| #define SSP1\_SSEL\_PIO0\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_23 \*/ |
| --- |

## [◆ ](#a241d8f9f8546f68c66e490a4f42951ca)SSP1\_SSEL\_PIO1\_23

| #define SSP1\_SSEL\_PIO1\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_23 \*/ |
| --- |

## [◆ ](#a9694c0dc682d5d6be38b963226aaef3c)SWCLK\_PIO0\_10

| #define SWCLK\_PIO0\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(10, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 0) /\* PIO0\_10 \*/ |
| --- |

## [◆ ](#a0b65345797054d59564518f73eee1602)SWDIO\_PIO0\_15

| #define SWDIO\_PIO0\_15   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(15, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_15 \*/ |
| --- |

## [◆ ](#afbfb770c4372aadbdb6f5c18d399e17e)TDI\_PIO0\_11

| #define TDI\_PIO0\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_11 \*/ |
| --- |

## [◆ ](#ace1983c57935ab76096a42fa0d9af286)TDO\_PIO0\_13

| #define TDO\_PIO0\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_13 \*/ |
| --- |

## [◆ ](#a8e608b93b683519cda35d166e08ab587)TMS\_PIO0\_12

| #define TMS\_PIO0\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_12 \*/ |
| --- |

## [◆ ](#ad8c652abc5c8558f9312bd0ea201d7fc)TRST\_PIO0\_14

| #define TRST\_PIO0\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_14 \*/ |
| --- |

## [◆ ](#aad418e1711b045ea50806d464c92fbcf)U0\_CTS\_PIO0\_7

| #define U0\_CTS\_PIO0\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(7, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_7 \*/ |
| --- |

## [◆ ](#a5ec91d14ec34a2080c1d857e1fd6f572)U0\_CTS\_PIO1\_9

| #define U0\_CTS\_PIO1\_9   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(33, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO1\_9 \*/ |
| --- |

## [◆ ](#aaf239310ed5db40a24ca15cc7f48ed2b)U0\_DCD\_PIO1\_21

| #define U0\_DCD\_PIO1\_21   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(45, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_21 \*/ |
| --- |

## [◆ ](#a0abbdcaf023079f9181f260779ced50e)U0\_DCD\_PIO1\_5

| #define U0\_DCD\_PIO1\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(29, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_5 \*/ |
| --- |

## [◆ ](#a3ed819b62c0253666670f98230fb6194)U0\_DSR\_PIO1\_20

| #define U0\_DSR\_PIO1\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(44, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_20 \*/ |
| --- |

## [◆ ](#a0a7cdf5fa1cae307725c7cf8742cc599)U0\_DSR\_PIO1\_4

| #define U0\_DSR\_PIO1\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(28, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_4 \*/ |
| --- |

## [◆ ](#a7a17c6326f865f7eee09ec236ce12216)U0\_DTR\_PIO1\_1

| #define U0\_DTR\_PIO1\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(25, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_1 \*/ |
| --- |

## [◆ ](#affc255b3a5b093927b05ec78056090fa)U0\_DTRn\_PIO1\_29

| #define U0\_DTRn\_PIO1\_29   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(53, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO1\_29 \*/ |
| --- |

## [◆ ](#a1b2efba93021237e6fd7e3e276fef4e5)U0\_RI\_PIO0\_23

| #define U0\_RI\_PIO0\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(23, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 3) /\* PIO0\_23 \*/ |
| --- |

## [◆ ](#aa43f68879f82d124e3d1da1b1a4bee16)U0\_RI\_PIO1\_11

| #define U0\_RI\_PIO1\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(35, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_11 \*/ |
| --- |

## [◆ ](#ad946bbd06292183b7bdcd8db7d93d980)U0\_RTS\_PIO0\_17

| #define U0\_RTS\_PIO0\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_17 \*/ |
| --- |

## [◆ ](#a030246ec2f49c51f0ea088ed565d0f6d)U0\_RTS\_PIO1\_28

| #define U0\_RTS\_PIO1\_28   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_28 \*/ |
| --- |

## [◆ ](#a22d6493688b04414c7dc732d43f4c0f2)U0\_RXD\_PIO0\_18

| #define U0\_RXD\_PIO0\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(18, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_18 \*/ |
| --- |

## [◆ ](#a974de383ed91f1e80b6e67ab95f627d3)U0\_RXD\_PIO1\_17

| #define U0\_RXD\_PIO1\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(41, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_17 \*/ |
| --- |

## [◆ ](#a3cc2c9440f957296aa32d4636b2d6130)U0\_RXD\_PIO1\_26

| #define U0\_RXD\_PIO1\_26   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(50, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_26 \*/ |
| --- |

## [◆ ](#a5f911210bf444c31df578680aa92ba9e)U0\_SCLK\_PIO0\_17

| #define U0\_SCLK\_PIO0\_17   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(17, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_17 \*/ |
| --- |

## [◆ ](#a2eb7dfc050a7afad6630db88a430ffa4)U0\_SCLK\_PIO1\_28

| #define U0\_SCLK\_PIO1\_28   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(52, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_28 \*/ |
| --- |

## [◆ ](#a602172b5fe5dde4f7064ea152914e3b4)U0\_TXD\_PIO0\_19

| #define U0\_TXD\_PIO0\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(19, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_19 \*/ |
| --- |

## [◆ ](#a15cb6f2cf2ca2ba9b04b54b490e2c88b)U0\_TXD\_PIO1\_18

| #define U0\_TXD\_PIO1\_18   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(42, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_18 \*/ |
| --- |

## [◆ ](#aef4522554340d95f52f21f6896d121c6)U0\_TXD\_PIO1\_27

| #define U0\_TXD\_PIO1\_27   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(51, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_27 \*/ |
| --- |

## [◆ ](#ac58b55301756d90dcbfac6264df577b2)U1\_CTS\_PIO0\_12

| #define U1\_CTS\_PIO0\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(12, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_12 \*/ |
| --- |

## [◆ ](#ad00e6299050aceda961b3b6af7a78f79)U1\_CTS\_PIO1\_13

| #define U1\_CTS\_PIO1\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(37, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_13 \*/ |
| --- |

## [◆ ](#aaa87da84c9da4433539b55b513ab932b)U1\_RTS\_PIO0\_11

| #define U1\_RTS\_PIO0\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_11 \*/ |
| --- |

## [◆ ](#ab9a1ba400672c6486a0f8647164a1397)U1\_RTS\_PIO2\_6

| #define U1\_RTS\_PIO2\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_6 \*/ |
| --- |

## [◆ ](#a3eb45ad4dd10da96ed90153ef3b53665)U1\_RXD\_PIO0\_13

| #define U1\_RXD\_PIO0\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(13, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_13 \*/ |
| --- |

## [◆ ](#a4af77ea4a454643946504e10d249edcc)U1\_RXD\_PIO1\_2

| #define U1\_RXD\_PIO1\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(26, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_2 \*/ |
| --- |

## [◆ ](#a3c5e8df87f093df6858f6ceb7e33e5ec)U1\_SCLK\_PIO0\_11

| #define U1\_SCLK\_PIO0\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(11, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 5) /\* PIO0\_11 \*/ |
| --- |

## [◆ ](#a3885a451ceef59f37c8cb470aa3c23d0)U1\_SCLK\_PIO2\_6

| #define U1\_SCLK\_PIO2\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(67, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_6 \*/ |
| --- |

## [◆ ](#a567bb0593686aa6552e868caeb623532)U1\_TXD\_PIO0\_14

| #define U1\_TXD\_PIO0\_14   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(14, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 4) /\* PIO0\_14 \*/ |
| --- |

## [◆ ](#a253fad10b49809895c3f27ec3e51a567)U1\_TXD\_PIO1\_8

| #define U1\_TXD\_PIO1\_8   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(32, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_8 \*/ |
| --- |

## [◆ ](#a14b9435d73cf7890108f3f7e929154e7)U2\_CTS\_PIO1\_19

| #define U2\_CTS\_PIO1\_19   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(43, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_19 \*/ |
| --- |

## [◆ ](#a23bb3cc2ede010588651fede510df3db)U2\_CTS\_PIO1\_7

| #define U2\_CTS\_PIO1\_7   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(31, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_7 \*/ |
| --- |

## [◆ ](#a2f2957c1a43d63106ce2d61678103f62)U2\_RTS\_PIO1\_10

| #define U2\_RTS\_PIO1\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_10 \*/ |
| --- |

## [◆ ](#afc6ec4baef4bad621e4d62ae945a1163)U2\_RTS\_PIO1\_25

| #define U2\_RTS\_PIO1\_25   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO1\_25 \*/ |
| --- |

## [◆ ](#a9fc4de327d564720e61a338e4a5d3b5b)U2\_RXD\_PIO0\_20

| #define U2\_RXD\_PIO0\_20   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(20, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO0\_20 \*/ |
| --- |

## [◆ ](#a48ac3c0096037bbe64d92b2d2b0e621f)U2\_RXD\_PIO1\_6

| #define U2\_RXD\_PIO1\_6   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(30, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_6 \*/ |
| --- |

## [◆ ](#ac7236d26fd68c0be4b0f80e7ac6614cd)U2\_SCLK\_PIO1\_10

| #define U2\_SCLK\_PIO1\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(34, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_10 \*/ |
| --- |

## [◆ ](#a784ceb0c6b7772018f082fcd508cba4f)U2\_SCLK\_PIO1\_25

| #define U2\_SCLK\_PIO1\_25   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(49, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO1\_25 \*/ |
| --- |

## [◆ ](#a4319b4d5227cd2a7ff75de78a422a870)U2\_TXD\_PIO1\_0

| #define U2\_TXD\_PIO1\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(24, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_0 \*/ |
| --- |

## [◆ ](#adbafcde4cb5f052835ed790774e91a67)U2\_TXD\_PIO1\_23

| #define U2\_TXD\_PIO1\_23   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(47, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO1\_23 \*/ |
| --- |

## [◆ ](#a478a19515c027a5282b061de7a201317)U3\_CTS\_PIO2\_5

| #define U3\_CTS\_PIO2\_5   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(66, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_5 \*/ |
| --- |

## [◆ ](#aa079f73f9150780aabd8e2cc2325c465)U3\_RTS\_PIO2\_2

| #define U3\_RTS\_PIO2\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_2 \*/ |
| --- |

## [◆ ](#a330a0f6bb26f2a8d1881433d42251d88)U3\_RXD\_PIO2\_3

| #define U3\_RXD\_PIO2\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(64, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_3 \*/ |
| --- |

## [◆ ](#ab257d298276dc7d42c7c4ccfbde4b2fe)U3\_SCLK\_PIO2\_2

| #define U3\_SCLK\_PIO2\_2   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(63, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_2 \*/ |
| --- |

## [◆ ](#a69efa41cce2c5e868b790df9bb2f2fe5)U3\_TXD\_PIO2\_4

| #define U3\_TXD\_PIO2\_4   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(65, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_4 \*/ |
| --- |

## [◆ ](#a2481a40bdab053f1d25e6fd4daeb90cc)U4\_CTS\_PIO2\_13

| #define U4\_CTS\_PIO2\_13   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(74, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_13 \*/ |
| --- |

## [◆ ](#a531b7e88f7193b4ce754081685e6d23f)U4\_RTS\_PIO2\_10

| #define U4\_RTS\_PIO2\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(71, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_10 \*/ |
| --- |

## [◆ ](#aaabe5ad6b984f52723df7c958e043cd2)U4\_RXD\_PIO2\_11

| #define U4\_RXD\_PIO2\_11   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(72, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_11 \*/ |
| --- |

## [◆ ](#a34a74c9cc41c9839ee54dccf1aaa9ad7)U4\_SCLK\_PIO2\_10

| #define U4\_SCLK\_PIO2\_10   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(71, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 2) /\* PIO2\_10 \*/ |
| --- |

## [◆ ](#aa676078e9cc9a7dbb114e9e39bbdee07)U4\_TXD\_PIO2\_12

| #define U4\_TXD\_PIO2\_12   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(73, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO2\_12 \*/ |
| --- |

## [◆ ](#a827fea9b1eb5d3d16dbb1f95bd06b40e)USB\_FTOGGLE\_PIO0\_1

| #define USB\_FTOGGLE\_PIO0\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(1, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 3) /\* PIO0\_1 \*/ |
| --- |

## [◆ ](#a410001d990fb8424e9f6d75f6a7f2c67)USB\_VBUS\_PIO0\_3

| #define USB\_VBUS\_PIO0\_3   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(3, [IOCON\_TYPE\_D](#a9ae60793668890cd0dc2117dc64f02ba), 1) /\* PIO0\_3 \*/ |
| --- |

## [◆ ](#a285bf9c6e5c1b7bfc8ada6ececbe466e)WAKEUP\_PIO0\_16

| #define WAKEUP\_PIO0\_16   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(16, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 0) /\* PIO0\_16 \*/ |
| --- |

## [◆ ](#a5f3bfb1721c59d5800bcdf187dbddeb1)XTALIN\_PIO2\_0

| #define XTALIN\_PIO2\_0   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(60, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO2\_0 \*/ |
| --- |

## [◆ ](#a8c1b112e94052158ccefdda7c023d9e0)XTALOUT\_PIO2\_1

| #define XTALOUT\_PIO2\_1   [IOCON\_MUX](#a3c281dcff389739802d68c2fc59d608e)(61, [IOCON\_TYPE\_A](#afd7386a10a00b7f0cfbb44d6ceb66df3), 1) /\* PIO2\_1 \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [lpc11u6x-pinctrl.h](lpc11u6x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
