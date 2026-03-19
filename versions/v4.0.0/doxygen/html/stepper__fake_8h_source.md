---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stepper__fake_8h_source.html
original_path: doxygen/html/stepper__fake_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_fake.h

[Go to the documentation of this file.](stepper__fake_8h.md)

1/\*

2 \* Copyright (c) 2024 Fabian Blatz <fabianblatz@gmail.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_FAKE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_FAKE\_H\_

9

10#include <[zephyr/drivers/stepper.h](stepper_8h.md)>

11#include <[zephyr/fff.h](fff_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](stepper__fake_8h.md#ab9da41c2f25f2821f2f5f3b931124efa)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_enable, const struct [device](structdevice.md) \*, const bool);

18

[ 19](stepper__fake_8h.md#a8e0a524a7327e63e505489b3e45a19da)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_move, const struct [device](structdevice.md) \*, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

20

[ 21](stepper__fake_8h.md#ac3194cdcf9bf9d919982491b0ef2582e)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_max\_velocity, const struct [device](structdevice.md) \*, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f));

22

[ 23](stepper__fake_8h.md#afb2aaac26841ac828f3ab2502822f08b)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_micro\_step\_res, const struct [device](structdevice.md) \*,

24 const enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30));

25

[ 26](stepper__fake_8h.md#a556a900c38b609db63950d8517ed530d)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_get\_micro\_step\_res, const struct [device](structdevice.md) \*,

27 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*);

28

[ 29](stepper__fake_8h.md#a1a17c9c0c73a4642ef10222cc0b1936c)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_actual\_position, const struct [device](structdevice.md) \*,

30 const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

31

[ 32](stepper__fake_8h.md#ae160ade09367603fe6db15a0ad443406)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_get\_actual\_position, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*);

33

[ 34](stepper__fake_8h.md#a71c280dd79bcea13f73a6d8820272287)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_target\_position, const struct [device](structdevice.md) \*,

35 const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

36

[ 37](stepper__fake_8h.md#a24fccf084c62398ba48009aa24c88a3c)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_is\_moving, const struct [device](structdevice.md) \*, bool \*);

38

[ 39](stepper__fake_8h.md#ae842dcc16678f77fb5a240643c56739d)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_enable\_constant\_velocity\_mode, const struct [device](structdevice.md) \*,

40 const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01), const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f));

41

[ 42](stepper__fake_8h.md#a0de88135395e6bf6536efcfc238c712e)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_event\_callback, const struct [device](structdevice.md) \*,

43 stepper\_event\_callback\_t, void \*);

44

45#ifdef \_\_cplusplus

46}

47#endif

48

49#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_FAKE\_H\_ \*/

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)

stepper\_direction

Stepper Motor direction options.

**Definition** stepper.h:60

[stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)

stepper\_micro\_step\_resolution

Stepper Motor micro step resolution options.

**Definition** stepper.h:36

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[stepper.h](stepper_8h.md)

Public API for Stepper Driver.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_fake.h](stepper__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
