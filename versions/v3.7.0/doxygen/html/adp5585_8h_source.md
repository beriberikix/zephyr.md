---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/adp5585_8h_source.html
original_path: doxygen/html/adp5585_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adp5585.h

[Go to the documentation of this file.](adp5585_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_ADP5585\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_ADP5585\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/device.h](device_8h.md)>

[ 14](adp5585_8h.md#afbd61635aa229f364824b9e84e96c7fa)#define ADP5585\_ID 0x00

[ 15](adp5585_8h.md#a0a6c9fc68d3bc48ec43a4a27c7f973dd)#define ADP5585\_INT\_STATUS 0x01

[ 16](adp5585_8h.md#a40d6f40ae61983958ae73d09eff68718)#define ADP5585\_STATUS 0x02

[ 17](adp5585_8h.md#afa83f7aace2fd46cf64e559bed0b11f0)#define ADP5585\_FIFO\_1 0x03

[ 18](adp5585_8h.md#a72d2335efa6fbabe89f1844b8bec2f70)#define ADP5585\_FIFO\_2 0x04

[ 19](adp5585_8h.md#a764a0a9a8b8ab3efabe00e547eb1dfea)#define ADP5585\_FIFO\_3 0x05

[ 20](adp5585_8h.md#a7e09ac2966e14165e9d1da7e8ad4b3f2)#define ADP5585\_FIFO\_4 0x06

[ 21](adp5585_8h.md#a41b6a6efcce33c063712d13f878f758c)#define ADP5585\_FIFO\_5 0x07

[ 22](adp5585_8h.md#a2e780a11e8498724fa6a169c86f6492b)#define ADP5585\_FIFO\_6 0x08

[ 23](adp5585_8h.md#a3e1738db835ff08fa2116145b16f0fa4)#define ADP5585\_FIFO\_7 0x09

[ 24](adp5585_8h.md#a5a60166191e51b418a80123e0bbf47c4)#define ADP5585\_FIFO\_8 0x0A

[ 25](adp5585_8h.md#a49471e825aa64dbdd117dbf8f0a7cf5d)#define ADP5585\_FIFO\_9 0x0B

[ 26](adp5585_8h.md#a96c863ab3cf6d2167ad671fae97ddf18)#define ADP5585\_FIFO\_10 0x0C

[ 27](adp5585_8h.md#a053caf41bbaa3cbd93c12439f14e5d47)#define ADP5585\_FIFO\_11 0x0D

[ 28](adp5585_8h.md#a53716a13d1d427397915b3a3cbb34b2c)#define ADP5585\_FIFO\_12 0x0E

[ 29](adp5585_8h.md#ac57c89eff3b3cadd5ed3d0a73040c21f)#define ADP5585\_FIFO\_13 0x0F

[ 30](adp5585_8h.md#ac5c9f36e90531803c38d5096649638a3)#define ADP5585\_FIFO\_14 0x10

[ 31](adp5585_8h.md#a55ddf942d0a7636f28d9a67e4bd01377)#define ADP5585\_FIFO\_15 0x11

[ 32](adp5585_8h.md#a4a106aa7ac374e1b7234de740f062315)#define ADP5585\_FIFO\_16 0x12

[ 33](adp5585_8h.md#a969cbf249f8e61e004c03b9ad7a7f01a)#define ADP5585\_GPI\_INT\_STAT\_A 0x13

[ 34](adp5585_8h.md#a9cd52a6ab5a30a221f5b57c42845f366)#define ADP5585\_GPI\_INT\_STAT\_B 0x14

[ 35](adp5585_8h.md#a30acc2f2100514223ae1a1745f9c3c7b)#define ADP5585\_GPI\_STATUS\_A 0x15

[ 36](adp5585_8h.md#a96ad72c5cb57c33d2949446e5243bae0)#define ADP5585\_GPI\_STATUS\_B 0x16

[ 37](adp5585_8h.md#a8367cd959eaff77e026fc90521889b84)#define ADP5585\_RPULL\_CONFIG\_A 0x17

[ 38](adp5585_8h.md#ae76fa8a7688f59df166bf816ea9d472b)#define ADP5585\_RPULL\_CONFIG\_B 0x18

[ 39](adp5585_8h.md#ae3692e46404852668e15e60387c76e86)#define ADP5585\_RPULL\_CONFIG\_C 0x19

[ 40](adp5585_8h.md#a7dd9182b40ed99cd14f988cc781d9413)#define ADP5585\_RPULL\_CONFIG\_D 0x1A

[ 41](adp5585_8h.md#a67bad2472c7e78cf9e12c79550a882b9)#define ADP5585\_GPI\_INT\_LEVEL\_A 0x1B

[ 42](adp5585_8h.md#acc6fe6801de4102c2eaf841a9c42f3bd)#define ADP5585\_GPI\_INT\_LEVEL\_B 0x1C

[ 43](adp5585_8h.md#ad079e787ca2988308623a29ce238002b)#define ADP5585\_GPI\_EVENT\_EN\_A 0x1D

[ 44](adp5585_8h.md#a05059407f14853547d2d5e2d572e3efa)#define ADP5585\_GPI\_EVENT\_EN\_B 0x1E

[ 45](adp5585_8h.md#acc0487d4ed5b3321e5e7477e2e7069b0)#define ADP5585\_GPI\_INTERRUPT\_EN\_A 0x1F

[ 46](adp5585_8h.md#a7623e23c6e768028be5df6567234ea32)#define ADP5585\_GPI\_INTERRUPT\_EN\_B 0x20

[ 47](adp5585_8h.md#a4712d02875b88c125b1e25c746440a31)#define ADP5585\_DEBOUNCE\_DIS\_A 0x21

[ 48](adp5585_8h.md#ac907fc30a58a7ff2d91a69c1c87594c6)#define ADP5585\_DEBOUNCE\_DIS\_B 0x22

[ 49](adp5585_8h.md#a9daac58d194d0db90caad7a3e0efba96)#define ADP5585\_GPO\_DATA\_OUT\_A 0x23

[ 50](adp5585_8h.md#a4c3152925821be1bd99172d7e9a98dab)#define ADP5585\_GPO\_DATA\_OUT\_B 0x24

[ 51](adp5585_8h.md#a4d16b97199e23781b31a1903e9b26ae8)#define ADP5585\_GPO\_OUT\_MODE\_A 0x25

[ 52](adp5585_8h.md#a09edb76ab453c790bc7ba70544d1bbea)#define ADP5585\_GPO\_OUT\_MODE\_B 0x26

[ 53](adp5585_8h.md#afe9637fe22334d0014bdd65c71a743eb)#define ADP5585\_GPIO\_DIRECTION\_A 0x27

[ 54](adp5585_8h.md#aec18185b14f96c0d8f7d05ea5f2b7db8)#define ADP5585\_GPIO\_DIRECTION\_B 0x28

[ 55](adp5585_8h.md#a73dcbcf77052ad254453422edea750ef)#define ADP5585\_RESET1\_EVENT\_A 0x29

[ 56](adp5585_8h.md#ab73730cdd193626c32a2ec34eabcf3c9)#define ADP5585\_RESET1\_EVENT\_B 0x2A

[ 57](adp5585_8h.md#af8ee993d6eef733634f4d06953456284)#define ADP5585\_RESET1\_EVENT\_C 0x2B

[ 58](adp5585_8h.md#a4a6c163e0c60a590ac0311336159a76b)#define ADP5585\_RESET2\_EVENT\_A 0x2C

[ 59](adp5585_8h.md#ab4368b4309e193c178b70a0f56a8d82e)#define ADP5585\_RESET2\_EVENT\_B 0x2D

[ 60](adp5585_8h.md#a94eecacd78ca46744f5672c5d042ff07)#define ADP5585\_RESET\_CFG 0x2E

[ 61](adp5585_8h.md#a23a8f65d404b7c0bafd55858858afa96)#define ADP5585\_PWM\_OFFT\_LOW 0x2F

[ 62](adp5585_8h.md#ae4c576fc2d0efcf137c6530326ead1be)#define ADP5585\_PWM\_OFFT\_HIGH 0x30

[ 63](adp5585_8h.md#a74fa6f7378722a569c298394ca2c3b36)#define ADP5585\_PWM\_ONT\_LOW 0x31

[ 64](adp5585_8h.md#a7bf28da865492a8c496613338a55933e)#define ADP5585\_PWM\_ONT\_HIGH 0x32

[ 65](adp5585_8h.md#a1de2da958c6db64a34a2de1fa6ffddba)#define ADP5585\_PWM\_CFG 0x33

[ 66](adp5585_8h.md#a3cd8ec997df5e5425613e20e5fa240c6)#define ADP5585\_LOGIC\_CFG 0x34

[ 67](adp5585_8h.md#a6944520e4d0b1187b4dea91f6c1adc10)#define ADP5585\_LOGIC\_FF\_CFG 0x35

[ 68](adp5585_8h.md#a370f09e02a005f200784f830fec3591f)#define ADP5585\_LOGIC\_INT\_EVENT\_EN 0x36

[ 69](adp5585_8h.md#a5c3dba7ca9da0b4df5ad2afcf4bcae5e)#define ADP5585\_POLL\_PTIME\_CFG 0x37

[ 70](adp5585_8h.md#ab657ba2f5015a956c3dd5d928684c98c)#define ADP5585\_PIN\_CONFIG\_A 0x38

[ 71](adp5585_8h.md#a3b730343c76b05b7ea6ef5fe69f2e819)#define ADP5585\_PIN\_CONFIG\_B 0x39

[ 72](adp5585_8h.md#a9abe95d8b24f41002df9318710b7e834)#define ADP5585\_PIN\_CONFIG\_C 0x3A

[ 73](adp5585_8h.md#accaa4211d0b1dbd645652ed279d62557)#define ADP5585\_GENERAL\_CFG 0x3B

[ 74](adp5585_8h.md#a6b4c4ba659f9414747b0ae06bc0cdcfd)#define ADP5585\_INT\_EN 0x3C

75

76/\* ID Register \*/

[ 77](adp5585_8h.md#a5b090f56fa476d7cca2f6899135229f8)#define ADP5585\_DEVICE\_ID\_MASK 0xF

[ 78](adp5585_8h.md#a3668ae7400564896daa2c609f8c4a594)#define ADP5585\_MAN\_ID\_MASK 0xF

[ 79](adp5585_8h.md#ac3364a58902030fbec498761fc442ffe)#define ADP5585\_MAN\_ID\_SHIFT 4

[ 80](adp5585_8h.md#a372daeaedd3583aea797089b37fbe5c0)#define ADP5585\_MAN\_ID 0x02

81

[ 82](adp5585_8h.md#a7371eba2de343b1c26e0c1ea8119eb32)#define ADP5585\_PWM\_CFG\_EN 0x1

[ 83](adp5585_8h.md#a0e4cbfb9cb957805c16e94d19e0420fd)#define ADP5585\_PWM\_CFG\_MODE 0x2

[ 84](adp5585_8h.md#aa04ec62322c733d66ee37303d29d03f4)#define ADP5585\_PIN\_CONFIG\_R3\_PWM 0x8

[ 85](adp5585_8h.md#a33ad97c1ffb9cc9a820f0609dfc76087)#define ADP5585\_PIN\_CONFIG\_R3\_MASK 0xC

[ 86](adp5585_8h.md#ab681a5188091e9a2443a622021bb560c)#define ADP5585\_GENERAL\_CFG\_OSC\_EN 0x80

87

88/\* INT\_EN and INT\_STATUS Register \*/

[ 89](adp5585_8h.md#a4ba78a1afbbb7df3c945e07c45685717)#define ADP5585\_INT\_EVENT (1U << 0)

[ 90](adp5585_8h.md#a4aad6f3752b5b76f2f6f4ec5c03c0dcb)#define ADP5585\_INT\_GPI (1U << 1)

[ 91](adp5585_8h.md#ad362d9d20ead42061bf577a75ae92107)#define ADP5585\_INT\_OVERFLOW (1U << 2)

[ 92](adp5585_8h.md#ab38755ce29cc619bb163a327eafc48e9)#define ADP5585\_INT\_LOGIC (1U << 4)

93

[ 94](adp5585_8h.md#a7d65da027f146e0ec4c574becb014e43)#define ADP5585\_REG\_MASK 0xFF

95

[ 96](structmfd__adp5585__config.md)struct [mfd\_adp5585\_config](structmfd__adp5585__config.md) {

[ 97](structmfd__adp5585__config.md#af0c8d2113efb5fad7193c5969294660b) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [reset\_gpio](structmfd__adp5585__config.md#af0c8d2113efb5fad7193c5969294660b);

[ 98](structmfd__adp5585__config.md#a29c59990dea7c1e219f1f42baa699feb) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [nint\_gpio](structmfd__adp5585__config.md#a29c59990dea7c1e219f1f42baa699feb);

[ 99](structmfd__adp5585__config.md#ab27f8be0f4f2d29b0fe7e400cd475cd4) struct [i2c\_dt\_spec](structi2c__dt__spec.md) [i2c\_bus](structmfd__adp5585__config.md#ab27f8be0f4f2d29b0fe7e400cd475cd4);

100};

101

[ 102](structmfd__adp5585__data.md)struct [mfd\_adp5585\_data](structmfd__adp5585__data.md) {

[ 103](structmfd__adp5585__data.md#aad6ae38b0cfe0b216f9a965718ae92bf) struct [k\_work](structk__work.md) [work](structmfd__adp5585__data.md#aad6ae38b0cfe0b216f9a965718ae92bf);

[ 104](structmfd__adp5585__data.md#a87322b6acebc0c77b4d98ab8ee6b57e6) struct k\_sem [lock](structmfd__adp5585__data.md#a87322b6acebc0c77b4d98ab8ee6b57e6);

[ 105](structmfd__adp5585__data.md#aa517e16739c65b8468df3ef26c3b7c06) const struct [device](structdevice.md) \*[dev](structmfd__adp5585__data.md#aa517e16739c65b8468df3ef26c3b7c06);

106 struct {

107#ifdef CONFIG\_GPIO\_ADP5585

108 const struct [device](structdevice.md) \*gpio\_dev;

109#endif /\* CONFIG\_GPIO\_ADP5585 \*/

[ 110](structmfd__adp5585__data.md#ac890b9075851d9b9b3a102043ba522ac) } [child](structmfd__adp5585__data.md#ac890b9075851d9b9b3a102043ba522ac);

[ 111](structmfd__adp5585__data.md#a22322bec62253aedbe8be191bf735e72) struct [gpio\_callback](structgpio__callback.md) [int\_gpio\_cb](structmfd__adp5585__data.md#a22322bec62253aedbe8be191bf735e72);

112};

113

118#ifdef CONFIG\_GPIO\_ADP5585

119void gpio\_adp5585\_irq\_handler(const struct [device](structdevice.md) \*dev);

120#endif /\* CONFIG\_GPIO\_ADP5585 \*/

121

122#ifdef \_\_cplusplus

123}

124#endif

125

126#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD5952\_H\_ \*/

[device.h](device_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:740

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3880

[mfd\_adp5585\_config](structmfd__adp5585__config.md)

**Definition** adp5585.h:96

[mfd\_adp5585\_config::nint\_gpio](structmfd__adp5585__config.md#a29c59990dea7c1e219f1f42baa699feb)

struct gpio\_dt\_spec nint\_gpio

**Definition** adp5585.h:98

[mfd\_adp5585\_config::i2c\_bus](structmfd__adp5585__config.md#ab27f8be0f4f2d29b0fe7e400cd475cd4)

struct i2c\_dt\_spec i2c\_bus

**Definition** adp5585.h:99

[mfd\_adp5585\_config::reset\_gpio](structmfd__adp5585__config.md#af0c8d2113efb5fad7193c5969294660b)

struct gpio\_dt\_spec reset\_gpio

**Definition** adp5585.h:97

[mfd\_adp5585\_data](structmfd__adp5585__data.md)

**Definition** adp5585.h:102

[mfd\_adp5585\_data::int\_gpio\_cb](structmfd__adp5585__data.md#a22322bec62253aedbe8be191bf735e72)

struct gpio\_callback int\_gpio\_cb

**Definition** adp5585.h:111

[mfd\_adp5585\_data::lock](structmfd__adp5585__data.md#a87322b6acebc0c77b4d98ab8ee6b57e6)

struct k\_sem lock

**Definition** adp5585.h:104

[mfd\_adp5585\_data::dev](structmfd__adp5585__data.md#aa517e16739c65b8468df3ef26c3b7c06)

const struct device \* dev

**Definition** adp5585.h:105

[mfd\_adp5585\_data::work](structmfd__adp5585__data.md#aad6ae38b0cfe0b216f9a965718ae92bf)

struct k\_work work

**Definition** adp5585.h:103

[mfd\_adp5585\_data::child](structmfd__adp5585__data.md#ac890b9075851d9b9b3a102043ba522ac)

struct mfd\_adp5585\_data::@377271251103256101275222207120274253377320164372 child

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [adp5585.h](adp5585_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
