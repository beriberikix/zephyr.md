---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cap__commander__broadcast__reception__stop__param.html
original_path: doxygen/html/structbt__cap__commander__broadcast__reception__stop__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_commander\_broadcast\_reception\_stop\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

`#include <[cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) | [type](#a35bc972b00c10b90544da19c659fc460) |
|  | The type of the set. |
| struct [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) \* | [param](#a36ce7cd132cd41a55872985433c2934d) |
|  | The set of devices for this procedure. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [count](#add81cdf1e3bad07b43602c8ce7c47593) |
|  | The number of parameters in `param`. |

## Field Documentation

## [◆ ](#add81cdf1e3bad07b43602c8ce7c47593)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_commander\_broadcast\_reception\_stop\_param::count |
| --- |

The number of parameters in `param`.

## [◆ ](#a36ce7cd132cd41a55872985433c2934d)param

| struct [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md)\* bt\_cap\_commander\_broadcast\_reception\_stop\_param::param |
| --- |

The set of devices for this procedure.

## [◆ ](#a35bc972b00c10b90544da19c659fc460)type

| enum [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) bt\_cap\_commander\_broadcast\_reception\_stop\_param::type |
| --- |

The type of the set.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
