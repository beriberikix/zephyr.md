---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__big__sync__param.html
original_path: doxygen/html/structbt__iso__big__sync__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_big\_sync\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

Broadcast Isochronous Group (BIG) Sync Parameters.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_iso\_chan](structbt__iso__chan.md) \*\* | [bis\_channels](#ac56d7206c3434837a52059716355adad) |
|  | Array of pointers to BIS channels. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_bis](#a96cd109e9f5820531635d48e88b4bff8) |
|  | Number channels in `bis_channels`. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bis\_bitfield](#a14b03509daf760edbead86659f733136) |
|  | Bitfield of the BISes to sync to. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mse](#a16b332b4a0f373cb21e5da6e6e383b9e) |
|  | Maximum subevents. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sync\_timeout](#a8e344870fc0e380e6588eb90c7ef72f9) |
|  | Synchronization timeout for the BIG (N \* 10 MS). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a8e5cffe8960477e7f64707d7dd4191f6) |
|  | Whether or not the streams of the BIG are encrypted. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcode](#aaecdeabed10b90e84b618dac1129a9dc) [16] |
|  | Broadcast code. |

## Detailed Description

Broadcast Isochronous Group (BIG) Sync Parameters.

## Field Documentation

## [◆ ](#aaecdeabed10b90e84b618dac1129a9dc)bcode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_big\_sync\_param::bcode[16] |
| --- |

Broadcast code.

The code used to derive the session key that is used to encrypt and decrypt BIS payloads.

If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0.

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

## [◆ ](#a14b03509daf760edbead86659f733136)bis\_bitfield

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_big\_sync\_param::bis\_bitfield |
| --- |

Bitfield of the BISes to sync to.

The BIS indexes start from 0x01, so the lowest allowed bit is [BIT(1)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") that represents index 0x01. To synchronize to e.g. BIS indexes 0x01 and 0x02, the bitfield value should be [BIT(1)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") | [BIT(2)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).").

## [◆ ](#ac56d7206c3434837a52059716355adad)bis\_channels

| struct [bt\_iso\_chan](structbt__iso__chan.md)\*\* bt\_iso\_big\_sync\_param::bis\_channels |
| --- |

Array of pointers to BIS channels.

## [◆ ](#a8e5cffe8960477e7f64707d7dd4191f6)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_iso\_big\_sync\_param::encryption |
| --- |

Whether or not the streams of the BIG are encrypted.

## [◆ ](#a16b332b4a0f373cb21e5da6e6e383b9e)mse

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_big\_sync\_param::mse |
| --- |

Maximum subevents.

The MSE (Maximum Subevents) parameter is the maximum number of subevents that a Controller should use to receive data payloads in each interval for a BIS.

Value range is BT\_ISO\_SYNC\_MSE\_MIN to BT\_ISO\_SYNC\_MSE\_MAX, or BT\_ISO\_SYNC\_MSE\_ANY to let the controller choose.

## [◆ ](#a96cd109e9f5820531635d48e88b4bff8)num\_bis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_big\_sync\_param::num\_bis |
| --- |

Number channels in `bis_channels`.

Maximum number of channels in a single group is BT\_ISO\_MAX\_GROUP\_ISO\_COUNT

## [◆ ](#a8e344870fc0e380e6588eb90c7ef72f9)sync\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_big\_sync\_param::sync\_timeout |
| --- |

Synchronization timeout for the BIG (N \* 10 MS).

Value range is BT\_ISO\_SYNC\_TIMEOUT\_MIN to BT\_ISO\_SYNC\_TIMEOUT\_MAX.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
