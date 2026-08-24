---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__cap__unicast__group__param.html
original_path: doxygen/html/structbt__cap__unicast__group__param.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cap\_unicast\_group\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Common Audio Profile (CAP)](group__bt__cap.md)

Parameters for the creating unicast groups with [bt\_cap\_unicast\_group\_create()](group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637 "Create unicast group.").
[More...](#details)

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [params\_count](#ab9748e9e230048af64ce9c9ce1006952) |
|  | The number of parameters in `params`. |
| struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) \* | [params](#a64ca2c5cc4f34821e567841ec8efe67b) |
|  | Array of stream parameters. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a97e67b903e72dd1f0fef4961810288b1) |
|  | Unicast Group packing mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_to\_p\_ft](#adb6cb5686b3d827156aef325b3dcdc84) |
|  | Central to Peripheral flush timeout. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_to\_c\_ft](#ab424be389b026ac5857e3bec1c3d686f) |
|  | Peripheral to Central flush timeout. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#ac52a0e09e3978a084e4fe558e4a5a848) |
|  | ISO interval. |

## Detailed Description

Parameters for the creating unicast groups with [bt\_cap\_unicast\_group\_create()](group__bt__cap.md#ga299ee8321aa5059e48244e1ae8080637 "Create unicast group.").

## Field Documentation

## [◆ ](#adb6cb5686b3d827156aef325b3dcdc84)c\_to\_p\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_unicast\_group\_param::c\_to\_p\_ft |
| --- |

Central to Peripheral flush timeout.

The flush timeout in multiples of ISO\_Interval for each payload sent from the Central to Peripheral.

Value range from [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98 "BT_ISO_FT_MIN") to [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e "BT_ISO_FT_MAX")

## [◆ ](#ac52a0e09e3978a084e4fe558e4a5a848)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_cap\_unicast\_group\_param::iso\_interval |
| --- |

ISO interval.

Time between consecutive CIS anchor points.

Value range from [BT\_ISO\_ISO\_INTERVAL\_MIN](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de "BT_ISO_ISO_INTERVAL_MIN") to [BT\_ISO\_ISO\_INTERVAL\_MAX](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3 "BT_ISO_ISO_INTERVAL_MAX").

## [◆ ](#ab424be389b026ac5857e3bec1c3d686f)p\_to\_c\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_unicast\_group\_param::p\_to\_c\_ft |
| --- |

Peripheral to Central flush timeout.

The flush timeout in multiples of ISO\_Interval for each payload sent from the Peripheral to Central.

Value range from [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98 "BT_ISO_FT_MIN") to [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e "BT_ISO_FT_MAX").

## [◆ ](#a97e67b903e72dd1f0fef4961810288b1)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_cap\_unicast\_group\_param::packing |
| --- |

Unicast Group packing mode.

[BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19 "BT_ISO_PACKING_SEQUENTIAL") or [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79 "BT_ISO_PACKING_INTERLEAVED").

Note
:   This is a recommendation to the controller, which the controller may ignore.

## [◆ ](#a64ca2c5cc4f34821e567841ec8efe67b)params

| struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md)\* bt\_cap\_unicast\_group\_param::params |
| --- |

Array of stream parameters.

## [◆ ](#ab9748e9e230048af64ce9c9ce1006952)params\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_cap\_unicast\_group\_param::params\_count |
| --- |

The number of parameters in `params`.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[cap.h](bluetooth_2audio_2cap_8h_source.md)

- [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
