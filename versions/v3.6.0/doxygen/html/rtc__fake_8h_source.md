---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtc__fake_8h_source.html
original_path: doxygen/html/rtc__fake_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtc\_fake.h

[Go to the documentation of this file.](rtc__fake_8h.md)

1/\*

2 \* Copyright (c) 2023 Prevas A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_RTC\_FAKE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_RTC\_FAKE\_H\_

9

10#include <[zephyr/drivers/rtc.h](rtc_8h.md)>

11#include <[zephyr/fff.h](fff_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](rtc__fake_8h.md#a047bae488fc3076166b0adbd440cf9cf)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_set\_time, const struct [device](structdevice.md) \*, const struct [rtc\_time](structrtc__time.md) \*);

[ 18](rtc__fake_8h.md#a27437477d21568ba0129e87ef9353c69)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_get\_time, const struct [device](structdevice.md) \*, struct [rtc\_time](structrtc__time.md) \*);

19

20#ifdef CONFIG\_RTC\_ALARM

21[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_alarm\_get\_supported\_fields, const struct [device](structdevice.md) \*, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e),

22 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e));

23[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_alarm\_set\_time, const struct [device](structdevice.md) \*, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e),

24 constr struct [rtc\_time](structrtc__time.md) \*);

25[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_alarm\_get\_time, const struct [device](structdevice.md) \*, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e),

26 struct [rtc\_time](structrtc__time.md) \*);

27[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_alarm\_is\_pending, const struct [device](structdevice.md) \*, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e));

28[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_alarm\_set\_callback, const struct [device](structdevice.md) \*[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e),

29 [rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d), void \*);

30#endif /\* CONFIG\_RTC\_ALARM \*/

31

32#ifdef CONFIG\_RTC\_UPDATE

33[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_update\_set\_callback, const struct [device](structdevice.md) \*[rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d),

34 void \*);

35#endif /\* CONFIG\_RTC\_UPDATE \*/

36

37#ifdef CONFIG\_RTC\_CALIBRATION

38[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_set\_calibration, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

39[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, rtc\_fake\_get\_calibration, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*);

40#endif /\* CONFIG\_RTC\_CALIBRATION \*/

41

42#ifdef \_\_cplusplus

43}

44#endif

45

46#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RTC\_RTC\_FAKE\_H\_ \*/

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[rtc\_alarm\_callback](group__rtc__interface.md#ga8fc3b6037a95e97b686875beff9a581d)

void(\* rtc\_alarm\_callback)(const struct device \*dev, uint16\_t id, void \*user\_data)

RTC alarm triggered callback.

**Definition** rtc.h:89

[rtc.h](rtc_8h.md)

Public real time clock driver API.

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[rtc\_time](structrtc__time.md)

Structure for storing date and time values with sub-second precision.

**Definition** rtc.h:59

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [rtc\_fake.h](rtc__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
