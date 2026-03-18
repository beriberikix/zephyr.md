---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp32s2-xtensa-intmux_8h_source.html
original_path: doxygen/html/esp32s2-xtensa-intmux_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2-xtensa-intmux.h

[Go to the documentation of this file.](esp32s2-xtensa-intmux_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32S2\_XTENSA\_INTMUX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32S2\_XTENSA\_INTMUX\_H\_

9

[ 10](esp32s2-xtensa-intmux_8h.md#ad000d08efc3e8a5fc56da537973a5cb8)#define WIFI\_MAC\_INTR\_SOURCE 0 /\* WiFi MAC, level \*/

[ 11](esp32s2-xtensa-intmux_8h.md#abfc935ef2963ee54b6a1f1279b4887ff)#define WIFI\_MAC\_NMI\_SOURCE 1 /\* WiFi MAC, NMI, use if MAC needs fix in NMI \*/

[ 12](esp32s2-xtensa-intmux_8h.md#af3cef5f23f39a396dec2a356f395ef69)#define WIFI\_PWR\_INTR\_SOURCE 2

[ 13](esp32s2-xtensa-intmux_8h.md#a5383f7fa77bc12a8301c54e0dfb66306)#define WIFI\_BB\_INTR\_SOURCE 3 /\* WiFi BB, level, we can do some calibration \*/

[ 14](esp32s2-xtensa-intmux_8h.md#a0b48425e316b45db6f105daa6f2a0cff)#define BT\_MAC\_INTR\_SOURCE 4 /\* will be cancelled \*/

[ 15](esp32s2-xtensa-intmux_8h.md#aca3a7357f242a4e91269736de6545470)#define BT\_BB\_INTR\_SOURCE 5 /\* BB, level \*/

[ 16](esp32s2-xtensa-intmux_8h.md#ab404d2ab995f39616675330f6462dd19)#define BT\_BB\_NMI\_SOURCE 6 /\* BT BB, NMI, use if BB have bug to fix in NMI \*/

[ 17](esp32s2-xtensa-intmux_8h.md#a14017a5bb9744f9c32138dbdcc09a786)#define RWBT\_INTR\_SOURCE 7 /\* RWBT, level \*/

[ 18](esp32s2-xtensa-intmux_8h.md#a8cf7f44d512a2c0b215397ae4c37a4f1)#define RWBLE\_INTR\_SOURCE 8 /\* RWBLE, level \*/

[ 19](esp32s2-xtensa-intmux_8h.md#a445a79e81929641c372257f4018127f6)#define RWBT\_NMI\_SOURCE 9 /\* RWBT, NMI, use if RWBT has bug to fix in NMI \*/

[ 20](esp32s2-xtensa-intmux_8h.md#a3b9cef18112f398bd4ada544f3e2b5a0)#define RWBLE\_NMI\_SOURCE 10 /\* RWBLE, NMI, use if RWBT has bug to fix in NMI \*/

[ 21](esp32s2-xtensa-intmux_8h.md#a24b7d137ebb32c58d60d5f84a3ce67db)#define SLC0\_INTR\_SOURCE 11 /\* SLC0, level \*/

[ 22](esp32s2-xtensa-intmux_8h.md#a8d8c7fb4a7206356ef7c7b41df4c1b7b)#define SLC1\_INTR\_SOURCE 12 /\* SLC1, level \*/

[ 23](esp32s2-xtensa-intmux_8h.md#aa714005c0707aaf1ba5b4a033bcb8f81)#define UHCI0\_INTR\_SOURCE 13 /\* UHCI0, level \*/

[ 24](esp32s2-xtensa-intmux_8h.md#a0837c2b982c45380cd89c136d5e9fb2c)#define UHCI1\_INTR\_SOURCE 14 /\* UHCI1, level \*/

[ 25](esp32s2-xtensa-intmux_8h.md#a22bf10410f0b99b9fe398accf66c51b1)#define TG0\_T0\_LEVEL\_INTR\_SOURCE 15 /\* TIMER\_GROUP0, TIMER0, level \*/

[ 26](esp32s2-xtensa-intmux_8h.md#a792cd371542eb8a60e4d381b168ae2b8)#define TG0\_T1\_LEVEL\_INTR\_SOURCE 16 /\* TIMER\_GROUP0, TIMER1, level \*/

[ 27](esp32s2-xtensa-intmux_8h.md#afc23d5890e9c8029e7d417291193a559)#define TG0\_WDT\_LEVEL\_INTR\_SOURCE 17 /\* TIMER\_GROUP0, WATCHDOG, level \*/

[ 28](esp32s2-xtensa-intmux_8h.md#a8ab5e103356b484d48b68cbafa34d418)#define TG0\_LACT\_LEVEL\_INTR\_SOURCE 18 /\* TIMER\_GROUP0, LACT, level \*/

[ 29](esp32s2-xtensa-intmux_8h.md#aee34beaabe47713742eb7633bd8430e3)#define TG1\_T0\_LEVEL\_INTR\_SOURCE 19 /\* TIMER\_GROUP1, TIMER0, level \*/

[ 30](esp32s2-xtensa-intmux_8h.md#a41b4592783755438167ac4444adcaade)#define TG1\_T1\_LEVEL\_INTR\_SOURCE 20 /\* TIMER\_GROUP1, TIMER1, level \*/

[ 31](esp32s2-xtensa-intmux_8h.md#a68616a67d062b7e57dbe6dd59151b85c)#define TG1\_WDT\_LEVEL\_INTR\_SOURCE 21 /\* TIMER\_GROUP1, WATCHDOG, level \*/

[ 32](esp32s2-xtensa-intmux_8h.md#aa3aeef6dc970aa8c6f7aec839835a384)#define TG1\_LACT\_LEVEL\_INTR\_SOURCE 22 /\* TIMER\_GROUP1, LACT, level \*/

[ 33](esp32s2-xtensa-intmux_8h.md#a64020d7c1f6557ef6da375f12acf68de)#define GPIO\_INTR\_SOURCE 23 /\* interrupt of GPIO, level \*/

[ 34](esp32s2-xtensa-intmux_8h.md#a23e7de652ab586c903ec999aa8e77e4e)#define GPIO\_NMI\_SOURCE 24 /\* interrupt of GPIO, NMI \*/

[ 35](esp32s2-xtensa-intmux_8h.md#afb98fcf1a9be6030f5ca87dea6675974)#define GPIO\_INTR\_SOURCE2 25 /\* interrupt of GPIO, level \*/

[ 36](esp32s2-xtensa-intmux_8h.md#ad11e04bc97a0115966929013f06efa50)#define GPIO\_NMI\_SOURCE2 26 /\* interrupt of GPIO, NMI \*/

[ 37](esp32s2-xtensa-intmux_8h.md#a5b31ad0ece8c26e3e1600837bc1121bb)#define DEDICATED\_GPIO\_INTR\_SOURCE 27 /\* interrupt of dedicated GPIO, level \*/

[ 38](esp32s2-xtensa-intmux_8h.md#a47c9d4be8d21b6f389993db5dbe2883d)#define FROM\_CPU\_INTR0\_SOURCE 28 /\* int0 from a CPU, level \*/

[ 39](esp32s2-xtensa-intmux_8h.md#a2f704a24d6d56f2e13aed56e86e8fb55)#define FROM\_CPU\_INTR1\_SOURCE 29 /\* int1 from a CPU, level \*/

[ 40](esp32s2-xtensa-intmux_8h.md#a470d4f804a7ddb5d107f1cafe8f19308)#define FROM\_CPU\_INTR2\_SOURCE 30 /\* int2 from a CPU, level, for DPORT Access \*/

[ 41](esp32s2-xtensa-intmux_8h.md#a0b8897c96de3f23e794440ef2ef2f523)#define FROM\_CPU\_INTR3\_SOURCE 31 /\* int3 from a CPU, level, for DPORT Access \*/

[ 42](esp32s2-xtensa-intmux_8h.md#a5779abc3d34c94cfad763d9ababebb9f)#define SPI1\_INTR\_SOURCE 32 /\* SPI1, level, flash r/w, do not use this \*/

[ 43](esp32s2-xtensa-intmux_8h.md#ac5d10660472f10fae0d0511f254b696d)#define SPI2\_INTR\_SOURCE 33 /\* SPI2, level \*/

[ 44](esp32s2-xtensa-intmux_8h.md#a95996e58c94e25db8b2d97de7595996f)#define SPI3\_INTR\_SOURCE 34 /\* SPI3, level \*/

[ 45](esp32s2-xtensa-intmux_8h.md#a6d41fd98988304b2ab82785c24140f8d)#define I2S0\_INTR\_SOURCE 35 /\* I2S0, level \*/

[ 46](esp32s2-xtensa-intmux_8h.md#a3b0877aad4fc7995be0cfb71fabb13a6)#define I2S1\_INTR\_SOURCE 36 /\* I2S1, level \*/

[ 47](esp32s2-xtensa-intmux_8h.md#af4569e6b552e35100134e167cf11c7da)#define UART0\_INTR\_SOURCE 37 /\* UART0, level \*/

[ 48](esp32s2-xtensa-intmux_8h.md#ad6f7d29b71a32716058033727bd01dc2)#define UART1\_INTR\_SOURCE 38 /\* UART1, level \*/

[ 49](esp32s2-xtensa-intmux_8h.md#a4a7728c85b344ae5f62684286519f647)#define UART2\_INTR\_SOURCE 39 /\* UART2, level \*/

[ 50](esp32s2-xtensa-intmux_8h.md#a26ce888bf67587b5ab6392f2ea0157c6)#define SDIO\_HOST\_INTR\_SOURCE 40 /\* SD/SDIO/MMC HOST, level \*/

[ 51](esp32s2-xtensa-intmux_8h.md#a29ff03b184368e0a9ad6caf0cc9288ca)#define PWM0\_INTR\_SOURCE 41 /\* PWM0, level, Reserved \*/

[ 52](esp32s2-xtensa-intmux_8h.md#ab9a0099e8acba4831c68af88a073e31d)#define PWM1\_INTR\_SOURCE 42 /\* PWM1, level, Reserved \*/

[ 53](esp32s2-xtensa-intmux_8h.md#a04211cd6f7671713ae845e451c5b008d)#define PWM2\_INTR\_SOURCE 43 /\* PWM2, level \*/

[ 54](esp32s2-xtensa-intmux_8h.md#a95fc4f3d268322f0c0951f188f7eff11)#define PWM3\_INTR\_SOURCE 44 /\* PWM3, level \*/

[ 55](esp32s2-xtensa-intmux_8h.md#a296f3d252d30615dbaea32d61cba9214)#define LEDC\_INTR\_SOURCE 45 /\* LED PWM, level \*/

[ 56](esp32s2-xtensa-intmux_8h.md#aaf244ea4b63d912e0ce8d59795c79f9d)#define EFUSE\_INTR\_SOURCE 46 /\* efuse, level, not likely to use \*/

[ 57](esp32s2-xtensa-intmux_8h.md#a3a56673ee10a809fb2e75065d84b6f8e)#define TWAI\_INTR\_SOURCE 47 /\* twai, level \*/

[ 58](esp32s2-xtensa-intmux_8h.md#a7a020da508049560356d36ab9607bca9)#define USB\_INTR\_SOURCE 48 /\* interrupt of USB, level \*/

[ 59](esp32s2-xtensa-intmux_8h.md#a80d2efc475574efe9250d0048a8a8c12)#define RTC\_CORE\_INTR\_SOURCE 49 /\* rtc core, level, include rtc watchdog \*/

[ 60](esp32s2-xtensa-intmux_8h.md#ac6d02a2b0f009553a9e52e7842fa959d)#define RMT\_INTR\_SOURCE 50 /\* remote controller, level \*/

[ 61](esp32s2-xtensa-intmux_8h.md#acfdc02f0268c6145e3ffd5221ce7152f)#define PCNT\_INTR\_SOURCE 51 /\* pulse count, level \*/

[ 62](esp32s2-xtensa-intmux_8h.md#a7a706aa628e14e55247d20c9853d76a9)#define I2C\_EXT0\_INTR\_SOURCE 52 /\* I2C controller1, level \*/

[ 63](esp32s2-xtensa-intmux_8h.md#ac0e06a214b3990cb35fa4975e2a85e8e)#define I2C\_EXT1\_INTR\_SOURCE 53 /\* I2C controller0, level \*/

[ 64](esp32s2-xtensa-intmux_8h.md#accd4889d9e375ba16ea00489e7115c30)#define RSA\_INTR\_SOURCE 54 /\* RSA accelerator, level \*/

[ 65](esp32s2-xtensa-intmux_8h.md#a59f92ba6a2f4b3fa9454558f37ff3e24)#define SHA\_INTR\_SOURCE 55 /\* interrupt of RSA accelerator, level \*/

[ 66](esp32s2-xtensa-intmux_8h.md#ad793803f54262a4dcf6b14140e9dc22b)#define AES\_INTR\_SOURCE 56 /\* interrupt of SHA accelerator, level \*/

[ 67](esp32s2-xtensa-intmux_8h.md#a7036cef97de80d47ffbdeff6478ccbec)#define SPI2\_DMA\_INTR\_SOURCE 57 /\* SPI2 DMA, level \*/

[ 68](esp32s2-xtensa-intmux_8h.md#a1916307ca85215eb4c995bc4ae83eb50)#define SPI3\_DMA\_INTR\_SOURCE 58 /\* interrupt of SPI3 DMA, level \*/

[ 69](esp32s2-xtensa-intmux_8h.md#a407bd79d5c36e715bcd21a64d8f77c04)#define WDT\_INTR\_SOURCE 59 /\* will be cancelled \*/

[ 70](esp32s2-xtensa-intmux_8h.md#a9f5fed8c34c9b971830ab3e083316271)#define TIMER1\_INTR\_SOURCE 60 /\* will be cancelled \*/

[ 71](esp32s2-xtensa-intmux_8h.md#a792de801f5e8339f61a381172782ee06)#define TIMER2\_INTR\_SOURCE 61 /\* will be cancelled \*/

[ 72](esp32s2-xtensa-intmux_8h.md#a3930148480a70cd784d84618fcc6ca4d)#define TG0\_T0\_EDGE\_INTR\_SOURCE 62 /\* TIMER\_GROUP0, TIMER0, EDGE \*/

[ 73](esp32s2-xtensa-intmux_8h.md#af32f59d8128f02c0b104adfd84a0e484)#define TG0\_T1\_EDGE\_INTR\_SOURCE 63 /\* TIMER\_GROUP0, TIMER1, EDGE \*/

[ 74](esp32s2-xtensa-intmux_8h.md#a6f69896f6b8b308d948856e624fc8da6)#define TG0\_WDT\_EDGE\_INTR\_SOURCE 64 /\* TIMER\_GROUP0, WATCH DOG, EDGE \*/

[ 75](esp32s2-xtensa-intmux_8h.md#aaf809080c506a114fe3b47d4d4911873)#define TG0\_LACT\_EDGE\_INTR\_SOURCE 65 /\* TIMER\_GROUP0, LACT, EDGE \*/

[ 76](esp32s2-xtensa-intmux_8h.md#a0470cb4879bd92a67e5bd71522c79894)#define TG1\_T0\_EDGE\_INTR\_SOURCE 66 /\* TIMER\_GROUP1, TIMER0, EDGE \*/

[ 77](esp32s2-xtensa-intmux_8h.md#a7315915335a06cbd3302b26eb5056ea1)#define TG1\_T1\_EDGE\_INTR\_SOURCE 67 /\* TIMER\_GROUP1, TIMER1, EDGE \*/

[ 78](esp32s2-xtensa-intmux_8h.md#a53372a881097f28f5c381879ad065796)#define TG1\_WDT\_EDGE\_INTR\_SOURCE 68 /\* TIMER\_GROUP1, WATCHDOG, EDGE \*/

[ 79](esp32s2-xtensa-intmux_8h.md#a4789654138f3c05bdf28370301971ade)#define TG1\_LACT\_EDGE\_INTR\_SOURCE 69 /\* TIMER\_GROUP0, LACT, EDGE \*/

[ 80](esp32s2-xtensa-intmux_8h.md#abc71e0e6d2e6ea7fc39d17297753e72e)#define CACHE\_IA\_INTR\_SOURCE 70 /\* Cache Invalid Access, level \*/

[ 81](esp32s2-xtensa-intmux_8h.md#a4cb07c15412c22b4939bb5a1e782f6e7)#define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE 71 /\* system timer 0, edge \*/

[ 82](esp32s2-xtensa-intmux_8h.md#a4ae5acb4be5a37cc87deb29ca61c8034)#define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE 72 /\* system timer 1, edge \*/

[ 83](esp32s2-xtensa-intmux_8h.md#a3c07aba15f9a2e9bc4a97031a241b512)#define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE 73 /\* system timer 2, edge \*/

[ 84](esp32s2-xtensa-intmux_8h.md#ab627766f8e6b851882c42596d7df540c)#define ASSIST\_DEBUG\_INTR\_SOURCE 74 /\* Assist debug module, level \*/

[ 85](esp32s2-xtensa-intmux_8h.md#aa7415869e67d460c0ed4c7e96810291a)#define PMS\_PRO\_IRAM0\_ILG\_INTR\_SOURCE 75 /\* illegal IRAM1 access, level \*/

[ 86](esp32s2-xtensa-intmux_8h.md#a7ab3b2f26d6ce8bc8f9ea83ff4c3a900)#define PMS\_PRO\_DRAM0\_ILG\_INTR\_SOURCE 76 /\* illegal DRAM0 access, level \*/

[ 87](esp32s2-xtensa-intmux_8h.md#acf9bfdff3964eeacafede5571615bdd6)#define PMS\_PRO\_DPORT\_ILG\_INTR\_SOURCE 77 /\* illegal DPORT access, level \*/

[ 88](esp32s2-xtensa-intmux_8h.md#ab4e4c60433d57d03b386d5bd9ab71370)#define PMS\_PRO\_AHB\_ILG\_INTR\_SOURCE 78 /\* illegal AHB access, level \*/

[ 89](esp32s2-xtensa-intmux_8h.md#ab2491671f5770a21823adc01763af792)#define PMS\_PRO\_CACHE\_ILG\_INTR\_SOURCE 79 /\* illegal CACHE access, level \*/

[ 90](esp32s2-xtensa-intmux_8h.md#a9c4f6388dd7312fdc4219cff984166a9)#define PMS\_DMA\_APB\_I\_ILG\_INTR\_SOURCE 80 /\* illegal APB access, level \*/

[ 91](esp32s2-xtensa-intmux_8h.md#a8d6a4e0e0994f8a55fd7ca4ce5a45399)#define PMS\_DMA\_RX\_I\_ILG\_INTR\_SOURCE 81 /\* illegal DMA RX access, level \*/

[ 92](esp32s2-xtensa-intmux_8h.md#aac17e93da6a160da2d85a43d4ddc8289)#define PMS\_DMA\_TX\_I\_ILG\_INTR\_SOURCE 82 /\* illegal DMA TX access, level \*/

[ 93](esp32s2-xtensa-intmux_8h.md#a36c488ff1605277f2772b1f80552f6ac)#define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE 83 /\* SPI0 Cache access and

[ 94](esp32s2-xtensa-intmux_8h.md#a03fc7ea80cff3be1cdf02d5f97434c71) \* SPI1 access rejected, level

[ 95](esp32s2-xtensa-intmux_8h.md#a9f521721b77fef0f3c19bea05a12e850) \*/

[ 96](esp32s2-xtensa-intmux_8h.md#a334a2d6fa713f6df7c46c96465a2d6b9)#define DMA\_COPY\_INTR\_SOURCE 84 /\* DMA copy, level \*/

[ 97](esp32s2-xtensa-intmux_8h.md#a344601acd9e077b22b5f2d2627d9032e)#define SPI4\_DMA\_INTR\_SOURCE 85 /\* SPI4 DMA, level \*/

[ 98](esp32s2-xtensa-intmux_8h.md#adecb822591c0c4bf063d67b2e74e9a40)#define SPI4\_INTR\_SOURCE 86 /\* SPI4, level \*/

[ 99](esp32s2-xtensa-intmux_8h.md#a68b408eb63057838c64c51718c5b1f7f)#define ICACHE\_PRELOAD\_INTR\_SOURCE 87 /\* ICache preload operation, level \*/

[ 100](esp32s2-xtensa-intmux_8h.md#ad81b659cea69558a9accb6cd9315b236)#define DCACHE\_PRELOAD\_INTR\_SOURCE 88 /\* DCache preload operation, level \*/

[ 101](esp32s2-xtensa-intmux_8h.md#a1334dc20d35277646113e699619d8856)#define APB\_ADC\_INTR\_SOURCE 89 /\* APB ADC, level \*/

[ 102](esp32s2-xtensa-intmux_8h.md#aefeb2487d77e00408d4b7f2faa4f840f)#define CRYPTO\_DMA\_INTR\_SOURCE 90 /\* encrypted DMA, level \*/

[ 103](esp32s2-xtensa-intmux_8h.md#a93a4db93be7bef5cdc22cc2854da84b6)#define CPU\_PERI\_ERROR\_INTR\_SOURCE 91 /\* CPU peripherals error, level \*/

[ 104](esp32s2-xtensa-intmux_8h.md#a8299c36b90f9e08bc421e527f69545bb)#define APB\_PERI\_ERROR\_INTR\_SOURCE 92 /\* APB peripherals error, level \*/

[ 105](esp32s2-xtensa-intmux_8h.md#ad57b1f253283c9a65fd95631a11d9532)#define DCACHE\_SYNC\_INTR\_SOURCE 93 /\* data cache sync done, level \*/

106#define ICACHE\_SYNC\_INTR\_SOURCE 94 /\* instruction cache sync done, level \*/

107#define MAX\_INTR\_SOURCE 95 /\* total number of interrupt sources \*/

108

109#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp32s2-xtensa-intmux.h](esp32s2-xtensa-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
