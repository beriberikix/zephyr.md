---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__commander__change__volume__param.html
original_path: doxygen/html/structbt__cap__commander__change__volume__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_volume\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for changing absolute volume.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#ad98625aa08f54759efd349921d104c88) |
|  | The type of the set. |
| union [bt\_cap\_set\_member](unionbt__cap__set__member.md) \* | [members](#a983656766a28118b018a70fef186f531) |
|  | Coordinated or ad-hoc set member. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#a37198e9118f80e5521f140b6aa1d2640) |
|  | The number of members in `members`. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [volume](#ada17f89c8948246d68818f2e44d5ea49) |
|  | The absolute volume to set. |

## Detailed Description

Parameters for changing absolute volume.

## Field Documentation

## [◆ ](#a37198e9118f80e5521f140b6aa1d2640)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_change\_volume\_param::count |
| --- |

The number of members in `members`.

## [◆ ](#a983656766a28118b018a70fef186f531)members

| union [bt\_cap\_set\_member](unionbt__cap__set__member.md)\* bt\_cap\_commander\_change\_volume\_param::members |
| --- |

Coordinated or ad-hoc set member.

## [◆ ](#ad98625aa08f54759efd349921d104c88)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_change\_volume\_param::type |
| --- |

The type of the set.

## [◆ ](#ada17f89c8948246d68818f2e44d5ea49)volume

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_commander\_change\_volume\_param::volume |
| --- |

The absolute volume to set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
