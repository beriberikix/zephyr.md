---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/blob__cli_8h_source.html
original_path: doxygen/html/blob__cli_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob\_cli.h

[Go to the documentation of this file.](blob__cli_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_CLI\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_CLI\_H\_

9

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11

12#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

13#include <[zephyr/bluetooth/mesh/blob.h](blob_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

25struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md);

26

[ 33](group__bt__mesh__blob__cli.md#ga882e9cec348625c7990de4ee5eb7ed5a)#define BT\_MESH\_MODEL\_BLOB\_CLI(\_cli) \

34 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_BLOB\_CLI, \_bt\_mesh\_blob\_cli\_op, \

35 NULL, \_cli, &\_bt\_mesh\_blob\_cli\_cb)

36

[ 40](structbt__mesh__blob__target__pull.md)struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) {

[ 42](structbt__mesh__blob__target__pull.md#a9234ee3246890285b5cd30c32866b718) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [block\_report\_timestamp](structbt__mesh__blob__target__pull.md#a9234ee3246890285b5cd30c32866b718);

43

[ 45](structbt__mesh__blob__target__pull.md#a19fc9a8a0b5202887e7fd73028805774) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [missing](structbt__mesh__blob__target__pull.md#a19fc9a8a0b5202887e7fd73028805774)[[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)([CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e), 8)];

46};

47

[ 49](structbt__mesh__blob__target.md)struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) {

[ 51](structbt__mesh__blob__target.md#aca0f3cabb5c457cfb11a4bc71c3bea85) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [n](structbt__mesh__blob__target.md#aca0f3cabb5c457cfb11a4bc71c3bea85);

52

[ 54](structbt__mesh__blob__target.md#ab4c032f92a4ec12e4bbd6fa84139c085) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__blob__target.md#ab4c032f92a4ec12e4bbd6fa84139c085);

55

[ 59](structbt__mesh__blob__target.md#a0498f23d640af4b006398d5482fbaa53) struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) \*[pull](structbt__mesh__blob__target.md#a0498f23d640af4b006398d5482fbaa53);

60

[ 62](structbt__mesh__blob__target.md#a62b5a5be44d52ebf09421de57933459d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__mesh__blob__target.md#a62b5a5be44d52ebf09421de57933459d);

63

[ 64](structbt__mesh__blob__target.md#a711a031e841bb54c4985d02a81c6846a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [procedure\_complete](structbt__mesh__blob__target.md#a711a031e841bb54c4985d02a81c6846a):1, /\* Procedure has been completed. \*/

[ 65](structbt__mesh__blob__target.md#a4eef4809023e8d4a4ee8beece5e83160) [acked](structbt__mesh__blob__target.md#a4eef4809023e8d4a4ee8beece5e83160):1, /\* Message has been acknowledged. Not used when sending. \*/

[ 66](structbt__mesh__blob__target.md#a3e14f4518ee054754dfa50d8070c1725) [timedout](structbt__mesh__blob__target.md#a3e14f4518ee054754dfa50d8070c1725):1, /\* Target node didn't respond after specified timeout. \*/

[ 67](structbt__mesh__blob__target.md#a7aa1066dbeee5ba4a5be5aa14d61d4d1) [skip](structbt__mesh__blob__target.md#a7aa1066dbeee5ba4a5be5aa14d61d4d1):1; /\* Skip Target node from broadcast. \*/

68};

69

[ 77](structbt__mesh__blob__xfer__info.md)struct [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md) {

[ 79](structbt__mesh__blob__xfer__info.md#aaeda1f5688bfb3cc3708e3797f3190a5) enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) [status](structbt__mesh__blob__xfer__info.md#aaeda1f5688bfb3cc3708e3797f3190a5);

80

[ 82](structbt__mesh__blob__xfer__info.md#a6cbb21582332cb23125624db5a02731a) enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) [mode](structbt__mesh__blob__xfer__info.md#a6cbb21582332cb23125624db5a02731a);

83

[ 85](structbt__mesh__blob__xfer__info.md#a6a8686872018ceb6e4e9fc52eaff5b9e) enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) [phase](structbt__mesh__blob__xfer__info.md#a6a8686872018ceb6e4e9fc52eaff5b9e);

86

[ 88](structbt__mesh__blob__xfer__info.md#a3a19a5f387b53dd32429c9e76e53a87f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [id](structbt__mesh__blob__xfer__info.md#a3a19a5f387b53dd32429c9e76e53a87f);

89

[ 91](structbt__mesh__blob__xfer__info.md#ac03d3ad7a618ee67f9bd7f1d52019cb7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structbt__mesh__blob__xfer__info.md#ac03d3ad7a618ee67f9bd7f1d52019cb7);

92

[ 94](structbt__mesh__blob__xfer__info.md#ad09a0e80202b4953788fcade5788f0ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [block\_size\_log](structbt__mesh__blob__xfer__info.md#ad09a0e80202b4953788fcade5788f0ef);

95

[ 97](structbt__mesh__blob__xfer__info.md#ae24ed28faaef6187850cb0f04da2b8c7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu\_size](structbt__mesh__blob__xfer__info.md#ae24ed28faaef6187850cb0f04da2b8c7);

98

[ 100](structbt__mesh__blob__xfer__info.md#a8825fba3258805db956b099ddfa19f9f) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[missing\_blocks](structbt__mesh__blob__xfer__info.md#a8825fba3258805db956b099ddfa19f9f);

101};

102

[ 104](structbt__mesh__blob__cli__inputs.md)struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) {

[ 108](structbt__mesh__blob__cli__inputs.md#a835a539b307c659f57da6c20e9223ed1) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [targets](structbt__mesh__blob__cli__inputs.md#a835a539b307c659f57da6c20e9223ed1);

109

[ 111](structbt__mesh__blob__cli__inputs.md#a7fb308f895c57b66b50e1ab060228cb3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__blob__cli__inputs.md#a7fb308f895c57b66b50e1ab060228cb3);

112

[ 117](structbt__mesh__blob__cli__inputs.md#ac204e179c2a6ea9cb672fc3c2f9ab017) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [group](structbt__mesh__blob__cli__inputs.md#ac204e179c2a6ea9cb672fc3c2f9ab017);

118

[ 120](structbt__mesh__blob__cli__inputs.md#adee5ecdba3adc4fe598483b1a160cafb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ttl](structbt__mesh__blob__cli__inputs.md#adee5ecdba3adc4fe598483b1a160cafb);

121

[ 135](structbt__mesh__blob__cli__inputs.md#a30fd3cd7a6df07f6aa90b85cdc6aea18) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout\_base](structbt__mesh__blob__cli__inputs.md#a30fd3cd7a6df07f6aa90b85cdc6aea18);

136};

137

[ 139](structbt__mesh__blob__cli__caps.md)struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) {

[ 141](structbt__mesh__blob__cli__caps.md#ae16411b1a36854d6f638a2bca1dc4c3b) size\_t [max\_size](structbt__mesh__blob__cli__caps.md#ae16411b1a36854d6f638a2bca1dc4c3b);

142

[ 144](structbt__mesh__blob__cli__caps.md#ac446317efdeca9edbb7df924d4e5a995) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [min\_block\_size\_log](structbt__mesh__blob__cli__caps.md#ac446317efdeca9edbb7df924d4e5a995);

145

[ 147](structbt__mesh__blob__cli__caps.md#a5d44b3b9bf7e47af2e6ba930b2826b15) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_block\_size\_log](structbt__mesh__blob__cli__caps.md#a5d44b3b9bf7e47af2e6ba930b2826b15);

148

[ 150](structbt__mesh__blob__cli__caps.md#a318c96b89597dfdf9b68fbc8b999af11) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_chunks](structbt__mesh__blob__cli__caps.md#a318c96b89597dfdf9b68fbc8b999af11);

151

[ 153](structbt__mesh__blob__cli__caps.md#ad149164240e7c20a57a28c25109079df) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_chunk\_size](structbt__mesh__blob__cli__caps.md#ad149164240e7c20a57a28c25109079df);

154

[ 156](structbt__mesh__blob__cli__caps.md#a89d6e1bbc55086cee410835edd6baf3a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu\_size](structbt__mesh__blob__cli__caps.md#a89d6e1bbc55086cee410835edd6baf3a);

157

[ 159](structbt__mesh__blob__cli__caps.md#a1c848a3a2a2ece3764df5cbf6cbfec6b) enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) [modes](structbt__mesh__blob__cli__caps.md#a1c848a3a2a2ece3764df5cbf6cbfec6b);

160};

161

[ 163](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073)enum [bt\_mesh\_blob\_cli\_state](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073) {

[ 165](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67) [BT\_MESH\_BLOB\_CLI\_STATE\_NONE](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67),

[ 167](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de) [BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de),

[ 169](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2) [BT\_MESH\_BLOB\_CLI\_STATE\_START](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2),

[ 171](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2) [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2),

[ 173](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9) [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9),

[ 175](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c) [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c),

[ 177](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96) [BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96),

[ 179](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646) [BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646),

[ 181](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9) [BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9),

[ 183](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c) [BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c),

184};

185

[ 190](structbt__mesh__blob__cli__cb.md)struct [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md) {

[ 202](structbt__mesh__blob__cli__cb.md#a58e749cadeb464299495ee74456c592c) void (\*[caps](structbt__mesh__blob__cli__cb.md#a58e749cadeb464299495ee74456c592c))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

203 const struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) \*[caps](structbt__mesh__blob__cli__cb.md#a58e749cadeb464299495ee74456c592c));

204

[ 215](structbt__mesh__blob__cli__cb.md#a26a5ebe87db105900b150f71d770234d) void (\*[lost\_target](structbt__mesh__blob__cli__cb.md#a26a5ebe87db105900b150f71d770234d))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

216 struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*target,

217 enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) reason);

218

[ 225](structbt__mesh__blob__cli__cb.md#a154a3308167eda4cd93ac28e379c52bc) void (\*[suspended](structbt__mesh__blob__cli__cb.md#a154a3308167eda4cd93ac28e379c52bc))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

226

[ 237](structbt__mesh__blob__cli__cb.md#a60bc49eab376b055a8c21099f86fdde7) void (\*[end](structbt__mesh__blob__cli__cb.md#a60bc49eab376b055a8c21099f86fdde7))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

238 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, bool success);

239

[ 249](structbt__mesh__blob__cli__cb.md#a4b01ef0ab0a367739a75751b57149546) void (\*[xfer\_progress](structbt__mesh__blob__cli__cb.md#a4b01ef0ab0a367739a75751b57149546))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

250 struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*target,

251 const struct [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md) \*info);

252

[ 259](structbt__mesh__blob__cli__cb.md#abb4a4d4d24bef076aad7ae56b08d23ed) void (\*[xfer\_progress\_complete](structbt__mesh__blob__cli__cb.md#abb4a4d4d24bef076aad7ae56b08d23ed))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

260};

261

263struct blob\_cli\_broadcast\_ctx {

265 void (\*[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d))(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst);

267 void (\*send\_complete)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst);

272 void (\*next)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

276 bool acked;

278 bool force\_unicast;

280 bool optional;

284 bool is\_inited;

285 /\* Defines a time in ms by which the broadcast API postpones sending the message to a next

286 \* target or completing the broadcast.

287 \*/

288 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) post\_send\_delay\_ms;

289};

291

[ 293](structbt__mesh__blob__cli.md)struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) {

[ 295](structbt__mesh__blob__cli.md#a6a0229165fe19af03a26e5cffa1e1486) const struct [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md) \*[cb](structbt__mesh__blob__cli.md#a6a0229165fe19af03a26e5cffa1e1486);

296

297 /\* Runtime state \*/

[ 298](structbt__mesh__blob__cli.md#ada23952593d2a498ed421895828f461f) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](structbt__mesh__blob__cli.md#ada23952593d2a498ed421895828f461f);

299

300 struct {

[ 301](structbt__mesh__blob__cli.md#a519aa0aa7aa66ca67cdf813fee1632c3) struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*[target](structbt__mesh__blob__cli.md#a519aa0aa7aa66ca67cdf813fee1632c3);

[ 302](structbt__mesh__blob__cli.md#a850d232b04118d7564537dc6763a476c) struct blob\_cli\_broadcast\_ctx [ctx](structbt__mesh__blob__cli.md#a850d232b04118d7564537dc6763a476c);

[ 303](structbt__mesh__blob__cli.md#add07e03f13b276fafabeb9cc4ba94d32) struct [k\_work\_delayable](structk__work__delayable.md) [retry](structbt__mesh__blob__cli.md#add07e03f13b276fafabeb9cc4ba94d32);

304 /\* Represents Client Timeout timer in a timestamp. Used in Pull mode only. \*/

[ 305](structbt__mesh__blob__cli.md#a850cc6f4426fec9dc9066953a1b992c8) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [cli\_timestamp](structbt__mesh__blob__cli.md#a850cc6f4426fec9dc9066953a1b992c8);

[ 306](structbt__mesh__blob__cli.md#a21b064cceace34605e42d5c295f12cd5) struct [k\_work\_delayable](structk__work__delayable.md) [complete](structbt__mesh__blob__cli.md#a21b064cceace34605e42d5c295f12cd5);

[ 307](structbt__mesh__blob__cli.md#a1778ae8975ed4b9bc67616e5a0bdf3a9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pending](structbt__mesh__blob__cli.md#a1778ae8975ed4b9bc67616e5a0bdf3a9);

[ 308](structbt__mesh__blob__cli.md#ab291086be3d9ecf03becd4200d783835) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retries](structbt__mesh__blob__cli.md#ab291086be3d9ecf03becd4200d783835);

[ 309](structbt__mesh__blob__cli.md#a85fdd17b04a06e880f20a0e2b1319ff0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sending](structbt__mesh__blob__cli.md#a85fdd17b04a06e880f20a0e2b1319ff0) : 1,

[ 310](structbt__mesh__blob__cli.md#a6d70ac26b7fec22dfdc21f479d867ef7) [cancelled](structbt__mesh__blob__cli.md#a6d70ac26b7fec22dfdc21f479d867ef7) : 1;

[ 311](structbt__mesh__blob__cli.md#a388183549ed5b1af0d2ac09263611a33) } [tx](structbt__mesh__blob__cli.md#a388183549ed5b1af0d2ac09263611a33);

312

[ 313](structbt__mesh__blob__cli.md#a49f0d79d76aaea785a5ad9160be40e8a) const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*[io](structbt__mesh__blob__cli.md#a49f0d79d76aaea785a5ad9160be40e8a);

[ 314](structbt__mesh__blob__cli.md#aa6c79f5476f96a35c731b63723b2c6cc) const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*[inputs](structbt__mesh__blob__cli.md#aa6c79f5476f96a35c731b63723b2c6cc);

[ 315](structbt__mesh__blob__cli.md#a9185cdadba15bce7b2bf2fcc6f85904a) const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*[xfer](structbt__mesh__blob__cli.md#a9185cdadba15bce7b2bf2fcc6f85904a);

[ 316](structbt__mesh__blob__cli.md#a2ffd91b68c0aab92f16d9fb4eac79f9d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [chunk\_interval\_ms](structbt__mesh__blob__cli.md#a2ffd91b68c0aab92f16d9fb4eac79f9d);

[ 317](structbt__mesh__blob__cli.md#a645fdb1f0efb281b1faae4692a3404f1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [block\_count](structbt__mesh__blob__cli.md#a645fdb1f0efb281b1faae4692a3404f1);

[ 318](structbt__mesh__blob__cli.md#aafaf644e30e10a8ad9ca6dc8b680eff6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chunk\_idx](structbt__mesh__blob__cli.md#aafaf644e30e10a8ad9ca6dc8b680eff6);

[ 319](structbt__mesh__blob__cli.md#aafe943fcada25f32b9a31b8d7586032a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu\_size](structbt__mesh__blob__cli.md#aafe943fcada25f32b9a31b8d7586032a);

[ 320](structbt__mesh__blob__cli.md#ab131637681a0cf0b3ceebad015b28726) enum [bt\_mesh\_blob\_cli\_state](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073) [state](structbt__mesh__blob__cli.md#ab131637681a0cf0b3ceebad015b28726);

[ 321](structbt__mesh__blob__cli.md#ac95970f7fd6b00fca284121394110250) struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) [block](structbt__mesh__blob__cli.md#ac95970f7fd6b00fca284121394110250);

[ 322](structbt__mesh__blob__cli.md#aa7713e6ad0183d18946646df7a5cb6ab) struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) [caps](structbt__mesh__blob__cli.md#aa7713e6ad0183d18946646df7a5cb6ab);

323};

324

[ 344](group__bt__mesh__blob__cli.md#gac401336775dc6274450d5e27ea1cd720)int [bt\_mesh\_blob\_cli\_caps\_get](group__bt__mesh__blob__cli.md#gac401336775dc6274450d5e27ea1cd720)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

345 const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs);

346

[ 368](group__bt__mesh__blob__cli.md#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)int [bt\_mesh\_blob\_cli\_send](group__bt__mesh__blob__cli.md#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

369 const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs,

370 const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer,

371 const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io);

372

[ 379](group__bt__mesh__blob__cli.md#ga78487f10fae6c87edaaf4e6ec8f7362c)int [bt\_mesh\_blob\_cli\_suspend](group__bt__mesh__blob__cli.md#ga78487f10fae6c87edaaf4e6ec8f7362c)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

380

[ 387](group__bt__mesh__blob__cli.md#ga5aed01e812215d153fdfafd6375cc453)int [bt\_mesh\_blob\_cli\_resume](group__bt__mesh__blob__cli.md#ga5aed01e812215d153fdfafd6375cc453)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

388

[ 393](group__bt__mesh__blob__cli.md#ga222c650657e9a7958b119d4dddd55783)void [bt\_mesh\_blob\_cli\_cancel](group__bt__mesh__blob__cli.md#ga222c650657e9a7958b119d4dddd55783)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

394

[ 407](group__bt__mesh__blob__cli.md#ga17a73cb313dbfc6652b4bcf638b9a30f)int [bt\_mesh\_blob\_cli\_xfer\_progress\_get](group__bt__mesh__blob__cli.md#ga17a73cb313dbfc6652b4bcf638b9a30f)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli,

408 const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs);

409

[ 416](group__bt__mesh__blob__cli.md#ga065196837cbf9d2626b5589ce2671441)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get](group__bt__mesh__blob__cli.md#ga065196837cbf9d2626b5589ce2671441)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

417

[ 425](group__bt__mesh__blob__cli.md#ga37bbc559b48ea8cfe7cb3ddf8cad24da)bool [bt\_mesh\_blob\_cli\_is\_busy](group__bt__mesh__blob__cli.md#ga37bbc559b48ea8cfe7cb3ddf8cad24da)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli);

426

[ 441](group__bt__mesh__blob__cli.md#ga047e0cd9817b2ff0a241b2ccfad2acf6)void [bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms](group__bt__mesh__blob__cli.md#ga047e0cd9817b2ff0a241b2ccfad2acf6)(struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) interval\_ms);

442

444extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_blob\_cli\_op[];

445extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_blob\_cli\_cb;

447

449

450#ifdef \_\_cplusplus

451}

452#endif

453

454#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_CLI\_H\_ \*/

[access.h](access_8h.md)

Access layer APIs.

[blob.h](blob_8h.md)

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:867

[bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms](group__bt__mesh__blob__cli.md#ga047e0cd9817b2ff0a241b2ccfad2acf6)

void bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms(struct bt\_mesh\_blob\_cli \*cli, uint32\_t interval\_ms)

Set chunk sending interval in ms.

[bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get](group__bt__mesh__blob__cli.md#ga065196837cbf9d2626b5589ce2671441)

uint8\_t bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get(struct bt\_mesh\_blob\_cli \*cli)

Get the current progress of the active transfer in percent.

[bt\_mesh\_blob\_cli\_xfer\_progress\_get](group__bt__mesh__blob__cli.md#ga17a73cb313dbfc6652b4bcf638b9a30f)

int bt\_mesh\_blob\_cli\_xfer\_progress\_get(struct bt\_mesh\_blob\_cli \*cli, const struct bt\_mesh\_blob\_cli\_inputs \*inputs)

Get the progress of BLOB transfer.

[bt\_mesh\_blob\_cli\_cancel](group__bt__mesh__blob__cli.md#ga222c650657e9a7958b119d4dddd55783)

void bt\_mesh\_blob\_cli\_cancel(struct bt\_mesh\_blob\_cli \*cli)

Cancel an ongoing transfer.

[bt\_mesh\_blob\_cli\_is\_busy](group__bt__mesh__blob__cli.md#ga37bbc559b48ea8cfe7cb3ddf8cad24da)

bool bt\_mesh\_blob\_cli\_is\_busy(struct bt\_mesh\_blob\_cli \*cli)

Get the current state of the BLOB Transfer Client.

[bt\_mesh\_blob\_cli\_resume](group__bt__mesh__blob__cli.md#ga5aed01e812215d153fdfafd6375cc453)

int bt\_mesh\_blob\_cli\_resume(struct bt\_mesh\_blob\_cli \*cli)

Resume the suspended transfer.

[bt\_mesh\_blob\_cli\_send](group__bt__mesh__blob__cli.md#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)

int bt\_mesh\_blob\_cli\_send(struct bt\_mesh\_blob\_cli \*cli, const struct bt\_mesh\_blob\_cli\_inputs \*inputs, const struct bt\_mesh\_blob\_xfer \*xfer, const struct bt\_mesh\_blob\_io \*io)

Perform a BLOB transfer.

[bt\_mesh\_blob\_cli\_suspend](group__bt__mesh__blob__cli.md#ga78487f10fae6c87edaaf4e6ec8f7362c)

int bt\_mesh\_blob\_cli\_suspend(struct bt\_mesh\_blob\_cli \*cli)

Suspend the active transfer.

[bt\_mesh\_blob\_cli\_caps\_get](group__bt__mesh__blob__cli.md#gac401336775dc6274450d5e27ea1cd720)

int bt\_mesh\_blob\_cli\_caps\_get(struct bt\_mesh\_blob\_cli \*cli, const struct bt\_mesh\_blob\_cli\_inputs \*inputs)

Retrieve transfer capabilities for a list of Target nodes.

[bt\_mesh\_blob\_cli\_state](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073)

bt\_mesh\_blob\_cli\_state

BLOB Transfer Client state.

**Definition** blob\_cli.h:163

[BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c)

@ BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK

Checking block status.

**Definition** blob\_cli.h:175

[BT\_MESH\_BLOB\_CLI\_STATE\_NONE](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67)

@ BT\_MESH\_BLOB\_CLI\_STATE\_NONE

No transfer is active.

**Definition** blob\_cli.h:165

[BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646)

@ BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL

Cancelling transfer.

**Definition** blob\_cli.h:179

[BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de)

@ BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET

Retrieving transfer capabilities.

**Definition** blob\_cli.h:167

[BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9)

@ BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED

Transfer is suspended.

**Definition** blob\_cli.h:181

[BT\_MESH\_BLOB\_CLI\_STATE\_START](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2)

@ BT\_MESH\_BLOB\_CLI\_STATE\_START

Sending transfer start.

**Definition** blob\_cli.h:169

[BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96)

@ BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK

Checking transfer status.

**Definition** blob\_cli.h:177

[BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9)

@ BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND

Sending block chunks.

**Definition** blob\_cli.h:173

[BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)

@ BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET

Checking transfer progress.

**Definition** blob\_cli.h:183

[BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2)

@ BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START

Sending block start.

**Definition** blob\_cli.h:171

[bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81)

bt\_mesh\_blob\_xfer\_phase

Transfer phase.

**Definition** blob.h:41

[CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX](group__bt__mesh__blob.md#ga4e1ea17e8a8ffd42f62d64286ddc576e)

#define CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX

**Definition** blob.h:25

[bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d)

bt\_mesh\_blob\_status

BLOB model status codes.

**Definition** blob.h:57

[bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618)

bt\_mesh\_blob\_xfer\_mode

BLOB transfer mode.

**Definition** blob.h:29

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:352

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[bt\_mesh\_blob\_block](structbt__mesh__blob__block.md)

BLOB transfer data block.

**Definition** blob.h:98

[bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md)

Transfer capabilities of a Target node.

**Definition** blob\_cli.h:139

[bt\_mesh\_blob\_cli\_caps::modes](structbt__mesh__blob__cli__caps.md#a1c848a3a2a2ece3764df5cbf6cbfec6b)

enum bt\_mesh\_blob\_xfer\_mode modes

Supported transfer modes.

**Definition** blob\_cli.h:159

[bt\_mesh\_blob\_cli\_caps::max\_chunks](structbt__mesh__blob__cli__caps.md#a318c96b89597dfdf9b68fbc8b999af11)

uint16\_t max\_chunks

Max number of chunks per block.

**Definition** blob\_cli.h:150

[bt\_mesh\_blob\_cli\_caps::max\_block\_size\_log](structbt__mesh__blob__cli__caps.md#a5d44b3b9bf7e47af2e6ba930b2826b15)

uint8\_t max\_block\_size\_log

Logarithmic representation of the maximum block size.

**Definition** blob\_cli.h:147

[bt\_mesh\_blob\_cli\_caps::mtu\_size](structbt__mesh__blob__cli__caps.md#a89d6e1bbc55086cee410835edd6baf3a)

uint16\_t mtu\_size

Max MTU size.

**Definition** blob\_cli.h:156

[bt\_mesh\_blob\_cli\_caps::min\_block\_size\_log](structbt__mesh__blob__cli__caps.md#ac446317efdeca9edbb7df924d4e5a995)

uint8\_t min\_block\_size\_log

Logarithmic representation of the minimum block size.

**Definition** blob\_cli.h:144

[bt\_mesh\_blob\_cli\_caps::max\_chunk\_size](structbt__mesh__blob__cli__caps.md#ad149164240e7c20a57a28c25109079df)

uint16\_t max\_chunk\_size

Max chunk size.

**Definition** blob\_cli.h:153

[bt\_mesh\_blob\_cli\_caps::max\_size](structbt__mesh__blob__cli__caps.md#ae16411b1a36854d6f638a2bca1dc4c3b)

size\_t max\_size

Max BLOB size.

**Definition** blob\_cli.h:141

[bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md)

Event handler callbacks for the BLOB Transfer Client model.

**Definition** blob\_cli.h:190

[bt\_mesh\_blob\_cli\_cb::suspended](structbt__mesh__blob__cli__cb.md#a154a3308167eda4cd93ac28e379c52bc)

void(\* suspended)(struct bt\_mesh\_blob\_cli \*cli)

Transfer is suspended.

**Definition** blob\_cli.h:225

[bt\_mesh\_blob\_cli\_cb::lost\_target](structbt__mesh__blob__cli__cb.md#a26a5ebe87db105900b150f71d770234d)

void(\* lost\_target)(struct bt\_mesh\_blob\_cli \*cli, struct bt\_mesh\_blob\_target \*target, enum bt\_mesh\_blob\_status reason)

Target node loss callback.

**Definition** blob\_cli.h:215

[bt\_mesh\_blob\_cli\_cb::xfer\_progress](structbt__mesh__blob__cli__cb.md#a4b01ef0ab0a367739a75751b57149546)

void(\* xfer\_progress)(struct bt\_mesh\_blob\_cli \*cli, struct bt\_mesh\_blob\_target \*target, const struct bt\_mesh\_blob\_xfer\_info \*info)

Transfer progress callback.

**Definition** blob\_cli.h:249

[bt\_mesh\_blob\_cli\_cb::caps](structbt__mesh__blob__cli__cb.md#a58e749cadeb464299495ee74456c592c)

void(\* caps)(struct bt\_mesh\_blob\_cli \*cli, const struct bt\_mesh\_blob\_cli\_caps \*caps)

Capabilities retrieval completion callback.

**Definition** blob\_cli.h:202

[bt\_mesh\_blob\_cli\_cb::end](structbt__mesh__blob__cli__cb.md#a60bc49eab376b055a8c21099f86fdde7)

void(\* end)(struct bt\_mesh\_blob\_cli \*cli, const struct bt\_mesh\_blob\_xfer \*xfer, bool success)

Transfer end callback.

**Definition** blob\_cli.h:237

[bt\_mesh\_blob\_cli\_cb::xfer\_progress\_complete](structbt__mesh__blob__cli__cb.md#abb4a4d4d24bef076aad7ae56b08d23ed)

void(\* xfer\_progress\_complete)(struct bt\_mesh\_blob\_cli \*cli)

End of Get Transfer Progress procedure.

**Definition** blob\_cli.h:259

[bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md)

BLOB Transfer Client transfer inputs.

**Definition** blob\_cli.h:104

[bt\_mesh\_blob\_cli\_inputs::timeout\_base](structbt__mesh__blob__cli__inputs.md#a30fd3cd7a6df07f6aa90b85cdc6aea18)

uint16\_t timeout\_base

Additional response time for the Target nodes, in 10-second increments.

**Definition** blob\_cli.h:135

[bt\_mesh\_blob\_cli\_inputs::app\_idx](structbt__mesh__blob__cli__inputs.md#a7fb308f895c57b66b50e1ab060228cb3)

uint16\_t app\_idx

AppKey index to send with.

**Definition** blob\_cli.h:111

[bt\_mesh\_blob\_cli\_inputs::targets](structbt__mesh__blob__cli__inputs.md#a835a539b307c659f57da6c20e9223ed1)

sys\_slist\_t targets

Linked list of Target nodes.

**Definition** blob\_cli.h:108

[bt\_mesh\_blob\_cli\_inputs::group](structbt__mesh__blob__cli__inputs.md#ac204e179c2a6ea9cb672fc3c2f9ab017)

uint16\_t group

Group address destination for the BLOB transfer, or BT\_MESH\_ADDR\_UNASSIGNED to send every message to ...

**Definition** blob\_cli.h:117

[bt\_mesh\_blob\_cli\_inputs::ttl](structbt__mesh__blob__cli__inputs.md#adee5ecdba3adc4fe598483b1a160cafb)

uint8\_t ttl

Time to live value of BLOB transfer messages.

**Definition** blob\_cli.h:120

[bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md)

BLOB Transfer Client model instance.

**Definition** blob\_cli.h:293

[bt\_mesh\_blob\_cli::pending](structbt__mesh__blob__cli.md#a1778ae8975ed4b9bc67616e5a0bdf3a9)

uint16\_t pending

**Definition** blob\_cli.h:307

[bt\_mesh\_blob\_cli::complete](structbt__mesh__blob__cli.md#a21b064cceace34605e42d5c295f12cd5)

struct k\_work\_delayable complete

**Definition** blob\_cli.h:306

[bt\_mesh\_blob\_cli::chunk\_interval\_ms](structbt__mesh__blob__cli.md#a2ffd91b68c0aab92f16d9fb4eac79f9d)

uint32\_t chunk\_interval\_ms

**Definition** blob\_cli.h:316

[bt\_mesh\_blob\_cli::tx](structbt__mesh__blob__cli.md#a388183549ed5b1af0d2ac09263611a33)

struct bt\_mesh\_blob\_cli::@115057135266161210151103154264314204011306001332 tx

[bt\_mesh\_blob\_cli::io](structbt__mesh__blob__cli.md#a49f0d79d76aaea785a5ad9160be40e8a)

const struct bt\_mesh\_blob\_io \* io

**Definition** blob\_cli.h:313

[bt\_mesh\_blob\_cli::target](structbt__mesh__blob__cli.md#a519aa0aa7aa66ca67cdf813fee1632c3)

struct bt\_mesh\_blob\_target \* target

**Definition** blob\_cli.h:301

[bt\_mesh\_blob\_cli::block\_count](structbt__mesh__blob__cli.md#a645fdb1f0efb281b1faae4692a3404f1)

uint16\_t block\_count

**Definition** blob\_cli.h:317

[bt\_mesh\_blob\_cli::cb](structbt__mesh__blob__cli.md#a6a0229165fe19af03a26e5cffa1e1486)

const struct bt\_mesh\_blob\_cli\_cb \* cb

Event handler callbacks.

**Definition** blob\_cli.h:295

[bt\_mesh\_blob\_cli::cancelled](structbt__mesh__blob__cli.md#a6d70ac26b7fec22dfdc21f479d867ef7)

uint8\_t cancelled

**Definition** blob\_cli.h:310

[bt\_mesh\_blob\_cli::cli\_timestamp](structbt__mesh__blob__cli.md#a850cc6f4426fec9dc9066953a1b992c8)

int64\_t cli\_timestamp

**Definition** blob\_cli.h:305

[bt\_mesh\_blob\_cli::ctx](structbt__mesh__blob__cli.md#a850d232b04118d7564537dc6763a476c)

struct blob\_cli\_broadcast\_ctx ctx

**Definition** blob\_cli.h:302

[bt\_mesh\_blob\_cli::sending](structbt__mesh__blob__cli.md#a85fdd17b04a06e880f20a0e2b1319ff0)

uint8\_t sending

**Definition** blob\_cli.h:309

[bt\_mesh\_blob\_cli::xfer](structbt__mesh__blob__cli.md#a9185cdadba15bce7b2bf2fcc6f85904a)

const struct bt\_mesh\_blob\_xfer \* xfer

**Definition** blob\_cli.h:315

[bt\_mesh\_blob\_cli::inputs](structbt__mesh__blob__cli.md#aa6c79f5476f96a35c731b63723b2c6cc)

const struct bt\_mesh\_blob\_cli\_inputs \* inputs

**Definition** blob\_cli.h:314

[bt\_mesh\_blob\_cli::caps](structbt__mesh__blob__cli.md#aa7713e6ad0183d18946646df7a5cb6ab)

struct bt\_mesh\_blob\_cli\_caps caps

**Definition** blob\_cli.h:322

[bt\_mesh\_blob\_cli::chunk\_idx](structbt__mesh__blob__cli.md#aafaf644e30e10a8ad9ca6dc8b680eff6)

uint16\_t chunk\_idx

**Definition** blob\_cli.h:318

[bt\_mesh\_blob\_cli::mtu\_size](structbt__mesh__blob__cli.md#aafe943fcada25f32b9a31b8d7586032a)

uint16\_t mtu\_size

**Definition** blob\_cli.h:319

[bt\_mesh\_blob\_cli::state](structbt__mesh__blob__cli.md#ab131637681a0cf0b3ceebad015b28726)

enum bt\_mesh\_blob\_cli\_state state

**Definition** blob\_cli.h:320

[bt\_mesh\_blob\_cli::retries](structbt__mesh__blob__cli.md#ab291086be3d9ecf03becd4200d783835)

uint8\_t retries

**Definition** blob\_cli.h:308

[bt\_mesh\_blob\_cli::block](structbt__mesh__blob__cli.md#ac95970f7fd6b00fca284121394110250)

struct bt\_mesh\_blob\_block block

**Definition** blob\_cli.h:321

[bt\_mesh\_blob\_cli::mod](structbt__mesh__blob__cli.md#ada23952593d2a498ed421895828f461f)

const struct bt\_mesh\_model \* mod

**Definition** blob\_cli.h:298

[bt\_mesh\_blob\_cli::retry](structbt__mesh__blob__cli.md#add07e03f13b276fafabeb9cc4ba94d32)

struct k\_work\_delayable retry

**Definition** blob\_cli.h:303

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md)

Target node's Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target nod...

**Definition** blob\_cli.h:40

[bt\_mesh\_blob\_target\_pull::missing](structbt__mesh__blob__target__pull.md#a19fc9a8a0b5202887e7fd73028805774)

uint8\_t missing[DIV\_ROUND\_UP(CONFIG\_BT\_MESH\_BLOB\_CHUNK\_COUNT\_MAX, 8)]

Missing chunks reported by this Target node.

**Definition** blob\_cli.h:45

[bt\_mesh\_blob\_target\_pull::block\_report\_timestamp](structbt__mesh__blob__target__pull.md#a9234ee3246890285b5cd30c32866b718)

int64\_t block\_report\_timestamp

Timestamp when the Block Report Timeout Timer expires for this Target node.

**Definition** blob\_cli.h:42

[bt\_mesh\_blob\_target](structbt__mesh__blob__target.md)

BLOB Transfer Client Target node.

**Definition** blob\_cli.h:49

[bt\_mesh\_blob\_target::pull](structbt__mesh__blob__target.md#a0498f23d640af4b006398d5482fbaa53)

struct bt\_mesh\_blob\_target\_pull \* pull

Target node's Pull mode context.

**Definition** blob\_cli.h:59

[bt\_mesh\_blob\_target::timedout](structbt__mesh__blob__target.md#a3e14f4518ee054754dfa50d8070c1725)

uint8\_t timedout

**Definition** blob\_cli.h:66

[bt\_mesh\_blob\_target::acked](structbt__mesh__blob__target.md#a4eef4809023e8d4a4ee8beece5e83160)

uint8\_t acked

**Definition** blob\_cli.h:65

[bt\_mesh\_blob\_target::status](structbt__mesh__blob__target.md#a62b5a5be44d52ebf09421de57933459d)

uint8\_t status

BLOB transfer status, see bt\_mesh\_blob\_status.

**Definition** blob\_cli.h:62

[bt\_mesh\_blob\_target::procedure\_complete](structbt__mesh__blob__target.md#a711a031e841bb54c4985d02a81c6846a)

uint8\_t procedure\_complete

**Definition** blob\_cli.h:64

[bt\_mesh\_blob\_target::skip](structbt__mesh__blob__target.md#a7aa1066dbeee5ba4a5be5aa14d61d4d1)

uint8\_t skip

**Definition** blob\_cli.h:67

[bt\_mesh\_blob\_target::addr](structbt__mesh__blob__target.md#ab4c032f92a4ec12e4bbd6fa84139c085)

uint16\_t addr

Target node address.

**Definition** blob\_cli.h:54

[bt\_mesh\_blob\_target::n](structbt__mesh__blob__target.md#aca0f3cabb5c457cfb11a4bc71c3bea85)

sys\_snode\_t n

Linked list node.

**Definition** blob\_cli.h:51

[bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md)

BLOB transfer information.

**Definition** blob\_cli.h:77

[bt\_mesh\_blob\_xfer\_info::id](structbt__mesh__blob__xfer__info.md#a3a19a5f387b53dd32429c9e76e53a87f)

uint64\_t id

BLOB ID.

**Definition** blob\_cli.h:88

[bt\_mesh\_blob\_xfer\_info::phase](structbt__mesh__blob__xfer__info.md#a6a8686872018ceb6e4e9fc52eaff5b9e)

enum bt\_mesh\_blob\_xfer\_phase phase

BLOB transfer phase.

**Definition** blob\_cli.h:85

[bt\_mesh\_blob\_xfer\_info::mode](structbt__mesh__blob__xfer__info.md#a6cbb21582332cb23125624db5a02731a)

enum bt\_mesh\_blob\_xfer\_mode mode

BLOB transfer mode.

**Definition** blob\_cli.h:82

[bt\_mesh\_blob\_xfer\_info::missing\_blocks](structbt__mesh__blob__xfer__info.md#a8825fba3258805db956b099ddfa19f9f)

const uint8\_t \* missing\_blocks

Bit field indicating blocks that were not received.

**Definition** blob\_cli.h:100

[bt\_mesh\_blob\_xfer\_info::status](structbt__mesh__blob__xfer__info.md#aaeda1f5688bfb3cc3708e3797f3190a5)

enum bt\_mesh\_blob\_status status

BLOB transfer status.

**Definition** blob\_cli.h:79

[bt\_mesh\_blob\_xfer\_info::size](structbt__mesh__blob__xfer__info.md#ac03d3ad7a618ee67f9bd7f1d52019cb7)

uint32\_t size

BLOB size in octets.

**Definition** blob\_cli.h:91

[bt\_mesh\_blob\_xfer\_info::block\_size\_log](structbt__mesh__blob__xfer__info.md#ad09a0e80202b4953788fcade5788f0ef)

uint8\_t block\_size\_log

Logarithmic representation of the block size.

**Definition** blob\_cli.h:94

[bt\_mesh\_blob\_xfer\_info::mtu\_size](structbt__mesh__blob__xfer__info.md#ae24ed28faaef6187850cb0f04da2b8c7)

uint16\_t mtu\_size

MTU size in octets.

**Definition** blob\_cli.h:97

[bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)

BLOB transfer.

**Definition** blob.h:123

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:891

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob\_cli.h](blob__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
