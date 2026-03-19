---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gpio__mmio32_8h_source.html
original_path: doxygen/html/gpio__mmio32_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_mmio32.h

[Go to the documentation of this file.](gpio__mmio32_8h.md)

1/\*

2 \* Copyright (c) 2016 Linaro Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_MMIO32\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_MMIO32\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18extern const struct gpio\_driver\_api [gpio\_mmio32\_api](gpio__mmio32_8h.md#ab8dc4ce9baa25b80565dbde9fd05dcb4);

19

[ 20](structgpio__mmio32__config.md)struct [gpio\_mmio32\_config](structgpio__mmio32__config.md) {

21 /\* gpio\_driver\_config needs to be first \*/

[ 22](structgpio__mmio32__config.md#ad5fd7d3cfb793bf0c1508e3893e93988) struct [gpio\_driver\_config](structgpio__driver__config.md) [common](structgpio__mmio32__config.md#ad5fd7d3cfb793bf0c1508e3893e93988);

[ 23](structgpio__mmio32__config.md#a5fbef61f21b8d8ac405cd511ed7b68d3) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[reg](structgpio__mmio32__config.md#a5fbef61f21b8d8ac405cd511ed7b68d3);

[ 24](structgpio__mmio32__config.md#a8ad0efe01100ad441e5c3cc39c23c2ca) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mask](structgpio__mmio32__config.md#a8ad0efe01100ad441e5c3cc39c23c2ca);

25};

26

[ 27](structgpio__mmio32__context.md)struct [gpio\_mmio32\_context](structgpio__mmio32__context.md) {

28 /\* gpio\_driver\_data needs to be first \*/

[ 29](structgpio__mmio32__context.md#abb005d6012734b1b1c5e1dea59c803a9) struct [gpio\_driver\_data](structgpio__driver__data.md) [common](structgpio__mmio32__context.md#abb005d6012734b1b1c5e1dea59c803a9);

[ 30](structgpio__mmio32__context.md#ac529b2beb2e3e5591eb6dfda590d725b) const struct [gpio\_mmio32\_config](structgpio__mmio32__config.md) \*[config](structgpio__mmio32__context.md#ac529b2beb2e3e5591eb6dfda590d725b);

31};

32

[ 33](gpio__mmio32_8h.md#a1896015c34f1b9dac9d8c50b391fdec0)int [gpio\_mmio32\_init](gpio__mmio32_8h.md#a1896015c34f1b9dac9d8c50b391fdec0)(const struct [device](structdevice.md) \*dev);

34

35#ifdef CONFIG\_GPIO\_MMIO32

36

48#define GPIO\_MMIO32\_INIT(node\_id, \_address, \_mask) \

49static struct gpio\_mmio32\_context \_CONCAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_ctx); \

50 \

51static const struct gpio\_mmio32\_config \_CONCAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_cfg) = { \

52 .common = { \

53 .port\_pin\_mask = \_mask, \

54 }, \

55 .reg = (volatile uint32\_t \*)\_address, \

56 .mask = \_mask, \

57}; \

58 \

59DEVICE\_DT\_DEFINE(node\_id, \

60 &gpio\_mmio32\_init, \

61 NULL, \

62 &\_CONCAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_ctx), \

63 &\_CONCAT(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_cfg), \

64 PRE\_KERNEL\_1, CONFIG\_KERNEL\_INIT\_PRIORITY\_DEVICE, \

65 &gpio\_mmio32\_api)

66

67

68#else /\* CONFIG\_GPIO\_MMIO32 \*/

69

70/\* Null definition for when support not configured into kernel \*/

[ 71](gpio__mmio32_8h.md#a91033e14faef5aebc20314549e08e932)#define GPIO\_MMIO32\_INIT(node\_id, \_address, \_mask)

72

73#endif

74

75#ifdef \_\_cplusplus

76}

77#endif

78

79#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GPIO\_GPIO\_MMIO32\_H\_ \*/

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_mmio32\_init](gpio__mmio32_8h.md#a1896015c34f1b9dac9d8c50b391fdec0)

int gpio\_mmio32\_init(const struct device \*dev)

[gpio\_mmio32\_api](gpio__mmio32_8h.md#ab8dc4ce9baa25b80565dbde9fd05dcb4)

const struct gpio\_driver\_api gpio\_mmio32\_api

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[gpio\_driver\_config](structgpio__driver__config.md)

This structure is common to all GPIO drivers and is expected to be the first element in the object po...

**Definition** gpio.h:690

[gpio\_driver\_data](structgpio__driver__data.md)

This structure is common to all GPIO drivers and is expected to be the first element in the driver's ...

**Definition** gpio.h:703

[gpio\_mmio32\_config](structgpio__mmio32__config.md)

**Definition** gpio\_mmio32.h:20

[gpio\_mmio32\_config::reg](structgpio__mmio32__config.md#a5fbef61f21b8d8ac405cd511ed7b68d3)

volatile uint32\_t \* reg

**Definition** gpio\_mmio32.h:23

[gpio\_mmio32\_config::mask](structgpio__mmio32__config.md#a8ad0efe01100ad441e5c3cc39c23c2ca)

uint32\_t mask

**Definition** gpio\_mmio32.h:24

[gpio\_mmio32\_config::common](structgpio__mmio32__config.md#ad5fd7d3cfb793bf0c1508e3893e93988)

struct gpio\_driver\_config common

**Definition** gpio\_mmio32.h:22

[gpio\_mmio32\_context](structgpio__mmio32__context.md)

**Definition** gpio\_mmio32.h:27

[gpio\_mmio32\_context::common](structgpio__mmio32__context.md#abb005d6012734b1b1c5e1dea59c803a9)

struct gpio\_driver\_data common

**Definition** gpio\_mmio32.h:29

[gpio\_mmio32\_context::config](structgpio__mmio32__context.md#ac529b2beb2e3e5591eb6dfda590d725b)

const struct gpio\_mmio32\_config \* config

**Definition** gpio\_mmio32.h:30

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_mmio32.h](gpio__mmio32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
