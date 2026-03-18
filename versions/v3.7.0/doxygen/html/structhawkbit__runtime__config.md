---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhawkbit__runtime__config.html
original_path: doxygen/html/structhawkbit__runtime__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkbit\_runtime\_config Struct Reference

[Third-party](group__third__party.md) » [hawkBit Firmware Over-the-Air](group__hawkbit.md)

hawkBit configuration structure.
[More...](#details)

`#include <[hawkbit.h](hawkbit_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [server\_addr](#aee3966a3387498d726ca960663b0b291) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [server\_port](#a33343e076372adca50c1bab528881565) |
| char \* | [auth\_token](#a519e5dbc87d0b472b87cb3dbf01a7807) |
| [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) | [tls\_tag](#a1fb0307aaeb6107428ae279108057af3) |

## Detailed Description

hawkBit configuration structure.

This structure is used to store the hawkBit configuration settings.

## Field Documentation

## [◆ ](#a519e5dbc87d0b472b87cb3dbf01a7807)auth\_token

| char\* hawkbit\_runtime\_config::auth\_token |
| --- |

## [◆ ](#aee3966a3387498d726ca960663b0b291)server\_addr

| char\* hawkbit\_runtime\_config::server\_addr |
| --- |

## [◆ ](#a33343e076372adca50c1bab528881565)server\_port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hawkbit\_runtime\_config::server\_port |
| --- |

## [◆ ](#a1fb0307aaeb6107428ae279108057af3)tls\_tag

| [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) hawkbit\_runtime\_config::tls\_tag |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[hawkbit.h](hawkbit_8h_source.md)

- [hawkbit\_runtime\_config](structhawkbit__runtime__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
