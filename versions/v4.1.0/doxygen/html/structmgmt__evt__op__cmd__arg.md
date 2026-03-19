---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmgmt__evt__op__cmd__arg.html
original_path: doxygen/html/structmgmt__evt__op__cmd__arg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt\_evt\_op\_cmd\_arg Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md)

Arguments for [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28 "Callback when a command is received, data is mgmt_evt_op_cmd_arg()."), [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770 "Callback when a status is updated, data is mgmt_evt_op_cmd_arg().") and [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12 "Callback when a command has been processed, data is mgmt_evt_op_cmd_arg().").
[More...](#details)

`#include <[callbacks.h](callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [group](#a0607126986dc0a1e9a0dae348d278741) |
|  | [mcumgr\_group\_t](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5 "MCUmgr groups.") |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#ac461e832ea0997ae19be72df4caf0bb7) |
|  | Message ID within group. |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [op](#acbd58ae2efe86685df33e58450753fe1) |  |
|  | [mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd "Opcodes; encoded in first byte of header.") used in [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28 "Callback when a command is received, data is mgmt_evt_op_cmd_arg().") [More...](#acbd58ae2efe86685df33e58450753fe1) |
| int   [err](#a7e7a469f944d27d92e25e42d56fa32d2) |  |
|  | [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes."), used in [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12 "Callback when a command has been processed, data is mgmt_evt_op_cmd_arg().") [More...](#a7e7a469f944d27d92e25e42d56fa32d2) |
| int   [status](#a4d08fca41a60aee6c458d510d528a307) |  |
|  | [img\_mgmt\_id\_upload\_t](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede "IMG_MGMT_ID_UPLOAD statuses."), used in [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770 "Callback when a status is updated, data is mgmt_evt_op_cmd_arg().") [More...](#a4d08fca41a60aee6c458d510d528a307) |
| }; |  |

## Detailed Description

Arguments for [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28 "Callback when a command is received, data is mgmt_evt_op_cmd_arg()."), [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770 "Callback when a status is updated, data is mgmt_evt_op_cmd_arg().") and [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12 "Callback when a command has been processed, data is mgmt_evt_op_cmd_arg().").

## Field Documentation

## [◆ ](#a934015f5837ffb19da82a2d175e68b03)[union]

| union { ... } [mgmt\_evt\_op\_cmd\_arg](structmgmt__evt__op__cmd__arg.md) |
| --- |

## [◆ ](#a7e7a469f944d27d92e25e42d56fa32d2)err

| int mgmt\_evt\_op\_cmd\_arg::err |
| --- |

[mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes."), used in [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12 "Callback when a command has been processed, data is mgmt_evt_op_cmd_arg().")

## [◆ ](#a0607126986dc0a1e9a0dae348d278741)group

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mgmt\_evt\_op\_cmd\_arg::group |
| --- |

[mcumgr\_group\_t](group__mcumgr__mgmt__api.md#ga81f98b9a0c3810f7d607b783f8e259b5 "MCUmgr groups.")

## [◆ ](#ac461e832ea0997ae19be72df4caf0bb7)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mgmt\_evt\_op\_cmd\_arg::id |
| --- |

Message ID within group.

## [◆ ](#acbd58ae2efe86685df33e58450753fe1)op

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mgmt\_evt\_op\_cmd\_arg::op |
| --- |

[mcumgr\_op\_t](group__mcumgr__mgmt__api.md#gae06a618f492f18e856742b4affab80dd "Opcodes; encoded in first byte of header.") used in [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28 "Callback when a command is received, data is mgmt_evt_op_cmd_arg().")

## [◆ ](#a4d08fca41a60aee6c458d510d528a307)status

| int mgmt\_evt\_op\_cmd\_arg::status |
| --- |

[img\_mgmt\_id\_upload\_t](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede "IMG_MGMT_ID_UPLOAD statuses."), used in [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770 "Callback when a status is updated, data is mgmt_evt_op_cmd_arg().")

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/mgmt/[callbacks.h](callbacks_8h_source.md)

- [mgmt\_evt\_op\_cmd\_arg](structmgmt__evt__op__cmd__arg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
