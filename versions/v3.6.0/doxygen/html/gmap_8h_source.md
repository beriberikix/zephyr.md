---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gmap_8h_source.html
original_path: doxygen/html/gmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gmap.h

[Go to the documentation of this file.](gmap_8h.md)

1

9

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_

12

13#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

14#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

15

22

[ 24](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56)enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) {

[ 31](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251) [BT\_GMAP\_ROLE\_UGG](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 38](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b) [BT\_GMAP\_ROLE\_UGT](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 45](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6) [BT\_GMAP\_ROLE\_BGS](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 52](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091) [BT\_GMAP\_ROLE\_BGR](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

53};

54

[ 56](group__bt__gmap.md#ga3ef43378bad84bbcd726e318cf0bc145)enum [bt\_gmap\_ugg\_feat](group__bt__gmap.md#ga3ef43378bad84bbcd726e318cf0bc145) {

[ 62](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e) [BT\_GMAP\_UGG\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 68](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331) [BT\_GMAP\_UGG\_FEAT\_96KBPS\_SOURCE](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 75](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1) [BT\_GMAP\_UGG\_FEAT\_MULTISINK](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

76};

77

[ 79](group__bt__gmap.md#ga0fe87d6d1412c15564ba7de29e3d7a48)enum [bt\_gmap\_ugt\_feat](group__bt__gmap.md#ga0fe87d6d1412c15564ba7de29e3d7a48) {

[ 85](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231) [BT\_GMAP\_UGT\_FEAT\_SOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 91](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88) [BT\_GMAP\_UGT\_FEAT\_80KBPS\_SOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 97](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c) [BT\_GMAP\_UGT\_FEAT\_SINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 103](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604) [BT\_GMAP\_UGT\_FEAT\_64KBPS\_SINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 109](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e) [BT\_GMAP\_UGT\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 116](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08) [BT\_GMAP\_UGT\_FEAT\_MULTISINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 124](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045) [BT\_GMAP\_UGT\_FEAT\_MULTISOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

125};

126

[ 128](group__bt__gmap.md#ga3a79c408b283864616a522b1f04cacaf)enum [bt\_gmap\_bgs\_feat](group__bt__gmap.md#ga3a79c408b283864616a522b1f04cacaf) {

[ 130](group__bt__gmap.md#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8) [BT\_GMAP\_BGS\_FEAT\_96KBPS](group__bt__gmap.md#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

131};

132

[ 134](group__bt__gmap.md#ga9c1145ad5334e14d4978b6d7d3c84b6c)enum [bt\_gmap\_bgr\_feat](group__bt__gmap.md#ga9c1145ad5334e14d4978b6d7d3c84b6c) {

[ 140](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630) [BT\_GMAP\_BGR\_FEAT\_MULTISINK](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 142](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6) [BT\_GMAP\_BGR\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

143};

144

[ 146](structbt__gmap__feat.md)struct [bt\_gmap\_feat](structbt__gmap__feat.md) {

[ 148](structbt__gmap__feat.md#a7e57da1f8aa0a6ac8e7f929f5ba7e9cd) enum [bt\_gmap\_ugg\_feat](group__bt__gmap.md#ga3ef43378bad84bbcd726e318cf0bc145) [ugg\_feat](structbt__gmap__feat.md#a7e57da1f8aa0a6ac8e7f929f5ba7e9cd);

[ 150](structbt__gmap__feat.md#a3793984ce81ff90aab8eb6ad635e24d5) enum [bt\_gmap\_ugt\_feat](group__bt__gmap.md#ga0fe87d6d1412c15564ba7de29e3d7a48) [ugt\_feat](structbt__gmap__feat.md#a3793984ce81ff90aab8eb6ad635e24d5);

[ 152](structbt__gmap__feat.md#a0ef9878ffcd04a6b88cc8364173cfc10) enum [bt\_gmap\_bgs\_feat](group__bt__gmap.md#ga3a79c408b283864616a522b1f04cacaf) [bgs\_feat](structbt__gmap__feat.md#a0ef9878ffcd04a6b88cc8364173cfc10);

[ 154](structbt__gmap__feat.md#a918d35e89da086321d728f61deb0c962) enum [bt\_gmap\_bgr\_feat](group__bt__gmap.md#ga9c1145ad5334e14d4978b6d7d3c84b6c) [bgr\_feat](structbt__gmap__feat.md#a918d35e89da086321d728f61deb0c962);

155};

156

[ 158](structbt__gmap__cb.md)struct [bt\_gmap\_cb](structbt__gmap__cb.md) {

[ 169](structbt__gmap__cb.md#a72c25ae277e04d419f41733d0b11aefc) void (\*[discover](structbt__gmap__cb.md#a72c25ae277e04d419f41733d0b11aefc))(struct bt\_conn \*conn, int err, enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role,

170 struct [bt\_gmap\_feat](structbt__gmap__feat.md) features);

171};

172

[ 182](group__bt__gmap.md#gacc4853bf69d0a13353fc941aa7e4e190)int [bt\_gmap\_cb\_register](group__bt__gmap.md#gacc4853bf69d0a13353fc941aa7e4e190)(const struct [bt\_gmap\_cb](structbt__gmap__cb.md) \*cb);

183

[ 198](group__bt__gmap.md#gab54963e226753d44085a7d1f5dccdef6)int [bt\_gmap\_discover](group__bt__gmap.md#gab54963e226753d44085a7d1f5dccdef6)(struct bt\_conn \*conn);

199

[ 211](group__bt__gmap.md#ga75211707bbdceff35235c353dc8c7609)int [bt\_gmap\_register](group__bt__gmap.md#ga75211707bbdceff35235c353dc8c7609)(enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features);

212

[ 231](group__bt__gmap.md#ga956efe257f06b627615a0a82d44db919)int [bt\_gmap\_set\_role](group__bt__gmap.md#ga956efe257f06b627615a0a82d44db919)(enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features);

232 /\* end of bt\_gmap \*/

234

235#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_GMAP\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_gmap\_ugt\_feat](group__bt__gmap.md#ga0fe87d6d1412c15564ba7de29e3d7a48)

bt\_gmap\_ugt\_feat

Unicast Game Terminal Feature bitfield.

**Definition** gmap.h:79

[bt\_gmap\_bgs\_feat](group__bt__gmap.md#ga3a79c408b283864616a522b1f04cacaf)

bt\_gmap\_bgs\_feat

Broadcast Game Sender Feature bitfield.

**Definition** gmap.h:128

[bt\_gmap\_ugg\_feat](group__bt__gmap.md#ga3ef43378bad84bbcd726e318cf0bc145)

bt\_gmap\_ugg\_feat

Unicast Game Gateway Feature bitfield.

**Definition** gmap.h:56

[bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56)

bt\_gmap\_role

Gaming Role bitfield.

**Definition** gmap.h:24

[bt\_gmap\_register](group__bt__gmap.md#ga75211707bbdceff35235c353dc8c7609)

int bt\_gmap\_register(enum bt\_gmap\_role role, struct bt\_gmap\_feat features)

Adds GMAS instance to database and sets the received Gaming Audio Profile role(s).

[bt\_gmap\_set\_role](group__bt__gmap.md#ga956efe257f06b627615a0a82d44db919)

int bt\_gmap\_set\_role(enum bt\_gmap\_role role, struct bt\_gmap\_feat features)

Set one or multiple Gaming Audio Profile roles and features dynamically.

[bt\_gmap\_bgr\_feat](group__bt__gmap.md#ga9c1145ad5334e14d4978b6d7d3c84b6c)

bt\_gmap\_bgr\_feat

Broadcast Game Receiver Feature bitfield.

**Definition** gmap.h:134

[bt\_gmap\_discover](group__bt__gmap.md#gab54963e226753d44085a7d1f5dccdef6)

int bt\_gmap\_discover(struct bt\_conn \*conn)

Discover Gaming Service on a remote device.

[bt\_gmap\_cb\_register](group__bt__gmap.md#gacc4853bf69d0a13353fc941aa7e4e190)

int bt\_gmap\_cb\_register(const struct bt\_gmap\_cb \*cb)

Registers the callbacks used by the Gaming Audio Profile.

[BT\_GMAP\_UGT\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e)

@ BT\_GMAP\_UGT\_FEAT\_MULTIPLEX

Support for receiving multiple LC3 codec frames per block in an SDU.

**Definition** gmap.h:109

[BT\_GMAP\_UGT\_FEAT\_80KBPS\_SOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88)

@ BT\_GMAP\_UGT\_FEAT\_80KBPS\_SOURCE

80 kbps source support

**Definition** gmap.h:91

[BT\_GMAP\_UGT\_FEAT\_64KBPS\_SINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604)

@ BT\_GMAP\_UGT\_FEAT\_64KBPS\_SINK

64 kbps sink support

**Definition** gmap.h:103

[BT\_GMAP\_UGT\_FEAT\_SOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231)

@ BT\_GMAP\_UGT\_FEAT\_SOURCE

Source support.

**Definition** gmap.h:85

[BT\_GMAP\_UGT\_FEAT\_MULTISOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045)

@ BT\_GMAP\_UGT\_FEAT\_MULTISOURCE

Support for sending at least two audio channels, each in a separate CIS.

**Definition** gmap.h:124

[BT\_GMAP\_UGT\_FEAT\_MULTISINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08)

@ BT\_GMAP\_UGT\_FEAT\_MULTISINK

Support for receiving at least two audio channels, each in a separate CIS.

**Definition** gmap.h:116

[BT\_GMAP\_UGT\_FEAT\_SINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c)

@ BT\_GMAP\_UGT\_FEAT\_SINK

Sink support.

**Definition** gmap.h:97

[BT\_GMAP\_BGS\_FEAT\_96KBPS](group__bt__gmap.md#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8)

@ BT\_GMAP\_BGS\_FEAT\_96KBPS

96 kbps support

**Definition** gmap.h:130

[BT\_GMAP\_UGG\_FEAT\_MULTISINK](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1)

@ BT\_GMAP\_UGG\_FEAT\_MULTISINK

Support for receiving at least two channels of audio, each in a separate CIS.

**Definition** gmap.h:75

[BT\_GMAP\_UGG\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e)

@ BT\_GMAP\_UGG\_FEAT\_MULTIPLEX

Support transmitting multiple LC3 codec frames per block in an SDU.

**Definition** gmap.h:62

[BT\_GMAP\_UGG\_FEAT\_96KBPS\_SOURCE](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331)

@ BT\_GMAP\_UGG\_FEAT\_96KBPS\_SOURCE

96 kbps source support

**Definition** gmap.h:68

[BT\_GMAP\_ROLE\_UGT](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b)

@ BT\_GMAP\_ROLE\_UGT

Gaming Role Unicast Game Terminal.

**Definition** gmap.h:38

[BT\_GMAP\_ROLE\_BGS](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6)

@ BT\_GMAP\_ROLE\_BGS

Gaming Role Broadcast Game Sender.

**Definition** gmap.h:45

[BT\_GMAP\_ROLE\_UGG](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251)

@ BT\_GMAP\_ROLE\_UGG

Gaming Role Unicast Game Gateway.

**Definition** gmap.h:31

[BT\_GMAP\_ROLE\_BGR](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091)

@ BT\_GMAP\_ROLE\_BGR

Gaming Role Broadcast Game Receiver.

**Definition** gmap.h:52

[BT\_GMAP\_BGR\_FEAT\_MULTISINK](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630)

@ BT\_GMAP\_BGR\_FEAT\_MULTISINK

Support for receiving at least two audio channels, each in a separate BIS.

**Definition** gmap.h:140

[BT\_GMAP\_BGR\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6)

@ BT\_GMAP\_BGR\_FEAT\_MULTIPLEX

Support for receiving multiple LC3 codec frames per block in an SDU.

**Definition** gmap.h:142

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[bt\_gmap\_cb](structbt__gmap__cb.md)

Hearing Access Service Client callback structure.

**Definition** gmap.h:158

[bt\_gmap\_cb::discover](structbt__gmap__cb.md#a72c25ae277e04d419f41733d0b11aefc)

void(\* discover)(struct bt\_conn \*conn, int err, enum bt\_gmap\_role role, struct bt\_gmap\_feat features)

Callback function for bt\_has\_discover.

**Definition** gmap.h:169

[bt\_gmap\_feat](structbt__gmap__feat.md)

Broadcast Game Receiver Feature bitfield.

**Definition** gmap.h:146

[bt\_gmap\_feat::bgs\_feat](structbt__gmap__feat.md#a0ef9878ffcd04a6b88cc8364173cfc10)

enum bt\_gmap\_bgs\_feat bgs\_feat

Remote Broadcast Game Sender features.

**Definition** gmap.h:152

[bt\_gmap\_feat::ugt\_feat](structbt__gmap__feat.md#a3793984ce81ff90aab8eb6ad635e24d5)

enum bt\_gmap\_ugt\_feat ugt\_feat

Unicast Game Terminal features.

**Definition** gmap.h:150

[bt\_gmap\_feat::ugg\_feat](structbt__gmap__feat.md#a7e57da1f8aa0a6ac8e7f929f5ba7e9cd)

enum bt\_gmap\_ugg\_feat ugg\_feat

Unicast Game Gateway features.

**Definition** gmap.h:148

[bt\_gmap\_feat::bgr\_feat](structbt__gmap__feat.md#a918d35e89da086321d728f61deb0c962)

enum bt\_gmap\_bgr\_feat bgr\_feat

Remote Broadcast Game Receiver features.

**Definition** gmap.h:154

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [gmap.h](gmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
