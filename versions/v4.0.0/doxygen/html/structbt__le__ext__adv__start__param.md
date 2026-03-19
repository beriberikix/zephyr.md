---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__le__ext__adv__start__param.html
original_path: doxygen/html/structbt__le__ext__adv__start__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_ext\_adv\_start\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a80bb1ef4316dd75ea1268241333f4346) |
|  | Advertiser timeout (N \* 10 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_events](#ab45ae0bfdb144071efcc64c30648388f) |
|  | Number of advertising events. |

## Field Documentation

## [◆ ](#ab45ae0bfdb144071efcc64c30648388f)num\_events

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_ext\_adv\_start\_param::num\_events |
| --- |

Number of advertising events.

Application will be notified by the advertiser sent callback. Set to zero for no limit.

## [◆ ](#a80bb1ef4316dd75ea1268241333f4346)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_ext\_adv\_start\_param::timeout |
| --- |

Advertiser timeout (N \* 10 ms).

Application will be notified by the advertiser sent callback. Set to zero for no timeout.

When using high duty cycle directed connectable advertising then this parameters must be set to a non-zero value less than or equal to the maximum of [BT\_GAP\_ADV\_HIGH\_DUTY\_CYCLE\_MAX\_TIMEOUT](group__bt__gap__defines.md#gabe483d4dd601b11ac3eea570c962b1ec "BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT").

If privacy

```
CONFIG_BT_PRIVACY
```

is enabled then the timeout must be less than

```
CONFIG_BT_RPA_TIMEOUT
```

.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_ext\_adv\_start\_param](structbt__le__ext__adv__start__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
