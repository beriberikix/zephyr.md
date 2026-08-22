---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__per__adv__param.html
original_path: doxygen/html/structbt__le__per__adv__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Parameters for configuring periodic advertising.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval\_min](#a49da44a3c0e4e866ffccffae5a9a22f7) |
|  | Minimum Periodic Advertising Interval (N \* 1.25 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval\_max](#a61308cfe72ad23372dfd2a3bd2550726) |
|  | Maximum Periodic Advertising Interval (N \* 1.25 ms). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a9b80c2427171920f466601e7e8468814) |
|  | Bit-field of periodic advertising options, see the [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28 "bt_le_adv_opt") field. |

## Detailed Description

Parameters for configuring periodic advertising.

This struct is used to configure the parameters for periodic advertising, including the minimum and maximum advertising intervals, options, and settings for subevents if periodic advertising responses are supported. The intervals are specified in units of 1.25 ms, and the options field can be used to modify other advertising behaviors. For extended advertisers, the periodic advertising parameters can be set or updated using this structure. Some parameters are conditional based on whether the device supports periodic advertising responses (configured via `CONFIG_BT_PER_ADV_RSP`).

Note
:   Used in [bt\_le\_per\_adv\_set\_param](group__bt__gap.md#gaa72029a2759123ec776061d2e80bf3a1 "bt_le_per_adv_set_param") function.

## Field Documentation

## [◆ ](#a61308cfe72ad23372dfd2a3bd2550726)interval\_max

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_param::interval\_max |
| --- |

Maximum Periodic Advertising Interval (N \* 1.25 ms).

Shall be less or equal to BT\_GAP\_PER\_ADV\_MAX\_INTERVAL and greater or equal to interval\_min.

## [◆ ](#a49da44a3c0e4e866ffccffae5a9a22f7)interval\_min

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_param::interval\_min |
| --- |

Minimum Periodic Advertising Interval (N \* 1.25 ms).

Shall be greater or equal to BT\_GAP\_PER\_ADV\_MIN\_INTERVAL and less or equal to interval\_max.

## [◆ ](#a9b80c2427171920f466601e7e8468814)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_per\_adv\_param::options |
| --- |

Bit-field of periodic advertising options, see the [bt\_le\_adv\_opt](group__bt__gap.md#gafbf81dab68b0e484d4742471c722fc28 "bt_le_adv_opt") field.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_param](structbt__le__per__adv__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
