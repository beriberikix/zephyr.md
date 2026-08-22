---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__irq__set__req.html
original_path: doxygen/html/structtisci__irq__set__req.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_irq\_set\_req Struct Reference

Request to set up an interrupt route.
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [valid\_params](#ac5dddf4f1bc933e82eb7dfdfdfb35307) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [src\_id](#af1c6cc734902f14d51ff46c971c1a576) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [src\_index](#a290247006f410254d3a4dbcdefc0ba75) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst\_id](#a2a17ba4d83290d1ca8ae8bf39760a31a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst\_host\_irq](#a1b01430d7e9140891589f0e48e79590a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ia\_id](#a2b8fd0bc0825d47fba8c961f68fcaef4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vint](#a2e3dd0054d9d0b029a6821f4df0af4ea) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [global\_event](#ab5f9849aef439771e81daf6a98303d17) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [vint\_status\_bit\_index](#a94ad73384be1f64054829a32ad70b066) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [secondary\_host](#ad122a8cf2af3f3df9615c3ca70ed3b06) |

## Detailed Description

Request to set up an interrupt route.

Configures peripherals within the interrupt subsystem according to the valid configuration provided.

Parameters
:   | [valid\_params](#ac5dddf4f1bc933e82eb7dfdfdfb35307) | Bitfield defining validity of interrupt route set parameters. Each bit corresponds to a field's validity. |
    | --- | --- |
    | [src\_id](#af1c6cc734902f14d51ff46c971c1a576) | ID of interrupt source peripheral. |
    | [src\_index](#a290247006f410254d3a4dbcdefc0ba75) | Interrupt source index within source peripheral. |
    | [dst\_id](#a2a17ba4d83290d1ca8ae8bf39760a31a) | SoC IR device ID (valid if TISCI\_MSG\_VALUE\_RM\_DST\_ID\_VALID is set). |
    | [dst\_host\_irq](#a1b01430d7e9140891589f0e48e79590a) | SoC IR output index (valid if TISCI\_MSG\_VALUE\_RM\_DST\_HOST\_IRQ\_VALID is set). |
    | [ia\_id](#a2b8fd0bc0825d47fba8c961f68fcaef4) | Device ID of interrupt aggregator (valid if TISCI\_MSG\_VALUE\_RM\_IA\_ID\_VALID is set). |
    | [vint](#a2e3dd0054d9d0b029a6821f4df0af4ea) | Virtual interrupt number (valid if TISCI\_MSG\_VALUE\_RM\_VINT\_VALID is set). |
    | [global\_event](#ab5f9849aef439771e81daf6a98303d17) | Global event mapped to interrupt aggregator (valid if TISCI\_MSG\_VALUE\_RM\_GLOBAL\_EVENT\_VALID is set). |
    | [vint\_status\_bit\_index](#a94ad73384be1f64054829a32ad70b066) | Virtual interrupt status bit (valid if TISCI\_MSG\_VALUE\_RM\_VINT\_STATUS\_BIT\_INDEX\_VALID is set). |
    | [secondary\_host](#ad122a8cf2af3f3df9615c3ca70ed3b06) | Secondary host value (valid if TISCI\_MSG\_VALUE\_RM\_SECONDARY\_HOST\_VALID is set). |

## Field Documentation

## [◆ ](#a1b01430d7e9140891589f0e48e79590a)dst\_host\_irq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::dst\_host\_irq |
| --- |

## [◆ ](#a2a17ba4d83290d1ca8ae8bf39760a31a)dst\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::dst\_id |
| --- |

## [◆ ](#ab5f9849aef439771e81daf6a98303d17)global\_event

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::global\_event |
| --- |

## [◆ ](#a2b8fd0bc0825d47fba8c961f68fcaef4)ia\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::ia\_id |
| --- |

## [◆ ](#ad122a8cf2af3f3df9615c3ca70ed3b06)secondary\_host

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_irq\_set\_req::secondary\_host |
| --- |

## [◆ ](#af1c6cc734902f14d51ff46c971c1a576)src\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::src\_id |
| --- |

## [◆ ](#a290247006f410254d3a4dbcdefc0ba75)src\_index

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::src\_index |
| --- |

## [◆ ](#ac5dddf4f1bc933e82eb7dfdfdfb35307)valid\_params

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tisci\_irq\_set\_req::valid\_params |
| --- |

## [◆ ](#a2e3dd0054d9d0b029a6821f4df0af4ea)vint

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_set\_req::vint |
| --- |

## [◆ ](#a94ad73384be1f64054829a32ad70b066)vint\_status\_bit\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_irq\_set\_req::vint\_status\_bit\_index |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_irq\_set\_req](structtisci__irq__set__req.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
