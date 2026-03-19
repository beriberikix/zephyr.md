---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__ots__client.html
original_path: doxygen/html/structbt__ots__client.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ots\_client Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Object Transfer Service (OTS)](group__bt__ots.md)

OTS client instance.
[More...](#details)

`#include <[ots.h](ots_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_handle](#a39818a4d776056212e82c4ba0626d0f1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [end\_handle](#a99727a6d064d79c3078a04b1d6d046db) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [feature\_handle](#a65608146d1a3e141635a015eb5092ab1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_name\_handle](#ae902c29051540141852869dd94edf7e0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_type\_handle](#ae2eebd727fd908ef2b2074c9c0b2ab4f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_size\_handle](#a83c5d653692dc3d7dbcfd5c8e2361f96) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_properties\_handle](#aabd4a625a341b4f7bdcdcff03e7ae76f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_created\_handle](#aff756cfa5f9431ed288563a95877cb53) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_modified\_handle](#a83cf53f6f7737620ea39dccbebe26dd4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [obj\_id\_handle](#a6ff62fb7570269358888c9ab865a5ec6) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [oacp\_handle](#ad56aaee2630d75a1bb5faf0f56486c0a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [olcp\_handle](#aa98ae5a468c46f1ffbfd08a6e82f420d) |
| struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) | [oacp\_sub\_params](#a98a75a8ed52a2b97be1ea273a21b8775) |
| struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) | [oacp\_sub\_disc\_params](#a8913d240d90b77ea72612ddbf816f528) |
| struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) | [olcp\_sub\_params](#a787b4851389e5da47a93969db6b3edcf) |
| struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) | [olcp\_sub\_disc\_params](#acbee05e7b1cd5c325a6982c6b32a732d) |
| struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) | [write\_params](#a0e6a0d97a1b8edc7a282aec12d95b0dc) |
| struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) | [read\_proc](#a87d273e283941a3b9f1402e2b514134b) |
| struct [bt\_ots\_client\_cb](structbt__ots__client__cb.md) \* | [cb](#a3aded7f58deb7f13c1c5adaa073f45f8) |
| struct [bt\_ots\_feat](structbt__ots__feat.md) | [features](#a8a6d138d506a5e2732f4c51971533ce9) |
| struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) | [cur\_object](#ac0fac55db40bf66aff358ce906fc8172) |

## Detailed Description

OTS client instance.

## Field Documentation

## [◆ ](#a3aded7f58deb7f13c1c5adaa073f45f8)cb

| struct [bt\_ots\_client\_cb](structbt__ots__client__cb.md)\* bt\_ots\_client::cb |
| --- |

## [◆ ](#ac0fac55db40bf66aff358ce906fc8172)cur\_object

| struct [bt\_ots\_obj\_metadata](structbt__ots__obj__metadata.md) bt\_ots\_client::cur\_object |
| --- |

## [◆ ](#a99727a6d064d79c3078a04b1d6d046db)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::end\_handle |
| --- |

## [◆ ](#a65608146d1a3e141635a015eb5092ab1)feature\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::feature\_handle |
| --- |

## [◆ ](#a8a6d138d506a5e2732f4c51971533ce9)features

| struct [bt\_ots\_feat](structbt__ots__feat.md) bt\_ots\_client::features |
| --- |

## [◆ ](#ad56aaee2630d75a1bb5faf0f56486c0a)oacp\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::oacp\_handle |
| --- |

## [◆ ](#a8913d240d90b77ea72612ddbf816f528)oacp\_sub\_disc\_params

| struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) bt\_ots\_client::oacp\_sub\_disc\_params |
| --- |

## [◆ ](#a98a75a8ed52a2b97be1ea273a21b8775)oacp\_sub\_params

| struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) bt\_ots\_client::oacp\_sub\_params |
| --- |

## [◆ ](#aff756cfa5f9431ed288563a95877cb53)obj\_created\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_created\_handle |
| --- |

## [◆ ](#a6ff62fb7570269358888c9ab865a5ec6)obj\_id\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_id\_handle |
| --- |

## [◆ ](#a83cf53f6f7737620ea39dccbebe26dd4)obj\_modified\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_modified\_handle |
| --- |

## [◆ ](#ae902c29051540141852869dd94edf7e0)obj\_name\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_name\_handle |
| --- |

## [◆ ](#aabd4a625a341b4f7bdcdcff03e7ae76f)obj\_properties\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_properties\_handle |
| --- |

## [◆ ](#a83c5d653692dc3d7dbcfd5c8e2361f96)obj\_size\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_size\_handle |
| --- |

## [◆ ](#ae2eebd727fd908ef2b2074c9c0b2ab4f)obj\_type\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::obj\_type\_handle |
| --- |

## [◆ ](#aa98ae5a468c46f1ffbfd08a6e82f420d)olcp\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::olcp\_handle |
| --- |

## [◆ ](#acbee05e7b1cd5c325a6982c6b32a732d)olcp\_sub\_disc\_params

| struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) bt\_ots\_client::olcp\_sub\_disc\_params |
| --- |

## [◆ ](#a787b4851389e5da47a93969db6b3edcf)olcp\_sub\_params

| struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) bt\_ots\_client::olcp\_sub\_params |
| --- |

## [◆ ](#a87d273e283941a3b9f1402e2b514134b)read\_proc

| struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) bt\_ots\_client::read\_proc |
| --- |

## [◆ ](#a39818a4d776056212e82c4ba0626d0f1)start\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_ots\_client::start\_handle |
| --- |

## [◆ ](#a0e6a0d97a1b8edc7a282aec12d95b0dc)write\_params

| struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) bt\_ots\_client::write\_params |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ots.h](ots_8h_source.md)

- [bt\_ots\_client](structbt__ots__client.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
