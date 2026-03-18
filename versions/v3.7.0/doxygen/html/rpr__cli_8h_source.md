---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rpr__cli_8h_source.html
original_path: doxygen/html/rpr__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpr\_cli.h

[Go to the documentation of this file.](rpr__cli_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_CLI\_H\_\_

8#define ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_CLI\_H\_\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

12#include <[zephyr/bluetooth/mesh/rpr.h](rpr_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

23

[ 29](group__bt__mesh__rpr__cli.md#gafa00eb1bff764a4ab723bb978b459297)#define BT\_MESH\_RPR\_SCAN\_MAX\_DEVS\_ANY 0

30

31struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md);

32

[ 39](group__bt__mesh__rpr__cli.md#ga83d18bb8d1108db9f7e54cd2cad32a99)#define BT\_MESH\_MODEL\_RPR\_CLI(\_cli) \

40 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_CLI, \

41 \_bt\_mesh\_rpr\_cli\_op, NULL, \_cli, &\_bt\_mesh\_rpr\_cli\_cb)

42

[ 44](structbt__mesh__rpr__scan__status.md)struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) {

[ 46](structbt__mesh__rpr__scan__status.md#a2e2023bc7dcb31ae8716203b726f7ebb) enum [bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90) [status](structbt__mesh__rpr__scan__status.md#a2e2023bc7dcb31ae8716203b726f7ebb);

[ 48](structbt__mesh__rpr__scan__status.md#ac9e5f2e4db9fc9b04dddd2687a712ff8) enum [bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291) [scan](structbt__mesh__rpr__scan__status.md#ac9e5f2e4db9fc9b04dddd2687a712ff8);

[ 50](structbt__mesh__rpr__scan__status.md#ac7fc9a15127dc1eae44d2ec610efd5be) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_devs](structbt__mesh__rpr__scan__status.md#ac7fc9a15127dc1eae44d2ec610efd5be);

[ 52](structbt__mesh__rpr__scan__status.md#a8d062579fb074ded769bf367e0287052) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [timeout](structbt__mesh__rpr__scan__status.md#a8d062579fb074ded769bf367e0287052);

53};

54

[ 56](structbt__mesh__rpr__caps.md)struct [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) {

[ 58](structbt__mesh__rpr__caps.md#af14cce916d388c18ca33d4fc9adb36b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_devs](structbt__mesh__rpr__caps.md#af14cce916d388c18ca33d4fc9adb36b5);

[ 60](structbt__mesh__rpr__caps.md#a2de75ef667698a6094051a71ba9808ce) bool [active\_scan](structbt__mesh__rpr__caps.md#a2de75ef667698a6094051a71ba9808ce);

61};

62

[ 64](structbt__mesh__rpr__cli.md)struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) {

[ 75](structbt__mesh__rpr__cli.md#a32b3c63218b506d1bc5759640cb3fb81) void (\*[scan\_report](structbt__mesh__rpr__cli.md#a32b3c63218b506d1bc5759640cb3fb81))(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

76 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*[srv](structbt__mesh__rpr__cli.md#a8f5eea4cbb042f8a83050ad4ebfc64b7),

77 struct [bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md) \*unprov,

78 struct [net\_buf\_simple](structnet__buf__simple.md) \*adv\_data);

79

80 /\* Internal parameters \*/

81

[ 82](structbt__mesh__rpr__cli.md#a9cc5b67937ec8e0ff93ddfb55cb11528) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [scan\_ack\_ctx](structbt__mesh__rpr__cli.md#a9cc5b67937ec8e0ff93ddfb55cb11528);

[ 83](structbt__mesh__rpr__cli.md#a0e5a8d697b87f5f05bbce0aaa8c1fb1a) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [prov\_ack\_ctx](structbt__mesh__rpr__cli.md#a0e5a8d697b87f5f05bbce0aaa8c1fb1a);

84

85 struct {

[ 86](structbt__mesh__rpr__cli.md#a64b12ca2ef9e47723c77a8af41eb0f89) struct [k\_work\_delayable](structk__work__delayable.md) [timeout](structbt__mesh__rpr__cli.md#a64b12ca2ef9e47723c77a8af41eb0f89);

[ 87](structbt__mesh__rpr__cli.md#a8f5eea4cbb042f8a83050ad4ebfc64b7) struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) [srv](structbt__mesh__rpr__cli.md#a8f5eea4cbb042f8a83050ad4ebfc64b7);

[ 88](structbt__mesh__rpr__cli.md#af03b9edb0a205e92182234c7a1355e0c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [time](structbt__mesh__rpr__cli.md#af03b9edb0a205e92182234c7a1355e0c);

[ 89](structbt__mesh__rpr__cli.md#a68eaadc451224e155227d14102ff0a54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_pdu](structbt__mesh__rpr__cli.md#a68eaadc451224e155227d14102ff0a54);

[ 90](structbt__mesh__rpr__cli.md#a8493c4b3c1e30cc0a6f58b765adb2e37) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_pdu](structbt__mesh__rpr__cli.md#a8493c4b3c1e30cc0a6f58b765adb2e37);

[ 91](structbt__mesh__rpr__cli.md#aa29cbb7e19cc659ce13b0b98604c93d5) enum [bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43) [state](structbt__mesh__rpr__cli.md#aa29cbb7e19cc659ce13b0b98604c93d5);

[ 92](structbt__mesh__rpr__cli.md#ad69049681d611aa48be4942745fb89a7) } [link](structbt__mesh__rpr__cli.md#ad69049681d611aa48be4942745fb89a7);

93

[ 94](structbt__mesh__rpr__cli.md#a188c9e610035b7225411b45733be5a85) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__rpr__cli.md#a188c9e610035b7225411b45733be5a85);

95};

96

[ 105](group__bt__mesh__rpr__cli.md#ga1cfef51b2d6389fb4b125cba4d21d739)int [bt\_mesh\_rpr\_scan\_caps\_get](group__bt__mesh__rpr__cli.md#ga1cfef51b2d6389fb4b125cba4d21d739)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

106 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

107 struct [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md) \*caps);

108

[ 117](group__bt__mesh__rpr__cli.md#ga03602b651a5bf1c88dac810e272ea142)int [bt\_mesh\_rpr\_scan\_get](group__bt__mesh__rpr__cli.md#ga03602b651a5bf1c88dac810e272ea142)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

118 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

119 struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status);

120

[ 144](group__bt__mesh__rpr__cli.md#gaf404922f2340442490f1ab29191f43e3)int [bt\_mesh\_rpr\_scan\_start](group__bt__mesh__rpr__cli.md#gaf404922f2340442490f1ab29191f43e3)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

145 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

146 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timeout,

147 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_devs,

148 struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status);

149

[ 188](group__bt__mesh__rpr__cli.md#ga934104e6ee33ba8c228fde4c68e752e1)int [bt\_mesh\_rpr\_scan\_start\_ext](group__bt__mesh__rpr__cli.md#ga934104e6ee33ba8c228fde4c68e752e1)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

189 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

190 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) timeout,

191 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ad\_types, size\_t ad\_count);

192

[ 201](group__bt__mesh__rpr__cli.md#ga007aa9b409d1370ed04c45efccdf0408)int [bt\_mesh\_rpr\_scan\_stop](group__bt__mesh__rpr__cli.md#ga007aa9b409d1370ed04c45efccdf0408)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

202 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

203 struct [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md) \*status);

204

[ 213](group__bt__mesh__rpr__cli.md#ga36de5bfca8ba9b03a99625fbc1734839)int [bt\_mesh\_rpr\_link\_get](group__bt__mesh__rpr__cli.md#ga36de5bfca8ba9b03a99625fbc1734839)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

214 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

215 struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \*rsp);

216

[ 225](group__bt__mesh__rpr__cli.md#gaa240b465a1ed5796b190d241e484d467)int [bt\_mesh\_rpr\_link\_close](group__bt__mesh__rpr__cli.md#gaa240b465a1ed5796b190d241e484d467)(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli,

226 const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv,

227 struct [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) \*rsp);

228

[ 233](group__bt__mesh__rpr__cli.md#ga93aca19586795801eefa04ffc4635533)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_rpr\_cli\_timeout\_get](group__bt__mesh__rpr__cli.md#ga93aca19586795801eefa04ffc4635533)(void);

234

[ 242](group__bt__mesh__rpr__cli.md#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)void [bt\_mesh\_rpr\_cli\_timeout\_set](group__bt__mesh__rpr__cli.md#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

243

245extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_rpr\_cli\_op[];

246extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_rpr\_cli\_cb;

248

250

251#ifdef \_\_cplusplus

252}

253#endif

254

255#endif /\* ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_CLI\_H\_\_ \*/

[access.h](access_8h.md)

Access layer APIs.

[bt\_mesh\_rpr\_scan\_stop](group__bt__mesh__rpr__cli.md#ga007aa9b409d1370ed04c45efccdf0408)

int bt\_mesh\_rpr\_scan\_stop(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_scan\_status \*status)

Stop any ongoing scanning on the Remote Provisioning Server.

[bt\_mesh\_rpr\_scan\_get](group__bt__mesh__rpr__cli.md#ga03602b651a5bf1c88dac810e272ea142)

int bt\_mesh\_rpr\_scan\_get(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_scan\_status \*status)

Get current scanning state of Remote Provisioning Server.

[bt\_mesh\_rpr\_scan\_caps\_get](group__bt__mesh__rpr__cli.md#ga1cfef51b2d6389fb4b125cba4d21d739)

int bt\_mesh\_rpr\_scan\_caps\_get(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_caps \*caps)

Get scanning capabilities of Remote Provisioning Server.

[bt\_mesh\_rpr\_link\_get](group__bt__mesh__rpr__cli.md#ga36de5bfca8ba9b03a99625fbc1734839)

int bt\_mesh\_rpr\_link\_get(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_link \*rsp)

Get the current link status of the Remote Provisioning Server.

[bt\_mesh\_rpr\_cli\_timeout\_set](group__bt__mesh__rpr__cli.md#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)

void bt\_mesh\_rpr\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[bt\_mesh\_rpr\_scan\_start\_ext](group__bt__mesh__rpr__cli.md#ga934104e6ee33ba8c228fde4c68e752e1)

int bt\_mesh\_rpr\_scan\_start\_ext(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, const uint8\_t uuid[16], uint8\_t timeout, const uint8\_t \*ad\_types, size\_t ad\_count)

Start extended scanning for unprovisioned devices.

[bt\_mesh\_rpr\_cli\_timeout\_get](group__bt__mesh__rpr__cli.md#ga93aca19586795801eefa04ffc4635533)

int32\_t bt\_mesh\_rpr\_cli\_timeout\_get(void)

Get the current transmission timeout value.

[bt\_mesh\_rpr\_link\_close](group__bt__mesh__rpr__cli.md#gaa240b465a1ed5796b190d241e484d467)

int bt\_mesh\_rpr\_link\_close(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_link \*rsp)

Close any open link on the Remote Provisioning Server.

[bt\_mesh\_rpr\_scan\_start](group__bt__mesh__rpr__cli.md#gaf404922f2340442490f1ab29191f43e3)

int bt\_mesh\_rpr\_scan\_start(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, const uint8\_t uuid[16], uint8\_t timeout, uint8\_t max\_devs, struct bt\_mesh\_rpr\_scan\_status \*status)

Start scanning for unprovisioned devices.

[bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43)

bt\_mesh\_rpr\_link\_state

**Definition** rpr.h:67

[bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90)

bt\_mesh\_rpr\_status

**Definition** rpr.h:37

[bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291)

bt\_mesh\_rpr\_scan

**Definition** rpr.h:52

[kernel.h](kernel_8h.md)

Public kernel APIs.

[rpr.h](rpr_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:809

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:887

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md)

Remote Provisioning Server scanning capabilities.

**Definition** rpr\_cli.h:56

[bt\_mesh\_rpr\_caps::active\_scan](structbt__mesh__rpr__caps.md#a2de75ef667698a6094051a71ba9808ce)

bool active\_scan

Supports active scan.

**Definition** rpr\_cli.h:60

[bt\_mesh\_rpr\_caps::max\_devs](structbt__mesh__rpr__caps.md#af14cce916d388c18ca33d4fc9adb36b5)

uint8\_t max\_devs

Max number of scannable devices.

**Definition** rpr\_cli.h:58

[bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md)

Remote Provisioning Client model instance.

**Definition** rpr\_cli.h:64

[bt\_mesh\_rpr\_cli::prov\_ack\_ctx](structbt__mesh__rpr__cli.md#a0e5a8d697b87f5f05bbce0aaa8c1fb1a)

struct bt\_mesh\_msg\_ack\_ctx prov\_ack\_ctx

**Definition** rpr\_cli.h:83

[bt\_mesh\_rpr\_cli::mod](structbt__mesh__rpr__cli.md#a188c9e610035b7225411b45733be5a85)

const struct bt\_mesh\_model \* mod

**Definition** rpr\_cli.h:94

[bt\_mesh\_rpr\_cli::scan\_report](structbt__mesh__rpr__cli.md#a32b3c63218b506d1bc5759640cb3fb81)

void(\* scan\_report)(struct bt\_mesh\_rpr\_cli \*cli, const struct bt\_mesh\_rpr\_node \*srv, struct bt\_mesh\_rpr\_unprov \*unprov, struct net\_buf\_simple \*adv\_data)

Scan report callback.

**Definition** rpr\_cli.h:75

[bt\_mesh\_rpr\_cli::timeout](structbt__mesh__rpr__cli.md#a64b12ca2ef9e47723c77a8af41eb0f89)

struct k\_work\_delayable timeout

**Definition** rpr\_cli.h:86

[bt\_mesh\_rpr\_cli::tx\_pdu](structbt__mesh__rpr__cli.md#a68eaadc451224e155227d14102ff0a54)

uint8\_t tx\_pdu

**Definition** rpr\_cli.h:89

[bt\_mesh\_rpr\_cli::rx\_pdu](structbt__mesh__rpr__cli.md#a8493c4b3c1e30cc0a6f58b765adb2e37)

uint8\_t rx\_pdu

**Definition** rpr\_cli.h:90

[bt\_mesh\_rpr\_cli::srv](structbt__mesh__rpr__cli.md#a8f5eea4cbb042f8a83050ad4ebfc64b7)

struct bt\_mesh\_rpr\_node srv

**Definition** rpr\_cli.h:87

[bt\_mesh\_rpr\_cli::scan\_ack\_ctx](structbt__mesh__rpr__cli.md#a9cc5b67937ec8e0ff93ddfb55cb11528)

struct bt\_mesh\_msg\_ack\_ctx scan\_ack\_ctx

**Definition** rpr\_cli.h:82

[bt\_mesh\_rpr\_cli::state](structbt__mesh__rpr__cli.md#aa29cbb7e19cc659ce13b0b98604c93d5)

enum bt\_mesh\_rpr\_link\_state state

**Definition** rpr\_cli.h:91

[bt\_mesh\_rpr\_cli::link](structbt__mesh__rpr__cli.md#ad69049681d611aa48be4942745fb89a7)

struct bt\_mesh\_rpr\_cli::@146376344033107143324154277353003224165264331171 link

[bt\_mesh\_rpr\_cli::time](structbt__mesh__rpr__cli.md#af03b9edb0a205e92182234c7a1355e0c)

uint8\_t time

**Definition** rpr\_cli.h:88

[bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md)

Remote Provisioning Link status.

**Definition** rpr.h:103

[bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md)

Remote provisioning actor, as seen across the mesh.

**Definition** rpr.h:76

[bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md)

Scan status response.

**Definition** rpr\_cli.h:44

[bt\_mesh\_rpr\_scan\_status::status](structbt__mesh__rpr__scan__status.md#a2e2023bc7dcb31ae8716203b726f7ebb)

enum bt\_mesh\_rpr\_status status

Current scan status.

**Definition** rpr\_cli.h:46

[bt\_mesh\_rpr\_scan\_status::timeout](structbt__mesh__rpr__scan__status.md#a8d062579fb074ded769bf367e0287052)

uint8\_t timeout

Seconds remaining of the scan.

**Definition** rpr\_cli.h:52

[bt\_mesh\_rpr\_scan\_status::max\_devs](structbt__mesh__rpr__scan__status.md#ac7fc9a15127dc1eae44d2ec610efd5be)

uint8\_t max\_devs

Max number of devices to report in current scan.

**Definition** rpr\_cli.h:50

[bt\_mesh\_rpr\_scan\_status::scan](structbt__mesh__rpr__scan__status.md#ac9e5f2e4db9fc9b04dddd2687a712ff8)

enum bt\_mesh\_rpr\_scan scan

Current scan state.

**Definition** rpr\_cli.h:48

[bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md)

Unprovisioned device.

**Definition** rpr.h:86

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3908

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [rpr\_cli.h](rpr__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
