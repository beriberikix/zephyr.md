---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tmap_8h_source.html
original_path: doxygen/html/tmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

14#include <zephyr/autoconf.h>

15#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

16#include <[zephyr/sys/util.h](util_8h.md)>

17#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

18

[ 20](tmap_8h.md#a4415bbd383d428c9cc316fd0a5a79733)#define BT\_TMAP\_CG\_SUPPORTED \

21 (IS\_ENABLED(CONFIG\_BT\_CAP\_INITIATOR) && IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST\_CLIENT) && \

22 IS\_ENABLED(CONFIG\_BT\_TBS) && IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_CTLR))

23

[ 25](tmap_8h.md#aadaddbccf51b9e7ad78962c1a5d05488)#define BT\_TMAP\_CT\_SUPPORTED \

26 (IS\_ENABLED(CONFIG\_BT\_CAP\_ACCEPTOR) && IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST\_SERVER) && \

27 IS\_ENABLED(CONFIG\_BT\_TBS\_CLIENT) && \

28 (IS\_ENABLED(CONFIG\_BT\_ASCS\_ASE\_SNK) && \

29 IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_REND) == IS\_ENABLED(CONFIG\_BT\_ASCS\_ASE\_SNK)))

30

[ 32](tmap_8h.md#a83b5ebc64ad7028a14276a8d6fa51a6a)#define BT\_TMAP\_UMS\_SUPPORTED \

33 (IS\_ENABLED(CONFIG\_BT\_CAP\_INITIATOR) && \

34 IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST\_CLIENT\_ASE\_SNK) && IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_CTLR) && \

35 IS\_ENABLED(CONFIG\_BT\_MCS))

36

[ 38](tmap_8h.md#a197b2f5c0c894c2a7d82f415a5a59a47)#define BT\_TMAP\_UMR\_SUPPORTED \

39 (IS\_ENABLED(CONFIG\_BT\_CAP\_ACCEPTOR) && IS\_ENABLED(CONFIG\_BT\_ASCS\_ASE\_SNK) && \

40 IS\_ENABLED(CONFIG\_BT\_VCP\_VOL\_REND))

41

[ 43](tmap_8h.md#a00b55b590540c664e9371ca2d0477af8)#define BT\_TMAP\_BMS\_SUPPORTED \

44 (IS\_ENABLED(CONFIG\_BT\_CAP\_INITIATOR) && IS\_ENABLED(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE))

45

[ 47](tmap_8h.md#a10e832a6c2cfefc4971d85f182141f3e)#define BT\_TMAP\_BMR\_SUPPORTED \

48 (IS\_ENABLED(CONFIG\_BT\_CAP\_ACCEPTOR) && IS\_ENABLED(CONFIG\_BT\_BAP\_BROADCAST\_SINK))

49

[ 51](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4)enum [bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4) {

[ 59](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6) [BT\_TMAP\_ROLE\_CG](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 67](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d) [BT\_TMAP\_ROLE\_CT](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 74](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501) [BT\_TMAP\_ROLE\_UMS](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 81](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22) [BT\_TMAP\_ROLE\_UMR](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 88](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308) [BT\_TMAP\_ROLE\_BMS](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 95](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8) [BT\_TMAP\_ROLE\_BMR](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

96};

97

[ 99](structbt__tmap__cb.md)struct [bt\_tmap\_cb](structbt__tmap__cb.md) {

[ 110](structbt__tmap__cb.md#a22ee1b605448a3707d8086de30572def) void (\*[discovery\_complete](structbt__tmap__cb.md#a22ee1b605448a3707d8086de30572def))(enum [bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4) role, struct bt\_conn \*conn, int err);

111};

112

[ 120](tmap_8h.md#a2c93d1bce7db000cef76c42e5cab48cb)int [bt\_tmap\_register](tmap_8h.md#a2c93d1bce7db000cef76c42e5cab48cb)(enum [bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4) role);

121

[ 130](tmap_8h.md#acb52c3e4c56f6b042398ac992628d521)int [bt\_tmap\_discover](tmap_8h.md#acb52c3e4c56f6b042398ac992628d521)(struct bt\_conn \*conn, const struct [bt\_tmap\_cb](structbt__tmap__cb.md) \*tmap\_cb);

131

[ 139](tmap_8h.md#a0b51b305d5a5d87df9f4082951bd28a5)void [bt\_tmap\_set\_role](tmap_8h.md#a0b51b305d5a5d87df9f4082951bd28a5)(enum [bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4) role);

140

141#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_TMAP\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[bt\_tmap\_cb](structbt__tmap__cb.md)

TMAP callback structure.

**Definition** tmap.h:99

[bt\_tmap\_cb::discovery\_complete](structbt__tmap__cb.md#a22ee1b605448a3707d8086de30572def)

void(\* discovery\_complete)(enum bt\_tmap\_role role, struct bt\_conn \*conn, int err)

TMAP discovery complete callback.

**Definition** tmap.h:110

[bt\_tmap\_set\_role](tmap_8h.md#a0b51b305d5a5d87df9f4082951bd28a5)

void bt\_tmap\_set\_role(enum bt\_tmap\_role role)

Set one or multiple TMAP roles dynamically.

[bt\_tmap\_register](tmap_8h.md#a2c93d1bce7db000cef76c42e5cab48cb)

int bt\_tmap\_register(enum bt\_tmap\_role role)

Adds TMAS instance to database and sets the received TMAP role(s).

[bt\_tmap\_role](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4)

bt\_tmap\_role

TMAP Role characteristic.

**Definition** tmap.h:51

[BT\_TMAP\_ROLE\_UMR](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22)

@ BT\_TMAP\_ROLE\_UMR

TMAP Unicast Media Receiver role.

**Definition** tmap.h:81

[BT\_TMAP\_ROLE\_UMS](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501)

@ BT\_TMAP\_ROLE\_UMS

TMAP Unicast Media Sender role.

**Definition** tmap.h:74

[BT\_TMAP\_ROLE\_CG](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6)

@ BT\_TMAP\_ROLE\_CG

TMAP Call Gateway role.

**Definition** tmap.h:59

[BT\_TMAP\_ROLE\_BMS](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308)

@ BT\_TMAP\_ROLE\_BMS

TMAP Broadcast Media Sender role.

**Definition** tmap.h:88

[BT\_TMAP\_ROLE\_CT](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d)

@ BT\_TMAP\_ROLE\_CT

TMAP Call Terminal role.

**Definition** tmap.h:67

[BT\_TMAP\_ROLE\_BMR](tmap_8h.md#a4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8)

@ BT\_TMAP\_ROLE\_BMR

TMAP Broadcast Media Receiver role.

**Definition** tmap.h:95

[bt\_tmap\_discover](tmap_8h.md#acb52c3e4c56f6b042398ac992628d521)

int bt\_tmap\_discover(struct bt\_conn \*conn, const struct bt\_tmap\_cb \*tmap\_cb)

Perform service discovery as TMAP Client.

[util.h](util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [tmap.h](tmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
