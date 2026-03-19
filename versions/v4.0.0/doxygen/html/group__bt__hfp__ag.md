---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__hfp__ag.html
original_path: doxygen/html/group__bt__hfp__ag.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| struct | [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) |
|  | HFP profile AG application callback. [More...](structbt__hfp__ag__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HFP\_AG\_CODEC\_CVSD](#gada6266f825879f39147c5d889e4192c9)   0x01 |
| #define | [BT\_HFP\_AG\_CODEC\_MSBC](#ga3591201c7310288ea2e01e2f77a0c0d3)   0x02 |
| #define | [BT\_HFP\_AG\_CODEC\_LC3\_SWB](#ga8a833c4b11dc9e8fd08a73a2af418d83)   0x03 |

| Enumerations | |
| --- | --- |
| enum | [bt\_hfp\_ag\_indicator](#ga37640efdcc737bfa0390df889a62f810) {     [BT\_HFP\_AG\_SERVICE\_IND](#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) = 0 , [BT\_HFP\_AG\_CALL\_IND](#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) = 1 , [BT\_HFP\_AG\_CALL\_SETUP\_IND](#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) = 2 , [BT\_HFP\_AG\_CALL\_HELD\_IND](#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) = 3 ,     [BT\_HFP\_AG\_SIGNAL\_IND](#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) = 4 , [BT\_HFP\_AG\_ROAM\_IND](#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) = 5 , [BT\_HFP\_AG\_BATTERY\_IND](#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) = 6 , [BT\_HFP\_AG\_IND\_MAX](#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)   } |

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
| int | [bt\_hfp\_ag\_reject](#ga7d9f25c3dfbac0af8e24b7d998635490) (struct bt\_hfp\_ag \*ag) |
|  | Reject the incoming call. |
| int | [bt\_hfp\_ag\_accept](#ga331262bc9024998435bf5f9154dddffc) (struct bt\_hfp\_ag \*ag) |
|  | Accept the incoming call. |
| int | [bt\_hfp\_ag\_terminate](#gaee0bb2269de783909e1c0d1658653047) (struct bt\_hfp\_ag \*ag) |
|  | Terminate the active/hold call. |
| int | [bt\_hfp\_ag\_outgoing](#ga580328104cf990c6f9e0a64642c16ebd) (struct bt\_hfp\_ag \*ag, const char \*number) |
|  | Dial a call. |
| int | [bt\_hfp\_ag\_remote\_ringing](#gaff92b4176aeaf9781e97b1b8d34efeb9) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote starts ringing. |
| int | [bt\_hfp\_ag\_remote\_reject](#ga4db1d508bebe6d468b498f328af70e9b) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote rejects the call. |
| int | [bt\_hfp\_ag\_remote\_accept](#ga9770c356e5003294f7c325ef7014c52a) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote accepts the call. |
| int | [bt\_hfp\_ag\_remote\_terminate](#ga1c115592d04ebdd208f67ed4bfaf056b) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote terminates the active/hold call. |

## Detailed Description

Hands Free Profile - Audio Gateway (HFP-AG).

## Macro Definition Documentation

## [◆ ](#gada6266f825879f39147c5d889e4192c9)BT\_HFP\_AG\_CODEC\_CVSD

| #define BT\_HFP\_AG\_CODEC\_CVSD   0x01 |
| --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

## [◆ ](#ga8a833c4b11dc9e8fd08a73a2af418d83)BT\_HFP\_AG\_CODEC\_LC3\_SWB

| #define BT\_HFP\_AG\_CODEC\_LC3\_SWB   0x03 |
| --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

## [◆ ](#ga3591201c7310288ea2e01e2f77a0c0d3)BT\_HFP\_AG\_CODEC\_MSBC

| #define BT\_HFP\_AG\_CODEC\_MSBC   0x02 |
| --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga37640efdcc737bfa0390df889a62f810)bt\_hfp\_ag\_indicator

| enum [bt\_hfp\_ag\_indicator](#ga37640efdcc737bfa0390df889a62f810) |
| --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

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

## Function Documentation

## [◆ ](#ga331262bc9024998435bf5f9154dddffc)bt\_hfp\_ag\_accept()

| int bt\_hfp\_ag\_accept | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Accept the incoming call.

Accept the incoming call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga5b602810558268396f0cb64adcb0d014)bt\_hfp\_ag\_connect()

| int bt\_hfp\_ag\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct bt\_hfp\_ag \*\* | *ag*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

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

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Disconnect the hfp ag session.

Disconnect the hfp ag session

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga580328104cf990c6f9e0a64642c16ebd)bt\_hfp\_ag\_outgoing()

| int bt\_hfp\_ag\_outgoing | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | const char \* | *number* ) |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Dial a call.

Dial a call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Dailing number. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga379ec1c540195549fc59417d8d1ce7e5)bt\_hfp\_ag\_register()

| int bt\_hfp\_ag\_register | ( | struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Register HFP AG profile.

Register Handsfree profile AG callbacks to monitor the state and get the required HFP details to display.

Parameters
:   | cb | callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga7d9f25c3dfbac0af8e24b7d998635490)bt\_hfp\_ag\_reject()

| int bt\_hfp\_ag\_reject | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Reject the incoming call.

Reject the incoming call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga9770c356e5003294f7c325ef7014c52a)bt\_hfp\_ag\_remote\_accept()

| int bt\_hfp\_ag\_remote\_accept | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote accepts the call.

Notify HFP Unit that the remote accepts the call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga443cd2928686f222d61f06c7477ea793)bt\_hfp\_ag\_remote\_incoming()

| int bt\_hfp\_ag\_remote\_incoming | ( | struct bt\_hfp\_ag \* | *ag*, |
| --- | --- | --- | --- |
|  |  | const char \* | *number* ) |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit of an incoming call.

Notify HFP Unit of an incoming call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |
    | number | Dailing number. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4db1d508bebe6d468b498f328af70e9b)bt\_hfp\_ag\_remote\_reject()

| int bt\_hfp\_ag\_remote\_reject | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote rejects the call.

Notify HFP Unit that the remote rejects the call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaff92b4176aeaf9781e97b1b8d34efeb9)bt\_hfp\_ag\_remote\_ringing()

| int bt\_hfp\_ag\_remote\_ringing | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote starts ringing.

Notify HFP Unit that the remote starts ringing.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga1c115592d04ebdd208f67ed4bfaf056b)bt\_hfp\_ag\_remote\_terminate()

| int bt\_hfp\_ag\_remote\_terminate | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Notify HFP Unit that the remote terminates the active/hold call.

Notify HFP Unit that the remote terminates the active/hold call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaee0bb2269de783909e1c0d1658653047)bt\_hfp\_ag\_terminate()

| int bt\_hfp\_ag\_terminate | ( | struct bt\_hfp\_ag \* | *ag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hfp_ag.h](hfp__ag_8h.md)>`

Terminate the active/hold call.

Terminate the active/hold call.

Parameters
:   | ag | HFP AG object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
