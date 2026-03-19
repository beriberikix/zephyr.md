---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mcc_8h.html
original_path: doxygen/html/mcc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcc.h File Reference

Bluetooth Media Control Client (MCC) APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/media_proxy.h](media__proxy_8h_source.md)>`

[Go to the source code of this file.](mcc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mcc\_cb](structbt__mcc__cb.md) |
|  | Media control client callbacks. [More...](structbt__mcc__cb.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_mcc\_discover\_mcs\_cb](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342)) (struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_mcc\_discover\_mcs()](group__bt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3 "Discover Media Control Service."). |
| typedef void(\* | [bt\_mcc\_read\_player\_name\_cb](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f)) (struct bt\_conn \*conn, int err, const char \*name) |
|  | Callback function for [bt\_mcc\_read\_player\_name()](group__bt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36 "Read Media Player Name."). |
| typedef void(\* | [bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) icon\_id) |
|  | Callback function for [bt\_mcc\_read\_icon\_obj\_id()](group__bt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389 "Read Icon Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_icon\_url\_cb](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0)) (struct bt\_conn \*conn, int err, const char \*icon\_url) |
|  | Callback function for [bt\_mcc\_read\_icon\_url()](group__bt__mcc.md#ga38733456db6bc6558a511e104577c9c9 "Read Icon Object URL."). |
| typedef void(\* | [bt\_mcc\_track\_changed\_ntf\_cb](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688)) (struct bt\_conn \*conn, int err) |
|  | Callback function for track changed notifications. |
| typedef void(\* | [bt\_mcc\_read\_track\_title\_cb](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402)) (struct bt\_conn \*conn, int err, const char \*title) |
|  | Callback function for [bt\_mcc\_read\_track\_title()](group__bt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373 "Read Track Title."). |
| typedef void(\* | [bt\_mcc\_read\_track\_duration\_cb](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c)) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dur) |
|  | Callback function for [bt\_mcc\_read\_track\_duration()](group__bt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5 "Read Track Duration."). |
| typedef void(\* | [bt\_mcc\_read\_track\_position\_cb](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263)) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
|  | Callback function for [bt\_mcc\_read\_track\_position()](group__bt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e "Read Track Position."). |
| typedef void(\* | [bt\_mcc\_set\_track\_position\_cb](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff)) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
|  | Callback function for [bt\_mcc\_set\_track\_position()](group__bt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf "Set Track position."). |
| typedef void(\* | [bt\_mcc\_read\_playback\_speed\_cb](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909)) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Callback function for [bt\_mcc\_read\_playback\_speed()](group__bt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609 "Read Playback speed."). |
| typedef void(\* | [bt\_mcc\_set\_playback\_speed\_cb](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779)) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Callback function for [bt\_mcc\_set\_playback\_speed()](group__bt__mcc.md#ga1382e5b6000896dc94f6489909301719 "Set Playback Speed."). |
| typedef void(\* | [bt\_mcc\_read\_seeking\_speed\_cb](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83)) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Callback function for [bt\_mcc\_read\_seeking\_speed()](group__bt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658 "Read Seeking speed."). |
| typedef void(\* | [bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_segments\_obj\_id()](group__bt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0 "Read Track Segments Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_current\_track\_obj\_id()](group__bt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9 "Read Current Track Object ID."). |
| typedef void(\* | [bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_set\_current\_track\_obj\_id()](group__bt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49 "Set Current Track Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for bt\_mcc\_read\_next\_track\_obj\_id\_obj(). |
| typedef void(\* | [bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_set\_next\_track\_obj\_id()](group__bt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084 "Set Next Track Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_parent\_group\_obj\_id()](group__bt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae "Read Parent Group Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_current\_group\_obj\_id()](group__bt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c "Read Current Group Object ID."). |
| typedef void(\* | [bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id) |
|  | Callback function for [bt\_mcc\_set\_current\_group\_obj\_id()](group__bt__mcc.md#gae3f385811f852d584595c6e531556aed "Set Current Group Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_playing\_order\_cb](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Callback function for [bt\_mcc\_read\_playing\_order()](group__bt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7 "Read Playing Order."). |
| typedef void(\* | [bt\_mcc\_set\_playing\_order\_cb](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Callback function for [bt\_mcc\_set\_playing\_order()](group__bt__mcc.md#ga05295649385c3a337401765627d09553 "Set Playing Order."). |
| typedef void(\* | [bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0)) (struct bt\_conn \*conn, int err, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders) |
|  | Callback function for [bt\_mcc\_read\_playing\_orders\_supported()](group__bt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4 "Read Playing Orders Supported."). |
| typedef void(\* | [bt\_mcc\_read\_media\_state\_cb](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Callback function for [bt\_mcc\_read\_media\_state()](group__bt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d "Read Media State."). |
| typedef void(\* | [bt\_mcc\_send\_cmd\_cb](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e)) (struct bt\_conn \*conn, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Callback function for [bt\_mcc\_send\_cmd()](group__bt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0 "Send a command."). |
| typedef void(\* | [bt\_mcc\_cmd\_ntf\_cb](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8)) (struct bt\_conn \*conn, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*ntf) |
|  | Callback function for command notifications. |
| typedef void(\* | [bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc)) (struct bt\_conn \*conn, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
|  | Callback function for [bt\_mcc\_read\_opcodes\_supported()](group__bt__mcc.md#ga692160554947f92e8c81912c5e597086 "Read Opcodes Supported."). |
| typedef void(\* | [bt\_mcc\_send\_search\_cb](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f)) (struct bt\_conn \*conn, int err, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Callback function for [bt\_mcc\_send\_search()](group__bt__mcc.md#ga324161056e03195820bbd7cc77ff287d "Send a Search command."). |
| typedef void(\* | [bt\_mcc\_search\_ntf\_cb](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
|  | Callback function for search notifications. |
| typedef void(\* | [bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_search\_results\_obj\_id()](group__bt__mcc.md#ga98814a516a027bdaa3250e93d55309fd "Search Results Group Object ID."). |
| typedef void(\* | [bt\_mcc\_read\_content\_control\_id\_cb](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Callback function for [bt\_mcc\_read\_content\_control\_id()](group__bt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963 "Read Content Control ID."). |
| typedef void(\* | [bt\_mcc\_otc\_obj\_selected\_cb](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3)) (struct bt\_conn \*conn, int err) |
|  | Callback function for object selected. |
| typedef void(\* | [bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c)) (struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_mcc\_otc\_read\_object\_metadata()](group__bt__mcc.md#gadf687cb26a6d00bca73e273da583df88 "Read the current object metadata."). |
| typedef void(\* | [bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_icon\_object()](group__bt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e "Read the Icon Object."). |
| typedef void(\* | [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_track\_segments\_object()](group__bt__mcc.md#gac22e840b65895aa018ab1b4535a87672 "Read the Track Segments Object."). |
| typedef void(\* | [bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_current\_track\_object()](group__bt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8 "Read the Current Track Object."). |
| typedef void(\* | [bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_next\_track\_object()](group__bt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e "Read the Next Track Object."). |
| typedef void(\* | [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_parent\_group\_object()](group__bt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518 "Read the Parent Group Object."). |
| typedef void(\* | [bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_current\_group\_object()](group__bt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6 "Read the Current Group Object."). |

| Functions | |
| --- | --- |
| int | [bt\_mcc\_init](group__bt__mcc.md#ga94de08bb0a1e1324600e4957b648e92b) (struct [bt\_mcc\_cb](structbt__mcc__cb.md) \*cb) |
|  | Initialize Media Control Client. |
| int | [bt\_mcc\_discover\_mcs](group__bt__mcc.md#gaa1f9ead03b4cccaff1e3390b8052b0f3) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) subscribe) |
|  | Discover Media Control Service. |
| int | [bt\_mcc\_read\_player\_name](group__bt__mcc.md#ga724ce71fc88f1ca4bcf209c92c177f36) (struct bt\_conn \*conn) |
|  | Read Media Player Name. |
| int | [bt\_mcc\_read\_icon\_obj\_id](group__bt__mcc.md#ga0e69de33c37957a2b5473df7d3c3f389) (struct bt\_conn \*conn) |
|  | Read Icon Object ID. |
| int | [bt\_mcc\_read\_icon\_url](group__bt__mcc.md#ga38733456db6bc6558a511e104577c9c9) (struct bt\_conn \*conn) |
|  | Read Icon Object URL. |
| int | [bt\_mcc\_read\_track\_title](group__bt__mcc.md#ga7dfa14489a4cea4b00053c9aa75cf373) (struct bt\_conn \*conn) |
|  | Read Track Title. |
| int | [bt\_mcc\_read\_track\_duration](group__bt__mcc.md#ga50a45f043bd2ae1741a120e02e9dc2f5) (struct bt\_conn \*conn) |
|  | Read Track Duration. |
| int | [bt\_mcc\_read\_track\_position](group__bt__mcc.md#gaf143098f5dfcfba01df3d6f06472779e) (struct bt\_conn \*conn) |
|  | Read Track Position. |
| int | [bt\_mcc\_set\_track\_position](group__bt__mcc.md#gad324366d33bef6b1ed1c8fc881bf44cf) (struct bt\_conn \*conn, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
|  | Set Track position. |
| int | [bt\_mcc\_read\_playback\_speed](group__bt__mcc.md#gaa566a4c42f0ab0ab6feddf4e25845609) (struct bt\_conn \*conn) |
|  | Read Playback speed. |
| int | [bt\_mcc\_set\_playback\_speed](group__bt__mcc.md#ga1382e5b6000896dc94f6489909301719) (struct bt\_conn \*conn, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Set Playback Speed. |
| int | [bt\_mcc\_read\_seeking\_speed](group__bt__mcc.md#ga366fdfaa23cef9f1c3ba7ddd36a67658) (struct bt\_conn \*conn) |
|  | Read Seeking speed. |
| int | [bt\_mcc\_read\_segments\_obj\_id](group__bt__mcc.md#ga4cb0a95e91d3ec00ede64663a2b932f0) (struct bt\_conn \*conn) |
|  | Read Track Segments Object ID. |
| int | [bt\_mcc\_read\_current\_track\_obj\_id](group__bt__mcc.md#ga5b3a8fb8e8251cf005b34e47619ae7b9) (struct bt\_conn \*conn) |
|  | Read Current Track Object ID. |
| int | [bt\_mcc\_set\_current\_track\_obj\_id](group__bt__mcc.md#ga8374ac230c5fe6b5a1bb7fa873fdeb49) (struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Track Object ID. |
| int | [bt\_mcc\_read\_next\_track\_obj\_id](group__bt__mcc.md#ga11e4c02ba0b1fbc197aaf071b82a1eed) (struct bt\_conn \*conn) |
|  | Read Next Track Object ID. |
| int | [bt\_mcc\_set\_next\_track\_obj\_id](group__bt__mcc.md#gafeebcbb0c77d5d4acbe151fd9888d084) (struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Next Track Object ID. |
| int | [bt\_mcc\_read\_current\_group\_obj\_id](group__bt__mcc.md#ga8cb43a6947df48113b082d8cc8ccf25c) (struct bt\_conn \*conn) |
|  | Read Current Group Object ID. |
| int | [bt\_mcc\_set\_current\_group\_obj\_id](group__bt__mcc.md#gae3f385811f852d584595c6e531556aed) (struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Group Object ID. |
| int | [bt\_mcc\_read\_parent\_group\_obj\_id](group__bt__mcc.md#ga3ccd5961cc4c8d82fa988d300e12e1ae) (struct bt\_conn \*conn) |
|  | Read Parent Group Object ID. |
| int | [bt\_mcc\_read\_playing\_order](group__bt__mcc.md#ga077a134ff1404fb76aa756a5531fd1d7) (struct bt\_conn \*conn) |
|  | Read Playing Order. |
| int | [bt\_mcc\_set\_playing\_order](group__bt__mcc.md#ga05295649385c3a337401765627d09553) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Set Playing Order. |
| int | [bt\_mcc\_read\_playing\_orders\_supported](group__bt__mcc.md#gaf61f6fcf3f96ccb6f5a72ffaad27dec4) (struct bt\_conn \*conn) |
|  | Read Playing Orders Supported. |
| int | [bt\_mcc\_read\_media\_state](group__bt__mcc.md#gac1b440cfa54dd4b6e23bb47bf885f88d) (struct bt\_conn \*conn) |
|  | Read Media State. |
| int | [bt\_mcc\_send\_cmd](group__bt__mcc.md#ga3f4a538bcf436e4e80b73ed6e077dfa0) (struct bt\_conn \*conn, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a command. |
| int | [bt\_mcc\_read\_opcodes\_supported](group__bt__mcc.md#ga692160554947f92e8c81912c5e597086) (struct bt\_conn \*conn) |
|  | Read Opcodes Supported. |
| int | [bt\_mcc\_send\_search](group__bt__mcc.md#ga324161056e03195820bbd7cc77ff287d) (struct bt\_conn \*conn, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Send a Search command. |
| int | [bt\_mcc\_read\_search\_results\_obj\_id](group__bt__mcc.md#ga98814a516a027bdaa3250e93d55309fd) (struct bt\_conn \*conn) |
|  | Search Results Group Object ID. |
| int | [bt\_mcc\_read\_content\_control\_id](group__bt__mcc.md#ga77cbf810c35d1a17efce1fae6a941963) (struct bt\_conn \*conn) |
|  | Read Content Control ID. |
| int | [bt\_mcc\_otc\_read\_object\_metadata](group__bt__mcc.md#gadf687cb26a6d00bca73e273da583df88) (struct bt\_conn \*conn) |
|  | Read the current object metadata. |
| int | [bt\_mcc\_otc\_read\_icon\_object](group__bt__mcc.md#gaba527d8f0307ab11150a5434231c0e7e) (struct bt\_conn \*conn) |
|  | Read the Icon Object. |
| int | [bt\_mcc\_otc\_read\_track\_segments\_object](group__bt__mcc.md#gac22e840b65895aa018ab1b4535a87672) (struct bt\_conn \*conn) |
|  | Read the Track Segments Object. |
| int | [bt\_mcc\_otc\_read\_current\_track\_object](group__bt__mcc.md#gac4b09a77df52d2681e7652591ca32bf8) (struct bt\_conn \*conn) |
|  | Read the Current Track Object. |
| int | [bt\_mcc\_otc\_read\_next\_track\_object](group__bt__mcc.md#ga611c9edebff5b4347ad1241ffd19f49e) (struct bt\_conn \*conn) |
|  | Read the Next Track Object. |
| int | [bt\_mcc\_otc\_read\_current\_group\_object](group__bt__mcc.md#ga4b1ebe682ad134795f8a1b494244f8b6) (struct bt\_conn \*conn) |
|  | Read the Current Group Object. |
| int | [bt\_mcc\_otc\_read\_parent\_group\_object](group__bt__mcc.md#gae001cb2d701457ce083aa8a0fd5ec518) (struct bt\_conn \*conn) |
|  | Read the Parent Group Object. |
| struct [bt\_ots\_client](structbt__ots__client.md) \* | [bt\_mcc\_otc\_inst](group__bt__mcc.md#gaa243806f65c4a37d41f25bcc4f1839fc) (struct bt\_conn \*conn) |
|  | Look up MCC OTC instance. |

## Detailed Description

Bluetooth Media Control Client (MCC) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [mcc.h](mcc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
