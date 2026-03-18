---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structwifi__nm__instance.html
original_path: doxygen/html/structwifi__nm__instance.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_nm\_instance Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Network Manager API](group__wifi__nm.md)

WiFi Network manager instance.
[More...](#details)

`#include <[wifi_nm.h](wifi__nm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a9789018a431b6c78bbbbed1bbaf634af) |
|  | Name of the Network manager instance. |
| const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md) \* | [ops](#a65e73ea84dfd64dc17f0af03477362ae) |
|  | Wi-Fi Management operations. |
| struct [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md) | [mgd\_ifaces](#a02184a7739d4b9a31b6142df3e0463c0) [CONFIG\_WIFI\_NM\_MAX\_MANAGED\_INTERFACES] |
|  | List of Managed interfaces. |

## Detailed Description

WiFi Network manager instance.

## Field Documentation

## [◆ ](#a02184a7739d4b9a31b6142df3e0463c0)mgd\_ifaces

| struct [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md) wifi\_nm\_instance::mgd\_ifaces[CONFIG\_WIFI\_NM\_MAX\_MANAGED\_INTERFACES] |
| --- |

List of Managed interfaces.

## [◆ ](#a9789018a431b6c78bbbbed1bbaf634af)name

| const char\* wifi\_nm\_instance::name |
| --- |

Name of the Network manager instance.

## [◆ ](#a65e73ea84dfd64dc17f0af03477362ae)ops

| const struct [wifi\_mgmt\_ops](structwifi__mgmt__ops.md)\* wifi\_nm\_instance::ops |
| --- |

Wi-Fi Management operations.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_nm.h](wifi__nm_8h_source.md)

- [wifi\_nm\_instance](structwifi__nm__instance.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
