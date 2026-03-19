---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2mfd_2npm1300_8h_source.html
original_path: doxygen/html/drivers_2mfd_2npm1300_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm1300.h

[Go to the documentation of this file.](drivers_2mfd_2npm1300_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM1300\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM1300\_H\_

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

[ 25](group__mdf__interface__npm1300.md#gad15bf59ebf3c5572347e939c4c2e6989)enum [mfd\_npm1300\_event\_t](group__mdf__interface__npm1300.md#gad15bf59ebf3c5572347e939c4c2e6989) {

[ 26](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a04241a0410734d82aee28c515a0a92c0) [NPM1300\_EVENT\_CHG\_COMPLETED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a04241a0410734d82aee28c515a0a92c0),

[ 27](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a153a82c7f6bac3393267c4ca0f16b8e3) [NPM1300\_EVENT\_CHG\_ERROR](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a153a82c7f6bac3393267c4ca0f16b8e3),

[ 28](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a8524187e6aa6ef0683265b1340cc117f) [NPM1300\_EVENT\_BATTERY\_DETECTED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a8524187e6aa6ef0683265b1340cc117f),

[ 29](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a98ff199ec155bd8ce7e42ede4aa90c78) [NPM1300\_EVENT\_BATTERY\_REMOVED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a98ff199ec155bd8ce7e42ede4aa90c78),

[ 30](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a70c303c4863161a086ddfe07fe315cd0) [NPM1300\_EVENT\_SHIPHOLD\_PRESS](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a70c303c4863161a086ddfe07fe315cd0),

[ 31](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989abb790b641b8d0a8d87b2fb5aabbc5bae) [NPM1300\_EVENT\_SHIPHOLD\_RELEASE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989abb790b641b8d0a8d87b2fb5aabbc5bae),

[ 32](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a182e6c0806f1d21802a628ccdf92c018) [NPM1300\_EVENT\_WATCHDOG\_WARN](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a182e6c0806f1d21802a628ccdf92c018),

[ 33](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989aebe54d5f1704b81873ca2dce17e44a47) [NPM1300\_EVENT\_VBUS\_DETECTED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989aebe54d5f1704b81873ca2dce17e44a47),

[ 34](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a94a3133140147f38e358ac97ed45ccaf) [NPM1300\_EVENT\_VBUS\_REMOVED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a94a3133140147f38e358ac97ed45ccaf),

[ 35](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a16f39a059833d1bb848c1e675748b582) [NPM1300\_EVENT\_GPIO0\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a16f39a059833d1bb848c1e675748b582),

[ 36](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a82fe1a2bcc5d2a4638d71f2b18fa73c7) [NPM1300\_EVENT\_GPIO1\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a82fe1a2bcc5d2a4638d71f2b18fa73c7),

[ 37](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a87ca56a02af057ff1920c7b2537ccecc) [NPM1300\_EVENT\_GPIO2\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a87ca56a02af057ff1920c7b2537ccecc),

[ 38](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a89b2ea4f842c92b118b36003b6b8175a) [NPM1300\_EVENT\_GPIO3\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a89b2ea4f842c92b118b36003b6b8175a),

[ 39](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a0a9d44a031ee84024ab13cccf2441f0e) [NPM1300\_EVENT\_GPIO4\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a0a9d44a031ee84024ab13cccf2441f0e),

[ 40](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a28557da1ca76c99c0a646cb687ef6291) [NPM1300\_EVENT\_MAX](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a28557da1ca76c99c0a646cb687ef6291)

41};

42

[ 54](group__mdf__interface__npm1300.md#ga021909959af74df2d324c7a98ce30c96)int [mfd\_npm1300\_reg\_read\_burst](group__mdf__interface__npm1300.md#ga021909959af74df2d324c7a98ce30c96)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, void \*data,

55 size\_t len);

56

[ 67](group__mdf__interface__npm1300.md#gaf068cde6e9482ee498429f75ab30c851)int [mfd\_npm1300\_reg\_read](group__mdf__interface__npm1300.md#gaf068cde6e9482ee498429f75ab30c851)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

68

[ 79](group__mdf__interface__npm1300.md#ga36e6db4a42e0ef3db7e63fcaad98d8cf)int [mfd\_npm1300\_reg\_write](group__mdf__interface__npm1300.md#ga36e6db4a42e0ef3db7e63fcaad98d8cf)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data);

80

[ 92](group__mdf__interface__npm1300.md#ga9bc9a9ae79181004f1303c12e2158fc7)int [mfd\_npm1300\_reg\_write2](group__mdf__interface__npm1300.md#ga9bc9a9ae79181004f1303c12e2158fc7)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data1,

93 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data2);

94

[ 106](group__mdf__interface__npm1300.md#gade28611b9ee6caee19d62f4de6f428f9)int [mfd\_npm1300\_reg\_update](group__mdf__interface__npm1300.md#gade28611b9ee6caee19d62f4de6f428f9)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data,

107 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

108

[ 118](group__mdf__interface__npm1300.md#gae009c00f3935a655631aef7b00efbffb)int [mfd\_npm1300\_set\_timer](group__mdf__interface__npm1300.md#gae009c00f3935a655631aef7b00efbffb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms);

119

[ 127](group__mdf__interface__npm1300.md#ga470c32ccd5eb357bbf7578ceb57be686)int [mfd\_npm1300\_reset](group__mdf__interface__npm1300.md#ga470c32ccd5eb357bbf7578ceb57be686)(const struct [device](structdevice.md) \*dev);

128

[ 140](group__mdf__interface__npm1300.md#ga8ebf64d5161863d8cf70179e5d9bc8e6)int [mfd\_npm1300\_hibernate](group__mdf__interface__npm1300.md#ga8ebf64d5161863d8cf70179e5d9bc8e6)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms);

141

[ 149](group__mdf__interface__npm1300.md#ga2ea73b039df7ae7a26b67ffe96de8cf0)int [mfd\_npm1300\_add\_callback](group__mdf__interface__npm1300.md#ga2ea73b039df7ae7a26b67ffe96de8cf0)(const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback);

150

[ 158](group__mdf__interface__npm1300.md#ga917ef06548659c0e447081ac475b4624)int [mfd\_npm1300\_remove\_callback](group__mdf__interface__npm1300.md#ga917ef06548659c0e447081ac475b4624)(const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback);

159

161

162#ifdef \_\_cplusplus

163}

164#endif

165

166#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM1300\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[mfd\_npm1300\_reg\_read\_burst](group__mdf__interface__npm1300.md#ga021909959af74df2d324c7a98ce30c96)

int mfd\_npm1300\_reg\_read\_burst(const struct device \*dev, uint8\_t base, uint8\_t offset, void \*data, size\_t len)

Read multiple registers from npm1300.

[mfd\_npm1300\_add\_callback](group__mdf__interface__npm1300.md#ga2ea73b039df7ae7a26b67ffe96de8cf0)

int mfd\_npm1300\_add\_callback(const struct device \*dev, struct gpio\_callback \*callback)

Add npm1300 event callback.

[mfd\_npm1300\_reg\_write](group__mdf__interface__npm1300.md#ga36e6db4a42e0ef3db7e63fcaad98d8cf)

int mfd\_npm1300\_reg\_write(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t data)

Write single register to npm1300.

[mfd\_npm1300\_reset](group__mdf__interface__npm1300.md#ga470c32ccd5eb357bbf7578ceb57be686)

int mfd\_npm1300\_reset(const struct device \*dev)

npm1300 full power reset

[mfd\_npm1300\_hibernate](group__mdf__interface__npm1300.md#ga8ebf64d5161863d8cf70179e5d9bc8e6)

int mfd\_npm1300\_hibernate(const struct device \*dev, uint32\_t time\_ms)

npm1300 hibernate

[mfd\_npm1300\_remove\_callback](group__mdf__interface__npm1300.md#ga917ef06548659c0e447081ac475b4624)

int mfd\_npm1300\_remove\_callback(const struct device \*dev, struct gpio\_callback \*callback)

Remove npm1300 event callback.

[mfd\_npm1300\_reg\_write2](group__mdf__interface__npm1300.md#ga9bc9a9ae79181004f1303c12e2158fc7)

int mfd\_npm1300\_reg\_write2(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t data1, uint8\_t data2)

Write two registers to npm1300.

[mfd\_npm1300\_event\_t](group__mdf__interface__npm1300.md#gad15bf59ebf3c5572347e939c4c2e6989)

mfd\_npm1300\_event\_t

**Definition** npm1300.h:25

[mfd\_npm1300\_reg\_update](group__mdf__interface__npm1300.md#gade28611b9ee6caee19d62f4de6f428f9)

int mfd\_npm1300\_reg\_update(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t data, uint8\_t mask)

Update selected bits in npm1300 register.

[mfd\_npm1300\_set\_timer](group__mdf__interface__npm1300.md#gae009c00f3935a655631aef7b00efbffb)

int mfd\_npm1300\_set\_timer(const struct device \*dev, uint32\_t time\_ms)

Write npm1300 timer register.

[mfd\_npm1300\_reg\_read](group__mdf__interface__npm1300.md#gaf068cde6e9482ee498429f75ab30c851)

int mfd\_npm1300\_reg\_read(const struct device \*dev, uint8\_t base, uint8\_t offset, uint8\_t \*data)

Read single register from npm1300.

[NPM1300\_EVENT\_CHG\_COMPLETED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a04241a0410734d82aee28c515a0a92c0)

@ NPM1300\_EVENT\_CHG\_COMPLETED

**Definition** npm1300.h:26

[NPM1300\_EVENT\_GPIO4\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a0a9d44a031ee84024ab13cccf2441f0e)

@ NPM1300\_EVENT\_GPIO4\_EDGE

**Definition** npm1300.h:39

[NPM1300\_EVENT\_CHG\_ERROR](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a153a82c7f6bac3393267c4ca0f16b8e3)

@ NPM1300\_EVENT\_CHG\_ERROR

**Definition** npm1300.h:27

[NPM1300\_EVENT\_GPIO0\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a16f39a059833d1bb848c1e675748b582)

@ NPM1300\_EVENT\_GPIO0\_EDGE

**Definition** npm1300.h:35

[NPM1300\_EVENT\_WATCHDOG\_WARN](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a182e6c0806f1d21802a628ccdf92c018)

@ NPM1300\_EVENT\_WATCHDOG\_WARN

**Definition** npm1300.h:32

[NPM1300\_EVENT\_MAX](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a28557da1ca76c99c0a646cb687ef6291)

@ NPM1300\_EVENT\_MAX

**Definition** npm1300.h:40

[NPM1300\_EVENT\_SHIPHOLD\_PRESS](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a70c303c4863161a086ddfe07fe315cd0)

@ NPM1300\_EVENT\_SHIPHOLD\_PRESS

**Definition** npm1300.h:30

[NPM1300\_EVENT\_GPIO1\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a82fe1a2bcc5d2a4638d71f2b18fa73c7)

@ NPM1300\_EVENT\_GPIO1\_EDGE

**Definition** npm1300.h:36

[NPM1300\_EVENT\_BATTERY\_DETECTED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a8524187e6aa6ef0683265b1340cc117f)

@ NPM1300\_EVENT\_BATTERY\_DETECTED

**Definition** npm1300.h:28

[NPM1300\_EVENT\_GPIO2\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a87ca56a02af057ff1920c7b2537ccecc)

@ NPM1300\_EVENT\_GPIO2\_EDGE

**Definition** npm1300.h:37

[NPM1300\_EVENT\_GPIO3\_EDGE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a89b2ea4f842c92b118b36003b6b8175a)

@ NPM1300\_EVENT\_GPIO3\_EDGE

**Definition** npm1300.h:38

[NPM1300\_EVENT\_VBUS\_REMOVED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a94a3133140147f38e358ac97ed45ccaf)

@ NPM1300\_EVENT\_VBUS\_REMOVED

**Definition** npm1300.h:34

[NPM1300\_EVENT\_BATTERY\_REMOVED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989a98ff199ec155bd8ce7e42ede4aa90c78)

@ NPM1300\_EVENT\_BATTERY\_REMOVED

**Definition** npm1300.h:29

[NPM1300\_EVENT\_SHIPHOLD\_RELEASE](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989abb790b641b8d0a8d87b2fb5aabbc5bae)

@ NPM1300\_EVENT\_SHIPHOLD\_RELEASE

**Definition** npm1300.h:31

[NPM1300\_EVENT\_VBUS\_DETECTED](group__mdf__interface__npm1300.md#ggad15bf59ebf3c5572347e939c4c2e6989aebe54d5f1704b81873ca2dce17e44a47)

@ NPM1300\_EVENT\_VBUS\_DETECTED

**Definition** npm1300.h:33

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [npm1300.h](drivers_2mfd_2npm1300_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
