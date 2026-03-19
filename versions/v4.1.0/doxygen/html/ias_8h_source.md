---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ias_8h_source.html
original_path: doxygen/html/ias_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ias.h

[Go to the documentation of this file.](ias_8h.md)

1/\*

2 \* Copyright (c) 2022 Codecoup

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_IAS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_IAS\_H\_

9

19

20#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

21#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 27](group__bt__ias.md#gabdaf2045e939bc71c060ee195494c9f0)enum [bt\_ias\_alert\_lvl](group__bt__ias.md#gabdaf2045e939bc71c060ee195494c9f0) {

[ 29](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997) [BT\_IAS\_ALERT\_LVL\_NO\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997),

30

[ 32](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd) [BT\_IAS\_ALERT\_LVL\_MILD\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd),

33

[ 35](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653) [BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653),

36};

37

[ 39](structbt__ias__cb.md)struct [bt\_ias\_cb](structbt__ias__cb.md) {

[ 45](structbt__ias__cb.md#ae0719b1f44f094ff0bbd3abea2bfdf15) void (\*[no\_alert](structbt__ias__cb.md#ae0719b1f44f094ff0bbd3abea2bfdf15))(void);

46

[ 52](structbt__ias__cb.md#aeffe89f9e5a9b87efbdd0af471de980d) void (\*[mild\_alert](structbt__ias__cb.md#aeffe89f9e5a9b87efbdd0af471de980d))(void);

53

[ 59](structbt__ias__cb.md#ad2974bbd16e8d4425370a57f62601af5) void (\*[high\_alert](structbt__ias__cb.md#ad2974bbd16e8d4425370a57f62601af5))(void);

60};

61

[ 66](group__bt__ias.md#gad810c9d74701dc48c12e4545bded95a4)int [bt\_ias\_local\_alert\_stop](group__bt__ias.md#gad810c9d74701dc48c12e4545bded95a4)(void);

67

[ 73](group__bt__ias.md#ga5dee0ec206e8ddbb9bc33c8df824fcb0)#define BT\_IAS\_CB\_DEFINE(\_name) \

74 static const STRUCT\_SECTION\_ITERABLE(bt\_ias\_cb, \_CONCAT(bt\_ias\_cb\_, \_name))

75

[ 76](structbt__ias__client__cb.md)struct [bt\_ias\_client\_cb](structbt__ias__client__cb.md) {

[ 84](structbt__ias__client__cb.md#a325ad34a67f9d9948740eb87862945b7) void (\*[discover](structbt__ias__client__cb.md#a325ad34a67f9d9948740eb87862945b7))(struct bt\_conn \*conn, int err);

85};

86

[ 94](group__bt__ias.md#ga040ef37207ddca54edb9839c721ca2f2)int [bt\_ias\_client\_alert\_write](group__bt__ias.md#ga040ef37207ddca54edb9839c721ca2f2)(struct bt\_conn \*conn, enum [bt\_ias\_alert\_lvl](group__bt__ias.md#gabdaf2045e939bc71c060ee195494c9f0));

95

[ 102](group__bt__ias.md#ga2628386523390e044e4a32fb2cf3e7b5)int [bt\_ias\_discover](group__bt__ias.md#ga2628386523390e044e4a32fb2cf3e7b5)(struct bt\_conn \*conn);

103

[ 110](group__bt__ias.md#ga481a20cbe9b3f128f8737f75535d2bfe)int [bt\_ias\_client\_cb\_register](group__bt__ias.md#ga481a20cbe9b3f128f8737f75535d2bfe)(const struct [bt\_ias\_client\_cb](structbt__ias__client__cb.md) \*cb);

111

112#ifdef \_\_cplusplus

113}

114#endif

115

119

120#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_IAS\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_ias\_client\_alert\_write](group__bt__ias.md#ga040ef37207ddca54edb9839c721ca2f2)

int bt\_ias\_client\_alert\_write(struct bt\_conn \*conn, enum bt\_ias\_alert\_lvl)

Set alert level.

[bt\_ias\_discover](group__bt__ias.md#ga2628386523390e044e4a32fb2cf3e7b5)

int bt\_ias\_discover(struct bt\_conn \*conn)

Discover Immediate Alert Service.

[bt\_ias\_client\_cb\_register](group__bt__ias.md#ga481a20cbe9b3f128f8737f75535d2bfe)

int bt\_ias\_client\_cb\_register(const struct bt\_ias\_client\_cb \*cb)

Register Immediate Alert Client callbacks.

[bt\_ias\_alert\_lvl](group__bt__ias.md#gabdaf2045e939bc71c060ee195494c9f0)

bt\_ias\_alert\_lvl

**Definition** ias.h:27

[bt\_ias\_local\_alert\_stop](group__bt__ias.md#gad810c9d74701dc48c12e4545bded95a4)

int bt\_ias\_local\_alert\_stop(void)

Method for stopping alert locally.

[BT\_IAS\_ALERT\_LVL\_MILD\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a6e141a98473fb7106e3a8c4957a234dd)

@ BT\_IAS\_ALERT\_LVL\_MILD\_ALERT

Device shall alert.

**Definition** ias.h:32

[BT\_IAS\_ALERT\_LVL\_NO\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a89768db1911db8984bb09cd14a907997)

@ BT\_IAS\_ALERT\_LVL\_NO\_ALERT

No alerting should be done on device.

**Definition** ias.h:29

[BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT](group__bt__ias.md#ggabdaf2045e939bc71c060ee195494c9f0a911711c47da25f9dd509c297b0171653)

@ BT\_IAS\_ALERT\_LVL\_HIGH\_ALERT

Device should alert in strongest possible way.

**Definition** ias.h:35

[bt\_ias\_cb](structbt__ias__cb.md)

Immediate Alert Service callback structure.

**Definition** ias.h:39

[bt\_ias\_cb::high\_alert](structbt__ias__cb.md#ad2974bbd16e8d4425370a57f62601af5)

void(\* high\_alert)(void)

Callback function for alert level value.

**Definition** ias.h:59

[bt\_ias\_cb::no\_alert](structbt__ias__cb.md#ae0719b1f44f094ff0bbd3abea2bfdf15)

void(\* no\_alert)(void)

Callback function to stop alert.

**Definition** ias.h:45

[bt\_ias\_cb::mild\_alert](structbt__ias__cb.md#aeffe89f9e5a9b87efbdd0af471de980d)

void(\* mild\_alert)(void)

Callback function for alert level value.

**Definition** ias.h:52

[bt\_ias\_client\_cb](structbt__ias__client__cb.md)

**Definition** ias.h:76

[bt\_ias\_client\_cb::discover](structbt__ias__client__cb.md#a325ad34a67f9d9948740eb87862945b7)

void(\* discover)(struct bt\_conn \*conn, int err)

Callback function for bt\_ias\_discover.

**Definition** ias.h:84

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [ias.h](ias_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
