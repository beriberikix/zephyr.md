---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcurrent__sense__amplifier__dt__spec.html
original_path: doxygen/html/structcurrent__sense__amplifier__dt__spec.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

current\_sense\_amplifier\_dt\_spec Struct Reference

`#include <[current_sense_amplifier.h](current__sense__amplifier_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [adc\_dt\_spec](structadc__dt__spec.md) | [port](#a98bdc38aeb90906cf2536408ba90aa7e) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sense\_micro\_ohms](#ad1af3e088bcdff151b4fc1a71fadf58f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sense\_gain\_mult](#aa0b6eecdad6c809ff548d21f0626a5ff) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sense\_gain\_div](#a1b1a7e7558ad17b5fb55c48a30de6a1c) |
| struct [gpio\_dt\_spec](structgpio__dt__spec.md) | [power\_gpio](#af35fab6c94e4d95ba850e8ba2e4a0961) |

## Field Documentation

## [◆ ](#a98bdc38aeb90906cf2536408ba90aa7e)port

| const struct [adc\_dt\_spec](structadc__dt__spec.md) current\_sense\_amplifier\_dt\_spec::port |
| --- |

## [◆ ](#af35fab6c94e4d95ba850e8ba2e4a0961)power\_gpio

| struct [gpio\_dt\_spec](structgpio__dt__spec.md) current\_sense\_amplifier\_dt\_spec::power\_gpio |
| --- |

## [◆ ](#a1b1a7e7558ad17b5fb55c48a30de6a1c)sense\_gain\_div

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) current\_sense\_amplifier\_dt\_spec::sense\_gain\_div |
| --- |

## [◆ ](#aa0b6eecdad6c809ff548d21f0626a5ff)sense\_gain\_mult

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) current\_sense\_amplifier\_dt\_spec::sense\_gain\_mult |
| --- |

## [◆ ](#ad1af3e088bcdff151b4fc1a71fadf58f)sense\_micro\_ohms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) current\_sense\_amplifier\_dt\_spec::sense\_micro\_ohms |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/adc/[current\_sense\_amplifier.h](current__sense__amplifier_8h_source.md)

- [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
