---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__commander__change__volume__offset__param.html
original_path: doxygen/html/structbt__cap__commander__change__volume__offset__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_change\_volume\_offset\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for changing volume offset.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a8c22810a91d3109c3d633156bf16dffd) |
|  | The type of the set. |
| struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) \* | [param](#a2610505f60d1a67ffef916dadefe841d) |
|  | The set of devices for this procedure. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#ae3d416680196b0ee753a80d6fccb468b) |
|  | The number of parameters in `param`. |

## Detailed Description

Parameters for changing volume offset.

## Field Documentation

## [◆ ](#ae3d416680196b0ee753a80d6fccb468b)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_change\_volume\_offset\_param::count |
| --- |

The number of parameters in `param`.

## [◆ ](#a2610505f60d1a67ffef916dadefe841d)param

| struct [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md)\* bt\_cap\_commander\_change\_volume\_offset\_param::param |
| --- |

The set of devices for this procedure.

## [◆ ](#a8c22810a91d3109c3d633156bf16dffd)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_change\_volume\_offset\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
