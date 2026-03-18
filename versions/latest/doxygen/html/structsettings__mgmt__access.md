---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsettings__mgmt__access.html
original_path: doxygen/html/structsettings__mgmt__access.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_mgmt\_access Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr settings\_mgmt callback API](group__mcumgr__callback__api__settings__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0 "Callback when a setting is read/written/deleted.") notification callback: This callback function is used to notify the application about a pending setting read/write/delete/load/save/commit request and to authorise or deny it.
[More...](#details)

`#include <[settings_mgmt_callbacks.h](settings__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [settings\_mgmt\_access\_types](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47) | [access](#a9b798a118844083d77af6db53df5eb37) |
|  | Type of access. |
| char \* | [name](#ae0f02e70ee2da823801d4d475f4a2e76) |
|  | Key name for accesses (only set for SETTINGS\_ACCESS\_READ, SETTINGS\_ACCESS\_WRITE and SETTINGS\_ACCESS\_DELETE). |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [val](#aeb23615be870929a987c6cfbd3f445de) |
|  | Data provided by the user (only set for SETTINGS\_ACCESS\_WRITE). |
| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | [val\_length](#ab13bdcd8763dca5a99d3d52270f9b4d2) |
|  | Length of data provided by the user (only set for SETTINGS\_ACCESS\_WRITE). |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0 "Callback when a setting is read/written/deleted.") notification callback: This callback function is used to notify the application about a pending setting read/write/delete/load/save/commit request and to authorise or deny it.

Access will be allowed so long as no handlers return an error, if one returns an error then access will be denied.

## Field Documentation

## [◆ ](#a9b798a118844083d77af6db53df5eb37)access

| enum [settings\_mgmt\_access\_types](group__mcumgr__callback__api__settings__mgmt.md#ga40c179f978718409c7db43448efc8f47) settings\_mgmt\_access::access |
| --- |

Type of access.

## [◆ ](#ae0f02e70ee2da823801d4d475f4a2e76)name

| char\* settings\_mgmt\_access::name |
| --- |

Key name for accesses (only set for SETTINGS\_ACCESS\_READ, SETTINGS\_ACCESS\_WRITE and SETTINGS\_ACCESS\_DELETE).

Note that this can be changed by handlers to redirect settings access if needed (as long as it does not exceed the maximum setting string size) if CONFIG\_MCUMGR\_GRP\_SETTINGS\_BUFFER\_TYPE\_STACK is selected, of maximum size CONFIG\_MCUMGR\_GRP\_SETTINGS\_NAME\_LEN.

Note: This string *must* be NULL terminated.

## [◆ ](#aeb23615be870929a987c6cfbd3f445de)val

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* settings\_mgmt\_access::val |
| --- |

Data provided by the user (only set for SETTINGS\_ACCESS\_WRITE).

## [◆ ](#ab13bdcd8763dca5a99d3d52270f9b4d2)val\_length

| const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)\* settings\_mgmt\_access::val\_length |
| --- |

Length of data provided by the user (only set for SETTINGS\_ACCESS\_WRITE).

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/settings\_mgmt/[settings\_mgmt\_callbacks.h](settings__mgmt__callbacks_8h_source.md)

- [settings\_mgmt\_access](structsettings__mgmt__access.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
