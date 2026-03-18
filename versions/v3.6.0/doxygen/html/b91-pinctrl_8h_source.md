---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/b91-pinctrl_8h_source.html
original_path: doxygen/html/b91-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

b91-pinctrl.h

[Go to the documentation of this file.](b91-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2021 Telink Semiconductor

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_B91\_PINCTRL\_COMMON\_H\_

8#define ZEPHYR\_B91\_PINCTRL\_COMMON\_H\_

9

10/\* IDs for GPIO functions \*/

11

[ 12](b91-pinctrl_8h.md#af74802aac35370a78d734c183d065927)#define B91\_FUNC\_A 0x00

[ 13](b91-pinctrl_8h.md#a80e3477cd2f866955e3e61712e88fe15)#define B91\_FUNC\_B 0x01

[ 14](b91-pinctrl_8h.md#ae00f63d1146dc5aa3e3fb586672be187)#define B91\_FUNC\_C 0x02

15

16/\* IDs for GPIO Ports \*/

17

[ 18](b91-pinctrl_8h.md#aafb690574da4bba9bd1394013a3b8c5f)#define B91\_PORT\_A 0x00

[ 19](b91-pinctrl_8h.md#a7a07ae7763882f9dde2372bfd2e7ed5f)#define B91\_PORT\_B 0x01

[ 20](b91-pinctrl_8h.md#a31164e5af693e763aee5a65f2566e71b)#define B91\_PORT\_C 0x02

[ 21](b91-pinctrl_8h.md#a85a32b0056d25e1b65495e94aefb0b0d)#define B91\_PORT\_D 0x03

[ 22](b91-pinctrl_8h.md#a4eb94b2b81a87fc1868752a1f23e19b9)#define B91\_PORT\_E 0x04

23

24/\* IDs for GPIO Pins \*/

25

[ 26](b91-pinctrl_8h.md#a26acab82d9dfd476f8ad2234463de25e)#define B91\_PIN\_0 0x01

[ 27](b91-pinctrl_8h.md#af5abb58004aebaddfd3536e3e7431032)#define B91\_PIN\_1 0x02

[ 28](b91-pinctrl_8h.md#a3bebe3d7a004486830f25887ba6784e4)#define B91\_PIN\_2 0x04

[ 29](b91-pinctrl_8h.md#a564cda0e7550d1ac7eade1a6478e6c5f)#define B91\_PIN\_3 0x08

[ 30](b91-pinctrl_8h.md#a4d4c50821490a48bf5c180d38e6562f7)#define B91\_PIN\_4 0x10

[ 31](b91-pinctrl_8h.md#aab839f7de5cd44c6501aa87918377e63)#define B91\_PIN\_5 0x20

[ 32](b91-pinctrl_8h.md#ad560e7cd90341acb45bcf7f971f50344)#define B91\_PIN\_6 0x40

[ 33](b91-pinctrl_8h.md#a1daded0f866fbeecc396ce8b460dfaf4)#define B91\_PIN\_7 0x80

34

35/\* B91 pinctrl pull-up/down \*/

36

[ 37](b91-pinctrl_8h.md#ab92d8f065db3db13bdf6f34681dba5f5)#define B91\_PULL\_NONE 0

[ 38](b91-pinctrl_8h.md#adabf515b2ca84d1b392128de1ca2c784)#define B91\_PULL\_DOWN 2

[ 39](b91-pinctrl_8h.md#aca2b2bc1fe29735ad65a7b498473b3fc)#define B91\_PULL\_UP 3

40

41/\* Pin function positions \*/

42

[ 43](b91-pinctrl_8h.md#a878ccfc0e6ee8b60108529fdde076434)#define B91\_PIN\_0\_FUNC\_POS 0x00

[ 44](b91-pinctrl_8h.md#a650fe8f7c3f5fb117149922d7e6fd4b2)#define B91\_PIN\_1\_FUNC\_POS 0x02

[ 45](b91-pinctrl_8h.md#af06c878c2b3ed58fbc216df02e2bd441)#define B91\_PIN\_2\_FUNC\_POS 0x04

[ 46](b91-pinctrl_8h.md#aa892ca9aafc68810179f074fe3977bdb)#define B91\_PIN\_3\_FUNC\_POS 0x06

[ 47](b91-pinctrl_8h.md#a29c13feae83222745e41d0533ab79028)#define B91\_PIN\_4\_FUNC\_POS 0x00

[ 48](b91-pinctrl_8h.md#a39e7598c002022c51c4756841c19765b)#define B91\_PIN\_5\_FUNC\_POS 0x02

[ 49](b91-pinctrl_8h.md#a1add045066251ac9562dbe9c957600ec)#define B91\_PIN\_6\_FUNC\_POS 0x04

[ 50](b91-pinctrl_8h.md#ad9b891a9dadf35a028978d9cab96821b)#define B91\_PIN\_7\_FUNC\_POS 0x06

51

52/\* B91 pin configuration bit field positions and masks \*/

53

[ 54](b91-pinctrl_8h.md#acd069bef9c0ea38053d084042549e2c4)#define B91\_PULL\_POS 19

[ 55](b91-pinctrl_8h.md#a63f6911e764836b3a3357352b2a88a86)#define B91\_PULL\_MSK 0x3

[ 56](b91-pinctrl_8h.md#a3d36f61c5c08be8735749041347680e4)#define B91\_FUNC\_POS 16

[ 57](b91-pinctrl_8h.md#a78cdf57b4bcbefaf7459a45cf35e9612)#define B91\_FUNC\_MSK 0x3

[ 58](b91-pinctrl_8h.md#a1de5dc69a54207b3aeb315df26e9fbce)#define B91\_PORT\_POS 8

[ 59](b91-pinctrl_8h.md#a05301516ef9160c2e7e12464034ca5f4)#define B91\_PORT\_MSK 0xFF

[ 60](b91-pinctrl_8h.md#add4262e10e4c8f626e4e5f29a794d8ad)#define B91\_PIN\_POS 0

[ 61](b91-pinctrl_8h.md#ad623894f4b0db2e5ccee6c481f36e096)#define B91\_PIN\_MSK 0xFFFF

[ 62](b91-pinctrl_8h.md#a31bc586c21d89de9ae8f56febbc9b6af)#define B91\_PIN\_ID\_MSK 0xFF

63

64/\* Setters and getters \*/

65

[ 66](b91-pinctrl_8h.md#af803cc8ae922bcf9ec7890173163c884)#define B91\_PINMUX\_SET(port, pin, func) ((func << B91\_FUNC\_POS) | \

67 (port << B91\_PORT\_POS) | \

68 (pin << B91\_PIN\_POS))

[ 69](b91-pinctrl_8h.md#a0859825b3954344a5fa3b81b5f2e709b)#define B91\_PINMUX\_GET\_PULL(pinmux) ((pinmux >> B91\_PULL\_POS) & B91\_PULL\_MSK)

[ 70](b91-pinctrl_8h.md#abde379851baa2cf7678a2c12a66f7056)#define B91\_PINMUX\_GET\_FUNC(pinmux) ((pinmux >> B91\_FUNC\_POS) & B91\_FUNC\_MSK)

[ 71](b91-pinctrl_8h.md#a3deef9c25fa8d14801cd406f0d56b153)#define B91\_PINMUX\_GET\_PIN(pinmux) ((pinmux >> B91\_PIN\_POS) & B91\_PIN\_MSK)

[ 72](b91-pinctrl_8h.md#ac79594fdd959968e627091f6f57a89eb)#define B91\_PINMUX\_GET\_PIN\_ID(pinmux) ((pinmux >> B91\_PIN\_POS) & B91\_PIN\_ID\_MSK)

73

74#endif /\* ZEPHYR\_B91\_PINCTRL\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [b91-pinctrl.h](b91-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
