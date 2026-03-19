---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mcc.html
original_path: doxygen/html/group__bt__mcc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Media Control Client (MCC)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Media Control Client (MCC) interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mcc\_cb](structbt__mcc__cb.md) |
|  | Media control client callbacks. [More...](structbt__mcc__cb.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_mcc\_discover\_mcs\_cb](#gab268faeca207e115ee1be0843ab8c342)) (struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_mcc\_discover\_mcs()](#gaa1f9ead03b4cccaff1e3390b8052b0f3). |
| typedef void(\* | [bt\_mcc\_read\_player\_name\_cb](#gaa943b61848ee43e91d473f6fdd0a604f)) (struct bt\_conn \*conn, int err, const char \*name) |
|  | Callback function for [bt\_mcc\_read\_player\_name()](#ga724ce71fc88f1ca4bcf209c92c177f36). |
| typedef void(\* | [bt\_mcc\_read\_icon\_obj\_id\_cb](#ga471d0491b70e5472e16c3035507761cc)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) icon\_id) |
|  | Callback function for [bt\_mcc\_read\_icon\_obj\_id()](#ga0e69de33c37957a2b5473df7d3c3f389). |
| typedef void(\* | [bt\_mcc\_read\_icon\_url\_cb](#gaaddc4abe38f6ca811967ae6a10d8f8f0)) (struct bt\_conn \*conn, int err, const char \*icon\_url) |
|  | Callback function for [bt\_mcc\_read\_icon\_url()](#ga38733456db6bc6558a511e104577c9c9). |
| typedef void(\* | [bt\_mcc\_track\_changed\_ntf\_cb](#ga67611a3068284b0c7fbb3ef07dfe7688)) (struct bt\_conn \*conn, int err) |
|  | Callback function for track changed notifications. |
| typedef void(\* | [bt\_mcc\_read\_track\_title\_cb](#ga6927860f1803aeade4994610da32d402)) (struct bt\_conn \*conn, int err, const char \*title) |
|  | Callback function for [bt\_mcc\_read\_track\_title()](#ga7dfa14489a4cea4b00053c9aa75cf373). |
| typedef void(\* | [bt\_mcc\_read\_track\_duration\_cb](#ga7cdb524ff9c34f24c1740adb9eca072c)) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dur) |
|  | Callback function for [bt\_mcc\_read\_track\_duration()](#ga50a45f043bd2ae1741a120e02e9dc2f5). |
| typedef void(\* | [bt\_mcc\_read\_track\_position\_cb](#ga128883c867b10e57d3f2f26a708b7263)) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
|  | Callback function for [bt\_mcc\_read\_track\_position()](#gaf143098f5dfcfba01df3d6f06472779e). |
| typedef void(\* | [bt\_mcc\_set\_track\_position\_cb](#ga1167f5e2ef4a7e78469aefc0cef18bff)) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
|  | Callback function for [bt\_mcc\_set\_track\_position()](#gad324366d33bef6b1ed1c8fc881bf44cf). |
| typedef void(\* | [bt\_mcc\_read\_playback\_speed\_cb](#ga6f5383be3f344c25361786d903640909)) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Callback function for [bt\_mcc\_read\_playback\_speed()](#gaa566a4c42f0ab0ab6feddf4e25845609). |
| typedef void(\* | [bt\_mcc\_set\_playback\_speed\_cb](#ga1322f2ddbb587c70fd23a7ccfc1fc779)) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Callback function for [bt\_mcc\_set\_playback\_speed()](#ga1382e5b6000896dc94f6489909301719). |
| typedef void(\* | [bt\_mcc\_read\_seeking\_speed\_cb](#ga3089e6165e8491325f7205279bb5bb83)) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Callback function for [bt\_mcc\_read\_seeking\_speed()](#ga366fdfaa23cef9f1c3ba7ddd36a67658). |
| typedef void(\* | [bt\_mcc\_read\_segments\_obj\_id\_cb](#ga1fbf0b4fd624626127774d2662083875)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_segments\_obj\_id()](#ga4cb0a95e91d3ec00ede64663a2b932f0). |
| typedef void(\* | [bt\_mcc\_read\_current\_track\_obj\_id\_cb](#ga28ac116604248643b0b203b4a314b7b1)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_current\_track\_obj\_id()](#ga5b3a8fb8e8251cf005b34e47619ae7b9). |
| typedef void(\* | [bt\_mcc\_set\_current\_track\_obj\_id\_cb](#gaf0d619b493a8fb4c00278a0a85bb2529)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_set\_current\_track\_obj\_id()](#ga8374ac230c5fe6b5a1bb7fa873fdeb49). |
| typedef void(\* | [bt\_mcc\_read\_next\_track\_obj\_id\_cb](#ga83d6614d4a0808782b1b4df115b872d2)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for bt\_mcc\_read\_next\_track\_obj\_id\_obj(). |
| typedef void(\* | [bt\_mcc\_set\_next\_track\_obj\_id\_cb](#ga2f3099d097b28ab9c4abf81e19474def)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_set\_next\_track\_obj\_id()](#gafeebcbb0c77d5d4acbe151fd9888d084). |
| typedef void(\* | [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](#ga48dd365aa637336b9899db4b6986a5e4)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_parent\_group\_obj\_id()](#ga3ccd5961cc4c8d82fa988d300e12e1ae). |
| typedef void(\* | [bt\_mcc\_read\_current\_group\_obj\_id\_cb](#ga5f21a1eed4bfe4dfbca40949af895723)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_current\_group\_obj\_id()](#ga8cb43a6947df48113b082d8cc8ccf25c). |
| typedef void(\* | [bt\_mcc\_set\_current\_group\_obj\_id\_cb](#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id) |
|  | Callback function for [bt\_mcc\_set\_current\_group\_obj\_id()](#gae3f385811f852d584595c6e531556aed). |
| typedef void(\* | [bt\_mcc\_read\_playing\_order\_cb](#gafb0869e0ef5332d39070081efdacf17c)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Callback function for [bt\_mcc\_read\_playing\_order()](#ga077a134ff1404fb76aa756a5531fd1d7). |
| typedef void(\* | [bt\_mcc\_set\_playing\_order\_cb](#ga1a12fb89adf29c83bca02f701213c6d7)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Callback function for [bt\_mcc\_set\_playing\_order()](#ga05295649385c3a337401765627d09553). |
| typedef void(\* | [bt\_mcc\_read\_playing\_orders\_supported\_cb](#gac45a2aff295535f70ac4a070e970b7a0)) (struct bt\_conn \*conn, int err, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders) |
|  | Callback function for [bt\_mcc\_read\_playing\_orders\_supported()](#gaf61f6fcf3f96ccb6f5a72ffaad27dec4). |
| typedef void(\* | [bt\_mcc\_read\_media\_state\_cb](#ga200a827f4bf5d65570ddabd028269f77)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Callback function for [bt\_mcc\_read\_media\_state()](#gac1b440cfa54dd4b6e23bb47bf885f88d). |
| typedef void(\* | [bt\_mcc\_send\_cmd\_cb](#gae4c2d1a5c41df1c3535418cc23d48f8e)) (struct bt\_conn \*conn, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Callback function for [bt\_mcc\_send\_cmd()](#ga3f4a538bcf436e4e80b73ed6e077dfa0). |
| typedef void(\* | [bt\_mcc\_cmd\_ntf\_cb](#ga50da90a5c351c99494208b44096a61c8)) (struct bt\_conn \*conn, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*ntf) |
|  | Callback function for command notifications. |
| typedef void(\* | [bt\_mcc\_read\_opcodes\_supported\_cb](#gab37df36e15132b9235d1093f5aa403cc)) (struct bt\_conn \*conn, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
|  | Callback function for [bt\_mcc\_read\_opcodes\_supported()](#ga692160554947f92e8c81912c5e597086). |
| typedef void(\* | [bt\_mcc\_send\_search\_cb](#ga9489c34b6006df8bd26e626030cab71f)) (struct bt\_conn \*conn, int err, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Callback function for [bt\_mcc\_send\_search()](#ga324161056e03195820bbd7cc77ff287d). |
| typedef void(\* | [bt\_mcc\_search\_ntf\_cb](#gab168a4c86de444dd066802c4a5fe41c3)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
|  | Callback function for search notifications. |
| typedef void(\* | [bt\_mcc\_read\_search\_results\_obj\_id\_cb](#ga5a39822a21a6f2aa7a6548c57979a926)) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Callback function for [bt\_mcc\_read\_search\_results\_obj\_id()](#ga98814a516a027bdaa3250e93d55309fd). |
| typedef void(\* | [bt\_mcc\_read\_content\_control\_id\_cb](#gadb607997fdcb3e57bbfc90790de4b927)) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Callback function for [bt\_mcc\_read\_content\_control\_id()](#ga77cbf810c35d1a17efce1fae6a941963). |
| typedef void(\* | [bt\_mcc\_otc\_obj\_selected\_cb](#gaf186e6adefa296de4146502665d738b3)) (struct bt\_conn \*conn, int err) |
|  | Callback function for object selected. |
| typedef void(\* | [bt\_mcc\_otc\_obj\_metadata\_cb](#ga9805222315ca6e6df0720233055af10c)) (struct bt\_conn \*conn, int err) |
|  | Callback function for [bt\_mcc\_otc\_read\_object\_metadata()](#gadf687cb26a6d00bca73e273da583df88). |
| typedef void(\* | [bt\_mcc\_otc\_read\_icon\_object\_cb](#ga13bedbb573bc5575ab75fc3ae65c1870)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_icon\_object()](#gaba527d8f0307ab11150a5434231c0e7e). |
| typedef void(\* | [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](#ga1c4c842879cd8b209080a59d3ba125f8)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_track\_segments\_object()](#gac22e840b65895aa018ab1b4535a87672). |
| typedef void(\* | [bt\_mcc\_otc\_read\_current\_track\_object\_cb](#gaff887eda3b84cad1052549f23c8dcfbe)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_current\_track\_object()](#gac4b09a77df52d2681e7652591ca32bf8). |
| typedef void(\* | [bt\_mcc\_otc\_read\_next\_track\_object\_cb](#ga920f25e04e1be4ad5f7e220c2e9102b5)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_next\_track\_object()](#ga611c9edebff5b4347ad1241ffd19f49e). |
| typedef void(\* | [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](#gaca904bacb552792ffd85c6a640f0ba48)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_parent\_group\_object()](#gae001cb2d701457ce083aa8a0fd5ec518). |
| typedef void(\* | [bt\_mcc\_otc\_read\_current\_group\_object\_cb](#ga0b309ae7ce23834f303c39017ffa4e50)) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Callback function for [bt\_mcc\_otc\_read\_current\_group\_object()](#ga4b1ebe682ad134795f8a1b494244f8b6). |

| Functions | |
| --- | --- |
| int | [bt\_mcc\_init](#ga94de08bb0a1e1324600e4957b648e92b) (struct [bt\_mcc\_cb](structbt__mcc__cb.md) \*cb) |
|  | Initialize Media Control Client. |
| int | [bt\_mcc\_discover\_mcs](#gaa1f9ead03b4cccaff1e3390b8052b0f3) (struct bt\_conn \*conn, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) subscribe) |
|  | Discover Media Control Service. |
| int | [bt\_mcc\_read\_player\_name](#ga724ce71fc88f1ca4bcf209c92c177f36) (struct bt\_conn \*conn) |
|  | Read Media Player Name. |
| int | [bt\_mcc\_read\_icon\_obj\_id](#ga0e69de33c37957a2b5473df7d3c3f389) (struct bt\_conn \*conn) |
|  | Read Icon Object ID. |
| int | [bt\_mcc\_read\_icon\_url](#ga38733456db6bc6558a511e104577c9c9) (struct bt\_conn \*conn) |
|  | Read Icon Object URL. |
| int | [bt\_mcc\_read\_track\_title](#ga7dfa14489a4cea4b00053c9aa75cf373) (struct bt\_conn \*conn) |
|  | Read Track Title. |
| int | [bt\_mcc\_read\_track\_duration](#ga50a45f043bd2ae1741a120e02e9dc2f5) (struct bt\_conn \*conn) |
|  | Read Track Duration. |
| int | [bt\_mcc\_read\_track\_position](#gaf143098f5dfcfba01df3d6f06472779e) (struct bt\_conn \*conn) |
|  | Read Track Position. |
| int | [bt\_mcc\_set\_track\_position](#gad324366d33bef6b1ed1c8fc881bf44cf) (struct bt\_conn \*conn, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
|  | Set Track position. |
| int | [bt\_mcc\_read\_playback\_speed](#gaa566a4c42f0ab0ab6feddf4e25845609) (struct bt\_conn \*conn) |
|  | Read Playback speed. |
| int | [bt\_mcc\_set\_playback\_speed](#ga1382e5b6000896dc94f6489909301719) (struct bt\_conn \*conn, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Set Playback Speed. |
| int | [bt\_mcc\_read\_seeking\_speed](#ga366fdfaa23cef9f1c3ba7ddd36a67658) (struct bt\_conn \*conn) |
|  | Read Seeking speed. |
| int | [bt\_mcc\_read\_segments\_obj\_id](#ga4cb0a95e91d3ec00ede64663a2b932f0) (struct bt\_conn \*conn) |
|  | Read Track Segments Object ID. |
| int | [bt\_mcc\_read\_current\_track\_obj\_id](#ga5b3a8fb8e8251cf005b34e47619ae7b9) (struct bt\_conn \*conn) |
|  | Read Current Track Object ID. |
| int | [bt\_mcc\_set\_current\_track\_obj\_id](#ga8374ac230c5fe6b5a1bb7fa873fdeb49) (struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Track Object ID. |
| int | [bt\_mcc\_read\_next\_track\_obj\_id](#ga11e4c02ba0b1fbc197aaf071b82a1eed) (struct bt\_conn \*conn) |
|  | Read Next Track Object ID. |
| int | [bt\_mcc\_set\_next\_track\_obj\_id](#gafeebcbb0c77d5d4acbe151fd9888d084) (struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Next Track Object ID. |
| int | [bt\_mcc\_read\_current\_group\_obj\_id](#ga8cb43a6947df48113b082d8cc8ccf25c) (struct bt\_conn \*conn) |
|  | Read Current Group Object ID. |
| int | [bt\_mcc\_set\_current\_group\_obj\_id](#gae3f385811f852d584595c6e531556aed) (struct bt\_conn \*conn, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Group Object ID. |
| int | [bt\_mcc\_read\_parent\_group\_obj\_id](#ga3ccd5961cc4c8d82fa988d300e12e1ae) (struct bt\_conn \*conn) |
|  | Read Parent Group Object ID. |
| int | [bt\_mcc\_read\_playing\_order](#ga077a134ff1404fb76aa756a5531fd1d7) (struct bt\_conn \*conn) |
|  | Read Playing Order. |
| int | [bt\_mcc\_set\_playing\_order](#ga05295649385c3a337401765627d09553) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Set Playing Order. |
| int | [bt\_mcc\_read\_playing\_orders\_supported](#gaf61f6fcf3f96ccb6f5a72ffaad27dec4) (struct bt\_conn \*conn) |
|  | Read Playing Orders Supported. |
| int | [bt\_mcc\_read\_media\_state](#gac1b440cfa54dd4b6e23bb47bf885f88d) (struct bt\_conn \*conn) |
|  | Read Media State. |
| int | [bt\_mcc\_send\_cmd](#ga3f4a538bcf436e4e80b73ed6e077dfa0) (struct bt\_conn \*conn, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a command. |
| int | [bt\_mcc\_read\_opcodes\_supported](#ga692160554947f92e8c81912c5e597086) (struct bt\_conn \*conn) |
|  | Read Opcodes Supported. |
| int | [bt\_mcc\_send\_search](#ga324161056e03195820bbd7cc77ff287d) (struct bt\_conn \*conn, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Send a Search command. |
| int | [bt\_mcc\_read\_search\_results\_obj\_id](#ga98814a516a027bdaa3250e93d55309fd) (struct bt\_conn \*conn) |
|  | Search Results Group Object ID. |
| int | [bt\_mcc\_read\_content\_control\_id](#ga77cbf810c35d1a17efce1fae6a941963) (struct bt\_conn \*conn) |
|  | Read Content Control ID. |
| int | [bt\_mcc\_otc\_read\_object\_metadata](#gadf687cb26a6d00bca73e273da583df88) (struct bt\_conn \*conn) |
|  | Read the current object metadata. |
| int | [bt\_mcc\_otc\_read\_icon\_object](#gaba527d8f0307ab11150a5434231c0e7e) (struct bt\_conn \*conn) |
|  | Read the Icon Object. |
| int | [bt\_mcc\_otc\_read\_track\_segments\_object](#gac22e840b65895aa018ab1b4535a87672) (struct bt\_conn \*conn) |
|  | Read the Track Segments Object. |
| int | [bt\_mcc\_otc\_read\_current\_track\_object](#gac4b09a77df52d2681e7652591ca32bf8) (struct bt\_conn \*conn) |
|  | Read the Current Track Object. |
| int | [bt\_mcc\_otc\_read\_next\_track\_object](#ga611c9edebff5b4347ad1241ffd19f49e) (struct bt\_conn \*conn) |
|  | Read the Next Track Object. |
| int | [bt\_mcc\_otc\_read\_current\_group\_object](#ga4b1ebe682ad134795f8a1b494244f8b6) (struct bt\_conn \*conn) |
|  | Read the Current Group Object. |
| int | [bt\_mcc\_otc\_read\_parent\_group\_object](#gae001cb2d701457ce083aa8a0fd5ec518) (struct bt\_conn \*conn) |
|  | Read the Parent Group Object. |
| struct [bt\_ots\_client](structbt__ots__client.md) \* | [bt\_mcc\_otc\_inst](#gaa243806f65c4a37d41f25bcc4f1839fc) (struct bt\_conn \*conn) |
|  | Look up MCC OTC instance. |

## Detailed Description

Bluetooth Media Control Client (MCC) interface.

Updated to the Media Control Profile specification revision 1.0

Since
:   3.0

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#ga50da90a5c351c99494208b44096a61c8)bt\_mcc\_cmd\_ntf\_cb

| typedef void(\* bt\_mcc\_cmd\_ntf\_cb) (struct bt\_conn \*conn, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*ntf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for command notifications.

Called when the media control point is notified

Notifications for commands (i.e. for writes to the media control point) use a different parameter structure than what is used for sending commands (writing to the media control point)

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | ntf | The command notification |

## [◆ ](#gab268faeca207e115ee1be0843ab8c342)bt\_mcc\_discover\_mcs\_cb

| typedef void(\* bt\_mcc\_discover\_mcs\_cb) (struct bt\_conn \*conn, int err) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_discover\_mcs()](#gaa1f9ead03b4cccaff1e3390b8052b0f3).

Called when a media control server is discovered

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |

## [◆ ](#ga9805222315ca6e6df0720233055af10c)bt\_mcc\_otc\_obj\_metadata\_cb

| typedef void(\* bt\_mcc\_otc\_obj\_metadata\_cb) (struct bt\_conn \*conn, int err) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_object\_metadata()](#gadf687cb26a6d00bca73e273da583df88).

Called when object metadata is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |

## [◆ ](#gaf186e6adefa296de4146502665d738b3)bt\_mcc\_otc\_obj\_selected\_cb

| typedef void(\* bt\_mcc\_otc\_obj\_selected\_cb) (struct bt\_conn \*conn, int err) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for object selected.

Called when an object is selected

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |

## [◆ ](#ga0b309ae7ce23834f303c39017ffa4e50)bt\_mcc\_otc\_read\_current\_group\_object\_cb

| typedef void(\* bt\_mcc\_otc\_read\_current\_group\_object\_cb) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_current\_group\_object()](#ga4b1ebe682ad134795f8a1b494244f8b6).

Called when the current group object is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | buf | Buffer containing the object contents |

If err is EMSGSIZE, the object contents have been truncated.

## [◆ ](#gaff887eda3b84cad1052549f23c8dcfbe)bt\_mcc\_otc\_read\_current\_track\_object\_cb

| typedef void(\* bt\_mcc\_otc\_read\_current\_track\_object\_cb) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_current\_track\_object()](#gac4b09a77df52d2681e7652591ca32bf8).

Called when the current track object is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | buf | Buffer containing the object contents |

If err is EMSGSIZE, the object contents have been truncated.

## [◆ ](#ga13bedbb573bc5575ab75fc3ae65c1870)bt\_mcc\_otc\_read\_icon\_object\_cb

| typedef void(\* bt\_mcc\_otc\_read\_icon\_object\_cb) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_icon\_object()](#gaba527d8f0307ab11150a5434231c0e7e).

Called when the icon object is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | buf | Buffer containing the object contents |

If err is EMSGSIZE, the object contents have been truncated.

## [◆ ](#ga920f25e04e1be4ad5f7e220c2e9102b5)bt\_mcc\_otc\_read\_next\_track\_object\_cb

| typedef void(\* bt\_mcc\_otc\_read\_next\_track\_object\_cb) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_next\_track\_object()](#ga611c9edebff5b4347ad1241ffd19f49e).

Called when the next track object is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | buf | Buffer containing the object contents |

If err is EMSGSIZE, the object contents have been truncated.

## [◆ ](#gaca904bacb552792ffd85c6a640f0ba48)bt\_mcc\_otc\_read\_parent\_group\_object\_cb

| typedef void(\* bt\_mcc\_otc\_read\_parent\_group\_object\_cb) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_parent\_group\_object()](#gae001cb2d701457ce083aa8a0fd5ec518).

Called when the parent group object is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | buf | Buffer containing the object contents |

If err is EMSGSIZE, the object contents have been truncated.

## [◆ ](#ga1c4c842879cd8b209080a59d3ba125f8)bt\_mcc\_otc\_read\_track\_segments\_object\_cb

| typedef void(\* bt\_mcc\_otc\_read\_track\_segments\_object\_cb) (struct bt\_conn \*conn, int err, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_otc\_read\_track\_segments\_object()](#gac22e840b65895aa018ab1b4535a87672).

Called when the track segments object is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | buf | Buffer containing the object contents |

If err is EMSGSIZE, the object contents have been truncated.

## [◆ ](#gadb607997fdcb3e57bbfc90790de4b927)bt\_mcc\_read\_content\_control\_id\_cb

| typedef void(\* bt\_mcc\_read\_content\_control\_id\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_content\_control\_id()](#ga77cbf810c35d1a17efce1fae6a941963).

Called when the content control ID is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | ccid | The Content Control ID |

## [◆ ](#ga5f21a1eed4bfe4dfbca40949af895723)bt\_mcc\_read\_current\_group\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_current\_group\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_current\_group\_obj\_id()](#ga8cb43a6947df48113b082d8cc8ccf25c).

Called when the current group object ID is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Current Group Object ID (UINT48) |

## [◆ ](#ga28ac116604248643b0b203b4a314b7b1)bt\_mcc\_read\_current\_track\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_current\_track\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_current\_track\_obj\_id()](#ga5b3a8fb8e8251cf005b34e47619ae7b9).

Called when the current track object ID is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Current Track Object ID (UINT48) |

## [◆ ](#ga471d0491b70e5472e16c3035507761cc)bt\_mcc\_read\_icon\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_icon\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) icon\_id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_icon\_obj\_id()](#ga0e69de33c37957a2b5473df7d3c3f389).

Called when the icon object ID is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | icon\_id | The ID of the Icon Object. This is a UINT48 in a [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |

## [◆ ](#gaaddc4abe38f6ca811967ae6a10d8f8f0)bt\_mcc\_read\_icon\_url\_cb

| typedef void(\* bt\_mcc\_read\_icon\_url\_cb) (struct bt\_conn \*conn, int err, const char \*icon\_url) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_icon\_url()](#ga38733456db6bc6558a511e104577c9c9).

Called when the icon URL is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | icon\_url | The URL of the Icon |

## [◆ ](#ga200a827f4bf5d65570ddabd028269f77)bt\_mcc\_read\_media\_state\_cb

| typedef void(\* bt\_mcc\_read\_media\_state\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_media\_state()](#gac1b440cfa54dd4b6e23bb47bf885f88d).

Called when the media state is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The Media State |

## [◆ ](#ga83d6614d4a0808782b1b4df115b872d2)bt\_mcc\_read\_next\_track\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_next\_track\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for bt\_mcc\_read\_next\_track\_obj\_id\_obj().

Called when the next track object ID is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Next Track Object ID (UINT48) |

## [◆ ](#gab37df36e15132b9235d1093f5aa403cc)bt\_mcc\_read\_opcodes\_supported\_cb

| typedef void(\* bt\_mcc\_read\_opcodes\_supported\_cb) (struct bt\_conn \*conn, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_opcodes\_supported()](#ga692160554947f92e8c81912c5e597086).

Called when the supported opcodes (commands) are read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | opcodes | The supported opcodes |

## [◆ ](#ga48dd365aa637336b9899db4b6986a5e4)bt\_mcc\_read\_parent\_group\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_parent\_group\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_parent\_group\_obj\_id()](#ga3ccd5961cc4c8d82fa988d300e12e1ae).

Called when the parent group object ID is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Parent Group Object ID (UINT48) |

## [◆ ](#ga6f5383be3f344c25361786d903640909)bt\_mcc\_read\_playback\_speed\_cb

| typedef void(\* bt\_mcc\_read\_playback\_speed\_cb) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_playback\_speed()](#gaa566a4c42f0ab0ab6feddf4e25845609).

Called when the playback speed is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | speed | The Playback Speed |

## [◆ ](#gaa943b61848ee43e91d473f6fdd0a604f)bt\_mcc\_read\_player\_name\_cb

| typedef void(\* bt\_mcc\_read\_player\_name\_cb) (struct bt\_conn \*conn, int err, const char \*name) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_player\_name()](#ga724ce71fc88f1ca4bcf209c92c177f36).

Called when the player name is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | name | Player name |

## [◆ ](#gafb0869e0ef5332d39070081efdacf17c)bt\_mcc\_read\_playing\_order\_cb

| typedef void(\* bt\_mcc\_read\_playing\_order\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_playing\_order()](#ga077a134ff1404fb76aa756a5531fd1d7).

Called when the playing order is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | order | The playback order |

## [◆ ](#gac45a2aff295535f70ac4a070e970b7a0)bt\_mcc\_read\_playing\_orders\_supported\_cb

| typedef void(\* bt\_mcc\_read\_playing\_orders\_supported\_cb) (struct bt\_conn \*conn, int err, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_playing\_orders\_supported()](#gaf61f6fcf3f96ccb6f5a72ffaad27dec4).

Called when the supported playing orders are read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | orders | The playing orders supported (bitmap) |

## [◆ ](#ga5a39822a21a6f2aa7a6548c57979a926)bt\_mcc\_read\_search\_results\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_search\_results\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_search\_results\_obj\_id()](#ga98814a516a027bdaa3250e93d55309fd).

Called when the search results object ID is read or notified

Note that the Search Results Object ID value may be zero, in case the characteristic does not exist on the server. (This will be the case if there has not been a successful search.)

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Search Results Object ID (UINT48) |

## [◆ ](#ga3089e6165e8491325f7205279bb5bb83)bt\_mcc\_read\_seeking\_speed\_cb

| typedef void(\* bt\_mcc\_read\_seeking\_speed\_cb) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_seeking\_speed()](#ga366fdfaa23cef9f1c3ba7ddd36a67658).

Called when the seeking speed is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | speed | The Seeking Speed |

## [◆ ](#ga1fbf0b4fd624626127774d2662083875)bt\_mcc\_read\_segments\_obj\_id\_cb

| typedef void(\* bt\_mcc\_read\_segments\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_segments\_obj\_id()](#ga4cb0a95e91d3ec00ede64663a2b932f0).

Called when the track segments object ID is read

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Track Segments Object ID (UINT48) |

## [◆ ](#ga7cdb524ff9c34f24c1740adb9eca072c)bt\_mcc\_read\_track\_duration\_cb

| typedef void(\* bt\_mcc\_read\_track\_duration\_cb) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dur) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_track\_duration()](#ga50a45f043bd2ae1741a120e02e9dc2f5).

Called when the track duration is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | dur | The duration of the track |

## [◆ ](#ga128883c867b10e57d3f2f26a708b7263)bt\_mcc\_read\_track\_position\_cb

| typedef void(\* bt\_mcc\_read\_track\_position\_cb) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_track\_position()](#gaf143098f5dfcfba01df3d6f06472779e).

Called when the track position is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | pos | The Track Position |

## [◆ ](#ga6927860f1803aeade4994610da32d402)bt\_mcc\_read\_track\_title\_cb

| typedef void(\* bt\_mcc\_read\_track\_title\_cb) (struct bt\_conn \*conn, int err, const char \*title) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_read\_track\_title()](#ga7dfa14489a4cea4b00053c9aa75cf373).

Called when the track title is read or notified

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | title | The title of the track |

## [◆ ](#gab168a4c86de444dd066802c4a5fe41c3)bt\_mcc\_search\_ntf\_cb

| typedef void(\* bt\_mcc\_search\_ntf\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for search notifications.

Called when the search control point is notified

Notifications for searches (i.e. for writes to the search control point) use a different parameter structure than what is used for sending searches (writing to the search control point)

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | result\_code | The search notification |

## [◆ ](#gae4c2d1a5c41df1c3535418cc23d48f8e)bt\_mcc\_send\_cmd\_cb

| typedef void(\* bt\_mcc\_send\_cmd\_cb) (struct bt\_conn \*conn, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_send\_cmd()](#ga3f4a538bcf436e4e80b73ed6e077dfa0).

Called when a command is sent, i.e. when the media control point is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | The command sent |

## [◆ ](#ga9489c34b6006df8bd26e626030cab71f)bt\_mcc\_send\_search\_cb

| typedef void(\* bt\_mcc\_send\_search\_cb) (struct bt\_conn \*conn, int err, const struct [mpl\_search](structmpl__search.md) \*search) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_send\_search()](#ga324161056e03195820bbd7cc77ff287d).

Called when a search is sent, i.e. when the search control point is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | search | The search set (or attempted to set) |

## [◆ ](#ga8bbb0d28f7dcf23a30a8ca56d647ac2c)bt\_mcc\_set\_current\_group\_obj\_id\_cb

| typedef void(\* bt\_mcc\_set\_current\_group\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) obj\_id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_set\_current\_group\_obj\_id()](#gae3f385811f852d584595c6e531556aed).

Called when the current group object ID is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | obj\_id | The Object ID (UINT48) set (or attempted to set) |

## [◆ ](#gaf0d619b493a8fb4c00278a0a85bb2529)bt\_mcc\_set\_current\_track\_obj\_id\_cb

| typedef void(\* bt\_mcc\_set\_current\_track\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_set\_current\_track\_obj\_id()](#ga8374ac230c5fe6b5a1bb7fa873fdeb49).

Called when the current track object ID is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Object ID (UINT48) set (or attempted to set) |

## [◆ ](#ga2f3099d097b28ab9c4abf81e19474def)bt\_mcc\_set\_next\_track\_obj\_id\_cb

| typedef void(\* bt\_mcc\_set\_next\_track\_obj\_id\_cb) (struct bt\_conn \*conn, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_set\_next\_track\_obj\_id()](#gafeebcbb0c77d5d4acbe151fd9888d084).

Called when the next track object ID is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | id | The Object ID (UINT48) set (or attempted to set) |

## [◆ ](#ga1322f2ddbb587c70fd23a7ccfc1fc779)bt\_mcc\_set\_playback\_speed\_cb

| typedef void(\* bt\_mcc\_set\_playback\_speed\_cb) (struct bt\_conn \*conn, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_set\_playback\_speed()](#ga1382e5b6000896dc94f6489909301719).

Called when the playback speed is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | speed | The Playback Speed set (or attempted to set) |

## [◆ ](#ga1a12fb89adf29c83bca02f701213c6d7)bt\_mcc\_set\_playing\_order\_cb

| typedef void(\* bt\_mcc\_set\_playing\_order\_cb) (struct bt\_conn \*conn, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_set\_playing\_order()](#ga05295649385c3a337401765627d09553).

Called when the playing order is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | order | The Playing Order set (or attempted to set) |

## [◆ ](#ga1167f5e2ef4a7e78469aefc0cef18bff)bt\_mcc\_set\_track\_position\_cb

| typedef void(\* bt\_mcc\_set\_track\_position\_cb) (struct bt\_conn \*conn, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) pos) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for [bt\_mcc\_set\_track\_position()](#gad324366d33bef6b1ed1c8fc881bf44cf).

Called when the track position is set

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |
    | pos | The Track Position set (or attempted to set) |

## [◆ ](#ga67611a3068284b0c7fbb3ef07dfe7688)bt\_mcc\_track\_changed\_ntf\_cb

| typedef void(\* bt\_mcc\_track\_changed\_ntf\_cb) (struct bt\_conn \*conn, int err) |
| --- |

`#include <[mcc.h](mcc_8h.md)>`

Callback function for track changed notifications.

Called when a track change is notified.

The track changed characteristic is a special case. It can not be read or set, it can only be notified.

Parameters
:   | conn | The connection that was used to initialise the media control client |
    | --- | --- |
    | err | Error value. 0 on success, GATT error or errno on fail |

## Function Documentation

## [◆ ](#gaa1f9ead03b4cccaff1e3390b8052b0f3)bt\_mcc\_discover\_mcs()

| int bt\_mcc\_discover\_mcs | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *subscribe* ) |

`#include <[mcc.h](mcc_8h.md)>`

Discover Media Control Service.

Discover Media Control Service (MCS) on the server given by the connection Optionally subscribe to notifications.

Shall be called once, after media control client initialization and before using other media control client functionality.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | subscribe | Whether to subscribe to notifications |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga94de08bb0a1e1324600e4957b648e92b)bt\_mcc\_init()

| int bt\_mcc\_init | ( | struct [bt\_mcc\_cb](structbt__mcc__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Initialize Media Control Client.

Parameters
:   | cb | Callbacks to be used |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaa243806f65c4a37d41f25bcc4f1839fc)bt\_mcc\_otc\_inst()

| struct [bt\_ots\_client](structbt__ots__client.md) \* bt\_mcc\_otc\_inst | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Look up MCC OTC instance.

Parameters
:   | conn | The connection to the MCC server. |
    | --- | --- |

Returns
:   Pointer to a MCC OTC instance if found else NULL.

## [◆ ](#ga4b1ebe682ad134795f8a1b494244f8b6)bt\_mcc\_otc\_read\_current\_group\_object()

| int bt\_mcc\_otc\_read\_current\_group\_object | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the Current Group Object.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gac4b09a77df52d2681e7652591ca32bf8)bt\_mcc\_otc\_read\_current\_track\_object()

| int bt\_mcc\_otc\_read\_current\_track\_object | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the Current Track Object.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaba527d8f0307ab11150a5434231c0e7e)bt\_mcc\_otc\_read\_icon\_object()

| int bt\_mcc\_otc\_read\_icon\_object | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the Icon Object.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga611c9edebff5b4347ad1241ffd19f49e)bt\_mcc\_otc\_read\_next\_track\_object()

| int bt\_mcc\_otc\_read\_next\_track\_object | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the Next Track Object.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gadf687cb26a6d00bca73e273da583df88)bt\_mcc\_otc\_read\_object\_metadata()

| int bt\_mcc\_otc\_read\_object\_metadata | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the current object metadata.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gae001cb2d701457ce083aa8a0fd5ec518)bt\_mcc\_otc\_read\_parent\_group\_object()

| int bt\_mcc\_otc\_read\_parent\_group\_object | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the Parent Group Object.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gac22e840b65895aa018ab1b4535a87672)bt\_mcc\_otc\_read\_track\_segments\_object()

| int bt\_mcc\_otc\_read\_track\_segments\_object | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read the Track Segments Object.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga77cbf810c35d1a17efce1fae6a941963)bt\_mcc\_read\_content\_control\_id()

| int bt\_mcc\_read\_content\_control\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Content Control ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga8cb43a6947df48113b082d8cc8ccf25c)bt\_mcc\_read\_current\_group\_obj\_id()

| int bt\_mcc\_read\_current\_group\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Current Group Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga5b3a8fb8e8251cf005b34e47619ae7b9)bt\_mcc\_read\_current\_track\_obj\_id()

| int bt\_mcc\_read\_current\_track\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Current Track Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga0e69de33c37957a2b5473df7d3c3f389)bt\_mcc\_read\_icon\_obj\_id()

| int bt\_mcc\_read\_icon\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Icon Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga38733456db6bc6558a511e104577c9c9)bt\_mcc\_read\_icon\_url()

| int bt\_mcc\_read\_icon\_url | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Icon Object URL.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gac1b440cfa54dd4b6e23bb47bf885f88d)bt\_mcc\_read\_media\_state()

| int bt\_mcc\_read\_media\_state | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Media State.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga11e4c02ba0b1fbc197aaf071b82a1eed)bt\_mcc\_read\_next\_track\_obj\_id()

| int bt\_mcc\_read\_next\_track\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Next Track Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga692160554947f92e8c81912c5e597086)bt\_mcc\_read\_opcodes\_supported()

| int bt\_mcc\_read\_opcodes\_supported | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Opcodes Supported.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga3ccd5961cc4c8d82fa988d300e12e1ae)bt\_mcc\_read\_parent\_group\_obj\_id()

| int bt\_mcc\_read\_parent\_group\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Parent Group Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaa566a4c42f0ab0ab6feddf4e25845609)bt\_mcc\_read\_playback\_speed()

| int bt\_mcc\_read\_playback\_speed | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Playback speed.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga724ce71fc88f1ca4bcf209c92c177f36)bt\_mcc\_read\_player\_name()

| int bt\_mcc\_read\_player\_name | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Media Player Name.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga077a134ff1404fb76aa756a5531fd1d7)bt\_mcc\_read\_playing\_order()

| int bt\_mcc\_read\_playing\_order | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Playing Order.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaf61f6fcf3f96ccb6f5a72ffaad27dec4)bt\_mcc\_read\_playing\_orders\_supported()

| int bt\_mcc\_read\_playing\_orders\_supported | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Playing Orders Supported.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga98814a516a027bdaa3250e93d55309fd)bt\_mcc\_read\_search\_results\_obj\_id()

| int bt\_mcc\_read\_search\_results\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Search Results Group Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga366fdfaa23cef9f1c3ba7ddd36a67658)bt\_mcc\_read\_seeking\_speed()

| int bt\_mcc\_read\_seeking\_speed | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Seeking speed.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga4cb0a95e91d3ec00ede64663a2b932f0)bt\_mcc\_read\_segments\_obj\_id()

| int bt\_mcc\_read\_segments\_obj\_id | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Track Segments Object ID.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga50a45f043bd2ae1741a120e02e9dc2f5)bt\_mcc\_read\_track\_duration()

| int bt\_mcc\_read\_track\_duration | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Track Duration.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaf143098f5dfcfba01df3d6f06472779e)bt\_mcc\_read\_track\_position()

| int bt\_mcc\_read\_track\_position | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Track Position.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga7dfa14489a4cea4b00053c9aa75cf373)bt\_mcc\_read\_track\_title()

| int bt\_mcc\_read\_track\_title | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcc.h](mcc_8h.md)>`

Read Track Title.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga3f4a538bcf436e4e80b73ed6e077dfa0)bt\_mcc\_send\_cmd()

| int bt\_mcc\_send\_cmd | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [mpl\_cmd](structmpl__cmd.md) \* | *cmd* ) |

`#include <[mcc.h](mcc_8h.md)>`

Send a command.

Write a command (e.g. "play", "pause") to the server's media control point.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | The command to send |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga324161056e03195820bbd7cc77ff287d)bt\_mcc\_send\_search()

| int bt\_mcc\_send\_search | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [mpl\_search](structmpl__search.md) \* | *search* ) |

`#include <[mcc.h](mcc_8h.md)>`

Send a Search command.

Write a search to the server's search control point.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | search | The search |

Returns
:   0 if success, errno on failure.

## [◆ ](#gae3f385811f852d584595c6e531556aed)bt\_mcc\_set\_current\_group\_obj\_id()

| int bt\_mcc\_set\_current\_group\_obj\_id | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[mcc.h](mcc_8h.md)>`

Set Current Group Object ID.

Set the Current Group to the group given by the `id` parameter

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | id | Object Transfer Service ID (UINT48) of the group to set as the current group |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga8374ac230c5fe6b5a1bb7fa873fdeb49)bt\_mcc\_set\_current\_track\_obj\_id()

| int bt\_mcc\_set\_current\_track\_obj\_id | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[mcc.h](mcc_8h.md)>`

Set Current Track Object ID.

Set the Current Track to the track given by the `id` parameter

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | id | Object Transfer Service ID (UINT48) of the track to set as the current track |

Returns
:   0 if success, errno on failure.

## [◆ ](#gafeebcbb0c77d5d4acbe151fd9888d084)bt\_mcc\_set\_next\_track\_obj\_id()

| int bt\_mcc\_set\_next\_track\_obj\_id | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[mcc.h](mcc_8h.md)>`

Set Next Track Object ID.

Set the Next Track to the track given by the `id` parameter

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | id | Object Transfer Service ID (UINT48) of the track to set as the next track |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga1382e5b6000896dc94f6489909301719)bt\_mcc\_set\_playback\_speed()

| int bt\_mcc\_set\_playback\_speed | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *speed* ) |

`#include <[mcc.h](mcc_8h.md)>`

Set Playback Speed.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | speed | Playback speed |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga05295649385c3a337401765627d09553)bt\_mcc\_set\_playing\_order()

| int bt\_mcc\_set\_playing\_order | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *order* ) |

`#include <[mcc.h](mcc_8h.md)>`

Set Playing Order.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | order | Playing order |

Returns
:   0 if success, errno on failure.

## [◆ ](#gad324366d33bef6b1ed1c8fc881bf44cf)bt\_mcc\_set\_track\_position()

| int bt\_mcc\_set\_track\_position | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *pos* ) |

`#include <[mcc.h](mcc_8h.md)>`

Set Track position.

Parameters
:   | conn | Connection to the peer device |
    | --- | --- |
    | pos | Track position |

Returns
:   0 if success, errno on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
