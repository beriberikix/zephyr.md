---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__bap__unicast__group__param.html
original_path: doxygen/html/structbt__bap__unicast__group__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_group\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Unicast Client APIs](group__bt__bap__unicast__client.md)

Parameters for the creating unicast groups with [bt\_bap\_unicast\_group\_create()](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21 "Create audio unicast group.").
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [params\_count](#a9cd09b720fa9a31364878ba205b3b58c) |
|  | The number of parameters in `params`. |
| struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) \* | [params](#aefae7dfccdaed2bc3f59ca63689d4f2e) |
|  | Array of stream parameters. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a6829c82346ca70772a4ab0dc93fbb88f) |
|  | Unicast Group packing mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_to\_p\_ft](#a7980c8e5c66a11507701ce2679b461ed) |
|  | Central to Peripheral flush timeout. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_to\_c\_ft](#a72e2c6dbeb7b7778f92af5cab2474a7e) |
|  | Peripheral to Central flush timeout. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#a278797713b97a6520247b01caa2938b9) |
|  | ISO interval. |

## Detailed Description

Parameters for the creating unicast groups with [bt\_bap\_unicast\_group\_create()](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21 "Create audio unicast group.").

## Field Documentation

## [◆ ](#a7980c8e5c66a11507701ce2679b461ed)c\_to\_p\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_unicast\_group\_param::c\_to\_p\_ft |
| --- |

Central to Peripheral flush timeout.

The flush timeout in multiples of ISO\_Interval for each payload sent from the Central to Peripheral.

Value range from [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98 "BT_ISO_FT_MIN") to [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e "BT_ISO_FT_MAX")

## [◆ ](#a278797713b97a6520247b01caa2938b9)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_unicast\_group\_param::iso\_interval |
| --- |

ISO interval.

Time between consecutive CIS anchor points.

Value range from [BT\_ISO\_ISO\_INTERVAL\_MIN](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de "BT_ISO_ISO_INTERVAL_MIN") to [BT\_ISO\_ISO\_INTERVAL\_MAX](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3 "BT_ISO_ISO_INTERVAL_MAX").

## [◆ ](#a72e2c6dbeb7b7778f92af5cab2474a7e)p\_to\_c\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_unicast\_group\_param::p\_to\_c\_ft |
| --- |

Peripheral to Central flush timeout.

The flush timeout in multiples of ISO\_Interval for each payload sent from the Peripheral to Central.

Value range from [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98 "BT_ISO_FT_MIN") to [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e "BT_ISO_FT_MAX").

## [◆ ](#a6829c82346ca70772a4ab0dc93fbb88f)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_unicast\_group\_param::packing |
| --- |

Unicast Group packing mode.

[BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19 "BT_ISO_PACKING_SEQUENTIAL") or [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79 "BT_ISO_PACKING_INTERLEAVED").

Note
:   This is a recommendation to the controller, which the controller may ignore.

## [◆ ](#aefae7dfccdaed2bc3f59ca63689d4f2e)params

| struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md)\* bt\_bap\_unicast\_group\_param::params |
| --- |

Array of stream parameters.

## [◆ ](#a9cd09b720fa9a31364878ba205b3b58c)params\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_bap\_unicast\_group\_param::params\_count |
| --- |

The number of parameters in `params`.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
