---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structenum__mgmt__detail__output.html
original_path: doxygen/html/structenum__mgmt__detail__output.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

enum\_mgmt\_detail\_output Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr enum\_mgmt callback API](group__mcumgr__callback__api__enum__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf "Callback when fetching details on supported command groups.") notification callback: This callback function is called once per command group when the detail command is used, it can be used to return additional information/fields in the response.
[More...](#details)

`#include <[enum_mgmt_callbacks.h](enum__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [mgmt\_group](structmgmt__group.md) \* | [group](#a787c1a41fbe135b85176d3b0bb6ccd92) |
|  | The group that is currently being enumerated. |
| zcbor\_state\_t \* | [zse](#a140d1f5cd4e4f7a88c5a1da98a927161) |
|  | The zcbor encoder which is currently being used to output group information, additional fields to the group can be added using this. |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf "Callback when fetching details on supported command groups.") notification callback: This callback function is called once per command group when the detail command is used, it can be used to return additional information/fields in the response.

## Field Documentation

## [◆ ](#a787c1a41fbe135b85176d3b0bb6ccd92)group

| const struct [mgmt\_group](structmgmt__group.md)\* enum\_mgmt\_detail\_output::group |
| --- |

The group that is currently being enumerated.

## [◆ ](#a140d1f5cd4e4f7a88c5a1da98a927161)zse

| zcbor\_state\_t\* enum\_mgmt\_detail\_output::zse |
| --- |

The zcbor encoder which is currently being used to output group information, additional fields to the group can be added using this.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/enum\_mgmt/[enum\_mgmt\_callbacks.h](enum__mgmt__callbacks_8h_source.md)

- [enum\_mgmt\_detail\_output](structenum__mgmt__detail__output.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
