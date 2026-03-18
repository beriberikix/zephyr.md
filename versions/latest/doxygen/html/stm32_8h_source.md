---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32_8h_source.html
original_path: doxygen/html/stm32_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32.h

[Go to the documentation of this file.](stm32_8h.md)

1/\*

2 \* Copyright (c) 2023 SILA Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_STM32\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_STM32\_H\_

10

11#include <[zephyr/device.h](device_8h.md)>

12

[ 13](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730)enum [i2c\_stm32\_mode](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730) {

[ 14](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730af4173c801cc5a4aeddd8bb1e01e74250) [I2CSTM32MODE\_I2C](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730af4173c801cc5a4aeddd8bb1e01e74250),

[ 15](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730a7a56a445c59c7fe860945a2e4a11c61b) [I2CSTM32MODE\_SMBUSHOST](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730a7a56a445c59c7fe860945a2e4a11c61b),

[ 16](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730ac8a7757cd18406545dbfb72df6c6162b) [I2CSTM32MODE\_SMBUSDEVICE](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730ac8a7757cd18406545dbfb72df6c6162b),

[ 17](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730aec2ff625d8a070fbd7ffe9246eb6bf07) [I2CSTM32MODE\_SMBUSDEVICEARP](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730aec2ff625d8a070fbd7ffe9246eb6bf07),

18};

19

[ 20](stm32_8h.md#ae82dc3ada1276b676169c95c6d239d82)void [i2c\_stm32\_set\_smbus\_mode](stm32_8h.md#ae82dc3ada1276b676169c95c6d239d82)(const struct [device](structdevice.md) \*dev, enum [i2c\_stm32\_mode](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730) mode);

21

22#ifdef CONFIG\_SMBUS\_STM32\_SMBALERT

23typedef void (\*i2c\_stm32\_smbalert\_cb\_func\_t)(const struct [device](structdevice.md) \*dev);

24

25void i2c\_stm32\_smbalert\_set\_callback(const struct [device](structdevice.md) \*dev, i2c\_stm32\_smbalert\_cb\_func\_t func,

26 const struct [device](structdevice.md) \*cb\_dev);

27void i2c\_stm32\_smbalert\_enable(const struct [device](structdevice.md) \*dev);

28void i2c\_stm32\_smbalert\_disable(const struct [device](structdevice.md) \*dev);

29#endif /\* CONFIG\_SMBUS\_STM32\_SMBALERT \*/

30

31#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_STM32\_H\_ \*/

[device.h](device_8h.md)

[i2c\_stm32\_mode](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730)

i2c\_stm32\_mode

**Definition** stm32.h:13

[I2CSTM32MODE\_SMBUSHOST](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730a7a56a445c59c7fe860945a2e4a11c61b)

@ I2CSTM32MODE\_SMBUSHOST

**Definition** stm32.h:15

[I2CSTM32MODE\_SMBUSDEVICE](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730ac8a7757cd18406545dbfb72df6c6162b)

@ I2CSTM32MODE\_SMBUSDEVICE

**Definition** stm32.h:16

[I2CSTM32MODE\_SMBUSDEVICEARP](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730aec2ff625d8a070fbd7ffe9246eb6bf07)

@ I2CSTM32MODE\_SMBUSDEVICEARP

**Definition** stm32.h:17

[I2CSTM32MODE\_I2C](stm32_8h.md#a1e3b0af0114531103001ffac5dc10730af4173c801cc5a4aeddd8bb1e01e74250)

@ I2CSTM32MODE\_I2C

**Definition** stm32.h:14

[i2c\_stm32\_set\_smbus\_mode](stm32_8h.md#ae82dc3ada1276b676169c95c6d239d82)

void i2c\_stm32\_set\_smbus\_mode(const struct device \*dev, enum i2c\_stm32\_mode mode)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [stm32.h](stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
