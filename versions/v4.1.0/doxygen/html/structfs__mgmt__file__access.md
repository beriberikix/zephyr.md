---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfs__mgmt__file__access.html
original_path: doxygen/html/structfs__mgmt__file__access.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt\_file\_access Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr callback API](group__mcumgr__callback__api.md) » [MCUmgr fs\_mgmt callback API](group__mcumgr__callback__api__fs__mgmt.md)

Structure provided in the [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3 "Callback when a file has been accessed, data is fs_mgmt_file_access().") notification callback: This callback function is used to notify the application about a pending file read/write request and to authorise or deny it.
[More...](#details)

`#include <[fs_mgmt_callbacks.h](fs__mgmt__callbacks_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [fs\_mgmt\_file\_access\_types](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9) | [access](#a3aeeaf6d4243c1aaa7d6129a2ef4a064) |
|  | Specifies the type of the operation that is being requested. |
| char \* | [filename](#a0155b69d23f3c5044e317eb236ff173c) |
|  | Path and filename of file be accesses, note that this can be changed by handlers to redirect file access if needed (as long as it does not exceed the maximum path string size). |

## Detailed Description

Structure provided in the [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3 "Callback when a file has been accessed, data is fs_mgmt_file_access().") notification callback: This callback function is used to notify the application about a pending file read/write request and to authorise or deny it.

Access will be allowed so long as all notification handlers return [MGMT\_ERR\_EOK](group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f "No error (success)."), if one returns an error then access will be denied.

## Field Documentation

## [◆ ](#a3aeeaf6d4243c1aaa7d6129a2ef4a064)access

| enum [fs\_mgmt\_file\_access\_types](group__mcumgr__callback__api__fs__mgmt.md#ga80e18873c1f4d97ea601a33042bc21f9) fs\_mgmt\_file\_access::access |
| --- |

Specifies the type of the operation that is being requested.

## [◆ ](#a0155b69d23f3c5044e317eb236ff173c)filename

| char\* fs\_mgmt\_file\_access::filename |
| --- |

Path and filename of file be accesses, note that this can be changed by handlers to redirect file access if needed (as long as it does not exceed the maximum path string size).

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/fs\_mgmt/[fs\_mgmt\_callbacks.h](fs__mgmt__callbacks_8h_source.md)

- [fs\_mgmt\_file\_access](structfs__mgmt__file__access.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
