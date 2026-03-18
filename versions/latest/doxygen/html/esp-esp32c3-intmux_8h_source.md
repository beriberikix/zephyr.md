---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp-esp32c3-intmux_8h_source.html
original_path: doxygen/html/esp-esp32c3-intmux_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-esp32c3-intmux.h

[Go to the documentation of this file.](esp-esp32c3-intmux_8h.md)

1/\*

2 \* Copyright (c) 2021 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C3\_INTMUX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C3\_INTMUX\_H\_

9

[ 10](esp-esp32c3-intmux_8h.md#ad000d08efc3e8a5fc56da537973a5cb8)#define WIFI\_MAC\_INTR\_SOURCE 0

[ 11](esp-esp32c3-intmux_8h.md#abfc935ef2963ee54b6a1f1279b4887ff)#define WIFI\_MAC\_NMI\_SOURCE 1

[ 12](esp-esp32c3-intmux_8h.md#af3cef5f23f39a396dec2a356f395ef69)#define WIFI\_PWR\_INTR\_SOURCE 2

[ 13](esp-esp32c3-intmux_8h.md#a5383f7fa77bc12a8301c54e0dfb66306)#define WIFI\_BB\_INTR\_SOURCE 3

[ 14](esp-esp32c3-intmux_8h.md#a0b48425e316b45db6f105daa6f2a0cff)#define BT\_MAC\_INTR\_SOURCE 4

[ 15](esp-esp32c3-intmux_8h.md#aca3a7357f242a4e91269736de6545470)#define BT\_BB\_INTR\_SOURCE 5

[ 16](esp-esp32c3-intmux_8h.md#ab404d2ab995f39616675330f6462dd19)#define BT\_BB\_NMI\_SOURCE 6

[ 17](esp-esp32c3-intmux_8h.md#a14017a5bb9744f9c32138dbdcc09a786)#define RWBT\_INTR\_SOURCE 7

[ 18](esp-esp32c3-intmux_8h.md#a8cf7f44d512a2c0b215397ae4c37a4f1)#define RWBLE\_INTR\_SOURCE 8

[ 19](esp-esp32c3-intmux_8h.md#a445a79e81929641c372257f4018127f6)#define RWBT\_NMI\_SOURCE 9

[ 20](esp-esp32c3-intmux_8h.md#a3b9cef18112f398bd4ada544f3e2b5a0)#define RWBLE\_NMI\_SOURCE 10

[ 21](esp-esp32c3-intmux_8h.md#a8b38a0acf3511d0de89607d7eac8f537)#define I2C\_MASTER\_SOURCE 11

[ 22](esp-esp32c3-intmux_8h.md#a24b7d137ebb32c58d60d5f84a3ce67db)#define SLC0\_INTR\_SOURCE 12

[ 23](esp-esp32c3-intmux_8h.md#a8d8c7fb4a7206356ef7c7b41df4c1b7b)#define SLC1\_INTR\_SOURCE 13

[ 24](esp-esp32c3-intmux_8h.md#ab2acf6e0b0eb1f7ea85f0910f90326dc)#define APB\_CTRL\_INTR\_SOURCE 14

[ 25](esp-esp32c3-intmux_8h.md#aa714005c0707aaf1ba5b4a033bcb8f81)#define UHCI0\_INTR\_SOURCE 15

[ 26](esp-esp32c3-intmux_8h.md#a64020d7c1f6557ef6da375f12acf68de)#define GPIO\_INTR\_SOURCE 16

[ 27](esp-esp32c3-intmux_8h.md#a23e7de652ab586c903ec999aa8e77e4e)#define GPIO\_NMI\_SOURCE 17

[ 28](esp-esp32c3-intmux_8h.md#a5779abc3d34c94cfad763d9ababebb9f)#define SPI1\_INTR\_SOURCE 18

[ 29](esp-esp32c3-intmux_8h.md#ac5d10660472f10fae0d0511f254b696d)#define SPI2\_INTR\_SOURCE 19

[ 30](esp-esp32c3-intmux_8h.md#a3b0877aad4fc7995be0cfb71fabb13a6)#define I2S1\_INTR\_SOURCE 20

[ 31](esp-esp32c3-intmux_8h.md#af4569e6b552e35100134e167cf11c7da)#define UART0\_INTR\_SOURCE 21

[ 32](esp-esp32c3-intmux_8h.md#ad6f7d29b71a32716058033727bd01dc2)#define UART1\_INTR\_SOURCE 22

[ 33](esp-esp32c3-intmux_8h.md#a296f3d252d30615dbaea32d61cba9214)#define LEDC\_INTR\_SOURCE 23

[ 34](esp-esp32c3-intmux_8h.md#aaf244ea4b63d912e0ce8d59795c79f9d)#define EFUSE\_INTR\_SOURCE 24

[ 35](esp-esp32c3-intmux_8h.md#a3a56673ee10a809fb2e75065d84b6f8e)#define TWAI\_INTR\_SOURCE 25

[ 36](esp-esp32c3-intmux_8h.md#a7a020da508049560356d36ab9607bca9)#define USB\_INTR\_SOURCE 26

[ 37](esp-esp32c3-intmux_8h.md#a80d2efc475574efe9250d0048a8a8c12)#define RTC\_CORE\_INTR\_SOURCE 27

[ 38](esp-esp32c3-intmux_8h.md#ac6d02a2b0f009553a9e52e7842fa959d)#define RMT\_INTR\_SOURCE 28

[ 39](esp-esp32c3-intmux_8h.md#a7a706aa628e14e55247d20c9853d76a9)#define I2C\_EXT0\_INTR\_SOURCE 29

[ 40](esp-esp32c3-intmux_8h.md#a9f5fed8c34c9b971830ab3e083316271)#define TIMER1\_INTR\_SOURCE 30

[ 41](esp-esp32c3-intmux_8h.md#a792de801f5e8339f61a381172782ee06)#define TIMER2\_INTR\_SOURCE 31

[ 42](esp-esp32c3-intmux_8h.md#a22bf10410f0b99b9fe398accf66c51b1)#define TG0\_T0\_LEVEL\_INTR\_SOURCE 32

[ 43](esp-esp32c3-intmux_8h.md#afc23d5890e9c8029e7d417291193a559)#define TG0\_WDT\_LEVEL\_INTR\_SOURCE 33

[ 44](esp-esp32c3-intmux_8h.md#aee34beaabe47713742eb7633bd8430e3)#define TG1\_T0\_LEVEL\_INTR\_SOURCE 34

[ 45](esp-esp32c3-intmux_8h.md#a68616a67d062b7e57dbe6dd59151b85c)#define TG1\_WDT\_LEVEL\_INTR\_SOURCE 35

[ 46](esp-esp32c3-intmux_8h.md#abc71e0e6d2e6ea7fc39d17297753e72e)#define CACHE\_IA\_INTR\_SOURCE 36

[ 47](esp-esp32c3-intmux_8h.md#a4cb07c15412c22b4939bb5a1e782f6e7)#define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE 37

[ 48](esp-esp32c3-intmux_8h.md#a4ae5acb4be5a37cc87deb29ca61c8034)#define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE 38

[ 49](esp-esp32c3-intmux_8h.md#a3c07aba15f9a2e9bc4a97031a241b512)#define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE 39

[ 50](esp-esp32c3-intmux_8h.md#a36c488ff1605277f2772b1f80552f6ac)#define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE 40

[ 51](esp-esp32c3-intmux_8h.md#a83a3ce01a7cc1f3d4095d260f96705d1)#define ICACHE\_PRELOAD0\_INTR\_SOURCE 41

[ 52](esp-esp32c3-intmux_8h.md#ae62a038d99a1fbd095213f05adfd8f0f)#define ICACHE\_SYNC0\_INTR\_SOURCE 42

[ 53](esp-esp32c3-intmux_8h.md#a68b408eb63057838c64c51718c5b1f7f)#define APB\_ADC\_INTR\_SOURCE 43

[ 54](esp-esp32c3-intmux_8h.md#a25d5f4b9fe34b025f0d780e9bafe9d96)#define DMA\_CH0\_INTR\_SOURCE 44

[ 55](esp-esp32c3-intmux_8h.md#a7026a776eda63a2aee8b3325dad72791)#define DMA\_CH1\_INTR\_SOURCE 45

[ 56](esp-esp32c3-intmux_8h.md#ad09b4d38f016ecc50dbf97f999991120)#define DMA\_CH2\_INTR\_SOURCE 46

[ 57](esp-esp32c3-intmux_8h.md#accd4889d9e375ba16ea00489e7115c30)#define RSA\_INTR\_SOURCE 47

[ 58](esp-esp32c3-intmux_8h.md#ad793803f54262a4dcf6b14140e9dc22b)#define AES\_INTR\_SOURCE 48

[ 59](esp-esp32c3-intmux_8h.md#a59f92ba6a2f4b3fa9454558f37ff3e24)#define SHA\_INTR\_SOURCE 49

[ 60](esp-esp32c3-intmux_8h.md#a47c9d4be8d21b6f389993db5dbe2883d)#define FROM\_CPU\_INTR0\_SOURCE 50

[ 61](esp-esp32c3-intmux_8h.md#a2f704a24d6d56f2e13aed56e86e8fb55)#define FROM\_CPU\_INTR1\_SOURCE 51

[ 62](esp-esp32c3-intmux_8h.md#a470d4f804a7ddb5d107f1cafe8f19308)#define FROM\_CPU\_INTR2\_SOURCE 52

[ 63](esp-esp32c3-intmux_8h.md#a0b8897c96de3f23e794440ef2ef2f523)#define FROM\_CPU\_INTR3\_SOURCE 53

[ 64](esp-esp32c3-intmux_8h.md#ab627766f8e6b851882c42596d7df540c)#define ASSIST\_DEBUG\_INTR\_SOURCE 54

[ 65](esp-esp32c3-intmux_8h.md#ac1b4f216b241ccb1ee89543a110795ac)#define DMA\_APBPERI\_PMS\_INTR\_SOURCE 55

[ 66](esp-esp32c3-intmux_8h.md#ac01e0a43892a021afe21998a4594bc9c)#define CORE0\_IRAM0\_PMS\_INTR\_SOURCE 56

[ 67](esp-esp32c3-intmux_8h.md#a1e105d1f6e499662772ce1b78a6ad027)#define CORE0\_DRAM0\_PMS\_INTR\_SOURCE 57

[ 68](esp-esp32c3-intmux_8h.md#a0562484da17734d4f3848fe28261ceca)#define CORE0\_PIF\_PMS\_INTR\_SOURCE 58

[ 69](esp-esp32c3-intmux_8h.md#a83166cdc662aeb9d1de9c9f0d3e2c330)#define CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE 59

[ 70](esp-esp32c3-intmux_8h.md#a4386805f6a7f861e5f71c9e6b31a106e)#define BAK\_PMS\_VIOLATE\_INTR\_SOURCE 60

[ 71](esp-esp32c3-intmux_8h.md#acea509fed0c77dfdb5e0f0ea7b5826af)#define CACHE\_CORE0\_ACS\_INTR\_SOURCE 61

72

73#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-esp32c3-intmux.h](esp-esp32c3-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
