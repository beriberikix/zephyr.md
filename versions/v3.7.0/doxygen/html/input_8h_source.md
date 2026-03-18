---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/input_8h_source.html
original_path: doxygen/html/input_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input.h

[Go to the documentation of this file.](input_8h.md)

1/\*

2 \* Copyright 2023 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_INPUT\_H\_

8#define ZEPHYR\_INCLUDE\_INPUT\_H\_

9

18

19#include <[stdint.h](stdint_8h.md)>

20#include <[zephyr/device.h](device_8h.md)>

21#include <[zephyr/dt-bindings/input/input-event-codes.h](input-event-codes_8h.md)>

22#include <[zephyr/kernel.h](kernel_8h.md)>

23#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 36](structinput__event.md)struct [input\_event](structinput__event.md) {

[ 38](structinput__event.md#a4022d0ddf8ca5be9b478cd0b2758d067) const struct [device](structdevice.md) \*[dev](structinput__event.md#a4022d0ddf8ca5be9b478cd0b2758d067);

[ 40](structinput__event.md#a015732c5d67a5374b93e980282a2a9d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sync](structinput__event.md#a015732c5d67a5374b93e980282a2a9d7);

[ 42](structinput__event.md#af74a1741fef30ee375d4a71628a9656e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structinput__event.md#af74a1741fef30ee375d4a71628a9656e);

[ 47](structinput__event.md#a5abe903fbf3b29643578be85c17ba6aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [code](structinput__event.md#a5abe903fbf3b29643578be85c17ba6aa);

[ 49](structinput__event.md#af18b63e5263e73fce8e38838e37d2bae) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [value](structinput__event.md#af18b63e5263e73fce8e38838e37d2bae);

50};

51

[ 70](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)int [input\_report](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)(const struct [device](structdevice.md) \*dev,

71 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, bool sync,

72 [k\_timeout\_t](structk__timeout__t.md) timeout);

73

[ 80](group__input__interface.md#gaeb9fa2d4bb990e67ab0a2bd20a141d20)static inline int [input\_report\_key](group__input__interface.md#gaeb9fa2d4bb990e67ab0a2bd20a141d20)(const struct [device](structdevice.md) \*dev,

81 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, bool sync,

82 [k\_timeout\_t](structk__timeout__t.md) timeout)

83{

84 return [input\_report](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)(dev, [INPUT\_EV\_KEY](group__input__events.md#ga4a517c31bdbdd1bd82ba456d256ef1f1), code, !!value, sync, timeout);

85}

86

[ 92](group__input__interface.md#gaffbf85b82d0cede81410dda8ed559201)static inline int [input\_report\_rel](group__input__interface.md#gaffbf85b82d0cede81410dda8ed559201)(const struct [device](structdevice.md) \*dev,

93 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, bool sync,

94 [k\_timeout\_t](structk__timeout__t.md) timeout)

95{

96 return [input\_report](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)(dev, [INPUT\_EV\_REL](group__input__events.md#ga02de6c85efab3d21eb81e88e54d58e03), code, value, sync, timeout);

97}

98

[ 104](group__input__interface.md#gaf94bdc8ca673de7947e011872f64ce6c)static inline int [input\_report\_abs](group__input__interface.md#gaf94bdc8ca673de7947e011872f64ce6c)(const struct [device](structdevice.md) \*dev,

105 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, bool sync,

106 [k\_timeout\_t](structk__timeout__t.md) timeout)

107{

108 return [input\_report](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)(dev, [INPUT\_EV\_ABS](group__input__events.md#gaa6bcd6755fbdb3eb103f03a72759ce4f), code, value, sync, timeout);

109}

110

[ 118](group__input__interface.md#ga401a03bb89dd59d518f7466a035571da)bool [input\_queue\_empty](group__input__interface.md#ga401a03bb89dd59d518f7466a035571da)(void);

119

[ 123](structinput__callback.md)struct [input\_callback](structinput__callback.md) {

[ 125](structinput__callback.md#afe8fa2362e5c2ad35a00e05f33498a20) const struct [device](structdevice.md) \*[dev](structinput__callback.md#afe8fa2362e5c2ad35a00e05f33498a20);

[ 127](structinput__callback.md#ace43e97a826282e97227980adfec52f9) void (\*[callback](structinput__callback.md#ace43e97a826282e97227980adfec52f9))(struct [input\_event](structinput__event.md) \*evt);

128};

129

[ 140](group__input__interface.md#gacd0045487023fe9652cbfe46f3b556b6)#define INPUT\_CALLBACK\_DEFINE(\_dev, \_callback) \

141 static const STRUCT\_SECTION\_ITERABLE(input\_callback, \

142 \_input\_callback\_\_##\_callback) = { \

143 .dev = \_dev, \

144 .callback = \_callback, \

145 }

146

147#ifdef \_\_cplusplus

148}

149#endif

150

152

153#endif /\* ZEPHYR\_INCLUDE\_INPUT\_H\_ \*/

[device.h](device_8h.md)

[INPUT\_EV\_REL](group__input__events.md#ga02de6c85efab3d21eb81e88e54d58e03)

#define INPUT\_EV\_REL

Relative coordinate event.

**Definition** input-event-codes.h:26

[INPUT\_EV\_KEY](group__input__events.md#ga4a517c31bdbdd1bd82ba456d256ef1f1)

#define INPUT\_EV\_KEY

Key event.

**Definition** input-event-codes.h:25

[INPUT\_EV\_ABS](group__input__events.md#gaa6bcd6755fbdb3eb103f03a72759ce4f)

#define INPUT\_EV\_ABS

Absolute coordinate event.

**Definition** input-event-codes.h:27

[input\_queue\_empty](group__input__interface.md#ga401a03bb89dd59d518f7466a035571da)

bool input\_queue\_empty(void)

Returns true if the input queue is empty.

[input\_report\_key](group__input__interface.md#gaeb9fa2d4bb990e67ab0a2bd20a141d20)

static int input\_report\_key(const struct device \*dev, uint16\_t code, int32\_t value, bool sync, k\_timeout\_t timeout)

Report a new INPUT\_EV\_KEY input event, note that value is converted to either 0 or 1.

**Definition** input.h:80

[input\_report\_abs](group__input__interface.md#gaf94bdc8ca673de7947e011872f64ce6c)

static int input\_report\_abs(const struct device \*dev, uint16\_t code, int32\_t value, bool sync, k\_timeout\_t timeout)

Report a new INPUT\_EV\_ABS input event.

**Definition** input.h:104

[input\_report](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)

int input\_report(const struct device \*dev, uint8\_t type, uint16\_t code, int32\_t value, bool sync, k\_timeout\_t timeout)

Report a new input event.

[input\_report\_rel](group__input__interface.md#gaffbf85b82d0cede81410dda8ed559201)

static int input\_report\_rel(const struct device \*dev, uint16\_t code, int32\_t value, bool sync, k\_timeout\_t timeout)

Report a new INPUT\_EV\_REL input event.

**Definition** input.h:92

[input-event-codes.h](input-event-codes_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[input\_callback](structinput__callback.md)

Input callback structure.

**Definition** input.h:123

[input\_callback::callback](structinput__callback.md#ace43e97a826282e97227980adfec52f9)

void(\* callback)(struct input\_event \*evt)

The callback function.

**Definition** input.h:127

[input\_callback::dev](structinput__callback.md#afe8fa2362e5c2ad35a00e05f33498a20)

const struct device \* dev

device pointer or NULL.

**Definition** input.h:125

[input\_event](structinput__event.md)

Input event structure.

**Definition** input.h:36

[input\_event::sync](structinput__event.md#a015732c5d67a5374b93e980282a2a9d7)

uint8\_t sync

Sync flag.

**Definition** input.h:40

[input\_event::dev](structinput__event.md#a4022d0ddf8ca5be9b478cd0b2758d067)

const struct device \* dev

Device generating the event or NULL.

**Definition** input.h:38

[input\_event::code](structinput__event.md#a5abe903fbf3b29643578be85c17ba6aa)

uint16\_t code

Event code (see INPUT\_KEY\_CODES, INPUT\_BTN\_CODES, INPUT\_ABS\_CODES, INPUT\_REL\_CODES,...

**Definition** input.h:47

[input\_event::value](structinput__event.md#af18b63e5263e73fce8e38838e37d2bae)

int32\_t value

Event value.

**Definition** input.h:49

[input\_event::type](structinput__event.md#af74a1741fef30ee375d4a71628a9656e)

uint8\_t type

Event type (see INPUT\_EV\_CODES).

**Definition** input.h:42

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input.h](input_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
