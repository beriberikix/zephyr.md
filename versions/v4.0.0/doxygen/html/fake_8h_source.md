---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fake_8h_source.html
original_path: doxygen/html/fake_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake.h

[Go to the documentation of this file.](fake_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_DRIVERS\_REGULATOR\_FAKE\_H\_

7#define ZEPHYR\_DRIVERS\_REGULATOR\_FAKE\_H\_

8

9#include <[zephyr/drivers/regulator.h](regulator_8h.md)>

10#include <[zephyr/fff.h](fff_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](fake_8h.md#a3973590380354a70707b61ada39abad6)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_enable, const struct [device](structdevice.md) \*);

[ 17](fake_8h.md#a609a165577a85410823a484352539ff6)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_disable, const struct [device](structdevice.md) \*);

[ 18](fake_8h.md#a1af81b030ae56448e418477127fbaeed)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(unsigned int, regulator\_fake\_count\_voltages,

19 const struct [device](structdevice.md) \*);

[ 20](fake_8h.md#ac3162ce9e5e63a2295069b2240cf0b71)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_list\_voltage, const struct [device](structdevice.md) \*,

21 unsigned int, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*);

[ 22](fake_8h.md#ad6b608cb8edd5a2039768d861b5a6717)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_set\_voltage, const struct [device](structdevice.md) \*,

23 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

[ 24](fake_8h.md#aa73c81a5d0935ef64319368eef4296a2)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_get\_voltage, const struct [device](structdevice.md) \*,

25 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*);

[ 26](fake_8h.md#a626edd60fb2e168ab5dfba443b4b8e79)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_set\_current\_limit,

27 const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2));

[ 28](fake_8h.md#a3266aa339ac0a61582534614832ed25f)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_get\_current\_limit,

29 const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*);

[ 30](fake_8h.md#aebac179a540a7dc8d049c54f86b04e6a)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_set\_mode, const struct [device](structdevice.md) \*,

31 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03));

[ 32](fake_8h.md#a4c48cea36164e758dc076714d405f9b0)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_get\_mode, const struct [device](structdevice.md) \*,

33 [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*);

[ 34](fake_8h.md#a67471c8a19ca69bd9d89b44918508a13)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_set\_active\_discharge, const struct [device](structdevice.md) \*,

35 bool);

[ 36](fake_8h.md#a3aef8e170371f8fd79f4451abbebe425)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_get\_active\_discharge, const struct [device](structdevice.md) \*,

37 bool \*);

[ 38](fake_8h.md#add0090864c178637d91938dd52f174d0)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_fake\_get\_error\_flags,

39 const struct [device](structdevice.md) \*, [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*);

40

[ 41](fake_8h.md#a4b0de95ee88a7d3dd01aff3185858a78)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_parent\_fake\_dvs\_state\_set,

42 const struct [device](structdevice.md) \*, [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd));

[ 43](fake_8h.md#a072d24303627a05781afad26742bc0b7)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, regulator\_parent\_fake\_ship\_mode,

44 const struct [device](structdevice.md) \*);

45

46#ifdef \_\_cplusplus

47}

48#endif

49

50#endif /\* ZEPHYR\_TESTS\_DRIVERS\_CAN\_SHELL\_FAKE\_CAN\_H\_ \*/

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03)

uint8\_t regulator\_mode\_t

Opaque type to store regulator modes.

**Definition** regulator.h:40

[regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90)

uint8\_t regulator\_error\_flags\_t

Opaque bit map for regulator error flags (see REGULATOR\_ERRORS).

**Definition** regulator.h:43

[regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd)

uint8\_t regulator\_dvs\_state\_t

Opaque type to store regulator DVS states.

**Definition** regulator.h:37

[regulator.h](regulator_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [regulator](dir_6524682a4461fdfb702081281f42371c.md)
- [fake.h](fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
