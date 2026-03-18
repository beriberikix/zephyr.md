---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smartbond-pinctrl_8h_source.html
original_path: doxygen/html/smartbond-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smartbond-pinctrl.h

[Go to the documentation of this file.](smartbond-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2022, Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SMARTBOND\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SMARTBOND\_PINCTRL\_H\_

9

[ 11](smartbond-pinctrl_8h.md#a7089e1e95fff22ba99344704b7f731b7)#define SMARTBOND\_FUNC\_GPIO 0

[ 12](smartbond-pinctrl_8h.md#a6ed07d7b66f1b82356a972237319ac9b)#define SMARTBOND\_FUNC\_UART\_RX 1

[ 13](smartbond-pinctrl_8h.md#a5dfe9979613105acf742ea4c64afb8f2)#define SMARTBOND\_FUNC\_UART\_TX 2

[ 14](smartbond-pinctrl_8h.md#ad9b9d93fd00717dba1a32feac99a760a)#define SMARTBOND\_FUNC\_UART2\_RX 3

[ 15](smartbond-pinctrl_8h.md#ab8dc0782b4c39f9f04bffbd68e201b07)#define SMARTBOND\_FUNC\_UART2\_TX 4

[ 16](smartbond-pinctrl_8h.md#a28291720995487ed1909701d27bb6608)#define SMARTBOND\_FUNC\_UART2\_CTSN 5

[ 17](smartbond-pinctrl_8h.md#aea2618531f8eca9f53a66df1c2e40cbe)#define SMARTBOND\_FUNC\_UART2\_RTSN 6

[ 18](smartbond-pinctrl_8h.md#a5b3943d551d13bdd36407145262a56f9)#define SMARTBOND\_FUNC\_UART3\_RX 7

[ 19](smartbond-pinctrl_8h.md#aa0d293e2a1c45c9f4a8b33b81d0efe09)#define SMARTBOND\_FUNC\_UART3\_TX 8

[ 20](smartbond-pinctrl_8h.md#ab78ba1d4ce9f4551480a8245439607f2)#define SMARTBOND\_FUNC\_UART3\_CTSN 9

[ 21](smartbond-pinctrl_8h.md#a34305c8d6c03afebd72736e274f34c86)#define SMARTBOND\_FUNC\_UART3\_RTSN 10

[ 22](smartbond-pinctrl_8h.md#acf912059ad7e32d8241f6c7881c4cb28)#define SMARTBOND\_FUNC\_ISO\_CLK 11

[ 23](smartbond-pinctrl_8h.md#aac93ef7075ed12f86b829bd705c7400a)#define SMARTBOND\_FUNC\_ISO\_DATA 12

[ 24](smartbond-pinctrl_8h.md#a43277e708883b30efd1fa2360801c9ea)#define SMARTBOND\_FUNC\_SPI\_DI 13

[ 25](smartbond-pinctrl_8h.md#a64d7cd483d90e3b1102243c191d189eb)#define SMARTBOND\_FUNC\_SPI\_DO 14

[ 26](smartbond-pinctrl_8h.md#a7b9f3eec74e21b5b2aaef12c234bea64)#define SMARTBOND\_FUNC\_SPI\_CLK 15

[ 27](smartbond-pinctrl_8h.md#a41d2f9824fb7d591b61482431b39d049)#define SMARTBOND\_FUNC\_SPI\_EN 16

[ 28](smartbond-pinctrl_8h.md#acab6331b3ee09ed93b7963c9e3c4e0e7)#define SMARTBOND\_FUNC\_SPI2\_DI 17

[ 29](smartbond-pinctrl_8h.md#ae0282ae5f03793c9c8af9d7affeefe23)#define SMARTBOND\_FUNC\_SPI2\_DO 18

[ 30](smartbond-pinctrl_8h.md#abb67eca8ba3b48ab5436a4609f1a633f)#define SMARTBOND\_FUNC\_SPI2\_CLK 19

[ 31](smartbond-pinctrl_8h.md#abe46de2948d1c93a938511a78f7a762f)#define SMARTBOND\_FUNC\_SPI2\_EN 20

[ 32](smartbond-pinctrl_8h.md#a5b5f41a1016d0430196ee473cbc7a2c5)#define SMARTBOND\_FUNC\_I2C\_SCL 21

[ 33](smartbond-pinctrl_8h.md#a3a8535069c0b427b0f970248563739fe)#define SMARTBOND\_FUNC\_I2C\_SDA 22

[ 34](smartbond-pinctrl_8h.md#ada4dba2404b4f79eb57ad2a8865c94e4)#define SMARTBOND\_FUNC\_I2C2\_SCL 23

[ 35](smartbond-pinctrl_8h.md#ac456dcf0d16f720e6f19459eb11f7ef3)#define SMARTBOND\_FUNC\_I2C2\_SDA 24

[ 36](smartbond-pinctrl_8h.md#a5613a9d97ed91227f724e632cd3a995a)#define SMARTBOND\_FUNC\_USB\_SOF 25

[ 37](smartbond-pinctrl_8h.md#a93ae4c46ba7233a074cae8a9750e3246)#define SMARTBOND\_FUNC\_ADC 26

[ 38](smartbond-pinctrl_8h.md#af55696a1a2c476841085901eb030bf06)#define SMARTBOND\_FUNC\_USB 27

[ 39](smartbond-pinctrl_8h.md#aa8f8d6b30ff693e02863aebce0fda1f7)#define SMARTBOND\_FUNC\_PCM\_DI 28

[ 40](smartbond-pinctrl_8h.md#a8d2af85827bae92e3323ae7af6795d39)#define SMARTBOND\_FUNC\_PCM\_DO 29

[ 41](smartbond-pinctrl_8h.md#a0350a10a2a18f35042eb1d1380d06e71)#define SMARTBOND\_FUNC\_PCM\_FSC 30

[ 42](smartbond-pinctrl_8h.md#ab966d361e29c0a4bec64edb8f1f13fcd)#define SMARTBOND\_FUNC\_PCM\_CLK 31

[ 43](smartbond-pinctrl_8h.md#a41038d013590b0fa06e0009071e77913)#define SMARTBOND\_FUNC\_PDM\_DATA 32

[ 44](smartbond-pinctrl_8h.md#a9c6dc0a72667b6659761fb900e6cb74e)#define SMARTBOND\_FUNC\_PDM\_CLK 33

[ 45](smartbond-pinctrl_8h.md#a10e19e7f0d69a912341211e18d88d9fb)#define SMARTBOND\_FUNC\_COEX\_EXT\_ACT 34

[ 46](smartbond-pinctrl_8h.md#a7e470cb7f8deb22199ac0fb2ec7e6867)#define SMARTBOND\_FUNC\_COEX\_SMART\_ACT 35

[ 47](smartbond-pinctrl_8h.md#a17ad842b2c1dfa9f7d2cf8ec9ec67589)#define SMARTBOND\_FUNC\_COEX\_SMART\_PRI 36

[ 48](smartbond-pinctrl_8h.md#ada643666dd9d0e7423c01b1852d01e08)#define SMARTBOND\_FUNC\_PORT0\_DCF 37

[ 49](smartbond-pinctrl_8h.md#a633ffca67ab63d296c82588a16717ecd)#define SMARTBOND\_FUNC\_PORT1\_DCF 38

[ 50](smartbond-pinctrl_8h.md#ae269c4303f7cbb595d015805870d489a)#define SMARTBOND\_FUNC\_PORT2\_DCF 39

[ 51](smartbond-pinctrl_8h.md#aee13677eb591c737d9aa87a56d5ab60e)#define SMARTBOND\_FUNC\_PORT3\_DCF 40

[ 52](smartbond-pinctrl_8h.md#a575776c065bdf0795f03931ef32a8014)#define SMARTBOND\_FUNC\_PORT4\_DCF 41

[ 53](smartbond-pinctrl_8h.md#adf15b25b1e76a63945454870bf8a5880)#define SMARTBOND\_FUNC\_CLOCK 42

[ 54](smartbond-pinctrl_8h.md#a2710985bfb03536edebe925e42701372)#define SMARTBOND\_FUNC\_PG 43

[ 55](smartbond-pinctrl_8h.md#a7131a57cb82a1fc7dff9e626dfaed3fa)#define SMARTBOND\_FUNC\_LCD 44

[ 56](smartbond-pinctrl_8h.md#ac101bc374eb5a717b7bf8188683c2f2e)#define SMARTBOND\_FUNC\_LCD\_SPI\_DC 45

[ 57](smartbond-pinctrl_8h.md#a02d15016a20227a7470db3ce37b32ae9)#define SMARTBOND\_FUNC\_LCD\_SPI\_DO 46

[ 58](smartbond-pinctrl_8h.md#ae17f0095eb1536bf0f477618d7f7d074)#define SMARTBOND\_FUNC\_LCD\_SPI\_CLK 47

[ 59](smartbond-pinctrl_8h.md#af7e0123b209509f766bdee6fd5473456)#define SMARTBOND\_FUNC\_LCD\_SPI\_EN 48

[ 60](smartbond-pinctrl_8h.md#afe4022d7379a973034954b15e838f90c)#define SMARTBOND\_FUNC\_TIM\_PWM 49

[ 61](smartbond-pinctrl_8h.md#a107f8c0c3a54d5fb01efa35f31edc6f9)#define SMARTBOND\_FUNC\_TIM2\_PWM 50

[ 62](smartbond-pinctrl_8h.md#aa569b7d607bb41d6cc856e177aa2aff9)#define SMARTBOND\_FUNC\_TIM\_1SHOT 51

[ 63](smartbond-pinctrl_8h.md#af9ed3f5a6c23379de2cdc58ce2856e66)#define SMARTBOND\_FUNC\_TIM2\_1SHOT 52

[ 64](smartbond-pinctrl_8h.md#a5a613b7538c4ae1252375f36f71128c4)#define SMARTBOND\_FUNC\_TIM3\_PWM 53

[ 65](smartbond-pinctrl_8h.md#a4aee45714b4104a48e1bebbcae2a1660)#define SMARTBOND\_FUNC\_TIM4\_PWM 54

66

[ 68](smartbond-pinctrl_8h.md#a50e52287199ec82f928e24e9d12fa97b)#define SMARTBOND\_PINMUX\_PIN\_POS 0

[ 69](smartbond-pinctrl_8h.md#ae48f1167f7190d6acc13d1890ec6f141)#define SMARTBOND\_PINMUX\_PIN\_MASK 0x1f

[ 70](smartbond-pinctrl_8h.md#ab4cec4ecf671814e804cb3ad18236ac4)#define SMARTBOND\_PINMUX\_PORT\_POS 5

[ 71](smartbond-pinctrl_8h.md#a8e82ad973c84c8b36240821fda17c07b)#define SMARTBOND\_PINMUX\_PORT\_MASK 0x01

[ 72](smartbond-pinctrl_8h.md#a0ed3e3f31e62d585a48fdfa04decf854)#define SMARTBOND\_PINMUX\_FUNC\_POS 6

[ 73](smartbond-pinctrl_8h.md#a4dae490f035db9e564d95cb62ceb101c)#define SMARTBOND\_PINMUX\_FUNC\_MASK 0xff

74

[ 76](smartbond-pinctrl_8h.md#a66c942c39b093b0dbd3d174d6265600c)#define SMARTBOND\_PINMUX(func, port, pin) \

77 (((SMARTBOND\_FUNC\_ ## func) << SMARTBOND\_PINMUX\_FUNC\_POS) | \

78 ((port) << SMARTBOND\_PINMUX\_PORT\_POS) | \

79 (pin) << SMARTBOND\_PINMUX\_PIN\_POS)

80

81#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SMARTBOND\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [smartbond-pinctrl.h](smartbond-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
