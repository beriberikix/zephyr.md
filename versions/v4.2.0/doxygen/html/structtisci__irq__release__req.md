---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__irq__release__req.html
original_path: doxygen/html/structtisci__irq__release__req.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_irq\_release\_req Struct Reference

Request to release interrupt peripheral resources.
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [valid\_params](#a068b9b4217d606f03898bdca2219bbf0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [src\_id](#adddef8e01c4ecd9b44327418bcc8a3ef) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [src\_index](#abb9cedc15e5923125e57f153ee1ed22a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst\_id](#ae646b23593b5f724fca6800c5c2e76bf) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [dst\_host\_irq](#a3643554ea453300f33806b5128cc6c0a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ia\_id](#aa6c09862a5e955a5ccbb78c7df2675fa) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vint](#a754e7c93d218a58e2bc18fd4ec086e40) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [global\_event](#a12eb81324f28254daece1170b1e6764d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [vint\_status\_bit\_index](#aedc07d5425720146b75b6757ca17c0d3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [secondary\_host](#a032e94a7d3c7384dc1f36c08b2d73e71) |

## Detailed Description

Request to release interrupt peripheral resources.

Releases interrupt peripheral resources according to the valid configuration provided.

Parameters
:   | [valid\_params](#a068b9b4217d606f03898bdca2219bbf0) | Bitfield defining validity of interrupt route release parameters. Each bit corresponds to a field's validity. |
    | --- | --- |
    | [src\_id](#adddef8e01c4ecd9b44327418bcc8a3ef) | ID of interrupt source peripheral. |
    | [src\_index](#abb9cedc15e5923125e57f153ee1ed22a) | Interrupt source index within source peripheral. |
    | [dst\_id](#ae646b23593b5f724fca6800c5c2e76bf) | SoC IR device ID (valid if TISCI\_MSG\_VALUE\_RM\_DST\_ID\_VALID is set). |
    | [dst\_host\_irq](#a3643554ea453300f33806b5128cc6c0a) | SoC IR output index (valid if TISCI\_MSG\_VALUE\_RM\_DST\_HOST\_IRQ\_VALID is set). |
    | [ia\_id](#aa6c09862a5e955a5ccbb78c7df2675fa) | Device ID of interrupt aggregator (valid if TISCI\_MSG\_VALUE\_RM\_IA\_ID\_VALID is set). |
    | [vint](#a754e7c93d218a58e2bc18fd4ec086e40) | Virtual interrupt number (valid if TISCI\_MSG\_VALUE\_RM\_VINT\_VALID is set). |
    | [global\_event](#a12eb81324f28254daece1170b1e6764d) | Global event mapped to interrupt aggregator (valid if TISCI\_MSG\_VALUE\_RM\_GLOBAL\_EVENT\_VALID is set). |
    | [vint\_status\_bit\_index](#aedc07d5425720146b75b6757ca17c0d3) | Virtual interrupt status bit (valid if TISCI\_MSG\_VALUE\_RM\_VINT\_STATUS\_BIT\_INDEX\_VALID is set). |
    | [secondary\_host](#a032e94a7d3c7384dc1f36c08b2d73e71) | Secondary host value (valid if TISCI\_MSG\_VALUE\_RM\_SECONDARY\_HOST\_VALID is set). |

## Field Documentation

## [◆ ](#a3643554ea453300f33806b5128cc6c0a)dst\_host\_irq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::dst\_host\_irq |
| --- |

## [◆ ](#ae646b23593b5f724fca6800c5c2e76bf)dst\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::dst\_id |
| --- |

## [◆ ](#a12eb81324f28254daece1170b1e6764d)global\_event

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::global\_event |
| --- |

## [◆ ](#aa6c09862a5e955a5ccbb78c7df2675fa)ia\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::ia\_id |
| --- |

## [◆ ](#a032e94a7d3c7384dc1f36c08b2d73e71)secondary\_host

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_irq\_release\_req::secondary\_host |
| --- |

## [◆ ](#adddef8e01c4ecd9b44327418bcc8a3ef)src\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::src\_id |
| --- |

## [◆ ](#abb9cedc15e5923125e57f153ee1ed22a)src\_index

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::src\_index |
| --- |

## [◆ ](#a068b9b4217d606f03898bdca2219bbf0)valid\_params

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tisci\_irq\_release\_req::valid\_params |
| --- |

## [◆ ](#a754e7c93d218a58e2bc18fd4ec086e40)vint

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_irq\_release\_req::vint |
| --- |

## [◆ ](#aedc07d5425720146b75b6757ca17c0d3)vint\_status\_bit\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_irq\_release\_req::vint\_status\_bit\_index |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_irq\_release\_req](structtisci__irq__release__req.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
