---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp-esp32c2-intmux_8h_source.html
original_path: doxygen/html/esp-esp32c2-intmux_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-esp32c2-intmux.h

[Go to the documentation of this file.](esp-esp32c2-intmux_8h.md)

1/\*

2 \* Copyright (c) 2024 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C2\_INTMUX\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_INTERRUPT\_CONTROLLER\_ESP32C2\_INTMUX\_H\_

9

[ 10](esp-esp32c2-intmux_8h.md#ad000d08efc3e8a5fc56da537973a5cb8)#define WIFI\_MAC\_INTR\_SOURCE 0

[ 11](esp-esp32c2-intmux_8h.md#abfc935ef2963ee54b6a1f1279b4887ff)#define WIFI\_MAC\_NMI\_SOURCE 1

[ 12](esp-esp32c2-intmux_8h.md#af3cef5f23f39a396dec2a356f395ef69)#define WIFI\_PWR\_INTR\_SOURCE 2

[ 13](esp-esp32c2-intmux_8h.md#a5383f7fa77bc12a8301c54e0dfb66306)#define WIFI\_BB\_INTR\_SOURCE 3

[ 14](esp-esp32c2-intmux_8h.md#a0b48425e316b45db6f105daa6f2a0cff)#define BT\_MAC\_INTR\_SOURCE 4

[ 15](esp-esp32c2-intmux_8h.md#aca3a7357f242a4e91269736de6545470)#define BT\_BB\_INTR\_SOURCE 5

[ 16](esp-esp32c2-intmux_8h.md#ab404d2ab995f39616675330f6462dd19)#define BT\_BB\_NMI\_SOURCE 6

[ 17](esp-esp32c2-intmux_8h.md#a2e2ebcd69706fcd8908616ba9d2eadee)#define LP\_TIMER\_SOURCE 7

[ 18](esp-esp32c2-intmux_8h.md#a994eca8b87e9db761ea2a93786c201df)#define COEX\_SOURCE 8

[ 19](esp-esp32c2-intmux_8h.md#aef8edd6dcae7c2f3e07c89dbe3450a1c)#define BLE\_TIMER\_SOURCE 9

[ 20](esp-esp32c2-intmux_8h.md#a30434b162fa1be66196eb0eb2aae4521)#define BLE\_SEC\_SOURCE 10

[ 21](esp-esp32c2-intmux_8h.md#a8b38a0acf3511d0de89607d7eac8f537)#define I2C\_MASTER\_SOURCE 11

[ 22](esp-esp32c2-intmux_8h.md#ab2acf6e0b0eb1f7ea85f0910f90326dc)#define APB\_CTRL\_INTR\_SOURCE 12

[ 23](esp-esp32c2-intmux_8h.md#a64020d7c1f6557ef6da375f12acf68de)#define GPIO\_INTR\_SOURCE 13

[ 24](esp-esp32c2-intmux_8h.md#a23e7de652ab586c903ec999aa8e77e4e)#define GPIO\_NMI\_SOURCE 14

[ 25](esp-esp32c2-intmux_8h.md#a5779abc3d34c94cfad763d9ababebb9f)#define SPI1\_INTR\_SOURCE 15

[ 26](esp-esp32c2-intmux_8h.md#ac5d10660472f10fae0d0511f254b696d)#define SPI2\_INTR\_SOURCE 16

[ 27](esp-esp32c2-intmux_8h.md#af4569e6b552e35100134e167cf11c7da)#define UART0\_INTR\_SOURCE 17

[ 28](esp-esp32c2-intmux_8h.md#ad6f7d29b71a32716058033727bd01dc2)#define UART1\_INTR\_SOURCE 18

[ 29](esp-esp32c2-intmux_8h.md#a296f3d252d30615dbaea32d61cba9214)#define LEDC\_INTR\_SOURCE 19

[ 30](esp-esp32c2-intmux_8h.md#aaf244ea4b63d912e0ce8d59795c79f9d)#define EFUSE\_INTR\_SOURCE 20

[ 31](esp-esp32c2-intmux_8h.md#a80d2efc475574efe9250d0048a8a8c12)#define RTC\_CORE\_INTR\_SOURCE 21

[ 32](esp-esp32c2-intmux_8h.md#a7a706aa628e14e55247d20c9853d76a9)#define I2C\_EXT0\_INTR\_SOURCE 22

[ 33](esp-esp32c2-intmux_8h.md#a22bf10410f0b99b9fe398accf66c51b1)#define TG0\_T0\_LEVEL\_INTR\_SOURCE 23

[ 34](esp-esp32c2-intmux_8h.md#afc23d5890e9c8029e7d417291193a559)#define TG0\_WDT\_LEVEL\_INTR\_SOURCE 24

[ 35](esp-esp32c2-intmux_8h.md#abc71e0e6d2e6ea7fc39d17297753e72e)#define CACHE\_IA\_INTR\_SOURCE 25

[ 36](esp-esp32c2-intmux_8h.md#a4cb07c15412c22b4939bb5a1e782f6e7)#define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE 26

[ 37](esp-esp32c2-intmux_8h.md#a4ae5acb4be5a37cc87deb29ca61c8034)#define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE 27

[ 38](esp-esp32c2-intmux_8h.md#a3c07aba15f9a2e9bc4a97031a241b512)#define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE 28

[ 39](esp-esp32c2-intmux_8h.md#a36c488ff1605277f2772b1f80552f6ac)#define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE 29

[ 40](esp-esp32c2-intmux_8h.md#a83a3ce01a7cc1f3d4095d260f96705d1)#define ICACHE\_PRELOAD0\_INTR\_SOURCE 30

[ 41](esp-esp32c2-intmux_8h.md#ae62a038d99a1fbd095213f05adfd8f0f)#define ICACHE\_SYNC0\_INTR\_SOURCE 31

[ 42](esp-esp32c2-intmux_8h.md#a68b408eb63057838c64c51718c5b1f7f)#define APB\_ADC\_INTR\_SOURCE 32

[ 43](esp-esp32c2-intmux_8h.md#a25d5f4b9fe34b025f0d780e9bafe9d96)#define DMA\_CH0\_INTR\_SOURCE 33

[ 44](esp-esp32c2-intmux_8h.md#a59f92ba6a2f4b3fa9454558f37ff3e24)#define SHA\_INTR\_SOURCE 34

[ 45](esp-esp32c2-intmux_8h.md#aa471b47ba3f4e7a17dac9702e250acf4)#define ECC\_INTR\_SOURCE 35

[ 46](esp-esp32c2-intmux_8h.md#a47c9d4be8d21b6f389993db5dbe2883d)#define FROM\_CPU\_INTR0\_SOURCE 36

[ 47](esp-esp32c2-intmux_8h.md#a2f704a24d6d56f2e13aed56e86e8fb55)#define FROM\_CPU\_INTR1\_SOURCE 37

[ 48](esp-esp32c2-intmux_8h.md#a470d4f804a7ddb5d107f1cafe8f19308)#define FROM\_CPU\_INTR2\_SOURCE 38

[ 49](esp-esp32c2-intmux_8h.md#a0b8897c96de3f23e794440ef2ef2f523)#define FROM\_CPU\_INTR3\_SOURCE 39

[ 50](esp-esp32c2-intmux_8h.md#ab627766f8e6b851882c42596d7df540c)#define ASSIST\_DEBUG\_INTR\_SOURCE 40

[ 51](esp-esp32c2-intmux_8h.md#a83166cdc662aeb9d1de9c9f0d3e2c330)#define CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE 41

[ 52](esp-esp32c2-intmux_8h.md#acea509fed0c77dfdb5e0f0ea7b5826af)#define CACHE\_CORE0\_ACS\_INTR\_SOURCE 42

53

54/\* RISC-V supports priority values from 1 (lowest) to 15.

55 \* As interrupt controller for Xtensa and RISC-V is shared, this is

56 \* set to an intermediate and compatible value.

57 \*/

[ 58](esp-esp32c2-intmux_8h.md#a2dbeaa0c017cdff0982b381cc96f0a6c)#define IRQ\_DEFAULT\_PRIORITY 3

59

[ 60](esp-esp32c2-intmux_8h.md#afc7bfcea2e621d81336ea6dd23310363)#define ESP\_INTR\_FLAG\_SHARED (1<<8) /\* Interrupt can be shared between ISRs \*/

61

62#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-esp32c2-intmux.h](esp-esp32c2-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
