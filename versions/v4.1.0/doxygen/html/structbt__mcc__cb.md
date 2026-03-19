---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mcc__cb.html
original_path: doxygen/html/structbt__mcc__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mcc\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Media Control Client (MCC)](group__bt__mcc.md)

Media control client callbacks.
[More...](#details)

`#include <[mcc.h](mcc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_mcc\_discover\_mcs\_cb](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342) | [discover\_mcs](#a2f48a0e0b891131347b0ddc2cb5a8ba7) |
|  | Callback when discovery has finished. |
| [bt\_mcc\_read\_player\_name\_cb](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f) | [read\_player\_name](#aeea1ef17b3b1e24c965d71f210952079) |
|  | Callback when reading the player name. |
| [bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc) | [read\_icon\_obj\_id](#a00acb676c73ebbad2b0180b3e8373150) |
|  | Callback when reading the icon object ID. |
| [bt\_mcc\_read\_icon\_url\_cb](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0) | [read\_icon\_url](#a8c7b5954e286d074a94a39bee266082c) |
|  | Callback when reading the icon URL. |
| [bt\_mcc\_track\_changed\_ntf\_cb](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688) | [track\_changed\_ntf](#abb7769b73564a22645bfe6b11f239637) |
|  | Callback when getting a track changed notification. |
| [bt\_mcc\_read\_track\_title\_cb](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402) | [read\_track\_title](#a3975e296b67eb244bf92254e9776ea3c) |
|  | Callback when reading the track title. |
| [bt\_mcc\_read\_track\_duration\_cb](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c) | [read\_track\_duration](#a85268d9ce708aef01aa528aaedf0f7e0) |
|  | Callback when reading the track duration. |
| [bt\_mcc\_read\_track\_position\_cb](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263) | [read\_track\_position](#ad1636e717ef5039586b7a1462041e888) |
|  | Callback when reading the track position. |
| [bt\_mcc\_set\_track\_position\_cb](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff) | [set\_track\_position](#affa57da8f325dce8298d097af38d0d62) |
|  | Callback when setting the track position. |
| [bt\_mcc\_read\_playback\_speed\_cb](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909) | [read\_playback\_speed](#a47f8d92b18b0e4ffb3aacde05e7cb410) |
|  | Callback when reading the playback speed. |
| [bt\_mcc\_set\_playback\_speed\_cb](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779) | [set\_playback\_speed](#a5f87b5d07241b4124911be0cd6c43b37) |
|  | Callback when setting the playback speed. |
| [bt\_mcc\_read\_seeking\_speed\_cb](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83) | [read\_seeking\_speed](#a75c8e63baf45a119e9007f246362ab8d) |
|  | Callback when reading the seeking speed. |
| [bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875) | [read\_segments\_obj\_id](#a810ceaee44fcbdec90a1ee227b6974df) |
|  | Callback when reading the segments object ID. |
| [bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1) | [read\_current\_track\_obj\_id](#a46bd2c23d92d8362cdf9ad4862b78407) |
|  | Callback when reading the current track object ID. |
| [bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529) | [set\_current\_track\_obj\_id](#ac9e182bbdd9671c5caee5bcd42198d90) |
|  | Callback when setting the current track object ID. |
| [bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2) | [read\_next\_track\_obj\_id](#a540797123f8968b49a6e98b30ea534c8) |
|  | Callback when reading the next track object ID. |
| [bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def) | [set\_next\_track\_obj\_id](#a4f2ea54d6c60beb28feab7b6453aec7c) |
|  | Callback when setting the next track object ID. |
| [bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723) | [read\_current\_group\_obj\_id](#a0e7757b6f911456feaca931cd33f117f) |
|  | Callback when reading the current group object ID. |
| [bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c) | [set\_current\_group\_obj\_id](#ad8d3eff0cc183797280c9f668a840add) |
|  | Callback when setting the current group object ID. |
| [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4) | [read\_parent\_group\_obj\_id](#a87583247634728d3d9af7eb411d088a7) |
|  | Callback when reading the parent group object ID. |
| [bt\_mcc\_read\_playing\_order\_cb](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c) | [read\_playing\_order](#a3538beef41edd96b8557b43c1266078b) |
|  | Callback when reading the playing order. |
| [bt\_mcc\_set\_playing\_order\_cb](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7) | [set\_playing\_order](#a00a0ba5ed665ef7fc2ca861d985ccd64) |
|  | Callback when setting the playing order. |
| [bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0) | [read\_playing\_orders\_supported](#a929d7b8fc925961048d5ff5e70a5126e) |
|  | Callback when reading the supported playing orders. |
| [bt\_mcc\_read\_media\_state\_cb](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77) | [read\_media\_state](#a38e4682608c7d7ff6c44431a6bdab3af) |
|  | Callback when reading the media state. |
| [bt\_mcc\_send\_cmd\_cb](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e) | [send\_cmd](#a90e62e90752087da36122a65f6c9ed4e) |
|  | Callback when sending a command. |
| [bt\_mcc\_cmd\_ntf\_cb](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8) | [cmd\_ntf](#a835f60ad32edc4311a624e779972f0d5) |
|  | Callback command notifications. |
| [bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc) | [read\_opcodes\_supported](#ad7ddcae67bf71030ac2d8438ac2e863f) |
|  | Callback when reading the supported opcodes. |
| [bt\_mcc\_send\_search\_cb](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f) | [send\_search](#a1c7277f390f6b478090611be9e82a4f8) |
|  | Callback when sending the a search query. |
| [bt\_mcc\_search\_ntf\_cb](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3) | [search\_ntf](#a9f7f3424aa230a8752f40a40b82b0b66) |
|  | Callback when receiving a search notification. |
| [bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926) | [read\_search\_results\_obj\_id](#aaa2bdfb99e5cd7c2a0d0c800533e8491) |
|  | Callback when reading the search results object ID. |
| [bt\_mcc\_read\_content\_control\_id\_cb](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927) | [read\_content\_control\_id](#ae4d0e2e4df695352e8d2ed76db1f420e) |
|  | Callback when reading the content control ID. |
| [bt\_mcc\_otc\_obj\_selected\_cb](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3) | [otc\_obj\_selected](#a17ebc9dbddd714d99b599b2a683ab771) |
|  | Callback when selecting an object. |
| [bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c) | [otc\_obj\_metadata](#af1c9664a2459550af0a6ed611fd17263) |
|  | Callback when receiving the current object metadata. |
| [bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870) | [otc\_icon\_object](#a054e0cfb27c01f43d499a2c44788cb73) |
|  | Callback when reading the current icon object. |
| [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8) | [otc\_track\_segments\_object](#a2c1b570ce8d83c3f20eb99807263a5cd) |
|  | Callback when reading the track segments object. |
| [bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe) | [otc\_current\_track\_object](#ad13669e60992a1a407534f387efd1da8) |
|  | Callback when reading the current track object. |
| [bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5) | [otc\_next\_track\_object](#a52724924ab19f59cc936344ebe13d437) |
|  | Callback when reading the next track object. |
| [bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50) | [otc\_current\_group\_object](#ac0e382f1117f983e7a2178fde274d460) |
|  | Callback when reading the current group object. |
| [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48) | [otc\_parent\_group\_object](#a872d0322ba3889f1f7d32e8966b53624) |
|  | Callback when reading the parent group object. |

## Detailed Description

Media control client callbacks.

## Field Documentation

## [◆ ](#a835f60ad32edc4311a624e779972f0d5)cmd\_ntf

| [bt\_mcc\_cmd\_ntf\_cb](group__bt__mcc.md#ga50da90a5c351c99494208b44096a61c8) bt\_mcc\_cb::cmd\_ntf |
| --- |

Callback command notifications.

## [◆ ](#a2f48a0e0b891131347b0ddc2cb5a8ba7)discover\_mcs

| [bt\_mcc\_discover\_mcs\_cb](group__bt__mcc.md#gab268faeca207e115ee1be0843ab8c342) bt\_mcc\_cb::discover\_mcs |
| --- |

Callback when discovery has finished.

## [◆ ](#ac0e382f1117f983e7a2178fde274d460)otc\_current\_group\_object

| [bt\_mcc\_otc\_read\_current\_group\_object\_cb](group__bt__mcc.md#ga0b309ae7ce23834f303c39017ffa4e50) bt\_mcc\_cb::otc\_current\_group\_object |
| --- |

Callback when reading the current group object.

## [◆ ](#ad13669e60992a1a407534f387efd1da8)otc\_current\_track\_object

| [bt\_mcc\_otc\_read\_current\_track\_object\_cb](group__bt__mcc.md#gaff887eda3b84cad1052549f23c8dcfbe) bt\_mcc\_cb::otc\_current\_track\_object |
| --- |

Callback when reading the current track object.

## [◆ ](#a054e0cfb27c01f43d499a2c44788cb73)otc\_icon\_object

| [bt\_mcc\_otc\_read\_icon\_object\_cb](group__bt__mcc.md#ga13bedbb573bc5575ab75fc3ae65c1870) bt\_mcc\_cb::otc\_icon\_object |
| --- |

Callback when reading the current icon object.

## [◆ ](#a52724924ab19f59cc936344ebe13d437)otc\_next\_track\_object

| [bt\_mcc\_otc\_read\_next\_track\_object\_cb](group__bt__mcc.md#ga920f25e04e1be4ad5f7e220c2e9102b5) bt\_mcc\_cb::otc\_next\_track\_object |
| --- |

Callback when reading the next track object.

## [◆ ](#af1c9664a2459550af0a6ed611fd17263)otc\_obj\_metadata

| [bt\_mcc\_otc\_obj\_metadata\_cb](group__bt__mcc.md#ga9805222315ca6e6df0720233055af10c) bt\_mcc\_cb::otc\_obj\_metadata |
| --- |

Callback when receiving the current object metadata.

## [◆ ](#a17ebc9dbddd714d99b599b2a683ab771)otc\_obj\_selected

| [bt\_mcc\_otc\_obj\_selected\_cb](group__bt__mcc.md#gaf186e6adefa296de4146502665d738b3) bt\_mcc\_cb::otc\_obj\_selected |
| --- |

Callback when selecting an object.

## [◆ ](#a872d0322ba3889f1f7d32e8966b53624)otc\_parent\_group\_object

| [bt\_mcc\_otc\_read\_parent\_group\_object\_cb](group__bt__mcc.md#gaca904bacb552792ffd85c6a640f0ba48) bt\_mcc\_cb::otc\_parent\_group\_object |
| --- |

Callback when reading the parent group object.

## [◆ ](#a2c1b570ce8d83c3f20eb99807263a5cd)otc\_track\_segments\_object

| [bt\_mcc\_otc\_read\_track\_segments\_object\_cb](group__bt__mcc.md#ga1c4c842879cd8b209080a59d3ba125f8) bt\_mcc\_cb::otc\_track\_segments\_object |
| --- |

Callback when reading the track segments object.

## [◆ ](#ae4d0e2e4df695352e8d2ed76db1f420e)read\_content\_control\_id

| [bt\_mcc\_read\_content\_control\_id\_cb](group__bt__mcc.md#gadb607997fdcb3e57bbfc90790de4b927) bt\_mcc\_cb::read\_content\_control\_id |
| --- |

Callback when reading the content control ID.

## [◆ ](#a0e7757b6f911456feaca931cd33f117f)read\_current\_group\_obj\_id

| [bt\_mcc\_read\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga5f21a1eed4bfe4dfbca40949af895723) bt\_mcc\_cb::read\_current\_group\_obj\_id |
| --- |

Callback when reading the current group object ID.

## [◆ ](#a46bd2c23d92d8362cdf9ad4862b78407)read\_current\_track\_obj\_id

| [bt\_mcc\_read\_current\_track\_obj\_id\_cb](group__bt__mcc.md#ga28ac116604248643b0b203b4a314b7b1) bt\_mcc\_cb::read\_current\_track\_obj\_id |
| --- |

Callback when reading the current track object ID.

## [◆ ](#a00acb676c73ebbad2b0180b3e8373150)read\_icon\_obj\_id

| [bt\_mcc\_read\_icon\_obj\_id\_cb](group__bt__mcc.md#ga471d0491b70e5472e16c3035507761cc) bt\_mcc\_cb::read\_icon\_obj\_id |
| --- |

Callback when reading the icon object ID.

## [◆ ](#a8c7b5954e286d074a94a39bee266082c)read\_icon\_url

| [bt\_mcc\_read\_icon\_url\_cb](group__bt__mcc.md#gaaddc4abe38f6ca811967ae6a10d8f8f0) bt\_mcc\_cb::read\_icon\_url |
| --- |

Callback when reading the icon URL.

## [◆ ](#a38e4682608c7d7ff6c44431a6bdab3af)read\_media\_state

| [bt\_mcc\_read\_media\_state\_cb](group__bt__mcc.md#ga200a827f4bf5d65570ddabd028269f77) bt\_mcc\_cb::read\_media\_state |
| --- |

Callback when reading the media state.

## [◆ ](#a540797123f8968b49a6e98b30ea534c8)read\_next\_track\_obj\_id

| [bt\_mcc\_read\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga83d6614d4a0808782b1b4df115b872d2) bt\_mcc\_cb::read\_next\_track\_obj\_id |
| --- |

Callback when reading the next track object ID.

## [◆ ](#ad7ddcae67bf71030ac2d8438ac2e863f)read\_opcodes\_supported

| [bt\_mcc\_read\_opcodes\_supported\_cb](group__bt__mcc.md#gab37df36e15132b9235d1093f5aa403cc) bt\_mcc\_cb::read\_opcodes\_supported |
| --- |

Callback when reading the supported opcodes.

## [◆ ](#a87583247634728d3d9af7eb411d088a7)read\_parent\_group\_obj\_id

| [bt\_mcc\_read\_parent\_group\_obj\_id\_cb](group__bt__mcc.md#ga48dd365aa637336b9899db4b6986a5e4) bt\_mcc\_cb::read\_parent\_group\_obj\_id |
| --- |

Callback when reading the parent group object ID.

## [◆ ](#a47f8d92b18b0e4ffb3aacde05e7cb410)read\_playback\_speed

| [bt\_mcc\_read\_playback\_speed\_cb](group__bt__mcc.md#ga6f5383be3f344c25361786d903640909) bt\_mcc\_cb::read\_playback\_speed |
| --- |

Callback when reading the playback speed.

## [◆ ](#aeea1ef17b3b1e24c965d71f210952079)read\_player\_name

| [bt\_mcc\_read\_player\_name\_cb](group__bt__mcc.md#gaa943b61848ee43e91d473f6fdd0a604f) bt\_mcc\_cb::read\_player\_name |
| --- |

Callback when reading the player name.

## [◆ ](#a3538beef41edd96b8557b43c1266078b)read\_playing\_order

| [bt\_mcc\_read\_playing\_order\_cb](group__bt__mcc.md#gafb0869e0ef5332d39070081efdacf17c) bt\_mcc\_cb::read\_playing\_order |
| --- |

Callback when reading the playing order.

## [◆ ](#a929d7b8fc925961048d5ff5e70a5126e)read\_playing\_orders\_supported

| [bt\_mcc\_read\_playing\_orders\_supported\_cb](group__bt__mcc.md#gac45a2aff295535f70ac4a070e970b7a0) bt\_mcc\_cb::read\_playing\_orders\_supported |
| --- |

Callback when reading the supported playing orders.

## [◆ ](#aaa2bdfb99e5cd7c2a0d0c800533e8491)read\_search\_results\_obj\_id

| [bt\_mcc\_read\_search\_results\_obj\_id\_cb](group__bt__mcc.md#ga5a39822a21a6f2aa7a6548c57979a926) bt\_mcc\_cb::read\_search\_results\_obj\_id |
| --- |

Callback when reading the search results object ID.

## [◆ ](#a75c8e63baf45a119e9007f246362ab8d)read\_seeking\_speed

| [bt\_mcc\_read\_seeking\_speed\_cb](group__bt__mcc.md#ga3089e6165e8491325f7205279bb5bb83) bt\_mcc\_cb::read\_seeking\_speed |
| --- |

Callback when reading the seeking speed.

## [◆ ](#a810ceaee44fcbdec90a1ee227b6974df)read\_segments\_obj\_id

| [bt\_mcc\_read\_segments\_obj\_id\_cb](group__bt__mcc.md#ga1fbf0b4fd624626127774d2662083875) bt\_mcc\_cb::read\_segments\_obj\_id |
| --- |

Callback when reading the segments object ID.

## [◆ ](#a85268d9ce708aef01aa528aaedf0f7e0)read\_track\_duration

| [bt\_mcc\_read\_track\_duration\_cb](group__bt__mcc.md#ga7cdb524ff9c34f24c1740adb9eca072c) bt\_mcc\_cb::read\_track\_duration |
| --- |

Callback when reading the track duration.

## [◆ ](#ad1636e717ef5039586b7a1462041e888)read\_track\_position

| [bt\_mcc\_read\_track\_position\_cb](group__bt__mcc.md#ga128883c867b10e57d3f2f26a708b7263) bt\_mcc\_cb::read\_track\_position |
| --- |

Callback when reading the track position.

## [◆ ](#a3975e296b67eb244bf92254e9776ea3c)read\_track\_title

| [bt\_mcc\_read\_track\_title\_cb](group__bt__mcc.md#ga6927860f1803aeade4994610da32d402) bt\_mcc\_cb::read\_track\_title |
| --- |

Callback when reading the track title.

## [◆ ](#a9f7f3424aa230a8752f40a40b82b0b66)search\_ntf

| [bt\_mcc\_search\_ntf\_cb](group__bt__mcc.md#gab168a4c86de444dd066802c4a5fe41c3) bt\_mcc\_cb::search\_ntf |
| --- |

Callback when receiving a search notification.

## [◆ ](#a90e62e90752087da36122a65f6c9ed4e)send\_cmd

| [bt\_mcc\_send\_cmd\_cb](group__bt__mcc.md#gae4c2d1a5c41df1c3535418cc23d48f8e) bt\_mcc\_cb::send\_cmd |
| --- |

Callback when sending a command.

## [◆ ](#a1c7277f390f6b478090611be9e82a4f8)send\_search

| [bt\_mcc\_send\_search\_cb](group__bt__mcc.md#ga9489c34b6006df8bd26e626030cab71f) bt\_mcc\_cb::send\_search |
| --- |

Callback when sending the a search query.

## [◆ ](#ad8d3eff0cc183797280c9f668a840add)set\_current\_group\_obj\_id

| [bt\_mcc\_set\_current\_group\_obj\_id\_cb](group__bt__mcc.md#ga8bbb0d28f7dcf23a30a8ca56d647ac2c) bt\_mcc\_cb::set\_current\_group\_obj\_id |
| --- |

Callback when setting the current group object ID.

## [◆ ](#ac9e182bbdd9671c5caee5bcd42198d90)set\_current\_track\_obj\_id

| [bt\_mcc\_set\_current\_track\_obj\_id\_cb](group__bt__mcc.md#gaf0d619b493a8fb4c00278a0a85bb2529) bt\_mcc\_cb::set\_current\_track\_obj\_id |
| --- |

Callback when setting the current track object ID.

## [◆ ](#a4f2ea54d6c60beb28feab7b6453aec7c)set\_next\_track\_obj\_id

| [bt\_mcc\_set\_next\_track\_obj\_id\_cb](group__bt__mcc.md#ga2f3099d097b28ab9c4abf81e19474def) bt\_mcc\_cb::set\_next\_track\_obj\_id |
| --- |

Callback when setting the next track object ID.

## [◆ ](#a5f87b5d07241b4124911be0cd6c43b37)set\_playback\_speed

| [bt\_mcc\_set\_playback\_speed\_cb](group__bt__mcc.md#ga1322f2ddbb587c70fd23a7ccfc1fc779) bt\_mcc\_cb::set\_playback\_speed |
| --- |

Callback when setting the playback speed.

## [◆ ](#a00a0ba5ed665ef7fc2ca861d985ccd64)set\_playing\_order

| [bt\_mcc\_set\_playing\_order\_cb](group__bt__mcc.md#ga1a12fb89adf29c83bca02f701213c6d7) bt\_mcc\_cb::set\_playing\_order |
| --- |

Callback when setting the playing order.

## [◆ ](#affa57da8f325dce8298d097af38d0d62)set\_track\_position

| [bt\_mcc\_set\_track\_position\_cb](group__bt__mcc.md#ga1167f5e2ef4a7e78469aefc0cef18bff) bt\_mcc\_cb::set\_track\_position |
| --- |

Callback when setting the track position.

## [◆ ](#abb7769b73564a22645bfe6b11f239637)track\_changed\_ntf

| [bt\_mcc\_track\_changed\_ntf\_cb](group__bt__mcc.md#ga67611a3068284b0c7fbb3ef07dfe7688) bt\_mcc\_cb::track\_changed\_ntf |
| --- |

Callback when getting a track changed notification.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[mcc.h](mcc_8h_source.md)

- [bt\_mcc\_cb](structbt__mcc__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
