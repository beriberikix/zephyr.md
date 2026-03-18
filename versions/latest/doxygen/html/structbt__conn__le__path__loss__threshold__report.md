---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__conn__le__path__loss__threshold__report.html
original_path: doxygen/html/structbt__conn__le__path__loss__threshold__report.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_path\_loss\_threshold\_report Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

LE Path Loss Monitoring Threshold Change Report Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_conn\_le\_path\_loss\_zone](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e) | [zone](#ab2b71b7ddccc40ced56657a548b98e77) |
|  | Path Loss zone as documented in Core Spec. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [path\_loss](#abe631b07816d6c18bacba64bfbd1e844) |
|  | Current path loss (dB). |

## Detailed Description

LE Path Loss Monitoring Threshold Change Report Structure.

## Field Documentation

## [◆ ](#abe631b07816d6c18bacba64bfbd1e844)path\_loss

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_path\_loss\_threshold\_report::path\_loss |
| --- |

Current path loss (dB).

## [◆ ](#ab2b71b7ddccc40ced56657a548b98e77)zone

| enum [bt\_conn\_le\_path\_loss\_zone](group__bt__conn.md#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e) bt\_conn\_le\_path\_loss\_threshold\_report::zone |
| --- |

Path Loss zone as documented in Core Spec.

Version 5.4 Vol.4, Part E, 7.7.65.32.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_path\_loss\_threshold\_report](structbt__conn__le__path__loss__threshold__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
