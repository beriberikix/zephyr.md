---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nxp__flexio_8h_source.html
original_path: doxygen/html/nxp__flexio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_flexio.h

[Go to the documentation of this file.](nxp__flexio_8h.md)

1/\*

2 \* Copyright (c) 2024, STRIM, ALC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_MISC\_NXP\_FLEXIO\_NXP\_FLEXIO\_H\_

8#define ZEPHYR\_DRIVERS\_MISC\_NXP\_FLEXIO\_NXP\_FLEXIO\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11

[ 17](structnxp__flexio__child__res.md)struct [nxp\_flexio\_child\_res](structnxp__flexio__child__res.md) {

[ 18](structnxp__flexio__child__res.md#afd4633d2dbb04c9155f9088206aa5772) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[shifter\_index](structnxp__flexio__child__res.md#afd4633d2dbb04c9155f9088206aa5772);

[ 19](structnxp__flexio__child__res.md#afac825cb54e1dcd093c8ca19a78fa4dd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [shifter\_count](structnxp__flexio__child__res.md#afac825cb54e1dcd093c8ca19a78fa4dd);

[ 20](structnxp__flexio__child__res.md#ae1187d65f541a282da4651a53b0626d8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[timer\_index](structnxp__flexio__child__res.md#ae1187d65f541a282da4651a53b0626d8);

[ 21](structnxp__flexio__child__res.md#ad62e4adfc76a26841f613552e871a187) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [timer\_count](structnxp__flexio__child__res.md#ad62e4adfc76a26841f613552e871a187);

22};

23

[ 30](nxp__flexio_8h.md#af11959c4e7c7a5ef56b082fcf0b7f42c)typedef int (\*[nxp\_flexio\_child\_isr\_t](nxp__flexio_8h.md#af11959c4e7c7a5ef56b082fcf0b7f42c))(void \*user\_data);

31

[ 36](structnxp__flexio__child.md)struct [nxp\_flexio\_child](structnxp__flexio__child.md) {

[ 37](structnxp__flexio__child.md#a1befee43b0d6a378983a8207fdb23b10) [nxp\_flexio\_child\_isr\_t](nxp__flexio_8h.md#af11959c4e7c7a5ef56b082fcf0b7f42c) [isr](structnxp__flexio__child.md#a1befee43b0d6a378983a8207fdb23b10);

[ 38](structnxp__flexio__child.md#a9490af6c5e89d9994a0419c80757b14e) void \*[user\_data](structnxp__flexio__child.md#a9490af6c5e89d9994a0419c80757b14e);

[ 39](structnxp__flexio__child.md#ae1c82ed160a226d48dee0ad6607cde34) struct [nxp\_flexio\_child\_res](structnxp__flexio__child__res.md) [res](structnxp__flexio__child.md#ae1c82ed160a226d48dee0ad6607cde34);

40};

41

[ 46](nxp__flexio_8h.md#a7e84a09852b713337d6e124eb2b8df7d)void [nxp\_flexio\_irq\_enable](nxp__flexio_8h.md#a7e84a09852b713337d6e124eb2b8df7d)(const struct [device](structdevice.md) \*dev);

47

[ 52](nxp__flexio_8h.md#a39b6b8b2eda354b4d3a40da48f41e3d2)void [nxp\_flexio\_irq\_disable](nxp__flexio_8h.md#a39b6b8b2eda354b4d3a40da48f41e3d2)(const struct [device](structdevice.md) \*dev);

53

[ 58](nxp__flexio_8h.md#a3be561d6ee29eb0e23f67ddcf234d22e)void [nxp\_flexio\_lock](nxp__flexio_8h.md#a3be561d6ee29eb0e23f67ddcf234d22e)(const struct [device](structdevice.md) \*dev);

59

[ 64](nxp__flexio_8h.md#ab5ff53d4ac41321fe4726e2ede175ac2)void [nxp\_flexio\_unlock](nxp__flexio_8h.md#ab5ff53d4ac41321fe4726e2ede175ac2)(const struct [device](structdevice.md) \*dev);

65

[ 76](nxp__flexio_8h.md#a9c5fdb0b5b11dcc04d42c2c7b98b3ffb)int [nxp\_flexio\_get\_rate](nxp__flexio_8h.md#a9c5fdb0b5b11dcc04d42c2c7b98b3ffb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate);

77

[ 85](nxp__flexio_8h.md#a1208ad4ef70419ff61a87b8b1ff8d446)int [nxp\_flexio\_child\_attach](nxp__flexio_8h.md#a1208ad4ef70419ff61a87b8b1ff8d446)(const struct [device](structdevice.md) \*dev,

86 const struct [nxp\_flexio\_child](structnxp__flexio__child.md) \*child);

87

88#endif /\* ZEPHYR\_DRIVERS\_MISC\_NXP\_FLEXIO\_NXP\_FLEXIO\_H\_ \*/

[device.h](device_8h.md)

[nxp\_flexio\_child\_attach](nxp__flexio_8h.md#a1208ad4ef70419ff61a87b8b1ff8d446)

int nxp\_flexio\_child\_attach(const struct device \*dev, const struct nxp\_flexio\_child \*child)

Attach flexio child to flexio controller.

[nxp\_flexio\_irq\_disable](nxp__flexio_8h.md#a39b6b8b2eda354b4d3a40da48f41e3d2)

void nxp\_flexio\_irq\_disable(const struct device \*dev)

Disable FlexIO IRQ.

[nxp\_flexio\_lock](nxp__flexio_8h.md#a3be561d6ee29eb0e23f67ddcf234d22e)

void nxp\_flexio\_lock(const struct device \*dev)

Lock FlexIO mutex.

[nxp\_flexio\_irq\_enable](nxp__flexio_8h.md#a7e84a09852b713337d6e124eb2b8df7d)

void nxp\_flexio\_irq\_enable(const struct device \*dev)

Enable FlexIO IRQ.

[nxp\_flexio\_get\_rate](nxp__flexio_8h.md#a9c5fdb0b5b11dcc04d42c2c7b98b3ffb)

int nxp\_flexio\_get\_rate(const struct device \*dev, uint32\_t \*rate)

Obtain the clock rate of sub-system used by the FlexIO.

[nxp\_flexio\_unlock](nxp__flexio_8h.md#ab5ff53d4ac41321fe4726e2ede175ac2)

void nxp\_flexio\_unlock(const struct device \*dev)

Unlock FlexIO mutex.

[nxp\_flexio\_child\_isr\_t](nxp__flexio_8h.md#af11959c4e7c7a5ef56b082fcf0b7f42c)

int(\* nxp\_flexio\_child\_isr\_t)(void \*user\_data)

Callback API to inform API user that FlexIO triggered interrupt.

**Definition** nxp\_flexio.h:30

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[nxp\_flexio\_child\_res](structnxp__flexio__child__res.md)

Structure containing information about the required resources for a FlexIO child.

**Definition** nxp\_flexio.h:17

[nxp\_flexio\_child\_res::timer\_count](structnxp__flexio__child__res.md#ad62e4adfc76a26841f613552e871a187)

uint8\_t timer\_count

**Definition** nxp\_flexio.h:21

[nxp\_flexio\_child\_res::timer\_index](structnxp__flexio__child__res.md#ae1187d65f541a282da4651a53b0626d8)

uint8\_t \* timer\_index

**Definition** nxp\_flexio.h:20

[nxp\_flexio\_child\_res::shifter\_count](structnxp__flexio__child__res.md#afac825cb54e1dcd093c8ca19a78fa4dd)

uint8\_t shifter\_count

**Definition** nxp\_flexio.h:19

[nxp\_flexio\_child\_res::shifter\_index](structnxp__flexio__child__res.md#afd4633d2dbb04c9155f9088206aa5772)

uint8\_t \* shifter\_index

**Definition** nxp\_flexio.h:18

[nxp\_flexio\_child](structnxp__flexio__child.md)

Structure containing the required child data for FlexIO.

**Definition** nxp\_flexio.h:36

[nxp\_flexio\_child::isr](structnxp__flexio__child.md#a1befee43b0d6a378983a8207fdb23b10)

nxp\_flexio\_child\_isr\_t isr

**Definition** nxp\_flexio.h:37

[nxp\_flexio\_child::user\_data](structnxp__flexio__child.md#a9490af6c5e89d9994a0419c80757b14e)

void \* user\_data

**Definition** nxp\_flexio.h:38

[nxp\_flexio\_child::res](structnxp__flexio__child.md#ae1c82ed160a226d48dee0ad6607cde34)

struct nxp\_flexio\_child\_res res

**Definition** nxp\_flexio.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [nxp\_flexio](dir_f4ffe9d878970d9b53b3a8be58885b76.md)
- [nxp\_flexio.h](nxp__flexio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
