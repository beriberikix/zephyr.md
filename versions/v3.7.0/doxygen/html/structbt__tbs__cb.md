---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__tbs__cb.html
original_path: doxygen/html/structbt__tbs__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_tbs\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Telephone Bearer Service (TBS)](group__bt__tbs.md)

Struct to hold the Telephone Bearer Service callbacks.
[More...](#details)

`#include <[tbs.h](tbs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_tbs\_originate\_call\_cb](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300) | [originate\_call](#a566504bee9c7334c53a23223e544855f) |
|  | Client originating call. |
| [bt\_tbs\_terminate\_call\_cb](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc) | [terminate\_call](#ab065a5c58db19feb2a1d3013983ed5aa) |
|  | Client terminating call. |
| [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) | [hold\_call](#a8b76dd9243e97d22e0d6c2ac578aa383) |
|  | Client holding call. |
| [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) | [accept\_call](#a798c09c04a563800c4d9328c1d9e2de6) |
|  | Client accepting call. |
| [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) | [retrieve\_call](#ad543a2f26d1749eba0774e2352b53692) |
|  | Client retrieving call. |
| [bt\_tbs\_join\_calls\_cb](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058) | [join\_calls](#ac1a99a703687a3ef5ebc12eca5f6c2e7) |
|  | Client joining calls. |
| [bt\_tbs\_authorize\_cb](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0) | [authorize](#ab7c859ffaebcf16db71c5d54bd4f5802) |
|  | Callback to authorize a client. |

## Detailed Description

Struct to hold the Telephone Bearer Service callbacks.

These can be registered for usage with [bt\_tbs\_register\_cb()](group__bt__tbs.md#ga76f120dba549225a6f2c2c22be08edfc "Register the callbacks for TBS.").

## Field Documentation

## [◆ ](#a798c09c04a563800c4d9328c1d9e2de6)accept\_call

| [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) bt\_tbs\_cb::accept\_call |
| --- |

Client accepting call.

## [◆ ](#ab7c859ffaebcf16db71c5d54bd4f5802)authorize

| [bt\_tbs\_authorize\_cb](group__bt__tbs.md#ga1cc9e7140531b07bf6a8dedbc17f24c0) bt\_tbs\_cb::authorize |
| --- |

Callback to authorize a client.

## [◆ ](#a8b76dd9243e97d22e0d6c2ac578aa383)hold\_call

| [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) bt\_tbs\_cb::hold\_call |
| --- |

Client holding call.

## [◆ ](#ac1a99a703687a3ef5ebc12eca5f6c2e7)join\_calls

| [bt\_tbs\_join\_calls\_cb](group__bt__tbs.md#gaa45b3f4837165d722c2df6f202a39058) bt\_tbs\_cb::join\_calls |
| --- |

Client joining calls.

## [◆ ](#a566504bee9c7334c53a23223e544855f)originate\_call

| [bt\_tbs\_originate\_call\_cb](group__bt__tbs.md#ga60e9e143f247bb7e668293f0233ce300) bt\_tbs\_cb::originate\_call |
| --- |

Client originating call.

## [◆ ](#ad543a2f26d1749eba0774e2352b53692)retrieve\_call

| [bt\_tbs\_call\_change\_cb](group__bt__tbs.md#ga2fa85f3cd96f25f6bb4f449fc9210fa1) bt\_tbs\_cb::retrieve\_call |
| --- |

Client retrieving call.

## [◆ ](#ab065a5c58db19feb2a1d3013983ed5aa)terminate\_call

| [bt\_tbs\_terminate\_call\_cb](group__bt__tbs.md#ga69e93b48b2a48e8a6552882660b791cc) bt\_tbs\_cb::terminate\_call |
| --- |

Client terminating call.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[tbs.h](tbs_8h_source.md)

- [bt\_tbs\_cb](structbt__tbs__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
