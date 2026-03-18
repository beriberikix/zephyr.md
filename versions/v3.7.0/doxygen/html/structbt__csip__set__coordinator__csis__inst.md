---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__csip__set__coordinator__csis__inst.html
original_path: doxygen/html/structbt__csip__set__coordinator__csis__inst.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_csip\_set\_coordinator\_csis\_inst Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Coordinated Set Identification Profile (CSIP)](group__bt__gatt__csip.md)

Struct representing a coordinated set instance on a remote device.
[More...](#details)

`#include <[csip.h](csip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) | [info](#a0c407932ad1fb5e36cd19daf28bac96d) |
|  | Information about the coordinated set. |
| void \* | [svc\_inst](#a7e7210dded5a084c5d45f9209895e37f) |
|  | Internally used pointer value. |

## Detailed Description

Struct representing a coordinated set instance on a remote device.

The values in this struct will be populated during discovery of sets ([bt\_csip\_set\_coordinator\_discover()](group__bt__gatt__csip.md#ga7e7ea4a92bb76aded86807571a2cbb73 "Initialise the csip_set_coordinator instance for a connection.")).

## Field Documentation

## [◆ ](#a0c407932ad1fb5e36cd19daf28bac96d)info

| struct [bt\_csip\_set\_coordinator\_set\_info](structbt__csip__set__coordinator__set__info.md) bt\_csip\_set\_coordinator\_csis\_inst::info |
| --- |

Information about the coordinated set.

## [◆ ](#a7e7210dded5a084c5d45f9209895e37f)svc\_inst

| void\* bt\_csip\_set\_coordinator\_csis\_inst::svc\_inst |
| --- |

Internally used pointer value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[csip.h](csip_8h_source.md)

- [bt\_csip\_set\_coordinator\_csis\_inst](structbt__csip__set__coordinator__csis__inst.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
