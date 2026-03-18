---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpfc__bias__reg.html
original_path: doxygen/html/structpfc__bias__reg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pfc\_bias\_reg Struct Reference

`#include <[pinctrl_rcar_common.h](pinctrl__rcar__common_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [puen](#af52bea8a971a9d529b88de56a96ba2f6) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pud](#ad5b3f9a184e18852279224bc8bd410f1) |
|  | Pull-enable or pull-up control register. |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pins](#ab3762934173a1c25c7c31ed04694d276) [32] |
|  | Pull-up/down or pull-down control register. |

## Field Documentation

## [◆ ](#ab3762934173a1c25c7c31ed04694d276)pins

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pfc\_bias\_reg::pins[32] |
| --- |

Pull-up/down or pull-down control register.

## [◆ ](#ad5b3f9a184e18852279224bc8bd410f1)pud

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pfc\_bias\_reg::pud |
| --- |

Pull-enable or pull-up control register.

## [◆ ](#af52bea8a971a9d529b88de56a96ba2f6)puen

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pfc\_bias\_reg::puen |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/pinctrl/[pinctrl\_rcar\_common.h](pinctrl__rcar__common_8h_source.md)

- [pfc\_bias\_reg](structpfc__bias__reg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
