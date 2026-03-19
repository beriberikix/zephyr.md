---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp32s3-xtensa-intmux_8h_source.html
original_path: doxygen/html/esp32s3-xtensa-intmux_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s3-xtensa-intmux.h

[Go to the documentation of this file.](esp32s3-xtensa-intmux_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32S3\_XTENSA\_INTMUX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32S3\_XTENSA\_INTMUX\_H\_

9

[ 10](esp32s3-xtensa-intmux_8h.md#ad000d08efc3e8a5fc56da537973a5cb8)#define WIFI\_MAC\_INTR\_SOURCE 0 /\* interrupt of WiFi MAC, level\*/

[ 11](esp32s3-xtensa-intmux_8h.md#abfc935ef2963ee54b6a1f1279b4887ff)#define WIFI\_MAC\_NMI\_SOURCE 1 /\* interrupt of WiFi MAC, NMI \*/

[ 12](esp32s3-xtensa-intmux_8h.md#af3cef5f23f39a396dec2a356f395ef69)#define WIFI\_PWR\_INTR\_SOURCE 2

[ 13](esp32s3-xtensa-intmux_8h.md#a5383f7fa77bc12a8301c54e0dfb66306)#define WIFI\_BB\_INTR\_SOURCE 3 /\* interrupt of WiFi BB, level\*/

[ 14](esp32s3-xtensa-intmux_8h.md#a0b48425e316b45db6f105daa6f2a0cff)#define BT\_MAC\_INTR\_SOURCE 4 /\* will be cancelled\*/

[ 15](esp32s3-xtensa-intmux_8h.md#aca3a7357f242a4e91269736de6545470)#define BT\_BB\_INTR\_SOURCE 5 /\* interrupt of BT BB, level\*/

[ 16](esp32s3-xtensa-intmux_8h.md#ab404d2ab995f39616675330f6462dd19)#define BT\_BB\_NMI\_SOURCE 6 /\* interrupt of BT BB, NMI\*/

[ 17](esp32s3-xtensa-intmux_8h.md#a14017a5bb9744f9c32138dbdcc09a786)#define RWBT\_INTR\_SOURCE 7 /\* interrupt of RWBT, level\*/

[ 18](esp32s3-xtensa-intmux_8h.md#a8cf7f44d512a2c0b215397ae4c37a4f1)#define RWBLE\_INTR\_SOURCE 8 /\* interrupt of RWBLE, level\*/

[ 19](esp32s3-xtensa-intmux_8h.md#a445a79e81929641c372257f4018127f6)#define RWBT\_NMI\_SOURCE 9 /\* interrupt of RWBT, NMI\*/

[ 20](esp32s3-xtensa-intmux_8h.md#a3b9cef18112f398bd4ada544f3e2b5a0)#define RWBLE\_NMI\_SOURCE 10 /\* interrupt of RWBLE, NMI\*/

[ 21](esp32s3-xtensa-intmux_8h.md#a8b38a0acf3511d0de89607d7eac8f537)#define I2C\_MASTER\_SOURCE 11 /\* interrupt of I2C Master, level\*/

[ 22](esp32s3-xtensa-intmux_8h.md#a24b7d137ebb32c58d60d5f84a3ce67db)#define SLC0\_INTR\_SOURCE 12 /\* interrupt of SLC0, level\*/

[ 23](esp32s3-xtensa-intmux_8h.md#a8d8c7fb4a7206356ef7c7b41df4c1b7b)#define SLC1\_INTR\_SOURCE 13 /\* interrupt of SLC1, level\*/

[ 24](esp32s3-xtensa-intmux_8h.md#aa714005c0707aaf1ba5b4a033bcb8f81)#define UHCI0\_INTR\_SOURCE 14 /\* interrupt of UHCI0, level\*/

[ 25](esp32s3-xtensa-intmux_8h.md#a0837c2b982c45380cd89c136d5e9fb2c)#define UHCI1\_INTR\_SOURCE 15 /\* interrupt of UHCI1, level\*/

[ 26](esp32s3-xtensa-intmux_8h.md#a64020d7c1f6557ef6da375f12acf68de)#define GPIO\_INTR\_SOURCE 16 /\* interrupt of GPIO, level\*/

[ 27](esp32s3-xtensa-intmux_8h.md#a23e7de652ab586c903ec999aa8e77e4e)#define GPIO\_NMI\_SOURCE 17 /\* interrupt of GPIO, NMI\*/

[ 28](esp32s3-xtensa-intmux_8h.md#afb98fcf1a9be6030f5ca87dea6675974)#define GPIO\_INTR\_SOURCE2 18 /\* interrupt of GPIO, level\*/

[ 29](esp32s3-xtensa-intmux_8h.md#ad11e04bc97a0115966929013f06efa50)#define GPIO\_NMI\_SOURCE2 19 /\* interrupt of GPIO, NMI\*/

[ 30](esp32s3-xtensa-intmux_8h.md#a5779abc3d34c94cfad763d9ababebb9f)#define SPI1\_INTR\_SOURCE 20 /\* interrupt of SPI1, level\*/

[ 31](esp32s3-xtensa-intmux_8h.md#ac5d10660472f10fae0d0511f254b696d)#define SPI2\_INTR\_SOURCE 21 /\* interrupt of SPI2, level\*/

[ 32](esp32s3-xtensa-intmux_8h.md#a95996e58c94e25db8b2d97de7595996f)#define SPI3\_INTR\_SOURCE 22 /\* interrupt of SPI3, level\*/

[ 33](esp32s3-xtensa-intmux_8h.md#a9632b36ac8096d9a56940be81637ade7)#define LCD\_CAM\_INTR\_SOURCE 24 /\* interrupt of LCD camera, level\*/

[ 34](esp32s3-xtensa-intmux_8h.md#a6d41fd98988304b2ab82785c24140f8d)#define I2S0\_INTR\_SOURCE 25 /\* interrupt of I2S0, level\*/

[ 35](esp32s3-xtensa-intmux_8h.md#a3b0877aad4fc7995be0cfb71fabb13a6)#define I2S1\_INTR\_SOURCE 26 /\* interrupt of I2S1, level\*/

[ 36](esp32s3-xtensa-intmux_8h.md#af4569e6b552e35100134e167cf11c7da)#define UART0\_INTR\_SOURCE 27 /\* interrupt of UART0, level\*/

[ 37](esp32s3-xtensa-intmux_8h.md#ad6f7d29b71a32716058033727bd01dc2)#define UART1\_INTR\_SOURCE 28 /\* interrupt of UART1, level\*/

[ 38](esp32s3-xtensa-intmux_8h.md#a4a7728c85b344ae5f62684286519f647)#define UART2\_INTR\_SOURCE 29 /\* interrupt of UART2, level\*/

[ 39](esp32s3-xtensa-intmux_8h.md#a26ce888bf67587b5ab6392f2ea0157c6)#define SDIO\_HOST\_INTR\_SOURCE 30 /\* interrupt of SD/SDIO/MMC HOST, level\*/

[ 40](esp32s3-xtensa-intmux_8h.md#a29ff03b184368e0a9ad6caf0cc9288ca)#define PWM0\_INTR\_SOURCE 31 /\* interrupt of PWM0, level, Reserved\*/

[ 41](esp32s3-xtensa-intmux_8h.md#ab9a0099e8acba4831c68af88a073e31d)#define PWM1\_INTR\_SOURCE 32 /\* interrupt of PWM1, level, Reserved\*/

[ 42](esp32s3-xtensa-intmux_8h.md#a296f3d252d30615dbaea32d61cba9214)#define LEDC\_INTR\_SOURCE 35 /\* interrupt of LED PWM, level\*/

[ 43](esp32s3-xtensa-intmux_8h.md#aaf244ea4b63d912e0ce8d59795c79f9d)#define EFUSE\_INTR\_SOURCE 36 /\* interrupt of efuse, level, not likely to use\*/

[ 44](esp32s3-xtensa-intmux_8h.md#a3a56673ee10a809fb2e75065d84b6f8e)#define TWAI\_INTR\_SOURCE 37 /\* interrupt of can, level\*/

[ 45](esp32s3-xtensa-intmux_8h.md#a7a020da508049560356d36ab9607bca9)#define USB\_INTR\_SOURCE 38 /\* interrupt of USB, level\*/

[ 46](esp32s3-xtensa-intmux_8h.md#a80d2efc475574efe9250d0048a8a8c12)#define RTC\_CORE\_INTR\_SOURCE 39 /\* interrupt of rtc core and watchdog, level\*/

[ 47](esp32s3-xtensa-intmux_8h.md#ac6d02a2b0f009553a9e52e7842fa959d)#define RMT\_INTR\_SOURCE 40 /\* interrupt of remote controller, level\*/

[ 48](esp32s3-xtensa-intmux_8h.md#acfdc02f0268c6145e3ffd5221ce7152f)#define PCNT\_INTR\_SOURCE 41 /\* interrupt of pulse count, level\*/

[ 49](esp32s3-xtensa-intmux_8h.md#a7a706aa628e14e55247d20c9853d76a9)#define I2C\_EXT0\_INTR\_SOURCE 42 /\* interrupt of I2C controller1, level\*/

[ 50](esp32s3-xtensa-intmux_8h.md#ac0e06a214b3990cb35fa4975e2a85e8e)#define I2C\_EXT1\_INTR\_SOURCE 43 /\* interrupt of I2C controller0, level\*/

[ 51](esp32s3-xtensa-intmux_8h.md#a7036cef97de80d47ffbdeff6478ccbec)#define SPI2\_DMA\_INTR\_SOURCE 44 /\* interrupt of SPI2 DMA, level\*/

[ 52](esp32s3-xtensa-intmux_8h.md#a1916307ca85215eb4c995bc4ae83eb50)#define SPI3\_DMA\_INTR\_SOURCE 45 /\* interrupt of SPI3 DMA, level\*/

[ 53](esp32s3-xtensa-intmux_8h.md#a407bd79d5c36e715bcd21a64d8f77c04)#define WDT\_INTR\_SOURCE 47 /\* will be cancelled\*/

[ 54](esp32s3-xtensa-intmux_8h.md#a9f5fed8c34c9b971830ab3e083316271)#define TIMER1\_INTR\_SOURCE 48

[ 55](esp32s3-xtensa-intmux_8h.md#a792de801f5e8339f61a381172782ee06)#define TIMER2\_INTR\_SOURCE 49

[ 56](esp32s3-xtensa-intmux_8h.md#a22bf10410f0b99b9fe398accf66c51b1)#define TG0\_T0\_LEVEL\_INTR\_SOURCE 50 /\* interrupt of TIMER\_GROUP0, TIMER0, EDGE\*/

[ 57](esp32s3-xtensa-intmux_8h.md#a792cd371542eb8a60e4d381b168ae2b8)#define TG0\_T1\_LEVEL\_INTR\_SOURCE 51 /\* interrupt of TIMER\_GROUP0, TIMER1, EDGE\*/

[ 58](esp32s3-xtensa-intmux_8h.md#afc23d5890e9c8029e7d417291193a559)#define TG0\_WDT\_LEVEL\_INTR\_SOURCE 52 /\* interrupt of TIMER\_GROUP0, WATCH DOG, EDGE\*/

[ 59](esp32s3-xtensa-intmux_8h.md#aee34beaabe47713742eb7633bd8430e3)#define TG1\_T0\_LEVEL\_INTR\_SOURCE 53 /\* interrupt of TIMER\_GROUP1, TIMER0, EDGE\*/

[ 60](esp32s3-xtensa-intmux_8h.md#a41b4592783755438167ac4444adcaade)#define TG1\_T1\_LEVEL\_INTR\_SOURCE 54 /\* interrupt of TIMER\_GROUP1, TIMER1, EDGE\*/

[ 61](esp32s3-xtensa-intmux_8h.md#a68616a67d062b7e57dbe6dd59151b85c)#define TG1\_WDT\_LEVEL\_INTR\_SOURCE 55 /\* interrupt of TIMER\_GROUP1, WATCHDOG, EDGE\*/

[ 62](esp32s3-xtensa-intmux_8h.md#abc71e0e6d2e6ea7fc39d17297753e72e)#define CACHE\_IA\_INTR\_SOURCE 56 /\* interrupt of Cache Invalid Access, LEVEL\*/

[ 63](esp32s3-xtensa-intmux_8h.md#a4cb07c15412c22b4939bb5a1e782f6e7)#define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE 57 /\* interrupt of system timer 0, EDGE\*/

[ 64](esp32s3-xtensa-intmux_8h.md#a4ae5acb4be5a37cc87deb29ca61c8034)#define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE 58 /\* interrupt of system timer 1, EDGE\*/

[ 65](esp32s3-xtensa-intmux_8h.md#a3c07aba15f9a2e9bc4a97031a241b512)#define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE 59 /\* interrupt of system timer 2, EDGE\*/

[ 66](esp32s3-xtensa-intmux_8h.md#a36c488ff1605277f2772b1f80552f6ac)#define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE 60 /\* interrupt of SPI0/SPI1 Cache/Rejected, LEVEL\*/

[ 67](esp32s3-xtensa-intmux_8h.md#a0bbd6ed9f1c48b0556d8c0655e627cea)#define DCACHE\_PRELOAD0\_INTR\_SOURCE 61 /\* interrupt of DCache preload operation, LEVEL\*/

[ 68](esp32s3-xtensa-intmux_8h.md#a83a3ce01a7cc1f3d4095d260f96705d1)#define ICACHE\_PRELOAD0\_INTR\_SOURCE 62 /\* interrupt of ICache perload operation, LEVEL\*/

[ 69](esp32s3-xtensa-intmux_8h.md#a1e4d7c3f4b201ef8e58b1fa1714124ae)#define DCACHE\_SYNC0\_INTR\_SOURCE 63 /\* interrupt of data cache sync done, LEVEL\*/

[ 70](esp32s3-xtensa-intmux_8h.md#ae62a038d99a1fbd095213f05adfd8f0f)#define ICACHE\_SYNC0\_INTR\_SOURCE 64 /\* interrupt of instr. cache sync done, LEVEL\*/

[ 71](esp32s3-xtensa-intmux_8h.md#a68b408eb63057838c64c51718c5b1f7f)#define APB\_ADC\_INTR\_SOURCE 65 /\* interrupt of APB ADC, LEVEL\*/

[ 72](esp32s3-xtensa-intmux_8h.md#acef66209252c6f17bac98dc2da2595b6)#define DMA\_IN\_CH0\_INTR\_SOURCE 66 /\* interrupt of general DMA RX channel 0, LEVEL\*/

[ 73](esp32s3-xtensa-intmux_8h.md#a4ab6c4d84a4ccfadbdf1cbf74cd7abe2)#define DMA\_IN\_CH1\_INTR\_SOURCE 67 /\* interrupt of general DMA RX channel 1, LEVEL\*/

[ 74](esp32s3-xtensa-intmux_8h.md#a090f29def5fb84f8925407b8d4df2b16)#define DMA\_IN\_CH2\_INTR\_SOURCE 68 /\* interrupt of general DMA RX channel 2, LEVEL\*/

[ 75](esp32s3-xtensa-intmux_8h.md#abab724f60c1226a009f8bc81e624e1bc)#define DMA\_IN\_CH3\_INTR\_SOURCE 69 /\* interrupt of general DMA RX channel 3, LEVEL\*/

[ 76](esp32s3-xtensa-intmux_8h.md#aa139ac344775a2d505b1d03da7a8f91d)#define DMA\_IN\_CH4\_INTR\_SOURCE 70 /\* interrupt of general DMA RX channel 4, LEVEL\*/

[ 77](esp32s3-xtensa-intmux_8h.md#aef145a19eb3530127030eefcd93c0cc6)#define DMA\_OUT\_CH0\_INTR\_SOURCE 71 /\* interrupt of general DMA TX channel 0, LEVEL\*/

[ 78](esp32s3-xtensa-intmux_8h.md#a7b0e98e5146a26ea18f71dde60a335fd)#define DMA\_OUT\_CH1\_INTR\_SOURCE 72 /\* interrupt of general DMA TX channel 1, LEVEL\*/

[ 79](esp32s3-xtensa-intmux_8h.md#acfc5282861029aaa04b137749ba20676)#define DMA\_OUT\_CH2\_INTR\_SOURCE 73 /\* interrupt of general DMA TX channel 2, LEVEL\*/

[ 80](esp32s3-xtensa-intmux_8h.md#a7a832824047aee2c1d830223dafc7108)#define DMA\_OUT\_CH3\_INTR\_SOURCE 74 /\* interrupt of general DMA TX channel 3, LEVEL\*/

[ 81](esp32s3-xtensa-intmux_8h.md#ae81c0d07a9856dfdbd74a82ee217f279)#define DMA\_OUT\_CH4\_INTR\_SOURCE 75 /\* interrupt of general DMA TX channel 4, LEVEL\*/

[ 82](esp32s3-xtensa-intmux_8h.md#accd4889d9e375ba16ea00489e7115c30)#define RSA\_INTR\_SOURCE 76 /\* interrupt of RSA accelerator, level\*/

[ 83](esp32s3-xtensa-intmux_8h.md#ad793803f54262a4dcf6b14140e9dc22b)#define AES\_INTR\_SOURCE 77 /\* interrupt of AES accelerator, level\*/

[ 84](esp32s3-xtensa-intmux_8h.md#a59f92ba6a2f4b3fa9454558f37ff3e24)#define SHA\_INTR\_SOURCE 78 /\* interrupt of SHA accelerator, level\*/

[ 85](esp32s3-xtensa-intmux_8h.md#a47c9d4be8d21b6f389993db5dbe2883d)#define FROM\_CPU\_INTR0\_SOURCE 79 /\* interrupt0 generated from a CPU, level\*/

[ 86](esp32s3-xtensa-intmux_8h.md#a2f704a24d6d56f2e13aed56e86e8fb55)#define FROM\_CPU\_INTR1\_SOURCE 80 /\* interrupt1 generated from a CPU, level\*/

[ 87](esp32s3-xtensa-intmux_8h.md#a470d4f804a7ddb5d107f1cafe8f19308)#define FROM\_CPU\_INTR2\_SOURCE 81 /\* interrupt2 generated from a CPU, level\*/

[ 88](esp32s3-xtensa-intmux_8h.md#a0b8897c96de3f23e794440ef2ef2f523)#define FROM\_CPU\_INTR3\_SOURCE 82 /\* interrupt3 generated from a CPU, level\*/

[ 89](esp32s3-xtensa-intmux_8h.md#ab627766f8e6b851882c42596d7df540c)#define ASSIST\_DEBUG\_INTR\_SOURCE 83 /\* interrupt of Assist debug module, LEVEL\*/

[ 90](esp32s3-xtensa-intmux_8h.md#ac1b4f216b241ccb1ee89543a110795ac)#define DMA\_APBPERI\_PMS\_INTR\_SOURCE 84

[ 91](esp32s3-xtensa-intmux_8h.md#ac01e0a43892a021afe21998a4594bc9c)#define CORE0\_IRAM0\_PMS\_INTR\_SOURCE 85

[ 92](esp32s3-xtensa-intmux_8h.md#a1e105d1f6e499662772ce1b78a6ad027)#define CORE0\_DRAM0\_PMS\_INTR\_SOURCE 86

[ 93](esp32s3-xtensa-intmux_8h.md#a0562484da17734d4f3848fe28261ceca)#define CORE0\_PIF\_PMS\_INTR\_SOURCE 87

[ 94](esp32s3-xtensa-intmux_8h.md#a83166cdc662aeb9d1de9c9f0d3e2c330)#define CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE 88

[ 95](esp32s3-xtensa-intmux_8h.md#adb42ba778970c402ab5cb916ec3324f0)#define CORE1\_IRAM0\_PMS\_INTR\_SOURCE 89

[ 96](esp32s3-xtensa-intmux_8h.md#ab1fb705fe2cd1b17e7365b9501be2e8d)#define CORE1\_DRAM0\_PMS\_INTR\_SOURCE 90

[ 97](esp32s3-xtensa-intmux_8h.md#a1a592159bbecb02de45259d3af06cf46)#define CORE1\_PIF\_PMS\_INTR\_SOURCE 91

[ 98](esp32s3-xtensa-intmux_8h.md#ab1ed75a1f02dd846a8418d69c1f657d8)#define CORE1\_PIF\_PMS\_SIZE\_INTR\_SOURCE 92

[ 99](esp32s3-xtensa-intmux_8h.md#a0f236ecbe185a7008b2c5bdc61413dce)#define BACKUP\_PMS\_VIOLATE\_INTR\_SOURCE 93

[ 100](esp32s3-xtensa-intmux_8h.md#acea509fed0c77dfdb5e0f0ea7b5826af)#define CACHE\_CORE0\_ACS\_INTR\_SOURCE 94

[ 101](esp32s3-xtensa-intmux_8h.md#a253daf8607f6268ca84bfac2e9e5b796)#define CACHE\_CORE1\_ACS\_INTR\_SOURCE 95

[ 102](esp32s3-xtensa-intmux_8h.md#a481f3447ba9cb1b05df5c8972d593f54)#define USB\_SERIAL\_JTAG\_INTR\_SOURCE 96

[ 103](esp32s3-xtensa-intmux_8h.md#a414affc383ce7ef21a67367e8cdcd278)#define PREI\_BACKUP\_INTR\_SOURCE 97

[ 104](esp32s3-xtensa-intmux_8h.md#a95d0cd3450c800d5555fe4df3bc9b92e)#define DMA\_EXTMEM\_REJECT\_SOURCE 98

[ 105](esp32s3-xtensa-intmux_8h.md#ad57b1f253283c9a65fd95631a11d9532)#define MAX\_INTR\_SOURCE 99 /\* number of interrupt sources \*/

106

107/\* For Xtensa architecture, zero will allocate low/medium

108 \* levels of priority (ESP\_INTR\_FLAG\_LOWMED)

109 \*/

[ 110](esp32s3-xtensa-intmux_8h.md#a2dbeaa0c017cdff0982b381cc96f0a6c)#define IRQ\_DEFAULT\_PRIORITY 0

111

[ 112](esp32s3-xtensa-intmux_8h.md#afc7bfcea2e621d81336ea6dd23310363)#define ESP\_INTR\_FLAG\_SHARED (1<<8) /\* Interrupt can be shared between ISRs \*/

113

114#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp32s3-xtensa-intmux.h](esp32s3-xtensa-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
