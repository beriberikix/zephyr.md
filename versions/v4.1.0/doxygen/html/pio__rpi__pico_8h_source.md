---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pio__rpi__pico_8h_source.html
original_path: doxygen/html/pio__rpi__pico_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pio\_rpi\_pico.h

[Go to the documentation of this file.](pio__rpi__pico_8h.md)

1/\*

2 \* Copyright (c) 2023 Tokita, Hiroshi <tokita.hiroshi@fujitsu.com>

3 \* Copyright (c) 2023 Yonatan Schachter

4 \* Copyright (c) 2023 Ionut Pavel <iocapa@iocapa.com>

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_DRIVERS\_MISC\_PIO\_PICO\_RPI\_PIO\_PICO\_RPI\_H\_

10#define ZEPHYR\_DRIVERS\_MISC\_PIO\_PICO\_RPI\_PIO\_PICO\_RPI\_H\_

11

12#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h.md)>

13

14#include <hardware/pio.h>

15

[ 25](pio__rpi__pico_8h.md#a744449bb6c1a409a9d8677c66667ea9b)#define RPI\_PICO\_PIO\_DEFINE\_PROGRAM(name, wrap\_target, wrap, ...) \

26 static const uint32\_t name ## \_wrap\_target = wrap\_target; \

27 static const uint32\_t name ## \_wrap = wrap; \

28 static const uint16\_t name ## \_program\_instructions[] = { \

29 \_\_VA\_ARGS\_\_ \

30 }; \

31 static const struct pio\_program name ## \_program = { \

32 .instructions = name ## \_program\_instructions, \

33 .length = ARRAY\_SIZE(name ## \_program\_instructions), \

34 .origin = -1, \

35 }

36

[ 42](pio__rpi__pico_8h.md#a0d74a21471e301563224d4673ca1a738)#define RPI\_PICO\_PIO\_GET\_WRAP\_TARGET(name) name ## \_wrap\_target

43

[ 49](pio__rpi__pico_8h.md#a5cc3f015332a73cba6141e94b8fbe67e)#define RPI\_PICO\_PIO\_GET\_WRAP(name) name ## \_wrap

50

[ 56](pio__rpi__pico_8h.md#a989341427ba2e681aba5c4d702d91927)#define RPI\_PICO\_PIO\_GET\_PROGRAM(name) &name ## \_program

57

[ 103](pio__rpi__pico_8h.md#a482acc1e13f4b6ef96f55a2c9e3b7a07)#define DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME(node\_id, p\_name, p\_idx, g\_name, g\_idx) \

104 RP2\_GET\_PIN\_NUM(DT\_PROP\_BY\_IDX( \

105 DT\_CHILD(DT\_PINCTRL\_BY\_NAME(node\_id, p\_name, p\_idx), g\_name), pinmux, g\_idx))

106

[ 119](pio__rpi__pico_8h.md#aa3620b14a4d34eed3302048d58a86893)#define DT\_INST\_RPI\_PICO\_PIO\_PIN\_BY\_NAME(inst, p\_name, p\_idx, g\_name, g\_idx) \

120 DT\_RPI\_PICO\_PIO\_PIN\_BY\_NAME(DT\_DRV\_INST(inst), p\_name, p\_idx, g\_name, g\_idx)

121

[ 128](pio__rpi__pico_8h.md#ad2aef23ab08361004bba9209f9e612c1)#define DT\_INST\_PIO\_PIN\_BY\_NAME(inst, name) \

129 DT\_PIO\_PIN\_BY\_NAME(DT\_DRV\_INST(inst), name)

130

[ 137](pio__rpi__pico_8h.md#af8e5b65f61711314c4c2a4f6a510209d)PIO [pio\_rpi\_pico\_get\_pio](pio__rpi__pico_8h.md#af8e5b65f61711314c4c2a4f6a510209d)(const struct [device](structdevice.md) \*dev);

138

[ 147](pio__rpi__pico_8h.md#ac3c70836b493b3fd535ea073c1f7d55b)int [pio\_rpi\_pico\_allocate\_sm](pio__rpi__pico_8h.md#ac3c70836b493b3fd535ea073c1f7d55b)(const struct [device](structdevice.md) \*dev, size\_t \*sm);

148

149#endif /\* ZEPHYR\_DRIVERS\_MISC\_PIO\_PICO\_RPI\_PIO\_PICO\_RPI\_H\_ \*/

[gpio.h](devicetree_2gpio_8h.md)

GPIO Devicetree macro public API header file.

[pio\_rpi\_pico\_allocate\_sm](pio__rpi__pico_8h.md#ac3c70836b493b3fd535ea073c1f7d55b)

int pio\_rpi\_pico\_allocate\_sm(const struct device \*dev, size\_t \*sm)

Allocate a state machine.

[pio\_rpi\_pico\_get\_pio](pio__rpi__pico_8h.md#af8e5b65f61711314c4c2a4f6a510209d)

PIO pio\_rpi\_pico\_get\_pio(const struct device \*dev)

Get PIO object.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [pio\_rpi\_pico](dir_226c323191fcba4fde21e80cdf6d98df.md)
- [pio\_rpi\_pico.h](pio__rpi__pico_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
