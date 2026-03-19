---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tmap_8h_source.html
original_path: doxygen/html/tmap_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmap.h

[Go to the documentation of this file.](tmap_8h.md)

1

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TMAP\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TMAP\_

13

28

29#include <zephyr/autoconf.h>

30#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

31#include <[zephyr/sys/util.h](sys_2util_8h.md)>

32#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

33

[ 35](group__bt__tmap.md#ga4ef8a550bb374a5f257860082e1411d4)enum [bt\_tmap\_role](group__bt__tmap.md#ga4ef8a550bb374a5f257860082e1411d4) {

[ 43](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6) [BT\_TMAP\_ROLE\_CG](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 51](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d) [BT\_TMAP\_ROLE\_CT](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 58](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501) [BT\_TMAP\_ROLE\_UMS](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 65](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22) [BT\_TMAP\_ROLE\_UMR](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 72](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308) [BT\_TMAP\_ROLE\_BMS](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 79](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8) [BT\_TMAP\_ROLE\_BMR](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

80};

81

[ 83](structbt__tmap__cb.md)struct [bt\_tmap\_cb](structbt__tmap__cb.md) {

[ 94](structbt__tmap__cb.md#a22ee1b605448a3707d8086de30572def) void (\*[discovery\_complete](structbt__tmap__cb.md#a22ee1b605448a3707d8086de30572def))(enum [bt\_tmap\_role](group__bt__tmap.md#ga4ef8a550bb374a5f257860082e1411d4) role, struct bt\_conn \*conn, int err);

95};

96

[ 104](group__bt__tmap.md#ga2c93d1bce7db000cef76c42e5cab48cb)int [bt\_tmap\_register](group__bt__tmap.md#ga2c93d1bce7db000cef76c42e5cab48cb)(enum [bt\_tmap\_role](group__bt__tmap.md#ga4ef8a550bb374a5f257860082e1411d4) role);

105

[ 114](group__bt__tmap.md#gacb52c3e4c56f6b042398ac992628d521)int [bt\_tmap\_discover](group__bt__tmap.md#gacb52c3e4c56f6b042398ac992628d521)(struct bt\_conn \*conn, const struct [bt\_tmap\_cb](structbt__tmap__cb.md) \*tmap\_cb);

115

[ 123](group__bt__tmap.md#ga0b51b305d5a5d87df9f4082951bd28a5)void [bt\_tmap\_set\_role](group__bt__tmap.md#ga0b51b305d5a5d87df9f4082951bd28a5)(enum [bt\_tmap\_role](group__bt__tmap.md#ga4ef8a550bb374a5f257860082e1411d4) role);

124

128

129#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TMAP\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_tmap\_set\_role](group__bt__tmap.md#ga0b51b305d5a5d87df9f4082951bd28a5)

void bt\_tmap\_set\_role(enum bt\_tmap\_role role)

Set one or multiple TMAP roles dynamically.

[bt\_tmap\_register](group__bt__tmap.md#ga2c93d1bce7db000cef76c42e5cab48cb)

int bt\_tmap\_register(enum bt\_tmap\_role role)

Adds TMAS instance to database and sets the received TMAP role(s).

[bt\_tmap\_role](group__bt__tmap.md#ga4ef8a550bb374a5f257860082e1411d4)

bt\_tmap\_role

TMAP Role characteristic.

**Definition** tmap.h:35

[bt\_tmap\_discover](group__bt__tmap.md#gacb52c3e4c56f6b042398ac992628d521)

int bt\_tmap\_discover(struct bt\_conn \*conn, const struct bt\_tmap\_cb \*tmap\_cb)

Perform service discovery as TMAP Client.

[BT\_TMAP\_ROLE\_UMR](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22)

@ BT\_TMAP\_ROLE\_UMR

TMAP Unicast Media Receiver role.

**Definition** tmap.h:65

[BT\_TMAP\_ROLE\_UMS](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501)

@ BT\_TMAP\_ROLE\_UMS

TMAP Unicast Media Sender role.

**Definition** tmap.h:58

[BT\_TMAP\_ROLE\_CG](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6)

@ BT\_TMAP\_ROLE\_CG

TMAP Call Gateway role.

**Definition** tmap.h:43

[BT\_TMAP\_ROLE\_BMS](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308)

@ BT\_TMAP\_ROLE\_BMS

TMAP Broadcast Media Sender role.

**Definition** tmap.h:72

[BT\_TMAP\_ROLE\_CT](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d)

@ BT\_TMAP\_ROLE\_CT

TMAP Call Terminal role.

**Definition** tmap.h:51

[BT\_TMAP\_ROLE\_BMR](group__bt__tmap.md#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8)

@ BT\_TMAP\_ROLE\_BMR

TMAP Broadcast Media Receiver role.

**Definition** tmap.h:79

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[bt\_tmap\_cb](structbt__tmap__cb.md)

TMAP callback structure.

**Definition** tmap.h:83

[bt\_tmap\_cb::discovery\_complete](structbt__tmap__cb.md#a22ee1b605448a3707d8086de30572def)

void(\* discovery\_complete)(enum bt\_tmap\_role role, struct bt\_conn \*conn, int err)

TMAP discovery complete callback.

**Definition** tmap.h:94

[util.h](sys_2util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [tmap.h](tmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
