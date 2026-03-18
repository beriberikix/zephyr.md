---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structwifi__iface__status.html
original_path: doxygen/html/structwifi__iface__status.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_iface\_status Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi interface status.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [state](#ac52806155be3d64954ac6d109e76ec57) |
|  | Interface state, see enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4 "Wi-Fi interface states."). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [ssid\_len](#ad82f281941e4f6ce1ef0bca008e26d41) |
|  | SSID length. |
| char | [ssid](#a30c4bef4e061346ba61857a558640d00) [32] |
|  | SSID. |
| char | [bssid](#a28afad15fc6689669c7b19337a64eaf3) [6] |
|  | BSSID. |
| enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) | [band](#ae1c141a18f4e225af2c22a8cb4f882a8) |
|  | Frequency band. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [channel](#a6432663156e5b2c424d254ed1eae0144) |
|  | Channel. |
| enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) | [iface\_mode](#ad33d2ec149a8d556e2472dd842ceadc0) |
|  | Interface mode, see enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b "Wi-Fi interface modes."). |
| enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) | [link\_mode](#ae2de076d79f2172793d65fe9cd31edc4) |
|  | Link mode, see enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62 "Wi-Fi link operating modes."). |
| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | [security](#a625ecec1abec8dd65cf155eab21a01b5) |
|  | Security type, see enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c "IEEE 802.11 security types."). |
| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) | [mfp](#aa1a9b644fd355526125ddd32416b7c24) |
|  | MFP options, see enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76 "IEEE 802.11w - Management frame protection."). |
| int | [rssi](#a4e593147b88eb4938d55a4de72fcc7f6) |
|  | RSSI. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [dtim\_period](#aae6c8cbaa16c81d308f08114d5103a3d) |
|  | DTIM period. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [beacon\_interval](#a241bfbe70628006b515b5f9e4f97665c) |
|  | Beacon interval. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [twt\_capable](#acfde8d64b463a9f553aa4fb689dc1917) |
|  | is TWT capable? |

## Detailed Description

Wi-Fi interface status.

## Field Documentation

## [◆ ](#ae1c141a18f4e225af2c22a8cb4f882a8)band

| enum [wifi\_frequency\_bands](group__wifi__mgmt.md#ga1e2f0439a322355fa7368ea880c9c15d) wifi\_iface\_status::band |
| --- |

Frequency band.

## [◆ ](#a241bfbe70628006b515b5f9e4f97665c)beacon\_interval

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short wifi\_iface\_status::beacon\_interval |
| --- |

Beacon interval.

## [◆ ](#a28afad15fc6689669c7b19337a64eaf3)bssid

| char wifi\_iface\_status::bssid[6] |
| --- |

BSSID.

## [◆ ](#a6432663156e5b2c424d254ed1eae0144)channel

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int wifi\_iface\_status::channel |
| --- |

Channel.

## [◆ ](#aae6c8cbaa16c81d308f08114d5103a3d)dtim\_period

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char wifi\_iface\_status::dtim\_period |
| --- |

DTIM period.

## [◆ ](#ad33d2ec149a8d556e2472dd842ceadc0)iface\_mode

| enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b) wifi\_iface\_status::iface\_mode |
| --- |

Interface mode, see enum [wifi\_iface\_mode](group__wifi__mgmt.md#ga584f6239ac14e2bedc5e6bd72756423b "Wi-Fi interface modes.").

## [◆ ](#ae2de076d79f2172793d65fe9cd31edc4)link\_mode

| enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62) wifi\_iface\_status::link\_mode |
| --- |

Link mode, see enum [wifi\_link\_mode](group__wifi__mgmt.md#gabdb2a784d4727b71ab44cca04e422c62 "Wi-Fi link operating modes.").

## [◆ ](#aa1a9b644fd355526125ddd32416b7c24)mfp

| enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76) wifi\_iface\_status::mfp |
| --- |

MFP options, see enum [wifi\_mfp\_options](group__wifi__mgmt.md#ga1f252da47d9650023d7fff6d08e49c76 "IEEE 802.11w - Management frame protection.").

## [◆ ](#a4e593147b88eb4938d55a4de72fcc7f6)rssi

| int wifi\_iface\_status::rssi |
| --- |

RSSI.

## [◆ ](#a625ecec1abec8dd65cf155eab21a01b5)security

| enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) wifi\_iface\_status::security |
| --- |

Security type, see enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c "IEEE 802.11 security types.").

## [◆ ](#a30c4bef4e061346ba61857a558640d00)ssid

| char wifi\_iface\_status::ssid[32] |
| --- |

SSID.

## [◆ ](#ad82f281941e4f6ce1ef0bca008e26d41)ssid\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int wifi\_iface\_status::ssid\_len |
| --- |

SSID length.

## [◆ ](#ac52806155be3d64954ac6d109e76ec57)state

| int wifi\_iface\_status::state |
| --- |

Interface state, see enum [wifi\_iface\_state](group__wifi__mgmt.md#ga981961f747b919d61d3ccbd41e4508b4 "Wi-Fi interface states.").

## [◆ ](#acfde8d64b463a9f553aa4fb689dc1917)twt\_capable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_iface\_status::twt\_capable |
| --- |

is TWT capable?

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_iface\_status](structwifi__iface__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
