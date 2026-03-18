---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structintr__handle__data__t.html
original_path: doxygen/html/structintr__handle__data__t.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intr\_handle\_data\_t Struct Reference

Interrupt handler associated data structure.
[More...](#details)

`#include <[intc_esp32.h](intc__esp32_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [vector\_desc\_t](structvector__desc__t.md) \* | [vector\_desc](#a54ce22a2f0818180fbe25d0e9edf2036) |
| struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \* | [shared\_vector\_desc](#a86785e459328fac2f0758d588159bf3e) |

## Detailed Description

Interrupt handler associated data structure.

## Field Documentation

## [◆ ](#a86785e459328fac2f0758d588159bf3e)shared\_vector\_desc

| struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md)\* intr\_handle\_data\_t::shared\_vector\_desc |
| --- |

## [◆ ](#a54ce22a2f0818180fbe25d0e9edf2036)vector\_desc

| struct [vector\_desc\_t](structvector__desc__t.md)\* intr\_handle\_data\_t::vector\_desc |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/interrupt\_controller/[intc\_esp32.h](intc__esp32_8h_source.md)

- [intr\_handle\_data\_t](structintr__handle__data__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
