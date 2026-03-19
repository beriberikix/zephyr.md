---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__rpr__scan__status.html
original_path: doxygen/html/structbt__mesh__rpr__scan__status.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_rpr\_scan\_status Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Remote Provisioning Client model](group__bt__mesh__rpr__cli.md)

Scan status response.
[More...](#details)

`#include <[rpr_cli.h](rpr__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90) | [status](#a2e2023bc7dcb31ae8716203b726f7ebb) |
|  | Current scan status. |
| enum [bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291) | [scan](#ac9e5f2e4db9fc9b04dddd2687a712ff8) |
|  | Current scan state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_devs](#ac7fc9a15127dc1eae44d2ec610efd5be) |
|  | Max number of devices to report in current scan. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [timeout](#a8d062579fb074ded769bf367e0287052) |
|  | Seconds remaining of the scan. |

## Detailed Description

Scan status response.

## Field Documentation

## [◆ ](#ac7fc9a15127dc1eae44d2ec610efd5be)max\_devs

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_scan\_status::max\_devs |
| --- |

Max number of devices to report in current scan.

## [◆ ](#ac9e5f2e4db9fc9b04dddd2687a712ff8)scan

| enum [bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291) bt\_mesh\_rpr\_scan\_status::scan |
| --- |

Current scan state.

## [◆ ](#a2e2023bc7dcb31ae8716203b726f7ebb)status

| enum [bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90) bt\_mesh\_rpr\_scan\_status::status |
| --- |

Current scan status.

## [◆ ](#a8d062579fb074ded769bf367e0287052)timeout

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_scan\_status::timeout |
| --- |

Seconds remaining of the scan.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[rpr\_cli.h](rpr__cli_8h_source.md)

- [bt\_mesh\_rpr\_scan\_status](structbt__mesh__rpr__scan__status.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
