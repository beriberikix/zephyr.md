---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mcumgr__callback__api.html
original_path: doxygen/html/group__mcumgr__callback__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr callback API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr callback API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [MCUmgr fs\_mgmt callback API](group__mcumgr__callback__api__fs__mgmt.md) |
|  | MCUmgr fs\_mgmt callback API. |
|  | [MCUmgr img\_mgmt callback API](group__mcumgr__callback__api__img__mgmt.md) |
|  | MCUmgr img\_mgmt callback API. |
|  | [MCUmgr os\_mgmt callback API](group__mcumgr__callback__api__os__mgmt.md) |
|  | MCUmgr os\_mgmt callback API. |
|  | [MCUmgr settings\_mgmt callback API](group__mcumgr__callback__api__settings__mgmt.md) |
|  | MCUmgr settings\_mgmt callback API. |

| Data Structures | |
| --- | --- |
| struct | [mgmt\_callback](structmgmt__callback.md) |
|  | MGMT callback struct. [More...](structmgmt__callback.md#details) |
| struct | [mgmt\_evt\_op\_cmd\_arg](structmgmt__evt__op__cmd__arg.md) |
|  | Arguments for [MGMT\_EVT\_OP\_CMD\_RECV](#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28), [MGMT\_EVT\_OP\_CMD\_STATUS](#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770) and [MGMT\_EVT\_OP\_CMD\_DONE](#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12). [More...](structmgmt__evt__op__cmd__arg.md#details) |

| Macros | |
| --- | --- |
| #define | [MGMT\_EVT\_GET\_GROUP](#gaa3290bd9a21f9718adac92bfe313161f)(event) |
|  | Get group from event. |
| #define | [MGMT\_EVT\_GET\_ID](#ga4c6ff3fb3b14a31e65248cec9840b1dd)(event) |
|  | Get event ID from event. |
| #define | [MGMT\_CB\_ERROR\_RET](#ga6b1f9ca0cf3e296f93c2fc497911dd15)   \_\_DEPRECATED\_MACRO [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) |

| Typedefs | |
| --- | --- |
| typedef enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c)(\* | [mgmt\_cb](#gae61f705224a859776ee5161dfda5ed7d)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) prev\_status, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*group, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*abort\_more, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size) |
|  | Function to be called on MGMT notification/event. |

| Enumerations | |
| --- | --- |
| enum | [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) { [MGMT\_CB\_OK](#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da) , [MGMT\_CB\_ERROR\_RC](#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) , [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) } |
|  | MGMT event callback return value. [More...](#ga1ba636c0efb7a91630ed9743e6fd4d6c) |
| enum | [mgmt\_cb\_groups](#ga40ecf8933112abe76d7fedb3dcc7cdbe) {     [MGMT\_EVT\_GRP\_ALL](#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a) = 0 , [MGMT\_EVT\_GRP\_SMP](#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c) , [MGMT\_EVT\_GRP\_OS](#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae) , [MGMT\_EVT\_GRP\_IMG](#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1) ,     [MGMT\_EVT\_GRP\_FS](#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48) , [MGMT\_EVT\_GRP\_SETTINGS](#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536) , [MGMT\_EVT\_GRP\_USER\_CUSTOM\_START](#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d) = MGMT\_GROUP\_ID\_PERUSER   } |
|  | MGMT event callback group IDs. [More...](#ga40ecf8933112abe76d7fedb3dcc7cdbe) |
| enum | [smp\_all\_events](#gaab6470007be89e5aab88838456f9561a) { [MGMT\_EVT\_OP\_ALL](#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_ALL) } |
|  | MGMT event opcodes for all command processing. [More...](#gaab6470007be89e5aab88838456f9561a) |
| enum | [smp\_group\_events](#ga590788274b4508c6203685d9e9252184) { [MGMT\_EVT\_OP\_CMD\_RECV](#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SMP, 0) , [MGMT\_EVT\_OP\_CMD\_STATUS](#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SMP, 1) , [MGMT\_EVT\_OP\_CMD\_DONE](#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SMP, 2) , [MGMT\_EVT\_OP\_CMD\_ALL](#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_SMP) } |
|  | MGMT event opcodes for base SMP command processing. [More...](#ga590788274b4508c6203685d9e9252184) |
| enum | [fs\_mgmt\_group\_events](#ga324223c20cbefe3400272e2789082c79) { [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_FS, 0) , [MGMT\_EVT\_OP\_FS\_MGMT\_ALL](#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_FS) } |
|  | MGMT event opcodes for filesystem management group. [More...](#ga324223c20cbefe3400272e2789082c79) |
| enum | [img\_mgmt\_group\_events](#ga3fa2c42bade08cca1122e32f6315f107) {     [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 0) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED](#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 1) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED](#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 2) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING](#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 3) ,     [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 4) , [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE](#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_IMG, 5) , [MGMT\_EVT\_OP\_IMG\_MGMT\_ALL](#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_IMG)   } |
|  | MGMT event opcodes for image management group. [More...](#ga3fa2c42bade08cca1122e32f6315f107) |
| enum | [os\_mgmt\_group\_events](#ga261346c700a2522542d8282ca76f88a5) {     [MGMT\_EVT\_OP\_OS\_MGMT\_RESET](#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 0) , [MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK](#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 1) , [MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND](#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 2) , [MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET](#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 3) ,     [MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET](#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_OS, 4) , [MGMT\_EVT\_OP\_OS\_MGMT\_ALL](#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_OS)   } |
|  | MGMT event opcodes for operating system management group. [More...](#ga261346c700a2522542d8282ca76f88a5) |
| enum | [settings\_mgmt\_group\_events](#ga1711bc9f45a8114a6b0c89db4a40e3de) { [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0) = MGMT\_DEF\_EVT\_OP\_ID(MGMT\_EVT\_GRP\_SETTINGS, 0) , [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL](#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2) = MGMT\_DEF\_EVT\_OP\_ALL(MGMT\_EVT\_GRP\_SETTINGS) } |
|  | MGMT event opcodes for settings management group. [More...](#ga1711bc9f45a8114a6b0c89db4a40e3de) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mgmt\_evt\_get\_index](#gab309008a29ddcde95654ad812463d3bc) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
|  | Get event ID index from event. |
| enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) | [mgmt\_callback\_notify](#gaf9308502f8137f7fb80667941cdd46ca) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*err\_rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*err\_group) |
|  | This function is called to notify registered callbacks about mcumgr notifications/events. |
| void | [mgmt\_callback\_register](#gaaf698627904995930784c96fb48a1d7b) (struct [mgmt\_callback](structmgmt__callback.md) \*callback) |
|  | Register event callback function. |
| void | [mgmt\_callback\_unregister](#ga24d97d6d17c5586a45abacb59d906bd2) (struct [mgmt\_callback](structmgmt__callback.md) \*callback) |
|  | Unregister event callback function. |

## Detailed Description

MCUmgr callback API.

## Macro Definition Documentation

## [◆ ](#ga6b1f9ca0cf3e296f93c2fc497911dd15)MGMT\_CB\_ERROR\_RET

| #define MGMT\_CB\_ERROR\_RET   \_\_DEPRECATED\_MACRO [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

## [◆ ](#gaa3290bd9a21f9718adac92bfe313161f)MGMT\_EVT\_GET\_GROUP

| #define MGMT\_EVT\_GET\_GROUP | ( |  | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[callbacks.h](callbacks_8h.md)>`

**Value:**

((event >> 16) & MGMT\_EVT\_OP\_ID\_ALL)

Get group from event.

## [◆ ](#ga4c6ff3fb3b14a31e65248cec9840b1dd)MGMT\_EVT\_GET\_ID

| #define MGMT\_EVT\_GET\_ID | ( |  | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[callbacks.h](callbacks_8h.md)>`

**Value:**

(event & MGMT\_EVT\_OP\_ID\_ALL)

Get event ID from event.

## Typedef Documentation

## [◆ ](#gae61f705224a859776ee5161dfda5ed7d)mgmt\_cb

| typedef enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c)(\* mgmt\_cb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) prev\_status, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*group, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*abort\_more, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

Function to be called on MGMT notification/event.

This callback function is used to notify an application or system about a MCUmgr mgmt event.

Parameters
:   | event | [mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd "Opcodes; encoded in first byte of header."). |
    | --- | --- |
    | prev\_status | [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) of the previous handler calls, if it is an error then it will be the first error that was returned by a handler (i.e. this handler is being called for a notification only, the return code will be ignored). |
    | rc | If prev\_status is [MGMT\_CB\_ERROR\_RC](#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) then this is the SMP error that was returned by the first handler that failed. If prev\_status is [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) then this will be the group error rc code returned by the first handler that failed. If the handler wishes to raise an SMP error, this must be set to the [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes.") status and [MGMT\_CB\_ERROR\_RC](#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) must be returned by the function, if the handler wishes to raise a ret error, this must be set to the group ret status and [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) must be returned by the function. |
    | group | If prev\_status is [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) then this is the group of the ret error that was returned by the first handler that failed. If the handler wishes to raise a ret error, this must be set to the group ret status and [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) must be returned by the function. |
    | abort\_more | Set to true to abort further processing by additional handlers. |
    | data | Optional event argument. |
    | data\_size | Size of optional event argument (0 if no data is provided). |

Returns
:   [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) indicating the status to return to the calling code (only checked when this is the first failure reported by a handler).

## Enumeration Type Documentation

## [◆ ](#ga324223c20cbefe3400272e2789082c79)fs\_mgmt\_group\_events

| enum [fs\_mgmt\_group\_events](#ga324223c20cbefe3400272e2789082c79) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event opcodes for filesystem management group.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS | Callback when a file has been accessed, data is [fs\_mgmt\_file\_access()](structfs__mgmt__file__access.md "Structure provided in the MGMT_EVT_OP_FS_MGMT_FILE_ACCESS notification callback: This callback functi..."). |
| MGMT\_EVT\_OP\_FS\_MGMT\_ALL | Used to enable all fs\_mgmt\_group events. |

## [◆ ](#ga3fa2c42bade08cca1122e32f6315f107)img\_mgmt\_group\_events

| enum [img\_mgmt\_group\_events](#ga3fa2c42bade08cca1122e32f6315f107) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event opcodes for image management group.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK | Callback when a client sends a file upload chunk, data is [img\_mgmt\_upload\_check()](structimg__mgmt__upload__check.md "Structure provided in the MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK notification callback: This callback functio..."). |
| MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED | Callback when a DFU operation is stopped. |
| MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED | Callback when a DFU operation is started. |
| MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING | Callback when a DFU operation has finished being transferred. |
| MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED | Callback when an image has been confirmed. |
| MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE | Callback when an image write command has finished writing to flash. |
| MGMT\_EVT\_OP\_IMG\_MGMT\_ALL | Used to enable all img\_mgmt\_group events. |

## [◆ ](#ga40ecf8933112abe76d7fedb3dcc7cdbe)mgmt\_cb\_groups

| enum [mgmt\_cb\_groups](#ga40ecf8933112abe76d7fedb3dcc7cdbe) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event callback group IDs.

Note that this is not a 1:1 mapping with [mcumgr\_group\_t](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5 "MCUmgr groups.") values.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_GRP\_ALL |  |
| MGMT\_EVT\_GRP\_SMP |  |
| MGMT\_EVT\_GRP\_OS |  |
| MGMT\_EVT\_GRP\_IMG |  |
| MGMT\_EVT\_GRP\_FS |  |
| MGMT\_EVT\_GRP\_SETTINGS |  |
| MGMT\_EVT\_GRP\_USER\_CUSTOM\_START |  |

## [◆ ](#ga1ba636c0efb7a91630ed9743e6fd4d6c)mgmt\_cb\_return

| enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event callback return value.

| Enumerator | |
| --- | --- |
| MGMT\_CB\_OK | No error. |
| MGMT\_CB\_ERROR\_RC | SMP protocol error and err\_rc contains the [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes.") error code. |
| MGMT\_CB\_ERROR\_ERR | Group (application-level) error and err\_group contains the group ID that caused the error and err\_rc contains the error code of that group to return. |

## [◆ ](#ga261346c700a2522542d8282ca76f88a5)os\_mgmt\_group\_events

| enum [os\_mgmt\_group\_events](#ga261346c700a2522542d8282ca76f88a5) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event opcodes for operating system management group.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_OP\_OS\_MGMT\_RESET | Callback when a reset command has been received, data is [os\_mgmt\_reset\_data](structos__mgmt__reset__data.md "Structure provided in the MGMT_EVT_OP_OS_MGMT_RESET notification callback: This callback function is ..."). |
| MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK | Callback when an info command is processed, data is [os\_mgmt\_info\_check](structos__mgmt__info__check.md). |
| MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND | Callback when an info command needs to output data, data is [os\_mgmt\_info\_append](structos__mgmt__info__append.md). |
| MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET | Callback when a datetime get command has been received. |
| MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET | Callback when a datetime set command has been received, data is struct [rtc\_time()](structrtc__time.md "Structure for storing date and time values with sub-second precision."). |
| MGMT\_EVT\_OP\_OS\_MGMT\_ALL | Used to enable all os\_mgmt\_group events. |

## [◆ ](#ga1711bc9f45a8114a6b0c89db4a40e3de)settings\_mgmt\_group\_events

| enum [settings\_mgmt\_group\_events](#ga1711bc9f45a8114a6b0c89db4a40e3de) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event opcodes for settings management group.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS | Callback when a setting is read/written/deleted. |
| MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL | Used to enable all settings\_mgmt\_group events. |

## [◆ ](#gaab6470007be89e5aab88838456f9561a)smp\_all\_events

| enum [smp\_all\_events](#gaab6470007be89e5aab88838456f9561a) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event opcodes for all command processing.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_OP\_ALL | Used to enable all events. |

## [◆ ](#ga590788274b4508c6203685d9e9252184)smp\_group\_events

| enum [smp\_group\_events](#ga590788274b4508c6203685d9e9252184) |
| --- |

`#include <[callbacks.h](callbacks_8h.md)>`

MGMT event opcodes for base SMP command processing.

| Enumerator | |
| --- | --- |
| MGMT\_EVT\_OP\_CMD\_RECV | Callback when a command is received, data is [mgmt\_evt\_op\_cmd\_arg()](structmgmt__evt__op__cmd__arg.md "Arguments for MGMT_EVT_OP_CMD_RECV, MGMT_EVT_OP_CMD_STATUS and MGMT_EVT_OP_CMD_DONE."). |
| MGMT\_EVT\_OP\_CMD\_STATUS | Callback when a status is updated, data is [mgmt\_evt\_op\_cmd\_arg()](structmgmt__evt__op__cmd__arg.md "Arguments for MGMT_EVT_OP_CMD_RECV, MGMT_EVT_OP_CMD_STATUS and MGMT_EVT_OP_CMD_DONE."). |
| MGMT\_EVT\_OP\_CMD\_DONE | Callback when a command has been processed, data is [mgmt\_evt\_op\_cmd\_arg()](structmgmt__evt__op__cmd__arg.md "Arguments for MGMT_EVT_OP_CMD_RECV, MGMT_EVT_OP_CMD_STATUS and MGMT_EVT_OP_CMD_DONE."). |
| MGMT\_EVT\_OP\_CMD\_ALL | Used to enable all smp\_group events. |

## Function Documentation

## [◆ ](#gaf9308502f8137f7fb80667941cdd46ca)mgmt\_callback\_notify()

| enum [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) mgmt\_callback\_notify | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_size*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *err\_rc*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *err\_group* ) |

`#include <[callbacks.h](callbacks_8h.md)>`

This function is called to notify registered callbacks about mcumgr notifications/events.

Parameters
:   | event | [mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd "Opcodes; encoded in first byte of header."). |
    | --- | --- |
    | data | Optional event argument. |
    | data\_size | Size of optional event argument (0 if none). |
    | err\_rc | Pointer to rc value. |
    | err\_group | Pointer to group value. |

Returns
:   [mgmt\_cb\_return](#ga1ba636c0efb7a91630ed9743e6fd4d6c) either [MGMT\_CB\_OK](#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da) if all handlers returned it, or [MGMT\_CB\_ERROR\_RC](#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) if the first failed handler returned an SMP error (in which case err\_rc will be updated with the SMP error) or [MGMT\_CB\_ERROR\_ERR](#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) if the first failed handler returned a ret group and error (in which case err\_group will be updated with the failed group ID and err\_rc will be updated with the group-specific error code).

## [◆ ](#gaaf698627904995930784c96fb48a1d7b)mgmt\_callback\_register()

| void mgmt\_callback\_register | ( | struct [mgmt\_callback](structmgmt__callback.md) \* | *callback* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[callbacks.h](callbacks_8h.md)>`

Register event callback function.

Parameters
:   | callback | Callback struct. |
    | --- | --- |

## [◆ ](#ga24d97d6d17c5586a45abacb59d906bd2)mgmt\_callback\_unregister()

| void mgmt\_callback\_unregister | ( | struct [mgmt\_callback](structmgmt__callback.md) \* | *callback* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[callbacks.h](callbacks_8h.md)>`

Unregister event callback function.

Parameters
:   | callback | Callback struct. |
    | --- | --- |

## [◆ ](#gab309008a29ddcde95654ad812463d3bc)mgmt\_evt\_get\_index()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mgmt\_evt\_get\_index | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[callbacks.h](callbacks_8h.md)>`

Get event ID index from event.

Parameters
:   | event | Event to get ID index from. |
    | --- | --- |

Returns
:   Event index.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
