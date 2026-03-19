---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2mfd_2npm2100_8h_source.html
original_path: doxygen/html/drivers_2mfd_2npm2100_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm2100.h

[Go to the documentation of this file.](drivers_2mfd_2npm2100_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM2100\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM2100\_H\_

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

[ 25](group__mdf__interface__npm2100.md#gae7433fd9cb33e7b3ac0b364d29dc6e32)enum [mfd\_npm2100\_event](group__mdf__interface__npm2100.md#gae7433fd9cb33e7b3ac0b364d29dc6e32) {

[ 26](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a40949e797419f2e317d49aad99ea5a88) [NPM2100\_EVENT\_SYS\_DIETEMP\_WARN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a40949e797419f2e317d49aad99ea5a88),

[ 27](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a51417298380c8aa90363d42370da3eff) [NPM2100\_EVENT\_SYS\_SHIPHOLD\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a51417298380c8aa90363d42370da3eff),

[ 28](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae70e607cc5cab890f3ee0388d192cd8d) [NPM2100\_EVENT\_SYS\_SHIPHOLD\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae70e607cc5cab890f3ee0388d192cd8d),

[ 29](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac16dbc92e22bfe720f00c7accd310443) [NPM2100\_EVENT\_SYS\_PGRESET\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac16dbc92e22bfe720f00c7accd310443),

[ 30](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a15406e035cadb7b3db4ffdcbc5b0dd4b) [NPM2100\_EVENT\_SYS\_PGRESET\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a15406e035cadb7b3db4ffdcbc5b0dd4b),

[ 31](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1cc0fb1202d777d1d15f866ef28eae4a) [NPM2100\_EVENT\_SYS\_TIMER\_EXPIRY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1cc0fb1202d777d1d15f866ef28eae4a),

[ 32](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b7adcddff5f20f35c421c9a0e296878) [NPM2100\_EVENT\_ADC\_VBAT\_READY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b7adcddff5f20f35c421c9a0e296878),

[ 33](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a3508143e9a6cc45aab022cb1d41c1f68) [NPM2100\_EVENT\_ADC\_DIETEMP\_READY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a3508143e9a6cc45aab022cb1d41c1f68),

[ 34](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1760e35770442b55a82176fbf8e18b49) [NPM2100\_EVENT\_ADC\_DROOP\_DETECT](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1760e35770442b55a82176fbf8e18b49),

[ 35](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a739b885852e147e69b3bf638fd41f11c) [NPM2100\_EVENT\_ADC\_VOUT\_READY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a739b885852e147e69b3bf638fd41f11c),

[ 36](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a5685e6db1ae012bf52fe84564e6d1333) [NPM2100\_EVENT\_GPIO0\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a5685e6db1ae012bf52fe84564e6d1333),

[ 37](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b942a768806d76a82dfcdb5e657f60f) [NPM2100\_EVENT\_GPIO0\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b942a768806d76a82dfcdb5e657f60f),

[ 38](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a66f462631778912d296b94639be9e453) [NPM2100\_EVENT\_GPIO1\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a66f462631778912d296b94639be9e453),

[ 39](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a244e3e287d8657bfde5696b9a59d0a25) [NPM2100\_EVENT\_GPIO1\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a244e3e287d8657bfde5696b9a59d0a25),

[ 40](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ada55f1aadb3d0159ca93512fa8ca37e6) [NPM2100\_EVENT\_BOOST\_VBAT\_WARN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ada55f1aadb3d0159ca93512fa8ca37e6),

[ 41](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae903153d89f42a509fb2c12e5d58d948) [NPM2100\_EVENT\_BOOST\_VOUT\_MIN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae903153d89f42a509fb2c12e5d58d948),

[ 42](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a523b2a318b7d0217d52fc460b9d90687) [NPM2100\_EVENT\_BOOST\_VOUT\_WARN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a523b2a318b7d0217d52fc460b9d90687),

[ 43](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ad61a6868a4eaf9ae53270da2f617a4d8) [NPM2100\_EVENT\_BOOST\_VOUT\_DPS](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ad61a6868a4eaf9ae53270da2f617a4d8),

[ 44](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a764671a05e6d92b140c7ac216ca3b883) [NPM2100\_EVENT\_BOOST\_VOUT\_OK](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a764671a05e6d92b140c7ac216ca3b883),

[ 45](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a6303f8860213e5de6514b483060354f2) [NPM2100\_EVENT\_LDOSW\_OCP](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a6303f8860213e5de6514b483060354f2),

[ 46](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a0bbb9e1c1a73735c734e17527a424f7f) [NPM2100\_EVENT\_LDOSW\_VINTFAIL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a0bbb9e1c1a73735c734e17527a424f7f),

[ 47](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac6f32faf88a0d8f5cf951c00900aca81) [NPM2100\_EVENT\_MAX](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac6f32faf88a0d8f5cf951c00900aca81)

48};

49

[ 50](group__mdf__interface__npm2100.md#ga6a89922f19450ace9d83a4e110625cfb)enum [mfd\_npm2100\_timer\_mode](group__mdf__interface__npm2100.md#ga6a89922f19450ace9d83a4e110625cfb) {

[ 51](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfba421611694d6f42d3e0e8ae1bbafbb03d) [NPM2100\_TIMER\_MODE\_GENERAL\_PURPOSE](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfba421611694d6f42d3e0e8ae1bbafbb03d),

[ 52](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad84e4df7668b904c2af3c537775354c6) [NPM2100\_TIMER\_MODE\_WDT\_RESET](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad84e4df7668b904c2af3c537775354c6),

[ 53](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad110b2ee5d1007416dce11faf71ae34c) [NPM2100\_TIMER\_MODE\_WDT\_POWER\_CYCLE](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad110b2ee5d1007416dce11faf71ae34c),

[ 54](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad3c74cd6c665f5cc49c57d83f873f276) [NPM2100\_TIMER\_MODE\_WAKEUP](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad3c74cd6c665f5cc49c57d83f873f276),

55};

56

[ 70](group__mdf__interface__npm2100.md#gaa684cdb822e0e36fefc74b59bfd2b706)int [mfd\_npm2100\_set\_timer](group__mdf__interface__npm2100.md#gaa684cdb822e0e36fefc74b59bfd2b706)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms,

71 enum [mfd\_npm2100\_timer\_mode](group__mdf__interface__npm2100.md#ga6a89922f19450ace9d83a4e110625cfb) mode);

72

[ 80](group__mdf__interface__npm2100.md#ga085bc3c2d5d775c55ae598a464c9d265)int [mfd\_npm2100\_start\_timer](group__mdf__interface__npm2100.md#ga085bc3c2d5d775c55ae598a464c9d265)(const struct [device](structdevice.md) \*dev);

81

[ 89](group__mdf__interface__npm2100.md#gac87a33389dfbf30e7f0059bd6aede7dc)int [mfd\_npm2100\_reset](group__mdf__interface__npm2100.md#gac87a33389dfbf30e7f0059bd6aede7dc)(const struct [device](structdevice.md) \*dev);

90

[ 106](group__mdf__interface__npm2100.md#ga4d34ac6e2c185976bc696ce0091b375a)int [mfd\_npm2100\_hibernate](group__mdf__interface__npm2100.md#ga4d34ac6e2c185976bc696ce0091b375a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms, bool pass\_through);

107

[ 115](group__mdf__interface__npm2100.md#ga137976d9909ad6ec179dce5722c4b865)int [mfd\_npm2100\_add\_callback](group__mdf__interface__npm2100.md#ga137976d9909ad6ec179dce5722c4b865)(const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback);

116

[ 124](group__mdf__interface__npm2100.md#ga342de8853f0afd2cdab08d2d42883b47)int [mfd\_npm2100\_remove\_callback](group__mdf__interface__npm2100.md#ga342de8853f0afd2cdab08d2d42883b47)(const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback);

125

127

128#ifdef \_\_cplusplus

129}

130#endif

131

132#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_NPM2100\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[mfd\_npm2100\_start\_timer](group__mdf__interface__npm2100.md#ga085bc3c2d5d775c55ae598a464c9d265)

int mfd\_npm2100\_start\_timer(const struct device \*dev)

Start npm2100 timer.

[mfd\_npm2100\_add\_callback](group__mdf__interface__npm2100.md#ga137976d9909ad6ec179dce5722c4b865)

int mfd\_npm2100\_add\_callback(const struct device \*dev, struct gpio\_callback \*callback)

Add npm2100 event callback.

[mfd\_npm2100\_remove\_callback](group__mdf__interface__npm2100.md#ga342de8853f0afd2cdab08d2d42883b47)

int mfd\_npm2100\_remove\_callback(const struct device \*dev, struct gpio\_callback \*callback)

Remove npm2100 event callback.

[mfd\_npm2100\_hibernate](group__mdf__interface__npm2100.md#ga4d34ac6e2c185976bc696ce0091b375a)

int mfd\_npm2100\_hibernate(const struct device \*dev, uint32\_t time\_ms, bool pass\_through)

npm2100 hibernate

[mfd\_npm2100\_timer\_mode](group__mdf__interface__npm2100.md#ga6a89922f19450ace9d83a4e110625cfb)

mfd\_npm2100\_timer\_mode

**Definition** npm2100.h:50

[mfd\_npm2100\_set\_timer](group__mdf__interface__npm2100.md#gaa684cdb822e0e36fefc74b59bfd2b706)

int mfd\_npm2100\_set\_timer(const struct device \*dev, uint32\_t time\_ms, enum mfd\_npm2100\_timer\_mode mode)

Write npm2100 timer register.

[mfd\_npm2100\_reset](group__mdf__interface__npm2100.md#gac87a33389dfbf30e7f0059bd6aede7dc)

int mfd\_npm2100\_reset(const struct device \*dev)

npm2100 full power reset

[mfd\_npm2100\_event](group__mdf__interface__npm2100.md#gae7433fd9cb33e7b3ac0b364d29dc6e32)

mfd\_npm2100\_event

**Definition** npm2100.h:25

[NPM2100\_TIMER\_MODE\_GENERAL\_PURPOSE](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfba421611694d6f42d3e0e8ae1bbafbb03d)

@ NPM2100\_TIMER\_MODE\_GENERAL\_PURPOSE

**Definition** npm2100.h:51

[NPM2100\_TIMER\_MODE\_WDT\_POWER\_CYCLE](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad110b2ee5d1007416dce11faf71ae34c)

@ NPM2100\_TIMER\_MODE\_WDT\_POWER\_CYCLE

**Definition** npm2100.h:53

[NPM2100\_TIMER\_MODE\_WAKEUP](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad3c74cd6c665f5cc49c57d83f873f276)

@ NPM2100\_TIMER\_MODE\_WAKEUP

**Definition** npm2100.h:54

[NPM2100\_TIMER\_MODE\_WDT\_RESET](group__mdf__interface__npm2100.md#gga6a89922f19450ace9d83a4e110625cfbad84e4df7668b904c2af3c537775354c6)

@ NPM2100\_TIMER\_MODE\_WDT\_RESET

**Definition** npm2100.h:52

[NPM2100\_EVENT\_LDOSW\_VINTFAIL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a0bbb9e1c1a73735c734e17527a424f7f)

@ NPM2100\_EVENT\_LDOSW\_VINTFAIL

**Definition** npm2100.h:46

[NPM2100\_EVENT\_SYS\_PGRESET\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a15406e035cadb7b3db4ffdcbc5b0dd4b)

@ NPM2100\_EVENT\_SYS\_PGRESET\_RISE

**Definition** npm2100.h:30

[NPM2100\_EVENT\_ADC\_DROOP\_DETECT](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1760e35770442b55a82176fbf8e18b49)

@ NPM2100\_EVENT\_ADC\_DROOP\_DETECT

**Definition** npm2100.h:34

[NPM2100\_EVENT\_SYS\_TIMER\_EXPIRY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1cc0fb1202d777d1d15f866ef28eae4a)

@ NPM2100\_EVENT\_SYS\_TIMER\_EXPIRY

**Definition** npm2100.h:31

[NPM2100\_EVENT\_GPIO1\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a244e3e287d8657bfde5696b9a59d0a25)

@ NPM2100\_EVENT\_GPIO1\_RISE

**Definition** npm2100.h:39

[NPM2100\_EVENT\_ADC\_VBAT\_READY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b7adcddff5f20f35c421c9a0e296878)

@ NPM2100\_EVENT\_ADC\_VBAT\_READY

**Definition** npm2100.h:32

[NPM2100\_EVENT\_GPIO0\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b942a768806d76a82dfcdb5e657f60f)

@ NPM2100\_EVENT\_GPIO0\_RISE

**Definition** npm2100.h:37

[NPM2100\_EVENT\_ADC\_DIETEMP\_READY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a3508143e9a6cc45aab022cb1d41c1f68)

@ NPM2100\_EVENT\_ADC\_DIETEMP\_READY

**Definition** npm2100.h:33

[NPM2100\_EVENT\_SYS\_DIETEMP\_WARN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a40949e797419f2e317d49aad99ea5a88)

@ NPM2100\_EVENT\_SYS\_DIETEMP\_WARN

**Definition** npm2100.h:26

[NPM2100\_EVENT\_SYS\_SHIPHOLD\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a51417298380c8aa90363d42370da3eff)

@ NPM2100\_EVENT\_SYS\_SHIPHOLD\_FALL

**Definition** npm2100.h:27

[NPM2100\_EVENT\_BOOST\_VOUT\_WARN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a523b2a318b7d0217d52fc460b9d90687)

@ NPM2100\_EVENT\_BOOST\_VOUT\_WARN

**Definition** npm2100.h:42

[NPM2100\_EVENT\_GPIO0\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a5685e6db1ae012bf52fe84564e6d1333)

@ NPM2100\_EVENT\_GPIO0\_FALL

**Definition** npm2100.h:36

[NPM2100\_EVENT\_LDOSW\_OCP](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a6303f8860213e5de6514b483060354f2)

@ NPM2100\_EVENT\_LDOSW\_OCP

**Definition** npm2100.h:45

[NPM2100\_EVENT\_GPIO1\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a66f462631778912d296b94639be9e453)

@ NPM2100\_EVENT\_GPIO1\_FALL

**Definition** npm2100.h:38

[NPM2100\_EVENT\_ADC\_VOUT\_READY](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a739b885852e147e69b3bf638fd41f11c)

@ NPM2100\_EVENT\_ADC\_VOUT\_READY

**Definition** npm2100.h:35

[NPM2100\_EVENT\_BOOST\_VOUT\_OK](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32a764671a05e6d92b140c7ac216ca3b883)

@ NPM2100\_EVENT\_BOOST\_VOUT\_OK

**Definition** npm2100.h:44

[NPM2100\_EVENT\_SYS\_PGRESET\_FALL](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac16dbc92e22bfe720f00c7accd310443)

@ NPM2100\_EVENT\_SYS\_PGRESET\_FALL

**Definition** npm2100.h:29

[NPM2100\_EVENT\_MAX](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac6f32faf88a0d8f5cf951c00900aca81)

@ NPM2100\_EVENT\_MAX

**Definition** npm2100.h:47

[NPM2100\_EVENT\_BOOST\_VOUT\_DPS](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ad61a6868a4eaf9ae53270da2f617a4d8)

@ NPM2100\_EVENT\_BOOST\_VOUT\_DPS

**Definition** npm2100.h:43

[NPM2100\_EVENT\_BOOST\_VBAT\_WARN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ada55f1aadb3d0159ca93512fa8ca37e6)

@ NPM2100\_EVENT\_BOOST\_VBAT\_WARN

**Definition** npm2100.h:40

[NPM2100\_EVENT\_SYS\_SHIPHOLD\_RISE](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae70e607cc5cab890f3ee0388d192cd8d)

@ NPM2100\_EVENT\_SYS\_SHIPHOLD\_RISE

**Definition** npm2100.h:28

[NPM2100\_EVENT\_BOOST\_VOUT\_MIN](group__mdf__interface__npm2100.md#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae903153d89f42a509fb2c12e5d58d948)

@ NPM2100\_EVENT\_BOOST\_VOUT\_MIN

**Definition** npm2100.h:41

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[gpio\_callback](structgpio__callback.md)

GPIO callback structure.

**Definition** gpio.h:741

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [npm2100.h](drivers_2mfd_2npm2100_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
