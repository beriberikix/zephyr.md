---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gpio__intc__stm32_8h_source.html
original_path: doxygen/html/gpio__intc__stm32_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_intc\_stm32.h

[Go to the documentation of this file.](gpio__intc__stm32_8h.md)

1/\*

2 \* Copyright (c) 2016 Open-RnD Sp. z o.o.

3 \* Copyright (c) 2024 STMicroelectronics

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_GPIO\_INTC\_STM32\_H\_

16#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_GPIO\_INTC\_STM32\_H\_

17

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

20

[ 24](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374);

25

[ 30](gpio__intc__stm32_8h.md#a03badd2828ca67e3f8adadc75fec2bd2)[stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374) [stm32\_gpio\_intc\_get\_pin\_irq\_line](gpio__intc__stm32_8h.md#a03badd2828ca67e3f8adadc75fec2bd2)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin);

31

[ 37](gpio__intc__stm32_8h.md#ad1c9359de9847ebd2670987302c48f8d)void [stm32\_gpio\_intc\_enable\_line](gpio__intc__stm32_8h.md#ad1c9359de9847ebd2670987302c48f8d)([stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374) line);

38

[ 44](gpio__intc__stm32_8h.md#a0bb3bd355218c41e9173f061f46ec997)void [stm32\_gpio\_intc\_disable\_line](gpio__intc__stm32_8h.md#a0bb3bd355218c41e9173f061f46ec997)([stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374) line);

45

[ 49](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61)enum [stm32\_gpio\_irq\_trigger](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61) {

50 /\* No trigger \*/

[ 51](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2) [STM32\_GPIO\_IRQ\_TRIG\_NONE](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2) = 0x0,

52 /\* Trigger on rising edge \*/

[ 53](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae) [STM32\_GPIO\_IRQ\_TRIG\_RISING](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae) = 0x1,

54 /\* Trigger on falling edge \*/

[ 55](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9) [STM32\_GPIO\_IRQ\_TRIG\_FALLING](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9) = 0x2,

56 /\* Trigger on both rising and falling edge \*/

[ 57](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301) [STM32\_GPIO\_IRQ\_TRIG\_BOTH](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301) = 0x3,

58 /\* Trigger on high level \*/

[ 59](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048) [STM32\_GPIO\_IRQ\_TRIG\_HIGH\_LEVEL](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048) = 0x4,

60 /\* Trigger on low level \*/

[ 61](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c) [STM32\_GPIO\_IRQ\_TRIG\_LOW\_LEVEL](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c) = 0x5

62};

63

[ 70](gpio__intc__stm32_8h.md#a23b9ea466101b4367232237ab5a9a42f)void [stm32\_gpio\_intc\_select\_line\_trigger](gpio__intc__stm32_8h.md#a23b9ea466101b4367232237ab5a9a42f)([stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374) line, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trg);

71

[ 80](gpio__intc__stm32_8h.md#a69ad9c575223c813f484423e56200560)typedef void (\*[stm32\_gpio\_irq\_cb\_t](gpio__intc__stm32_8h.md#a69ad9c575223c813f484423e56200560))([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin, void \*user);

81

[ 90](gpio__intc__stm32_8h.md#a4a750e87f445487c517f24a0266f6a4b)int [stm32\_gpio\_intc\_set\_irq\_callback](gpio__intc__stm32_8h.md#a4a750e87f445487c517f24a0266f6a4b)([stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374) line,

91 [stm32\_gpio\_irq\_cb\_t](gpio__intc__stm32_8h.md#a69ad9c575223c813f484423e56200560) cb, void \*user);

92

[ 98](gpio__intc__stm32_8h.md#a21b0c2213fbcdf179c8b4bdb29561863)void [stm32\_gpio\_intc\_remove\_irq\_callback](gpio__intc__stm32_8h.md#a21b0c2213fbcdf179c8b4bdb29561863)([stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374) line);

99

101

102#if defined(CONFIG\_EXTI\_STM32) /\* EXTI-specific extensions \*/

109void stm32\_exti\_set\_line\_src\_port([gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) line, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) port);

110

117[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) stm32\_exti\_get\_line\_src\_port([gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) line);

118#endif /\* CONFIG\_EXTI\_STM32 \*/

119

120#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_GPIO\_INTC\_STM32\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[stm32\_gpio\_intc\_get\_pin\_irq\_line](gpio__intc__stm32_8h.md#a03badd2828ca67e3f8adadc75fec2bd2)

stm32\_gpio\_irq\_line\_t stm32\_gpio\_intc\_get\_pin\_irq\_line(uint32\_t port, gpio\_pin\_t pin)

Get the GPIO interrupt line value corresponding to specified pin of GPIO port port.

[stm32\_gpio\_intc\_disable\_line](gpio__intc__stm32_8h.md#a0bb3bd355218c41e9173f061f46ec997)

void stm32\_gpio\_intc\_disable\_line(stm32\_gpio\_irq\_line\_t line)

Disable GPIO interrupts for specified line.

[stm32\_gpio\_intc\_remove\_irq\_callback](gpio__intc__stm32_8h.md#a21b0c2213fbcdf179c8b4bdb29561863)

void stm32\_gpio\_intc\_remove\_irq\_callback(stm32\_gpio\_irq\_line\_t line)

Removes the interrupt callback of specified EXTI line.

[stm32\_gpio\_intc\_select\_line\_trigger](gpio__intc__stm32_8h.md#a23b9ea466101b4367232237ab5a9a42f)

void stm32\_gpio\_intc\_select\_line\_trigger(stm32\_gpio\_irq\_line\_t line, uint32\_t trg)

Select trigger for interrupt on specified GPIO line.

[stm32\_gpio\_intc\_set\_irq\_callback](gpio__intc__stm32_8h.md#a4a750e87f445487c517f24a0266f6a4b)

int stm32\_gpio\_intc\_set\_irq\_callback(stm32\_gpio\_irq\_line\_t line, stm32\_gpio\_irq\_cb\_t cb, void \*user)

Set callback invoked when an interrupt occurs on specified GPIO line.

[stm32\_gpio\_irq\_line\_t](gpio__intc__stm32_8h.md#a52c69f3ce04242217e00981c1315a374)

uint32\_t stm32\_gpio\_irq\_line\_t

GPIO interrupt controller API for STM32 MCUs.

**Definition** gpio\_intc\_stm32.h:24

[stm32\_gpio\_irq\_cb\_t](gpio__intc__stm32_8h.md#a69ad9c575223c813f484423e56200560)

void(\* stm32\_gpio\_irq\_cb\_t)(gpio\_port\_pins\_t pin, void \*user)

GPIO interrupt callback function signature.

**Definition** gpio\_intc\_stm32.h:80

[stm32\_gpio\_irq\_trigger](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61)

stm32\_gpio\_irq\_trigger

GPIO interrupt trigger flags.

**Definition** gpio\_intc\_stm32.h:49

[STM32\_GPIO\_IRQ\_TRIG\_LOW\_LEVEL](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a2a13de1280bfac5e1cb484db56843e2c)

@ STM32\_GPIO\_IRQ\_TRIG\_LOW\_LEVEL

**Definition** gpio\_intc\_stm32.h:61

[STM32\_GPIO\_IRQ\_TRIG\_FALLING](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a2d20b462dad9d074ce7bb1479d3066c9)

@ STM32\_GPIO\_IRQ\_TRIG\_FALLING

**Definition** gpio\_intc\_stm32.h:55

[STM32\_GPIO\_IRQ\_TRIG\_BOTH](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a46af906f79e53b4301c50292840bd301)

@ STM32\_GPIO\_IRQ\_TRIG\_BOTH

**Definition** gpio\_intc\_stm32.h:57

[STM32\_GPIO\_IRQ\_TRIG\_RISING](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a601ac25a6a83f5a01dc8ce8bb8f547ae)

@ STM32\_GPIO\_IRQ\_TRIG\_RISING

**Definition** gpio\_intc\_stm32.h:53

[STM32\_GPIO\_IRQ\_TRIG\_HIGH\_LEVEL](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61a961343f06deca1a4ae9288b81e167048)

@ STM32\_GPIO\_IRQ\_TRIG\_HIGH\_LEVEL

**Definition** gpio\_intc\_stm32.h:59

[STM32\_GPIO\_IRQ\_TRIG\_NONE](gpio__intc__stm32_8h.md#a8f9c3db22937ebe4382215227c410b61adb4cda594aec45886263f14968e6b3d2)

@ STM32\_GPIO\_IRQ\_TRIG\_NONE

**Definition** gpio\_intc\_stm32.h:51

[stm32\_gpio\_intc\_enable\_line](gpio__intc__stm32_8h.md#ad1c9359de9847ebd2670987302c48f8d)

void stm32\_gpio\_intc\_enable\_line(stm32\_gpio\_irq\_line\_t line)

Enable GPIO interrupts for specified line.

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:255

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:234

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gpio\_intc\_stm32.h](gpio__intc__stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
