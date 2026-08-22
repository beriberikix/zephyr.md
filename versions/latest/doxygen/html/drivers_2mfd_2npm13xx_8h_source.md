---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2mfd_2npm13xx_8h_source.html
original_path: doxygen/html/drivers_2mfd_2npm13xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm13xx.h

[Go to the documentation of this file.](drivers_2mfd_2npm13xx_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM13XX\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM13XX\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

18

19#include <stddef.h>

20#include <[stdint.h](stdint_8h.md)>

21

22#include <[zephyr/device.h](device_8h.md)>

23#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

24

[ 25](group__mfd__interface__npm13xx.md#ga4ac9f47283f10ea1d847cbd0038aad7a)enum [mfd\_npm13xx\_event\_t](group__mfd__interface__npm13xx.md#ga4ac9f47283f10ea1d847cbd0038aad7a) {

[ 26](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858) [NPM13XX\_EVENT\_CHG\_COMPLETED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858),

[ 27](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6) [NPM13XX\_EVENT\_CHG\_ERROR](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6),

[ 28](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c) [NPM13XX\_EVENT\_BATTERY\_DETECTED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c),

[ 29](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d) [NPM13XX\_EVENT\_BATTERY\_REMOVED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d),

[ 30](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646) [NPM13XX\_EVENT\_SHIPHOLD\_PRESS](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646),

[ 31](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5) [NPM13XX\_EVENT\_SHIPHOLD\_RELEASE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5),

[ 32](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7) [NPM13XX\_EVENT\_WATCHDOG\_WARN](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7),

[ 33](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b) [NPM13XX\_EVENT\_VBUS\_DETECTED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b),

[ 34](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e) [NPM13XX\_EVENT\_VBUS\_REMOVED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e),

[ 35](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8) [NPM13XX\_EVENT\_GPIO0\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8),

[ 36](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c) [NPM13XX\_EVENT\_GPIO1\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c),

[ 37](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25) [NPM13XX\_EVENT\_GPIO2\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25),

[ 38](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b) [NPM13XX\_EVENT\_GPIO3\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b),

[ 39](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35) [NPM13XX\_EVENT\_GPIO4\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35),

[ 40](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa) [NPM13XX\_EVENT\_MAX](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)

41};

42

[ 54](group__mfd__interface__npm13xx.md#gabba0559ce29b71e1ce7065bf5d36f8d8)int [mfd\_npm13xx\_reg\_read\_burst](group__mfd__interface__npm13xx.md#gabba0559ce29b71e1ce7065bf5d36f8d8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, void \*data,

55 size\_t len);

56

[ 67](group__mfd__interface__npm13xx.md#ga154c4c48888ff1587d157b16e38d2584)int [mfd\_npm13xx\_reg\_read](group__mfd__interface__npm13xx.md#ga154c4c48888ff1587d157b16e38d2584)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

68

[ 79](group__mfd__interface__npm13xx.md#gac1c7815a4bcfb2262fd4f02d28f2f781)int [mfd\_npm13xx\_reg\_write](group__mfd__interface__npm13xx.md#gac1c7815a4bcfb2262fd4f02d28f2f781)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data);

80

[ 92](group__mfd__interface__npm13xx.md#gaeb317a7b4aa2ad37e69c2fda77dbbd0e)int [mfd\_npm13xx\_reg\_write2](group__mfd__interface__npm13xx.md#gaeb317a7b4aa2ad37e69c2fda77dbbd0e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data1,

93 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data2);

94

[ 106](group__mfd__interface__npm13xx.md#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)int [mfd\_npm13xx\_reg\_update](group__mfd__interface__npm13xx.md#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data,

107 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

108

[ 118](group__mfd__interface__npm13xx.md#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)int [mfd\_npm13xx\_set\_timer](group__mfd__interface__npm13xx.md#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms);

119

[ 127](group__mfd__interface__npm13xx.md#ga43c5a5225a0cc2738506d5556ecb06ba)int [mfd\_npm13xx\_reset](group__mfd__interface__npm13xx.md#ga43c5a5225a0cc2738506d5556ecb06ba)(const struct [device](structdevice.md) \*dev);

128

[ 140](group__mfd__interface__npm13xx.md#gaf23758d56ac58f814bc2f093ebfa1282)int [mfd\_npm13xx\_hibernate](group__mfd__interface__npm13xx.md#gaf23758d56ac58f814bc2f093ebfa1282)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms);

141

[ 149](group__mfd__interface__npm13xx.md#ga3cac4a85cee20242d3a988d9830ea547)int [mfd\_npm13xx\_add\_callback](group__mfd__interface__npm13xx.md#ga3cac4a85cee20242d3a988d9830ea547)(const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback);

150

[ 158](group__mfd__interface__npm13xx.md#ga35fbc854545b9113f6ec36677491b151)int [mfd\_npm13xx\_remove\_callback](group__mfd__interface__npm13xx.md#ga35fbc854545b9113f6ec36677491b151)(const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback);

159

161

162#ifdef \_\_cplusplus

163}

164#endif

165

166#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM13XX\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[mfd\_npm13xx\_reg\_read](group__mfd__interface__npm13xx.md#ga154c4c48888ff1587d157b16e38d2584)

int mfd\_npm13xx\_reg\_read(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t \*data)

Read single register from npm13xx.

[mfd\_npm13xx\_reg\_update](group__mfd__interface__npm13xx.md#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)

int mfd\_npm13xx\_reg\_update(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t data, uint8\_t mask)

Update selected bits in npm13xx register.

[mfd\_npm13xx\_remove\_callback](group__mfd__interface__npm13xx.md#ga35fbc854545b9113f6ec36677491b151)

int mfd\_npm13xx\_remove\_callback(const struct device \*dev, struct gpio\_callback \*callback)

Remove npm13xx event callback.

[mfd\_npm13xx\_add\_callback](group__mfd__interface__npm13xx.md#ga3cac4a85cee20242d3a988d9830ea547)

int mfd\_npm13xx\_add\_callback(const struct device \*dev, struct gpio\_callback \*callback)

Add npm13xx event callback.

[mfd\_npm13xx\_set\_timer](group__mfd__interface__npm13xx.md#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)

int mfd\_npm13xx\_set\_timer(const struct device \*dev, uint32\_t time\_ms)

Write npm13xx timer register.

[mfd\_npm13xx\_reset](group__mfd__interface__npm13xx.md#ga43c5a5225a0cc2738506d5556ecb06ba)

int mfd\_npm13xx\_reset(const struct device \*dev)

npm13xx full power reset

[mfd\_npm13xx\_event\_t](group__mfd__interface__npm13xx.md#ga4ac9f47283f10ea1d847cbd0038aad7a)

mfd\_npm13xx\_event\_t

**Definition** npm13xx.h:25

[mfd\_npm13xx\_reg\_read\_burst](group__mfd__interface__npm13xx.md#gabba0559ce29b71e1ce7065bf5d36f8d8)

int mfd\_npm13xx\_reg\_read\_burst(const struct device \*dev, uint8\_t base, uint8\_t offset, void \*data, size\_t len)

Read multiple registers from npm13xx.

[mfd\_npm13xx\_reg\_write](group__mfd__interface__npm13xx.md#gac1c7815a4bcfb2262fd4f02d28f2f781)

int mfd\_npm13xx\_reg\_write(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t data)

Write single register to npm13xx.

[mfd\_npm13xx\_reg\_write2](group__mfd__interface__npm13xx.md#gaeb317a7b4aa2ad37e69c2fda77dbbd0e)

int mfd\_npm13xx\_reg\_write2(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t data1, uint8\_t data2)

Write two registers to npm13xx.

[mfd\_npm13xx\_hibernate](group__mfd__interface__npm13xx.md#gaf23758d56ac58f814bc2f093ebfa1282)

int mfd\_npm13xx\_hibernate(const struct device \*dev, uint32\_t time\_ms)

npm13xx hibernate

[NPM13XX\_EVENT\_WATCHDOG\_WARN](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7)

@ NPM13XX\_EVENT\_WATCHDOG\_WARN

**Definition** npm13xx.h:32

[NPM13XX\_EVENT\_GPIO0\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8)

@ NPM13XX\_EVENT\_GPIO0\_EDGE

**Definition** npm13xx.h:35

[NPM13XX\_EVENT\_BATTERY\_REMOVED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d)

@ NPM13XX\_EVENT\_BATTERY\_REMOVED

**Definition** npm13xx.h:29

[NPM13XX\_EVENT\_SHIPHOLD\_RELEASE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5)

@ NPM13XX\_EVENT\_SHIPHOLD\_RELEASE

**Definition** npm13xx.h:31

[NPM13XX\_EVENT\_GPIO2\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25)

@ NPM13XX\_EVENT\_GPIO2\_EDGE

**Definition** npm13xx.h:37

[NPM13XX\_EVENT\_GPIO3\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b)

@ NPM13XX\_EVENT\_GPIO3\_EDGE

**Definition** npm13xx.h:38

[NPM13XX\_EVENT\_GPIO4\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35)

@ NPM13XX\_EVENT\_GPIO4\_EDGE

**Definition** npm13xx.h:39

[NPM13XX\_EVENT\_CHG\_COMPLETED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858)

@ NPM13XX\_EVENT\_CHG\_COMPLETED

**Definition** npm13xx.h:26

[NPM13XX\_EVENT\_MAX](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)

@ NPM13XX\_EVENT\_MAX

**Definition** npm13xx.h:40

[NPM13XX\_EVENT\_CHG\_ERROR](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6)

@ NPM13XX\_EVENT\_CHG\_ERROR

**Definition** npm13xx.h:27

[NPM13XX\_EVENT\_BATTERY\_DETECTED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c)

@ NPM13XX\_EVENT\_BATTERY\_DETECTED

**Definition** npm13xx.h:28

[NPM13XX\_EVENT\_SHIPHOLD\_PRESS](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646)

@ NPM13XX\_EVENT\_SHIPHOLD\_PRESS

**Definition** npm13xx.h:30

[NPM13XX\_EVENT\_VBUS\_REMOVED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e)

@ NPM13XX\_EVENT\_VBUS\_REMOVED

**Definition** npm13xx.h:34

[NPM13XX\_EVENT\_GPIO1\_EDGE](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c)

@ NPM13XX\_EVENT\_GPIO1\_EDGE

**Definition** npm13xx.h:36

[NPM13XX\_EVENT\_VBUS\_DETECTED](group__mfd__interface__npm13xx.md#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b)

@ NPM13XX\_EVENT\_VBUS\_DETECTED

**Definition** npm13xx.h:33

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [npm13xx.h](drivers_2mfd_2npm13xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
