---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hfp__ag_8h.html
original_path: doxygen/html/hfp__ag_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hfp\_ag.h File Reference

Handsfree Profile Audio Gateway handling.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

[Go to the source code of this file.](hfp__ag_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) |
|  | HFP profile AG application callback. [More...](structbt__hfp__ag__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HFP\_AG\_CODEC\_CVSD](group__bt__hfp__ag.md#gada6266f825879f39147c5d889e4192c9)   0x01 |
| #define | [BT\_HFP\_AG\_CODEC\_MSBC](group__bt__hfp__ag.md#ga3591201c7310288ea2e01e2f77a0c0d3)   0x02 |
| #define | [BT\_HFP\_AG\_CODEC\_LC3\_SWB](group__bt__hfp__ag.md#ga8a833c4b11dc9e8fd08a73a2af418d83)   0x03 |

| Enumerations | |
| --- | --- |
| enum | [bt\_hfp\_ag\_indicator](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810) {     [BT\_HFP\_AG\_SERVICE\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) = 0 , [BT\_HFP\_AG\_CALL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) = 1 , [BT\_HFP\_AG\_CALL\_SETUP\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) = 2 , [BT\_HFP\_AG\_CALL\_HELD\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) = 3 ,     [BT\_HFP\_AG\_SIGNAL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) = 4 , [BT\_HFP\_AG\_ROAM\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) = 5 , [BT\_HFP\_AG\_BATTERY\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) = 6 , [BT\_HFP\_AG\_IND\_MAX](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)   } |

| Functions | |
| --- | --- |
| int | [bt\_hfp\_ag\_register](group__bt__hfp__ag.md#ga379ec1c540195549fc59417d8d1ce7e5) (struct [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) \*cb) |
|  | Register HFP AG profile. |
| int | [bt\_hfp\_ag\_connect](group__bt__hfp__ag.md#ga5b602810558268396f0cb64adcb0d014) (struct bt\_conn \*conn, struct bt\_hfp\_ag \*\*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Create the hfp ag session. |
| int | [bt\_hfp\_ag\_disconnect](group__bt__hfp__ag.md#gadf0b4aef701cf0986ea9599ad79d451a) (struct bt\_hfp\_ag \*ag) |
|  | Disconnect the hfp ag session. |
| int | [bt\_hfp\_ag\_remote\_incoming](group__bt__hfp__ag.md#ga443cd2928686f222d61f06c7477ea793) (struct bt\_hfp\_ag \*ag, const char \*number) |
|  | Notify HFP Unit of an incoming call. |
| int | [bt\_hfp\_ag\_reject](group__bt__hfp__ag.md#ga7d9f25c3dfbac0af8e24b7d998635490) (struct bt\_hfp\_ag \*ag) |
|  | Reject the incoming call. |
| int | [bt\_hfp\_ag\_accept](group__bt__hfp__ag.md#ga331262bc9024998435bf5f9154dddffc) (struct bt\_hfp\_ag \*ag) |
|  | Accept the incoming call. |
| int | [bt\_hfp\_ag\_terminate](group__bt__hfp__ag.md#gaee0bb2269de783909e1c0d1658653047) (struct bt\_hfp\_ag \*ag) |
|  | Terminate the active/hold call. |
| int | [bt\_hfp\_ag\_outgoing](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd) (struct bt\_hfp\_ag \*ag, const char \*number) |
|  | Dial a call. |
| int | [bt\_hfp\_ag\_remote\_ringing](group__bt__hfp__ag.md#gaff92b4176aeaf9781e97b1b8d34efeb9) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote starts ringing. |
| int | [bt\_hfp\_ag\_remote\_reject](group__bt__hfp__ag.md#ga4db1d508bebe6d468b498f328af70e9b) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote rejects the call. |
| int | [bt\_hfp\_ag\_remote\_accept](group__bt__hfp__ag.md#ga9770c356e5003294f7c325ef7014c52a) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote accepts the call. |
| int | [bt\_hfp\_ag\_remote\_terminate](group__bt__hfp__ag.md#ga1c115592d04ebdd208f67ed4bfaf056b) (struct bt\_hfp\_ag \*ag) |
|  | Notify HFP Unit that the remote terminates the active/hold call. |

## Detailed Description

Handsfree Profile Audio Gateway handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_ag.h](hfp__ag_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
