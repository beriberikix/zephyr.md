---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structcurrent__sense__amplifier__dt__spec.html
original_path: doxygen/html/structcurrent__sense__amplifier__dt__spec.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

current\_sense\_amplifier\_dt\_spec Struct Reference

`#include <[zephyr/drivers/adc/current_sense_amplifier.h](current__sense__amplifier_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [adc\_dt\_spec](structadc__dt__spec.md) | [port](#aed51d08ce3824d91f31b7ad64926c667) |
| struct [gpio\_dt\_spec](structgpio__dt__spec.md) | [power\_gpio](#af35fab6c94e4d95ba850e8ba2e4a0961) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sense\_milli\_ohms](#ad6efaf2c197a7ca3db1085aa900aed23) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sense\_gain\_mult](#a8c7af3b111721f0b654a3943670c5614) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sense\_gain\_div](#a3f94f49afc001c36ed42ae640bb7b157) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [noise\_threshold](#a140af0a4a6bcf73149dc7eec69b87e7b) |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [zero\_current\_voltage\_mv](#a4f1e3b2bba6178fa5d36f1d734ce1111) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_calibration](#a37f6a98c94ec822854608fef74df8ee7) |

## Field Documentation

## [◆ ](#a37f6a98c94ec822854608fef74df8ee7)enable\_calibration

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) current\_sense\_amplifier\_dt\_spec::enable\_calibration |
| --- |

## [◆ ](#a140af0a4a6bcf73149dc7eec69b87e7b)noise\_threshold

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) current\_sense\_amplifier\_dt\_spec::noise\_threshold |
| --- |

## [◆ ](#aed51d08ce3824d91f31b7ad64926c667)port

| struct [adc\_dt\_spec](structadc__dt__spec.md) current\_sense\_amplifier\_dt\_spec::port |
| --- |

## [◆ ](#af35fab6c94e4d95ba850e8ba2e4a0961)power\_gpio

| struct [gpio\_dt\_spec](structgpio__dt__spec.md) current\_sense\_amplifier\_dt\_spec::power\_gpio |
| --- |

## [◆ ](#a3f94f49afc001c36ed42ae640bb7b157)sense\_gain\_div

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) current\_sense\_amplifier\_dt\_spec::sense\_gain\_div |
| --- |

## [◆ ](#a8c7af3b111721f0b654a3943670c5614)sense\_gain\_mult

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) current\_sense\_amplifier\_dt\_spec::sense\_gain\_mult |
| --- |

## [◆ ](#ad6efaf2c197a7ca3db1085aa900aed23)sense\_milli\_ohms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) current\_sense\_amplifier\_dt\_spec::sense\_milli\_ohms |
| --- |

## [◆ ](#a4f1e3b2bba6178fa5d36f1d734ce1111)zero\_current\_voltage\_mv

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) current\_sense\_amplifier\_dt\_spec::zero\_current\_voltage\_mv |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/adc/[current\_sense\_amplifier.h](current__sense__amplifier_8h_source.md)

- [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
