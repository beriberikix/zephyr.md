---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__le__cs__step__data__tone__info.html
original_path: doxygen/html/structbt__hci__le__cs__step__data__tone__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_le\_cs\_step\_data\_tone\_info Struct Reference

Format for per-antenna path step data in modes 2 and 3.
[More...](#details)

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phase\_correction\_term](#aeb76aeb54cb4e5613496431ec6d0093a) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [extension\_indicator](#a5f2e5e95b97d2be49a8ff1d9376892e8): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [quality\_indicator](#a4d31c0759c17789cb4b9bdc90a8870ca): 4 |

## Detailed Description

Format for per-antenna path step data in modes 2 and 3.

## Field Documentation

## [◆ ](#a5f2e5e95b97d2be49a8ff1d9376892e8)extension\_indicator

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_tone\_info::extension\_indicator |
| --- |

## [◆ ](#aeb76aeb54cb4e5613496431ec6d0093a)phase\_correction\_term

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_tone\_info::phase\_correction\_term[3] |
| --- |

## [◆ ](#a4d31c0759c17789cb4b9bdc90a8870ca)quality\_indicator

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_le\_cs\_step\_data\_tone\_info::quality\_indicator |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_le\_cs\_step\_data\_tone\_info](structbt__hci__le__cs__step__data__tone__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
