---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/silabs-pinctrl-dbus_8h_source.html
original_path: doxygen/html/silabs-pinctrl-dbus_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

silabs-pinctrl-dbus.h

[Go to the documentation of this file.](silabs-pinctrl-dbus_8h.md)

1/\*

2 \* Copyright (c) 2024 Silicon Labs

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SILABS\_PINCTRL\_DBUS\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SILABS\_PINCTRL\_DBUS\_H\_

8

9#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

10

11/\*

12 \* Silabs Series 2 DBUS configuration is encoded in a 32-bit bitfield organized as follows:

13 \*

14 \* 31 : Whether the configuration represents an analog pin

15 \* If digital (bit 31 == 0):

16 \* 30 : Reserved

17 \* 29 : Route register presence (fixed routes have no route register)

18 \* 28..24: Route register offset in words from peripheral config (offset of <fun>ROUTE

19 \* register in GPIO\_<periph>ROUTE\_TypeDef)

20 \* 23..19: Enable bit (offset into ROUTEEN register for given function)

21 \* 18 : Enable bit presence (some inputs are auto-enabled)

22 \* 17..8 : Peripheral config offset in words from DBUS base within GPIO (offset of <periph>ROUTE[n]

23 \* register in GPIO\_TypeDef minus offset of first route register [DBGROUTEPEN, 0x440])

24 \* 7..4 : GPIO pin

25 \* 3..0 : GPIO port

26 \* If analog (bit 31 == 1):

27 \* 15..14: Bus selection (A, B, CD)

28 \* 13..12: Bus selection (EVEN0, EVEN1, ODD0, ODD1)

29 \* 11..8 : Peripheral selection (bit in GPIO\_nBUSALLOC bitfield)

30 \* 7 ..0 : Reserved

31 \*/

32

[ 33](silabs-pinctrl-dbus_8h.md#abcb19a19db6aa4c3d5fdfeb91b402742)#define SILABS\_PINCTRL\_GPIO\_PORT\_MASK 0x0000000FUL

[ 34](silabs-pinctrl-dbus_8h.md#a1e87772911ce845375bbbd87f8197cd5)#define SILABS\_PINCTRL\_GPIO\_PIN\_MASK 0x000000F0UL

[ 35](silabs-pinctrl-dbus_8h.md#ab30280b4a9235fa54509c4a0474815eb)#define SILABS\_PINCTRL\_PERIPH\_BASE\_MASK 0x0003FF00UL

[ 36](silabs-pinctrl-dbus_8h.md#a001ac259d04f65ecbcdc148085eabc63)#define SILABS\_PINCTRL\_HAVE\_EN\_MASK 0x00040000UL

[ 37](silabs-pinctrl-dbus_8h.md#a7eab868fae2d52d4d3ce596d0598494b)#define SILABS\_PINCTRL\_EN\_BIT\_MASK 0x00F80000UL

[ 38](silabs-pinctrl-dbus_8h.md#a904daec2c54793fc013e72a394fcdaf1)#define SILABS\_PINCTRL\_ROUTE\_MASK 0x1F000000UL

[ 39](silabs-pinctrl-dbus_8h.md#a71ebb23975e6b133f8b9f0eeb1a97ccc)#define SILABS\_PINCTRL\_HAVE\_ROUTE\_MASK 0x20000000UL

40

[ 41](silabs-pinctrl-dbus_8h.md#ab6546e7d8e43f44316e9205cbbf4958f)#define SILABS\_PINCTRL\_ANALOG\_MASK 0x80000000UL

[ 42](silabs-pinctrl-dbus_8h.md#a9c56c5ddaf62514981c576e8f1740c19)#define SILABS\_PINCTRL\_ABUS\_BUS\_MASK 0x0000C000UL

[ 43](silabs-pinctrl-dbus_8h.md#a76b1bb8aec6c12482b9d11ddcae9c177)#define SILABS\_PINCTRL\_ABUS\_PARITY\_MASK 0x00003000UL

[ 44](silabs-pinctrl-dbus_8h.md#a9d75fc562522d3fb7f54765a1fa57d41)#define SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK 0x00000F00UL

45

[ 46](silabs-pinctrl-dbus_8h.md#a524de9c4274f58e7fac79825203a29b8)#define SILABS\_PINCTRL\_UNUSED 0xFF

[ 47](silabs-pinctrl-dbus_8h.md#afb799e274f9128cdb1ef3d3437b3b8f9)#define SILABS\_PINCTRL\_ANALOG 0xAA

48

[ 49](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)#define SILABS\_DBUS(port, pin, periph\_base, en\_present, en\_bit, route) \

50 (FIELD\_PREP(SILABS\_PINCTRL\_GPIO\_PORT\_MASK, port) | \

51 FIELD\_PREP(SILABS\_PINCTRL\_GPIO\_PIN\_MASK, pin) | \

52 FIELD\_PREP(SILABS\_PINCTRL\_PERIPH\_BASE\_MASK, periph\_base) | \

53 FIELD\_PREP(SILABS\_PINCTRL\_HAVE\_EN\_MASK, en\_present) | \

54 FIELD\_PREP(SILABS\_PINCTRL\_EN\_BIT\_MASK, en\_bit) | \

55 FIELD\_PREP(SILABS\_PINCTRL\_ROUTE\_MASK, route) | \

56 FIELD\_PREP(SILABS\_PINCTRL\_HAVE\_ROUTE\_MASK, 1))

57

[ 58](silabs-pinctrl-dbus_8h.md#a66d91269d40839f864a6af1f0983adb0)#define SILABS\_FIXED\_ROUTE(port, pin, periph\_base, en\_bit) \

59 (FIELD\_PREP(SILABS\_PINCTRL\_GPIO\_PORT\_MASK, port) | \

60 FIELD\_PREP(SILABS\_PINCTRL\_GPIO\_PIN\_MASK, pin) | \

61 FIELD\_PREP(SILABS\_PINCTRL\_PERIPH\_BASE\_MASK, periph\_base) | \

62 FIELD\_PREP(SILABS\_PINCTRL\_HAVE\_EN\_MASK, 1) | \

63 FIELD\_PREP(SILABS\_PINCTRL\_EN\_BIT\_MASK, en\_bit) | \

64 FIELD\_PREP(SILABS\_PINCTRL\_HAVE\_ROUTE\_MASK, 0))

65

[ 66](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)#define SILABS\_ABUS(bus, parity, peripheral) \

67 (FIELD\_PREP(SILABS\_PINCTRL\_ANALOG\_MASK, 1) | \

68 FIELD\_PREP(SILABS\_PINCTRL\_ABUS\_BUS\_MASK, bus) | \

69 FIELD\_PREP(SILABS\_PINCTRL\_ABUS\_PARITY\_MASK, parity) | \

70 FIELD\_PREP(SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK, peripheral))

71

72#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_SILABS\_PINCTRL\_DBUS\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs-pinctrl-dbus.h](silabs-pinctrl-dbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
