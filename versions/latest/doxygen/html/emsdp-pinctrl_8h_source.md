---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/emsdp-pinctrl_8h_source.html
original_path: doxygen/html/emsdp-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emsdp-pinctrl.h

[Go to the documentation of this file.](emsdp-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Synopsys

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_EMSDP\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_EMSDP\_PINCTRL\_H\_

9

[ 10](emsdp-pinctrl_8h.md#ab07e23c5f619d84e177d7baf9549efca)#define PMOD\_A 0

[ 11](emsdp-pinctrl_8h.md#aa3823decf67cee6f76693f8c6cd30eeb)#define PMOD\_B 1

[ 12](emsdp-pinctrl_8h.md#a0dd9718643bf7f00ca593262ddfbbd92)#define PMOD\_C 2

[ 13](emsdp-pinctrl_8h.md#acad741047fd7dca25a3dd8a62aa29462)#define ARDUINO\_PIN\_0 3

[ 14](emsdp-pinctrl_8h.md#aceb50b34589a0d29d5c07b2846de8eaa)#define ARDUINO\_PIN\_1 4

[ 15](emsdp-pinctrl_8h.md#a442a4d1d35251c8e39845582afc92f7a)#define ARDUINO\_PIN\_2 5

[ 16](emsdp-pinctrl_8h.md#ae52d466203b1be7d2a8b52a05efa0c49)#define ARDUINO\_PIN\_3 6

[ 17](emsdp-pinctrl_8h.md#a4c9ea65aa36101fde55e6b28f2ee99fc)#define ARDUINO\_PIN\_4 7

[ 18](emsdp-pinctrl_8h.md#a9b264db3d6951e7b8fd115eede94f9f0)#define ARDUINO\_PIN\_5 8

[ 19](emsdp-pinctrl_8h.md#a4610d5acda40575f42f367db84e7a90a)#define ARDUINO\_PIN\_6 9

[ 20](emsdp-pinctrl_8h.md#a9ec207e1ec82310017a39485ac63548b)#define ARDUINO\_PIN\_7 10

[ 21](emsdp-pinctrl_8h.md#a015145fa7fd3f0337d0870e0d1e291a4)#define ARDUINO\_PIN\_8 11

[ 22](emsdp-pinctrl_8h.md#a93a418c3f0d1e46b8da3482bddc1ae9b)#define ARDUINO\_PIN\_9 12

[ 23](emsdp-pinctrl_8h.md#a0a6f8661753df638c06695364980fdbb)#define ARDUINO\_PIN\_10 13

[ 24](emsdp-pinctrl_8h.md#a9387f1733914a0fc5938510573282a35)#define ARDUINO\_PIN\_11 14

[ 25](emsdp-pinctrl_8h.md#a34be4848158ca64f9ad7723ab2e3ea66)#define ARDUINO\_PIN\_12 15

[ 26](emsdp-pinctrl_8h.md#a1bd18a419e095cdfe447689fdcd196be)#define ARDUINO\_PIN\_13 16

[ 27](emsdp-pinctrl_8h.md#addf72d6c5939a165f880f5af2697d5ed)#define ARDUINO\_PIN\_AD0 17

[ 28](emsdp-pinctrl_8h.md#a4c596158e197cf793d779851e071de4f)#define ARDUINO\_PIN\_AD1 18

[ 29](emsdp-pinctrl_8h.md#a73669f8af7e092ddde87a739ce596bac)#define ARDUINO\_PIN\_AD2 19

[ 30](emsdp-pinctrl_8h.md#a84eb57d06a2dc41118e6127f33cd0319)#define ARDUINO\_PIN\_AD3 20

[ 31](emsdp-pinctrl_8h.md#ad99538f6aaa63c918ce4390d2a38373f)#define ARDUINO\_PIN\_AD4 21

[ 32](emsdp-pinctrl_8h.md#ae1c52d372a374566fcd122123c1fcf57)#define ARDUINO\_PIN\_AD5 22

[ 33](emsdp-pinctrl_8h.md#abf7781624ba129f1a537d56aa2bac01e)#define UNMUXED\_PIN 23

34

[ 35](emsdp-pinctrl_8h.md#abb36b48a04e5abd4e22ab56744ae1b37)#define PMOD\_GPIO 0

[ 36](emsdp-pinctrl_8h.md#a9111f3995638bedae3ee9220cc0c5a68)#define PMOD\_UARTA 1

[ 37](emsdp-pinctrl_8h.md#a88f4a41ed095c3f5aa209bc6cad15b22)#define PMOD\_UARTB 2

[ 38](emsdp-pinctrl_8h.md#aea0ba40189cebd5c8406e77d648e01fd)#define PMOD\_SPI 3

[ 39](emsdp-pinctrl_8h.md#a0cc7225a1454d158b9fa65809cf834aa)#define PMOD\_I2C 4

[ 40](emsdp-pinctrl_8h.md#a736c7c925872797a21ccf2ea65808ef3)#define PMOD\_PWM\_MODE1 5

[ 41](emsdp-pinctrl_8h.md#a57392e5d0e3cc75e60b383ec80def9b0)#define PMOD\_PWM\_MODE2 6

[ 42](emsdp-pinctrl_8h.md#ad0035019700eb6a69270c16a374188cb)#define PMOD\_PWM\_MODE3 7

[ 43](emsdp-pinctrl_8h.md#a3be02cd4af84cacb1127464d8e999cf1)#define ARDUINO\_GPIO 8

[ 44](emsdp-pinctrl_8h.md#a9b66efcf31ffd935735691c1827cd14e)#define ARDUINO\_UART 9

[ 45](emsdp-pinctrl_8h.md#ad5cafc3df8b742439455acce87a9ef99)#define ARDUINO\_SPI 10

[ 46](emsdp-pinctrl_8h.md#aeb8771f0409c18b445525e92eb3c875b)#define ARDUINO\_I2C 11

[ 47](emsdp-pinctrl_8h.md#a0526d4e7f01317e0b4d43726bb32f8c1)#define ARDUINO\_PWM 12

[ 48](emsdp-pinctrl_8h.md#a7d29cce436d0b1dbeb7d89b0e26b0447)#define ARDUINO\_ADC 13

[ 49](emsdp-pinctrl_8h.md#a4535604664cddc3ddd4559945f0c876b)#define NOT\_PINMUX 14

50

51

52#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_EMSDP\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [emsdp-pinctrl.h](emsdp-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
