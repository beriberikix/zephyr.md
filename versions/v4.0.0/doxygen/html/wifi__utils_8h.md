---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/wifi__utils_8h.html
original_path: doxygen/html/wifi__utils_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_utils.h File Reference

Utility functions to be used by the Wi-Fi subsystem.
[More...](#details)

[Go to the source code of this file.](wifi__utils_8h_source.md)

| Wi-Fi utility functions. | |
| --- | --- |
| Utility functions for the Wi-Fi subsystem. | |
| #define | [WIFI\_UTILS\_MAX\_BAND\_STR\_LEN](group__wifi__mgmt.md#ga1104c3c97b460f9f3e15a7a9c56e80af)   3 |
|  | Maximum length of the band specification string. |
| #define | [WIFI\_UTILS\_MAX\_CHAN\_STR\_LEN](group__wifi__mgmt.md#gaacc3c661affda7b376a4024efd645f0b)   4 |
|  | Maximum length of the channel specification string. |
| int | [wifi\_utils\_parse\_scan\_bands](group__wifi__mgmt.md#ga4c91cd7dff0fd9e5402970f3222dc20d) (char \*scan\_bands\_str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*band\_map) |
|  | Convert a band specification string to a bitmap representing the bands. |
| int | [wifi\_utils\_parse\_scan\_ssids](group__wifi__mgmt.md#ga471a96d3fb6d610a591508b52d4c05a4) (char \*scan\_ssids\_str, const char \*ssids[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_ssids) |
|  | Append a string containing an SSID to an array of SSID strings. |
| int | [wifi\_utils\_parse\_scan\_chan](group__wifi__mgmt.md#gaba9f3117bcef9da1efc1841d3bd9adfd) (char \*scan\_chan\_str, struct [wifi\_band\_channel](structwifi__band__channel.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_channels) |
|  | Convert a string containing a specification of scan channels to an array. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan](group__wifi__mgmt.md#gaf1872d0ed2efd3737a36dcc0ab13f18e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) band, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against a band. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan\_2g](group__wifi__mgmt.md#gaf408ba9f75354d3eca735b4804fdf199) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against the 2.4 GHz band. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan\_5g](group__wifi__mgmt.md#gae013eee6d6b74126c29d6ca7b2036310) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against the 5 GHz band. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_utils\_validate\_chan\_6g](group__wifi__mgmt.md#ga2606742e23f48da5ca1660aeac47888b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan) |
|  | Validate a channel against the 6 GHz band. |

## Detailed Description

Utility functions to be used by the Wi-Fi subsystem.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_utils.h](wifi__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
