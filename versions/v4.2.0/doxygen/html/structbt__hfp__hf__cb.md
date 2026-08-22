---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__hfp__hf__cb.html
original_path: doxygen/html/structbt__hfp__hf__cb.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hfp\_hf\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hands Free Profile (HFP)](group__bt__hfp.md)

HFP profile application callback.
[More...](#details)

`#include <[zephyr/bluetooth/classic/hfp_hf.h](hfp__hf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#a68c09fe6aac4ff7f3b24e6a550e75d1e) )(struct bt\_conn \*conn, struct bt\_hfp\_hf \*hf) |
|  | HF connected callback to application. |
| void(\* | [disconnected](#afdf28b8d8f9598ee2f6fa826aba4fbba) )(struct bt\_hfp\_hf \*hf) |
|  | HF disconnected callback to application. |
| void(\* | [sco\_connected](#a6ea6f5a866d7e4da5e3fe894d700f6b6) )(struct bt\_hfp\_hf \*hf, struct bt\_conn \*sco\_conn) |
|  | HF SCO/eSCO connected Callback. |
| void(\* | [sco\_disconnected](#a4586240506c876c9f58cf60a091b4044) )(struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
|  | HF SCO/eSCO disconnected Callback. |
| void(\* | [service](#a8483c3a3ba8b0e5131bec6fce5dbc36d) )(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [outgoing](#a46677dbfe7e73dcdc3b6cacb0aa9fa58) )(struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call) |
|  | HF call outgoing Callback. |
| void(\* | [remote\_ringing](#ace8989f64fea9301d6f48e5252ceb2de) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF call outgoing call is ringing Callback. |
| void(\* | [incoming](#a597d2e9b20ffc2dfedd53aea2969727e) )(struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call) |
|  | HF call incoming Callback. |
| void(\* | [incoming\_held](#a71f0f50a83defe014b3b364dcc16ad9d) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF incoming call on hold Callback. |
| void(\* | [accept](#a44ae68eb055f23c30dd761fd6eb1c6cd) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF call accept Callback. |
| void(\* | [reject](#a9f248f9c7e3830c6941225bd4d2363d3) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF call reject Callback. |
| void(\* | [terminate](#a691ec076d6fba14636b873cf75262e81) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF call terminate Callback. |
| void(\* | [held](#af6fe24140f5a5a1aea2eff7b1e534cfd) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF call held Callback. |
| void(\* | [retrieve](#a4977076381a5c4daf620aa6c6ab558d3) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF call retrieve Callback. |
| void(\* | [signal](#add68ca4e00f7a5dbc28282ee29bea087) )(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [roam](#a13b35eb32e4f579d853657a2ea89af42) )(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [battery](#a17faaab9a9af5dc53018fc2f94855bea) )(struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | HF indicator Callback. |
| void(\* | [ring\_indication](#a2712d3a5d68bdf2de6dc27f938590c0a) )(struct bt\_hfp\_hf\_call \*call) |
|  | HF incoming call Ring indication callback to application. |
| void(\* | [dialing](#a80e98b5dd212158c255215b8a304d67c) )(struct bt\_hfp\_hf \*hf, int err) |
|  | HF call dialing Callback. |
| void(\* | [clip](#abcbdaa8312f6efe3711da0aabba52bce) )(struct bt\_hfp\_hf\_call \*call, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
|  | HF calling line identification notification callback to application. |
| void(\* | [vgm](#a512de9839559def9c2110a310f21ca03) )(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | HF microphone gain notification callback to application. |
| void(\* | [vgs](#a385cbe2c3a9c402a09b873a3ce753d8b) )(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
|  | HF speaker gain notification callback to application. |
| void(\* | [inband\_ring](#acc1ff77f98329986c2120b0c9c4f565a) )(struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) inband) |
|  | HF in-band ring tone notification callback to application. |
| void(\*)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) | [operator)](#a187ef5f2b7e4a4d8a4963e51453aefdb) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) format, char \*operator);void(\*codec\_negotiate |
|  | HF network operator notification callback to application. |
| void(\* | [ecnr\_turn\_off](#a0f2da8d9169658c03d2dabe2c8b1cf6f) )(struct bt\_hfp\_hf \*hf, int err) |
|  | HF ECNR turns off callback. |
| void(\* | [call\_waiting](#a283a791f330a49f402cde0233ad05f6e) )(struct bt\_hfp\_hf\_call \*call, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
|  | HF call waiting notification callback to application. |
| void(\* | [voice\_recognition](#a07da1a6c86031c42749972d5d9fb7677) )(struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
|  | Voice recognition activation/deactivation callback. |
| void(\* | [vre\_state](#a298a6d3315535331ffb779899db9f973) )(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Voice recognition engine state callback. |
| void(\* | [textual\_representation](#a1e7a4046b01ce4753352f86c209e171f) )(struct bt\_hfp\_hf \*hf, char \*id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) operation, char \*text) |
|  | Textual representation callback. |
| void(\* | [request\_phone\_number](#ac1e9fb5d0446d498b6cf3705a05633e2) )(struct bt\_hfp\_hf \*hf, const char \*number) |
|  | Request phone number callback. |
| void(\* | [subscriber\_number](#ae5682d96bdf18b148fac7ce1d9cbdb75) )(struct bt\_hfp\_hf \*hf, const char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)) |
|  | Query subscriber number callback. |

## Detailed Description

HFP profile application callback.

## Field Documentation

## [◆ ](#a44ae68eb055f23c30dd761fd6eb1c6cd)accept

| void(\* bt\_hfp\_hf\_cb::accept) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call accept Callback.

This callback provides the incoming/outgoing call active status to the application.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#a17faaab9a9af5dc53018fc2f94855bea)battery

| void(\* bt\_hfp\_hf\_cb::battery) (struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback battery service indicator value to the application

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | value | battery indicator value received from the AG. |

## [◆ ](#a283a791f330a49f402cde0233ad05f6e)call\_waiting

| void(\* bt\_hfp\_hf\_cb::call\_waiting) (struct bt\_hfp\_hf\_call \*call, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
| --- |

HF call waiting notification callback to application.

If this callback is provided it will be called whenever there is a unsolicited result code +CCWA. This notification can be enabled/disabled by calling function [bt\_hfp\_hf\_call\_waiting\_notify](group__bt__hfp.md#ga3afb0d82551708975dbeb9c903c3d1fb "Handsfree HF enable/disable call waiting notification."). If `CONFIG_BT_HFP_HF_3WAY_CALL` is not enabled, the unsolicited result code +CCWA will be ignored. And the callback will not be notified.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |
    | number | Notified phone number. |
    | type | Specify the format of the phone number. |

## [◆ ](#abcbdaa8312f6efe3711da0aabba52bce)clip

| void(\* bt\_hfp\_hf\_cb::clip) (struct bt\_hfp\_hf\_call \*call, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
| --- |

HF calling line identification notification callback to application.

If this callback is provided it will be called whenever there is a unsolicited result code +CLIP. If `CONFIG_BT_HFP_HF_CLI` is not enabled, the unsolicited result code +CLIP will be ignored. And the callback will not be notified.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |
    | number | Notified phone number. |
    | type | Specify the format of the phone number. |

## [◆ ](#a68c09fe6aac4ff7f3b24e6a550e75d1e)connected

| void(\* bt\_hfp\_hf\_cb::connected) (struct bt\_conn \*conn, struct bt\_hfp\_hf \*hf) |
| --- |

HF connected callback to application.

If this callback is provided it will be called whenever the connection completes.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | hf | HFP HF object. |

## [◆ ](#a80e98b5dd212158c255215b8a304d67c)dialing

| void(\* bt\_hfp\_hf\_cb::dialing) (struct bt\_hfp\_hf \*hf, int err) |
| --- |

HF call dialing Callback.

This callback provides call dialing result to the application.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | err | Result of calling dialing. |

## [◆ ](#afdf28b8d8f9598ee2f6fa826aba4fbba)disconnected

| void(\* bt\_hfp\_hf\_cb::disconnected) (struct bt\_hfp\_hf \*hf) |
| --- |

HF disconnected callback to application.

If this callback is provided it will be called whenever the connection gets disconnected, including when a connection gets rejected or cancelled or any error in SLC establishment. And the HFP HF object will be freed after the registered callback [disconnected](#afdf28b8d8f9598ee2f6fa826aba4fbba) returned.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |

## [◆ ](#a0f2da8d9169658c03d2dabe2c8b1cf6f)ecnr\_turn\_off

| void(\* bt\_hfp\_hf\_cb::ecnr\_turn\_off) (struct bt\_hfp\_hf \*hf, int err) |
| --- |

HF ECNR turns off callback.

If this callback is provided it will be called whenever the response of ECNR turning off is received from AG. If `CONFIG_BT_HFP_HF_ECNR` is not enabled, the callback will not be notified.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | err | The result of request. |

## [◆ ](#af6fe24140f5a5a1aea2eff7b1e534cfd)held

| void(\* bt\_hfp\_hf\_cb::held) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call held Callback.

This callback provides call held to the application

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#acc1ff77f98329986c2120b0c9c4f565a)inband\_ring

| void(\* bt\_hfp\_hf\_cb::inband\_ring) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) inband) |
| --- |

HF in-band ring tone notification callback to application.

If this callback is provided it will be called whenever there is a unsolicited result code +BSIR issued by the AG to indicate to the HF that the in-band ring tone setting has been locally changed.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | inband | In-band ring tone status from the AG. |

## [◆ ](#a597d2e9b20ffc2dfedd53aea2969727e)incoming

| void(\* bt\_hfp\_hf\_cb::incoming) (struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call incoming Callback.

This callback provides the incoming call status to the application.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | call | HFP HF call object. |

## [◆ ](#a71f0f50a83defe014b3b364dcc16ad9d)incoming\_held

| void(\* bt\_hfp\_hf\_cb::incoming\_held) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF incoming call on hold Callback.

This callback provides the incoming call on hold status to the application.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#a187ef5f2b7e4a4d8a4963e51453aefdb)operator)

| void(\*)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) bt\_hfp\_hf\_cb::operator)(struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) format, char \*operator); void(\*codec\_negotiate |
| --- |

HF network operator notification callback to application.

If this callback is provided it will be called whenever there is a response code +COPS issued by the AG to response the AT+COPS? command issued by the HF by calling function [bt\_hfp\_hf\_get\_operator](group__bt__hfp.md#gaaa9fbdceec140f274fc88c063a4cd4b8 "Handsfree HF requests currently selected operator.").

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | mode | Current mode. |
    | format | Format of the operator parameter string. It should be zero. |
    | operator | A string in alphanumeric format representing the name of the network operator. |

## [◆ ](#a46677dbfe7e73dcdc3b6cacb0aa9fa58)outgoing

| void(\* bt\_hfp\_hf\_cb::outgoing) (struct bt\_hfp\_hf \*hf, struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call outgoing Callback.

This callback provides the outgoing call status to the application.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | call | HFP HF call object. |

## [◆ ](#a9f248f9c7e3830c6941225bd4d2363d3)reject

| void(\* bt\_hfp\_hf\_cb::reject) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call reject Callback.

This callback provides the incoming/outgoing call reject status to the application.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#ace8989f64fea9301d6f48e5252ceb2de)remote\_ringing

| void(\* bt\_hfp\_hf\_cb::remote\_ringing) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call outgoing call is ringing Callback.

This callback provides the outgoing call is ringing status to the application.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#ac1e9fb5d0446d498b6cf3705a05633e2)request\_phone\_number

| void(\* bt\_hfp\_hf\_cb::request\_phone\_number) (struct bt\_hfp\_hf \*hf, const char \*number) |
| --- |

Request phone number callback.

If this callback is provided it will be called whenever the result code +BINP: <Phone number> is received from AG. If the request is failed, the number will be NULL.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | number | Value of <Phone number>. |

## [◆ ](#a4977076381a5c4daf620aa6c6ab558d3)retrieve

| void(\* bt\_hfp\_hf\_cb::retrieve) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call retrieve Callback.

This callback provides call retrieved to the application

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#a2712d3a5d68bdf2de6dc27f938590c0a)ring\_indication

| void(\* bt\_hfp\_hf\_cb::ring\_indication) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF incoming call Ring indication callback to application.

If this callback is provided it will be called whenever there is an incoming call.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#a13b35eb32e4f579d853657a2ea89af42)roam

| void(\* bt\_hfp\_hf\_cb::roam) (struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides roaming indicator value to the application

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | value | roaming indicator value received from the AG. |

## [◆ ](#a6ea6f5a866d7e4da5e3fe894d700f6b6)sco\_connected

| void(\* bt\_hfp\_hf\_cb::sco\_connected) (struct bt\_hfp\_hf \*hf, struct bt\_conn \*sco\_conn) |
| --- |

HF SCO/eSCO connected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection completes.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | sco\_conn | SCO/eSCO Connection object. |

## [◆ ](#a4586240506c876c9f58cf60a091b4044)sco\_disconnected

| void(\* bt\_hfp\_hf\_cb::sco\_disconnected) (struct bt\_conn \*sco\_conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason) |
| --- |

HF SCO/eSCO disconnected Callback.

If this callback is provided it will be called whenever the SCO/eSCO connection gets disconnected.

Parameters
:   | conn | SCO/eSCO Connection object. |
    | --- | --- |
    | reason | BT\_HCI\_ERR\_\* reason for the disconnection. |

## [◆ ](#a8483c3a3ba8b0e5131bec6fce5dbc36d)service

| void(\* bt\_hfp\_hf\_cb::service) (struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides service indicator value to the application

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | value | service indicator value received from the AG. |

## [◆ ](#add68ca4e00f7a5dbc28282ee29bea087)signal

| void(\* bt\_hfp\_hf\_cb::signal) (struct bt\_hfp\_hf \*hf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
| --- |

HF indicator Callback.

This callback provides signal indicator value to the application

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | value | signal indicator value received from the AG. |

## [◆ ](#ae5682d96bdf18b148fac7ce1d9cbdb75)subscriber\_number

| void(\* bt\_hfp\_hf\_cb::subscriber\_number) (struct bt\_hfp\_hf \*hf, const char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)) |
| --- |

Query subscriber number callback.

If this callback is provided it will be called whenever the result code +CUNM: [<alpha>],<number>, <type>,[<speed> ,<[service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)>] is received from AG. <alpha>: This optional field is not supported, and shall be left blank. <number>: Quoted string containing the phone number in the format specified by <type>. <type> field specifies the format of the phone number provided, and can be one of the following values:

- values 128-143: The phone number format may be a national or international format, and may contain prefix and/or escape digits. No changes on the number presentation are required.
- values 144-159: The phone number format is an international number, including the country code prefix. If the plus sign ("+") is not included as part of the number and shall be added by the AG as needed.
- values 160-175: National number. No prefix nor escape digits included. <speed>: This optional field is not supported, and shall be left blank. <[service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)>: Indicates which service this phone number relates to. Shall be either 4 (voice) or 5 (fax).

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | number | Value of <number> without quotes. |
    | type | Value of <type>. |
    | [service](#a8483c3a3ba8b0e5131bec6fce5dbc36d) | Value of <[service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)>. |

## [◆ ](#a691ec076d6fba14636b873cf75262e81)terminate

| void(\* bt\_hfp\_hf\_cb::terminate) (struct bt\_hfp\_hf\_call \*call) |
| --- |

HF call terminate Callback.

This callback provides the incoming/outgoing call terminate status to the application.

Parameters
:   | call | HFP HF call object. |
    | --- | --- |

## [◆ ](#a1e7a4046b01ce4753352f86c209e171f)textual\_representation

| void(\* bt\_hfp\_hf\_cb::textual\_representation) (struct bt\_hfp\_hf \*hf, char \*id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) operation, char \*text) |
| --- |

Textual representation callback.

If this callback is provided it will be called whenever the unsolicited result code +BVRA: 1,<vrecstate>,
<textualRepresentation> is received from AG. <textualRepresentation>: <textID>,<textType>,<textOperation>,
<string>. <textID>: Unique ID of the current text as a hexadecimal string (a maximum of 4 characters in length, but less than 4 characters in length is valid). <textType>: ID of the textType from the following list: 0 - Text recognized by the AG from the audio input provided by the HF 1 - Text of the audio output from the AG 2 - Text of the audio output from the AG that contains a question 3 - Text of the audio output from the AG that contains an error description <textOperation>: ID of the operation of the text 1 - NewText: Indicates that a new text started. Shall be used when the <textID> changes 2 - Replace: Replace any existing text with the same <textID> and same <textType> 3 - Append: Attach new text to existing text and keep the same <textID> and same <textType> <string>: The <string> parameter shall be a UTF-8 text string and shall always be contained within double quotes. If `CONFIG_BT_HFP_HF_VOICE_RECG_TEXT` is not enabled, the unsolicited result code +BVRA will be ignored. And the callback will not be notified.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | id | Value of <textID>. |
    | type | Value of <textType>. |
    | operation | Value of <textOperation>. |
    | text | Value of <string>. |

## [◆ ](#a512de9839559def9c2110a310f21ca03)vgm

| void(\* bt\_hfp\_hf\_cb::vgm) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
| --- |

HF microphone gain notification callback to application.

If this callback is provided it will be called whenever there is a unsolicited result code +VGM. If `CONFIG_BT_HFP_HF_VOLUME` is not enabled, the unsolicited result code +VGM will be ignored. And the callback will not be notified.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | gain | Microphone gain. |

## [◆ ](#a385cbe2c3a9c402a09b873a3ce753d8b)vgs

| void(\* bt\_hfp\_hf\_cb::vgs) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gain) |
| --- |

HF speaker gain notification callback to application.

If this callback is provided it will be called whenever there is a unsolicited result code +VGS. If `CONFIG_BT_HFP_HF_VOLUME` is not enabled, the unsolicited result code +VGS will be ignored. And the callback will not be notified.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | gain | Speaker gain. |

## [◆ ](#a07da1a6c86031c42749972d5d9fb7677)voice\_recognition

| void(\* bt\_hfp\_hf\_cb::voice\_recognition) (struct bt\_hfp\_hf \*hf, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
| --- |

Voice recognition activation/deactivation callback.

If this callback is provided it will be called whenever the unsolicited result code +BVRA is notified the HF when the voice recognition function in the AG is activated/deactivated autonomously from the AG. If `CONFIG_BT_HFP_HF_VOICE_RECG` is not enabled, the unsolicited result code +BVRA will be ignored. And the callback will not be notified.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | activate | Voice recognition activation/deactivation. |

## [◆ ](#a298a6d3315535331ffb779899db9f973)vre\_state

| void(\* bt\_hfp\_hf\_cb::vre\_state) (struct bt\_hfp\_hf \*hf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Voice recognition engine state callback.

If this callback is provided it will be called whenever the unsolicited result code +BVRA: 1,<vrecstate> is received from AG. <vrecstate>: Bitmask that reflects the current state of the voice recognition engine on the AG. Bit 0 - If it is 1, the AG is ready to accept audio input Bit 1 - If it is 1, the AG is sending audio to the HF Bit 2 - If it is 1, the AG is processing the audio input If `CONFIG_BT_HFP_HF_ENH_VOICE_RECG` is not enabled, the unsolicited result code +BVRA will be ignored. And the callback will not be notified.

Parameters
:   | hf | HFP HF object. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Value of <vrecstate>. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[hfp\_hf.h](hfp__hf_8h_source.md)

- [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
