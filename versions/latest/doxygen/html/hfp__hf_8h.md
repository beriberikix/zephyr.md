---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/hfp__hf_8h.html
original_path: doxygen/html/hfp__hf_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_hf.h File Reference

Handsfree Profile handling.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

[Go to the source code of this file.](hfp__hf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) |
|  | HFP profile application callback. [More...](structbt__hfp__hf__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HFP\_HF\_CODEC\_CVSD](group__bt__hfp.md#ga0e46a981a70dcdecbae119ebb6d61aa0)   0x01 |
| #define | [BT\_HFP\_HF\_CODEC\_MSBC](group__bt__hfp.md#gaea9fb177ae8ba32650dc93f1b2953333)   0x02 |
| #define | [BT\_HFP\_HF\_CODEC\_LC3\_SWB](group__bt__hfp.md#gac8ab2e9ff6c8b9a06ac460f751dec1ad)   0x03 |

| Enumerations | |
| --- | --- |
| enum | [hfp\_hf\_ag\_indicators](group__bt__hfp.md#ga862b201be555821e932f6df5599eaa57) {     [HF\_SERVICE\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8) = 0 , [HF\_CALL\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6) , [HF\_CALL\_SETUP\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de) , [HF\_CALL\_HELD\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf) ,     [HF\_SIGNAL\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0) , [HF\_ROAM\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae) , [HF\_BATTERY\_IND](group__bt__hfp.md#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)   } |

| Functions | |
| --- | --- |
| int | [bt\_hfp\_hf\_register](group__bt__hfp.md#ga2e4a7c05a3ba9a32eab50b9904f7f161) (struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \*cb) |
|  | Register HFP HF profile. |
| int | [bt\_hfp\_hf\_connect](group__bt__hfp.md#ga302e9ed397b056edef518470c6ea1d62) (struct bt\_conn \*conn, struct bt\_hfp\_hf \*\*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Initiate the service level connection establishment procedure. |
| int | [bt\_hfp\_hf\_disconnect](group__bt__hfp.md#gaf5e7ef119731c0dc35bec61fb7c34774) (struct bt\_hfp\_hf \*hf) |
|  | Release the service level connection. |
| int | [bt\_hfp\_hf\_cli](group__bt__hfp.md#ga64ac1971dc7b1dacf6685bdc0c71e34c) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Handsfree HF enable/disable Calling Line Identification (CLI) Notification. |
| int | [bt\_hfp\_hf\_vgm](group__bt__hfp.md#ga0602cee7a90ca4afe90b65d748024472) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | Handsfree HF report Gain of Microphone (VGM). |
| int | [bt\_hfp\_hf\_vgs](group__bt__hfp.md#ga0c1c35b3117f78f43a6300d4ff7dd18b) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | Handsfree HF report Gain of Speaker (VGS). |
| int | [bt\_hfp\_hf\_get\_operator](group__bt__hfp.md#gaaa9fbdceec140f274fc88c063a4cd4b8) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF requests currently selected operator. |
| int | [bt\_hfp\_hf\_accept](group__bt__hfp.md#ga5bad80355fd7903abcee84437d399829) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF accept the incoming call. |
| int | [bt\_hfp\_hf\_reject](group__bt__hfp.md#gac4e3d88b80b69840d52050dcd72c9ab3) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF reject the incoming call. |
| int | [bt\_hfp\_hf\_terminate](group__bt__hfp.md#gabbce5fbf0dec27e1c5a4da144fbfc9c1) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF terminate the incoming call. |
| int | [bt\_hfp\_hf\_hold\_incoming](group__bt__hfp.md#ga540bf6ec23c632b3f736e6302ef32ebd) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF put the incoming call on hold. |
| int | [bt\_hfp\_hf\_query\_respond\_hold\_status](group__bt__hfp.md#ga70e086f6a02cb116317a8e80f76abf6d) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF query respond and hold status of AG. |
| int | [bt\_hfp\_hf\_number\_call](group__bt__hfp.md#gac57d7188e3f8b6e1e28d2a55c2567dbf) (struct bt\_hfp\_hf \*hf, const char \*number) |
|  | Handsfree HF phone number call. |
| int | [bt\_hfp\_hf\_memory\_dial](group__bt__hfp.md#gabacb666eb0f43db8614413a4ae0ce60a) (struct bt\_hfp\_hf \*hf, const char \*location) |
|  | Handsfree HF memory dialing call. |
| int | [bt\_hfp\_hf\_redial](group__bt__hfp.md#ga9611012a35df66fac324b99b16e5d958) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF redial last number. |
| int | [bt\_hfp\_hf\_audio\_connect](group__bt__hfp.md#gad29bf40953faf638cc08acf919eb8f4f) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF setup audio connection. |
| int | [bt\_hfp\_hf\_select\_codec](group__bt__hfp.md#ga34649dbecca2513c0b5bcd0e109b2551) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_id) |
|  | Handsfree HF set selected codec id. |
| int | [bt\_hfp\_hf\_set\_codecs](group__bt__hfp.md#ga91fc2204f50df07567f87a2b7a18e69f) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_ids) |
|  | Handsfree HF set supported codec ids. |
| int | [bt\_hfp\_hf\_turn\_off\_ecnr](group__bt__hfp.md#ga7f37a9c009b4e55b7060d635c5b0c67b) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF turns off AG's EC and NR. |
| int | [bt\_hfp\_hf\_call\_waiting\_notify](group__bt__hfp.md#ga3afb0d82551708975dbeb9c903c3d1fb) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Handsfree HF enable/disable call waiting notification. |
| int | [bt\_hfp\_hf\_release\_all\_held](group__bt__hfp.md#ga06e7e93578601693fa377a240e0d18a7) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF release all held calls. |
| int | [bt\_hfp\_hf\_set\_udub](group__bt__hfp.md#ga7389e5723e01b661b5e9c9d2114918b8) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF set User Determined User Busy (UDUB) for a waiting call. |
| int | [bt\_hfp\_hf\_release\_active\_accept\_other](group__bt__hfp.md#ga36be4ff5fd805c4413ba90b1f62b9143) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF release all active calls and accept other call. |
| int | [bt\_hfp\_hf\_hold\_active\_accept\_other](group__bt__hfp.md#ga40de46a6651eb85aa6d04ad66f528803) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF hold all active calls and accept other call. |
| int | [bt\_hfp\_hf\_join\_conversation](group__bt__hfp.md#ga04d9fe3524c9522e98830507886bdfc6) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF add a held call to the conversation. |
| int | [bt\_hfp\_hf\_explicit\_call\_transfer](group__bt__hfp.md#ga2b48a0938e65899417b2f3ab1fa4c548) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF explicit call transfer. |
| int | [bt\_hfp\_hf\_release\_specified\_call](group__bt__hfp.md#ga1ad888c3b967d3f9b2e5ccee303b9ad7) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF release call with specified index. |
| int | [bt\_hfp\_hf\_private\_consultation\_mode](group__bt__hfp.md#gac3c038818cda3645eaadc5374d18c3ee) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF request private consultation mode with specified call. |
| int | [bt\_hfp\_hf\_voice\_recognition](group__bt__hfp.md#gaeed952ce163ef2466ece04af24b76a28) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
|  | Handsfree HF enable/disable the voice recognition function. |
| int | [bt\_hfp\_hf\_ready\_to\_accept\_audio](group__bt__hfp.md#ga3f6b43bf53fa04a6e71e883dc38f988b) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF indicate that the HF is ready to accept audio. |
| int | [bt\_hfp\_hf\_request\_phone\_number](group__bt__hfp.md#ga92d89b0b37186688e86091a7a8015245) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF attach a phone number for a voice tag. |
| int | [bt\_hfp\_hf\_transmit\_dtmf\_code](group__bt__hfp.md#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0) (struct bt\_hfp\_hf\_call \*call, char code) |
|  | Handsfree HF Transmit A specific DTMF Code. |
| int | [bt\_hfp\_hf\_query\_subscriber](group__bt__hfp.md#gad5dab4dcb66d52a80e0689a86de5fec3) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF Query Subscriber Number Information. |
| int | [bt\_hfp\_hf\_indicator\_status](group__bt__hfp.md#gab743d3e14fa13b71ddaf26d46cf41fb3) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Handsfree HF set AG indicator activated/deactivated status. |
| int | [bt\_hfp\_hf\_enhanced\_safety](group__bt__hfp.md#gab6710ce433812c3bf785b787008c36be) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Handsfree HF enable/disable enhanced safety. |
| int | [bt\_hfp\_hf\_battery](group__bt__hfp.md#ga2f0e6012503a9b59b03a0fb508d12f88) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Handsfree HF remaining battery level. |

## Detailed Description

Handsfree Profile handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_hf.h](hfp__hf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
