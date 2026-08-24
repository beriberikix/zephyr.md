---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/hfp__ag_8h.html
original_path: doxygen/html/hfp__ag_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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
| struct | [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) |
|  | The ongoing call. [More...](structbt__hfp__ag__ongoing__call.md#details) |
| struct | [bt\_hfp\_ag\_cb](structbt__hfp__ag__cb.md) |
|  | HFP profile AG application callback. [More...](structbt__hfp__ag__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HFP\_AG\_CODEC\_CVSD](group__bt__hfp__ag.md#gada6266f825879f39147c5d889e4192c9)   0x01 |
| #define | [BT\_HFP\_AG\_CODEC\_MSBC](group__bt__hfp__ag.md#ga3591201c7310288ea2e01e2f77a0c0d3)   0x02 |
| #define | [BT\_HFP\_AG\_CODEC\_LC3\_SWB](group__bt__hfp__ag.md#ga8a833c4b11dc9e8fd08a73a2af418d83)   0x03 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bt\_hfp\_ag\_query\_subscriber\_func\_t](group__bt__hfp__ag.md#ga8e9b485f7ea0b9e16d96f578cdc587c3)) (struct bt\_hfp\_ag \*ag, char \*number, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) service) |
|  | Query subscriber number callback function. |

| Enumerations | |
| --- | --- |
| enum | [bt\_hfp\_ag\_indicator](group__bt__hfp__ag.md#ga37640efdcc737bfa0390df889a62f810) {     [BT\_HFP\_AG\_SERVICE\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a13fa7a77558d6ddf93ddd8b9e34c5234) = 0 , [BT\_HFP\_AG\_CALL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a78ef8e7f1f03e8b0da2dda8bb3f9ea2d) = 1 , [BT\_HFP\_AG\_CALL\_SETUP\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a1829dd27fbc24ca6d9952df8df681dc5) = 2 , [BT\_HFP\_AG\_CALL\_HELD\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a2869f7d789510ec91a9a520111d2a62b) = 3 ,     [BT\_HFP\_AG\_SIGNAL\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a30869bb7156f0bc4011e3f41c1fdb493) = 4 , [BT\_HFP\_AG\_ROAM\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810aad71a9e71a040453774da0e17139d863) = 5 , [BT\_HFP\_AG\_BATTERY\_IND](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810a3555b3da0680b4eb596c70be768aa609) = 6 , [BT\_HFP\_AG\_IND\_MAX](group__bt__hfp__ag.md#gga37640efdcc737bfa0390df889a62f810ae52dc798fb656997b3c87b7170c85f36)   } |
| enum | [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) { [HFP\_AG\_ENHANCED\_SAFETY\_IND](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403afd31a626b024de7e6e68ade0d776b14f) = 1 , [HFP\_AG\_BATTERY\_LEVEL\_IND](group__bt__hfp__ag.md#gga030c97d703fb45a2055653c51cb1b403a9719aca10a790eb9f62d498bc4bec9d1) = 2 } |
| enum | [bt\_hfp\_ag\_call\_status](group__bt__hfp__ag.md#gad2220b4a470cb3d537cf09492847568e) {     [BT\_HFP\_AG\_CALL\_STATUS\_ACTIVE](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4c387d6e8628fc40e9969c95ff9ea658) = 0 , [BT\_HFP\_AG\_CALL\_STATUS\_HELD](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568eac2acf82710d562fd2852139f7e8146e2) = 1 , [BT\_HFP\_AG\_CALL\_STATUS\_DIALING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea09545d4deadcc910c42b615d21f91963) = 2 , [BT\_HFP\_AG\_CALL\_STATUS\_ALERTING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea423017739b17f57e0a8adb7d6b9cffae) = 3 ,     [BT\_HFP\_AG\_CALL\_STATUS\_INCOMING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea4faad88cf6cb9926f78e7da7065713f8) = 4 , [BT\_HFP\_AG\_CALL\_STATUS\_WAITING](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea5b1a40f632b8d9ce3b02ffacb1a07fb2) = 5 , [BT\_HFP\_AG\_CALL\_STATUS\_INCOMING\_HELD](group__bt__hfp__ag.md#ggad2220b4a470cb3d537cf09492847568ea2e155da5b54cb32a400de1d44ebc2542) = 6   } |
| enum | [bt\_hfp\_ag\_call\_dir](group__bt__hfp__ag.md#ga019020ee2ed73c218f7dadf8371bf9a6) { [BT\_HFP\_AG\_CALL\_DIR\_OUTGOING](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a83ea29c4261577438e481e2b9f0c7d37) = 0 , [BT\_HFP\_AG\_CALL\_DIR\_INCOMING](group__bt__hfp__ag.md#gga019020ee2ed73c218f7dadf8371bf9a6a08a4f52a9ca4fdcaa1c6575b1b378b55) = 1 } |

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
| int | [bt\_hfp\_ag\_hold\_incoming](group__bt__hfp__ag.md#gab288d6e6b45a24b706328da58ca43a3b) (struct bt\_hfp\_ag\_call \*call) |
|  | Put the incoming call on hold. |
| int | [bt\_hfp\_ag\_reject](group__bt__hfp__ag.md#ga195daffc37f1a3f210ba52dae1a9c4c2) (struct bt\_hfp\_ag\_call \*call) |
|  | Reject the incoming call. |
| int | [bt\_hfp\_ag\_accept](group__bt__hfp__ag.md#ga351e1b78b8c19c3971554fabb331e5c6) (struct bt\_hfp\_ag\_call \*call) |
|  | Accept the incoming call. |
| int | [bt\_hfp\_ag\_terminate](group__bt__hfp__ag.md#ga2f2e85a6076930ed87bc0727c75209a9) (struct bt\_hfp\_ag\_call \*call) |
|  | Terminate the active/hold call. |
| int | [bt\_hfp\_ag\_retrieve](group__bt__hfp__ag.md#ga405fcf8e03bac39bd5b0e7bf2766045f) (struct bt\_hfp\_ag\_call \*call) |
|  | Retrieve the held call. |
| int | [bt\_hfp\_ag\_hold](group__bt__hfp__ag.md#ga4bbcec3ed5394e965aa7404dc968b94d) (struct bt\_hfp\_ag\_call \*call) |
|  | Hold the active call. |
| int | [bt\_hfp\_ag\_outgoing](group__bt__hfp__ag.md#ga580328104cf990c6f9e0a64642c16ebd) (struct bt\_hfp\_ag \*ag, const char \*number) |
|  | Dial a call. |
| int | [bt\_hfp\_ag\_remote\_ringing](group__bt__hfp__ag.md#ga0a12a56baa25e2aea101a387fcccb88e) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote starts ringing. |
| int | [bt\_hfp\_ag\_remote\_reject](group__bt__hfp__ag.md#gacb1b361e6b0a441102f7ccd641eb3e6b) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote rejects the call. |
| int | [bt\_hfp\_ag\_remote\_accept](group__bt__hfp__ag.md#ga018d8ed8912f9dcef8c5fa37ac2bd889) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote accepts the call. |
| int | [bt\_hfp\_ag\_remote\_terminate](group__bt__hfp__ag.md#ga525085c7c75e412ca43ba8b23cbc0c3d) (struct bt\_hfp\_ag\_call \*call) |
|  | Notify HFP Unit that the remote terminates the active/hold call. |
| int | [bt\_hfp\_ag\_explicit\_call\_transfer](group__bt__hfp__ag.md#ga5e249248a52d7c95c9d3f3f852bf2314) (struct bt\_hfp\_ag \*ag) |
|  | explicit call transfer |
| int | [bt\_hfp\_ag\_vgm](group__bt__hfp__ag.md#ga53778bd332c95fa4357d254f5ef125a2) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vgm) |
|  | Set the HF microphone gain. |
| int | [bt\_hfp\_ag\_vgs](group__bt__hfp__ag.md#gabdad8c764c91e133598584d741ed9d4b) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) vgs) |
|  | Set the HF speaker gain. |
| int | [bt\_hfp\_ag\_set\_operator](group__bt__hfp__ag.md#gaaf066dce38c028254b6c1880bcebaa13) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, char \*name) |
|  | Set currently network operator. |
| int | [bt\_hfp\_ag\_audio\_connect](group__bt__hfp__ag.md#ga542a1754a16e32a9b2651f1230aa7066) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Create audio connection. |
| int | [bt\_hfp\_ag\_inband\_ringtone](group__bt__hfp__ag.md#ga881ea4d3cc732fb5d804df203dde7746) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) inband) |
|  | Set In-Band Ring Tone. |
| int | [bt\_hfp\_ag\_voice\_recognition](group__bt__hfp__ag.md#ga28682fc5d8cfee9c0adece68bcb94c3f) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) activate) |
|  | Enable/disable the voice recognition function. |
| int | [bt\_hfp\_ag\_vre\_state](group__bt__hfp__ag.md#ga3668f3997afe9ab678f9eb2e6faf324d) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | set voice recognition engine state |
| int | [bt\_hfp\_ag\_vre\_textual\_representation](group__bt__hfp__ag.md#ga4e71364283448c7c5d3306c111aa167d) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const char \*id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) operation, const char \*text) |
|  | set voice recognition engine state and textual representation |
| int | [bt\_hfp\_ag\_signal\_strength](group__bt__hfp__ag.md#ga20ef1240e0ff72d914405b259cc3164f) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) strength) |
|  | Set signal strength. |
| int | [bt\_hfp\_ag\_roaming\_status](group__bt__hfp__ag.md#ga0f8b2e463aefbf74b26ac4f27033486c) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status) |
|  | Set roaming status. |
| int | [bt\_hfp\_ag\_battery\_level](group__bt__hfp__ag.md#ga4da632e9775051df6a5b5010fd3806df) (struct bt\_hfp\_ag \*ag, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Set battery level. |
| int | [bt\_hfp\_ag\_service\_availability](group__bt__hfp__ag.md#gaf838e54046c380931f23a59919ccfa5b) (struct bt\_hfp\_ag \*ag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) available) |
|  | Set service availability. |
| int | [bt\_hfp\_ag\_hf\_indicator](group__bt__hfp__ag.md#gaacc2df6144e1a33b13635855fe74f1f1) (struct bt\_hfp\_ag \*ag, enum [hfp\_ag\_hf\_indicators](group__bt__hfp__ag.md#ga030c97d703fb45a2055653c51cb1b403) indicator, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Activate/deactivate HF indicator. |
| int | [bt\_hfp\_ag\_ongoing\_calls](group__bt__hfp__ag.md#ga5614bf3f1de11959a0364f458523e06e) (struct bt\_hfp\_ag \*ag, struct [bt\_hfp\_ag\_ongoing\_call](structbt__hfp__ag__ongoing__call.md) \*calls, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Set the ongoing calls. |

## Detailed Description

Handsfree Profile Audio Gateway handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [hfp\_ag.h](hfp__ag_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
