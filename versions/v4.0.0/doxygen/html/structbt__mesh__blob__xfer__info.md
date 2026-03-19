---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__blob__xfer__info.html
original_path: doxygen/html/structbt__mesh__blob__xfer__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_xfer\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

BLOB transfer information.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) | [status](#aaeda1f5688bfb3cc3708e3797f3190a5) |
|  | BLOB transfer status. |
| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) | [mode](#a6cbb21582332cb23125624db5a02731a) |
|  | BLOB transfer mode. |
| enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) | [phase](#a6a8686872018ceb6e4e9fc52eaff5b9e) |
|  | BLOB transfer phase. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [id](#a3a19a5f387b53dd32429c9e76e53a87f) |
|  | BLOB ID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [size](#ac03d3ad7a618ee67f9bd7f1d52019cb7) |
|  | BLOB size in octets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [block\_size\_log](#ad09a0e80202b4953788fcade5788f0ef) |
|  | Logarithmic representation of the block size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu\_size](#ae24ed28faaef6187850cb0f04da2b8c7) |
|  | MTU size in octets. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [missing\_blocks](#a8825fba3258805db956b099ddfa19f9f) |
|  | Bit field indicating blocks that were not received. |

## Detailed Description

BLOB transfer information.

If `phase` is [BT\_MESH\_BLOB\_XFER\_PHASE\_INACTIVE](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600 "BT_MESH_BLOB_XFER_PHASE_INACTIVE"), the fields below `phase` are not initialized. If `phase` is [BT\_MESH\_BLOB\_XFER\_PHASE\_WAITING\_FOR\_START](group__bt__mesh__blob.md#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9 "BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START"), the fields below `id` are not initialized.

## Field Documentation

## [◆ ](#ad09a0e80202b4953788fcade5788f0ef)block\_size\_log

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_xfer\_info::block\_size\_log |
| --- |

Logarithmic representation of the block size.

## [◆ ](#a3a19a5f387b53dd32429c9e76e53a87f)id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bt\_mesh\_blob\_xfer\_info::id |
| --- |

BLOB ID.

## [◆ ](#a8825fba3258805db956b099ddfa19f9f)missing\_blocks

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_blob\_xfer\_info::missing\_blocks |
| --- |

Bit field indicating blocks that were not received.

## [◆ ](#a6cbb21582332cb23125624db5a02731a)mode

| enum [bt\_mesh\_blob\_xfer\_mode](group__bt__mesh__blob.md#gae0cb28c0e50d02f6e003062457053618) bt\_mesh\_blob\_xfer\_info::mode |
| --- |

BLOB transfer mode.

## [◆ ](#ae24ed28faaef6187850cb0f04da2b8c7)mtu\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_xfer\_info::mtu\_size |
| --- |

MTU size in octets.

## [◆ ](#a6a8686872018ceb6e4e9fc52eaff5b9e)phase

| enum [bt\_mesh\_blob\_xfer\_phase](group__bt__mesh__blob.md#ga26ed2c64bae03758a8a53b28052d0f81) bt\_mesh\_blob\_xfer\_info::phase |
| --- |

BLOB transfer phase.

## [◆ ](#ac03d3ad7a618ee67f9bd7f1d52019cb7)size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_blob\_xfer\_info::size |
| --- |

BLOB size in octets.

## [◆ ](#aaeda1f5688bfb3cc3708e3797f3190a5)status

| enum [bt\_mesh\_blob\_status](group__bt__mesh__blob.md#ga7b5e2895a6577103a8a680a94ee7776d) bt\_mesh\_blob\_xfer\_info::status |
| --- |

BLOB transfer status.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
