---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/transceiver_8h_source.html
original_path: doxygen/html/transceiver_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

23

29

34typedef int (\*can\_transceiver\_enable\_t)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

35

40typedef int (\*can\_transceiver\_disable\_t)(const struct [device](structdevice.md) \*dev);

41

42\_\_subsystem struct can\_transceiver\_driver\_api {

43 can\_transceiver\_enable\_t enable;

44 can\_transceiver\_disable\_t disable;

45};

46

48

[ 64](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694)static inline int [can\_transceiver\_enable](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode)

65{

66 const struct can\_transceiver\_driver\_api \*api =

67 (const struct can\_transceiver\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

68

69 return api->enable(dev, mode);

70}

71

[ 86](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be)static inline int [can\_transceiver\_disable](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be)(const struct [device](structdevice.md) \*dev)

87{

88 const struct can\_transceiver\_driver\_api \*api =

89 (const struct can\_transceiver\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

90

91 return api->disable(dev);

92}

93

97

98#ifdef \_\_cplusplus

99}

100#endif

101

102#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_TRANSCEIVER\_H\_ \*/

[device.h](device_8h.md)

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:116

[can\_transceiver\_enable](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694)

static int can\_transceiver\_enable(const struct device \*dev, can\_mode\_t mode)

Enable CAN transceiver.

**Definition** transceiver.h:64

[can\_transceiver\_disable](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be)

static int can\_transceiver\_disable(const struct device \*dev)

Disable CAN transceiver.

**Definition** transceiver.h:86

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [transceiver.h](transceiver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
