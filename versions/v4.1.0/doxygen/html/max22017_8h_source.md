---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/max22017_8h_source.html
original_path: doxygen/html/max22017_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max22017.h

[Go to the documentation of this file.](max22017_8h.md)

1/\*

2 \* Copyright (c) 2024 Analog Devices Inc.

3 \* Copyright (c) 2024 Baylibre SAS

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_MAX22017\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_MAX22017\_H\_

10

11#include <[zephyr/device.h](device_8h.md)>

12

[ 13](max22017_8h.md#a69b46acb4bf6ed483c1f453a77d7c257)#define MAX22017\_LDAC\_TOGGLE\_TIME 200

[ 14](max22017_8h.md#a6420606c34753e82d867742e2f6ff846)#define MAX22017\_MAX\_CHANNEL 2

[ 15](max22017_8h.md#a4fb90ff0a6659973ec6f47800b04357a)#define MAX22017\_CRC\_POLY 0x8c /\* reversed 0x31 poly for crc8-maxim \*/

16

[ 17](max22017_8h.md#a29a9caa9d9f52d9d58ede62a7b09ff84)#define MAX22017\_GEN\_ID\_OFF 0x00

[ 18](max22017_8h.md#a395ddcfd27a1926a3787181f87242526)#define MAX22017\_GEN\_ID\_PROD\_ID GENMASK(15, 8)

[ 19](max22017_8h.md#a6eb309fd6558e06a84127335e769d2d9)#define MAX22017\_GEN\_ID\_REV\_ID GENMASK(7, 0)

20

[ 21](max22017_8h.md#a799bc9d76c76b5cfd4e0c4782e61c68d)#define MAX22017\_GEN\_SERIAL\_MSB\_OFF 0x01

[ 22](max22017_8h.md#a71543d48878b7290f2e81ecf1689d9c5)#define MAX22017\_GEN\_SERIAL\_MSB\_SERIAL\_MSB GENMASK(15, 0)

23

[ 24](max22017_8h.md#a269a0c9109afed5e63f29c9364d3931a)#define MAX22017\_GEN\_SERIAL\_LSB\_OFF 0x02

[ 25](max22017_8h.md#adbfda2921aaaf988e18efe7577ae8ed8)#define MAX22017\_GEN\_SERIAL\_LSB\_SERIAL\_LSB GENMASK(15, 0)

26

[ 27](max22017_8h.md#a8a77450cfed9423297323d451521e55d)#define MAX22017\_GEN\_CNFG\_OFF 0x03

[ 28](max22017_8h.md#a77447c3bae3e076fe6c19eb761e54d0a)#define MAX22017\_GEN\_CNFG\_OPENWIRE\_DTCT\_CNFG GENMASK(15, 14)

[ 29](max22017_8h.md#aa3c6c039ffd5caeb411e8f057351a47b)#define MAX22017\_GEN\_CNFG\_TMOUT\_SEL GENMASK(13, 10)

[ 30](max22017_8h.md#a888207719162d5eb973e65f8f16bcee9)#define MAX22017\_GEN\_CNFG\_TMOUT\_CNFG BIT(9)

[ 31](max22017_8h.md#a3d90df4835aa9814d64ed157ba55dc89)#define MAX22017\_GEN\_CNFG\_TMOUT\_EN BIT(8)

[ 32](max22017_8h.md#a53ff3e5d22a4121c5a8e0d468f62adfe)#define MAX22017\_GEN\_CNFG\_THSHDN\_CNFG GENMASK(7, 6)

[ 33](max22017_8h.md#ab8ee545a7f918e680496c733bc094d1b)#define MAX22017\_GEN\_CNFG\_OVC\_SHDN\_CNFG GENMASK(5, 4)

[ 34](max22017_8h.md#aad7bdcad31409154f76037090a602f2d)#define MAX22017\_GEN\_CNFG\_OVC\_CNFG GENMASK(3, 2)

[ 35](max22017_8h.md#ad677c0bfb0565436848ce8fa3ab497b1)#define MAX22017\_GEN\_CNFG\_CRC\_EN BIT(1)

[ 36](max22017_8h.md#a2ef6bf6ae5c000d84f5910f6ba5c55ba)#define MAX22017\_GEN\_CNFG\_DACREF\_SEL BIT(0)

37

[ 38](max22017_8h.md#a9197693c7b15a5337a19659efc2e250c)#define MAX22017\_GEN\_GPIO\_CTRL\_OFF 0x04

[ 39](max22017_8h.md#abe8bd23109b597ea8349316c0d1d8427)#define MAX22017\_GEN\_GPIO\_CTRL\_GPIO\_EN GENMASK(13, 8)

[ 40](max22017_8h.md#a52d221379e6bcdba5ed8d2f287b64f84)#define MAX22017\_GEN\_GPIO\_CTRL\_GPIO\_DIR GENMASK(5, 0)

41

[ 42](max22017_8h.md#adac6b2dde0ca575d402e781f4ecf5420)#define MAX22017\_GEN\_GPIO\_DATA\_OFF 0x05

[ 43](max22017_8h.md#a0c2800b8921081669472db86ce0c92d3)#define MAX22017\_GEN\_GPIO\_DATA\_GPO\_DATA GENMASK(13, 8)

[ 44](max22017_8h.md#a43846e179219f0738c1ad1a4b464ab32)#define MAX22017\_GEN\_GPIO\_DATA\_GPI\_DATA GENMASK(5, 0)

45

[ 46](max22017_8h.md#ab46c131ba1e50d5f86c3e27b807b7a7b)#define MAX22017\_GEN\_GPI\_INT\_OFF 0x06

[ 47](max22017_8h.md#acb8737f0e19a94dc66024cda4536208f)#define MAX22017\_GEN\_GPI\_INT\_GPI\_POS\_EDGE\_INT GENMASK(13, 8)

[ 48](max22017_8h.md#abc8ca54142d80a1d14a63092e553b582)#define MAX22017\_GEN\_GPI\_INT\_GPI\_NEG\_EDGE\_INT GENMASK(5, 0)

49

[ 50](max22017_8h.md#a24277b36f8fe9b994fa8de1c63c06fed)#define MAX22017\_GEN\_GPI\_INT\_STA\_OFF 0x07

[ 51](max22017_8h.md#ab3f2d018f43cda0121afed3f920d631f)#define MAX22017\_GEN\_GPI\_INT\_STA\_GPI\_POS\_EDGE\_INT\_STA GENMASK(13, 8)

[ 52](max22017_8h.md#a2428e64221646898a7fc8dc68e350f5e)#define MAX22017\_GEN\_GPI\_INT\_STA\_GPI\_NEG\_EDGE\_INT\_STA GENMASK(5, 0)

53

[ 54](max22017_8h.md#aad01e617a20eed924aa47003d7a73ef4)#define MAX22017\_GEN\_INT\_OFF 0x08

[ 55](max22017_8h.md#a950db8f0491cb67a25eb2eb5ad740a70)#define MAX22017\_GEN\_INT\_FAIL\_INT BIT(15)

[ 56](max22017_8h.md#a27eac9949479c8d1f42f68da05d39383)#define MAX22017\_GEN\_INT\_CONV\_OVF\_INT GENMASK(13, 12)

[ 57](max22017_8h.md#ae956e4148f8da78321a8b444495da665)#define MAX22017\_GEN\_INT\_OPENWIRE\_DTCT\_INT GENMASK(11, 10)

[ 58](max22017_8h.md#ac9bf908c94cb4d7949f74d288b8cafeb)#define MAX22017\_GEN\_INT\_HVDD\_INT BIT(9)

[ 59](max22017_8h.md#ab0dae9b77818a8fee73d5b997cdc9a3c)#define MAX22017\_GEN\_INT\_TMOUT\_INT BIT(8)

[ 60](max22017_8h.md#a7833344d8d071ba5d591391294e3392f)#define MAX22017\_GEN\_INT\_THSHDN\_INT GENMASK(7, 6)

[ 61](max22017_8h.md#a22d2450dd425193fb6a68e4b337fb05d)#define MAX22017\_GEN\_INT\_THWRNG\_INT GENMASK(5, 4)

[ 62](max22017_8h.md#a950ee60a66d4770719dc285ec8233ba8)#define MAX22017\_GEN\_INT\_OVC\_INT GENMASK(3, 2)

[ 63](max22017_8h.md#ac5582d36610f0eb5b0795d6c20c6dfce)#define MAX22017\_GEN\_INT\_CRC\_INT BIT(1)

[ 64](max22017_8h.md#ad9a98581421dd420920ca8b499131594)#define MAX22017\_GEN\_INT\_GPI\_INT BIT(0)

65

[ 66](max22017_8h.md#afaa5cf0a23d3b86bdb0aa8f64794a349)#define MAX22017\_GEN\_INTEN\_OFF 0x09

[ 67](max22017_8h.md#a569d0198591bd1ac8cf3017985797161)#define MAX22017\_GEN\_INTEN\_CONV\_OVF\_INTEN GENMASK(13, 12)

[ 68](max22017_8h.md#ab0d04e5d3b9a275e2f6d358d55f9ecec)#define MAX22017\_GEN\_INTEN\_OPENWIRE\_DTCT\_INTEN GENMASK(11, 10)

[ 69](max22017_8h.md#a27665ac4ca4283876c7b0d82c68a0955)#define MAX22017\_GEN\_INTEN\_HVDD\_INTEN BIT(9)

[ 70](max22017_8h.md#a3759acb5df5704f36d97c159561efd10)#define MAX22017\_GEN\_INTEN\_TMOUT\_INTEN BIT(8)

[ 71](max22017_8h.md#a53365f203a2a2d4687807a7e709edfe7)#define MAX22017\_GEN\_INTEN\_THSHDN\_INTEN GENMASK(7, 6)

[ 72](max22017_8h.md#a9e9534a6244dc77b41b464be99997306)#define MAX22017\_GEN\_INTEN\_THWRNG\_INTEN GENMASK(5, 4)

[ 73](max22017_8h.md#a9ec0c3a38830359ca2eebecc37275fe5)#define MAX22017\_GEN\_INTEN\_OVC\_INTEN GENMASK(3, 2)

[ 74](max22017_8h.md#aabcebfeedc9571ed8d951bf876fe4231)#define MAX22017\_GEN\_INTEN\_CRC\_INTEN BIT(1)

[ 75](max22017_8h.md#a0ae1361d7e475c8a4eb2850d132a4498)#define MAX22017\_GEN\_INTEN\_GPI\_INTEN BIT(0)

76

[ 77](max22017_8h.md#a291a4ec441b4374377950c4c7f4badbf)#define MAX22017\_GEN\_RST\_CTRL\_OFF 0x0A

[ 78](max22017_8h.md#a1693f93cd62731fe95c7ce1e1007d800)#define MAX22017\_GEN\_RST\_CTRL\_AO\_COEFF\_RELOAD GENMASK(15, 14)

[ 79](max22017_8h.md#ad544ab22f6ebf4a5a0d794a92145e2b5)#define MAX22017\_GEN\_RST\_CTRL\_GEN\_RST BIT(9)

80

[ 81](max22017_8h.md#a3bcd3cbd0b9e3fb93e24388a0b384ae9)#define MAX22017\_AO\_CMD\_OFF 0x40

[ 82](max22017_8h.md#a4e77f6704c235280628933321f691712)#define MAX22017\_AO\_CMD\_AO\_LD\_CTRL GENMASK(15, 14)

83

[ 84](max22017_8h.md#a9ed535b03f0aede89e5309005cec296c)#define MAX22017\_AO\_STA\_OFF 0x41

[ 85](max22017_8h.md#a3b4266da3e1fd880341e3bf3c4789ad1)#define MAX22017\_AO\_STA\_BUSY\_STA GENMASK(15, 14)

[ 86](max22017_8h.md#ab483e9896b6884a238d560d5e2f988cc)#define MAX22017\_AO\_STA\_SLEW\_STA GENMASK(13, 12)

[ 87](max22017_8h.md#afef14d877f9cb5771f70ed20ef2b6619)#define MAX22017\_AO\_STA\_FAIL\_STA BIT(0)

88

[ 89](max22017_8h.md#a2bd588d5437464244088f003b9c2665f)#define MAX22017\_AO\_CNFG\_OFF 0x42

[ 90](max22017_8h.md#af1add45a9664316f60a653369562fa9c)#define MAX22017\_AO\_CNFG\_AO\_LD\_CNFG GENMASK(15, 14)

[ 91](max22017_8h.md#a018306445ab0bd9305f7e9ca311936bc)#define MAX22017\_AO\_CNFG\_AO\_CM\_SENSE GENMASK(13, 12)

[ 92](max22017_8h.md#a39a986f264a8f861f91b8e139e8085de)#define MAX22017\_AO\_CNFG\_AO\_UNI GENMASK(11, 10)

[ 93](max22017_8h.md#a5293ea7da75751e93c0130c306727bda)#define MAX22017\_AO\_CNFG\_AO\_MODE GENMASK(9, 8)

[ 94](max22017_8h.md#aadf01e360a09401fdcaef4fc4ec39265)#define MAX22017\_AO\_CNFG\_AO\_OPENWIRE\_DTCT\_LMT GENMASK(5, 4)

[ 95](max22017_8h.md#a5d44e9a362380c61176052e98afadaf5)#define MAX22017\_AO\_CNFG\_AI\_EN GENMASK(3, 2)

[ 96](max22017_8h.md#ab2dfe72b9fa038e192c7daae2ffb3bd5)#define MAX22017\_AO\_CNFG\_AO\_EN GENMASK(1, 0)

97

[ 98](max22017_8h.md#a30e655032be25236b337941649ab4587)#define MAX22017\_AO\_SLEW\_RATE\_CHn\_OFF(n) (0x43 + n)

[ 99](max22017_8h.md#aead931e808873a41e7749083abdb5bc9)#define MAX22017\_AO\_SLEW\_RATE\_CHn\_AO\_SR\_EN\_CHn BIT(5)

[ 100](max22017_8h.md#a5e59cb1143c01be37e3cbf7cb8db35eb)#define MAX22017\_AO\_SLEW\_RATE\_CHn\_AO\_SR\_SEL\_CHn BIT(4)

[ 101](max22017_8h.md#a882b209cbcb535cb10102a2f21501482)#define MAX22017\_AO\_SLEW\_RATE\_CHn\_AO\_SR\_STEP\_SIZE\_CHn GENMASK(3, 2)

[ 102](max22017_8h.md#a59f3f06a4a2405bbc96df4b487b35cd4)#define MAX22017\_AO\_SLEW\_RATE\_CHn\_AO\_SR\_UPDATE\_RATE\_CHn GENMASK(1, 0)

103

[ 104](max22017_8h.md#a7bcc6214915085619e5f549557d78ea4)#define MAX22017\_AO\_DATA\_CHn\_OFF(n) (0x45 + n)

[ 105](max22017_8h.md#a37a9fc76107c849f89d1db6914db1ab9)#define MAX22017\_AO\_DATA\_CHn\_AO\_DATA\_CH GENMASK(15, 0)

106

[ 107](max22017_8h.md#ab31ff3c83a67336f3c62e8ca08f3dd25)#define MAX22017\_AO\_OFFSET\_CORR\_CHn\_OFF(n) (0x47 + (2 \* n))

[ 108](max22017_8h.md#a4ed090f64827549887dec94b9c159f3b)#define MAX22017\_AO\_OFFSET\_CORR\_CHn\_AO\_OFFSET\_CH GENMASK(15, 0)

109

[ 110](max22017_8h.md#a5e40e0dffc60182fe012069d31d6b881)#define MAX22017\_AO\_GAIN\_CORR\_CHn\_OFF(n) (0x48 + (2 \* n))

[ 111](max22017_8h.md#afb46c37c05d65b550178a22c7fa388aa)#define MAX22017\_AO\_GAIN\_CORR\_CHn\_AO\_GAIN\_CH GENMASK(15, 0)

112

[ 113](max22017_8h.md#aa1b178c2a60337d8b9dcfb4ac8315d14)#define MAX22017\_SPI\_TRANS\_ADDR GENMASK(7, 1)

[ 114](max22017_8h.md#a0189fe593af9379781b6f63998b2d268)#define MAX22017\_SPI\_TRANS\_DIR BIT(0)

[ 115](max22017_8h.md#aa16b8b5dc1817df754d5228f4c335fc9)#define MAX22017\_SPI\_TRANS\_PAYLOAD GENMASK(15, 0)

116

122

[ 132](group__mdf__interface__max22017.md#ga7c051fa0697ae672a4dddbfa84059ad0)int [max22017\_reg\_read](group__mdf__interface__max22017.md#ga7c051fa0697ae672a4dddbfa84059ad0)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value);

133

[ 143](group__mdf__interface__max22017.md#gac4a4a29f7ae31af97f19d700264a604d)int [max22017\_reg\_write](group__mdf__interface__max22017.md#gac4a4a29f7ae31af97f19d700264a604d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

144

148

[ 149](structmax22017__data.md)struct [max22017\_data](structmax22017__data.md) {

[ 150](structmax22017__data.md#a0f281976d848ce06e43e39d7c8e555f6) const struct [device](structdevice.md) \*[dev](structmax22017__data.md#a0f281976d848ce06e43e39d7c8e555f6);

[ 151](structmax22017__data.md#a996ed1088ac25904049fd500ff20c8d5) struct [k\_mutex](structk__mutex.md) [lock](structmax22017__data.md#a996ed1088ac25904049fd500ff20c8d5);

[ 152](structmax22017__data.md#a3e58c68a77e41a0009ed3b8f314e8a1d) struct [k\_work](structk__work.md) [int\_work](structmax22017__data.md#a3e58c68a77e41a0009ed3b8f314e8a1d);

[ 153](structmax22017__data.md#a3404c90326b35195ccce3d502205b0ae) struct [gpio\_callback](structgpio__callback.md) [callback\_int](structmax22017__data.md#a3404c90326b35195ccce3d502205b0ae);

[ 154](structmax22017__data.md#afb03a179a5d64e90003f1fb8f4f6100a) bool [crc\_enabled](structmax22017__data.md#afb03a179a5d64e90003f1fb8f4f6100a);

155#ifdef CONFIG\_GPIO\_MAX22017

156 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) callbacks\_gpi;

157#endif

158};

159

160#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_MAX22017\_H\_ \*/

[device.h](device_8h.md)

[max22017\_reg\_read](group__mdf__interface__max22017.md#ga7c051fa0697ae672a4dddbfa84059ad0)

int max22017\_reg\_read(const struct device \*dev, uint8\_t addr, uint16\_t \*value)

Read register from max22017.

[max22017\_reg\_write](group__mdf__interface__max22017.md#gac4a4a29f7ae31af97f19d700264a604d)

int max22017\_reg\_write(const struct device \*dev, uint8\_t addr, uint16\_t value)

Write register to max22017.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4006

[max22017\_data](structmax22017__data.md)

**Definition** max22017.h:149

[max22017\_data::dev](structmax22017__data.md#a0f281976d848ce06e43e39d7c8e555f6)

const struct device \* dev

**Definition** max22017.h:150

[max22017\_data::callback\_int](structmax22017__data.md#a3404c90326b35195ccce3d502205b0ae)

struct gpio\_callback callback\_int

**Definition** max22017.h:153

[max22017\_data::int\_work](structmax22017__data.md#a3e58c68a77e41a0009ed3b8f314e8a1d)

struct k\_work int\_work

**Definition** max22017.h:152

[max22017\_data::lock](structmax22017__data.md#a996ed1088ac25904049fd500ff20c8d5)

struct k\_mutex lock

**Definition** max22017.h:151

[max22017\_data::crc\_enabled](structmax22017__data.md#afb03a179a5d64e90003f1fb8f4f6100a)

bool crc\_enabled

**Definition** max22017.h:154

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [max22017.h](max22017_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
