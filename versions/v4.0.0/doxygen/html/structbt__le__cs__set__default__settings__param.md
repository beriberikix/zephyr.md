---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__le__cs__set__default__settings__param.html
original_path: doxygen/html/structbt__le__cs__set__default__settings__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_cs\_set\_default\_settings\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Channel Sounding (CS)](group__bt__le__cs.md)

Default CS settings in the local Controller.
[More...](#details)

`#include <[cs.h](cs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_initiator\_role](#a6a68056e10ea18ab2bb33202a39387a4) |
|  | Enable CS initiator role. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_reflector\_role](#a7e532de60b09424da17be0e61dbafb2d) |
|  | Enable CS reflector role. |
| enum [bt\_le\_cs\_sync\_antenna\_selection\_opt](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643) | [cs\_sync\_antenna\_selection](#a581ab5686e3eedfde84817d0ffcff587) |
|  | Antenna identifier to be used for CS\_SYNC packets by the local controller. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [max\_tx\_power](#a31a3b73d2bc44306f6905a2a1958b62b) |
|  | Maximum output power (Effective Isotropic Radiated Power) to be used for all CS transmissions. |

## Detailed Description

Default CS settings in the local Controller.

## Field Documentation

## [◆ ](#a581ab5686e3eedfde84817d0ffcff587)cs\_sync\_antenna\_selection

| enum [bt\_le\_cs\_sync\_antenna\_selection\_opt](group__bt__le__cs.md#ga9f286cdeeee0e9df06e6b3df1e9ab643) bt\_le\_cs\_set\_default\_settings\_param::cs\_sync\_antenna\_selection |
| --- |

Antenna identifier to be used for CS\_SYNC packets by the local controller.

## [◆ ](#a6a68056e10ea18ab2bb33202a39387a4)enable\_initiator\_role

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_le\_cs\_set\_default\_settings\_param::enable\_initiator\_role |
| --- |

Enable CS initiator role.

## [◆ ](#a7e532de60b09424da17be0e61dbafb2d)enable\_reflector\_role

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_le\_cs\_set\_default\_settings\_param::enable\_reflector\_role |
| --- |

Enable CS reflector role.

## [◆ ](#a31a3b73d2bc44306f6905a2a1958b62b)max\_tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_cs\_set\_default\_settings\_param::max\_tx\_power |
| --- |

Maximum output power (Effective Isotropic Radiated Power) to be used for all CS transmissions.

Value range is [BT\_HCI\_OP\_LE\_CS\_MIN\_MAX\_TX\_POWER](hci__types_8h.md#a040315a8ac4f80a2c497919a2fd4d7bc "BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER") to [BT\_HCI\_OP\_LE\_CS\_MAX\_MAX\_TX\_POWER](hci__types_8h.md#a29a240b2d3f209b1f5f3d96e380dde08 "BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[cs.h](cs_8h_source.md)

- [bt\_le\_cs\_set\_default\_settings\_param](structbt__le__cs__set__default__settings__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
