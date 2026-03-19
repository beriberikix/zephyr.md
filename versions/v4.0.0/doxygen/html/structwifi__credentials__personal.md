---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwifi__credentials__personal.html
original_path: doxygen/html/structwifi__credentials__personal.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_credentials\_personal Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi credentials library](group__wifi__credentials.md)

Wi-Fi Personal credentials entry.
[More...](#details)

`#include <[wifi_credentials.h](wifi__credentials_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [wifi\_credentials\_header](structwifi__credentials__header.md) | [header](#a40f13f70ee0dd797d31b643cc754440c) |
|  | Header. |
| char | [password](#ae9ed5b123e0467054e6e18831c2b29c5) [[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(64, CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH)] |
|  | Password/PSK. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [password\_len](#a627104585a2f6d58e2f899563c2993ad) |
|  | Length of the password. |

## Detailed Description

Wi-Fi Personal credentials entry.

Note
:   Contains only the header and a password. For PSK security, passwords can be up to [WIFI\_PSK\_MAX\_LEN](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc "Maximum PSK length.") bytes long including NULL termination. For SAE security it can range up to CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH.

## Field Documentation

## [◆ ](#a40f13f70ee0dd797d31b643cc754440c)header

| struct [wifi\_credentials\_header](structwifi__credentials__header.md) wifi\_credentials\_personal::header |
| --- |

Header.

## [◆ ](#ae9ed5b123e0467054e6e18831c2b29c5)password

| char wifi\_credentials\_personal::password[[MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(64, CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH)] |
| --- |

Password/PSK.

## [◆ ](#a627104585a2f6d58e2f899563c2993ad)password\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wifi\_credentials\_personal::password\_len |
| --- |

Length of the password.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_credentials.h](wifi__credentials_8h_source.md)

- [wifi\_credentials\_personal](structwifi__credentials__personal.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
