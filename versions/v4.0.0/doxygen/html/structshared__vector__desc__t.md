---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structshared__vector__desc__t.html
original_path: doxygen/html/structshared__vector__desc__t.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_vector\_desc\_t Struct Reference

`#include <[intc_esp32.h](intc__esp32_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [disabled](#a36afb23eff0489280549ac96fea0ee41): 1 |
| int | [source](#af868d1b2bf579938907ef07f5b15d517): 8 |
| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [statusreg](#acb593daeddd30515742759a73fc7838f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [statusmask](#a9078649e1b33c0ad3ee624789fda95cb) |
| [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) | [isr](#aa438daab7ce59980b664824142be8f84) |
| void \* | [arg](#a4ab5f28adbb5115ca6a37a3ab6c5328e) |
| struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \* | [next](#aee24289457fcde842c2b557bce5cd605) |

## Field Documentation

## [◆ ](#a4ab5f28adbb5115ca6a37a3ab6c5328e)arg

| void\* shared\_vector\_desc\_t::arg |
| --- |

## [◆ ](#a36afb23eff0489280549ac96fea0ee41)disabled

| int shared\_vector\_desc\_t::disabled |
| --- |

## [◆ ](#aa438daab7ce59980b664824142be8f84)isr

| [intr\_handler\_t](intc__esp32_8h.md#a637aa0db4839d3e945e74c56e82218f2) shared\_vector\_desc\_t::isr |
| --- |

## [◆ ](#aee24289457fcde842c2b557bce5cd605)next

| struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md)\* shared\_vector\_desc\_t::next |
| --- |

## [◆ ](#af868d1b2bf579938907ef07f5b15d517)source

| int shared\_vector\_desc\_t::source |
| --- |

## [◆ ](#a9078649e1b33c0ad3ee624789fda95cb)statusmask

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shared\_vector\_desc\_t::statusmask |
| --- |

## [◆ ](#acb593daeddd30515742759a73fc7838f)statusreg

| volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* shared\_vector\_desc\_t::statusreg |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/interrupt\_controller/[intc\_esp32.h](intc__esp32_8h_source.md)

- [shared\_vector\_desc\_t](structshared__vector__desc__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
