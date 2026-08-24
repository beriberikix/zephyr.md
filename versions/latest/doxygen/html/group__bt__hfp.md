---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__bt__hfp.html
original_path: doxygen/html/group__bt__hfp.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hands Free Profile (HFP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Hands Free Profile (HFP).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) |
|  | HFP profile application callback. [More...](structbt__hfp__hf__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HFP\_HF\_CODEC\_CVSD](#ga0e46a981a70dcdecbae119ebb6d61aa0)   0x01 |
| #define | [BT\_HFP\_HF\_CODEC\_MSBC](#gaea9fb177ae8ba32650dc93f1b2953333)   0x02 |
| #define | [BT\_HFP\_HF\_CODEC\_LC3\_SWB](#gac8ab2e9ff6c8b9a06ac460f751dec1ad)   0x03 |

| Enumerations | |
| --- | --- |
| enum | [hfp\_hf\_ag\_indicators](#ga862b201be555821e932f6df5599eaa57) {     [HF\_SERVICE\_IND](#gga862b201be555821e932f6df5599eaa57adb3fae0b3684e8d035e195a91d24deb8) = 0 , [HF\_CALL\_IND](#gga862b201be555821e932f6df5599eaa57ad8620b141e11f48b46b9cd5ef1842fe6) , [HF\_CALL\_SETUP\_IND](#gga862b201be555821e932f6df5599eaa57a24ceb35eba4e18dbde198b77a7db98de) , [HF\_CALL\_HELD\_IND](#gga862b201be555821e932f6df5599eaa57ad0cfee8ab087438502689d12cafa39cf) ,     [HF\_SIGNAL\_IND](#gga862b201be555821e932f6df5599eaa57ac5055465440ffe897930cbfdabb7c3d0) , [HF\_ROAM\_IND](#gga862b201be555821e932f6df5599eaa57a3f9c27a235db99073918a904d6902eae) , [HF\_BATTERY\_IND](#gga862b201be555821e932f6df5599eaa57a1444cacc3f0307e7b53a0375807668c5)   } |

| Functions | |
| --- | --- |
| int | [bt\_hfp\_hf\_register](#ga2e4a7c05a3ba9a32eab50b9904f7f161) (struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \*cb) |
|  | Register HFP HF profile. |
| int | [bt\_hfp\_hf\_connect](#ga302e9ed397b056edef518470c6ea1d62) (struct bt\_conn \*conn, struct bt\_hfp\_hf \*\*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Initiate the service level connection establishment procedure. |
| int | [bt\_hfp\_hf\_disconnect](#gaf5e7ef119731c0dc35bec61fb7c34774) (struct bt\_hfp\_hf \*hf) |
|  | Release the service level connection. |
| int | [bt\_hfp\_hf\_cli](#ga64ac1971dc7b1dacf6685bdc0c71e34c) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Handsfree HF enable/disable Calling Line Identification (CLI) Notification. |
| int | [bt\_hfp\_hf\_vgm](#ga0602cee7a90ca4afe90b65d748024472) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | Handsfree HF report Gain of Microphone (VGM). |
| int | [bt\_hfp\_hf\_vgs](#ga0c1c35b3117f78f43a6300d4ff7dd18b) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | Handsfree HF report Gain of Speaker (VGS). |
| int | [bt\_hfp\_hf\_get\_operator](#gaaa9fbdceec140f274fc88c063a4cd4b8) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF requests currently selected operator. |
| int | [bt\_hfp\_hf\_accept](#ga5bad80355fd7903abcee84437d399829) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF accept the incoming call. |
| int | [bt\_hfp\_hf\_reject](#gac4e3d88b80b69840d52050dcd72c9ab3) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF reject the incoming call. |
| int | [bt\_hfp\_hf\_terminate](#gabbce5fbf0dec27e1c5a4da144fbfc9c1) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF terminate the incoming call. |
| int | [bt\_hfp\_hf\_hold\_incoming](#ga540bf6ec23c632b3f736e6302ef32ebd) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF put the incoming call on hold. |
| int | [bt\_hfp\_hf\_query\_respond\_hold\_status](#ga70e086f6a02cb116317a8e80f76abf6d) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF query respond and hold status of AG. |
| int | [bt\_hfp\_hf\_number\_call](#gac57d7188e3f8b6e1e28d2a55c2567dbf) (struct bt\_hfp\_hf \*hf, const char \*number) |
|  | Handsfree HF phone number call. |
| int | [bt\_hfp\_hf\_memory\_dial](#gabacb666eb0f43db8614413a4ae0ce60a) (struct bt\_hfp\_hf \*hf, const char \*location) |
|  | Handsfree HF memory dialing call. |
| int | [bt\_hfp\_hf\_redial](#ga9611012a35df66fac324b99b16e5d958) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF redial last number. |
| int | [bt\_hfp\_hf\_audio\_connect](#gad29bf40953faf638cc08acf919eb8f4f) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF setup audio connection. |
| int | [bt\_hfp\_hf\_select\_codec](#ga34649dbecca2513c0b5bcd0e109b2551) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_id) |
|  | Handsfree HF set selected codec id. |
| int | [bt\_hfp\_hf\_set\_codecs](#ga91fc2204f50df07567f87a2b7a18e69f) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_ids) |
|  | Handsfree HF set supported codec ids. |
| int | [bt\_hfp\_hf\_turn\_off\_ecnr](#ga7f37a9c009b4e55b7060d635c5b0c67b) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF turns off AG's EC and NR. |
| int | [bt\_hfp\_hf\_call\_waiting\_notify](#ga3afb0d82551708975dbeb9c903c3d1fb) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Handsfree HF enable/disable call waiting notification. |
| int | [bt\_hfp\_hf\_release\_all\_held](#ga06e7e93578601693fa377a240e0d18a7) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF release all held calls. |
| int | [bt\_hfp\_hf\_set\_udub](#ga7389e5723e01b661b5e9c9d2114918b8) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF set User Determined User Busy (UDUB) for a waiting call. |
| int | [bt\_hfp\_hf\_release\_active\_accept\_other](#ga36be4ff5fd805c4413ba90b1f62b9143) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF release all active calls and accept other call. |
| int | [bt\_hfp\_hf\_hold\_active\_accept\_other](#ga40de46a6651eb85aa6d04ad66f528803) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF hold all active calls and accept other call. |
| int | [bt\_hfp\_hf\_join\_conversation](#ga04d9fe3524c9522e98830507886bdfc6) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF add a held call to the conversation. |
| int | [bt\_hfp\_hf\_explicit\_call\_transfer](#ga2b48a0938e65899417b2f3ab1fa4c548) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF explicit call transfer. |
| int | [bt\_hfp\_hf\_release\_specified\_call](#ga1ad888c3b967d3f9b2e5ccee303b9ad7) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF release call with specified index. |
| int | [bt\_hfp\_hf\_private\_consultation\_mode](#gac3c038818cda3645eaadc5374d18c3ee) (struct bt\_hfp\_hf\_call \*call) |
|  | Handsfree HF request private consultation mode with specified call. |
| int | [bt\_hfp\_hf\_voice\_recognition](#gaeed952ce163ef2466ece04af24b76a28) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
|  | Handsfree HF enable/disable the voice recognition function. |
| int | [bt\_hfp\_hf\_ready\_to\_accept\_audio](#ga3f6b43bf53fa04a6e71e883dc38f988b) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF indicate that the HF is ready to accept audio. |
| int | [bt\_hfp\_hf\_request\_phone\_number](#ga92d89b0b37186688e86091a7a8015245) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF attach a phone number for a voice tag. |
| int | [bt\_hfp\_hf\_transmit\_dtmf\_code](#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0) (struct bt\_hfp\_hf\_call \*call, char code) |
|  | Handsfree HF Transmit A specific DTMF Code. |
| int | [bt\_hfp\_hf\_query\_subscriber](#gad5dab4dcb66d52a80e0689a86de5fec3) (struct bt\_hfp\_hf \*hf) |
|  | Handsfree HF Query Subscriber Number Information. |
| int | [bt\_hfp\_hf\_indicator\_status](#gab743d3e14fa13b71ddaf26d46cf41fb3) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Handsfree HF set AG indicator activated/deactivated status. |
| int | [bt\_hfp\_hf\_enhanced\_safety](#gab6710ce433812c3bf785b787008c36be) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Handsfree HF enable/disable enhanced safety. |
| int | [bt\_hfp\_hf\_battery](#ga2f0e6012503a9b59b03a0fb508d12f88) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Handsfree HF remaining battery level. |

## Detailed Description

Hands Free Profile (HFP).

## Macro Definition Documentation

## [◆ ](#ga0e46a981a70dcdecbae119ebb6d61aa0)BT\_HFP\_HF\_CODEC\_CVSD

| #define BT\_HFP\_HF\_CODEC\_CVSD   0x01 |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

## [◆ ](#gac8ab2e9ff6c8b9a06ac460f751dec1ad)BT\_HFP\_HF\_CODEC\_LC3\_SWB

| #define BT\_HFP\_HF\_CODEC\_LC3\_SWB   0x03 |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

## [◆ ](#gaea9fb177ae8ba32650dc93f1b2953333)BT\_HFP\_HF\_CODEC\_MSBC

| #define BT\_HFP\_HF\_CODEC\_MSBC   0x02 |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga862b201be555821e932f6df5599eaa57)hfp\_hf\_ag\_indicators

| enum [hfp\_hf\_ag\_indicators](#ga862b201be555821e932f6df5599eaa57) |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

| Enumerator | |
| --- | --- |
| HF\_SERVICE\_IND |  |
| HF\_CALL\_IND |  |
| HF\_CALL\_SETUP\_IND |  |
| HF\_CALL\_HELD\_IND |  |
| HF\_SIGNAL\_IND |  |
| HF\_ROAM\_IND |  |
| HF\_BATTERY\_IND |  |

## Function Documentation

## [◆ ](#ga5bad80355fd7903abcee84437d399829)bt\_hfp\_hf\_accept()

| int bt\_hfp\_hf\_accept | ( | struct bt\_hfp\_hf\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF accept the incoming call.

Send the ATA command to accept the incoming call. OR, send the AT+BTRH=1 command to accept a held incoming call.

Note
:   It cannot be used when multiple calls are ongoing.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gad29bf40953faf638cc08acf919eb8f4f)bt\_hfp\_hf\_audio\_connect()

| int bt\_hfp\_hf\_audio\_connect | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF setup audio connection.

Setup audio conenction by sending AT+BCC. If `CONFIG_BT_HFP_HF_CODEC_NEG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga2f0e6012503a9b59b03a0fb508d12f88)bt\_hfp\_hf\_battery()

| int bt\_hfp\_hf\_battery | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF remaining battery level.

It allows HF to transfer of HF indicator remaining battery level value. If `CONFIG_BT_HFP_HF_HF_INDICATOR_BATTERY` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | level | The remaining battery level. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga3afb0d82551708975dbeb9c903c3d1fb)bt\_hfp\_hf\_call\_waiting\_notify()

| int bt\_hfp\_hf\_call\_waiting\_notify | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF enable/disable call waiting notification.

Enable call waiting notification by sending AT+CCWA=1. Disable call waiting notification by sending AT+CCWA=0. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | enable | Enable/disable. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga64ac1971dc7b1dacf6685bdc0c71e34c)bt\_hfp\_hf\_cli()

| int bt\_hfp\_hf\_cli | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF enable/disable Calling Line Identification (CLI) Notification.

Enable/disable Calling Line Identification (CLI) Notification. The AT command AT+CLIP will be sent to the AG to enable/disable the CLI unsolicited result code +CLIP when calling the function. If `CONFIG_BT_HFP_HF_CLI` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | enable | Enable/disable CLI. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga302e9ed397b056edef518470c6ea1d62)bt\_hfp\_hf\_connect()

| int bt\_hfp\_hf\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_hfp\_hf \*\* | *hf*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Initiate the service level connection establishment procedure.

Initiate the service level connection establishment procedure on the ACL connection specified by the parameter conn using the specific RFCOMM channel discovered by the function [bt\_br\_discovery\_start](group__bt__gap.md#ga9760190192dde5c498ec96628468be8d "Start BR/EDR discovery.").

The parameter hf is a output parameter. When the service level connection establishment procedure is initiated without any error, the HFP HF object is allocated and it will be returned via the parameter hf if the parameter hf is not a NULL pointer.

When service level conenction is established, the registered callback connected will be triggered to notify the application that the service level connection establishment procedure is done. And the HFP HF object is valid at this time. It means after the function is called without any error, all interfaces provided by HFP HF can only be called after the registered callback connected is triggered.

Parameters
:   | conn | ACL connection object. |
    | --- | --- |
    | hf | Created HFP HF object. |
    | channel | Peer RFCOMM channel to be connected. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaf5e7ef119731c0dc35bec61fb7c34774)bt\_hfp\_hf\_disconnect()

| int bt\_hfp\_hf\_disconnect | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Release the service level connection.

Release the service level connection from the peer device.

The function can only be called after the registered callback connected is triggered.

If the function is called without any error, the HFP HF object is invalid at this time. All interfaces provided by HFP HF should not be called anymore.

If the service level connection is released, the registered callback disconnected will be triggered to notify the application that the service level connection release procedure is done. And the HFP HF object will be freed after the registered callback disconnected returned.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gab6710ce433812c3bf785b787008c36be)bt\_hfp\_hf\_enhanced\_safety()

| int bt\_hfp\_hf\_enhanced\_safety | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF enable/disable enhanced safety.

It allows HF to transfer of HF indicator enhanced safety value. If `CONFIG_BT_HFP_HF_HF_INDICATOR_ENH_SAFETY` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | enable | The enhanced safety is enabled/disabled. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga2b48a0938e65899417b2f3ab1fa4c548)bt\_hfp\_hf\_explicit\_call\_transfer()

| int bt\_hfp\_hf\_explicit\_call\_transfer | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF explicit call transfer.

Connects the two calls and disconnects the subscriber from both calls (Explicit Call Transfer) by sending AT+CHLD=4. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaaa9fbdceec140f274fc88c063a4cd4b8)bt\_hfp\_hf\_get\_operator()

| int bt\_hfp\_hf\_get\_operator | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF requests currently selected operator.

Send the AT+COPS? (Read) command to find the currently selected operator.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga40de46a6651eb85aa6d04ad66f528803)bt\_hfp\_hf\_hold\_active\_accept\_other()

| int bt\_hfp\_hf\_hold\_active\_accept\_other | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF hold all active calls and accept other call.

Hold all active calls (if any exist) and accepts the other (held or waiting) call by sending AT+CHLD=2. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga540bf6ec23c632b3f736e6302ef32ebd)bt\_hfp\_hf\_hold\_incoming()

| int bt\_hfp\_hf\_hold\_incoming | ( | struct bt\_hfp\_hf\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF put the incoming call on hold.

Send the AT+BTRH=0 command to put the incoming call on hold. If the incoming call has been held, the callback on\_hold will be triggered.

Note
:   It cannot be used when multiple calls are ongoing.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gab743d3e14fa13b71ddaf26d46cf41fb3)bt\_hfp\_hf\_indicator\_status()

| int bt\_hfp\_hf\_indicator\_status | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *status* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF set AG indicator activated/deactivated status.

It allows HF to issue the AT+BIA command if it needs to change the activated/deactivated status of indicators in the AG. The index of all indicators can be activated/deactivated are defined in enum [hfp\_hf\_ag\_indicators](#ga862b201be555821e932f6df5599eaa57). The each bit of parameter status represents the indicator status corresponding to the index. Such as, value 0b111110 of status means the AG indicator service is required to be deactivated. Others are required to be activated.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | status | The activated/deactivated bitmap status of AG indicators. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga04d9fe3524c9522e98830507886bdfc6)bt\_hfp\_hf\_join\_conversation()

| int bt\_hfp\_hf\_join\_conversation | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF add a held call to the conversation.

Add a held call to the conversation by sending AT+CHLD=3. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gabacb666eb0f43db8614413a4ae0ce60a)bt\_hfp\_hf\_memory\_dial()

| int bt\_hfp\_hf\_memory\_dial | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | const char \* | *location* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF memory dialing call.

Initiate outgoing voice calls using the memory dialing feature of the AG. Send the ATD>Nan... command to start memory dialing. The result of the command will be notified through the callback dialing.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | location | Memory location. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gac57d7188e3f8b6e1e28d2a55c2567dbf)bt\_hfp\_hf\_number\_call()

| int bt\_hfp\_hf\_number\_call | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | const char \* | *number* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF phone number call.

Initiate outgoing voice calls by providing the destination phone number to the AG. Send the ATDdd…dd command to start phone number call. The result of the command will be notified through the callback dialing.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | number | Phone number. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gac3c038818cda3645eaadc5374d18c3ee)bt\_hfp\_hf\_private\_consultation\_mode()

| int bt\_hfp\_hf\_private\_consultation\_mode | ( | struct bt\_hfp\_hf\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF request private consultation mode with specified call.

Request private consultation mode with specified call (Place all calls on hold EXCEPT the call indicated by <idx>.) by sending AT+CHLD=2<idx>. <idx> is index of specified call. If `CONFIG_BT_HFP_HF_ECC` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga70e086f6a02cb116317a8e80f76abf6d)bt\_hfp\_hf\_query\_respond\_hold\_status()

| int bt\_hfp\_hf\_query\_respond\_hold\_status | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF query respond and hold status of AG.

Send the AT+BTRH? command to query respond and hold status of AG. The status respond and hold will be notified through callback on\_hold.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gad5dab4dcb66d52a80e0689a86de5fec3)bt\_hfp\_hf\_query\_subscriber()

| int bt\_hfp\_hf\_query\_subscriber | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF Query Subscriber Number Information.

It allows HF to query the AG subscriber number by sending AT+CNUM.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga3f6b43bf53fa04a6e71e883dc38f988b)bt\_hfp\_hf\_ready\_to\_accept\_audio()

| int bt\_hfp\_hf\_ready\_to\_accept\_audio | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF indicate that the HF is ready to accept audio.

This value indicates that the HF is ready to accept audio when the Audio Connection is first established. The HF shall only send this value if the eSCO link has been established. If `CONFIG_BT_HFP_HF_ENH_VOICE_RECG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga9611012a35df66fac324b99b16e5d958)bt\_hfp\_hf\_redial()

| int bt\_hfp\_hf\_redial | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF redial last number.

Initiate outgoing voice calls by recalling the last number dialed by the AG. Send the AT+BLDN command to recall the last number. The result of the command will be notified through the callback dialing.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga2e4a7c05a3ba9a32eab50b9904f7f161)bt\_hfp\_hf\_register()

| int bt\_hfp\_hf\_register | ( | struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Register HFP HF profile.

Register Handsfree profile callbacks to monitor the state and get the required HFP details to display.

Parameters
:   | cb | callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gac4e3d88b80b69840d52050dcd72c9ab3)bt\_hfp\_hf\_reject()

| int bt\_hfp\_hf\_reject | ( | struct bt\_hfp\_hf\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF reject the incoming call.

Send the AT+CHUP command to reject the incoming call. OR, send the AT+BTRH=2 command to reject a held incoming call.

Note
:   It cannot be used when multiple calls are ongoing.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga36be4ff5fd805c4413ba90b1f62b9143)bt\_hfp\_hf\_release\_active\_accept\_other()

| int bt\_hfp\_hf\_release\_active\_accept\_other | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF release all active calls and accept other call.

Release all active calls (if any exist) and accepts the other (held or waiting) call by sending AT+CHLD=1. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga06e7e93578601693fa377a240e0d18a7)bt\_hfp\_hf\_release\_all\_held()

| int bt\_hfp\_hf\_release\_all\_held | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF release all held calls.

Release all held calls by sending AT+CHLD=0. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga1ad888c3b967d3f9b2e5ccee303b9ad7)bt\_hfp\_hf\_release\_specified\_call()

| int bt\_hfp\_hf\_release\_specified\_call | ( | struct bt\_hfp\_hf\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF release call with specified index.

Release call with specified index by sending AT+CHLD=1<idx>. <idx> is index of specified call. If `CONFIG_BT_HFP_HF_ECC` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga92d89b0b37186688e86091a7a8015245)bt\_hfp\_hf\_request\_phone\_number()

| int bt\_hfp\_hf\_request\_phone\_number | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF attach a phone number for a voice tag.

Send AT command "AT+BINP=1" to request phone number to the AG.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga34649dbecca2513c0b5bcd0e109b2551)bt\_hfp\_hf\_select\_codec()

| int bt\_hfp\_hf\_select\_codec | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *codec\_id* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF set selected codec id.

Set selected codec id by sending AT+BCS. The function is used to response the codec negotiation request notified by callback codec\_negotiate. The parameter codec\_id should be same as id of callback codec\_negotiate if the id could be supported. Or, call [bt\_hfp\_hf\_set\_codecs](#ga91fc2204f50df07567f87a2b7a18e69f) to notify the AG Codec IDs supported by HFP HF. If `CONFIG_BT_HFP_HF_CODEC_NEG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | codec\_id | Selected codec id. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga91fc2204f50df07567f87a2b7a18e69f)bt\_hfp\_hf\_set\_codecs()

| int bt\_hfp\_hf\_set\_codecs | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *codec\_ids* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF set supported codec ids.

Set supported codec ids by sending AT+BAC. This function is used to notify AG the supported Codec IDs of HF. If `CONFIG_BT_HFP_HF_CODEC_NEG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | codec\_ids | Supported codec IDs. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga7389e5723e01b661b5e9c9d2114918b8)bt\_hfp\_hf\_set\_udub()

| int bt\_hfp\_hf\_set\_udub | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF set User Determined User Busy (UDUB) for a waiting call.

Set User Determined User Busy (UDUB) for a waiting call by sending AT+CHLD=0. If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gabbce5fbf0dec27e1c5a4da144fbfc9c1)bt\_hfp\_hf\_terminate()

| int bt\_hfp\_hf\_terminate | ( | struct bt\_hfp\_hf\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF terminate the incoming call.

Send the AT+CHUP command to terminate the incoming call.

Note
:   It cannot be used when multiple calls are ongoing.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga6a3a6bc61a3a74f5a4a48d7e39bd74a0)bt\_hfp\_hf\_transmit\_dtmf\_code()

| int bt\_hfp\_hf\_transmit\_dtmf\_code | ( | struct bt\_hfp\_hf\_call \* | *call*, |
| --- | --- | --- | --- |
|  |  | char | *code* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF Transmit A specific DTMF Code.

During an ongoing call, the HF transmits the AT+VTS command to instruct the AG to transmit a specific DTMF code to its network connection. The set of the code is "0-9,#,\*,A-D".

Parameters
:   | call | HFP HF call object. |
    | --- | --- |
    | code | A specific DTMF code. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga7f37a9c009b4e55b7060d635c5b0c67b)bt\_hfp\_hf\_turn\_off\_ecnr()

| int bt\_hfp\_hf\_turn\_off\_ecnr | ( | struct bt\_hfp\_hf \* | *hf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF turns off AG's EC and NR.

Turn off the AG's EC and NR by sending AT+NREC=0. The result of the command is notified through the callback ecnr\_turn\_off. If `CONFIG_BT_HFP_HF_ECNR` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga0602cee7a90ca4afe90b65d748024472)bt\_hfp\_hf\_vgm()

| int bt\_hfp\_hf\_vgm | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gain* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF report Gain of Microphone (VGM).

Report Gain of Microphone (VGM). The AT command AT+VGM=<gain> will be sent to the AG to report its current microphone gain level setting to the AG. <gain> is a decimal numeric constant, relating to a particular (implementation dependent) volume level controlled by the HF. This command does not change the microphone gain of the AG; it simply indicates the current value of the microphone gain in the HF. If `CONFIG_BT_HFP_HF_VOLUME` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called. For "Volume Level Synchronization", the HF application could call the function to set VGM gain value in HF connection callback function. Then after the HF connection callback returned, VGM gain will be sent to HFP AG.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | gain | Gain of microphone. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga0c1c35b3117f78f43a6300d4ff7dd18b)bt\_hfp\_hf\_vgs()

| int bt\_hfp\_hf\_vgs | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gain* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF report Gain of Speaker (VGS).

Report Gain of Speaker (VGS). The AT command AT+VGS=<gain> will be sent to the AG to report its current speaker gain level setting to the AG. <gain> is a decimal numeric constant, relating to a particular (implementation dependent) volume level controlled by the HF. This command does not change the speaker gain of the AG; it simply indicates the current value of the speaker gain in the HF. If `CONFIG_BT_HFP_HF_VOLUME` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called. For "Volume Level Synchronization", the HF application could call the function to set VGS gain value in HF connection callback function. Then after the HF connection callback returned, VGS gain will be sent to HFP AG.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | gain | Gain of speaker. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaeed952ce163ef2466ece04af24b76a28)bt\_hfp\_hf\_voice\_recognition()

| int bt\_hfp\_hf\_voice\_recognition | ( | struct bt\_hfp\_hf \* | *hf*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *activate* ) |

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h.md)>`

Handsfree HF enable/disable the voice recognition function.

Enables/disables the voice recognition function in the AG. If `CONFIG_BT_HFP_HF_VOICE_RECG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | activate | Activate/deactivate the voice recognition function. |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
