---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/heartbeat_8h_source.html
original_path: doxygen/html/heartbeat_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

heartbeat.h

[Go to the documentation of this file.](heartbeat_8h.md)

1

4

5/\*

6 \* Copyright (c) 2020 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEARTBEAT\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEARTBEAT\_H\_

12

13#include <[stdint.h](stdint_8h.md)>

14

15#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

16#include <[zephyr/sys/slist.h](slist_8h.md)>

17

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 30](structbt__mesh__hb__pub.md)struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) {

[ 32](structbt__mesh__hb__pub.md#aaeb4c9000088418d8688b4f2f964335a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst](structbt__mesh__hb__pub.md#aaeb4c9000088418d8688b4f2f964335a);

[ 34](structbt__mesh__hb__pub.md#a7161896dd5e337b2b0ee671f59a2444a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](structbt__mesh__hb__pub.md#a7161896dd5e337b2b0ee671f59a2444a);

[ 36](structbt__mesh__hb__pub.md#a82dd3457291cc4a939883590e27fdbfb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__hb__pub.md#a82dd3457291cc4a939883590e27fdbfb);

[ 43](structbt__mesh__hb__pub.md#a08f32f66fb5c7c0011651633ad212bc9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [feat](structbt__mesh__hb__pub.md#a08f32f66fb5c7c0011651633ad212bc9);

[ 45](structbt__mesh__hb__pub.md#af8ed3029b088c7b45be4912eb0d9024d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__hb__pub.md#af8ed3029b088c7b45be4912eb0d9024d);

[ 47](structbt__mesh__hb__pub.md#a0bf6205724b157fe374e24c024f240c9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [period](structbt__mesh__hb__pub.md#a0bf6205724b157fe374e24c024f240c9);

48};

49

[ 51](structbt__mesh__hb__sub.md)struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) {

[ 53](structbt__mesh__hb__sub.md#af7b20a7337c31110b1ae38c7eacc071a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [period](structbt__mesh__hb__sub.md#af7b20a7337c31110b1ae38c7eacc071a);

[ 55](structbt__mesh__hb__sub.md#ad66fd08eb09d475bef9c290fa7ae0a90) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [remaining](structbt__mesh__hb__sub.md#ad66fd08eb09d475bef9c290fa7ae0a90);

[ 57](structbt__mesh__hb__sub.md#afb9fba6c32257690539dd621e215708b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [src](structbt__mesh__hb__sub.md#afb9fba6c32257690539dd621e215708b);

[ 59](structbt__mesh__hb__sub.md#ab10708af9ddfd7a80c370d40d2146a8b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst](structbt__mesh__hb__sub.md#ab10708af9ddfd7a80c370d40d2146a8b);

[ 61](structbt__mesh__hb__sub.md#a41dd595eb6a0c980c49f84aca11b3ac2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [count](structbt__mesh__hb__sub.md#a41dd595eb6a0c980c49f84aca11b3ac2);

[ 68](structbt__mesh__hb__sub.md#aae4eb4e77166dfb49a7341ae8fcb9e6e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_hops](structbt__mesh__hb__sub.md#aae4eb4e77166dfb49a7341ae8fcb9e6e);

[ 75](structbt__mesh__hb__sub.md#a38252818d3a2e136e5dfc9bda847d0b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_hops](structbt__mesh__hb__sub.md#a38252818d3a2e136e5dfc9bda847d0b0);

76};

77

[ 79](structbt__mesh__hb__cb.md)struct [bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md) {

[ 94](structbt__mesh__hb__cb.md#aa3b85249e1a40842c0f937385a72103f) void (\*[recv](structbt__mesh__hb__cb.md#aa3b85249e1a40842c0f937385a72103f))(const struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hops,

95 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) feat);

96

[ 104](structbt__mesh__hb__cb.md#aa979e024174fa19f047a26f94b54a9d3) void (\*[sub\_end](structbt__mesh__hb__cb.md#aa979e024174fa19f047a26f94b54a9d3))(const struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*sub);

105

[ 112](structbt__mesh__hb__cb.md#acc5559541f53e2987899433d4d434557) void (\*[pub\_sent](structbt__mesh__hb__cb.md#acc5559541f53e2987899433d4d434557))(const struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \*pub);

113};

114

[ 123](group__bt__mesh__heartbeat.md#ga517f009151a7eeaa898a853fd0d7a93a)#define BT\_MESH\_HB\_CB\_DEFINE(\_name) \

124 static const STRUCT\_SECTION\_ITERABLE(bt\_mesh\_hb\_cb, \_name)

125

[ 130](group__bt__mesh__heartbeat.md#ga2e95d8f9d75f1bea13a9584d201fd713)void [bt\_mesh\_hb\_pub\_get](group__bt__mesh__heartbeat.md#ga2e95d8f9d75f1bea13a9584d201fd713)(struct [bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md) \*get);

131

[ 136](group__bt__mesh__heartbeat.md#ga3013c3da6cc1a34b0c98c56fba7e7877)void [bt\_mesh\_hb\_sub\_get](group__bt__mesh__heartbeat.md#ga3013c3da6cc1a34b0c98c56fba7e7877)(struct [bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md) \*get);

137

138#ifdef \_\_cplusplus

139}

140#endif

144

145#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEARTBEAT\_H\_ \*/

[bt\_mesh\_hb\_pub\_get](group__bt__mesh__heartbeat.md#ga2e95d8f9d75f1bea13a9584d201fd713)

void bt\_mesh\_hb\_pub\_get(struct bt\_mesh\_hb\_pub \*get)

Get the current Heartbeat publication parameters.

[bt\_mesh\_hb\_sub\_get](group__bt__mesh__heartbeat.md#ga3013c3da6cc1a34b0c98c56fba7e7877)

void bt\_mesh\_hb\_sub\_get(struct bt\_mesh\_hb\_sub \*get)

Get the current Heartbeat subscription parameters.

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_hb\_cb](structbt__mesh__hb__cb.md)

Heartbeat callback structure.

**Definition** heartbeat.h:79

[bt\_mesh\_hb\_cb::recv](structbt__mesh__hb__cb.md#aa3b85249e1a40842c0f937385a72103f)

void(\* recv)(const struct bt\_mesh\_hb\_sub \*sub, uint8\_t hops, uint16\_t feat)

Receive callback for heartbeats.

**Definition** heartbeat.h:94

[bt\_mesh\_hb\_cb::sub\_end](structbt__mesh__hb__cb.md#aa979e024174fa19f047a26f94b54a9d3)

void(\* sub\_end)(const struct bt\_mesh\_hb\_sub \*sub)

Subscription end callback for heartbeats.

**Definition** heartbeat.h:104

[bt\_mesh\_hb\_cb::pub\_sent](structbt__mesh__hb__cb.md#acc5559541f53e2987899433d4d434557)

void(\* pub\_sent)(const struct bt\_mesh\_hb\_pub \*pub)

Publication sent callback for heartbeats.

**Definition** heartbeat.h:112

[bt\_mesh\_hb\_pub](structbt__mesh__hb__pub.md)

Heartbeat Publication parameters.

**Definition** heartbeat.h:30

[bt\_mesh\_hb\_pub::feat](structbt__mesh__hb__pub.md#a08f32f66fb5c7c0011651633ad212bc9)

uint16\_t feat

Bitmap of features that trigger a Heartbeat publication if they change.

**Definition** heartbeat.h:43

[bt\_mesh\_hb\_pub::period](structbt__mesh__hb__pub.md#a0bf6205724b157fe374e24c024f240c9)

uint32\_t period

Publication period in seconds.

**Definition** heartbeat.h:47

[bt\_mesh\_hb\_pub::count](structbt__mesh__hb__pub.md#a7161896dd5e337b2b0ee671f59a2444a)

uint16\_t count

Remaining publish count.

**Definition** heartbeat.h:34

[bt\_mesh\_hb\_pub::ttl](structbt__mesh__hb__pub.md#a82dd3457291cc4a939883590e27fdbfb)

uint8\_t ttl

Time To Live value.

**Definition** heartbeat.h:36

[bt\_mesh\_hb\_pub::dst](structbt__mesh__hb__pub.md#aaeb4c9000088418d8688b4f2f964335a)

uint16\_t dst

Destination address.

**Definition** heartbeat.h:32

[bt\_mesh\_hb\_pub::net\_idx](structbt__mesh__hb__pub.md#af8ed3029b088c7b45be4912eb0d9024d)

uint16\_t net\_idx

Network index used for publishing.

**Definition** heartbeat.h:45

[bt\_mesh\_hb\_sub](structbt__mesh__hb__sub.md)

Heartbeat Subscription parameters.

**Definition** heartbeat.h:51

[bt\_mesh\_hb\_sub::max\_hops](structbt__mesh__hb__sub.md#a38252818d3a2e136e5dfc9bda847d0b0)

uint8\_t max\_hops

Maximum hops in received messages, ie the longest registered path from the publishing node to the sub...

**Definition** heartbeat.h:75

[bt\_mesh\_hb\_sub::count](structbt__mesh__hb__sub.md#a41dd595eb6a0c980c49f84aca11b3ac2)

uint16\_t count

The number of received Heartbeat messages so far.

**Definition** heartbeat.h:61

[bt\_mesh\_hb\_sub::min\_hops](structbt__mesh__hb__sub.md#aae4eb4e77166dfb49a7341ae8fcb9e6e)

uint8\_t min\_hops

Minimum hops in received messages, ie the shortest registered path from the publishing node to the su...

**Definition** heartbeat.h:68

[bt\_mesh\_hb\_sub::dst](structbt__mesh__hb__sub.md#ab10708af9ddfd7a80c370d40d2146a8b)

uint16\_t dst

Destination address to received Heartbeats on.

**Definition** heartbeat.h:59

[bt\_mesh\_hb\_sub::remaining](structbt__mesh__hb__sub.md#ad66fd08eb09d475bef9c290fa7ae0a90)

uint32\_t remaining

Remaining subscription time in seconds.

**Definition** heartbeat.h:55

[bt\_mesh\_hb\_sub::period](structbt__mesh__hb__sub.md#af7b20a7337c31110b1ae38c7eacc071a)

uint32\_t period

Subscription period in seconds.

**Definition** heartbeat.h:53

[bt\_mesh\_hb\_sub::src](structbt__mesh__hb__sub.md#afb9fba6c32257690539dd621e215708b)

uint16\_t src

Source address to receive Heartbeats from.

**Definition** heartbeat.h:57

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [heartbeat.h](heartbeat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
