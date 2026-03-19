---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/transceiver_8h_source.html
original_path: doxygen/html/transceiver_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

transceiver.h

[Go to the documentation of this file.](transceiver_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_TRANSCEIVER\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_TRANSCEIVER\_H\_

9

10#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

25

31

36typedef int (\*can\_transceiver\_enable\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

37

42typedef int (\*can\_transceiver\_disable\_t)(const struct [device](structdevice.md) \*dev);

43

44\_\_subsystem struct can\_transceiver\_driver\_api {

45 can\_transceiver\_enable\_t enable;

46 can\_transceiver\_disable\_t disable;

47};

48

50

[ 66](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694)static inline int [can\_transceiver\_enable](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode)

67{

68 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(can\_transceiver, dev)->enable(dev, mode);

69}

70

[ 85](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be)static inline int [can\_transceiver\_disable](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be)(const struct [device](structdevice.md) \*dev)

86{

87 return [DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)(can\_transceiver, dev)->disable(dev);

88}

89

93

94#ifdef \_\_cplusplus

95}

96#endif

97

98#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_TRANSCEIVER\_H\_ \*/

[device.h](device_8h.md)

[DEVICE\_API\_GET](device_8h.md#a9907e8ee5e7be8c3b5d52b13bd33970a)

#define DEVICE\_API\_GET(\_class, \_dev)

Expands to the pointer of a device's API for a given class.

**Definition** device.h:1263

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:116

[can\_transceiver\_enable](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694)

static int can\_transceiver\_enable(const struct device \*dev, can\_mode\_t mode)

Enable CAN transceiver.

**Definition** transceiver.h:66

[can\_transceiver\_disable](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be)

static int can\_transceiver\_disable(const struct device \*dev)

Disable CAN transceiver.

**Definition** transceiver.h:85

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [transceiver.h](transceiver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
