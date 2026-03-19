---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__cap__commander__distribute__broadcast__code__param.html
original_path: doxygen/html/structbt__cap__commander__distribute__broadcast__code__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_distribute\_broadcast\_code\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for distributing broadcast code.
[More...](#details)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a9605ad1590ff0279b46d639d38278933) |
|  | The type of the set. |
| struct [bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md) \* | [param](#a03be4b2fac7803de233c8a1024640cc2) |
|  | The set of devices for this procedure. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#a86316e3bf53edca67e0743072f0f2ee3) |
|  | The number of parameters in `param`. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [broadcast\_code](#ac7d426c975c1e2324f52486abf9298b9) [[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
|  | 16-octet broadcast code. |

## Detailed Description

Parameters for distributing broadcast code.

## Field Documentation

## [◆ ](#ac7d426c975c1e2324f52486abf9298b9)broadcast\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_commander\_distribute\_broadcast\_code\_param::broadcast\_code[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)] |
| --- |

16-octet broadcast code.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a86316e3bf53edca67e0743072f0f2ee3)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_distribute\_broadcast\_code\_param::count |
| --- |

The number of parameters in `param`.

## [◆ ](#a03be4b2fac7803de233c8a1024640cc2)param

| struct [bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md)\* bt\_cap\_commander\_distribute\_broadcast\_code\_param::param |
| --- |

The set of devices for this procedure.

## [◆ ](#a9605ad1590ff0279b46d639d38278933)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_distribute\_broadcast\_code\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
