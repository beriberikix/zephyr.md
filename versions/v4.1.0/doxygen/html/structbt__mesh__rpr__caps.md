---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__rpr__caps.html
original_path: doxygen/html/structbt__mesh__rpr__caps.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_rpr\_caps Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Remote Provisioning Client model](group__bt__mesh__rpr__cli.md)

Remote Provisioning Server scanning capabilities.
[More...](#details)

`#include <[rpr_cli.h](rpr__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_devs](#af14cce916d388c18ca33d4fc9adb36b5) |
|  | Max number of scannable devices. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [active\_scan](#a2de75ef667698a6094051a71ba9808ce) |
|  | Supports active scan. |

## Detailed Description

Remote Provisioning Server scanning capabilities.

## Field Documentation

## [◆ ](#a2de75ef667698a6094051a71ba9808ce)active\_scan

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_rpr\_caps::active\_scan |
| --- |

Supports active scan.

## [◆ ](#af14cce916d388c18ca33d4fc9adb36b5)max\_devs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_caps::max\_devs |
| --- |

Max number of scannable devices.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[rpr\_cli.h](rpr__cli_8h_source.md)

- [bt\_mesh\_rpr\_caps](structbt__mesh__rpr__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
