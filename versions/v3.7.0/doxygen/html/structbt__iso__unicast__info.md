---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__iso__unicast__info.html
original_path: doxygen/html/structbt__iso__unicast__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_unicast\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Unicast Info Structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cig\_sync\_delay](#a029c450e2324bbc6ee8fda6d1d10deef) |
|  | The maximum time in us for all PDUs of all CIS in a CIG event. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cis\_sync\_delay](#acbc8c068907eba204d369cf76f4f112d) |
|  | The maximum time in us for all PDUs of this CIS in a CIG event. |
| struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) | [central](#a4fc402b934ae8aa65493df01c88cae34) |
|  | TX information for the central to peripheral data path. |
| struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) | [peripheral](#a03b084fefcab049efbe1a609a59d9c54) |
|  | TX information for the peripheral to central data. |

## Detailed Description

ISO Unicast Info Structure.

## Field Documentation

## [◆ ](#a4fc402b934ae8aa65493df01c88cae34)central

| struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) bt\_iso\_unicast\_info::central |
| --- |

TX information for the central to peripheral data path.

## [◆ ](#a029c450e2324bbc6ee8fda6d1d10deef)cig\_sync\_delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_unicast\_info::cig\_sync\_delay |
| --- |

The maximum time in us for all PDUs of all CIS in a CIG event.

## [◆ ](#acbc8c068907eba204d369cf76f4f112d)cis\_sync\_delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_unicast\_info::cis\_sync\_delay |
| --- |

The maximum time in us for all PDUs of this CIS in a CIG event.

## [◆ ](#a03b084fefcab049efbe1a609a59d9c54)peripheral

| struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) bt\_iso\_unicast\_info::peripheral |
| --- |

TX information for the peripheral to central data.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_unicast\_info](structbt__iso__unicast__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
