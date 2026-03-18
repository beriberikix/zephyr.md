---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp-esp32c6-intmux_8h_source.html
original_path: doxygen/html/esp-esp32c6-intmux_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-esp32c6-intmux.h

[Go to the documentation of this file.](esp-esp32c6-intmux_8h.md)

1/\*

2 \* Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C6\_INTMUX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C6\_INTMUX\_H\_

9

[ 10](esp-esp32c6-intmux_8h.md#ad000d08efc3e8a5fc56da537973a5cb8)#define WIFI\_MAC\_INTR\_SOURCE 0 /\* interrupt of WiFi MAC, level\*/

[ 11](esp-esp32c6-intmux_8h.md#abfc935ef2963ee54b6a1f1279b4887ff)#define WIFI\_MAC\_NMI\_SOURCE 1 /\* interrupt of WiFi MAC, NMI\*/

[ 12](esp-esp32c6-intmux_8h.md#af3cef5f23f39a396dec2a356f395ef69)#define WIFI\_PWR\_INTR\_SOURCE 2

[ 13](esp-esp32c6-intmux_8h.md#a5383f7fa77bc12a8301c54e0dfb66306)#define WIFI\_BB\_INTR\_SOURCE 3 /\* interrupt of WiFi BB, level\*/

[ 14](esp-esp32c6-intmux_8h.md#a0b48425e316b45db6f105daa6f2a0cff)#define BT\_MAC\_INTR\_SOURCE 4 /\* will be cancelled\*/

[ 15](esp-esp32c6-intmux_8h.md#aca3a7357f242a4e91269736de6545470)#define BT\_BB\_INTR\_SOURCE 5 /\* interrupt of BT BB, level\*/

[ 16](esp-esp32c6-intmux_8h.md#ab404d2ab995f39616675330f6462dd19)#define BT\_BB\_NMI\_SOURCE 6 /\* interrupt of BT BB, NMI\*/

[ 17](esp-esp32c6-intmux_8h.md#ad03c6b1b20803d8b41a35f15bf7ddf4d)#define LP\_TIMER\_INTR\_SOURCE 7

[ 18](esp-esp32c6-intmux_8h.md#a7dff8de43b99c2d24bc48f88a0afdae0)#define COEX\_INTR\_SOURCE 8

[ 19](esp-esp32c6-intmux_8h.md#adbc876ad874f671f39e35d196e8f7a6b)#define BLE\_TIMER\_INTR\_SOURCE 9

[ 20](esp-esp32c6-intmux_8h.md#a111640b45d607cd611e7928f965537d4)#define BLE\_SEC\_INTR\_SOURCE 10

[ 21](esp-esp32c6-intmux_8h.md#a8b38a0acf3511d0de89607d7eac8f537)#define I2C\_MASTER\_SOURCE 11 /\* interrupt of I2C Master, level\*/

[ 22](esp-esp32c6-intmux_8h.md#a3562ce23b1b55e367bc9165b68e6b937)#define ZB\_MAC\_SOURCE 12

[ 23](esp-esp32c6-intmux_8h.md#a1a3ba4507baef4ff4da50836708a90d5)#define PMU\_INTR\_SOURCE 13

[ 24](esp-esp32c6-intmux_8h.md#aaf244ea4b63d912e0ce8d59795c79f9d)#define EFUSE\_INTR\_SOURCE 14 /\* interrupt of efuse, level, not likely to use\*/

[ 25](esp-esp32c6-intmux_8h.md#ab8231886be224cfd7393b672377e8d65)#define LP\_RTC\_TIMER\_INTR\_SOURCE 15

[ 26](esp-esp32c6-intmux_8h.md#a0a11e636f52c56d92deaf08b06b15d9d)#define LP\_UART\_INTR\_SOURCE 16

[ 27](esp-esp32c6-intmux_8h.md#a5e3657824945848e65fafefa96033d8a)#define LP\_I2C\_INTR\_SOURCE 17

[ 28](esp-esp32c6-intmux_8h.md#a0575e1c89bfd864c0d2b54a0ec861037)#define LP\_WDT\_INTR\_SOURCE 18

[ 29](esp-esp32c6-intmux_8h.md#a1b6615100454fa7836acd2d8d54a15ad)#define LP\_PERI\_TIMEOUT\_INTR\_SOURCE 19

[ 30](esp-esp32c6-intmux_8h.md#a0887b9c26ba83d8c04da11623484571c)#define LP\_APM\_M0\_INTR\_SOURCE 20

[ 31](esp-esp32c6-intmux_8h.md#ad68dafecd716c3b3b5af87048e70dc46)#define LP\_APM\_M1\_INTR\_SOURCE 21

[ 32](esp-esp32c6-intmux_8h.md#a47c9d4be8d21b6f389993db5dbe2883d)#define FROM\_CPU\_INTR0\_SOURCE 22 /\* interrupt0 generated from a CPU, level\*/

[ 33](esp-esp32c6-intmux_8h.md#a2f704a24d6d56f2e13aed56e86e8fb55)#define FROM\_CPU\_INTR1\_SOURCE 23 /\* interrupt1 generated from a CPU, level\*/

[ 34](esp-esp32c6-intmux_8h.md#a470d4f804a7ddb5d107f1cafe8f19308)#define FROM\_CPU\_INTR2\_SOURCE 24 /\* interrupt2 generated from a CPU, level\*/

[ 35](esp-esp32c6-intmux_8h.md#a0b8897c96de3f23e794440ef2ef2f523)#define FROM\_CPU\_INTR3\_SOURCE 25 /\* interrupt3 generated from a CPU, level\*/

[ 36](esp-esp32c6-intmux_8h.md#ab627766f8e6b851882c42596d7df540c)#define ASSIST\_DEBUG\_INTR\_SOURCE 26 /\* interrupt of Assist debug module, LEVEL\*/

[ 37](esp-esp32c6-intmux_8h.md#ad6312c1a757038238df60334c1777410)#define TRACE\_INTR\_SOURCE 27

[ 38](esp-esp32c6-intmux_8h.md#a102f4242826c646d8babb5b161a0c092)#define CACHE\_INTR\_SOURCE 28

[ 39](esp-esp32c6-intmux_8h.md#a3a3b6cb7a8509d87c4565657b14e80c3)#define CPU\_PERI\_TIMEOUT\_INTR\_SOURCE 29

[ 40](esp-esp32c6-intmux_8h.md#a64020d7c1f6557ef6da375f12acf68de)#define GPIO\_INTR\_SOURCE 30 /\* interrupt of GPIO, level\*/

[ 41](esp-esp32c6-intmux_8h.md#a23e7de652ab586c903ec999aa8e77e4e)#define GPIO\_NMI\_SOURCE 31 /\* interrupt of GPIO, NMI\*/

[ 42](esp-esp32c6-intmux_8h.md#a9eb00cc7adbaba58008b1190cfe4d63b)#define PAU\_INTR\_SOURCE 32

[ 43](esp-esp32c6-intmux_8h.md#a6c7756a44b101b5075aedac9baf733b9)#define HP\_PERI\_TIMEOUT\_INTR\_SOURCE 33

[ 44](esp-esp32c6-intmux_8h.md#a4a57355bb47da52cb90571f2efb405d8)#define MODEM\_PERI\_TIMEOUT\_INTR\_SOURCE 34

[ 45](esp-esp32c6-intmux_8h.md#aa38b79495b31783ef39d627c88ac158b)#define HP\_APM\_M0\_INTR\_SOURCE 35

[ 46](esp-esp32c6-intmux_8h.md#a0e5f1e66fb5502c426c42de7248f026f)#define HP\_APM\_M1\_INTR\_SOURCE 36

[ 47](esp-esp32c6-intmux_8h.md#a4ef1ca8c6b71640fdf5ca7c7eed845c5)#define HP\_APM\_M2\_INTR\_SOURCE 37

[ 48](esp-esp32c6-intmux_8h.md#a04a62fcb5b5ea0c0ab7029c5440a7a61)#define HP\_APM\_M3\_INTR\_SOURCE 38

[ 49](esp-esp32c6-intmux_8h.md#a99a7a79ead0fe03a5cfbada6eee24a7a)#define LP\_APM0\_INTR\_SOURCE 39

[ 50](esp-esp32c6-intmux_8h.md#a6c1065701cb5a46b1b686ab0ab67f279)#define MSPI\_INTR\_SOURCE 40

[ 51](esp-esp32c6-intmux_8h.md#a3b0877aad4fc7995be0cfb71fabb13a6)#define I2S1\_INTR\_SOURCE 41 /\* interrupt of I2S1, level\*/

[ 52](esp-esp32c6-intmux_8h.md#aa714005c0707aaf1ba5b4a033bcb8f81)#define UHCI0\_INTR\_SOURCE 42 /\* interrupt of UHCI0, level\*/

[ 53](esp-esp32c6-intmux_8h.md#af4569e6b552e35100134e167cf11c7da)#define UART0\_INTR\_SOURCE 43 /\* interrupt of UART0, level\*/

[ 54](esp-esp32c6-intmux_8h.md#ad6f7d29b71a32716058033727bd01dc2)#define UART1\_INTR\_SOURCE 44 /\* interrupt of UART1, level\*/

[ 55](esp-esp32c6-intmux_8h.md#a296f3d252d30615dbaea32d61cba9214)#define LEDC\_INTR\_SOURCE 45 /\* interrupt of LED PWM, level\*/

[ 56](esp-esp32c6-intmux_8h.md#a55da996fa56498f1afbc1c33cf02b69f)#define TWAI0\_INTR\_SOURCE 46 /\* interrupt of can0, level\*/

[ 57](esp-esp32c6-intmux_8h.md#a18c1ae17b147afa71043a79c82f45c05)#define TWAI1\_INTR\_SOURCE 47 /\* interrupt of can1, level\*/

[ 58](esp-esp32c6-intmux_8h.md#a481f3447ba9cb1b05df5c8972d593f54)#define USB\_SERIAL\_JTAG\_INTR\_SOURCE 48 /\* interrupt of USB, level\*/

[ 59](esp-esp32c6-intmux_8h.md#ac6d02a2b0f009553a9e52e7842fa959d)#define RMT\_INTR\_SOURCE 49 /\* interrupt of remote controller, level\*/

[ 60](esp-esp32c6-intmux_8h.md#a7a706aa628e14e55247d20c9853d76a9)#define I2C\_EXT0\_INTR\_SOURCE 50 /\* interrupt of I2C controller1, level\*/

[ 61](esp-esp32c6-intmux_8h.md#a22bf10410f0b99b9fe398accf66c51b1)#define TG0\_T0\_LEVEL\_INTR\_SOURCE 51 /\* interrupt of TIMER\_GROUP0, TIMER0, level\*/

[ 62](esp-esp32c6-intmux_8h.md#a792cd371542eb8a60e4d381b168ae2b8)#define TG0\_T1\_LEVEL\_INTR\_SOURCE 52 /\* interrupt of TIMER\_GROUP0, TIMER1, level\*/

[ 63](esp-esp32c6-intmux_8h.md#afc23d5890e9c8029e7d417291193a559)#define TG0\_WDT\_LEVEL\_INTR\_SOURCE 53 /\* interrupt of TIMER\_GROUP0, WATCH DOG, level\*/

[ 64](esp-esp32c6-intmux_8h.md#aee34beaabe47713742eb7633bd8430e3)#define TG1\_T0\_LEVEL\_INTR\_SOURCE 54 /\* interrupt of TIMER\_GROUP1, TIMER0, level\*/

[ 65](esp-esp32c6-intmux_8h.md#a41b4592783755438167ac4444adcaade)#define TG1\_T1\_LEVEL\_INTR\_SOURCE 55 /\* interrupt of TIMER\_GROUP1, TIMER1, level\*/

[ 66](esp-esp32c6-intmux_8h.md#a68616a67d062b7e57dbe6dd59151b85c)#define TG1\_WDT\_LEVEL\_INTR\_SOURCE 56 /\* interrupt of TIMER\_GROUP1, WATCHDOG, level\*/

[ 67](esp-esp32c6-intmux_8h.md#a4cb07c15412c22b4939bb5a1e782f6e7)#define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE 57 /\* interrupt of system timer 0, EDGE\*/

[ 68](esp-esp32c6-intmux_8h.md#a4ae5acb4be5a37cc87deb29ca61c8034)#define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE 58 /\* interrupt of system timer 1, EDGE\*/

[ 69](esp-esp32c6-intmux_8h.md#a3c07aba15f9a2e9bc4a97031a241b512)#define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE 59 /\* interrupt of system timer 2, EDGE\*/

[ 70](esp-esp32c6-intmux_8h.md#a68b408eb63057838c64c51718c5b1f7f)#define APB\_ADC\_INTR\_SOURCE 60 /\* interrupt of APB ADC, LEVEL\*/

[ 71](esp-esp32c6-intmux_8h.md#ac3db7d29241dd164d73565532e1505c5)#define MCPWM0\_INTR\_SOURCE 61 /\* interrupt of MCPWM0, LEVEL\*/

[ 72](esp-esp32c6-intmux_8h.md#acfdc02f0268c6145e3ffd5221ce7152f)#define PCNT\_INTR\_SOURCE 62

[ 73](esp-esp32c6-intmux_8h.md#a52d986b2c7adde41251fd2085e3635c6)#define PARL\_IO\_INTR\_SOURCE 63

[ 74](esp-esp32c6-intmux_8h.md#a24b7d137ebb32c58d60d5f84a3ce67db)#define SLC0\_INTR\_SOURCE 64

[ 75](esp-esp32c6-intmux_8h.md#afab3ba0bfb48f7bc723065afc4894cbc)#define SLC\_INTR\_SOURCE 65

[ 76](esp-esp32c6-intmux_8h.md#acef66209252c6f17bac98dc2da2595b6)#define DMA\_IN\_CH0\_INTR\_SOURCE 66 /\* interrupt of general DMA IN channel 0, LEVEL\*/

[ 77](esp-esp32c6-intmux_8h.md#a4ab6c4d84a4ccfadbdf1cbf74cd7abe2)#define DMA\_IN\_CH1\_INTR\_SOURCE 67 /\* interrupt of general DMA IN channel 1, LEVEL\*/

[ 78](esp-esp32c6-intmux_8h.md#a090f29def5fb84f8925407b8d4df2b16)#define DMA\_IN\_CH2\_INTR\_SOURCE 68 /\* interrupt of general DMA IN channel 2, LEVEL\*/

[ 79](esp-esp32c6-intmux_8h.md#aef145a19eb3530127030eefcd93c0cc6)#define DMA\_OUT\_CH0\_INTR\_SOURCE 69 /\* interrupt of general DMA OUT channel 0, LEVEL\*/

[ 80](esp-esp32c6-intmux_8h.md#a7b0e98e5146a26ea18f71dde60a335fd)#define DMA\_OUT\_CH1\_INTR\_SOURCE 70 /\* interrupt of general DMA OUT channel 1, LEVEL\*/

[ 81](esp-esp32c6-intmux_8h.md#acfc5282861029aaa04b137749ba20676)#define DMA\_OUT\_CH2\_INTR\_SOURCE 71 /\* interrupt of general DMA OUT channel 2, LEVEL\*/

[ 82](esp-esp32c6-intmux_8h.md#ab9aa4535fd0bcff815bffa3fce8fe94b)#define GSPI2\_INTR\_SOURCE 72

[ 83](esp-esp32c6-intmux_8h.md#ad793803f54262a4dcf6b14140e9dc22b)#define AES\_INTR\_SOURCE 73 /\* interrupt of AES accelerator, level\*/

[ 84](esp-esp32c6-intmux_8h.md#a59f92ba6a2f4b3fa9454558f37ff3e24)#define SHA\_INTR\_SOURCE 74 /\* interrupt of SHA accelerator, level\*/

[ 85](esp-esp32c6-intmux_8h.md#accd4889d9e375ba16ea00489e7115c30)#define RSA\_INTR\_SOURCE 75 /\* interrupt of RSA accelerator, level\*/

[ 86](esp-esp32c6-intmux_8h.md#aa471b47ba3f4e7a17dac9702e250acf4)#define ECC\_INTR\_SOURCE 76 /\* interrupt of ECC accelerator, level\*/

[ 87](esp-esp32c6-intmux_8h.md#ad57b1f253283c9a65fd95631a11d9532)#define MAX\_INTR\_SOURCE 77

88

89#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C6\_INTMUX\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-esp32c6-intmux.h](esp-esp32c6-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
