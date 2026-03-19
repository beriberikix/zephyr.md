---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__csip__set__coordinator__cb.html
original_path: doxygen/html/structbt__csip__set__coordinator__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_csip\_set\_coordinator\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Coordinated Set Identification Profile (CSIP)](group__bt__csip.md)

Struct to hold the Coordinated Set Identification Profile Set Coordinator callbacks.
[More...](#details)

`#include <[csip.h](csip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c) | [discover](#a724060375ef6f53fcdbabcc12032a4b0) |
|  | Callback when discovery has finished. |
| [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) | [lock\_set](#a25474d60bcd8ee07ef3691554d9bd7ba) |
|  | Callback when locking a set has finished. |
| [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) | [release\_set](#acc1efc493dd05f14fdc010240982e0de) |
|  | Callback when unlocking a set has finished. |
| [bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b) | [lock\_changed](#adfa831556d13dbda8f06f69f69f9cac1) |
|  | Callback when a set's lock state has changed. |
| [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2) | [sirk\_changed](#a5bb08e8ce5759f67d2ff02459efe114d) |
|  | Callback when a set's SIRK has changed. |
| [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb) | [ordered\_access](#ae8cf52f1ace4ea1d56ec2204c59bb71c) |
|  | Callback for the ordered access procedure. |

## Detailed Description

Struct to hold the Coordinated Set Identification Profile Set Coordinator callbacks.

These can be registered for usage with [bt\_csip\_set\_coordinator\_register\_cb()](group__bt__csip.md#ga08c514fda44e5a9b5cfc16be629c2b37 "Registers callbacks for csip_set_coordinator.").

## Field Documentation

## [◆ ](#a724060375ef6f53fcdbabcc12032a4b0)discover

| [bt\_csip\_set\_coordinator\_discover\_cb](group__bt__csip.md#gaeee5f0691ba0d63a370ac5dd94cb4d5c) bt\_csip\_set\_coordinator\_cb::discover |
| --- |

Callback when discovery has finished.

## [◆ ](#adfa831556d13dbda8f06f69f69f9cac1)lock\_changed

| [bt\_csip\_set\_coordinator\_lock\_changed\_cb](group__bt__csip.md#ga991ee886c814e0b72fa12ed58ef4a90b) bt\_csip\_set\_coordinator\_cb::lock\_changed |
| --- |

Callback when a set's lock state has changed.

## [◆ ](#a25474d60bcd8ee07ef3691554d9bd7ba)lock\_set

| [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) bt\_csip\_set\_coordinator\_cb::lock\_set |
| --- |

Callback when locking a set has finished.

## [◆ ](#ae8cf52f1ace4ea1d56ec2204c59bb71c)ordered\_access

| [bt\_csip\_set\_coordinator\_ordered\_access\_cb\_t](group__bt__csip.md#ga0f2e0b610a4db975a72c6d9a645964cb) bt\_csip\_set\_coordinator\_cb::ordered\_access |
| --- |

Callback for the ordered access procedure.

## [◆ ](#acc1efc493dd05f14fdc010240982e0de)release\_set

| [bt\_csip\_set\_coordinator\_lock\_set\_cb](group__bt__csip.md#ga994431ea69920d9e84f35ca6e1e5f634) bt\_csip\_set\_coordinator\_cb::release\_set |
| --- |

Callback when unlocking a set has finished.

## [◆ ](#a5bb08e8ce5759f67d2ff02459efe114d)sirk\_changed

| [bt\_csip\_set\_coordinator\_sirk\_changed\_cb](group__bt__csip.md#gacdb98c9ae3248064e90352387df7cef2) bt\_csip\_set\_coordinator\_cb::sirk\_changed |
| --- |

Callback when a set's SIRK has changed.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[csip.h](csip_8h_source.md)

- [bt\_csip\_set\_coordinator\_cb](structbt__csip__set__coordinator__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
