---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__unicast__group__param.html
original_path: doxygen/html/structbt__bap__unicast__group__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_group\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Unicast Client APIs](group__bt__bap__unicast__client.md)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [params\_count](#a9cd09b720fa9a31364878ba205b3b58c) |
|  | The number of parameters in `params`. |
| struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) \* | [params](#aefae7dfccdaed2bc3f59ca63689d4f2e) |
|  | Array of stream parameters. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a6829c82346ca70772a4ab0dc93fbb88f) |
|  | Unicast Group packing mode. |

## Field Documentation

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
