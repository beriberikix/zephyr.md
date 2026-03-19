---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stepper__fake_8h_source.html
original_path: doxygen/html/stepper__fake_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 17](stepper__fake_8h.md#ae9527dafbb37dd0207aec5241b4a8fb2)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_enable, const struct [device](structdevice.md) \*, bool);

18

[ 19](stepper__fake_8h.md#afe6a5486c1b72f821601e1f430cef0c5)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_move\_by, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

20

[ 21](stepper__fake_8h.md#a36764a70e9b74e26ed701c9772dd7e14)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_microstep\_interval, const struct [device](structdevice.md) \*, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1));

22

[ 23](stepper__fake_8h.md#afbd42aab8c3e0d8e294fb7fdb685ba2e)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_micro\_step\_res, const struct [device](structdevice.md) \*,

24 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30));

25

[ 26](stepper__fake_8h.md#a556a900c38b609db63950d8517ed530d)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_get\_micro\_step\_res, const struct [device](structdevice.md) \*,

27 enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*);

28

[ 29](stepper__fake_8h.md#a848d1840a0b41d4c8e53e7ced3103b74)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_reference\_position, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

30

[ 31](stepper__fake_8h.md#ae160ade09367603fe6db15a0ad443406)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_get\_actual\_position, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*);

32

[ 33](stepper__fake_8h.md#accb03188680de98f807ff5cc8b58738d)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_move\_to, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

34

[ 35](stepper__fake_8h.md#a24fccf084c62398ba48009aa24c88a3c)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_is\_moving, const struct [device](structdevice.md) \*, bool \*);

36

[ 37](stepper__fake_8h.md#ab4259f57f69e26ffac35fe3eeb5c273d)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_run, const struct [device](structdevice.md) \*, enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01));

38

[ 39](stepper__fake_8h.md#a0de88135395e6bf6536efcfc238c712e)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, fake\_stepper\_set\_event\_callback, const struct [device](structdevice.md) \*,

40 stepper\_event\_callback\_t, void \*);

41

42#ifdef \_\_cplusplus

43}

44#endif

45

46#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_STEPPER\_STEPPER\_FAKE\_H\_ \*/

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)

stepper\_direction

Stepper Motor direction options.

**Definition** stepper.h:65

[stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)

stepper\_micro\_step\_resolution

Stepper Motor micro-step resolution options.

**Definition** stepper.h:41

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[stepper.h](stepper_8h.md)

Public API for Stepper Driver.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_fake.h](stepper__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
