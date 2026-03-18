---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/exti__stm32_8h_source.html
original_path: doxygen/html/exti__stm32_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

exti\_stm32.h

[Go to the documentation of this file.](exti__stm32_8h.md)

1/\*

2 \* Copyright (c) 2016 Open-RnD Sp. z o.o.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

20

21#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EXTI\_STM32\_H\_

22#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EXTI\_STM32\_H\_

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25

[ 26](exti__stm32_8h.md#ac77d469d5ec2ea32fb52b89f062fece5)#define STM32\_EXTI\_LINE\_NONE 0xFFFFFFFFU

27

[ 33](exti__stm32_8h.md#af40d4b71f65e3fc1b6bd3f353e58eaae)void [stm32\_exti\_enable](exti__stm32_8h.md#af40d4b71f65e3fc1b6bd3f353e58eaae)(int line);

34

[ 40](exti__stm32_8h.md#a77ed08c11acc54d4d00544b862383ec2)void [stm32\_exti\_disable](exti__stm32_8h.md#a77ed08c11acc54d4d00544b862383ec2)(int line);

41

[ 45](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7)enum [stm32\_exti\_trigger](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7) {

46 /\* clear trigger \*/

[ 47](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7aa44b00e6dd732140f0c152ec6a5ad0e0) [STM32\_EXTI\_TRIG\_NONE](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7aa44b00e6dd732140f0c152ec6a5ad0e0) = 0x0,

48 /\* trigger on rising edge \*/

[ 49](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7ac1ab9fda0db1fb1a852bfe358c7e6485) [STM32\_EXTI\_TRIG\_RISING](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7ac1ab9fda0db1fb1a852bfe358c7e6485) = 0x1,

50 /\* trigger on falling edge \*/

[ 51](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7a8a53325045c0825c5fd379d83a04f5e4) [STM32\_EXTI\_TRIG\_FALLING](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7a8a53325045c0825c5fd379d83a04f5e4) = 0x2,

52 /\* trigger on both rising & falling edge \*/

[ 53](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7a013afe4b3bfc4921f30dad835e7f87cc) [STM32\_EXTI\_TRIG\_BOTH](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7a013afe4b3bfc4921f30dad835e7f87cc) = 0x3,

54};

55

[ 62](exti__stm32_8h.md#aefb5e5f4a048cc233df749df9e45ac8a)void [stm32\_exti\_trigger](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7)(int line, int trg);

63

64/\* callback for exti interrupt \*/

[ 65](exti__stm32_8h.md#a7ee31db62548a8e6977ede220fc3fce9)typedef void (\*[stm32\_exti\_callback\_t](exti__stm32_8h.md#a7ee31db62548a8e6977ede220fc3fce9)) (int line, void \*user);

66

[ 74](exti__stm32_8h.md#ac9f5b3e69ef25b3f0855f9bad22c826a)int [stm32\_exti\_set\_callback](exti__stm32_8h.md#ac9f5b3e69ef25b3f0855f9bad22c826a)(int line, [stm32\_exti\_callback\_t](exti__stm32_8h.md#a7ee31db62548a8e6977ede220fc3fce9) cb, void \*data);

75

[ 81](exti__stm32_8h.md#a1cf8d3d58087960e3f570369172e3015)void [stm32\_exti\_unset\_callback](exti__stm32_8h.md#a1cf8d3d58087960e3f570369172e3015)(int line);

82

83#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EXTI\_STM32\_H\_ \*/

[stm32\_exti\_unset\_callback](exti__stm32_8h.md#a1cf8d3d58087960e3f570369172e3015)

void stm32\_exti\_unset\_callback(int line)

unset EXTI interrupt callback

[stm32\_exti\_trigger](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7)

stm32\_exti\_trigger

EXTI trigger flags.

**Definition** exti\_stm32.h:45

[STM32\_EXTI\_TRIG\_BOTH](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7a013afe4b3bfc4921f30dad835e7f87cc)

@ STM32\_EXTI\_TRIG\_BOTH

**Definition** exti\_stm32.h:53

[STM32\_EXTI\_TRIG\_FALLING](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7a8a53325045c0825c5fd379d83a04f5e4)

@ STM32\_EXTI\_TRIG\_FALLING

**Definition** exti\_stm32.h:51

[STM32\_EXTI\_TRIG\_NONE](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7aa44b00e6dd732140f0c152ec6a5ad0e0)

@ STM32\_EXTI\_TRIG\_NONE

**Definition** exti\_stm32.h:47

[STM32\_EXTI\_TRIG\_RISING](exti__stm32_8h.md#a2caf7f256985537368b079f565adb9e7ac1ab9fda0db1fb1a852bfe358c7e6485)

@ STM32\_EXTI\_TRIG\_RISING

**Definition** exti\_stm32.h:49

[stm32\_exti\_disable](exti__stm32_8h.md#a77ed08c11acc54d4d00544b862383ec2)

void stm32\_exti\_disable(int line)

disable EXTI interrupt for specific line

[stm32\_exti\_callback\_t](exti__stm32_8h.md#a7ee31db62548a8e6977ede220fc3fce9)

void(\* stm32\_exti\_callback\_t)(int line, void \*user)

**Definition** exti\_stm32.h:65

[stm32\_exti\_set\_callback](exti__stm32_8h.md#ac9f5b3e69ef25b3f0855f9bad22c826a)

int stm32\_exti\_set\_callback(int line, stm32\_exti\_callback\_t cb, void \*data)

set EXTI interrupt callback

[stm32\_exti\_enable](exti__stm32_8h.md#af40d4b71f65e3fc1b6bd3f353e58eaae)

void stm32\_exti\_enable(int line)

enable EXTI interrupt for specific line

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [exti\_stm32.h](exti__stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
