---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ti__dmtimer_8h.html
original_path: doxygen/html/ti__dmtimer_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti\_dmtimer.h File Reference

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](ti__dmtimer_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TI\_DM\_TIMER\_TIDR](#a1f6e7aaf701af4ae2f6c1733f583c030)   (0x00) |
| #define | [TI\_DM\_TIMER\_TIOCP\_CFG](#aa56da16a805b0751da5b13e1e8cf614e)   (0x10) |
| #define | [TI\_DM\_TIMER\_IRQ\_EOI](#a883a455ac45e71a764197e86a6ac608a)   (0x20) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_RAW](#aed6f6246fb153daade0cef1b8d5e9986)   (0x24) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS](#aa8b0aad13e3bf9d9a0592a97748c0df0)   (0x28) /\* Interrupt status register \*/ |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET](#ab996271ed6baab36eb37ecdf65812753)   (0x2c) /\* Interrupt enable register \*/ |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR](#a8b4633934985ba40556e6dedb2fef05d)   (0x30) /\* Interrupt disable register \*/ |
| #define | [TI\_DM\_TIMER\_IRQWAKEEN](#abae8f0515e3c839f6591abee28b2fe2b)   (0x34) |
| #define | [TI\_DM\_TIMER\_TCLR](#aeac307067f8a8bb76ad21858e73e896d)   (0x38) /\* Control register \*/ |
| #define | [TI\_DM\_TIMER\_TCRR](#a3b95a3a1b84ab51e68829b8da58ec653)   (0x3c) /\* Counter register \*/ |
| #define | [TI\_DM\_TIMER\_TLDR](#a2add6ea2a2a6b74b6441bf39f6c92104)   (0x40) /\* Load register \*/ |
| #define | [TI\_DM\_TIMER\_TTGR](#a5a96b8379a240c79f3ace9a11df8d74e)   (0x44) |
| #define | [TI\_DM\_TIMER\_TWPS](#ada67d1b0a5a4d30f6444ad95fe6b8b92)   (0x48) |
| #define | [TI\_DM\_TIMER\_TMAR](#ac1f3248a4b71e01474f95a54bd904a6f)   (0x4c) /\* Match register \*/ |
| #define | [TI\_DM\_TIMER\_TCAR1](#a434e08af9ecba1079fdc48803a6050b3)   (0x50) |
| #define | [TI\_DM\_TIMER\_TSICR](#a61a110e410de5cf55dfe73016560fd1e)   (0x54) |
| #define | [TI\_DM\_TIMER\_TCAR2](#a8467a67685d64c8db4ed8e790da33794)   (0x58) |
| #define | [TI\_DM\_TIMER\_TPIR](#ad7d5db65865c15fd9be2a112df6f262b)   (0x5c) |
| #define | [TI\_DM\_TIMER\_TNIR](#a860d9c4171c98d5f04ea3119264005ff)   (0x60) |
| #define | [TI\_DM\_TIMER\_TCVR](#ad0da36c4613a3c3016eee79ec6ee4182)   (0x64) |
| #define | [TI\_DM\_TIMER\_TOCR](#a448d5710703a7693a53f26ca8607a27b)   (0x68) |
| #define | [TI\_DM\_TIMER\_TOWR](#aa8ca463e0376a2c8d8a6f595ee6eb856)   (0x6c) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_SHIFT](#a6f07c56007ec7faba21303036574d9a8)   (0) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_MASK](#ab1b3b1f674bb6cfb2280de8cd961a2f8)   (0x00000001) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_SHIFT](#ac456e3d253745c1392125c7d042dbca5)   (1) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_MASK](#acb7221b7876ad443b10b29c509490fce)   (0x00000002) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_SHIFT](#a3c6acb16edf7747adefde2c6ceb7c6b8)   (2) |
| #define | [TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_MASK](#a0e8210c88b07fee206ae521972031ca5)   (0x00000004) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_SHIFT](#aaf00df3b3bf832258b6c280d7873ac4c)   (0) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_MASK](#a47498b7867d3f5d7e18ddfb2da57bd2e)   (0x00000001) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_SHIFT](#a29dad34e523db41e20a6e04630f49518)   (1) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_MASK](#a2f364c3b0a669315a9c43204b86e1411)   (0x00000002) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_SHIFT](#a832440567ccef54d18b992f450bfea7b)   (2) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_MASK](#a062dc13aa47f730ae3e96c7327087ff4)   (0x00000004) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_SHIFT](#a0025f82e15a59ad473276eb9021d76a4)   (0) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_MASK](#adaadc8ffb62f9e2cc742cd2a1a1fddee)   (0x00000001) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_SHIFT](#a58f2aab3a04560d7dbe73ca19abc3583)   (1) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_MASK](#a383168b3e88b65bc8e944c077b1c32e5)   (0x00000002) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_SHIFT](#a5f8d4f83fbc9e3e249e8ecf63e6a4888)   (2) |
| #define | [TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_MASK](#a5380a6d8bec09d9013d3c53078c9774f)   (0x00000004) |
| #define | [TI\_DM\_TIMER\_TCLR\_ST\_SHIFT](#a89c93b281bd2b94ad65ca2be0085f101)   (0) |
| #define | [TI\_DM\_TIMER\_TCLR\_ST\_MASK](#ab7c38741f258b57d663cba9db98bfd2b)   (0x00000001) |
| #define | [TI\_DM\_TIMER\_TCLR\_AR\_SHIFT](#a0acc5881afa115f5cfeb30c5c9562cac)   (1) |
| #define | [TI\_DM\_TIMER\_TCLR\_AR\_MASK](#a8930ee981bf263f957f03e4005de1914)   (0x00000002) |
| #define | [TI\_DM\_TIMER\_TCLR\_PTV\_SHIFT](#aed7a065bab0107cf992fba11be76a114)   (2) |
| #define | [TI\_DM\_TIMER\_TCLR\_PTV\_MASK](#a4d1e122bb953d4f6131a0af934862687)   (0x0000001c) |
| #define | [TI\_DM\_TIMER\_TCLR\_PRE\_SHIFT](#ad03f6e7dc83dcf000170764d49caa9e2)   (5) |
| #define | [TI\_DM\_TIMER\_TCLR\_PRE\_MASK](#a76270082286c83d24892bb732b3ac661)   (0x00000020) |
| #define | [TI\_DM\_TIMER\_TCLR\_CE\_SHIFT](#a8a62240a5df6a22a7f6f7f4e6e556199)   (6) |
| #define | [TI\_DM\_TIMER\_TCLR\_CE\_MASK](#a41d49ed8260dde05209ec472d9cdded7)   (0x00000040) |
| #define | [TI\_DM\_TIMER\_TCLR\_SCPWM\_SHIFT](#addd64fdd8ce7aa631acb4070457ab001)   (7) |
| #define | [TI\_DM\_TIMER\_TCLR\_SCPWM\_MASK](#a335faed7df51516361f8c71ca6cdd3d0)   (0x00000080) |
| #define | [TI\_DM\_TIMER\_TCLR\_TCM\_SHIFT](#a05956685e5d2e0807bdfcc624871e912)   (8) |
| #define | [TI\_DM\_TIMER\_TCLR\_TCM\_MASK](#a401b116bdd9f2ae1ef421eab2d9a68b8)   (0x00000300) |
| #define | [TI\_DM\_TIMER\_TCLR\_TRG\_SHIFT](#ad6a33b765f80b62951c9c49511d4c159)   (10) |
| #define | [TI\_DM\_TIMER\_TCLR\_TRG\_MASK](#a3a038b27593cbd4b46b1cc1a0ac45c16)   (0x00000c00) |
| #define | [TI\_DM\_TIMER\_TCLR\_PT\_SHIFT](#af7a3217343141ed60d37416e6165fac6)   (12) |
| #define | [TI\_DM\_TIMER\_TCLR\_PT\_MASK](#a7dba4ee7a2a2fca79f0cef998476b176)   (0x00001000) |
| #define | [TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_SHIFT](#ad2391b2472de54667863e2e528f305a5)   (13) |
| #define | [TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_MASK](#ada8250d08e208124c42d76ccc218c5df)   (0x00002000) |
| #define | [TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_SHIFT](#aac119b490b0103d9487bfbedfeb00e31)   (14) |
| #define | [TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_MASK](#a8d5d36a375e89dc541587c6bae49a546)   (0x00004000) |
| #define | [TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_SHIFT](#a0b25a9454f5b47ca438791b9fc3ea9ef)   (0) |
| #define | [TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_MASK](#a86ba1990c4c0779134849e08557db422)   (0xffffffff) |
| #define | [TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_SHIFT](#a882d4518296c0e42c266d645399b78e8)   (0) |
| #define | [TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_MASK](#af2879252745d377777ee4237659e3299)   (0xffffffff) |
| #define | [TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_SHIFT](#a28e1f82f16738262a2984214965f83ef)   (0) |
| #define | [TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_MASK](#a59820ad3de0f2118150a95de05a05fb5)   (0xffffffff) |

## Macro Definition Documentation

## [◆ ](#a883a455ac45e71a764197e86a6ac608a)TI\_DM\_TIMER\_IRQ\_EOI

| #define TI\_DM\_TIMER\_IRQ\_EOI   (0x20) |
| --- |

## [◆ ](#a8b4633934985ba40556e6dedb2fef05d)TI\_DM\_TIMER\_IRQENABLE\_CLR

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR   (0x30) /\* Interrupt disable register \*/ |
| --- |

## [◆ ](#adaadc8ffb62f9e2cc742cd2a1a1fddee)TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_MASK   (0x00000001) |
| --- |

## [◆ ](#a0025f82e15a59ad473276eb9021d76a4)TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR\_MAT\_EN\_FLAG\_SHIFT   (0) |
| --- |

## [◆ ](#a383168b3e88b65bc8e944c077b1c32e5)TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_MASK   (0x00000002) |
| --- |

## [◆ ](#a58f2aab3a04560d7dbe73ca19abc3583)TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR\_OVF\_EN\_FLAG\_SHIFT   (1) |
| --- |

## [◆ ](#a5380a6d8bec09d9013d3c53078c9774f)TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_MASK   (0x00000004) |
| --- |

## [◆ ](#a5f8d4f83fbc9e3e249e8ecf63e6a4888)TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQENABLE\_CLR\_TCAR\_EN\_FLAG\_SHIFT   (2) |
| --- |

## [◆ ](#ab996271ed6baab36eb37ecdf65812753)TI\_DM\_TIMER\_IRQENABLE\_SET

| #define TI\_DM\_TIMER\_IRQENABLE\_SET   (0x2c) /\* Interrupt enable register \*/ |
| --- |

## [◆ ](#a47498b7867d3f5d7e18ddfb2da57bd2e)TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_MASK   (0x00000001) |
| --- |

## [◆ ](#aaf00df3b3bf832258b6c280d7873ac4c)TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQENABLE\_SET\_MAT\_EN\_FLAG\_SHIFT   (0) |
| --- |

## [◆ ](#a2f364c3b0a669315a9c43204b86e1411)TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_MASK   (0x00000002) |
| --- |

## [◆ ](#a29dad34e523db41e20a6e04630f49518)TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQENABLE\_SET\_OVF\_EN\_FLAG\_SHIFT   (1) |
| --- |

## [◆ ](#a062dc13aa47f730ae3e96c7327087ff4)TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_MASK   (0x00000004) |
| --- |

## [◆ ](#a832440567ccef54d18b992f450bfea7b)TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQENABLE\_SET\_TCAR\_EN\_FLAG\_SHIFT   (2) |
| --- |

## [◆ ](#aa8b0aad13e3bf9d9a0592a97748c0df0)TI\_DM\_TIMER\_IRQSTATUS

| #define TI\_DM\_TIMER\_IRQSTATUS   (0x28) /\* Interrupt status register \*/ |
| --- |

## [◆ ](#ab1b3b1f674bb6cfb2280de8cd961a2f8)TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_MASK   (0x00000001) |
| --- |

## [◆ ](#a6f07c56007ec7faba21303036574d9a8)TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQSTATUS\_MAT\_IT\_FLAG\_SHIFT   (0) |
| --- |

## [◆ ](#acb7221b7876ad443b10b29c509490fce)TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_MASK   (0x00000002) |
| --- |

## [◆ ](#ac456e3d253745c1392125c7d042dbca5)TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQSTATUS\_OVF\_IT\_FLAG\_SHIFT   (1) |
| --- |

## [◆ ](#aed6f6246fb153daade0cef1b8d5e9986)TI\_DM\_TIMER\_IRQSTATUS\_RAW

| #define TI\_DM\_TIMER\_IRQSTATUS\_RAW   (0x24) |
| --- |

## [◆ ](#a0e8210c88b07fee206ae521972031ca5)TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_MASK

| #define TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_MASK   (0x00000004) |
| --- |

## [◆ ](#a3c6acb16edf7747adefde2c6ceb7c6b8)TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_SHIFT

| #define TI\_DM\_TIMER\_IRQSTATUS\_TCAR\_IT\_FLAG\_SHIFT   (2) |
| --- |

## [◆ ](#abae8f0515e3c839f6591abee28b2fe2b)TI\_DM\_TIMER\_IRQWAKEEN

| #define TI\_DM\_TIMER\_IRQWAKEEN   (0x34) |
| --- |

## [◆ ](#a434e08af9ecba1079fdc48803a6050b3)TI\_DM\_TIMER\_TCAR1

| #define TI\_DM\_TIMER\_TCAR1   (0x50) |
| --- |

## [◆ ](#a8467a67685d64c8db4ed8e790da33794)TI\_DM\_TIMER\_TCAR2

| #define TI\_DM\_TIMER\_TCAR2   (0x58) |
| --- |

## [◆ ](#aeac307067f8a8bb76ad21858e73e896d)TI\_DM\_TIMER\_TCLR

| #define TI\_DM\_TIMER\_TCLR   (0x38) /\* Control register \*/ |
| --- |

## [◆ ](#a8930ee981bf263f957f03e4005de1914)TI\_DM\_TIMER\_TCLR\_AR\_MASK

| #define TI\_DM\_TIMER\_TCLR\_AR\_MASK   (0x00000002) |
| --- |

## [◆ ](#a0acc5881afa115f5cfeb30c5c9562cac)TI\_DM\_TIMER\_TCLR\_AR\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_AR\_SHIFT   (1) |
| --- |

## [◆ ](#ada8250d08e208124c42d76ccc218c5df)TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_MASK

| #define TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_MASK   (0x00002000) |
| --- |

## [◆ ](#ad2391b2472de54667863e2e528f305a5)TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_CAPT\_MODE\_SHIFT   (13) |
| --- |

## [◆ ](#a41d49ed8260dde05209ec472d9cdded7)TI\_DM\_TIMER\_TCLR\_CE\_MASK

| #define TI\_DM\_TIMER\_TCLR\_CE\_MASK   (0x00000040) |
| --- |

## [◆ ](#a8a62240a5df6a22a7f6f7f4e6e556199)TI\_DM\_TIMER\_TCLR\_CE\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_CE\_SHIFT   (6) |
| --- |

## [◆ ](#a8d5d36a375e89dc541587c6bae49a546)TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_MASK

| #define TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_MASK   (0x00004000) |
| --- |

## [◆ ](#aac119b490b0103d9487bfbedfeb00e31)TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_GPO\_CFG\_SHIFT   (14) |
| --- |

## [◆ ](#a76270082286c83d24892bb732b3ac661)TI\_DM\_TIMER\_TCLR\_PRE\_MASK

| #define TI\_DM\_TIMER\_TCLR\_PRE\_MASK   (0x00000020) |
| --- |

## [◆ ](#ad03f6e7dc83dcf000170764d49caa9e2)TI\_DM\_TIMER\_TCLR\_PRE\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_PRE\_SHIFT   (5) |
| --- |

## [◆ ](#a7dba4ee7a2a2fca79f0cef998476b176)TI\_DM\_TIMER\_TCLR\_PT\_MASK

| #define TI\_DM\_TIMER\_TCLR\_PT\_MASK   (0x00001000) |
| --- |

## [◆ ](#af7a3217343141ed60d37416e6165fac6)TI\_DM\_TIMER\_TCLR\_PT\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_PT\_SHIFT   (12) |
| --- |

## [◆ ](#a4d1e122bb953d4f6131a0af934862687)TI\_DM\_TIMER\_TCLR\_PTV\_MASK

| #define TI\_DM\_TIMER\_TCLR\_PTV\_MASK   (0x0000001c) |
| --- |

## [◆ ](#aed7a065bab0107cf992fba11be76a114)TI\_DM\_TIMER\_TCLR\_PTV\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_PTV\_SHIFT   (2) |
| --- |

## [◆ ](#a335faed7df51516361f8c71ca6cdd3d0)TI\_DM\_TIMER\_TCLR\_SCPWM\_MASK

| #define TI\_DM\_TIMER\_TCLR\_SCPWM\_MASK   (0x00000080) |
| --- |

## [◆ ](#addd64fdd8ce7aa631acb4070457ab001)TI\_DM\_TIMER\_TCLR\_SCPWM\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_SCPWM\_SHIFT   (7) |
| --- |

## [◆ ](#ab7c38741f258b57d663cba9db98bfd2b)TI\_DM\_TIMER\_TCLR\_ST\_MASK

| #define TI\_DM\_TIMER\_TCLR\_ST\_MASK   (0x00000001) |
| --- |

## [◆ ](#a89c93b281bd2b94ad65ca2be0085f101)TI\_DM\_TIMER\_TCLR\_ST\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_ST\_SHIFT   (0) |
| --- |

## [◆ ](#a401b116bdd9f2ae1ef421eab2d9a68b8)TI\_DM\_TIMER\_TCLR\_TCM\_MASK

| #define TI\_DM\_TIMER\_TCLR\_TCM\_MASK   (0x00000300) |
| --- |

## [◆ ](#a05956685e5d2e0807bdfcc624871e912)TI\_DM\_TIMER\_TCLR\_TCM\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_TCM\_SHIFT   (8) |
| --- |

## [◆ ](#a3a038b27593cbd4b46b1cc1a0ac45c16)TI\_DM\_TIMER\_TCLR\_TRG\_MASK

| #define TI\_DM\_TIMER\_TCLR\_TRG\_MASK   (0x00000c00) |
| --- |

## [◆ ](#ad6a33b765f80b62951c9c49511d4c159)TI\_DM\_TIMER\_TCLR\_TRG\_SHIFT

| #define TI\_DM\_TIMER\_TCLR\_TRG\_SHIFT   (10) |
| --- |

## [◆ ](#a3b95a3a1b84ab51e68829b8da58ec653)TI\_DM\_TIMER\_TCRR

| #define TI\_DM\_TIMER\_TCRR   (0x3c) /\* Counter register \*/ |
| --- |

## [◆ ](#a86ba1990c4c0779134849e08557db422)TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_MASK

| #define TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_MASK   (0xffffffff) |
| --- |

## [◆ ](#a0b25a9454f5b47ca438791b9fc3ea9ef)TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_SHIFT

| #define TI\_DM\_TIMER\_TCRR\_TIMER\_COUNTER\_SHIFT   (0) |
| --- |

## [◆ ](#ad0da36c4613a3c3016eee79ec6ee4182)TI\_DM\_TIMER\_TCVR

| #define TI\_DM\_TIMER\_TCVR   (0x64) |
| --- |

## [◆ ](#a1f6e7aaf701af4ae2f6c1733f583c030)TI\_DM\_TIMER\_TIDR

| #define TI\_DM\_TIMER\_TIDR   (0x00) |
| --- |

## [◆ ](#aa56da16a805b0751da5b13e1e8cf614e)TI\_DM\_TIMER\_TIOCP\_CFG

| #define TI\_DM\_TIMER\_TIOCP\_CFG   (0x10) |
| --- |

## [◆ ](#a2add6ea2a2a6b74b6441bf39f6c92104)TI\_DM\_TIMER\_TLDR

| #define TI\_DM\_TIMER\_TLDR   (0x40) /\* Load register \*/ |
| --- |

## [◆ ](#af2879252745d377777ee4237659e3299)TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_MASK

| #define TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_MASK   (0xffffffff) |
| --- |

## [◆ ](#a882d4518296c0e42c266d645399b78e8)TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_SHIFT

| #define TI\_DM\_TIMER\_TLDR\_LOAD\_VALUE\_SHIFT   (0) |
| --- |

## [◆ ](#ac1f3248a4b71e01474f95a54bd904a6f)TI\_DM\_TIMER\_TMAR

| #define TI\_DM\_TIMER\_TMAR   (0x4c) /\* Match register \*/ |
| --- |

## [◆ ](#a59820ad3de0f2118150a95de05a05fb5)TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_MASK

| #define TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_MASK   (0xffffffff) |
| --- |

## [◆ ](#a28e1f82f16738262a2984214965f83ef)TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_SHIFT

| #define TI\_DM\_TIMER\_TMAR\_COMPARE\_VALUE\_SHIFT   (0) |
| --- |

## [◆ ](#a860d9c4171c98d5f04ea3119264005ff)TI\_DM\_TIMER\_TNIR

| #define TI\_DM\_TIMER\_TNIR   (0x60) |
| --- |

## [◆ ](#a448d5710703a7693a53f26ca8607a27b)TI\_DM\_TIMER\_TOCR

| #define TI\_DM\_TIMER\_TOCR   (0x68) |
| --- |

## [◆ ](#aa8ca463e0376a2c8d8a6f595ee6eb856)TI\_DM\_TIMER\_TOWR

| #define TI\_DM\_TIMER\_TOWR   (0x6c) |
| --- |

## [◆ ](#ad7d5db65865c15fd9be2a112df6f262b)TI\_DM\_TIMER\_TPIR

| #define TI\_DM\_TIMER\_TPIR   (0x5c) |
| --- |

## [◆ ](#a61a110e410de5cf55dfe73016560fd1e)TI\_DM\_TIMER\_TSICR

| #define TI\_DM\_TIMER\_TSICR   (0x54) |
| --- |

## [◆ ](#a5a96b8379a240c79f3ace9a11df8d74e)TI\_DM\_TIMER\_TTGR

| #define TI\_DM\_TIMER\_TTGR   (0x44) |
| --- |

## [◆ ](#ada67d1b0a5a4d30f6444ad95fe6b8b92)TI\_DM\_TIMER\_TWPS

| #define TI\_DM\_TIMER\_TWPS   (0x48) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [ti\_dmtimer.h](ti__dmtimer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
