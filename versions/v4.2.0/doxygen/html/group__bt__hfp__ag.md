---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__bt__hfp__ag.html
original_path: doxygen/html/group__bt__hfp__ag.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hands Free Profile - Audio Gateway (HFP-AG)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Hands Free Profile - Audio Gateway (HFP-AG).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) |
|  | The ongoing call. [More...](structbt__hfp__ag__ongoing__call.md#details) |
| struct | [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) |
|  | HFP profile AG application callback. [More...](structbt__hfp__ag__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HFP\_AG\_CODEC\_CVSD](#gada6266f825879f39147c5d889e4192c9)   0x01 |
| #define | [BT\_HFP\_AG\_CODEC\_MSBC](#ga3591201c7310288ea2e01e2f77a0c0d3)   0x02 |
| #define | [BT\_HFP\_AG\_CODEC\_LC3\_SWB](#ga8a833c4b11dc9e8fd08a73a2af418d83)   0x03 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bt\_hfp\_ag\_query\_subscriber\_func\_t](#ga8e9b485f7ea0b9e16d96f578cdc587c3)) (struct bt\_hfp\_ag \*ag, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) service) |
|  | Query subscriber number callback function. |

| Enumerations | |
| --- | --- |
| enum | [bt\_hfp\_ag\_indicator](#ga37640efdcc737bfa0390df889a62f810) {     [BT\_HFP\_AG\_SERVICE\_IND](#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) = 0 , [BT\_HFP\_AG\_CALL\_IND](#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) = 1 , [BT\_HFP\_AG\_CALL\_SETUP\_IND](#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) = 2 , [BT\_HFP\_AG\_CALL\_HELD\_IND](#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) = 3 ,     [BT\_HFP\_AG\_SIGNAL\_IND](#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) = 4 , [BT\_HFP\_AG\_ROAM\_IND](#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) = 5 , [BT\_HFP\_AG\_BATTERY\_IND](#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) = 6 , [BT\_HFP\_AG\_IND\_MAX](#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)   } |
| enum | [hfp\_ag\_hf\_indicators](#ga030c97d703fb45a2055653c51cb1b403) { [HFP\_AG\_ENHANCED\_SAFETY\_IND](#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f) = 1 , [HFP\_AG\_BATTERY\_LEVEL\_IND](#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1) = 2 } |
| enum | [bt\_hfp\_ag\_call\_status](#gad2220b4a470cb3d537cf09492847568e) {     [BT\_HFP\_AG\_CALL\_STATUS\_ACTIVE](#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658) = 0 , [BT\_HFP\_AG\_CALL\_STATUS\_HELD](#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2) = 1 , [BT\_HFP\_AG\_CALL\_STATUS\_DIALING](#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963) = 2 , [BT\_HFP\_AG\_CALL\_STATUS\_ALERTING](#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae) = 3 ,     [BT\_HFP\_AG\_CALL\_STATUS\_INCOMING](#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8) = 4 , [BT\_HFP\_AG\_CALL\_STATUS\_WAITING](#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2) = 5 , [BT\_HFP\_AG\_CALL\_STATUS\_INCOMING\_HELD](#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542) = 6   } |
| enum | [bt\_hfp\_ag\_call\_dir](#ga019020ee2ed73c218f7dadf8371bf9a6) { [BT\_HFP\_AG\_CALL\_DIR\_OUTGOING](#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37) = 0 , [BT\_HFP\_AG\_CALL\_DIR\_INCOMING](#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55) = 1 } |

| Functions | |
| --- | --- |
| int | [bt\_hfp\_ag\_register](#ga379ec1c540195549fc59417d8d1ce7e5) (struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) \*cb) |
|  | Register HFP AG profile. |
| int | [bt\_hfp\_ag\_connect](#ga5b602810558268396f0cb64adcb0d014) (struct bt\_conn \*conn, struct bt\_hfp\_ag \*\*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Create the hfp ag session. |
| int | [bt\_hfp\_ag\_disconnect](#gadf0b4aef701cf0986ea9599ad79d451a) (struct bt\_hfp\_ag \*ag) |
|  | Disconnect the hfp ag session. |
| int | [bt\_hfp\_ag\_remote\_incoming](#ga443cd2928686f222d61f06c7477ea793) (struct bt\_hfp\_ag \*ag, const char \*number) |
|  | Notify HFP Unit of an incoming call. |
| int | [bt\_hfp\_ag\_hold\_incoming](#gab288d6e6b45a24b706328da58ca43a3b) (struct bt\_hfp\_ag\_call \*call) |
|  | Put the incoming call on hold. |
| int | [bt\_hfp\_ag\_reject](#ga195daffc37f1a3f210ba52dae1a9c4c2) (struct bt\_hfp\_ag\_call \*call) |
|  | Reject the incoming call. |
| int | [bt\_hfp\_ag\_accept](#ga351e1b78b8c19c3971554fabb331e5c6) (struct bt\_hfp\_ag\_call \*call) |
|  | Accept the incoming call. |
| int | [bt\_hfp\_ag\_terminate](#ga2f2e85a6076930ed87bc0727c75209a9) (struct bt\_hfp\_ag\_call \*call) |
|  | Terminate the active/hold call. |
| int | [bt\_hfp\_ag\_retrieve](#ga405fcf8e03bac39bd5b0e7bf2766045f) (struct bt\_hfp\_ag\_call \*call) |
|  | Retrieve the held call. |
| int | [bt\_hfp\_ag\_hold](#ga4bbcec3ed5394e965aa7404dc968b94d) (struct bt\_hfp\_ag\_call \*call) |
|  | Hold the active call. |
| int | [bt\_hfp\_ag\_outgoing](#ga580328104cf990c6f9e0a64642c16ebd) (struct bt\_hfp\_ag \*ag, const char \*number) |
|  | Dial a call. |
| int | [bt\_hfp\_ag\_remote\_ringing](#ga0a12a56baa25e2aea101a387fcccb88e) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote starts ringing. |
| int | [bt\_hfp\_ag\_remote\_reject](#gacb1b361e6b0a441102f7ccd641eb3e6b) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote rejects the call. |
| int | [bt\_hfp\_ag\_remote\_accept](#ga018d8ed8912f9dcef8c5fa37ac2bd889) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote accepts the call. |
| int | [bt\_hfp\_ag\_remote\_terminate](#ga525085c7c75e412ca43ba8b23cbc0c3d) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote terminates the active/hold call. |
| int | [bt\_hfp\_ag\_explicit\_call\_transfer](#ga5e249248a52d7c95c9d3f3f852bf2314) (struct bt\_hfp\_ag \*ag) |
|  | explicit call transfer |
| int | [bt\_hfp\_ag\_vgm](#ga53778bd332c95fa4357d254f5ef125a2) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vgm) |
|  | Set the HF microphone gain. |
| int | [bt\_hfp\_ag\_vgs](#gabdad8c764c91e133598584d741ed9d4b) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vgs) |
|  | Set the HF speaker gain. |
| int | [bt\_hfp\_ag\_set\_operator](#gaaf066dce38c028254b6c1880bcebaa13) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, char \*name) |
|  | Set currently network operator. |
| int | [bt\_hfp\_ag\_audio\_connect](#ga542a1754a16e32a9b2651f1230aa7066) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Create audio connection. |
| int | [bt\_hfp\_ag\_inband\_ringtone](#ga881ea4d3cc732fb5d804df203dde7746) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) inband) |
|  | Set In-Band Ring Tone. |
| int | [bt\_hfp\_ag\_voice\_recognition](#ga28682fc5d8cfee9c0adece68bcb94c3f) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
|  | Enable/disable the voice recognition function. |
| int | [bt\_hfp\_ag\_vre\_state](#ga3668f3997afe9ab678f9eb2e6faf324d) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | set voice recognition engine state |
| int | [bt\_hfp\_ag\_vre\_textual\_representation](#ga4e71364283448c7c5d3306c111aa167d) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const char \*id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) operation, const char \*text) |
|  | set voice recognition engine state and textual representation |
| int | [bt\_hfp\_ag\_signal\_strength](#ga20ef1240e0ff72d914405b259cc3164f) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) strength) |
|  | Set signal strength. |
| int | [bt\_hfp\_ag\_roaming\_status](#ga0f8b2e463aefbf74b26ac4f27033486c) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Set roaming status. |
| int | [bt\_hfp\_ag\_battery\_level](#ga4da632e9775051df6a5b5010fd3806df) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Set battery level. |
| int | [bt\_hfp\_ag\_service\_availability](#gaf838e54046c380931f23a59919ccfa5b) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) available) |
|  | Set service availability. |
| int | [bt\_hfp\_ag\_hf\_indicator](#gaacc2df6144e1a33b13635855fe74f1f1) (struct bt\_hfp\_ag \*ag, enum [hfp\_ag\_hf\_indicators](#ga030c97d703fb45a2055653c51cb1b403) indicator, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Activate/deactivate HF indicator. |
| int | [bt\_hfp\_ag\_ongoing\_calls](#ga5614bf3f1de11959a0364f458523e06e) (struct bt\_hfp\_ag \*ag, struct [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) \*calls, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Set the ongoing calls. |

## Detailed Description

Hands Free Profile - Audio Gateway (HFP-AG).

## Macro Definition Documentation

## [◆ ](#gada6266f825879f39147c5d889e4192c9)BT\_HFP\_AG\_CODEC\_CVSD

| #define BT\_HFP\_AG\_CODEC\_CVSD   0x01 |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

## [◆ ](#ga8a833c4b11dc9e8fd08a73a2af418d83)BT\_HFP\_AG\_CODEC\_LC3\_SWB

| #define BT\_HFP\_AG\_CODEC\_LC3\_SWB   0x03 |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

## [◆ ](#ga3591201c7310288ea2e01e2f77a0c0d3)BT\_HFP\_AG\_CODEC\_MSBC

| #define BT\_HFP\_AG\_CODEC\_MSBC   0x02 |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

## Typedef Documentation

## [◆ ](#ga8e9b485f7ea0b9e16d96f578cdc587c3)bt\_hfp\_ag\_query\_subscriber\_func\_t

| typedef int(\* bt\_hfp\_ag\_query\_subscriber\_func\_t) (struct bt\_hfp\_ag \*ag, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) service) |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Query subscriber number callback function.

When AG wants to send subscriber number information, all information will be passed through the callback. And the subscriber number information will be sent out in this function.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Subscriber number. |
    | type | Type of subscriber number specifies the format of the phone number provided, and can be one of the following values:  - values 128-143: The phone number format may be a national or international format, and may contain prefix and/or escape digits. No changes on the number presentation are required. - values 144-159: The phone number format is an international number, including the country code prefix. If the plus sign ("+") is not included as part of the number and shall be added by the AG as needed. - values 160-175: National number. No prefix nor escape digits included. |
    | service | Service of subscriber number indicates which service this phone number relates to. Shall be either 4 (voice) or 5 (fax). |

Returns
:   0 if should continue to the next subscriber number information.
:   negative value to stop.

## Enumeration Type Documentation

## [◆ ](#ga019020ee2ed73c218f7dadf8371bf9a6)bt\_hfp\_ag\_call\_dir

| enum [bt\_hfp\_ag\_call\_dir](#ga019020ee2ed73c218f7dadf8371bf9a6) |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_HFP\_AG\_CALL\_DIR\_OUTGOING |  |
| BT\_HFP\_AG\_CALL\_DIR\_INCOMING |  |

## [◆ ](#gad2220b4a470cb3d537cf09492847568e)bt\_hfp\_ag\_call\_status

| enum [bt\_hfp\_ag\_call\_status](#gad2220b4a470cb3d537cf09492847568e) |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_HFP\_AG\_CALL\_STATUS\_ACTIVE |  |
| BT\_HFP\_AG\_CALL\_STATUS\_HELD |  |
| BT\_HFP\_AG\_CALL\_STATUS\_DIALING |  |
| BT\_HFP\_AG\_CALL\_STATUS\_ALERTING |  |
| BT\_HFP\_AG\_CALL\_STATUS\_INCOMING |  |
| BT\_HFP\_AG\_CALL\_STATUS\_WAITING |  |
| BT\_HFP\_AG\_CALL\_STATUS\_INCOMING\_HELD |  |

## [◆ ](#ga37640efdcc737bfa0390df889a62f810)bt\_hfp\_ag\_indicator

| enum [bt\_hfp\_ag\_indicator](#ga37640efdcc737bfa0390df889a62f810) |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_HFP\_AG\_SERVICE\_IND |  |
| BT\_HFP\_AG\_CALL\_IND |  |
| BT\_HFP\_AG\_CALL\_SETUP\_IND |  |
| BT\_HFP\_AG\_CALL\_HELD\_IND |  |
| BT\_HFP\_AG\_SIGNAL\_IND |  |
| BT\_HFP\_AG\_ROAM\_IND |  |
| BT\_HFP\_AG\_BATTERY\_IND |  |
| BT\_HFP\_AG\_IND\_MAX |  |

## [◆ ](#ga030c97d703fb45a2055653c51cb1b403)hfp\_ag\_hf\_indicators

| enum [hfp\_ag\_hf\_indicators](#ga030c97d703fb45a2055653c51cb1b403) |
| --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

| Enumerator | |
| --- | --- |
| HFP\_AG\_ENHANCED\_SAFETY\_IND |  |
| HFP\_AG\_BATTERY\_LEVEL\_IND |  |

## Function Documentation

## [◆ ](#ga351e1b78b8c19c3971554fabb331e5c6)bt\_hfp\_ag\_accept()

| int bt\_hfp\_ag\_accept | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Accept the incoming call.

Accept the incoming call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga542a1754a16e32a9b2651f1230aa7066)bt\_hfp\_ag\_audio\_connect()

| int bt\_hfp\_ag\_audio\_connect | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Create audio connection.

Create audio conenction by HFP AG. There are two setups included, Codec connection and audio connection. The codec connection will be established firstly if the codec negotiation are supported by both side. If the passed codec id is not same as the last codec connection, the codec connection procedure will be triggered. After the codec conenction is established, the audio conenction will be started. The passed codec id could be one of BT\_HFP\_AG\_CODEC\_XXX. If the codec negotiation feature is supported by both side, the codec id could be one of the bitmaps of ids notified by callback codec. Or, the id should be BT\_HFP\_AG\_CODEC\_CVSD.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | id | Codec Id. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4da632e9775051df6a5b5010fd3806df)bt\_hfp\_ag\_battery\_level()

| int bt\_hfp\_ag\_battery\_level | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set battery level.

Set battery level.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | level | battery level. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga5b602810558268396f0cb64adcb0d014)bt\_hfp\_ag\_connect()

| int bt\_hfp\_ag\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_hfp\_ag \*\* | *ag*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Create the hfp ag session.

Create the hfp ag session

Parameters
:   | conn | ACL connection object. |
    | --- | --- |
    | ag | Created HFP AG object. |
    | channel | Peer rfcomm channel to be connected. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gadf0b4aef701cf0986ea9599ad79d451a)bt\_hfp\_ag\_disconnect()

| int bt\_hfp\_ag\_disconnect | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Disconnect the hfp ag session.

Disconnect the hfp ag session

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga5e249248a52d7c95c9d3f3f852bf2314)bt\_hfp\_ag\_explicit\_call\_transfer()

| int bt\_hfp\_ag\_explicit\_call\_transfer | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

explicit call transfer

Connects the two calls and disconnects the subscriber from both calls (Explicit Call Transfer). If `CONFIG_BT_HFP_AG_3WAY_CALL` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaacc2df6144e1a33b13635855fe74f1f1)bt\_hfp\_ag\_hf\_indicator()

| int bt\_hfp\_ag\_hf\_indicator | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | enum [hfp\_ag\_hf\_indicators](#ga030c97d703fb45a2055653c51cb1b403) | *indicator*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Activate/deactivate HF indicator.

It allows HF to issue the +BIND unsolicited result code to activate/deactivate of the AG’s supported HF Indicators. The indicator of supported indicators can be activated/deactivated are defined in enum [hfp\_ag\_hf\_indicators](#ga030c97d703fb45a2055653c51cb1b403). BT\_HFP\_AG\_HF\_INDICATOR\_ENH\_SAFETY is used to support Enhanced Safety. Only the configuration has been enabled, the indicator can be HFP\_AG\_ENHANCED\_SAFETY\_IND. BT\_HFP\_AG\_HF\_INDICATOR\_BATTERY is used to support Remaining level of Battery. Only the configuration has been enabled, the indicator can be HFP\_AG\_BATTERY\_LEVEL\_IND. If `CONFIG_BT_HFP_HF_HF_INDICATORS` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | indicator | The indicator of the AG’s supported HF Indicators. |
    | enable | enable/disable specific HF Indicator. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4bbcec3ed5394e965aa7404dc968b94d)bt\_hfp\_ag\_hold()

| int bt\_hfp\_ag\_hold | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Hold the active call.

Hold the active call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gab288d6e6b45a24b706328da58ca43a3b)bt\_hfp\_ag\_hold\_incoming()

| int bt\_hfp\_ag\_hold\_incoming | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Put the incoming call on hold.

Put the incoming call on hold.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga881ea4d3cc732fb5d804df203dde7746)bt\_hfp\_ag\_inband\_ringtone()

| int bt\_hfp\_ag\_inband\_ringtone | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *inband* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set In-Band Ring Tone.

Set In-Band Ring Tone.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | inband | In-band or no in-band. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga5614bf3f1de11959a0364f458523e06e)bt\_hfp\_ag\_ongoing\_calls()

| int bt\_hfp\_ag\_ongoing\_calls | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) \* | *calls*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *count* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set the ongoing calls.

It is used to set the ongoing calls when AT command AT+CIND? is received.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | calls | Ongoing calls. |
    | count | Ongoing call count. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga580328104cf990c6f9e0a64642c16ebd)bt\_hfp\_ag\_outgoing()

| int bt\_hfp\_ag\_outgoing | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | const char \* | *number* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Dial a call.

Dial a call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Dialing number. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga379ec1c540195549fc59417d8d1ce7e5)bt\_hfp\_ag\_register()

| int bt\_hfp\_ag\_register | ( | struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Register HFP AG profile.

Register Handsfree profile AG callbacks to monitor the state and get the required HFP details to display.

Parameters
:   | cb | callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga195daffc37f1a3f210ba52dae1a9c4c2)bt\_hfp\_ag\_reject()

| int bt\_hfp\_ag\_reject | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Reject the incoming call.

Reject the incoming call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga018d8ed8912f9dcef8c5fa37ac2bd889)bt\_hfp\_ag\_remote\_accept()

| int bt\_hfp\_ag\_remote\_accept | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote accepts the call.

Notify HFP Unit that the remote accepts the call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga443cd2928686f222d61f06c7477ea793)bt\_hfp\_ag\_remote\_incoming()

| int bt\_hfp\_ag\_remote\_incoming | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | const char \* | *number* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit of an incoming call.

Notify HFP Unit of an incoming call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Dialing number. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gacb1b361e6b0a441102f7ccd641eb3e6b)bt\_hfp\_ag\_remote\_reject()

| int bt\_hfp\_ag\_remote\_reject | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote rejects the call.

Notify HFP Unit that the remote rejects the call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga0a12a56baa25e2aea101a387fcccb88e)bt\_hfp\_ag\_remote\_ringing()

| int bt\_hfp\_ag\_remote\_ringing | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote starts ringing.

Notify HFP Unit that the remote starts ringing.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga525085c7c75e412ca43ba8b23cbc0c3d)bt\_hfp\_ag\_remote\_terminate()

| int bt\_hfp\_ag\_remote\_terminate | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote terminates the active/hold call.

Notify HFP Unit that the remote terminates the active/hold call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga405fcf8e03bac39bd5b0e7bf2766045f)bt\_hfp\_ag\_retrieve()

| int bt\_hfp\_ag\_retrieve | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Retrieve the held call.

Retrieve the held call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga0f8b2e463aefbf74b26ac4f27033486c)bt\_hfp\_ag\_roaming\_status()

| int bt\_hfp\_ag\_roaming\_status | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *status* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set roaming status.

Set roaming status.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | status | Roaming status. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaf838e54046c380931f23a59919ccfa5b)bt\_hfp\_ag\_service\_availability()

| int bt\_hfp\_ag\_service\_availability | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *available* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set service availability.

Set service availability.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | available | service availability |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaaf066dce38c028254b6c1880bcebaa13)bt\_hfp\_ag\_set\_operator()

| int bt\_hfp\_ag\_set\_operator | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mode*, |
|  |  | char \* | *name* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set currently network operator.

Set currently network operator.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | mode | Current mode and provides no information with regard to the name of the operator. |
    | name | A string in alphanumeric format representing the name of the network operator. This string shall not exceed 16 characters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga20ef1240e0ff72d914405b259cc3164f)bt\_hfp\_ag\_signal\_strength()

| int bt\_hfp\_ag\_signal\_strength | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *strength* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set signal strength.

Set signal strength.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | strength | Signal strength. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga2f2e85a6076930ed87bc0727c75209a9)bt\_hfp\_ag\_terminate()

| int bt\_hfp\_ag\_terminate | ( | struct bt\_hfp\_ag\_call \* | *call* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Terminate the active/hold call.

Terminate the active/hold call.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga53778bd332c95fa4357d254f5ef125a2)bt\_hfp\_ag\_vgm()

| int bt\_hfp\_ag\_vgm | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *vgm* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set the HF microphone gain.

Set the HF microphone gain

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | vgm | Microphone gain value. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gabdad8c764c91e133598584d741ed9d4b)bt\_hfp\_ag\_vgs()

| int bt\_hfp\_ag\_vgs | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *vgs* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Set the HF speaker gain.

Set the HF speaker gain

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | vgs | Speaker gain value. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga28682fc5d8cfee9c0adece68bcb94c3f)bt\_hfp\_ag\_voice\_recognition()

| int bt\_hfp\_ag\_voice\_recognition | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *activate* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

Enable/disable the voice recognition function.

Enables/disables the voice recognition function. If `CONFIG_BT_HFP_AG_VOICE_RECG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | activate | Activate/deactivate the voice recognition function. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga3668f3997afe9ab678f9eb2e6faf324d)bt\_hfp\_ag\_vre\_state()

| int bt\_hfp\_ag\_vre\_state | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

set voice recognition engine state

It is used to set the voice recognition engine state. The unsolicited result code +BVRA: 1,<vrecstate> will be sent. <vrecstate>: Bitmask that reflects the current state of the voice recognition engine on the AG. Bit 0 - If it is 1, the AG is ready to accept audio input Bit 1 - If it is 1, the AG is sending audio to the HF Bit 2 - If it is 1, the AG is processing the audio input If `CONFIG_BT_HFP_AG_ENH_VOICE_RECG` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The value of <vrecstate>. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4e71364283448c7c5d3306c111aa167d)bt\_hfp\_ag\_vre\_textual\_representation()

| int bt\_hfp\_ag\_vre\_textual\_representation | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state*, |
|  |  | const char \* | *id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *operation*, |
|  |  | const char \* | *text* ) |

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h.md)>`

set voice recognition engine state and textual representation

It is used to set the voice recognition engine state with textual representation. unsolicited result code +BVRA: 1,<vrecstate>,
<textualRepresentation> will be sent. <vrecstate> is same as parameter [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) of function [bt\_hfp\_ag\_vre\_state](#ga3668f3997afe9ab678f9eb2e6faf324d). <textualRepresentation>: <textID>,<textType>,<textOperation>,
<string>. <textID>: Unique ID of the current text as a hexadecimal string (a maximum of 4 characters in length, but less than 4 characters in length is valid). <textType>: ID of the textType from the following list: 0 - Text recognized by the AG from the audio input provided by the HF 1 - Text of the audio output from the AG 2 - Text of the audio output from the AG that contains a question 3 - Text of the audio output from the AG that contains an error description <textOperation>: ID of the operation of the text 1 - NewText: Indicates that a new text started. Shall be used when the <textID> changes 2 - Replace: Replace any existing text with the same <textID> and same <textType> 3 - Append: Attach new text to existing text and keep the same <textID> and same <textType> <string>: The <string> parameter shall be a UTF-8 text string and shall always be contained within double quotes. If `CONFIG_BT_HFP_AG_VOICE_RECG_TEXT` is not enabled, the error -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33 "Unsupported value.") will be returned if the function called.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The value of <vrecstate>. |
    | id | Value of <textID>. |
    | type | Value of <textType>. |
    | operation | Value of <textOperation>. |
    | text | Value of <string>. |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
