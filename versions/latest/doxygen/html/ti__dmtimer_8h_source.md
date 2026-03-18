---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ti__dmtimer_8h_source.html
original_path: doxygen/html/ti__dmtimer_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti\_dmtimer.h

[Go to the documentation of this file.](ti__dmtimer_8h.md)

1/\* Copyright (C) 2023 BeagleBoard.org Foundation

2 \* Copyright (C) 2023 S Prashanth

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_TIMERS\_TI\_DMTIMER\_H\_

8#define ZEPHYR\_DRIVERS\_TIMERS\_TI\_DMTIMER\_H\_

9

10#include <[zephyr/devicetree.h](devicetree_8h.md)>

11

[ 12](ti__dmtimer_8h.md#a1f6e7aaf701af4ae2f6c1733f583c030)#define TI\_DM\_TIMER\_TIDR (0x00)

[ 13](ti__dmtimer_8h.md#aa56da16a805b0751da5b13e1e8cf614e)#define TI\_DM\_TIMER\_TIOCP\_CFG (0x10)

[ 14](ti__dmtimer_8h.md#a883a455ac45e71a764197e86a6ac608a)#define TI\_DM\_TIMER\_IRQ\_EOI (0x20)

[ 15](ti__dmtimer_8h.md#aed6f6246fb153daade0cef1b8d5e9986)#define TI\_DM\_TIMER\_IRQSTATUS\_RAW (0x24)

[ 16](ti__dmtimer_8h.md#aa8b0aad13e3bf9d9a0592a97748c0df0)#define TI\_DM\_TIMER\_IRQSTATUS (0x28) /\* Interrupt status register \*/

[ 17](ti__dmtimer_8h.md#ab996271ed6baab36eb37ecdf65812753)#define TI\_DM\_TIMER\_IRQENABLE\_SET (0x2c) /\* Interrupt enable register \*/

[ 18](ti__dmtimer_8h.md#a8b4633934985ba40556e6dedb2fef05d)#define TI\_DM\_TIMER\_IRQENABLE\_CLR (0x30) /\* Interrupt disable register \*/

[ 19](ti__dmtimer_8h.md#abae8f0515e3c839f6591abee28b2fe2b)#define TI\_DM\_TIMER\_IRQWAKEEN (0x34)

[ 20](ti__dmtimer_8h.md#aeac307067f8a8bb76ad21858e73e896d)#define TI\_DM\_TIMER\_TCLR (0x38) /\* Control register \*/

[ 21](ti__dmtimer_8h.md#a3b95a3a1b84ab51e68829b8da58ec653)#define TI\_DM\_TIMER\_TCRR (0x3c) /\* Counter register \*/

[ 22](ti__dmtimer_8h.md#a2add6ea2a2a6b74b6441bf39f6c92104)#define TI\_DM\_TIMER\_TLDR (0x40) /\* Load register \*/

[ 23](ti__dmtimer_8h.md#a5a96b8379a240c79f3ace9a11df8d74e)#define TI\_DM\_TIMER\_TTGR (0x44)

[ 24](ti__dmtimer_8h.md#ada67d1b0a5a4d30f6444ad95fe6b8b92)#define TI\_DM\_TIMER\_TWPS (0x48)

[ 25](ti__dmtimer_8h.md#ac1f3248a4b71e01474f95a54bd904a6f)#define TI\_DM\_TIMER\_TMAR (0x4c) /\* Match register \*/

[ 26](ti__dmtimer_8h.md#a434e08af9ecba1079fdc48803a6050b3)#define TI\_DM\_TIMER\_TCAR1 (0x50)

[ 27](ti__dmtimer_8h.md#a61a110e410de5cf55dfe73016560fd1e)#define TI\_DM\_TIMER\_TSICR (0x54)

[ 28](ti__dmtimer_8h.md#a8467a67685d64c8db4ed8e790da33794)#define TI\_DM\_TIMER\_TCAR2 (0x58)

[ 29](ti__dmtimer_8h.md#ad7d5db65865c15fd9be2a112df6f262b)#define TI\_DM\_TIMER\_TPIR (0x5c)

[ 30](ti__dmtimer_8h.md#a860d9c4171c98d5f04ea3119264005ff)#define TI\_DM\_TIMER\_TNIR (0x60)

[ 31](ti__dmtimer_8h.md#ad0da36c4613a3c3016eee79ec6ee4182)#define TI\_DM\_TIMER\_TCVR (0x64)

[ 32](ti__dmtimer_8h.md#a448d5710703a7693a53f26ca8607a27b)#define TI\_DM\_TIMER\_TOCR (0x68)

[ 33](ti__dmtimer_8h.md#aa8ca463e0376a2c8d8a6f595ee6eb856)#define TI\_DM\_TIMER\_TOWR (0x6c)

34

[ 35](ti__dmtimer_8h.md#a6f07c56007ec7faba21303036574d9a8)#define TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_SHIFT (0)

[ 36](ti__dmtimer_8h.md#ab1b3b1f674bb6cfb2280de8cd961a2f8)#define TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_MASK (0x00000001)

37

[ 38](ti__dmtimer_8h.md#ac456e3d253745c1392125c7d042dbca5)#define TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_SHIFT (1)

[ 39](ti__dmtimer_8h.md#acb7221b7876ad443b10b29c509490fce)#define TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_MASK (0x00000002)

40

[ 41](ti__dmtimer_8h.md#a3c6acb16edf7747adefde2c6ceb7c6b8)#define TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_SHIFT (2)

[ 42](ti__dmtimer_8h.md#a0e8210c88b07fee206ae521972031ca5)#define TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_MASK (0x00000004)

43

[ 44](ti__dmtimer_8h.md#aaf00df3b3bf832258b6c280d7873ac4c)#define TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_SHIFT (0)

[ 45](ti__dmtimer_8h.md#a47498b7867d3f5d7e18ddfb2da57bd2e)#define TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_MASK (0x00000001)

46

[ 47](ti__dmtimer_8h.md#a29dad34e523db41e20a6e04630f49518)#define TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_SHIFT (1)

[ 48](ti__dmtimer_8h.md#a2f364c3b0a669315a9c43204b86e1411)#define TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_MASK (0x00000002)

49

[ 50](ti__dmtimer_8h.md#a832440567ccef54d18b992f450bfea7b)#define TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_SHIFT (2)

[ 51](ti__dmtimer_8h.md#a062dc13aa47f730ae3e96c7327087ff4)#define TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_MASK (0x00000004)

52

[ 53](ti__dmtimer_8h.md#a0025f82e15a59ad473276eb9021d76a4)#define TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_SHIFT (0)

[ 54](ti__dmtimer_8h.md#adaadc8ffb62f9e2cc742cd2a1a1fddee)#define TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_MASK (0x00000001)

55

[ 56](ti__dmtimer_8h.md#a58f2aab3a04560d7dbe73ca19abc3583)#define TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_SHIFT (1)

[ 57](ti__dmtimer_8h.md#a383168b3e88b65bc8e944c077b1c32e5)#define TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_MASK (0x00000002)

58

[ 59](ti__dmtimer_8h.md#a5f8d4f83fbc9e3e249e8ecf63e6a4888)#define TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_SHIFT (2)

[ 60](ti__dmtimer_8h.md#a5380a6d8bec09d9013d3c53078c9774f)#define TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_MASK (0x00000004)

61

[ 62](ti__dmtimer_8h.md#a89c93b281bd2b94ad65ca2be0085f101)#define TI\_DM\_TIMER\_TCLR\_ST\_SHIFT (0)

[ 63](ti__dmtimer_8h.md#ab7c38741f258b57d663cba9db98bfd2b)#define TI\_DM\_TIMER\_TCLR\_ST\_MASK (0x00000001)

64

[ 65](ti__dmtimer_8h.md#a0acc5881afa115f5cfeb30c5c9562cac)#define TI\_DM\_TIMER\_TCLR\_AR\_SHIFT (1)

[ 66](ti__dmtimer_8h.md#a8930ee981bf263f957f03e4005de1914)#define TI\_DM\_TIMER\_TCLR\_AR\_MASK (0x00000002)

67

[ 68](ti__dmtimer_8h.md#aed7a065bab0107cf992fba11be76a114)#define TI\_DM\_TIMER\_TCLR\_PTV\_SHIFT (2)

[ 69](ti__dmtimer_8h.md#a4d1e122bb953d4f6131a0af934862687)#define TI\_DM\_TIMER\_TCLR\_PTV\_MASK (0x0000001c)

70

[ 71](ti__dmtimer_8h.md#ad03f6e7dc83dcf000170764d49caa9e2)#define TI\_DM\_TIMER\_TCLR\_PRE\_SHIFT (5)

[ 72](ti__dmtimer_8h.md#a76270082286c83d24892bb732b3ac661)#define TI\_DM\_TIMER\_TCLR\_PRE\_MASK (0x00000020)

73

[ 74](ti__dmtimer_8h.md#a8a62240a5df6a22a7f6f7f4e6e556199)#define TI\_DM\_TIMER\_TCLR\_CE\_SHIFT (6)

[ 75](ti__dmtimer_8h.md#a41d49ed8260dde05209ec472d9cdded7)#define TI\_DM\_TIMER\_TCLR\_CE\_MASK (0x00000040)

76

[ 77](ti__dmtimer_8h.md#addd64fdd8ce7aa631acb4070457ab001)#define TI\_DM\_TIMER\_TCLR\_SCPWM\_SHIFT (7)

[ 78](ti__dmtimer_8h.md#a335faed7df51516361f8c71ca6cdd3d0)#define TI\_DM\_TIMER\_TCLR\_SCPWM\_MASK (0x00000080)

79

[ 80](ti__dmtimer_8h.md#a05956685e5d2e0807bdfcc624871e912)#define TI\_DM\_TIMER\_TCLR\_TCM\_SHIFT (8)

[ 81](ti__dmtimer_8h.md#a401b116bdd9f2ae1ef421eab2d9a68b8)#define TI\_DM\_TIMER\_TCLR\_TCM\_MASK (0x00000300)

82

[ 83](ti__dmtimer_8h.md#ad6a33b765f80b62951c9c49511d4c159)#define TI\_DM\_TIMER\_TCLR\_TRG\_SHIFT (10)

[ 84](ti__dmtimer_8h.md#a3a038b27593cbd4b46b1cc1a0ac45c16)#define TI\_DM\_TIMER\_TCLR\_TRG\_MASK (0x00000c00)

85

[ 86](ti__dmtimer_8h.md#af7a3217343141ed60d37416e6165fac6)#define TI\_DM\_TIMER\_TCLR\_PT\_SHIFT (12)

[ 87](ti__dmtimer_8h.md#a7dba4ee7a2a2fca79f0cef998476b176)#define TI\_DM\_TIMER\_TCLR\_PT\_MASK (0x00001000)

88

[ 89](ti__dmtimer_8h.md#ad2391b2472de54667863e2e528f305a5)#define TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_SHIFT (13)

[ 90](ti__dmtimer_8h.md#ada8250d08e208124c42d76ccc218c5df)#define TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_MASK (0x00002000)

91

[ 92](ti__dmtimer_8h.md#aac119b490b0103d9487bfbedfeb00e31)#define TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_SHIFT (14)

[ 93](ti__dmtimer_8h.md#a8d5d36a375e89dc541587c6bae49a546)#define TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_MASK (0x00004000)

94

[ 95](ti__dmtimer_8h.md#a0b25a9454f5b47ca438791b9fc3ea9ef)#define TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_SHIFT (0)

[ 96](ti__dmtimer_8h.md#a86ba1990c4c0779134849e08557db422)#define TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_MASK (0xffffffff)

97

[ 98](ti__dmtimer_8h.md#a882d4518296c0e42c266d645399b78e8)#define TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_SHIFT (0)

[ 99](ti__dmtimer_8h.md#af2879252745d377777ee4237659e3299)#define TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_MASK (0xffffffff)

100

[ 101](ti__dmtimer_8h.md#a28e1f82f16738262a2984214965f83ef)#define TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_SHIFT (0)

[ 102](ti__dmtimer_8h.md#a59820ad3de0f2118150a95de05a05fb5)#define TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_MASK (0xffffffff)

103

104#endif /\* ZEPHYR\_DRIVERS\_TIMERS\_TI\_DMTIMER\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [ti\_dmtimer.h](ti__dmtimer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
