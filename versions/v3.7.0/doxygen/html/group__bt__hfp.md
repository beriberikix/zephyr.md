---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__hfp.html
original_path: doxygen/html/group__bt__hfp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| struct | [bt\_hfp\_hf\_cmd\_complete](structbt__hfp__hf__cmd__complete.md) |
|  | HFP HF Command completion field. [More...](structbt__hfp__hf__cmd__complete.md#details) |
| struct | [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) |
|  | HFP profile application callback. [More...](structbt__hfp__hf__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [HFP\_HF\_CMD\_OK](#ga7c90e2ab7ed6c5b25252f88408235598)   0 |
| #define | [HFP\_HF\_CMD\_ERROR](#ga463b8eb680e7cbedfbf9c5e5628558af)   1 |
| #define | [HFP\_HF\_CMD\_CME\_ERROR](#ga80133496d4868f11381d14fe46cfdb51)   2 |
| #define | [HFP\_HF\_CMD\_UNKNOWN\_ERROR](#ga613fa4c3e102c7ab20e587f34c14d5c6)   4 |

| Enumerations | |
| --- | --- |
| enum | [bt\_hfp\_hf\_at\_cmd](#gae88edd233a1f00e6d12be7fe3ac8c9fd) { [BT\_HFP\_HF\_ATA](#ggae88edd233a1f00e6d12be7fe3ac8c9fdae80220d66b99e9f0954fa9491565f641) , [BT\_HFP\_HF\_AT\_CHUP](#ggae88edd233a1f00e6d12be7fe3ac8c9fdaa777f4b5e3b8310e528e535ca0667a18) } |

| Functions | |
| --- | --- |
| int | [bt\_hfp\_hf\_register](#ga2e4a7c05a3ba9a32eab50b9904f7f161) (struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \*cb) |
|  | Register HFP HF profile. |
| int | [bt\_hfp\_hf\_send\_cmd](#ga88f700df453cfca14926afb1db9c70d0) (struct bt\_conn \*conn, enum [bt\_hfp\_hf\_at\_cmd](#gae88edd233a1f00e6d12be7fe3ac8c9fd) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Handsfree client Send AT. |

## Detailed Description

Hands Free Profile (HFP).

## Macro Definition Documentation

## [◆ ](#ga80133496d4868f11381d14fe46cfdb51)HFP\_HF\_CMD\_CME\_ERROR

| #define HFP\_HF\_CMD\_CME\_ERROR   2 |
| --- |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

## [◆ ](#ga463b8eb680e7cbedfbf9c5e5628558af)HFP\_HF\_CMD\_ERROR

| #define HFP\_HF\_CMD\_ERROR   1 |
| --- |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

## [◆ ](#ga7c90e2ab7ed6c5b25252f88408235598)HFP\_HF\_CMD\_OK

| #define HFP\_HF\_CMD\_OK   0 |
| --- |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

## [◆ ](#ga613fa4c3e102c7ab20e587f34c14d5c6)HFP\_HF\_CMD\_UNKNOWN\_ERROR

| #define HFP\_HF\_CMD\_UNKNOWN\_ERROR   4 |
| --- |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gae88edd233a1f00e6d12be7fe3ac8c9fd)bt\_hfp\_hf\_at\_cmd

| enum [bt\_hfp\_hf\_at\_cmd](#gae88edd233a1f00e6d12be7fe3ac8c9fd) |
| --- |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_HFP\_HF\_ATA |  |
| BT\_HFP\_HF\_AT\_CHUP |  |

## Function Documentation

## [◆ ](#ga2e4a7c05a3ba9a32eab50b9904f7f161)bt\_hfp\_hf\_register()

| int bt\_hfp\_hf\_register | ( | struct [bt\_hfp\_hf\_cb](structbt__hfp__hf__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

Register HFP HF profile.

Register Handsfree profile callbacks to monitor the state and get the required HFP details to display.

Parameters
:   | cb | callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga88f700df453cfca14926afb1db9c70d0)bt\_hfp\_hf\_send\_cmd()

| int bt\_hfp\_hf\_send\_cmd | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_hfp\_hf\_at\_cmd](#gae88edd233a1f00e6d12be7fe3ac8c9fd) | *cmd* ) |

`#include <[hfp_hf.h](hfp__hf_8h.md)>`

Handsfree client Send AT.

Send specific AT commands to handsfree client profile.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | AT command to be sent. |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
