---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__ext__adv__sent__info.html
original_path: doxygen/html/structbt__le__ext__adv__sent__info.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_sent\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Info of the advertising sent event.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_sent](#a80f661efd35b069c2f8700851e9429a2) |
|  | If the advertising set was started with a non-zero [bt\_le\_ext\_adv\_start\_param::num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f "bt_le_ext_adv_start_param::num_events"), this field contains the number of times this advertising set has been sent since it was enabled. |

## Detailed Description

Info of the advertising sent event.

Note
:   Used in [bt\_le\_ext\_adv\_cb](structbt__le__ext__adv__cb.md "bt_le_ext_adv_cb").

## Field Documentation

## [◆ ](#a80f661efd35b069c2f8700851e9429a2)num\_sent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_ext\_adv\_sent\_info::num\_sent |
| --- |

If the advertising set was started with a non-zero [bt\_le\_ext\_adv\_start\_param::num\_events](structbt__le__ext__adv__start__param.md#ab45ae0bfdb144071efcc64c30648388f "bt_le_ext_adv_start_param::num_events"), this field contains the number of times this advertising set has been sent since it was enabled.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_sent\_info](structbt__le__ext__adv__sent__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
