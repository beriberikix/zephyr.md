---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/callbacks_8h.html
original_path: doxygen/html/callbacks_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

callbacks.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/mgmt/mgmt.h](mgmt_8h_source.md)>`

[Go to the source code of this file.](callbacks_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mgmt\_callback](structmgmt__callback.md) |
|  | MGMT callback struct. [More...](structmgmt__callback.md#details) |
| struct | [mgmt\_evt\_op\_cmd\_arg](structmgmt__evt__op__cmd__arg.md) |
|  | Arguments for [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28 "Callback when a command is received, data is mgmt_evt_op_cmd_arg()."), [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770 "Callback when a status is updated, data is mgmt_evt_op_cmd_arg().") and [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12 "Callback when a command has been processed, data is mgmt_evt_op_cmd_arg()."). [More...](structmgmt__evt__op__cmd__arg.md#details) |

| Macros | |
| --- | --- |
| #define | [MGMT\_EVT\_GET\_GROUP](group__mcumgr__callback__api.md#gaa3290bd9a21f9718adac92bfe313161f)(event) |
|  | Get group from event. |
| #define | [MGMT\_EVT\_GET\_ID](group__mcumgr__callback__api.md#ga4c6ff3fb3b14a31e65248cec9840b1dd)(event) |
|  | Get event ID from event. |
| #define | [MGMT\_CB\_ERROR\_RET](group__mcumgr__callback__api.md#ga6b1f9ca0cf3e296f93c2fc497911dd15)   \_\_DEPRECATED\_MACRO [MGMT\_CB\_ERROR\_ERR](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) |

| Typedefs | |
| --- | --- |
| typedef enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c)(\* | [mgmt\_cb](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) prev\_status, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[group](structgroup.md), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*abort\_more, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size) |
|  | Function to be called on MGMT notification/event. |

| Enumerations | |
| --- | --- |
| enum | [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) { [MGMT\_CB\_OK](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da) , [MGMT\_CB\_ERROR\_RC](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) , [MGMT\_CB\_ERROR\_ERR](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) } |
|  | MGMT event callback return value. [More...](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) |
| enum | [mgmt\_cb\_groups](group__mcumgr__callback__api.md#ga40ecf8933112abe76d7fedb3dcc7cdbe) {     [MGMT\_EVT\_GRP\_ALL](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a) = 0 , [MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c) , [MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae) , [MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1) ,     [MGMT\_EVT\_GRP\_FS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48) , [MGMT\_EVT\_GRP\_SETTINGS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536) , [MGMT\_EVT\_GRP\_ENUM](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3) , [MGMT\_EVT\_GRP\_USER\_CUSTOM\_START](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d) = MGMT\_GROUP\_ID\_PERUSER   } |
|  | MGMT event callback group IDs. [More...](group__mcumgr__callback__api.md#ga40ecf8933112abe76d7fedb3dcc7cdbe) |
| enum | [smp\_all\_events](group__mcumgr__callback__api.md#gaab6470007be89e5aab88838456f9561a) { [MGMT\_EVT\_OP\_ALL](group__mcumgr__callback__api.md#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_ALL) } |
|  | MGMT event opcodes for all command processing. [More...](group__mcumgr__callback__api.md#gaab6470007be89e5aab88838456f9561a) |
| enum | [smp\_group\_events](group__mcumgr__callback__api.md#ga590788274b4508c6203685d9e9252184) { [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SMP, 0) , [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SMP, 1) , [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SMP, 2) , [MGMT\_EVT\_OP\_CMD\_ALL](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_SMP) } |
|  | MGMT event opcodes for base SMP command processing. [More...](group__mcumgr__callback__api.md#ga590788274b4508c6203685d9e9252184) |
| enum | [fs\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga324223c20cbefe3400272e2789082c79) { [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_FS, 0) , [MGMT\_EVT\_OP\_FS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_FS) } |
|  | MGMT event opcodes for filesystem management group. [More...](group__mcumgr__callback__api.md#ga324223c20cbefe3400272e2789082c79) |
| enum | [img\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga3fa2c42bade08cca1122e32f6315f107) {     [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 0) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 1) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 2) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 3) ,     [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 4) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 5) , [MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 6) , [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 7) ,     [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 8) , [MGMT\_EVT\_OP\_IMG\_MGMT\_ALL](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_IMG)   } |
|  | MGMT event opcodes for image management group. [More...](group__mcumgr__callback__api.md#ga3fa2c42bade08cca1122e32f6315f107) |
| enum | [os\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga261346c700a2522542d8282ca76f88a5) {     [MGMT\_EVT\_OP\_OS\_MGMT\_RESET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 0) , [MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 1) , [MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 2) , [MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 3) ,     [MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 4) , [MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 5) , [MGMT\_EVT\_OP\_OS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_OS)   } |
|  | MGMT event opcodes for operating system management group. [More...](group__mcumgr__callback__api.md#ga261346c700a2522542d8282ca76f88a5) |
| enum | [settings\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga1711bc9f45a8114a6b0c89db4a40e3de) { [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SETTINGS, 0) , [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_SETTINGS) } |
|  | MGMT event opcodes for settings management group. [More...](group__mcumgr__callback__api.md#ga1711bc9f45a8114a6b0c89db4a40e3de) |
| enum | [enum\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga7ddc4c031948a2fee56fcbdb7d675a1d) { [MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_ENUM, 0) , [MGMT\_EVT\_OP\_ENUM\_MGMT\_ALL](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_ENUM) } |
|  | MGMT event opcodes for enumeration management group. [More...](group__mcumgr__callback__api.md#ga7ddc4c031948a2fee56fcbdb7d675a1d) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mgmt\_evt\_get\_index](group__mcumgr__callback__api.md#gab309008a29ddcde95654ad812463d3bc) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
|  | Get event ID index from event. |
| enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) | [mgmt\_callback\_notify](group__mcumgr__callback__api.md#gaf9308502f8137f7fb80667941cdd46ca) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*err\_rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*err\_group) |
|  | This function is called to notify registered callbacks about mcumgr notifications/events. |
| void | [mgmt\_callback\_register](group__mcumgr__callback__api.md#gaaf698627904995930784c96fb48a1d7b) (struct [mgmt\_callback](structmgmt__callback.md) \*callback) |
|  | Register event callback function. |
| void | [mgmt\_callback\_unregister](group__mcumgr__callback__api.md#ga24d97d6d17c5586a45abacb59d906bd2) (struct [mgmt\_callback](structmgmt__callback.md) \*callback) |
|  | Unregister event callback function. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [callbacks.h](callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
