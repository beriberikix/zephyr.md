---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/can__fake_8h_source.html
original_path: doxygen/html/can__fake_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_fake.h

[Go to the documentation of this file.](can__fake_8h.md)

1/\*

2 \* Copyright (c) 2022 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_FAKE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_FAKE\_H\_

9

10#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

11#include <[zephyr/fff.h](fff_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](structfake__can__start__Fake.md#a074da35cf170f2c4c4e85c79d23bca68)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_start](can__fake_8h.md#a5e914edb27ac71877770d2eda4d12168), const struct [device](structdevice.md) \*);

18

[ 19](structfake__can__stop__Fake.md#a8ed74f448aeee4b7c9527b6352184587)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_stop](can__fake_8h.md#ac6e6dbfe92179f3bc3d8af87adb86b92), const struct [device](structdevice.md) \*);

20

[ 21](structfake__can__set__timing__Fake.md#a688e98a0b933b87bc6294636e509252c)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_set\_timing](can__fake_8h.md#a1fb34fd3c818455f5229f40b5ae12b2d), const struct [device](structdevice.md) \*, const struct [can\_timing](structcan__timing.md) \*);

22

23[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_set\_timing\_data](can__fake_8h.md#a6c76206203aa4576156c64b1db1bfcd2), const struct [device](structdevice.md) \*,

[ 24](structfake__can__set__timing__data__Fake.md#a34f4146ceabf0e70469bf7bde574e95a) const struct [can\_timing](structcan__timing.md) \*);

25

[ 26](structfake__can__get__capabilities__Fake.md#a6b17d900a403bc6f9b937a334deda02a)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_get\_capabilities](can__fake_8h.md#ab2dc51fd7ba6044d25fc7a2711af790a), const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*);

27

[ 28](structfake__can__set__mode__Fake.md#a4c6b9383a5b18f4910daac77b0b551f4)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_set\_mode](can__fake_8h.md#a8173a9fd5b1b1cf27269957694def2c6), const struct [device](structdevice.md) \*, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7));

29

30[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_send](can__fake_8h.md#a7afc5d8f3fc1a07024c861b05c0b4e0a), const struct [device](structdevice.md) \*, const struct [can\_frame](structcan__frame.md) \*,

[ 31](structfake__can__send__Fake.md#a3537b8b901274f1bbdb508e52a180f95) [k\_timeout\_t](structk__timeout__t.md), [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca), void \*);

32

33[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_add\_rx\_filter](can__fake_8h.md#a4f71e88bf6db1c701e98d40730e164c8), const struct [device](structdevice.md) \*, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f),

[ 34](structfake__can__add__rx__filter__Fake.md#a53ee3dde1b6ced22e58602d893f3d2f9) void \*, const struct [can\_filter](structcan__filter.md) \*);

35

[ 36](structfake__can__remove__rx__filter__Fake.md#a56275f173f6ae79a2baa2b5fd6f53335)[DECLARE\_FAKE\_VOID\_FUNC](fff_8h.md#ab3a6abd531c44d2ec1d249e3e100ff3c)([fake\_can\_remove\_rx\_filter](can__fake_8h.md#a8731abdacd8354e7a4772289bfda130f), const struct [device](structdevice.md) \*, int);

37

[ 38](structfake__can__recover__Fake.md#a3833492b2003d3936ba0bc1d1d39c50d)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_recover](can__fake_8h.md#a5894e3d832e853a26df7b612b00e651e), const struct [device](structdevice.md) \*, [k\_timeout\_t](structk__timeout__t.md));

39

40[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_get\_state](can__fake_8h.md#a864f1e7500cf69387822e0dad8f8eb78), const struct [device](structdevice.md) \*, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*,

[ 41](structfake__can__get__state__Fake.md#a5c405d3ba0cd766e745103a6e8065239) struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*);

42

43[DECLARE\_FAKE\_VOID\_FUNC](fff_8h.md#ab3a6abd531c44d2ec1d249e3e100ff3c)([fake\_can\_set\_state\_change\_callback](can__fake_8h.md#ae3c1524cc1dcd6de77cc347392ab05dc), const struct [device](structdevice.md) \*,

[ 44](structfake__can__set__state__change__callback__Fake.md#ab38acb1d5b28cdbdb091354f0831adb1) [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d), void \*);

45

[ 46](structfake__can__get__max__filters__Fake.md#aeafbc134795c08a0da417352a78f32d7)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_get\_max\_filters](can__fake_8h.md#ad4f291d6297e4ebd336b199bb9836930), const struct [device](structdevice.md) \*, bool);

47

[ 48](structfake__can__get__core__clock__Fake.md#a977411871f80bf3660c56ca95aafec4f)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int, [fake\_can\_get\_core\_clock](can__fake_8h.md#adaaefe390feebf9b84ed5479a86172d7), const struct [device](structdevice.md) \*, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*);

49

50#ifdef \_\_cplusplus

51}

52#endif

53

54#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_FAKE\_H\_ \*/

[fake\_can\_set\_timing](can__fake_8h.md#a1fb34fd3c818455f5229f40b5ae12b2d)

int fake\_can\_set\_timing(const struct device \*arg0, const struct can\_timing \*arg1)

[fake\_can\_add\_rx\_filter](can__fake_8h.md#a4f71e88bf6db1c701e98d40730e164c8)

int fake\_can\_add\_rx\_filter(const struct device \*arg0, can\_rx\_callback\_t arg1, void \*arg2, const struct can\_filter \*arg3)

[fake\_can\_recover](can__fake_8h.md#a5894e3d832e853a26df7b612b00e651e)

int fake\_can\_recover(const struct device \*arg0, k\_timeout\_t arg1)

[fake\_can\_start](can__fake_8h.md#a5e914edb27ac71877770d2eda4d12168)

int fake\_can\_start(const struct device \*arg0)

[fake\_can\_set\_timing\_data](can__fake_8h.md#a6c76206203aa4576156c64b1db1bfcd2)

int fake\_can\_set\_timing\_data(const struct device \*arg0, const struct can\_timing \*arg1)

[fake\_can\_send](can__fake_8h.md#a7afc5d8f3fc1a07024c861b05c0b4e0a)

int fake\_can\_send(const struct device \*arg0, const struct can\_frame \*arg1, k\_timeout\_t arg2, can\_tx\_callback\_t arg3, void \*arg4)

[fake\_can\_set\_mode](can__fake_8h.md#a8173a9fd5b1b1cf27269957694def2c6)

int fake\_can\_set\_mode(const struct device \*arg0, can\_mode\_t arg1)

[fake\_can\_get\_state](can__fake_8h.md#a864f1e7500cf69387822e0dad8f8eb78)

int fake\_can\_get\_state(const struct device \*arg0, enum can\_state \*arg1, struct can\_bus\_err\_cnt \*arg2)

[fake\_can\_remove\_rx\_filter](can__fake_8h.md#a8731abdacd8354e7a4772289bfda130f)

void fake\_can\_remove\_rx\_filter(const struct device \*arg0, int arg1)

[fake\_can\_get\_capabilities](can__fake_8h.md#ab2dc51fd7ba6044d25fc7a2711af790a)

int fake\_can\_get\_capabilities(const struct device \*arg0, can\_mode\_t \*arg1)

[fake\_can\_stop](can__fake_8h.md#ac6e6dbfe92179f3bc3d8af87adb86b92)

int fake\_can\_stop(const struct device \*arg0)

[fake\_can\_get\_max\_filters](can__fake_8h.md#ad4f291d6297e4ebd336b199bb9836930)

int fake\_can\_get\_max\_filters(const struct device \*arg0, bool arg1)

[fake\_can\_get\_core\_clock](can__fake_8h.md#adaaefe390feebf9b84ed5479a86172d7)

int fake\_can\_get\_core\_clock(const struct device \*arg0, uint32\_t \*arg1)

[fake\_can\_set\_state\_change\_callback](can__fake_8h.md#ae3c1524cc1dcd6de77cc347392ab05dc)

void fake\_can\_set\_state\_change\_callback(const struct device \*arg0, can\_state\_change\_callback\_t arg1, void \*arg2)

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VOID\_FUNC](fff_8h.md#ab3a6abd531c44d2ec1d249e3e100ff3c)

#define DECLARE\_FAKE\_VOID\_FUNC(...)

**Definition** fff.h:8691

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)

void(\* can\_state\_change\_callback\_t)(const struct device \*dev, enum can\_state state, struct can\_bus\_err\_cnt err\_cnt, void \*user\_data)

Defines the state change callback handler function signature.

**Definition** can.h:312

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:125

[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)

void(\* can\_rx\_callback\_t)(const struct device \*dev, struct can\_frame \*frame, void \*user\_data)

Defines the application callback handler function signature for receiving.

**Definition** can.h:301

[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)

void(\* can\_tx\_callback\_t)(const struct device \*dev, int error, void \*user\_data)

Defines the application callback handler function signature.

**Definition** can.h:292

[can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)

can\_state

Defines the state of the CAN controller.

**Definition** can.h:130

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[can\_bus\_err\_cnt](structcan__bus__err__cnt.md)

CAN controller error counters.

**Definition** can.h:232

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:218

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:172

[can\_timing](structcan__timing.md)

CAN bus timing structure.

**Definition** can.h:271

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [can\_fake.h](can__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
