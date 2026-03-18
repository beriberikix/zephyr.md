---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp-xtensa-intmux_8h_source.html
original_path: doxygen/html/esp-xtensa-intmux_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-xtensa-intmux.h

[Go to the documentation of this file.](esp-xtensa-intmux_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_XTENSA\_INTMUX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_XTENSA\_INTMUX\_H\_

9

[ 10](esp-xtensa-intmux_8h.md#ad000d08efc3e8a5fc56da537973a5cb8)#define WIFI\_MAC\_INTR\_SOURCE 0 /\* WiFi MAC, level \*/

[ 11](esp-xtensa-intmux_8h.md#abfc935ef2963ee54b6a1f1279b4887ff)#define WIFI\_MAC\_NMI\_SOURCE 1 /\* WiFi MAC, NMI, use if MAC needs fix in NMI \*/

[ 12](esp-xtensa-intmux_8h.md#a5383f7fa77bc12a8301c54e0dfb66306)#define WIFI\_BB\_INTR\_SOURCE 2 /\* WiFi BB, level, we can do some calibration \*/

[ 13](esp-xtensa-intmux_8h.md#a0b48425e316b45db6f105daa6f2a0cff)#define BT\_MAC\_INTR\_SOURCE 3 /\* will be cancelled \*/

[ 14](esp-xtensa-intmux_8h.md#aca3a7357f242a4e91269736de6545470)#define BT\_BB\_INTR\_SOURCE 4 /\* BB, level \*/

[ 15](esp-xtensa-intmux_8h.md#ab404d2ab995f39616675330f6462dd19)#define BT\_BB\_NMI\_SOURCE 5 /\* BT BB, NMI, use if BB have bug to fix in NMI \*/

[ 16](esp-xtensa-intmux_8h.md#a14017a5bb9744f9c32138dbdcc09a786)#define RWBT\_INTR\_SOURCE 6 /\* RWBT, level \*/

[ 17](esp-xtensa-intmux_8h.md#a8cf7f44d512a2c0b215397ae4c37a4f1)#define RWBLE\_INTR\_SOURCE 7 /\* RWBLE, level \*/

[ 18](esp-xtensa-intmux_8h.md#a445a79e81929641c372257f4018127f6)#define RWBT\_NMI\_SOURCE 8 /\* RWBT, NMI, use if RWBT has bug to fix in NMI \*/

[ 19](esp-xtensa-intmux_8h.md#a3b9cef18112f398bd4ada544f3e2b5a0)#define RWBLE\_NMI\_SOURCE 9 /\* RWBLE, NMI, use if RWBT has bug to fix in NMI \*/

[ 20](esp-xtensa-intmux_8h.md#a24b7d137ebb32c58d60d5f84a3ce67db)#define SLC0\_INTR\_SOURCE 10 /\* SLC0, level \*/

[ 21](esp-xtensa-intmux_8h.md#a8d8c7fb4a7206356ef7c7b41df4c1b7b)#define SLC1\_INTR\_SOURCE 11 /\* SLC1, level \*/

[ 22](esp-xtensa-intmux_8h.md#aa714005c0707aaf1ba5b4a033bcb8f81)#define UHCI0\_INTR\_SOURCE 12 /\* UHCI0, level \*/

[ 23](esp-xtensa-intmux_8h.md#a0837c2b982c45380cd89c136d5e9fb2c)#define UHCI1\_INTR\_SOURCE 13 /\* UHCI1, level \*/

[ 24](esp-xtensa-intmux_8h.md#a22bf10410f0b99b9fe398accf66c51b1)#define TG0\_T0\_LEVEL\_INTR\_SOURCE 14 /\* TIMER\_GROUP0, TIMER0, level \*/

[ 25](esp-xtensa-intmux_8h.md#a792cd371542eb8a60e4d381b168ae2b8)#define TG0\_T1\_LEVEL\_INTR\_SOURCE 15 /\* TIMER\_GROUP0, TIMER1, level \*/

[ 26](esp-xtensa-intmux_8h.md#afc23d5890e9c8029e7d417291193a559)#define TG0\_WDT\_LEVEL\_INTR\_SOURCE 16 /\* TIMER\_GROUP0, WATCHDOG, level \*/

[ 27](esp-xtensa-intmux_8h.md#a8ab5e103356b484d48b68cbafa34d418)#define TG0\_LACT\_LEVEL\_INTR\_SOURCE 17 /\* TIMER\_GROUP0, LACT, level \*/

[ 28](esp-xtensa-intmux_8h.md#aee34beaabe47713742eb7633bd8430e3)#define TG1\_T0\_LEVEL\_INTR\_SOURCE 18 /\* TIMER\_GROUP1, TIMER0, level \*/

[ 29](esp-xtensa-intmux_8h.md#a41b4592783755438167ac4444adcaade)#define TG1\_T1\_LEVEL\_INTR\_SOURCE 19 /\* TIMER\_GROUP1, TIMER1, level \*/

[ 30](esp-xtensa-intmux_8h.md#a68616a67d062b7e57dbe6dd59151b85c)#define TG1\_WDT\_LEVEL\_INTR\_SOURCE 20 /\* TIMER\_GROUP1, WATCHDOG, level \*/

[ 31](esp-xtensa-intmux_8h.md#aa3aeef6dc970aa8c6f7aec839835a384)#define TG1\_LACT\_LEVEL\_INTR\_SOURCE 21 /\* TIMER\_GROUP1, LACT, level \*/

[ 32](esp-xtensa-intmux_8h.md#a64020d7c1f6557ef6da375f12acf68de)#define GPIO\_INTR\_SOURCE 22 /\* interrupt of GPIO, level \*/

[ 33](esp-xtensa-intmux_8h.md#a23e7de652ab586c903ec999aa8e77e4e)#define GPIO\_NMI\_SOURCE 23 /\* interrupt of GPIO, NMI \*/

[ 34](esp-xtensa-intmux_8h.md#a47c9d4be8d21b6f389993db5dbe2883d)#define FROM\_CPU\_INTR0\_SOURCE 24 /\* int0 from a CPU, level \*/

[ 35](esp-xtensa-intmux_8h.md#a2f704a24d6d56f2e13aed56e86e8fb55)#define FROM\_CPU\_INTR1\_SOURCE 25 /\* int1 from a CPU, level \*/

[ 36](esp-xtensa-intmux_8h.md#a470d4f804a7ddb5d107f1cafe8f19308)#define FROM\_CPU\_INTR2\_SOURCE 26 /\* int2 from a CPU, level, for DPORT Access \*/

[ 37](esp-xtensa-intmux_8h.md#a0b8897c96de3f23e794440ef2ef2f523)#define FROM\_CPU\_INTR3\_SOURCE 27 /\* int3 from a CPU, level, for DPORT Access \*/

[ 38](esp-xtensa-intmux_8h.md#a68709f6f268cf15d132f19f282063e4c)#define SPI0\_INTR\_SOURCE 28 /\* SPI0, level, for $ Access, do not use this \*/

[ 39](esp-xtensa-intmux_8h.md#a5779abc3d34c94cfad763d9ababebb9f)#define SPI1\_INTR\_SOURCE 29 /\* SPI1, level, flash r/w, do not use this \*/

[ 40](esp-xtensa-intmux_8h.md#ac5d10660472f10fae0d0511f254b696d)#define SPI2\_INTR\_SOURCE 30 /\* SPI2, level \*/

[ 41](esp-xtensa-intmux_8h.md#a95996e58c94e25db8b2d97de7595996f)#define SPI3\_INTR\_SOURCE 31 /\* SPI3, level \*/

[ 42](esp-xtensa-intmux_8h.md#a6d41fd98988304b2ab82785c24140f8d)#define I2S0\_INTR\_SOURCE 32 /\* I2S0, level \*/

[ 43](esp-xtensa-intmux_8h.md#a3b0877aad4fc7995be0cfb71fabb13a6)#define I2S1\_INTR\_SOURCE 33 /\* I2S1, level \*/

[ 44](esp-xtensa-intmux_8h.md#af4569e6b552e35100134e167cf11c7da)#define UART0\_INTR\_SOURCE 34 /\* UART0, level \*/

[ 45](esp-xtensa-intmux_8h.md#ad6f7d29b71a32716058033727bd01dc2)#define UART1\_INTR\_SOURCE 35 /\* UART1, level \*/

[ 46](esp-xtensa-intmux_8h.md#a4a7728c85b344ae5f62684286519f647)#define UART2\_INTR\_SOURCE 36 /\* UART2, level \*/

[ 47](esp-xtensa-intmux_8h.md#a26ce888bf67587b5ab6392f2ea0157c6)#define SDIO\_HOST\_INTR\_SOURCE 37 /\* SD/SDIO/MMC HOST, level \*/

[ 48](esp-xtensa-intmux_8h.md#a9953ad6d2f47793c28ef67a280c18ebd)#define ETH\_MAC\_INTR\_SOURCE 38 /\* ethernet mac, level \*/

[ 49](esp-xtensa-intmux_8h.md#a29ff03b184368e0a9ad6caf0cc9288ca)#define PWM0\_INTR\_SOURCE 39 /\* PWM0, level, Reserved \*/

[ 50](esp-xtensa-intmux_8h.md#ab9a0099e8acba4831c68af88a073e31d)#define PWM1\_INTR\_SOURCE 40 /\* PWM1, level, Reserved \*/

[ 51](esp-xtensa-intmux_8h.md#a04211cd6f7671713ae845e451c5b008d)#define PWM2\_INTR\_SOURCE 41 /\* PWM2, level \*/

[ 52](esp-xtensa-intmux_8h.md#a95fc4f3d268322f0c0951f188f7eff11)#define PWM3\_INTR\_SOURCE 42 /\* PWM3, level \*/

[ 53](esp-xtensa-intmux_8h.md#a296f3d252d30615dbaea32d61cba9214)#define LEDC\_INTR\_SOURCE 43 /\* LED PWM, level \*/

[ 54](esp-xtensa-intmux_8h.md#aaf244ea4b63d912e0ce8d59795c79f9d)#define EFUSE\_INTR\_SOURCE 44 /\* efuse, level, not likely to use \*/

[ 55](esp-xtensa-intmux_8h.md#a3a56673ee10a809fb2e75065d84b6f8e)#define TWAI\_INTR\_SOURCE 45 /\* twai, level \*/

[ 56](esp-xtensa-intmux_8h.md#ab61f6cd5397d79c3b654aef3585ff4a8)#define CAN\_INTR\_SOURCE TWAI\_INTR\_SOURCE

[ 57](esp-xtensa-intmux_8h.md#a80d2efc475574efe9250d0048a8a8c12)#define RTC\_CORE\_INTR\_SOURCE 46 /\* rtc core, level, include rtc watchdog \*/

[ 58](esp-xtensa-intmux_8h.md#ac6d02a2b0f009553a9e52e7842fa959d)#define RMT\_INTR\_SOURCE 47 /\* remote controller, level \*/

[ 59](esp-xtensa-intmux_8h.md#acfdc02f0268c6145e3ffd5221ce7152f)#define PCNT\_INTR\_SOURCE 48 /\* pulse count, level \*/

[ 60](esp-xtensa-intmux_8h.md#a7a706aa628e14e55247d20c9853d76a9)#define I2C\_EXT0\_INTR\_SOURCE 49 /\* I2C controller1, level \*/

[ 61](esp-xtensa-intmux_8h.md#ac0e06a214b3990cb35fa4975e2a85e8e)#define I2C\_EXT1\_INTR\_SOURCE 50 /\* I2C controller0, level \*/

[ 62](esp-xtensa-intmux_8h.md#accd4889d9e375ba16ea00489e7115c30)#define RSA\_INTR\_SOURCE 51 /\* RSA accelerator, level \*/

[ 63](esp-xtensa-intmux_8h.md#a1532868105af99387eb159c1e6e80fe5)#define SPI1\_DMA\_INTR\_SOURCE 52 /\* SPI1 DMA, for flash r/w, do not use it \*/

[ 64](esp-xtensa-intmux_8h.md#a7036cef97de80d47ffbdeff6478ccbec)#define SPI2\_DMA\_INTR\_SOURCE 53 /\* SPI2 DMA, level \*/

[ 65](esp-xtensa-intmux_8h.md#a1916307ca85215eb4c995bc4ae83eb50)#define SPI3\_DMA\_INTR\_SOURCE 54 /\* interrupt of SPI3 DMA, level \*/

[ 66](esp-xtensa-intmux_8h.md#a407bd79d5c36e715bcd21a64d8f77c04)#define WDT\_INTR\_SOURCE 55 /\* will be cancelled \*/

[ 67](esp-xtensa-intmux_8h.md#a9f5fed8c34c9b971830ab3e083316271)#define TIMER1\_INTR\_SOURCE 56 /\* will be cancelled \*/

[ 68](esp-xtensa-intmux_8h.md#a792de801f5e8339f61a381172782ee06)#define TIMER2\_INTR\_SOURCE 57 /\* will be cancelled \*/

[ 69](esp-xtensa-intmux_8h.md#a3930148480a70cd784d84618fcc6ca4d)#define TG0\_T0\_EDGE\_INTR\_SOURCE 58 /\* TIMER\_GROUP0, TIMER0, EDGE \*/

[ 70](esp-xtensa-intmux_8h.md#af32f59d8128f02c0b104adfd84a0e484)#define TG0\_T1\_EDGE\_INTR\_SOURCE 59 /\* TIMER\_GROUP0, TIMER1, EDGE \*/

[ 71](esp-xtensa-intmux_8h.md#a6f69896f6b8b308d948856e624fc8da6)#define TG0\_WDT\_EDGE\_INTR\_SOURCE 60 /\* TIMER\_GROUP0, WATCH DOG, EDGE \*/

[ 72](esp-xtensa-intmux_8h.md#aaf809080c506a114fe3b47d4d4911873)#define TG0\_LACT\_EDGE\_INTR\_SOURCE 61 /\* TIMER\_GROUP0, LACT, EDGE \*/

[ 73](esp-xtensa-intmux_8h.md#a0470cb4879bd92a67e5bd71522c79894)#define TG1\_T0\_EDGE\_INTR\_SOURCE 62 /\* TIMER\_GROUP1, TIMER0, EDGE \*/

[ 74](esp-xtensa-intmux_8h.md#a7315915335a06cbd3302b26eb5056ea1)#define TG1\_T1\_EDGE\_INTR\_SOURCE 63 /\* TIMER\_GROUP1, TIMER1, EDGE \*/

[ 75](esp-xtensa-intmux_8h.md#a53372a881097f28f5c381879ad065796)#define TG1\_WDT\_EDGE\_INTR\_SOURCE 64 /\* TIMER\_GROUP1, WATCHDOG, EDGE \*/

[ 76](esp-xtensa-intmux_8h.md#a4789654138f3c05bdf28370301971ade)#define TG1\_LACT\_EDGE\_INTR\_SOURCE 65 /\* TIMER\_GROUP0, LACT, EDGE \*/

[ 77](esp-xtensa-intmux_8h.md#ace5101394746eb3170217828730eae21)#define MMU\_IA\_INTR\_SOURCE 66 /\* MMU Invalid Access, LEVEL \*/

[ 78](esp-xtensa-intmux_8h.md#af66ad44b93cebc47323913b312f0f020)#define MPU\_IA\_INTR\_SOURCE 67 /\* MPU Invalid Access, LEVEL \*/

[ 79](esp-xtensa-intmux_8h.md#abc71e0e6d2e6ea7fc39d17297753e72e)#define CACHE\_IA\_INTR\_SOURCE 68 /\* Cache Invalid Access, LEVEL \*/

[ 80](esp-xtensa-intmux_8h.md#ad57b1f253283c9a65fd95631a11d9532)#define MAX\_INTR\_SOURCE 69 /\* total number of interrupt sources \*/

81

82#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-xtensa-intmux.h](esp-xtensa-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
