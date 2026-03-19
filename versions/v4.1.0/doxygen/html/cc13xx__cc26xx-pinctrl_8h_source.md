---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cc13xx__cc26xx-pinctrl_8h_source.html
original_path: doxygen/html/cc13xx__cc26xx-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cc13xx\_cc26xx-pinctrl.h

[Go to the documentation of this file.](cc13xx__cc26xx-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2015 - 2017, Texas Instruments Incorporated

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef CC13XX\_CC26XX\_PINCTRL\_COMMON\_H\_

8#define CC13XX\_CC26XX\_PINCTRL\_COMMON\_H\_

9

10/\* Adapted from hal/ti/simplelink/source/ti/devices/cc13x2\_cc26x2/driverlib/ioc.h \*/

11

12/\* IOC Peripheral Port Mapping \*/

[ 13](cc13xx__cc26xx-pinctrl_8h.md#a28f8e101ae30e86989a5c7b35be8f2d1)#define IOC\_PORT\_GPIO 0x00000000 /\* Default general purpose IO usage \*/

[ 14](cc13xx__cc26xx-pinctrl_8h.md#a2dade73b9db2292ee357ec1ae92ed2d0)#define IOC\_PORT\_AON\_CLK32K 0x00000007 /\* AON External 32kHz clock \*/

[ 15](cc13xx__cc26xx-pinctrl_8h.md#a1b04b35124c351075fe3974adeb4d9aa)#define IOC\_PORT\_AUX\_IO 0x00000008 /\* AUX IO Pin \*/

[ 16](cc13xx__cc26xx-pinctrl_8h.md#a3ee91cd12de013161c91f231676b279c)#define IOC\_PORT\_MCU\_SSI0\_RX 0x00000009 /\* MCU SSI0 Receive Pin \*/

[ 17](cc13xx__cc26xx-pinctrl_8h.md#a984735dec2b09061ab1be699a708367f)#define IOC\_PORT\_MCU\_SSI0\_TX 0x0000000A /\* MCU SSI0 Transmit Pin \*/

[ 18](cc13xx__cc26xx-pinctrl_8h.md#a5e72bbc3a52d1bd643059f9a2037db03)#define IOC\_PORT\_MCU\_SSI0\_FSS 0x0000000B /\* MCU SSI0 FSS Pin \*/

[ 19](cc13xx__cc26xx-pinctrl_8h.md#acfeabd6ba536f550b52c98eba600f99c)#define IOC\_PORT\_MCU\_SSI0\_CLK 0x0000000C /\* MCU SSI0 Clock Pin \*/

[ 20](cc13xx__cc26xx-pinctrl_8h.md#aa318c337f1371b5f81ebf427a43cf318)#define IOC\_PORT\_MCU\_I2C\_MSSDA 0x0000000D /\* MCU I2C Data Pin \*/

[ 21](cc13xx__cc26xx-pinctrl_8h.md#a7d3e1312e3803326770e4d734e25b2eb)#define IOC\_PORT\_MCU\_I2C\_MSSCL 0x0000000E /\* MCU I2C Clock Pin \*/

[ 22](cc13xx__cc26xx-pinctrl_8h.md#aab1fbb3fbc8a90bd4d8fb1b55f69eb44)#define IOC\_PORT\_MCU\_UART0\_RX 0x0000000F /\* MCU UART0 Receive Pin \*/

[ 23](cc13xx__cc26xx-pinctrl_8h.md#ac1adc319c3a412383fbd03d4dc9f08f5)#define IOC\_PORT\_MCU\_UART0\_TX 0x00000010 /\* MCU UART0 Transmit Pin \*/

[ 24](cc13xx__cc26xx-pinctrl_8h.md#ad86b00b6011d22d55d31c8c2681edea8)#define IOC\_PORT\_MCU\_UART0\_CTS 0x00000011 /\* MCU UART0 Clear To Send Pin \*/

[ 25](cc13xx__cc26xx-pinctrl_8h.md#acdc4b3216e14a0525a9bff563c618505)#define IOC\_PORT\_MCU\_UART0\_RTS 0x00000012 /\* MCU UART0 Request To Send Pin \*/

[ 26](cc13xx__cc26xx-pinctrl_8h.md#a81eb684c41b27ab5c2e434f74cac653a)#define IOC\_PORT\_MCU\_UART1\_RX 0x00000013 /\* MCU UART1 Receive Pin \*/

[ 27](cc13xx__cc26xx-pinctrl_8h.md#aabad6396786ac0fba4e030fa3bafaebe)#define IOC\_PORT\_MCU\_UART1\_TX 0x00000014 /\* MCU UART1 Transmit Pin \*/

[ 28](cc13xx__cc26xx-pinctrl_8h.md#a3891eea57014086f4d9665c5659df9f9)#define IOC\_PORT\_MCU\_UART1\_CTS 0x00000015 /\* MCU UART1 Clear To Send Pin \*/

[ 29](cc13xx__cc26xx-pinctrl_8h.md#a07f27135f53b5f70c9cf611fee1da81c)#define IOC\_PORT\_MCU\_UART1\_RTS 0x00000016 /\* MCU UART1 Request To Send Pin \*/

[ 30](cc13xx__cc26xx-pinctrl_8h.md#abb2e44fdb358359785db59197e43bf77)#define IOC\_PORT\_MCU\_PORT\_EVENT0 0x00000017 /\* MCU PORT EVENT 0 \*/

[ 31](cc13xx__cc26xx-pinctrl_8h.md#a53158c583bdc22b05a3ab803976f86f3)#define IOC\_PORT\_MCU\_PORT\_EVENT1 0x00000018 /\* MCU PORT EVENT 1 \*/

[ 32](cc13xx__cc26xx-pinctrl_8h.md#a3c31d2aee7d57f0b939678d24489b288)#define IOC\_PORT\_MCU\_PORT\_EVENT2 0x00000019 /\* MCU PORT EVENT 2 \*/

[ 33](cc13xx__cc26xx-pinctrl_8h.md#af74865ea575600cdef510d96b765fcaa)#define IOC\_PORT\_MCU\_PORT\_EVENT3 0x0000001A /\* MCU PORT EVENT 3 \*/

[ 34](cc13xx__cc26xx-pinctrl_8h.md#a8c29bb202c04366637a067403cb04798)#define IOC\_PORT\_MCU\_PORT\_EVENT4 0x0000001B /\* MCU PORT EVENT 4 \*/

[ 35](cc13xx__cc26xx-pinctrl_8h.md#a5018eb7bb384ce6240bc5ce37f684fd4)#define IOC\_PORT\_MCU\_PORT\_EVENT5 0x0000001C /\* MCU PORT EVENT 5 \*/

[ 36](cc13xx__cc26xx-pinctrl_8h.md#a627f8281323ce4d84edc61c921e5fc35)#define IOC\_PORT\_MCU\_PORT\_EVENT6 0x0000001D /\* MCU PORT EVENT 6 \*/

[ 37](cc13xx__cc26xx-pinctrl_8h.md#ae058c9773b968e08c17f848e8a17e33e)#define IOC\_PORT\_MCU\_PORT\_EVENT7 0x0000001E /\* MCU PORT EVENT 7 \*/

[ 38](cc13xx__cc26xx-pinctrl_8h.md#a5bf13b897900e2f62c82d84d23558c9b)#define IOC\_PORT\_MCU\_SWV 0x00000020 /\* Serial Wire Viewer \*/

[ 39](cc13xx__cc26xx-pinctrl_8h.md#adc4c2aa534badaa6a40a994012968226)#define IOC\_PORT\_MCU\_SSI1\_RX 0x00000021 /\* MCU SSI1 Receive Pin \*/

[ 40](cc13xx__cc26xx-pinctrl_8h.md#a9024a0c4d78a72ff56c12d9ef6bce984)#define IOC\_PORT\_MCU\_SSI1\_TX 0x00000022 /\* MCU SSI1 Transmit Pin \*/

[ 41](cc13xx__cc26xx-pinctrl_8h.md#a8517079f7b23895467d0c6c5cee74051)#define IOC\_PORT\_MCU\_SSI1\_FSS 0x00000023 /\* MCU SSI1 FSS Pin \*/

[ 42](cc13xx__cc26xx-pinctrl_8h.md#aa657dc9b3b551a535207a5c70944c7ad)#define IOC\_PORT\_MCU\_SSI1\_CLK 0x00000024 /\* MCU SSI1 Clock Pin \*/

[ 43](cc13xx__cc26xx-pinctrl_8h.md#ad8d7633125f181d03a832504ca0333af)#define IOC\_PORT\_MCU\_I2S\_AD0 0x00000025 /\* MCU I2S Data Pin 0 \*/

[ 44](cc13xx__cc26xx-pinctrl_8h.md#a3e3c593f43d20f8b976104e4370e2bfe)#define IOC\_PORT\_MCU\_I2S\_AD1 0x00000026 /\* MCU I2S Data Pin 1 \*/

[ 45](cc13xx__cc26xx-pinctrl_8h.md#a87f51f7808c53fb7a1d0ab0cfc7c3bfb)#define IOC\_PORT\_MCU\_I2S\_WCLK 0x00000027 /\* MCU I2S Frame/Word Clock \*/

[ 46](cc13xx__cc26xx-pinctrl_8h.md#a27b5fe5cdbd768684939c52662ed919a)#define IOC\_PORT\_MCU\_I2S\_BCLK 0x00000028 /\* MCU I2S Bit Clock \*/

[ 47](cc13xx__cc26xx-pinctrl_8h.md#a72287ec0a2c5f0423e785d3e371a120e)#define IOC\_PORT\_MCU\_I2S\_MCLK 0x00000029 /\* MCU I2S Master clock 2 \*/

[ 48](cc13xx__cc26xx-pinctrl_8h.md#ae6a1e66015d48324657ede92613381be)#define IOC\_PORT\_RFC\_TRC 0x0000002E /\* RF Core Tracer \*/

[ 49](cc13xx__cc26xx-pinctrl_8h.md#a00a019e1ddf52b2913e8358c18095ed4)#define IOC\_PORT\_RFC\_GPO0 0x0000002F /\* RC Core Data Out Pin 0 \*/

[ 50](cc13xx__cc26xx-pinctrl_8h.md#a00ea75c9456ac6b11e666757750ae342)#define IOC\_PORT\_RFC\_GPO1 0x00000030 /\* RC Core Data Out Pin 1 \*/

[ 51](cc13xx__cc26xx-pinctrl_8h.md#a5f19fce0ef7c834714af2e7f1c2bd06d)#define IOC\_PORT\_RFC\_GPO2 0x00000031 /\* RC Core Data Out Pin 2 \*/

[ 52](cc13xx__cc26xx-pinctrl_8h.md#ac940779073013ae6912da19fe598d999)#define IOC\_PORT\_RFC\_GPO3 0x00000032 /\* RC Core Data Out Pin 3 \*/

[ 53](cc13xx__cc26xx-pinctrl_8h.md#af0c7ce805a62bed97029d997406e8ec7)#define IOC\_PORT\_RFC\_GPI0 0x00000033 /\* RC Core Data In Pin 0 \*/

[ 54](cc13xx__cc26xx-pinctrl_8h.md#a6f1fc00a44a3311866187ce0c7470b1f)#define IOC\_PORT\_RFC\_GPI1 0x00000034 /\* RC Core Data In Pin 1 \*/

[ 55](cc13xx__cc26xx-pinctrl_8h.md#a34286b14818f96f8e3955eebc3f453eb)#define IOC\_PORT\_RFC\_SMI\_DL\_OUT 0x00000035 /\* RF Core SMI Data Link Out \*/

[ 56](cc13xx__cc26xx-pinctrl_8h.md#a38268821c556568eb9b8d0bd1b6bf4a4)#define IOC\_PORT\_RFC\_SMI\_DL\_IN 0x00000036 /\* RF Core SMI Data Link in \*/

[ 57](cc13xx__cc26xx-pinctrl_8h.md#a8fa600a45bb7210a0a869232883a36d7)#define IOC\_PORT\_RFC\_SMI\_CL\_OUT 0x00000037 /\* RF Core SMI Command Link Out \*/

[ 58](cc13xx__cc26xx-pinctrl_8h.md#a8955bb4c29c837e71983307d2fc46155)#define IOC\_PORT\_RFC\_SMI\_CL\_IN 0x00000038 /\* RF Core SMI Command Link In \*/

59

60/\* Edge Detection \*/

[ 61](cc13xx__cc26xx-pinctrl_8h.md#a86134934e741c66f26bd4490e1f48553)#define IOC\_NO\_EDGE 0x00000000 /\* No edge detection \*/

[ 62](cc13xx__cc26xx-pinctrl_8h.md#a812505ce5828cd40a9030f37445b7860)#define IOC\_FALLING\_EDGE 0x00010000 /\* Edge detection on falling edge \*/

[ 63](cc13xx__cc26xx-pinctrl_8h.md#ac7124cf50c094bfc24313d88aa8c06f4)#define IOC\_RISING\_EDGE 0x00020000 /\* Edge detection on rising edge \*/

[ 64](cc13xx__cc26xx-pinctrl_8h.md#aff5b936c3bbd5bd0e9429c8c7ac5f6a8)#define IOC\_BOTH\_EDGES 0x00030000 /\* Edge detection on both edges \*/

65

66#endif /\* CC13XX\_CC26XX\_PINCTRL\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [cc13xx\_cc26xx-pinctrl.h](cc13xx__cc26xx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
