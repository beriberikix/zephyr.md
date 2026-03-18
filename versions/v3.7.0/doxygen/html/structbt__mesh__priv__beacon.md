---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__priv__beacon.html
original_path: doxygen/html/structbt__mesh__priv__beacon.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_priv\_beacon Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Private Beacon Client](group__bt__mesh__priv__beacon__cli.md)

Private Beacon.
[More...](#details)

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [enabled](#ac38424ed4ebcd69307568763ff2d6ffb) |
|  | Private beacon is enabled. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rand\_interval](#a1a4972527afde6f9aa5c7726d85ddd45) |
|  | Random refresh interval (in 10 second steps), or 0 to keep current value. |

## Detailed Description

Private Beacon.

## Field Documentation

## [◆ ](#ac38424ed4ebcd69307568763ff2d6ffb)enabled

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_priv\_beacon::enabled |
| --- |

Private beacon is enabled.

## [◆ ](#a1a4972527afde6f9aa5c7726d85ddd45)rand\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_priv\_beacon::rand\_interval |
| --- |

Random refresh interval (in 10 second steps), or 0 to keep current value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[priv\_beacon\_cli.h](priv__beacon__cli_8h_source.md)

- [bt\_mesh\_priv\_beacon](structbt__mesh__priv__beacon.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
