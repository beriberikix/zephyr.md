---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__rpr__unprov.html
original_path: doxygen/html/structbt__mesh__rpr__unprov.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_rpr\_unprov Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Remote Provisioning models](group__bt__mesh__rpr.md)

Unprovisioned device.
[More...](#details)

`#include <[rpr.h](rpr_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uuid](#aa5fe6bad39edcb45d2e024c1c890c680) [16] |
|  | Unprovisioned device UUID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a9d0103e4899b445c2c20d62749889e3e) |
|  | Flags, see `BT_MESH_RPR_UNPROV_*` flags. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a26ffffb174704a0a6a35418886e2a971) |
|  | RSSI of unprovisioned device, as received by server. |
| [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) | [oob](#a51e9bfeb3145c29644378d6ec5400e75) |
|  | Out of band information. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hash](#ade58aed40bfaffb6f23a4e0570e370dd) |
|  | URI hash in unprovisioned beacon. |

## Detailed Description

Unprovisioned device.

## Field Documentation

## [◆ ](#a9d0103e4899b445c2c20d62749889e3e)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_unprov::flags |
| --- |

Flags, see `BT_MESH_RPR_UNPROV_*` flags.

## [◆ ](#ade58aed40bfaffb6f23a4e0570e370dd)hash

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_rpr\_unprov::hash |
| --- |

URI hash in unprovisioned beacon.

Only valid if `flags` has [BT\_MESH\_RPR\_UNPROV\_HASH](group__bt__mesh__rpr.md#ga94522cf0b3832b576100b787808474bd "BT_MESH_RPR_UNPROV_HASH") set.

## [◆ ](#a51e9bfeb3145c29644378d6ec5400e75)oob

| [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) bt\_mesh\_rpr\_unprov::oob |
| --- |

Out of band information.

## [◆ ](#a26ffffb174704a0a6a35418886e2a971)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_mesh\_rpr\_unprov::rssi |
| --- |

RSSI of unprovisioned device, as received by server.

## [◆ ](#aa5fe6bad39edcb45d2e024c1c890c680)uuid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_unprov::uuid[16] |
| --- |

Unprovisioned device UUID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[rpr.h](rpr_8h_source.md)

- [bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
