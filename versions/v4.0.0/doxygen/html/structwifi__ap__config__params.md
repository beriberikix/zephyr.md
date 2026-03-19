---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__ap__config__params.html
original_path: doxygen/html/structwifi__ap__config__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_ap\_config\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi AP configuration parameter.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) | [type](#a4c391cf504a994ed0bc4971afdf76774) |
|  | Parameter used to identify the different AP parameters. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_inactivity](#a289866d9209450e893281b4c198a546a) |
|  | Parameter used for setting maximum inactivity duration for stations. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_num\_sta](#a7fc0fad99f53ed8e1ac40b74ec98bf9a) |
|  | Parameter used for setting maximum number of stations. |

## Detailed Description

Wi-Fi AP configuration parameter.

## Field Documentation

## [◆ ](#a289866d9209450e893281b4c198a546a)max\_inactivity

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_ap\_config\_params::max\_inactivity |
| --- |

Parameter used for setting maximum inactivity duration for stations.

## [◆ ](#a7fc0fad99f53ed8e1ac40b74ec98bf9a)max\_num\_sta

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_ap\_config\_params::max\_num\_sta |
| --- |

Parameter used for setting maximum number of stations.

## [◆ ](#a4c391cf504a994ed0bc4971afdf76774)type

| enum [wifi\_ap\_config\_param](group__wifi__mgmt.md#ga83546cf946a9123c563609e8903d9642) wifi\_ap\_config\_params::type |
| --- |

Parameter used to identify the different AP parameters.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_ap\_config\_params](structwifi__ap__config__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
