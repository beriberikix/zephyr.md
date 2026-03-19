---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__credentials__enterprise.html
original_path: doxygen/html/structwifi__credentials__enterprise.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_credentials\_enterprise Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi credentials library](group__wifi__credentials.md)

Wi-Fi Enterprise credentials entry.
[More...](#details)

`#include <[wifi_credentials.h](wifi__credentials_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [wifi\_credentials\_header](structwifi__credentials__header.md) | [header](#a58ba430cb51a80009639263ebe412895) |
|  | Header. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [identity\_len](#aadd1fe1f5d3f3983a5cd82d5d33a4ff4) |
|  | Length of the identity. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [anonymous\_identity\_len](#a8871721054c824b056fcbb9492bf96aa) |
|  | Length of the anonymous identity. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [password\_len](#aeb480da7b9b4c7e0f4ab3b86977032f9) |
|  | Length of the password. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [ca\_cert\_len](#a74d046dbfdc2f1208848c564c8d98843) |
|  | Length of the CA certificate. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [client\_cert\_len](#a33525f5af6db7813b8f19554fd5c04f0) |
|  | Length of the client certificate. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [private\_key\_len](#a757f7cfbaf1874be1300f68bf42ebc9d) |
|  | Length of the private key. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [private\_key\_pw\_len](#ab532c721b2e10c44bf660d67ca63f994) |
|  | Length of the private key password. |

## Detailed Description

Wi-Fi Enterprise credentials entry.

Note
:   This functionality is not yet implemented.

## Field Documentation

## [◆ ](#a8871721054c824b056fcbb9492bf96aa)anonymous\_identity\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::anonymous\_identity\_len |
| --- |

Length of the anonymous identity.

## [◆ ](#a74d046dbfdc2f1208848c564c8d98843)ca\_cert\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::ca\_cert\_len |
| --- |

Length of the CA certificate.

## [◆ ](#a33525f5af6db7813b8f19554fd5c04f0)client\_cert\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::client\_cert\_len |
| --- |

Length of the client certificate.

## [◆ ](#a58ba430cb51a80009639263ebe412895)header

| struct [wifi\_credentials\_header](structwifi__credentials__header.md) wifi\_credentials\_enterprise::header |
| --- |

Header.

## [◆ ](#aadd1fe1f5d3f3983a5cd82d5d33a4ff4)identity\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::identity\_len |
| --- |

Length of the identity.

## [◆ ](#aeb480da7b9b4c7e0f4ab3b86977032f9)password\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::password\_len |
| --- |

Length of the password.

## [◆ ](#a757f7cfbaf1874be1300f68bf42ebc9d)private\_key\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::private\_key\_len |
| --- |

Length of the private key.

## [◆ ](#ab532c721b2e10c44bf660d67ca63f994)private\_key\_pw\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_enterprise::private\_key\_pw\_len |
| --- |

Length of the private key password.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_credentials.h](wifi__credentials_8h_source.md)

- [wifi\_credentials\_enterprise](structwifi__credentials__enterprise.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
