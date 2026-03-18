---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__iso__chan.html
original_path: doxygen/html/structbt__iso__chan.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_chan Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Channel structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_conn \* | [iso](#a7fd728385a3aec11be8883bdee8aedea) |
|  | Channel connection reference. |
| struct [bt\_iso\_chan\_ops](structbt__iso__chan__ops.md) \* | [ops](#a214fe133602ac8dcfaaec7f372e12da8) |
|  | Channel operations reference. |
| struct [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md) \* | [qos](#abe94fca71506bd590d9ef4465258914d) |
|  | Channel QoS reference. |
| enum [bt\_iso\_state](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201) | [state](#a2b0fc7180d1983ee4a415c5331bed93d) |
|  | Channel state. |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [required\_sec\_level](#a75347e4f16e715be06298ccf36c8521c) |
|  | The required security level of the channel. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#aba7bf6dcad93b121c46daa6ad473a51c) |

## Detailed Description

ISO Channel structure.

## Field Documentation

## [◆ ](#a7fd728385a3aec11be8883bdee8aedea)iso

| struct bt\_conn\* bt\_iso\_chan::iso |
| --- |

Channel connection reference.

## [◆ ](#aba7bf6dcad93b121c46daa6ad473a51c)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_iso\_chan::node |
| --- |

## [◆ ](#a214fe133602ac8dcfaaec7f372e12da8)ops

| struct [bt\_iso\_chan\_ops](structbt__iso__chan__ops.md)\* bt\_iso\_chan::ops |
| --- |

Channel operations reference.

## [◆ ](#abe94fca71506bd590d9ef4465258914d)qos

| struct [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md)\* bt\_iso\_chan::qos |
| --- |

Channel QoS reference.

## [◆ ](#a75347e4f16e715be06298ccf36c8521c)required\_sec\_level

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_iso\_chan::required\_sec\_level |
| --- |

The required security level of the channel.

This value can be set as the central before connecting a CIS with [bt\_iso\_chan\_connect()](group__bt__iso.md#ga98953a261f3699b62cd19ab4977e0b4c "Connect ISO channels on ACL connections."). The value is overwritten to [bt\_iso\_server::sec\_level](structbt__iso__server.md#a43b53fd63d4deaa1c5599499eec29c99 "bt_iso_server::sec_level") for the peripheral once a channel has been accepted.

Only available when `CONFIG_BT_SMP` is enabled.

## [◆ ](#a2b0fc7180d1983ee4a415c5331bed93d)state

| enum [bt\_iso\_state](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201) bt\_iso\_chan::state |
| --- |

Channel state.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan](structbt__iso__chan.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
