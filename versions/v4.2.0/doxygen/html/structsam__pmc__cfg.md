---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structsam__pmc__cfg.html
original_path: doxygen/html/structsam__pmc__cfg.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sam\_pmc\_cfg Struct Reference

`#include <[zephyr/drivers/clock_control/mchp_sam_pmc.h](mchp__sam__pmc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const | [reg](#aa2584519cb128e96715a6a01140f609c) |
| const struct [device](structdevice.md) \* | [td\_slck](#a0fc5ba6ce43a1f7b91d854ace83f59df) |
| const struct [device](structdevice.md) \* | [md\_slck](#abd4cbbd2082fe579bc6edd3d4548f390) |
| const struct [device](structdevice.md) \* | [main\_xtal](#a8459cfb8ca7a99416e0c2e5e9a680481) |
| const struct [sam\_sckc\_config](structsam__sckc__config.md) | [td\_slck\_cfg](#a3029662f9fa5ca96c142a9564c44f4d2) |
| const struct [sam\_sckc\_config](structsam__sckc__config.md) | [md\_slck\_cfg](#a149d058d1170af8eb75628dfd6b9cc92) |

## Field Documentation

## [◆ ](#a8459cfb8ca7a99416e0c2e5e9a680481)main\_xtal

| const struct [device](structdevice.md)\* sam\_pmc\_cfg::main\_xtal |
| --- |

## [◆ ](#abd4cbbd2082fe579bc6edd3d4548f390)md\_slck

| const struct [device](structdevice.md)\* sam\_pmc\_cfg::md\_slck |
| --- |

## [◆ ](#a149d058d1170af8eb75628dfd6b9cc92)md\_slck\_cfg

| const struct [sam\_sckc\_config](structsam__sckc__config.md) sam\_pmc\_cfg::md\_slck\_cfg |
| --- |

## [◆ ](#aa2584519cb128e96715a6a01140f609c)reg

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* const sam\_pmc\_cfg::reg |
| --- |

## [◆ ](#a0fc5ba6ce43a1f7b91d854ace83f59df)td\_slck

| const struct [device](structdevice.md)\* sam\_pmc\_cfg::td\_slck |
| --- |

## [◆ ](#a3029662f9fa5ca96c142a9564c44f4d2)td\_slck\_cfg

| const struct [sam\_sckc\_config](structsam__sckc__config.md) sam\_pmc\_cfg::td\_slck\_cfg |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/clock\_control/[mchp\_sam\_pmc.h](mchp__sam__pmc_8h_source.md)

- [sam\_pmc\_cfg](structsam__pmc__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
