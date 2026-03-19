---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hfp__ag_8h_source.html
original_path: doxygen/html/hfp__ag_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_ag.h

[Go to the documentation of this file.](hfp__ag_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright 2023-2024 NXP

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_AG\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_AG\_H\_

13

20

21#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27/\* HFP AG Indicators \*/

[ 28](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810)enum [bt\_hfp\_ag\_indicator](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810) {

[ 29](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) [BT\_HFP\_AG\_SERVICE\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) = 0, /\* Service availability indicator \*/

[ 30](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) [BT\_HFP\_AG\_CALL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) = 1, /\* call status indicator \*/

[ 31](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) [BT\_HFP\_AG\_CALL\_SETUP\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) = 2, /\* Call set up status indicator \*/

[ 32](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) [BT\_HFP\_AG\_CALL\_HELD\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) = 3, /\* Call hold status indicator \*/

[ 33](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) [BT\_HFP\_AG\_SIGNAL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) = 4, /\* Signal strength indicator \*/

[ 34](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) [BT\_HFP\_AG\_ROAM\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) = 5, /\* Roaming status indicator \*/

[ 35](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) [BT\_HFP\_AG\_BATTERY\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) = 6, /\* Battery change indicator \*/

[ 36](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36) [BT\_HFP\_AG\_IND\_MAX](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36) /\* Indicator MAX value \*/

37};

38

39/\* HFP CODEC \*/

[ 40](group__bt__hfp__ag.md#gada6266f825879f39147c5d889e4192c9)#define BT\_HFP\_AG\_CODEC\_CVSD 0x01

[ 41](group__bt__hfp__ag.md#ga3591201c7310288ea2e01e2f77a0c0d3)#define BT\_HFP\_AG\_CODEC\_MSBC 0x02

[ 42](group__bt__hfp__ag.md#ga8a833c4b11dc9e8fd08a73a2af418d83)#define BT\_HFP\_AG\_CODEC\_LC3\_SWB 0x03

43

44struct bt\_hfp\_ag;

45

[ 47](structbt__hfp__ag__cb.md)struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) {

[ 55](structbt__hfp__ag__cb.md#a1468a8757c6809ea29fa66983303284f) void (\*[connected](structbt__hfp__ag__cb.md#a1468a8757c6809ea29fa66983303284f))(struct bt\_hfp\_ag \*ag);

[ 64](structbt__hfp__ag__cb.md#af9c53ab021dbbf1017d71895581960c4) void (\*[disconnected](structbt__hfp__ag__cb.md#af9c53ab021dbbf1017d71895581960c4))(struct bt\_hfp\_ag \*ag);

[ 73](structbt__hfp__ag__cb.md#aac2b1ff4d80361e0e5eea2481027b4cf) void (\*[sco\_connected](structbt__hfp__ag__cb.md#aac2b1ff4d80361e0e5eea2481027b4cf))(struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn);

[ 82](structbt__hfp__ag__cb.md#ab2f62feda2c535db446d55a5f56922f9) void (\*[sco\_disconnected](structbt__hfp__ag__cb.md#ab2f62feda2c535db446d55a5f56922f9))(struct bt\_hfp\_ag \*ag);

83

[ 96](structbt__hfp__ag__cb.md#af335450c5e63139485fa5a131814d650) int (\*[memory\_dial](structbt__hfp__ag__cb.md#af335450c5e63139485fa5a131814d650))(struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number);

97

[ 106](structbt__hfp__ag__cb.md#a967407f8869798b99287740e19ea215b) void (\*[outgoing](structbt__hfp__ag__cb.md#a967407f8869798b99287740e19ea215b))(struct bt\_hfp\_ag \*ag, const char \*number);

107

[ 116](structbt__hfp__ag__cb.md#adea86dd7d3b5b3ecabd093bace2de1fc) void (\*[incoming](structbt__hfp__ag__cb.md#adea86dd7d3b5b3ecabd093bace2de1fc))(struct bt\_hfp\_ag \*ag, const char \*number);

117

[ 126](structbt__hfp__ag__cb.md#acae15cb697a20b6ca292d1f7f32ae0db) void (\*[ringing](structbt__hfp__ag__cb.md#acae15cb697a20b6ca292d1f7f32ae0db))(struct bt\_hfp\_ag \*ag, bool in\_band);

127

[ 135](structbt__hfp__ag__cb.md#a149ddc0677064aa85bf3fd0fd43f922c) void (\*[accept](structbt__hfp__ag__cb.md#a149ddc0677064aa85bf3fd0fd43f922c))(struct bt\_hfp\_ag \*ag);

136

[ 144](structbt__hfp__ag__cb.md#a9b857cdfd8b29f2bc08013b7eb62081b) void (\*[reject](structbt__hfp__ag__cb.md#a9b857cdfd8b29f2bc08013b7eb62081b))(struct bt\_hfp\_ag \*ag);

145

[ 153](structbt__hfp__ag__cb.md#aa00e1cb683e8cbe05483204649604e53) void (\*[terminate](structbt__hfp__ag__cb.md#aa00e1cb683e8cbe05483204649604e53))(struct bt\_hfp\_ag \*ag);

154

[ 162](structbt__hfp__ag__cb.md#a2f15172060cc5d225894be5c8311610b) void (\*[codec](structbt__hfp__ag__cb.md#a2f15172060cc5d225894be5c8311610b))(struct bt\_hfp\_ag \*ag, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ids);

163};

164

[ 174](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5)int [bt\_hfp\_ag\_register](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5)(struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) \*cb);

175

[ 186](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014)int [bt\_hfp\_ag\_connect](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014)(struct bt\_conn \*conn, struct bt\_hfp\_ag \*\*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

187

[ 196](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a)int [bt\_hfp\_ag\_disconnect](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a)(struct bt\_hfp\_ag \*ag);

197

[ 207](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793)int [bt\_hfp\_ag\_remote\_incoming](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793)(struct bt\_hfp\_ag \*ag, const char \*number);

208

[ 217](group__bt__hfp__ag.md#ga7d9f25c3dfbac0af8e24b7d998635490)int [bt\_hfp\_ag\_reject](group__bt__hfp__ag.md#ga7d9f25c3dfbac0af8e24b7d998635490)(struct bt\_hfp\_ag \*ag);

218

[ 227](group__bt__hfp__ag.md#ga331262bc9024998435bf5f9154dddffc)int [bt\_hfp\_ag\_accept](group__bt__hfp__ag.md#ga331262bc9024998435bf5f9154dddffc)(struct bt\_hfp\_ag \*ag);

228

[ 237](group__bt__hfp__ag.md#gaee0bb2269de783909e1c0d1658653047)int [bt\_hfp\_ag\_terminate](group__bt__hfp__ag.md#gaee0bb2269de783909e1c0d1658653047)(struct bt\_hfp\_ag \*ag);

238

[ 248](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd)int [bt\_hfp\_ag\_outgoing](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd)(struct bt\_hfp\_ag \*ag, const char \*number);

249

[ 258](group__bt__hfp__ag.md#gaff92b4176aeaf9781e97b1b8d34efeb9)int [bt\_hfp\_ag\_remote\_ringing](group__bt__hfp__ag.md#gaff92b4176aeaf9781e97b1b8d34efeb9)(struct bt\_hfp\_ag \*ag);

259

[ 268](group__bt__hfp__ag.md#ga4db1d508bebe6d468b498f328af70e9b)int [bt\_hfp\_ag\_remote\_reject](group__bt__hfp__ag.md#ga4db1d508bebe6d468b498f328af70e9b)(struct bt\_hfp\_ag \*ag);

269

[ 278](group__bt__hfp__ag.md#ga9770c356e5003294f7c325ef7014c52a)int [bt\_hfp\_ag\_remote\_accept](group__bt__hfp__ag.md#ga9770c356e5003294f7c325ef7014c52a)(struct bt\_hfp\_ag \*ag);

279

[ 288](group__bt__hfp__ag.md#ga1c115592d04ebdd208f67ed4bfaf056b)int [bt\_hfp\_ag\_remote\_terminate](group__bt__hfp__ag.md#ga1c115592d04ebdd208f67ed4bfaf056b)(struct bt\_hfp\_ag \*ag);

289

290#ifdef \_\_cplusplus

291}

292#endif

293

297

298#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HFP\_HF\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_hfp\_ag\_remote\_terminate](group__bt__hfp__ag.md#ga1c115592d04ebdd208f67ed4bfaf056b)

int bt\_hfp\_ag\_remote\_terminate(struct bt\_hfp\_ag \*ag)

Notify HFP Unit that the remote terminates the active/hold call.

[bt\_hfp\_ag\_accept](group__bt__hfp__ag.md#ga331262bc9024998435bf5f9154dddffc)

int bt\_hfp\_ag\_accept(struct bt\_hfp\_ag \*ag)

Accept the incoming call.

[bt\_hfp\_ag\_indicator](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810)

bt\_hfp\_ag\_indicator

**Definition** hfp\_ag.h:28

[bt\_hfp\_ag\_register](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5)

int bt\_hfp\_ag\_register(struct bt\_hfp\_ag\_cb \*cb)

Register HFP AG profile.

[bt\_hfp\_ag\_remote\_incoming](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793)

int bt\_hfp\_ag\_remote\_incoming(struct bt\_hfp\_ag \*ag, const char \*number)

Notify HFP Unit of an incoming call.

[bt\_hfp\_ag\_remote\_reject](group__bt__hfp__ag.md#ga4db1d508bebe6d468b498f328af70e9b)

int bt\_hfp\_ag\_remote\_reject(struct bt\_hfp\_ag \*ag)

Notify HFP Unit that the remote rejects the call.

[bt\_hfp\_ag\_outgoing](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd)

int bt\_hfp\_ag\_outgoing(struct bt\_hfp\_ag \*ag, const char \*number)

Dial a call.

[bt\_hfp\_ag\_connect](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014)

int bt\_hfp\_ag\_connect(struct bt\_conn \*conn, struct bt\_hfp\_ag \*\*ag, uint8\_t channel)

Create the hfp ag session.

[bt\_hfp\_ag\_reject](group__bt__hfp__ag.md#ga7d9f25c3dfbac0af8e24b7d998635490)

int bt\_hfp\_ag\_reject(struct bt\_hfp\_ag \*ag)

Reject the incoming call.

[bt\_hfp\_ag\_remote\_accept](group__bt__hfp__ag.md#ga9770c356e5003294f7c325ef7014c52a)

int bt\_hfp\_ag\_remote\_accept(struct bt\_hfp\_ag \*ag)

Notify HFP Unit that the remote accepts the call.

[bt\_hfp\_ag\_disconnect](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a)

int bt\_hfp\_ag\_disconnect(struct bt\_hfp\_ag \*ag)

Disconnect the hfp ag session.

[bt\_hfp\_ag\_terminate](group__bt__hfp__ag.md#gaee0bb2269de783909e1c0d1658653047)

int bt\_hfp\_ag\_terminate(struct bt\_hfp\_ag \*ag)

Terminate the active/hold call.

[bt\_hfp\_ag\_remote\_ringing](group__bt__hfp__ag.md#gaff92b4176aeaf9781e97b1b8d34efeb9)

int bt\_hfp\_ag\_remote\_ringing(struct bt\_hfp\_ag \*ag)

Notify HFP Unit that the remote starts ringing.

[BT\_HFP\_AG\_SERVICE\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234)

@ BT\_HFP\_AG\_SERVICE\_IND

**Definition** hfp\_ag.h:29

[BT\_HFP\_AG\_CALL\_SETUP\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5)

@ BT\_HFP\_AG\_CALL\_SETUP\_IND

**Definition** hfp\_ag.h:31

[BT\_HFP\_AG\_CALL\_HELD\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b)

@ BT\_HFP\_AG\_CALL\_HELD\_IND

**Definition** hfp\_ag.h:32

[BT\_HFP\_AG\_SIGNAL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493)

@ BT\_HFP\_AG\_SIGNAL\_IND

**Definition** hfp\_ag.h:33

[BT\_HFP\_AG\_BATTERY\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609)

@ BT\_HFP\_AG\_BATTERY\_IND

**Definition** hfp\_ag.h:35

[BT\_HFP\_AG\_CALL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d)

@ BT\_HFP\_AG\_CALL\_IND

**Definition** hfp\_ag.h:30

[BT\_HFP\_AG\_ROAM\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863)

@ BT\_HFP\_AG\_ROAM\_IND

**Definition** hfp\_ag.h:34

[BT\_HFP\_AG\_IND\_MAX](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)

@ BT\_HFP\_AG\_IND\_MAX

**Definition** hfp\_ag.h:36

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md)

HFP profile AG application callback.

**Definition** hfp\_ag.h:47

[bt\_hfp\_ag\_cb::connected](structbt__hfp__ag__cb.md#a1468a8757c6809ea29fa66983303284f)

void(\* connected)(struct bt\_hfp\_ag \*ag)

HF AG connected callback to application.

**Definition** hfp\_ag.h:55

[bt\_hfp\_ag\_cb::accept](structbt__hfp__ag__cb.md#a149ddc0677064aa85bf3fd0fd43f922c)

void(\* accept)(struct bt\_hfp\_ag \*ag)

HF call accept Callback.

**Definition** hfp\_ag.h:135

[bt\_hfp\_ag\_cb::codec](structbt__hfp__ag__cb.md#a2f15172060cc5d225894be5c8311610b)

void(\* codec)(struct bt\_hfp\_ag \*ag, uint32\_t ids)

Supported codec Ids callback.

**Definition** hfp\_ag.h:162

[bt\_hfp\_ag\_cb::outgoing](structbt__hfp__ag__cb.md#a967407f8869798b99287740e19ea215b)

void(\* outgoing)(struct bt\_hfp\_ag \*ag, const char \*number)

HF outgoing Callback.

**Definition** hfp\_ag.h:106

[bt\_hfp\_ag\_cb::reject](structbt__hfp__ag__cb.md#a9b857cdfd8b29f2bc08013b7eb62081b)

void(\* reject)(struct bt\_hfp\_ag \*ag)

HF call reject Callback.

**Definition** hfp\_ag.h:144

[bt\_hfp\_ag\_cb::terminate](structbt__hfp__ag__cb.md#aa00e1cb683e8cbe05483204649604e53)

void(\* terminate)(struct bt\_hfp\_ag \*ag)

HF call terminate Callback.

**Definition** hfp\_ag.h:153

[bt\_hfp\_ag\_cb::sco\_connected](structbt__hfp__ag__cb.md#aac2b1ff4d80361e0e5eea2481027b4cf)

void(\* sco\_connected)(struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn)

HF SCO/eSCO connected Callback.

**Definition** hfp\_ag.h:73

[bt\_hfp\_ag\_cb::sco\_disconnected](structbt__hfp__ag__cb.md#ab2f62feda2c535db446d55a5f56922f9)

void(\* sco\_disconnected)(struct bt\_hfp\_ag \*ag)

HF SCO/eSCO disconnected Callback.

**Definition** hfp\_ag.h:82

[bt\_hfp\_ag\_cb::ringing](structbt__hfp__ag__cb.md#acae15cb697a20b6ca292d1f7f32ae0db)

void(\* ringing)(struct bt\_hfp\_ag \*ag, bool in\_band)

HF ringing Callback.

**Definition** hfp\_ag.h:126

[bt\_hfp\_ag\_cb::incoming](structbt__hfp__ag__cb.md#adea86dd7d3b5b3ecabd093bace2de1fc)

void(\* incoming)(struct bt\_hfp\_ag \*ag, const char \*number)

HF incoming Callback.

**Definition** hfp\_ag.h:116

[bt\_hfp\_ag\_cb::memory\_dial](structbt__hfp__ag__cb.md#af335450c5e63139485fa5a131814d650)

int(\* memory\_dial)(struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number)

HF memory dialing request Callback.

**Definition** hfp\_ag.h:96

[bt\_hfp\_ag\_cb::disconnected](structbt__hfp__ag__cb.md#af9c53ab021dbbf1017d71895581960c4)

void(\* disconnected)(struct bt\_hfp\_ag \*ag)

HF disconnected callback to application.

**Definition** hfp\_ag.h:64

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_ag.h](hfp__ag_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
