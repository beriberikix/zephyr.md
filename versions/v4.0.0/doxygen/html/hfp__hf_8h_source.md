---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hfp__hf_8h_source.html
original_path: doxygen/html/hfp__hf_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_hf.h

[Go to the documentation of this file.](hfp__hf_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_

12

19

20#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26/\* AT Commands \*/

[ 27](group__bt__hfp.md#gae88edd233a1f00e6d12be7fe3ac8c9fd)enum [bt\_hfp\_hf\_at\_cmd](group__bt__hfp.md#gae88edd233a1f00e6d12be7fe3ac8c9fd) {

[ 28](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdae80220d66b99e9f0954fa9491565f641) [BT\_HFP\_HF\_ATA](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdae80220d66b99e9f0954fa9491565f641),

[ 29](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdaa777f4b5e3b8310e528e535ca0667a18) [BT\_HFP\_HF\_AT\_CHUP](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdaa777f4b5e3b8310e528e535ca0667a18),

30};

31

32/\*

33 \* Command complete types for the application

34 \*/

[ 35](group__bt__hfp.md#ga7c90e2ab7ed6c5b25252f88408235598)#define HFP\_HF\_CMD\_OK 0

[ 36](group__bt__hfp.md#ga463b8eb680e7cbedfbf9c5e5628558af)#define HFP\_HF\_CMD\_ERROR 1

[ 37](group__bt__hfp.md#ga80133496d4868f11381d14fe46cfdb51)#define HFP\_HF\_CMD\_CME\_ERROR 2

[ 38](group__bt__hfp.md#ga613fa4c3e102c7ab20e587f34c14d5c6)#define HFP\_HF\_CMD\_UNKNOWN\_ERROR 4

39

[ 41](structbt__hfp__hf__cmd__complete.md)struct [bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md) {

42 /\* Command complete status \*/

[ 43](structbt__hfp__hf__cmd__complete.md#a4ebda4942e909b11d35906b330ef62d7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structbt__hfp__hf__cmd__complete.md#a4ebda4942e909b11d35906b330ef62d7);

44 /\* CME error number to be added \*/

[ 45](structbt__hfp__hf__cmd__complete.md#ac5030c2bee23077c88fd71ba5f005c16) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cme](structbt__hfp__hf__cmd__complete.md#ac5030c2bee23077c88fd71ba5f005c16);

46};

47

[ 49](structbt__hfp__hf__cb.md)struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) {

[ 57](structbt__hfp__hf__cb.md#a989373632ab9c5e9f5ee6a8b15d2818d) void (\*[connected](structbt__hfp__hf__cb.md#a989373632ab9c5e9f5ee6a8b15d2818d))(struct bt\_conn \*conn);

[ 66](structbt__hfp__hf__cb.md#a064e7e6471d537aebc36f3273443cf45) void (\*[disconnected](structbt__hfp__hf__cb.md#a064e7e6471d537aebc36f3273443cf45))(struct bt\_conn \*conn);

[ 75](structbt__hfp__hf__cb.md#ab99c8d781f4d2f298bd87ab7c6a1cfab) void (\*[sco\_connected](structbt__hfp__hf__cb.md#ab99c8d781f4d2f298bd87ab7c6a1cfab))(struct bt\_conn \*conn, struct bt\_conn \*sco\_conn);

[ 84](structbt__hfp__hf__cb.md#a4586240506c876c9f58cf60a091b4044) void (\*[sco\_disconnected](structbt__hfp__hf__cb.md#a4586240506c876c9f58cf60a091b4044))(struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

[ 92](structbt__hfp__hf__cb.md#a8e9062e76d30dc9db0b4be9f6ec3e26f) void (\*[service](structbt__hfp__hf__cb.md#a8e9062e76d30dc9db0b4be9f6ec3e26f))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 100](structbt__hfp__hf__cb.md#a216dcba1621369bc8c8ace22a8b707e8) void (\*[call](structbt__hfp__hf__cb.md#a216dcba1621369bc8c8ace22a8b707e8))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 108](structbt__hfp__hf__cb.md#a0b120f6fd8e20432bab8d9f4f695482f) void (\*[call\_setup](structbt__hfp__hf__cb.md#a0b120f6fd8e20432bab8d9f4f695482f))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 116](structbt__hfp__hf__cb.md#aa9e2671fee627a0767c3f6cb269a39d0) void (\*[call\_held](structbt__hfp__hf__cb.md#aa9e2671fee627a0767c3f6cb269a39d0))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 124](structbt__hfp__hf__cb.md#a485cdbf03ef3bce0a156c13c33eed3e1) void (\*[signal](structbt__hfp__hf__cb.md#a485cdbf03ef3bce0a156c13c33eed3e1))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 132](structbt__hfp__hf__cb.md#addc8b3aef445ba67df5d340a5a3e9989) void (\*[roam](structbt__hfp__hf__cb.md#addc8b3aef445ba67df5d340a5a3e9989))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 140](structbt__hfp__hf__cb.md#a8deff765f7aa622d495e768b3137871f) void (\*[battery](structbt__hfp__hf__cb.md#a8deff765f7aa622d495e768b3137871f))(struct bt\_conn \*conn, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

[ 148](structbt__hfp__hf__cb.md#a580dd17c688c0e6375ef7c84a3751213) void (\*[ring\_indication](structbt__hfp__hf__cb.md#a580dd17c688c0e6375ef7c84a3751213))(struct bt\_conn \*conn);

[ 156](structbt__hfp__hf__cb.md#aa86799138890884ef18e7e0fe4774945) void (\*[cmd\_complete\_cb](structbt__hfp__hf__cb.md#aa86799138890884ef18e7e0fe4774945))(struct bt\_conn \*conn,

157 struct [bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

158};

159

[ 169](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161)int [bt\_hfp\_hf\_register](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161)(struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \*cb);

170

[ 180](group__bt__hfp.md#ga88f700df453cfca14926afb1db9c70d0)int [bt\_hfp\_hf\_send\_cmd](group__bt__hfp.md#ga88f700df453cfca14926afb1db9c70d0)(struct bt\_conn \*conn, enum [bt\_hfp\_hf\_at\_cmd](group__bt__hfp.md#gae88edd233a1f00e6d12be7fe3ac8c9fd) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

181

182#ifdef \_\_cplusplus

183}

184#endif

185

189

190#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_hfp\_hf\_register](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161)

int bt\_hfp\_hf\_register(struct bt\_hfp\_hf\_cb \*cb)

Register HFP HF profile.

[bt\_hfp\_hf\_send\_cmd](group__bt__hfp.md#ga88f700df453cfca14926afb1db9c70d0)

int bt\_hfp\_hf\_send\_cmd(struct bt\_conn \*conn, enum bt\_hfp\_hf\_at\_cmd cmd)

Handsfree client Send AT.

[bt\_hfp\_hf\_at\_cmd](group__bt__hfp.md#gae88edd233a1f00e6d12be7fe3ac8c9fd)

bt\_hfp\_hf\_at\_cmd

**Definition** hfp\_hf.h:27

[BT\_HFP\_HF\_AT\_CHUP](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdaa777f4b5e3b8310e528e535ca0667a18)

@ BT\_HFP\_HF\_AT\_CHUP

**Definition** hfp\_hf.h:29

[BT\_HFP\_HF\_ATA](group__bt__hfp.md#ggae88edd233a1f00e6d12be7fe3ac8c9fdae80220d66b99e9f0954fa9491565f641)

@ BT\_HFP\_HF\_ATA

**Definition** hfp\_hf.h:28

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md)

HFP profile application callback.

**Definition** hfp\_hf.h:49

[bt\_hfp\_hf\_cb::disconnected](structbt__hfp__hf__cb.md#a064e7e6471d537aebc36f3273443cf45)

void(\* disconnected)(struct bt\_conn \*conn)

HF disconnected callback to application.

**Definition** hfp\_hf.h:66

[bt\_hfp\_hf\_cb::call\_setup](structbt__hfp__hf__cb.md#a0b120f6fd8e20432bab8d9f4f695482f)

void(\* call\_setup)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:108

[bt\_hfp\_hf\_cb::call](structbt__hfp__hf__cb.md#a216dcba1621369bc8c8ace22a8b707e8)

void(\* call)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:100

[bt\_hfp\_hf\_cb::sco\_disconnected](structbt__hfp__hf__cb.md#a4586240506c876c9f58cf60a091b4044)

void(\* sco\_disconnected)(struct bt\_conn \*sco\_conn, uint8\_t reason)

HF SCO/eSCO disconnected Callback.

**Definition** hfp\_hf.h:84

[bt\_hfp\_hf\_cb::signal](structbt__hfp__hf__cb.md#a485cdbf03ef3bce0a156c13c33eed3e1)

void(\* signal)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:124

[bt\_hfp\_hf\_cb::ring\_indication](structbt__hfp__hf__cb.md#a580dd17c688c0e6375ef7c84a3751213)

void(\* ring\_indication)(struct bt\_conn \*conn)

HF incoming call Ring indication callback to application.

**Definition** hfp\_hf.h:148

[bt\_hfp\_hf\_cb::battery](structbt__hfp__hf__cb.md#a8deff765f7aa622d495e768b3137871f)

void(\* battery)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:140

[bt\_hfp\_hf\_cb::service](structbt__hfp__hf__cb.md#a8e9062e76d30dc9db0b4be9f6ec3e26f)

void(\* service)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:92

[bt\_hfp\_hf\_cb::connected](structbt__hfp__hf__cb.md#a989373632ab9c5e9f5ee6a8b15d2818d)

void(\* connected)(struct bt\_conn \*conn)

HF connected callback to application.

**Definition** hfp\_hf.h:57

[bt\_hfp\_hf\_cb::cmd\_complete\_cb](structbt__hfp__hf__cb.md#aa86799138890884ef18e7e0fe4774945)

void(\* cmd\_complete\_cb)(struct bt\_conn \*conn, struct bt\_hfp\_hf\_cmd\_complete \*cmd)

HF notify command completed callback to application.

**Definition** hfp\_hf.h:156

[bt\_hfp\_hf\_cb::call\_held](structbt__hfp__hf__cb.md#aa9e2671fee627a0767c3f6cb269a39d0)

void(\* call\_held)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:116

[bt\_hfp\_hf\_cb::sco\_connected](structbt__hfp__hf__cb.md#ab99c8d781f4d2f298bd87ab7c6a1cfab)

void(\* sco\_connected)(struct bt\_conn \*conn, struct bt\_conn \*sco\_conn)

HF SCO/eSCO connected Callback.

**Definition** hfp\_hf.h:75

[bt\_hfp\_hf\_cb::roam](structbt__hfp__hf__cb.md#addc8b3aef445ba67df5d340a5a3e9989)

void(\* roam)(struct bt\_conn \*conn, uint32\_t value)

HF indicator Callback.

**Definition** hfp\_hf.h:132

[bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md)

HFP HF Command completion field.

**Definition** hfp\_hf.h:41

[bt\_hfp\_hf\_cmd\_complete::type](structbt__hfp__hf__cmd__complete.md#a4ebda4942e909b11d35906b330ef62d7)

uint8\_t type

**Definition** hfp\_hf.h:43

[bt\_hfp\_hf\_cmd\_complete::cme](structbt__hfp__hf__cmd__complete.md#ac5030c2bee23077c88fd71ba5f005c16)

uint8\_t cme

**Definition** hfp\_hf.h:45

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_hf.h](hfp__hf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
