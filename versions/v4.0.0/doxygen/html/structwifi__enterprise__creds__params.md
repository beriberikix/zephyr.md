---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__enterprise__creds__params.html
original_path: doxygen/html/structwifi__enterprise__creds__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_enterprise\_creds\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi enterprise mode credentials.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ca\_cert](#ae37381504a457b2f1d56dd5270c6711d) |
|  | CA certification. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ca\_cert\_len](#a5f7060fcd2ca3db0b202faf15062564b) |
|  | CA certification length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [client\_cert](#a81d61179feba627be5c6456130b9f2af) |
|  | Client certification. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [client\_cert\_len](#a5f122d59b25b00af2db7eeac93d5482e) |
|  | Client certification length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [client\_key](#a8d88f5a8a6ccc8a9a883078af49ae96b) |
|  | Client key. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [client\_key\_len](#a09f5b34c81fe871e7513358499518d95) |
|  | Client key length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ca\_cert2](#ad9b867873709d7f2363fef49d7b6f2ca) |
|  | CA certification of phase2. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ca\_cert2\_len](#abf35045e71afb0cb9ea25c635c5ac141) |
|  | Phase2 CA certification length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [client\_cert2](#a133126e338d89563733268a03e2fa613) |
|  | Client certification of phase2. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [client\_cert2\_len](#adbe26c9b88f44eb6b875888f6a03e1bb) |
|  | Phase2 Client certification length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [client\_key2](#abcda4d7820681d517d70d8f130b47050) |
|  | Client key of phase2. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [client\_key2\_len](#a3da90b8a8dfa848f617579760ad4f971) |
|  | Phase2 Client key length. |

## Detailed Description

Wi-Fi enterprise mode credentials.

## Field Documentation

## [◆ ](#ae37381504a457b2f1d56dd5270c6711d)ca\_cert

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_enterprise\_creds\_params::ca\_cert |
| --- |

CA certification.

## [◆ ](#ad9b867873709d7f2363fef49d7b6f2ca)ca\_cert2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_enterprise\_creds\_params::ca\_cert2 |
| --- |

CA certification of phase2.

## [◆ ](#abf35045e71afb0cb9ea25c635c5ac141)ca\_cert2\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_enterprise\_creds\_params::ca\_cert2\_len |
| --- |

Phase2 CA certification length.

## [◆ ](#a5f7060fcd2ca3db0b202faf15062564b)ca\_cert\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_enterprise\_creds\_params::ca\_cert\_len |
| --- |

CA certification length.

## [◆ ](#a81d61179feba627be5c6456130b9f2af)client\_cert

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_enterprise\_creds\_params::client\_cert |
| --- |

Client certification.

## [◆ ](#a133126e338d89563733268a03e2fa613)client\_cert2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_enterprise\_creds\_params::client\_cert2 |
| --- |

Client certification of phase2.

## [◆ ](#adbe26c9b88f44eb6b875888f6a03e1bb)client\_cert2\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_enterprise\_creds\_params::client\_cert2\_len |
| --- |

Phase2 Client certification length.

## [◆ ](#a5f122d59b25b00af2db7eeac93d5482e)client\_cert\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_enterprise\_creds\_params::client\_cert\_len |
| --- |

Client certification length.

## [◆ ](#a8d88f5a8a6ccc8a9a883078af49ae96b)client\_key

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_enterprise\_creds\_params::client\_key |
| --- |

Client key.

## [◆ ](#abcda4d7820681d517d70d8f130b47050)client\_key2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* wifi\_enterprise\_creds\_params::client\_key2 |
| --- |

Client key of phase2.

## [◆ ](#a3da90b8a8dfa848f617579760ad4f971)client\_key2\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_enterprise\_creds\_params::client\_key2\_len |
| --- |

Phase2 Client key length.

## [◆ ](#a09f5b34c81fe871e7513358499518d95)client\_key\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_enterprise\_creds\_params::client\_key\_len |
| --- |

Client key length.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_enterprise\_creds\_params](structwifi__enterprise__creds__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
