---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/eth__nxp__enet__qos_8h_source.html
original_path: doxygen/html/eth__nxp__enet__qos_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_nxp\_enet\_qos.h

[Go to the documentation of this file.](eth__nxp__enet__qos_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_QOS\_H\_\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_QOS\_H\_\_

9

10#include <fsl\_device\_registers.h>

11#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

12

13/\* Different platforms named the peripheral different in the register definitions \*/

14#ifdef CONFIG\_SOC\_SERIES\_MCXN

15#undef ENET

16#define ENET\_QOS\_NAME ENET

17#define ENET\_QOS\_ALIGNMENT 4

18typedef ENET\_Type enet\_qos\_t;

19#else

20#error "ENET\_QOS not enabled on this SOC series"

21#endif

22

23#define \_PREFIX\_UNDERLINE(x) \_##x

24#define \_ENET\_QOS\_REG\_FIELD(reg, field) MACRO\_MAP\_CAT(\_PREFIX\_UNDERLINE, reg, field, MASK)

25#define \_ENET\_QOS\_REG\_MASK(reg, field) CONCAT(ENET\_QOS\_NAME, \_ENET\_QOS\_REG\_FIELD(reg, field))

26

27/\* Deciphers value of a field from a read value of an enet qos register

28 \*

29 \* reg: name of the register

30 \* field: name of the bit field within the register

31 \* val: value that had been read from the register

32 \*/

[ 33](eth__nxp__enet__qos_8h.md#abab3f7ab5002f46083788303b4b4d645)#define ENET\_QOS\_REG\_GET(reg, field, val) FIELD\_GET(\_ENET\_QOS\_REG\_MASK(reg, field), val)

34

35/\* Prepares value of a field for a write to an enet qos register

36 \*

37 \* reg: name of the register

38 \* field: name of the bit field within the register

39 \* val: value to put into the field

40 \*/

[ 41](eth__nxp__enet__qos_8h.md#a1e774124651c10843efc0feaf426225f)#define ENET\_QOS\_REG\_PREP(reg, field, val) FIELD\_PREP(\_ENET\_QOS\_REG\_MASK(reg, field), val)

42

43

[ 44](eth__nxp__enet__qos_8h.md#a43e2b2075cec6bc77dbbaf606a14df6f)#define ENET\_QOS\_ALIGN\_ADDR\_SHIFT(x) (x >> (ENET\_QOS\_ALIGNMENT >> 1))

45

[ 46](structnxp__enet__qos__config.md)struct [nxp\_enet\_qos\_config](structnxp__enet__qos__config.md) {

[ 47](structnxp__enet__qos__config.md#aee279c78eb397e48b8bb98e34ee74ed6) const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*[pincfg](structnxp__enet__qos__config.md#aee279c78eb397e48b8bb98e34ee74ed6);

[ 48](structnxp__enet__qos__config.md#adccf48e699c07360b1d6989b3e99b271) const struct [device](structdevice.md) \*[clock\_dev](structnxp__enet__qos__config.md#adccf48e699c07360b1d6989b3e99b271);

[ 49](structnxp__enet__qos__config.md#a60394ad2fbfe59bcfc1c36d403be1c01) [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) [clock\_subsys](structnxp__enet__qos__config.md#a60394ad2fbfe59bcfc1c36d403be1c01);

[ 50](structnxp__enet__qos__config.md#a45491916ea24ab9b99fe2fc14cf94552) enet\_qos\_t \*[base](structnxp__enet__qos__config.md#a45491916ea24ab9b99fe2fc14cf94552);

51};

[ 52](eth__nxp__enet__qos_8h.md#ae47d351bc24796a02b96e854c02fe630)#define ENET\_QOS\_MODULE\_CFG(module\_dev) ((struct nxp\_enet\_qos\_config \*) module\_dev->config)

53

54#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_NXP\_ENET\_H\_\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)

void \* clock\_control\_subsys\_t

clock\_control\_subsys\_t is a type to identify a clock controller sub-system.

**Definition** clock\_control.h:58

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[nxp\_enet\_qos\_config](structnxp__enet__qos__config.md)

**Definition** eth\_nxp\_enet\_qos.h:46

[nxp\_enet\_qos\_config::base](structnxp__enet__qos__config.md#a45491916ea24ab9b99fe2fc14cf94552)

enet\_qos\_t \* base

**Definition** eth\_nxp\_enet\_qos.h:50

[nxp\_enet\_qos\_config::clock\_subsys](structnxp__enet__qos__config.md#a60394ad2fbfe59bcfc1c36d403be1c01)

clock\_control\_subsys\_t clock\_subsys

**Definition** eth\_nxp\_enet\_qos.h:49

[nxp\_enet\_qos\_config::clock\_dev](structnxp__enet__qos__config.md#adccf48e699c07360b1d6989b3e99b271)

const struct device \* clock\_dev

**Definition** eth\_nxp\_enet\_qos.h:48

[nxp\_enet\_qos\_config::pincfg](structnxp__enet__qos__config.md#aee279c78eb397e48b8bb98e34ee74ed6)

const struct pinctrl\_dev\_config \* pincfg

**Definition** eth\_nxp\_enet\_qos.h:47

[pinctrl\_dev\_config](structpinctrl__dev__config.md)

Pin controller configuration for a given device.

**Definition** pinctrl.h:62

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_nxp\_enet\_qos.h](eth__nxp__enet__qos_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
