---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/clock__agilex__ll_8h.html
original_path: doxygen/html/clock__agilex__ll_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_agilex\_ll.h File Reference

`#include <socfpga_handoff.h>`

[Go to the source code of this file.](clock__agilex__ll_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CLKMGR\_OFFSET](#a7ce2e6aec96ecc51999e93153e45c437)   0xffd10000 |
| #define | [CLKMGR\_CTRL](#af5d589d3674dd3ab4092a1b8fc54c36e)   0x0 |
| #define | [CLKMGR\_STAT](#a7aa1ea6315cdfba9836596bdd9330d6f)   0x4 |
| #define | [CLKMGR\_INTRCLR](#a0b70ada815bf2d1165e09c01d341b13d)   0x14 |
| #define | [CLKMGR\_MAINPLL](#aa6f1c676b1fd193c48c0aaf7554b2d6e)   0xffd10024 |
| #define | [CLKMGR\_MAINPLL\_EN](#af4f0772c563c9016457459e623681ffe)   0x0 |
| #define | [CLKMGR\_MAINPLL\_BYPASS](#a4a8e8063880880a26f938675bb6af59b)   0xc |
| #define | [CLKMGR\_MAINPLL\_MPUCLK](#a87ea7de8d3625861d119d7b9e17b72b1)   0x18 |
| #define | [CLKMGR\_MAINPLL\_NOCCLK](#a7e31fed5050598f8944186b387d738ba)   0x1c |
| #define | [CLKMGR\_MAINPLL\_NOCDIV](#a5dea9faa03275b82f29cc03bb7a82998)   0x20 |
| #define | [CLKMGR\_MAINPLL\_PLLGLOB](#a86db445343ab57a0c7d7650bd3a5d727)   0x24 |
| #define | [CLKMGR\_MAINPLL\_FDBCK](#a585119c5c27cf0b02b925cfca929c1a4)   0x28 |
| #define | [CLKMGR\_MAINPLL\_MEM](#a44c3eb51a678369d368f5def509ec098)   0x2c |
| #define | [CLKMGR\_MAINPLL\_MEMSTAT](#add31f35ee1f5d3c75324143fd9d91e2a)   0x30 |
| #define | [CLKMGR\_MAINPLL\_PLLC0](#ab09e3ec031a2f074172e165ac5928aa7)   0x34 |
| #define | [CLKMGR\_MAINPLL\_PLLC1](#aaf0a5fa071ee92ce4de423ac44984e36)   0x38 |
| #define | [CLKMGR\_MAINPLL\_VCOCALIB](#a4a3459c7a5d1df04882a8cf21b477629)   0x3c |
| #define | [CLKMGR\_MAINPLL\_PLLC2](#a5149cc7c7323438b9660608329cafb18)   0x40 |
| #define | [CLKMGR\_MAINPLL\_PLLC3](#a3ce82fe6e2087d5c46b75c4ccc44ac9d)   0x44 |
| #define | [CLKMGR\_MAINPLL\_PLLM](#af354805596754d304bc54ca0e75306c0)   0x48 |
| #define | [CLKMGR\_MAINPLL\_LOSTLOCK](#ad18f16daf2a4ce5e628f16a829097d61)   0x54 |
| #define | [CLKMGR\_PERPLL](#abffd6d11b10b59f792c74bd292778d97)   0xffd1007c |
| #define | [CLKMGR\_PERPLL\_EN](#aca57ee95281d79ae0429fbfe29a116f5)   0x0 |
| #define | [CLKMGR\_PERPLL\_BYPASS](#afa44f1602dd9a119077821a57a9639ec)   0xc |
| #define | [CLKMGR\_PERPLL\_EMACCTL](#a61ed24c0d6e3cd458bbcfec8a67acc34)   0x18 |
| #define | [CLKMGR\_PERPLL\_GPIODIV](#aa9e9981aa179f50973776374b83eee45)   0x1c |
| #define | [CLKMGR\_PERPLL\_PLLGLOB](#a5c5113dd9047084667ad3b6c48c9b059)   0x20 |
| #define | [CLKMGR\_PERPLL\_FDBCK](#af03410c71da48d28ade194581b655aba)   0x24 |
| #define | [CLKMGR\_PERPLL\_MEM](#a9a704394b4a7706895cc5bd3327d9b1e)   0x28 |
| #define | [CLKMGR\_PERPLL\_MEMSTAT](#ad8e83a05ecaa545e5c8d7cc4fd13b12c)   0x2c |
| #define | [CLKMGR\_PERPLL\_PLLC0](#a94f5888bfcec5a4a04df8226defc56a1)   0x30 |
| #define | [CLKMGR\_PERPLL\_PLLC1](#affe47567111a1959d4b060a171411811)   0x34 |
| #define | [CLKMGR\_PERPLL\_VCOCALIB](#a83c322b74ee05528ffbe9434bcf52067)   0x38 |
| #define | [CLKMGR\_PERPLL\_PLLC2](#a9cac40abca09e28cac234e92ca2de7fc)   0x3c |
| #define | [CLKMGR\_PERPLL\_PLLC3](#a8f386922aae4a7c70359302b7b044b27)   0x40 |
| #define | [CLKMGR\_PERPLL\_PLLM](#a8334e2e3d21ff2d36fa4d744d68b9a70)   0x44 |
| #define | [CLKMGR\_PERPLL\_LOSTLOCK](#a05fb71dae6c53fd336c3ae792f51eb25)   0x50 |
| #define | [CLKMGR\_ALTERA](#a2fb528b9c63cb22806e89265a0ea5f67)   0xffd100d0 |
| #define | [CLKMGR\_ALTERA\_JTAG](#a99f91779ac440853879974133e2a18d9)   0x0 |
| #define | [CLKMGR\_ALTERA\_EMACACTR](#a2e37d7f74049fd3203370d67f97f0d1b)   0x4 |
| #define | [CLKMGR\_ALTERA\_EMACBCTR](#a478ee107d6162910a8508c95de702672)   0x8 |
| #define | [CLKMGR\_ALTERA\_EMACPTPCTR](#a348269b9667529877e138fe85b45453f)   0xc |
| #define | [CLKMGR\_ALTERA\_GPIODBCTR](#a938138d6369d0f84d4c0ca350aec33aa)   0x10 |
| #define | [CLKMGR\_ALTERA\_SDMMCCTR](#a5877bdb7b50181bdd08956cb81b89878)   0x14 |
| #define | [CLKMGR\_ALTERA\_S2FUSER0CTR](#ad66a4e5eedaee77dd554601bc9e0700e)   0x18 |
| #define | [CLKMGR\_ALTERA\_S2FUSER1CTR](#a3855729ea087e571004c7fff1e718a9e)   0x1c |
| #define | [CLKMGR\_ALTERA\_PSIREFCTR](#a31f2df94d9b2cc020d4abab3b0152007)   0x20 |
| #define | [CLKMGR\_ALTERA\_EXTCNTRST](#ae13120d546f6efecbbd0b13bf68e6324)   0x24 |
| #define | [CLKMGR\_MEM\_REQ](#a983bee0c9f469bc77fa1725c4bb481be)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CLKMGR\_MEM\_WR](#a92722915ca5ab507ebc3849fc45271bf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CLKMGR\_MEM\_ERR](#a185c1b42f6b54f1bf77727957a1e34b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| #define | [CLKMGR\_MEM\_WDAT\_OFFSET](#ac771635c52ff366a2b083b5d86a36a68)   16 |
| #define | [CLKMGR\_MEM\_ADDR](#a8f4fd8cb47546aa1217472c18b65ec2a)   0x4027 |
| #define | [CLKMGR\_MEM\_WDAT](#a466aa1fc4ffacf0494df00dcb43cae63)   0x80 |
| #define | [CLKMGR\_CTRL\_BOOTMODE\_SET\_MSK](#ab78537c12a99cc485ccceab8ff661145)   0x00000001 |
| #define | [CLKMGR\_STAT\_BUSY\_E\_BUSY](#ae0c120f58b7c7c672b432d1550bd5f49)   0x1 |
| #define | [CLKMGR\_STAT\_BUSY](#a49b947aba126c7dfc0c32145c8ba3b13)(x) |
| #define | [CLKMGR\_STAT\_MAINPLLLOCKED](#a631937c42d864f312399859fdf09d895)(x) |
| #define | [CLKMGR\_STAT\_PERPLLLOCKED](#ac09c2acac5dce5da3f333c603393f9d9)(x) |
| #define | [CLKMGR\_INTRCLR\_MAINLOCKLOST\_SET\_MSK](#ac51105f17860589a1222c91d633c3e14)   0x00000004 |
| #define | [CLKMGR\_INTRCLR\_PERLOCKLOST\_SET\_MSK](#a90cba4544b7ff82fe03faa9659e69cc1)   0x00000008 |
| #define | [CLKMGR\_INTOSC\_HZ](#a7901ba453bc5083e5b71108051cd53aa)   460000000 |
| #define | [CLKMGR\_MAINPLL\_EN\_RESET](#ae6382ca96b72dc2169219c092428d522)   0x000000ff |
| #define | [CLKMGR\_PERPLL\_EN\_RESET](#a0efbebef5965f0fdc2fefa4336aeca0f)   0x00000fff |
| #define | [CLKMGR\_PERPLL\_EN\_SDMMCCLK](#abed91c06356654901088ca6d64b46b41)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CLKMGR\_PERPLL\_GPIODIV\_GPIODBCLK\_SET](#a1a8ce17cc92e9c8a55ed5a56c79183df)(x) |
| #define | [CLKMGR\_ALTERA\_EXTCNTRST\_RESET](#a1b0ef45bf5d6403362a4c0579b7221c3)   0xff |
| #define | [CLKMGR\_PSRC](#ab8dcd2c21c183c097b74a8b2c5974b73)(x) |
| #define | [CLKMGR\_PSRC\_MAIN](#a52626e2d7ad13fc2ad32d0ee9b5bd048)   0 |
| #define | [CLKMGR\_PSRC\_PER](#a7101c2e1996f4adee854745ff9feb938)   1 |
| #define | [CLKMGR\_PLLGLOB\_PSRC\_EOSC1](#a1e26c5032c40ffe903109e23aae95170)   0x0 |
| #define | [CLKMGR\_PLLGLOB\_PSRC\_INTOSC](#a55457cdf91596fab57fe5016898dd66f)   0x1 |
| #define | [CLKMGR\_PLLGLOB\_PSRC\_F2S](#acd3529f6d4fe0298ac156e80b1e2e9c3)   0x2 |
| #define | [CLKMGR\_PLLM\_MDIV](#ab39e427e438e5a994573bc8df4400727)(x) |
| #define | [CLKMGR\_PLLGLOB\_PD\_SET\_MSK](#a3fb498116d432701d280e503200559a2)   0x00000001 |
| #define | [CLKMGR\_PLLGLOB\_RST\_SET\_MSK](#a8413bbfbee567a7dfec2bf7c82b663d4)   0x00000002 |
| #define | [CLKMGR\_PLLGLOB\_REFCLKDIV](#af6208d347c28b5688f4a6caefe3eced7)(x) |
| #define | [CLKMGR\_PLLGLOB\_AREFCLKDIV](#a1da55c1bbb0e133afe769e0e9f3be5d7)(x) |
| #define | [CLKMGR\_PLLGLOB\_DREFCLKDIV](#ad9bdc9e849335224cd4449c3e45a5779)(x) |
| #define | [CLKMGR\_VCOCALIB\_HSCNT\_SET](#a818647eff6b91c033efc41c2022bf16b)(x) |
| #define | [CLKMGR\_VCOCALIB\_MSCNT\_SET](#a054daafab40b9f41a2269eadaea78e05)(x) |
| #define | [CLKMGR\_CLR\_LOSTLOCK\_BYPASS](#af6457691c9e7ed5014fadad1fb36a6fb)   0x20000000 |

| Functions | |
| --- | --- |
| void | [config\_clkmgr\_handoff](#acbc7941cdcb96d94336aef1649fdd4e9) (struct handoff \*hoff\_ptr) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [get\_mpu\_clk](#ad2b025eee2ac7f5ac5f49c004d1f66e9) (void) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [get\_wdt\_clk](#a223981ca09133eb12a2be066426be7bd) (void) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [get\_uart\_clk](#a15c79941c9f9622bb453349dc1b965a6) (void) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [get\_mmc\_clk](#afa5f97189dc639da0859fe027c0af4ee) (void) |

## Macro Definition Documentation

## [◆ ](#a2fb528b9c63cb22806e89265a0ea5f67)CLKMGR\_ALTERA

| #define CLKMGR\_ALTERA   0xffd100d0 |
| --- |

## [◆ ](#a2e37d7f74049fd3203370d67f97f0d1b)CLKMGR\_ALTERA\_EMACACTR

| #define CLKMGR\_ALTERA\_EMACACTR   0x4 |
| --- |

## [◆ ](#a478ee107d6162910a8508c95de702672)CLKMGR\_ALTERA\_EMACBCTR

| #define CLKMGR\_ALTERA\_EMACBCTR   0x8 |
| --- |

## [◆ ](#a348269b9667529877e138fe85b45453f)CLKMGR\_ALTERA\_EMACPTPCTR

| #define CLKMGR\_ALTERA\_EMACPTPCTR   0xc |
| --- |

## [◆ ](#ae13120d546f6efecbbd0b13bf68e6324)CLKMGR\_ALTERA\_EXTCNTRST

| #define CLKMGR\_ALTERA\_EXTCNTRST   0x24 |
| --- |

## [◆ ](#a1b0ef45bf5d6403362a4c0579b7221c3)CLKMGR\_ALTERA\_EXTCNTRST\_RESET

| #define CLKMGR\_ALTERA\_EXTCNTRST\_RESET   0xff |
| --- |

## [◆ ](#a938138d6369d0f84d4c0ca350aec33aa)CLKMGR\_ALTERA\_GPIODBCTR

| #define CLKMGR\_ALTERA\_GPIODBCTR   0x10 |
| --- |

## [◆ ](#a99f91779ac440853879974133e2a18d9)CLKMGR\_ALTERA\_JTAG

| #define CLKMGR\_ALTERA\_JTAG   0x0 |
| --- |

## [◆ ](#a31f2df94d9b2cc020d4abab3b0152007)CLKMGR\_ALTERA\_PSIREFCTR

| #define CLKMGR\_ALTERA\_PSIREFCTR   0x20 |
| --- |

## [◆ ](#ad66a4e5eedaee77dd554601bc9e0700e)CLKMGR\_ALTERA\_S2FUSER0CTR

| #define CLKMGR\_ALTERA\_S2FUSER0CTR   0x18 |
| --- |

## [◆ ](#a3855729ea087e571004c7fff1e718a9e)CLKMGR\_ALTERA\_S2FUSER1CTR

| #define CLKMGR\_ALTERA\_S2FUSER1CTR   0x1c |
| --- |

## [◆ ](#a5877bdb7b50181bdd08956cb81b89878)CLKMGR\_ALTERA\_SDMMCCTR

| #define CLKMGR\_ALTERA\_SDMMCCTR   0x14 |
| --- |

## [◆ ](#af6457691c9e7ed5014fadad1fb36a6fb)CLKMGR\_CLR\_LOSTLOCK\_BYPASS

| #define CLKMGR\_CLR\_LOSTLOCK\_BYPASS   0x20000000 |
| --- |

## [◆ ](#af5d589d3674dd3ab4092a1b8fc54c36e)CLKMGR\_CTRL

| #define CLKMGR\_CTRL   0x0 |
| --- |

## [◆ ](#ab78537c12a99cc485ccceab8ff661145)CLKMGR\_CTRL\_BOOTMODE\_SET\_MSK

| #define CLKMGR\_CTRL\_BOOTMODE\_SET\_MSK   0x00000001 |
| --- |

## [◆ ](#a7901ba453bc5083e5b71108051cd53aa)CLKMGR\_INTOSC\_HZ

| #define CLKMGR\_INTOSC\_HZ   460000000 |
| --- |

## [◆ ](#a0b70ada815bf2d1165e09c01d341b13d)CLKMGR\_INTRCLR

| #define CLKMGR\_INTRCLR   0x14 |
| --- |

## [◆ ](#ac51105f17860589a1222c91d633c3e14)CLKMGR\_INTRCLR\_MAINLOCKLOST\_SET\_MSK

| #define CLKMGR\_INTRCLR\_MAINLOCKLOST\_SET\_MSK   0x00000004 |
| --- |

## [◆ ](#a90cba4544b7ff82fe03faa9659e69cc1)CLKMGR\_INTRCLR\_PERLOCKLOST\_SET\_MSK

| #define CLKMGR\_INTRCLR\_PERLOCKLOST\_SET\_MSK   0x00000008 |
| --- |

## [◆ ](#aa6f1c676b1fd193c48c0aaf7554b2d6e)CLKMGR\_MAINPLL

| #define CLKMGR\_MAINPLL   0xffd10024 |
| --- |

## [◆ ](#a4a8e8063880880a26f938675bb6af59b)CLKMGR\_MAINPLL\_BYPASS

| #define CLKMGR\_MAINPLL\_BYPASS   0xc |
| --- |

## [◆ ](#af4f0772c563c9016457459e623681ffe)CLKMGR\_MAINPLL\_EN

| #define CLKMGR\_MAINPLL\_EN   0x0 |
| --- |

## [◆ ](#ae6382ca96b72dc2169219c092428d522)CLKMGR\_MAINPLL\_EN\_RESET

| #define CLKMGR\_MAINPLL\_EN\_RESET   0x000000ff |
| --- |

## [◆ ](#a585119c5c27cf0b02b925cfca929c1a4)CLKMGR\_MAINPLL\_FDBCK

| #define CLKMGR\_MAINPLL\_FDBCK   0x28 |
| --- |

## [◆ ](#ad18f16daf2a4ce5e628f16a829097d61)CLKMGR\_MAINPLL\_LOSTLOCK

| #define CLKMGR\_MAINPLL\_LOSTLOCK   0x54 |
| --- |

## [◆ ](#a44c3eb51a678369d368f5def509ec098)CLKMGR\_MAINPLL\_MEM

| #define CLKMGR\_MAINPLL\_MEM   0x2c |
| --- |

## [◆ ](#add31f35ee1f5d3c75324143fd9d91e2a)CLKMGR\_MAINPLL\_MEMSTAT

| #define CLKMGR\_MAINPLL\_MEMSTAT   0x30 |
| --- |

## [◆ ](#a87ea7de8d3625861d119d7b9e17b72b1)CLKMGR\_MAINPLL\_MPUCLK

| #define CLKMGR\_MAINPLL\_MPUCLK   0x18 |
| --- |

## [◆ ](#a7e31fed5050598f8944186b387d738ba)CLKMGR\_MAINPLL\_NOCCLK

| #define CLKMGR\_MAINPLL\_NOCCLK   0x1c |
| --- |

## [◆ ](#a5dea9faa03275b82f29cc03bb7a82998)CLKMGR\_MAINPLL\_NOCDIV

| #define CLKMGR\_MAINPLL\_NOCDIV   0x20 |
| --- |

## [◆ ](#ab09e3ec031a2f074172e165ac5928aa7)CLKMGR\_MAINPLL\_PLLC0

| #define CLKMGR\_MAINPLL\_PLLC0   0x34 |
| --- |

## [◆ ](#aaf0a5fa071ee92ce4de423ac44984e36)CLKMGR\_MAINPLL\_PLLC1

| #define CLKMGR\_MAINPLL\_PLLC1   0x38 |
| --- |

## [◆ ](#a5149cc7c7323438b9660608329cafb18)CLKMGR\_MAINPLL\_PLLC2

| #define CLKMGR\_MAINPLL\_PLLC2   0x40 |
| --- |

## [◆ ](#a3ce82fe6e2087d5c46b75c4ccc44ac9d)CLKMGR\_MAINPLL\_PLLC3

| #define CLKMGR\_MAINPLL\_PLLC3   0x44 |
| --- |

## [◆ ](#a86db445343ab57a0c7d7650bd3a5d727)CLKMGR\_MAINPLL\_PLLGLOB

| #define CLKMGR\_MAINPLL\_PLLGLOB   0x24 |
| --- |

## [◆ ](#af354805596754d304bc54ca0e75306c0)CLKMGR\_MAINPLL\_PLLM

| #define CLKMGR\_MAINPLL\_PLLM   0x48 |
| --- |

## [◆ ](#a4a3459c7a5d1df04882a8cf21b477629)CLKMGR\_MAINPLL\_VCOCALIB

| #define CLKMGR\_MAINPLL\_VCOCALIB   0x3c |
| --- |

## [◆ ](#a8f4fd8cb47546aa1217472c18b65ec2a)CLKMGR\_MEM\_ADDR

| #define CLKMGR\_MEM\_ADDR   0x4027 |
| --- |

## [◆ ](#a185c1b42f6b54f1bf77727957a1e34b0)CLKMGR\_MEM\_ERR

| #define CLKMGR\_MEM\_ERR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| --- |

## [◆ ](#a983bee0c9f469bc77fa1725c4bb481be)CLKMGR\_MEM\_REQ

| #define CLKMGR\_MEM\_REQ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#a466aa1fc4ffacf0494df00dcb43cae63)CLKMGR\_MEM\_WDAT

| #define CLKMGR\_MEM\_WDAT   0x80 |
| --- |

## [◆ ](#ac771635c52ff366a2b083b5d86a36a68)CLKMGR\_MEM\_WDAT\_OFFSET

| #define CLKMGR\_MEM\_WDAT\_OFFSET   16 |
| --- |

## [◆ ](#a92722915ca5ab507ebc3849fc45271bf)CLKMGR\_MEM\_WR

| #define CLKMGR\_MEM\_WR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#a7ce2e6aec96ecc51999e93153e45c437)CLKMGR\_OFFSET

| #define CLKMGR\_OFFSET   0xffd10000 |
| --- |

## [◆ ](#abffd6d11b10b59f792c74bd292778d97)CLKMGR\_PERPLL

| #define CLKMGR\_PERPLL   0xffd1007c |
| --- |

## [◆ ](#afa44f1602dd9a119077821a57a9639ec)CLKMGR\_PERPLL\_BYPASS

| #define CLKMGR\_PERPLL\_BYPASS   0xc |
| --- |

## [◆ ](#a61ed24c0d6e3cd458bbcfec8a67acc34)CLKMGR\_PERPLL\_EMACCTL

| #define CLKMGR\_PERPLL\_EMACCTL   0x18 |
| --- |

## [◆ ](#aca57ee95281d79ae0429fbfe29a116f5)CLKMGR\_PERPLL\_EN

| #define CLKMGR\_PERPLL\_EN   0x0 |
| --- |

## [◆ ](#a0efbebef5965f0fdc2fefa4336aeca0f)CLKMGR\_PERPLL\_EN\_RESET

| #define CLKMGR\_PERPLL\_EN\_RESET   0x00000fff |
| --- |

## [◆ ](#abed91c06356654901088ca6d64b46b41)CLKMGR\_PERPLL\_EN\_SDMMCCLK

| #define CLKMGR\_PERPLL\_EN\_SDMMCCLK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#af03410c71da48d28ade194581b655aba)CLKMGR\_PERPLL\_FDBCK

| #define CLKMGR\_PERPLL\_FDBCK   0x24 |
| --- |

## [◆ ](#aa9e9981aa179f50973776374b83eee45)CLKMGR\_PERPLL\_GPIODIV

| #define CLKMGR\_PERPLL\_GPIODIV   0x1c |
| --- |

## [◆ ](#a1a8ce17cc92e9c8a55ed5a56c79183df)CLKMGR\_PERPLL\_GPIODIV\_GPIODBCLK\_SET

| #define CLKMGR\_PERPLL\_GPIODIV\_GPIODBCLK\_SET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) << 0) & 0x0000ffff)

## [◆ ](#a05fb71dae6c53fd336c3ae792f51eb25)CLKMGR\_PERPLL\_LOSTLOCK

| #define CLKMGR\_PERPLL\_LOSTLOCK   0x50 |
| --- |

## [◆ ](#a9a704394b4a7706895cc5bd3327d9b1e)CLKMGR\_PERPLL\_MEM

| #define CLKMGR\_PERPLL\_MEM   0x28 |
| --- |

## [◆ ](#ad8e83a05ecaa545e5c8d7cc4fd13b12c)CLKMGR\_PERPLL\_MEMSTAT

| #define CLKMGR\_PERPLL\_MEMSTAT   0x2c |
| --- |

## [◆ ](#a94f5888bfcec5a4a04df8226defc56a1)CLKMGR\_PERPLL\_PLLC0

| #define CLKMGR\_PERPLL\_PLLC0   0x30 |
| --- |

## [◆ ](#affe47567111a1959d4b060a171411811)CLKMGR\_PERPLL\_PLLC1

| #define CLKMGR\_PERPLL\_PLLC1   0x34 |
| --- |

## [◆ ](#a9cac40abca09e28cac234e92ca2de7fc)CLKMGR\_PERPLL\_PLLC2

| #define CLKMGR\_PERPLL\_PLLC2   0x3c |
| --- |

## [◆ ](#a8f386922aae4a7c70359302b7b044b27)CLKMGR\_PERPLL\_PLLC3

| #define CLKMGR\_PERPLL\_PLLC3   0x40 |
| --- |

## [◆ ](#a5c5113dd9047084667ad3b6c48c9b059)CLKMGR\_PERPLL\_PLLGLOB

| #define CLKMGR\_PERPLL\_PLLGLOB   0x20 |
| --- |

## [◆ ](#a8334e2e3d21ff2d36fa4d744d68b9a70)CLKMGR\_PERPLL\_PLLM

| #define CLKMGR\_PERPLL\_PLLM   0x44 |
| --- |

## [◆ ](#a83c322b74ee05528ffbe9434bcf52067)CLKMGR\_PERPLL\_VCOCALIB

| #define CLKMGR\_PERPLL\_VCOCALIB   0x38 |
| --- |

## [◆ ](#a1da55c1bbb0e133afe769e0e9f3be5d7)CLKMGR\_PLLGLOB\_AREFCLKDIV

| #define CLKMGR\_PLLGLOB\_AREFCLKDIV | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00000f00) >> 8)

## [◆ ](#ad9bdc9e849335224cd4449c3e45a5779)CLKMGR\_PLLGLOB\_DREFCLKDIV

| #define CLKMGR\_PLLGLOB\_DREFCLKDIV | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00003000) >> 12)

## [◆ ](#a3fb498116d432701d280e503200559a2)CLKMGR\_PLLGLOB\_PD\_SET\_MSK

| #define CLKMGR\_PLLGLOB\_PD\_SET\_MSK   0x00000001 |
| --- |

## [◆ ](#a1e26c5032c40ffe903109e23aae95170)CLKMGR\_PLLGLOB\_PSRC\_EOSC1

| #define CLKMGR\_PLLGLOB\_PSRC\_EOSC1   0x0 |
| --- |

## [◆ ](#acd3529f6d4fe0298ac156e80b1e2e9c3)CLKMGR\_PLLGLOB\_PSRC\_F2S

| #define CLKMGR\_PLLGLOB\_PSRC\_F2S   0x2 |
| --- |

## [◆ ](#a55457cdf91596fab57fe5016898dd66f)CLKMGR\_PLLGLOB\_PSRC\_INTOSC

| #define CLKMGR\_PLLGLOB\_PSRC\_INTOSC   0x1 |
| --- |

## [◆ ](#af6208d347c28b5688f4a6caefe3eced7)CLKMGR\_PLLGLOB\_REFCLKDIV

| #define CLKMGR\_PLLGLOB\_REFCLKDIV | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00003f00) >> 8)

## [◆ ](#a8413bbfbee567a7dfec2bf7c82b663d4)CLKMGR\_PLLGLOB\_RST\_SET\_MSK

| #define CLKMGR\_PLLGLOB\_RST\_SET\_MSK   0x00000002 |
| --- |

## [◆ ](#ab39e427e438e5a994573bc8df4400727)CLKMGR\_PLLM\_MDIV

| #define CLKMGR\_PLLM\_MDIV | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & 0x000003ff)

## [◆ ](#ab8dcd2c21c183c097b74a8b2c5974b73)CLKMGR\_PSRC

| #define CLKMGR\_PSRC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00030000) >> 16)

## [◆ ](#a52626e2d7ad13fc2ad32d0ee9b5bd048)CLKMGR\_PSRC\_MAIN

| #define CLKMGR\_PSRC\_MAIN   0 |
| --- |

## [◆ ](#a7101c2e1996f4adee854745ff9feb938)CLKMGR\_PSRC\_PER

| #define CLKMGR\_PSRC\_PER   1 |
| --- |

## [◆ ](#a7aa1ea6315cdfba9836596bdd9330d6f)CLKMGR\_STAT

| #define CLKMGR\_STAT   0x4 |
| --- |

## [◆ ](#a49b947aba126c7dfc0c32145c8ba3b13)CLKMGR\_STAT\_BUSY

| #define CLKMGR\_STAT\_BUSY | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00000001) >> 0)

## [◆ ](#ae0c120f58b7c7c672b432d1550bd5f49)CLKMGR\_STAT\_BUSY\_E\_BUSY

| #define CLKMGR\_STAT\_BUSY\_E\_BUSY   0x1 |
| --- |

## [◆ ](#a631937c42d864f312399859fdf09d895)CLKMGR\_STAT\_MAINPLLLOCKED

| #define CLKMGR\_STAT\_MAINPLLLOCKED | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00000100) >> 8)

## [◆ ](#ac09c2acac5dce5da3f333c603393f9d9)CLKMGR\_STAT\_PERPLLLOCKED

| #define CLKMGR\_STAT\_PERPLLLOCKED | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & 0x00010000) >> 16)

## [◆ ](#a818647eff6b91c033efc41c2022bf16b)CLKMGR\_VCOCALIB\_HSCNT\_SET

| #define CLKMGR\_VCOCALIB\_HSCNT\_SET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) << 0) & 0x000003ff)

## [◆ ](#a054daafab40b9f41a2269eadaea78e05)CLKMGR\_VCOCALIB\_MSCNT\_SET

| #define CLKMGR\_VCOCALIB\_MSCNT\_SET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) << 16) & 0x00ff0000)

## Function Documentation

## [◆ ](#acbc7941cdcb96d94336aef1649fdd4e9)config\_clkmgr\_handoff()

| void config\_clkmgr\_handoff | ( | struct handoff \* | *hoff\_ptr* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#afa5f97189dc639da0859fe027c0af4ee)get\_mmc\_clk()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) get\_mmc\_clk | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad2b025eee2ac7f5ac5f49c004d1f66e9)get\_mpu\_clk()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) get\_mpu\_clk | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a15c79941c9f9622bb453349dc1b965a6)get\_uart\_clk()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) get\_uart\_clk | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a223981ca09133eb12a2be066426be7bd)get\_wdt\_clk()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) get\_wdt\_clk | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_agilex\_ll.h](clock__agilex__ll_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
