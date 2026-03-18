---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structwifi__twt__flow__info.html
original_path: doxygen/html/structwifi__twt__flow__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_twt\_flow\_info Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi TWT flow information.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [twt\_interval](#ae15ba49fa54f82cc6a1fb0d4572114b7) |
|  | Interval = Wake up time + Sleeping time. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dialog\_token](#a123ce10bed8b62b01919a7ea7644a0ba) |
|  | Dialog token, used to map requests to responses. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flow\_id](#acb0c618f1cebcb172f342cfe222683be) |
|  | Flow ID, used to map setup with teardown. |
| enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) | [negotiation\_type](#a620ae8ba546e4091d74280cb1553b2cf) |
|  | TWT negotiation type, see enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8 "Wi-Fi Target Wake Time (TWT) negotiation types."). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [responder](#ac82e4de8ffc82f851061f8ba8d217dc1) |
|  | Requestor or responder. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [trigger](#a952a67bd092c5dadba387bb13449c6f3) |
|  | Trigger enabled or disabled. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [implicit](#afb480be82d1c6f351bd634fd83bfa5c7) |
|  | Implicit or explicit. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [announce](#afc81a5111c265fd9bb2aca5f9510bfa8) |
|  | Announced or unannounced. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [twt\_wake\_interval](#aede6cb0cfc999fac8ded49e2981a3762) |
|  | Wake up time. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [twt\_wake\_ahead\_duration](#a6384d3829d54a58a53eafcb74c64a658) |
|  | Wake ahead duration. |

## Detailed Description

Wi-Fi TWT flow information.

## Field Documentation

## [◆ ](#afc81a5111c265fd9bb2aca5f9510bfa8)announce

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_flow\_info::announce |
| --- |

Announced or unannounced.

## [◆ ](#a123ce10bed8b62b01919a7ea7644a0ba)dialog\_token

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_flow\_info::dialog\_token |
| --- |

Dialog token, used to map requests to responses.

## [◆ ](#acb0c618f1cebcb172f342cfe222683be)flow\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_flow\_info::flow\_id |
| --- |

Flow ID, used to map setup with teardown.

## [◆ ](#afb480be82d1c6f351bd634fd83bfa5c7)implicit

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_flow\_info::implicit |
| --- |

Implicit or explicit.

## [◆ ](#a620ae8ba546e4091d74280cb1553b2cf)negotiation\_type

| enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) wifi\_twt\_flow\_info::negotiation\_type |
| --- |

TWT negotiation type, see enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8 "Wi-Fi Target Wake Time (TWT) negotiation types.").

## [◆ ](#ac82e4de8ffc82f851061f8ba8d217dc1)responder

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_flow\_info::responder |
| --- |

Requestor or responder.

## [◆ ](#a952a67bd092c5dadba387bb13449c6f3)trigger

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_flow\_info::trigger |
| --- |

Trigger enabled or disabled.

## [◆ ](#ae15ba49fa54f82cc6a1fb0d4572114b7)twt\_interval

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) wifi\_twt\_flow\_info::twt\_interval |
| --- |

Interval = Wake up time + Sleeping time.

## [◆ ](#a6384d3829d54a58a53eafcb74c64a658)twt\_wake\_ahead\_duration

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_twt\_flow\_info::twt\_wake\_ahead\_duration |
| --- |

Wake ahead duration.

## [◆ ](#aede6cb0cfc999fac8ded49e2981a3762)twt\_wake\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_twt\_flow\_info::twt\_wake\_interval |
| --- |

Wake up time.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
