---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/wifi_8h.html
original_path: doxygen/html/wifi_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi.h File Reference

IEEE 802.11 protocol and general Wi-Fi definitions.
[More...](#details)

`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](wifi_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_COUNTRY\_CODE\_LEN](group__wifi__mgmt.md#ga6766ef7bcb001f1fb526a4083b6cd8bc)   2 |
| #define | [WIFI\_LISTEN\_INTERVAL\_MIN](group__wifi__mgmt.md#gae8f678a142ff5c3550ef2796564e2cf7)   0 |
| #define | [WIFI\_LISTEN\_INTERVAL\_MAX](group__wifi__mgmt.md#ga5f38446f609dd58891ec5f394067b97f)   65535 |
| #define | [WIFI\_SSID\_MAX\_LEN](group__wifi__mgmt.md#gad62c60666c9fdffe2e0e9c4388f87886)   32 |
| #define | [WIFI\_PSK\_MIN\_LEN](group__wifi__mgmt.md#gaa8e19abf8c85f237ba5033740ceff553)   8 |
| #define | [WIFI\_PSK\_MAX\_LEN](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc)   64 |
| #define | [WIFI\_SAE\_PSWD\_MAX\_LEN](group__wifi__mgmt.md#gab63fa744cc2e049cfd635ab0a187971f)   128 |
| #define | [WIFI\_MAC\_ADDR\_LEN](group__wifi__mgmt.md#ga29409ff83a53c6464decdde9bdd04de6)   6 |
| #define | [WIFI\_CHANNEL\_MIN](group__wifi__mgmt.md#ga260e473dac1e823fd298a2c982470e0b)   1 |
| #define | [WIFI\_CHANNEL\_MAX](group__wifi__mgmt.md#ga8ea9141108f93b419f6a6530bf67bd95)   233 |
| #define | [WIFI\_CHANNEL\_ANY](group__wifi__mgmt.md#ga3876cd718af9f8a7b3682546da854544)   255 |
| #define | [WIFI\_INTERFACE\_INDEX\_MIN](group__wifi__mgmt.md#gaa1a74ef94af57a7ea966c691c065a46d)   1 |
| #define | [WIFI\_INTERFACE\_INDEX\_MAX](group__wifi__mgmt.md#gaa6cbecd7d4197d453038d3da7ef6be7b)   255 |

| Enumerations | |
| --- | --- |
| enum | [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) {     [WIFI\_SECURITY\_TYPE\_NONE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca3f0a729e3c906d9c398a9fba163a0a9e) = 0 , [WIFI\_SECURITY\_TYPE\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca1b9f70d6425eaa5a94211826a91c2368) , [WIFI\_SECURITY\_TYPE\_PSK\_SHA256](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca0554b0fd5a6233aba5e25b035488380e) , [WIFI\_SECURITY\_TYPE\_SAE](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca00d5a50935f70344f03c778055755c2f) ,     [WIFI\_SECURITY\_TYPE\_WAPI](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca37ab810084b3e024731f440e708b363d) , [WIFI\_SECURITY\_TYPE\_EAP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cacce1e8fbfbf71fb4d669e9d0bfb04f80) , [WIFI\_SECURITY\_TYPE\_WEP](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca39b793d7f7c49dee4e60a5c6e6831724) , [WIFI\_SECURITY\_TYPE\_WPA\_PSK](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca4fd23c30c3b666132903fef27fd0651a) ,     **\_\_WIFI\_SECURITY\_TYPE\_AFTER\_LAST** , [WIFI\_SECURITY\_TYPE\_MAX](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9cad17136673954190e01f783aca46e4b11) = \_\_WIFI\_SECURITY\_TYPE\_AFTER\_LAST - 1 , [WIFI\_SECURITY\_TYPE\_UNKNOWN](group__wifi__mgmt.md#ggadde31a04fa25ed805115c6b31854cd9ca8020497e098d4d6b9204ccf559c1ceaa)   } |
|  | IEEE 802.11 security types. [More...](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) |
| enum | [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) {     [WIFI\_MFP\_DISABLE](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a260e7b4688790ed39f4f7dc70547e969) = 0 , [WIFI\_MFP\_OPTIONAL](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a3ffdc747c7c70f7c1b70c96292f57fbf) , [WIFI\_MFP\_REQUIRED](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76af118a2f047c13db04d164235fa15f840) , **\_\_WIFI\_MFP\_AFTER\_LAST** ,     [WIFI\_MFP\_MAX](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76a649ca13c972fe7c8ad3ad085cb6df8ac) = \_\_WIFI\_MFP\_AFTER\_LAST - 1 , [WIFI\_MFP\_UNKNOWN](group__wifi__mgmt.md#gga1f252da47d9650023d7fff6d08e49c76aa6c8309128f71abdb748a87c935da378)   } |
|  | IEEE 802.11w - Management frame protection. [More...](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) |
| enum | [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) {     [WIFI\_FREQ\_BAND\_2\_4\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da5f9b51af36837670cca39e21e46b0b11) = 0 , [WIFI\_FREQ\_BAND\_5\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15dad967a3e96fd9aa8201071310a6a62895) , [WIFI\_FREQ\_BAND\_6\_GHZ](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da4f82878368ada29ce8986dd173efdcc0) , **\_\_WIFI\_FREQ\_BAND\_AFTER\_LAST** ,     [WIFI\_FREQ\_BAND\_MAX](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15daea3a12c499228420adc9f3aac21d67a5) = \_\_WIFI\_FREQ\_BAND\_AFTER\_LAST - 1 , [WIFI\_FREQ\_BAND\_UNKNOWN](group__wifi__mgmt.md#gga1e2f0439a322355fa7368ea880c9c15da8091041d87f7df93223527a31e7e76a5)   } |
|  | IEEE 802.11 operational frequency bands (not exhaustive). [More...](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) |
| enum | [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) {     [WIFI\_STATE\_DISCONNECTED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0b8eb7a4abfc3767cf2fc8244529435f) = 0 , [WIFI\_STATE\_INTERFACE\_DISABLED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a19974cdb014393eb790b798f274a0a5c) , [WIFI\_STATE\_INACTIVE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aec77d64f5aa60ab16b92b959674fa598) , [WIFI\_STATE\_SCANNING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a95d7970cb93ec284fbdc1d4ec5d6f99b) ,     [WIFI\_STATE\_AUTHENTICATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a96a063e6a22124d4c9f5403833da47ba) , [WIFI\_STATE\_ASSOCIATING](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaed2e6aeb678013a1723061e13de463b) , [WIFI\_STATE\_ASSOCIATED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a890de4b839cbf4608da8895ea0999ddc) , [WIFI\_STATE\_4WAY\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a20c83447900bda237aab6466ca56f969) ,     [WIFI\_STATE\_GROUP\_HANDSHAKE](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0efa624eebc1f985c9a25e155f2ecf1e) , [WIFI\_STATE\_COMPLETED](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4aaeaa0f48af3cdd51c20d37001a06106f) , **\_\_WIFI\_STATE\_AFTER\_LAST** , [WIFI\_STATE\_MAX](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a8385cb08d9b7479ce237faed184fa35b) = \_\_WIFI\_STATE\_AFTER\_LAST - 1 ,     [WIFI\_STATE\_UNKNOWN](group__wifi__mgmt.md#gga981961f747b919d61d3ccbd41e4508b4a0224a71eca32a9753f05d01f97064e64)   } |
|  | Wi-Fi interface states. [More...](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) |
| enum | [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) {     [WIFI\_MODE\_INFRA](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423bae5da6b5ad0afa9d29172935e3409f813) = 0 , [WIFI\_MODE\_IBSS](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba2ca83b19fb80412c2e6577164ebb393b) = 1 , [WIFI\_MODE\_AP](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba0e26010a13582e90def7366d6d663fe8) = 2 , [WIFI\_MODE\_P2P\_GO](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba777a0cbe012477f334d9b3fa7999d889) = 3 ,     [WIFI\_MODE\_P2P\_GROUP\_FORMATION](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423babaabed89e520fb03599ca941d6742521) = 4 , [WIFI\_MODE\_MESH](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf52eb7740bf223c253ec8754a6defa68) = 5 , **\_\_WIFI\_MODE\_AFTER\_LAST** , [WIFI\_MODE\_MAX](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423ba96245dc44888c3ef2d5488ae18263b11) = \_\_WIFI\_MODE\_AFTER\_LAST - 1 ,     [WIFI\_MODE\_UNKNOWN](group__wifi__mgmt.md#gga584f6239ac14e2bedc5e6bd72756423baf8f224061fb80e065d41caab718efb95)   } |
|  | Wi-Fi interface modes. [More...](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) |
| enum | [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) {     [WIFI\_0](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a530e059ee3ee741248c212287d3798f8) = 0 , [WIFI\_1](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62abe63329d11a9642d6d9dec3120d1f36c) , [WIFI\_2](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aaf818813d87ea19fbe8396aff3f0c1d9) , [WIFI\_3](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62aeca0be00ba42d701b6f148036a18e362) ,     [WIFI\_4](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8e92427770e1ae2a3fe36deff6e6eef2) , [WIFI\_5](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a4c94fcb62c5213c6e1cf46409ef6b824) , [WIFI\_6](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ab9d56217d0abd71f7f824930ea226ffe) , [WIFI\_6E](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a1bbbd42fc347212077fbac6f8be6f6a6) ,     [WIFI\_7](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a8a121ae16410908526a2ce8c0beb9934) , **\_\_WIFI\_LINK\_MODE\_AFTER\_LAST** , [WIFI\_LINK\_MODE\_MAX](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62a46d398614f6787c3fcd71ea71acb52e5) = \_\_WIFI\_LINK\_MODE\_AFTER\_LAST - 1 , [WIFI\_LINK\_MODE\_UNKNOWN](group__wifi__mgmt.md#ggabdb2a784d4727b71ab44cca04e422c62ac1c8bdda14fc2ca9292421648938aeba)   } |
|  | Wi-Fi link operating modes. [More...](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) |
| enum | [wifi\_scan\_type](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) { [WIFI\_SCAN\_TYPE\_ACTIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaa7cb9f32d9cbed0c055394eb3ce0c67d9) = 0 , [WIFI\_SCAN\_TYPE\_PASSIVE](group__wifi__mgmt.md#ggad30e29eda65ccafdbd7f11865937b8eaab286c65b4c0e4405b37db8fd7f72808f) } |
|  | Wi-Fi scanning types. [More...](group__wifi__mgmt.md#gad30e29eda65ccafdbd7f11865937b8ea) |
| enum | [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) { [WIFI\_PS\_DISABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa9860ebd60aad1694c2c903e18bbc5e82) = 0 , [WIFI\_PS\_ENABLED](group__wifi__mgmt.md#gga0fffeb57b68fb8cdef9d3d571368b8caa3c1495662d43fb52261c4137096a4c47) } |
|  | Wi-Fi power save states. [More...](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) |
| enum | [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) { [WIFI\_PS\_MODE\_LEGACY](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca761cfe837bd3b531d1e58298b5b1c5fd) = 0 , [WIFI\_PS\_MODE\_WMM](group__wifi__mgmt.md#ggaffae7d2a754be5eb952ad2b83edad54ca528fb6047805bd00691b3ae14bd5eae5) } |
|  | Wi-Fi power save modes. [More...](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) |
| enum | [wifi\_operational\_modes](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35) {     [WIFI\_STA\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a340a5486c7da955853acdb005c4781f7) = BIT(0) , [WIFI\_MONITOR\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ad5bc242078274f20949d9afa8c67b696) = BIT(1) , [WIFI\_TX\_INJECTION\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35a2106a5725118f9b9b2a0ce04453adb74) = BIT(2) , [WIFI\_PROMISCUOUS\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aeb9bbb00469b4038f16b8b7cd2c5bf56) = BIT(3) ,     [WIFI\_AP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35aa25a1cb94f2d78baed38752af5d195bd) = BIT(4) , [WIFI\_SOFTAP\_MODE](group__wifi__mgmt.md#gga4a9243eeb974111d6047fd3d8d9cbf35ab2463380f240d8a51ef5b02e648c5623) = BIT(5)   } |
|  | Wifi operational mode. [More...](group__wifi__mgmt.md#ga4a9243eeb974111d6047fd3d8d9cbf35) |
| enum | [wifi\_filter](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f) { [WIFI\_PACKET\_FILTER\_ALL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa4ef04395b41e0578bdeb77b5e7b8612b) = BIT(0) , [WIFI\_PACKET\_FILTER\_MGMT](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fa2829d4e8b62d23d9fa5feb7cd9b2b2fc) = BIT(1) , [WIFI\_PACKET\_FILTER\_DATA](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1faca13230b05c62ece57186d6f01e5e244) = BIT(2) , [WIFI\_PACKET\_FILTER\_CTRL](group__wifi__mgmt.md#ggaa60495242c66a3fac294886856121c1fad55696b27a792f0a4aefbcf4ff0182de) = BIT(3) } |
|  | Mode filter settings. [More...](group__wifi__mgmt.md#gaa60495242c66a3fac294886856121c1f) |
| enum | [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) { [WIFI\_TWT\_SETUP](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a127b1ba136c0a8b226378ce6398c4c45) = 0 , [WIFI\_TWT\_TEARDOWN](group__wifi__mgmt.md#ggad0e998aeb1b27c4f203ca76339d323a3a8b7aef65a36005a1fc29367b9455e41f) } |
|  | Wi-Fi Target Wake Time (TWT) operations. [More...](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) |
| enum | [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) { [WIFI\_TWT\_INDIVIDUAL](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8ad8205ed96091863156066d9df874bee0) = 0 , [WIFI\_TWT\_BROADCAST](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a66d66faf5c949fa414b163eacb3871fa) , [WIFI\_TWT\_WAKE\_TBTT](group__wifi__mgmt.md#gga695123cd534e2499f516a07fdc5cafa8a8eef8349e12980c39e63fd11ce2ab978) } |
|  | Wi-Fi Target Wake Time (TWT) negotiation types. [More...](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) |
| enum | [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) {     [WIFI\_TWT\_SETUP\_CMD\_REQUEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a7b6568e80a31a17a742c23ae0f6892bd) = 0 , [WIFI\_TWT\_SETUP\_CMD\_SUGGEST](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022abdd60c33f3a61b21c9f72bd66897b648) , [WIFI\_TWT\_SETUP\_CMD\_DEMAND](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a4a687e30a23f1705e5b359b7d7b6366e) , [WIFI\_TWT\_SETUP\_CMD\_GROUPING](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a846145fb934c5235a5afea275263c279) ,     [WIFI\_TWT\_SETUP\_CMD\_ACCEPT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022afb7fb9876e2774f45cc7688b0308b64a) , [WIFI\_TWT\_SETUP\_CMD\_ALTERNATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a8247cf7843a5d2a7ddf48da1c5be9ae1) , [WIFI\_TWT\_SETUP\_CMD\_DICTATE](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022a9965a5ee6b30a64d6849690f60d859f3) , [WIFI\_TWT\_SETUP\_CMD\_REJECT](group__wifi__mgmt.md#gga31c78afc89bfdc4b54cee177843f8022aed1c84e6699331726aa75477e9a1f565)   } |
|  | Wi-Fi Target Wake Time (TWT) setup commands. [More...](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) |
| enum | [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) { [WIFI\_TWT\_RESP\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa0ec181caece9e9d5f12827c6c5390286) = 0 , [WIFI\_TWT\_RESP\_NOT\_RECEIVED](group__wifi__mgmt.md#gga4d03aedac13ee4512d7717ac624f319aa757054d1ad2033ebc6b9a0fb1f3b2c72) } |
|  | Wi-Fi Target Wake Time (TWT) negotiation status. [More...](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) |
| enum | [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) {     [WIFI\_TWT\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ad1336b74984f46238b4baf6ea0b7ad13) , [WIFI\_TWT\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7069a257d030d3df36ce944e7bb33556) , [WIFI\_TWT\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a7ee7ac64ab2471620825b949be37da2d) , [WIFI\_TWT\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a8602d648589b0341fb50940a79400fef) ,     [WIFI\_TWT\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6aa17ee943d673d66444568526211f8831) , [WIFI\_TWT\_FAIL\_PEER\_NOT\_HE\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a86c8021210168b64b2b967e6e5611860) , [WIFI\_TWT\_FAIL\_PEER\_NOT\_TWT\_CAPAB](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac712d17d6babb65323af23311c4f81ce) , [WIFI\_TWT\_FAIL\_OPERATION\_IN\_PROGRESS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6ac3aed05ad40e7e489a3c2b53c01a05c7) ,     [WIFI\_TWT\_FAIL\_INVALID\_FLOW\_ID](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a490d146c72579b610ee02424dc01bcb6) , [WIFI\_TWT\_FAIL\_IP\_NOT\_ASSIGNED](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6a0783df9338c2f1a55fc5cd31f9a257ee) , [WIFI\_TWT\_FAIL\_FLOW\_ALREADY\_EXISTS](group__wifi__mgmt.md#gga97fa304f9a1db2294a93cccd4c93bcf6afc608d761adc76392854eefd4561dc5c)   } |
|  | Target Wake Time (TWT) error codes. [More...](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) |
| enum | [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) { [WIFI\_TWT\_TEARDOWN\_SUCCESS](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a17a0d82cff424ff5bdf462b6db63f965) = 0 , [WIFI\_TWT\_TEARDOWN\_FAILED](group__wifi__mgmt.md#ggad3709d07aaa3ed59b48f9dd7bd181989a53b36533aa40cb076be68cd1c902582d) } |
|  | Wi-Fi Target Wake Time (TWT) teradown status. [More...](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) |
| enum | [wifi\_ps\_param\_type](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) {     [WIFI\_PS\_PARAM\_STATE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a4f676a7085b7b0a37e717980412a379d) , [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a1999ab313a62a9208d683fb1d3e01c90) , [WIFI\_PS\_PARAM\_WAKEUP\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912a93ce25e041d81fdaa6c3c77f526a8db8) , [WIFI\_PS\_PARAM\_MODE](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912ac65551112d0fdc28ec3805d2f70ddaab) ,     [WIFI\_PS\_PARAM\_TIMEOUT](group__wifi__mgmt.md#ggabe45d132797047c098041331c8f6f912aefc0c3c93b09f30270f8e7914e9c9c29)   } |
|  | Wi-Fi power save parameters. [More...](group__wifi__mgmt.md#gabe45d132797047c098041331c8f6f912) |
| enum | [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) { [WIFI\_PS\_WAKEUP\_MODE\_DTIM](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7fad7232d95f68a6ce41cdaedc58444bba6) = 0 , [WIFI\_PS\_WAKEUP\_MODE\_LISTEN\_INTERVAL](group__wifi__mgmt.md#ggac7f907644847e905d67c709fa4afae7facbd61628e83216011745cb225e0c8b30) } |
|  | Wi-Fi power save modes. [More...](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) |
| enum | [wifi\_config\_ps\_param\_fail\_reason](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) {     [WIFI\_PS\_PARAM\_FAIL\_UNSPECIFIED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3bed30a7c9b20bcad82214b7e47edd38) , [WIFI\_PS\_PARAM\_FAIL\_CMD\_EXEC\_FAIL](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a72bd1e14e5f5a7e154d609ecb27f9394) , [WIFI\_PS\_PARAM\_FAIL\_OPERATION\_NOT\_SUPPORTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af764fa8f4030bdff396fd7142d8c0093) , [WIFI\_PS\_PARAM\_FAIL\_UNABLE\_TO\_GET\_IFACE\_STATUS](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0a3ad0f43ac7afa204e7dd66838a8618b3) ,     [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_NOT\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abdc89ebeae1d558d83cfa85e236a083a) , [WIFI\_PS\_PARAM\_FAIL\_DEVICE\_CONNECTED](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0af93e9a85a784937562d85683bb433486) , [WIFI\_PS\_PARAM\_LISTEN\_INTERVAL\_RANGE\_INVALID](group__wifi__mgmt.md#ggad98099584d2222ede93aba42b1fbaff0abec8aa7ba9d334a23f4286d220eabe1f)   } |
|  | Wi-Fi power save error codes. [More...](group__wifi__mgmt.md#gad98099584d2222ede93aba42b1fbaff0) |

| Functions | |
| --- | --- |
| const char \* | [wifi\_security\_txt](group__wifi__mgmt.md#ga9bb9f658d7806e42b3ee351fb3e7dfa0) (enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) security) |
|  | Helper function to get user-friendly security type name. |
| const char \* | [wifi\_mfp\_txt](group__wifi__mgmt.md#ga22354241197a9227fdba77e67d471f5c) (enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) mfp) |
|  | Helper function to get user-friendly MFP name. |
| const char \* | [wifi\_band\_txt](group__wifi__mgmt.md#ga44f875bf0d931b66d582f5dca2d65ed5) (enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) band) |
|  | Helper function to get user-friendly frequency band name. |
| const char \* | [wifi\_state\_txt](group__wifi__mgmt.md#ga03d306912dc96178e21d3c82c104582f) (enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Helper function to get user-friendly interface state name. |
| const char \* | [wifi\_mode\_txt](group__wifi__mgmt.md#gad78536ce1f30accfa45f258b6bf8c73d) (enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) mode) |
|  | Helper function to get user-friendly interface mode name. |
| const char \* | [wifi\_link\_mode\_txt](group__wifi__mgmt.md#ga0d9d6e2150fb187025300904357f7b4d) (enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) link\_mode) |
|  | Helper function to get user-friendly link mode name. |
| const char \* | [wifi\_ps\_txt](group__wifi__mgmt.md#gafbeb5f7fa97fd2ba0c691da0f8853ef2) (enum [wifi\_ps](group__wifi__mgmt.md#ga0fffeb57b68fb8cdef9d3d571368b8ca) ps\_name) |
|  | Helper function to get user-friendly ps name. |
| const char \* | [wifi\_ps\_mode\_txt](group__wifi__mgmt.md#gadb21d49f64e04fba59433e51d5b3481c) (enum [wifi\_ps\_mode](group__wifi__mgmt.md#gaffae7d2a754be5eb952ad2b83edad54c) ps\_mode) |
|  | Helper function to get user-friendly ps mode name. |
| const char \* | [wifi\_twt\_operation\_txt](group__wifi__mgmt.md#gadb125925e851bf7569424cd4295e7712) (enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) twt\_operation) |
|  | Helper function to get user-friendly twt operation name. |
| const char \* | [wifi\_twt\_negotiation\_type\_txt](group__wifi__mgmt.md#ga6a74e999d63ee491df68447219ef2a0d) (enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) twt\_negotiation) |
|  | Helper function to get user-friendly twt negotiation type name. |
| const char \* | [wifi\_twt\_setup\_cmd\_txt](group__wifi__mgmt.md#gae3ca047cc6ef6b6a2e44ba6574d41a44) (enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) twt\_setup) |
|  | Helper function to get user-friendly twt setup cmd name. |
| static const char \* | [wifi\_twt\_get\_err\_code\_str](group__wifi__mgmt.md#gab2e6a6e1d8358a8f34d67bd632709b3d) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no) |
|  | Helper function to get user-friendly TWT error code name. |
| const char \* | [wifi\_ps\_wakeup\_mode\_txt](group__wifi__mgmt.md#ga6fd645f891234136b3028574a0af9666) (enum [wifi\_ps\_wakeup\_mode](group__wifi__mgmt.md#gac7f907644847e905d67c709fa4afae7f) ps\_wakeup\_mode) |
|  | Helper function to get user-friendly ps wakeup mode name. |
| static const char \* | [wifi\_ps\_get\_config\_err\_code\_str](group__wifi__mgmt.md#ga8b72e7989964963a25f42ed1dba240a0) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) err\_no) |
|  | Helper function to get user-friendly power save error code name. |

## Detailed Description

IEEE 802.11 protocol and general Wi-Fi definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi.h](wifi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
