---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__hfp__ag__cb.html
original_path: doxygen/html/structbt__hfp__ag__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hfp\_ag\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hands Free Profile - Audio Gateway (HFP-AG)](group__bt__hfp__ag.md)

HFP profile AG application callback.
[More...](#details)

`#include <[zephyr/bluetooth/classic/hfp_ag.h](hfp__ag_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#ab9506172c5b23bf97b5d59ddaddd7282) )(struct bt\_conn \*conn, struct bt\_hfp\_ag \*ag) |
|  | HF AG connected callback to application. |
| void(\* | [disconnected](#af9c53ab021dbbf1017d71895581960c4) )(struct bt\_hfp\_ag \*ag) |
|  | HF disconnected callback to application. |
| void(\* | [sco\_connected](#aac2b1ff4d80361e0e5eea2481027b4cf) )(struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn) |
|  | HF SCO/eSCO connected Callback. |
| void(\* | [sco\_disconnected](#a95600361e59a516f220a314e920c5858) )(struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | HF SCO/eSCO disconnected Callback. |
| int(\* | [get\_ongoing\_call](#ac3771d39b8f1982514bbb23fc7773468) )(struct bt\_hfp\_ag \*ag) |
|  | Get ongoing call information Callback. |
| int(\* | [memory\_dial](#af335450c5e63139485fa5a131814d650) )(struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number) |
|  | HF memory dialing request Callback. |
| int(\* | [number\_call](#a98c497e706ed5fcfe6fd308741893e91) )(struct bt\_hfp\_ag \*ag, const char \*number) |
|  | HF phone number calling request Callback. |
| void(\* | [outgoing](#a8946de63ef24bbbc69e285abe2d141c1) )(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number) |
|  | HF outgoing Callback. |
| void(\* | [incoming](#aa0a4ab5aad6557a786ccf2f6861b932c) )(struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number) |
|  | HF incoming Callback. |
| void(\* | [incoming\_held](#a5b9f1c48e15a74b052678c491a592a5f) )(struct bt\_hfp\_ag\_call \*call) |
|  | HF incoming call is held Callback. |
| void(\* | [ringing](#a0b8967f487d64556851420b2f4e059fe) )(struct bt\_hfp\_ag\_call \*call, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) in\_band) |
|  | HF ringing Callback. |
| void(\* | [accept](#a7da69bf1f5b85130ce2656c4915ba6d8) )(struct bt\_hfp\_ag\_call \*call) |
|  | HF call accept Callback. |
| void(\* | [held](#abe78441b0f01acd72713c7658f4e0274) )(struct bt\_hfp\_ag\_call \*call) |
|  | HF call held Callback. |
| void(\* | [retrieve](#a9d6b978f82de6ded48881a87eb90aebb) )(struct bt\_hfp\_ag\_call \*call) |
|  | HF call retrieve Callback. |
| void(\* | [reject](#abe1b5d71279c2e3292b3b90043d75224) )(struct bt\_hfp\_ag\_call \*call) |
|  | HF call reject Callback. |
| void(\* | [terminate](#adf9960da8a3f4c38f7fcd60501522462) )(struct bt\_hfp\_ag\_call \*call) |
|  | HF call terminate Callback. |
| void(\* | [codec](#a2f15172060cc5d225894be5c8311610b) )(struct bt\_hfp\_ag \*ag, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ids) |
|  | Supported codec Ids callback. |
| void(\* | [codec\_negotiate](#a82abcad15f921fb0c99cc705e139aac1) )(struct bt\_hfp\_ag \*ag, int err) |
|  | Codec negotiate callback. |
| void(\* | [audio\_connect\_req](#a390377048e8623889515f2c6b6be0874) )(struct bt\_hfp\_ag \*ag) |
|  | Audio connection request callback. |
| void(\* | [vgm](#aaad37582866c420ee41c3f730de16eb4) )(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | HF VGM setting callback. |
| void(\* | [vgs](#a38adb040dee9abd794f952322bf3d615) )(struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | HF VGS setting callback. |
| void(\* | [ecnr\_turn\_off](#ac3c09ffe392e167dd5aae82e740b5050) )(struct bt\_hfp\_ag \*ag) |
|  | HF ECNR turns off callback. |
| void(\* | [explicit\_call\_transfer](#ac06c1ddfa5cdc4ecb81a838e32299c8a) )(struct bt\_hfp\_ag \*ag) |
|  | HF explicit call transfer callback. |
| void(\* | [voice\_recognition](#a16c528018a2e9e97320df885c049454f) )(struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
|  | Voice recognition activation/deactivation callback. |
| void(\* | [ready\_to\_accept\_audio](#ad9925958c87b164113f607bd680ce2c3) )(struct bt\_hfp\_ag \*ag) |
|  | Ready to accept audio callback. |
| int(\* | [request\_phone\_number](#aecc8cdaf372d93f9cb531604f9b82d65) )(struct bt\_hfp\_ag \*ag, char \*\*number) |
|  | Request phone number callback. |
| void(\* | [transmit\_dtmf\_code](#ad690d69c9786c69ad85e005e778b316c) )(struct bt\_hfp\_ag \*ag, char code) |
|  | Transmit a DTMF Code callback. |
| int(\* | [subscriber\_number](#a976016f32e462daf38cd6d24ba18ff3d) )(struct bt\_hfp\_ag \*ag, [bt\_hfp\_ag\_query\_subscriber\_func\_t](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3) func) |
|  | Get subscriber number callback. |
| void(\* | [hf\_indicator\_value](#a965d39254b75668f968d9a2bb5cffeba) )(struct bt\_hfp\_ag \*ag, enum [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) indicator, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator value callback. |

## Detailed Description

HFP profile AG application callback.

## Field Documentation

## [◆ ](#a7da69bf1f5b85130ce2656c4915ba6d8)accept

| void(\* bt\_hfp\_ag\_cb::accept) (struct bt\_hfp\_ag\_call \*call) |
| --- |

HF call accept Callback.

If this callback is provided it will be called whenever the call is accepted.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

## [◆ ](#a390377048e8623889515f2c6b6be0874)audio\_connect\_req

| void(\* bt\_hfp\_ag\_cb::audio\_connect\_req) (struct bt\_hfp\_ag \*ag) |
| --- |

Audio connection request callback.

If this callback is provided it will be called whenever the audio conenction request is triggered by HF. When AT+BCC AT command received, it means the procedure of establishment of audio connection is triggered by HF. If the callback is provided by application, AG needs to start the codec connection procedure by calling function [bt\_hfp\_ag\_audio\_connect](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066 "Create audio connection.") in application layer. Or, the codec conenction procedure will be started with default codec id [BT\_HFP\_AG\_CODEC\_CVSD](group__bt__hfp__ag.md#gada6266f825879f39147c5d889e4192c9).

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | err | Result of codec negotiation. |

## [◆ ](#a2f15172060cc5d225894be5c8311610b)codec

| void(\* bt\_hfp\_ag\_cb::codec) (struct bt\_hfp\_ag \*ag, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ids) |
| --- |

Supported codec Ids callback.

If this callback is provided it will be called whenever the supported codec ids are updated.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#a82abcad15f921fb0c99cc705e139aac1)codec\_negotiate

| void(\* bt\_hfp\_ag\_cb::codec\_negotiate) (struct bt\_hfp\_ag \*ag, int err) |
| --- |

Codec negotiate callback.

If this callback is provided it will be called whenever the codec negotiation succeeded or failed.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | err | Result of codec negotiation. |

## [◆ ](#ab9506172c5b23bf97b5d59ddaddd7282)connected

| void(\* bt\_hfp\_ag\_cb::connected) (struct bt\_conn \*conn, struct bt\_hfp\_ag \*ag) |
| --- |

HF AG connected callback to application.

If this callback is provided it will be called whenever the AG connection completes.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | ag | HFP AG object. |

## [◆ ](#af9c53ab021dbbf1017d71895581960c4)disconnected

| void(\* bt\_hfp\_ag\_cb::disconnected) (struct bt\_hfp\_ag \*ag) |
| --- |

HF disconnected callback to application.

If this callback is provided it will be called whenever the connection gets disconnected, including when a connection gets rejected or cancelled or any error in SLC establishment.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#ac3c09ffe392e167dd5aae82e740b5050)ecnr\_turn\_off

| void(\* bt\_hfp\_ag\_cb::ecnr\_turn\_off) (struct bt\_hfp\_ag \*ag) |
| --- |

HF ECNR turns off callback.

If this callback is provided it will be called whenever the ECNR turning off request is received from HF. If the callback is NULL or `CONFIG_BT_HFP_AG_ECNR` is not enabled, the response result code of AT command will be an AT ERROR.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#ac06c1ddfa5cdc4ecb81a838e32299c8a)explicit\_call\_transfer

| void(\* bt\_hfp\_ag\_cb::explicit\_call\_transfer) (struct bt\_hfp\_ag \*ag) |
| --- |

HF explicit call transfer callback.

If this callback is provided it will be called whenever the AT+CHLD=4 is sent from HF. When the callback is notified, the application should connect the two calls and disconnects the subscriber from both calls (Explicit Call Transfer). After the callback returned, the call objects will be invalid. If the callback is NULL, the response result code of AT command will be an AT ERROR. If `CONFIG_BT_HFP_AG_3WAY_CALL` is not enabled, the callback will not be notified.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#ac3771d39b8f1982514bbb23fc7773468)get\_ongoing\_call

| int(\* bt\_hfp\_ag\_cb::get\_ongoing\_call) (struct bt\_hfp\_ag \*ag) |
| --- |

Get ongoing call information Callback.

If this callback is provided it will be called whenever the AT command AT+CIND? is received from HF has been sent. After the callback notified, the ongoing calls should be set via function [bt\_hfp\_ag\_ongoing\_calls()](group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e "Set the ongoing calls.") within the timeout `CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT`.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Note
:   The AG is in SLC establishment phase. The AG callback [connected()](#ab9506172c5b23bf97b5d59ddaddd7282) is not notified at this time.

Returns
:   0 in case of success. The response +CIND will be sent after the function [bt\_hfp\_ag\_ongoing\_calls()](group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e "Set the ongoing calls.") called or after the time exceeds `CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT`. Or negative value in case of error. The response +CIND will be replied immediately.

## [◆ ](#abe78441b0f01acd72713c7658f4e0274)held

| void(\* bt\_hfp\_ag\_cb::held) (struct bt\_hfp\_ag\_call \*call) |
| --- |

HF call held Callback.

If this callback is provided it will be called whenever the call is held.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

## [◆ ](#a965d39254b75668f968d9a2bb5cffeba)hf\_indicator\_value

| void(\* bt\_hfp\_ag\_cb::hf\_indicator\_value) (struct bt\_hfp\_ag \*ag, enum [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) indicator, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator value callback.

If this callback is provided it will be called whenever the AT command AT+BIEV is received. If `CONFIG_BT_HFP_AG_HF_INDICATORS` is not enabled, the callback will not be notified.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | indicator | HF indicator |
    | value | The value of specific indicator |

## [◆ ](#aa0a4ab5aad6557a786ccf2f6861b932c)incoming

| void(\* bt\_hfp\_ag\_cb::incoming) (struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number) |
| --- |

HF incoming Callback.

If this callback is provided it will be called whenever a new call is incoming.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | call | HFP AG call object. |
    | number | Incoming number |

## [◆ ](#a5b9f1c48e15a74b052678c491a592a5f)incoming\_held

| void(\* bt\_hfp\_ag\_cb::incoming\_held) (struct bt\_hfp\_ag\_call \*call) |
| --- |

HF incoming call is held Callback.

If this callback is provided it will be called whenever the incoming call is held but not accepted.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

## [◆ ](#af335450c5e63139485fa5a131814d650)memory\_dial

| int(\* bt\_hfp\_ag\_cb::memory\_dial) (struct bt\_hfp\_ag \*ag, const char \*location, char \*\*number) |
| --- |

HF memory dialing request Callback.

If this callback is provided it will be called whenever a new call is requested with memory dialing from HF. Get the phone number according to the given AG memory location.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | location | AG memory location |
    | number | Dialing number |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a98c497e706ed5fcfe6fd308741893e91)number\_call

| int(\* bt\_hfp\_ag\_cb::number\_call) (struct bt\_hfp\_ag \*ag, const char \*number) |
| --- |

HF phone number calling request Callback.

If this callback is provided it will be called whenever a new call is requested with specific phone number from HF. When the callback is triggered, the application needs to start dialing the number with the passed phone number. If the callback is invalid, the phone number dialing from HF cannot be supported.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Dialing number |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a8946de63ef24bbbc69e285abe2d141c1)outgoing

| void(\* bt\_hfp\_ag\_cb::outgoing) (struct bt\_hfp\_ag \*ag, struct bt\_hfp\_ag\_call \*call, const char \*number) |
| --- |

HF outgoing Callback.

If this callback is provided it will be called whenever a new call is outgoing.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | call | HFP AG call object. |
    | number | Dialing number |

## [◆ ](#ad9925958c87b164113f607bd680ce2c3)ready\_to\_accept\_audio

| void(\* bt\_hfp\_ag\_cb::ready\_to\_accept\_audio) (struct bt\_hfp\_ag \*ag) |
| --- |

Ready to accept audio callback.

If this callback is provided it will be called whenever the HF is ready to accept audio. If the feature Enhanced Voice Recognition Status is supported by HF, the callback will be notified if the AT command AT+BVRA=2 is received. The HF may send this value during an ongoing VR (Voice Recognition) session to terminate audio output from the AG (if there is any) and prepare the AG for new audio input. Or, the callback will be notified after the voice recognition is activated. If `CONFIG_BT_HFP_AG_ENH_VOICE_RECG` is not enabled, the callback will not be notified.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

## [◆ ](#abe1b5d71279c2e3292b3b90043d75224)reject

| void(\* bt\_hfp\_ag\_cb::reject) (struct bt\_hfp\_ag\_call \*call) |
| --- |

HF call reject Callback.

If this callback is provided it will be called whenever the call is rejected.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

## [◆ ](#aecc8cdaf372d93f9cb531604f9b82d65)request\_phone\_number

| int(\* bt\_hfp\_ag\_cb::request\_phone\_number) (struct bt\_hfp\_ag \*ag, char \*\*number) |
| --- |

Request phone number callback.

If this callback is provided it will be called whenever the AT command AT+BINP=1 is received. If the upper layer accepts the request, it shall obtain a phone number. If the upper layer rejects the request, it shall return a an error. If `CONFIG_BT_HFP_AG_VOICE_TAG` is not enabled, the callback will not be notified.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Phone number of voice tag. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a9d6b978f82de6ded48881a87eb90aebb)retrieve

| void(\* bt\_hfp\_ag\_cb::retrieve) (struct bt\_hfp\_ag\_call \*call) |
| --- |

HF call retrieve Callback.

If this callback is provided it will be called whenever the call is retrieved.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

## [◆ ](#a0b8967f487d64556851420b2f4e059fe)ringing

| void(\* bt\_hfp\_ag\_cb::ringing) (struct bt\_hfp\_ag\_call \*call, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) in\_band) |
| --- |

HF ringing Callback.

If this callback is provided it will be called whenever the call is in the ringing

Parameters
:   | call | HFP AG call object. |
    | --- | --- |
    | in\_bond | true - in-bond ringing, false - No in-bond ringing |

## [◆ ](#aac2b1ff4d80361e0e5eea2481027b4cf)sco\_connected

| void(\* bt\_hfp\_ag\_cb::sco\_connected) (struct bt\_hfp\_ag \*ag, struct bt\_conn \*sco\_conn) |
| --- |

HF SCO/eSCO connected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection completes.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | sco\_conn | SCO/eSCO Connection object. |

## [◆ ](#a95600361e59a516f220a314e920c5858)sco\_disconnected

| void(\* bt\_hfp\_ag\_cb::sco\_disconnected) (struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

HF SCO/eSCO disconnected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection gets disconnected.

Parameters
:   | conn | SCO/eSCO Connection object. |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

## [◆ ](#a976016f32e462daf38cd6d24ba18ff3d)subscriber\_number

| int(\* bt\_hfp\_ag\_cb::subscriber\_number) (struct bt\_hfp\_ag \*ag, [bt\_hfp\_ag\_query\_subscriber\_func\_t](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3) func) |
| --- |

Get subscriber number callback.

If this callback is provided it will be called whenever the AT command AT+CNUM is received.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | func | Query subscriber number callback. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#adf9960da8a3f4c38f7fcd60501522462)terminate

| void(\* bt\_hfp\_ag\_cb::terminate) (struct bt\_hfp\_ag\_call \*call) |
| --- |

HF call terminate Callback.

If this callback is provided it will be called whenever the call is terminated.

Parameters
:   | call | HFP AG call object. |
    | --- | --- |

## [◆ ](#ad690d69c9786c69ad85e005e778b316c)transmit\_dtmf\_code

| void(\* bt\_hfp\_ag\_cb::transmit\_dtmf\_code) (struct bt\_hfp\_ag \*ag, char code) |
| --- |

Transmit a DTMF Code callback.

If this callback is provided it will be called whenever the AT command AT+VTS=<code> is received. During an ongoing call, the HF transmits the AT+VTS command to instruct the AG to transmit a specific DTMF code to its network connection.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | code | A specific DTMF code. |

## [◆ ](#aaad37582866c420ee41c3f730de16eb4)vgm

| void(\* bt\_hfp\_ag\_cb::vgm) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
| --- |

HF VGM setting callback.

If this callback is provided it will be called whenever the VGM gain setting is informed from HF.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | gain | HF microphone gain value. |

## [◆ ](#a38adb040dee9abd794f952322bf3d615)vgs

| void(\* bt\_hfp\_ag\_cb::vgs) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
| --- |

HF VGS setting callback.

If this callback is provided it will be called whenever the VGS gain setting is informed from HF.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | gain | HF speaker gain value. |

## [◆ ](#a16c528018a2e9e97320df885c049454f)voice\_recognition

| void(\* bt\_hfp\_ag\_cb::voice\_recognition) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
| --- |

Voice recognition activation/deactivation callback.

If this callback is provided it will be called whenever the voice recognition activation is changed. If voice recognition is activated, the upper layer should call [bt\_hfp\_ag\_audio\_connect](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066 "Create audio connection.") with appropriate codec ID to setup audio connection. If the callback is not provided by upper layer, the function [bt\_hfp\_ag\_audio\_connect](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066 "Create audio connection.") will be called with default codec ID [BT\_HFP\_AG\_CODEC\_CVSD](group__bt__hfp__ag.md#gada6266f825879f39147c5d889e4192c9). If `CONFIG_BT_HFP_AG_VOICE_RECG` is not enabled, the callback will not be notified.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | activate | Voice recognition activation/deactivation. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[hfp\_ag.h](hfp__ag_8h_source.md)

- [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
