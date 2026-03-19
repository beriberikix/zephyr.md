---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcomp__nrf__comp__se__config.html
original_path: doxygen/html/structcomp__nrf__comp__se__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

comp\_nrf\_comp\_se\_config Struct Reference

Single-ended mode configuration structure.
[More...](#details)

`#include <[nrf_comp.h](nrf__comp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) | [psel](#ab8508ca57b1a7e3b4c129a6f16a26342) |
|  | Positive input selection. |
| enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) | [sp\_mode](#a484cc2b4c38c7b5a8c05e87e560c7b5e) |
|  | Speed mode selection. |
| enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) | [isource](#a3ffb95afd621727dedbc617e3072cfd9) |
|  | Current source configuration. |
| enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) | [extrefsel](#a48c793942f10f04ec6fa8ea54ae9f8ac) |
|  | External reference selection. |
| enum [comp\_nrf\_comp\_refsel](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553) | [refsel](#a3a7c4e624cb7e34624732dbe4b5ab4f8) |
|  | Reference selection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [th\_down](#ad4c0e1711565c3bd05c08a6eaf593aad) |
|  | Hysteresis down threshold configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [th\_up](#a72dcaac8a0508b8859397b7926238112) |
|  | Hysteresis up threshold configuration. |

## Detailed Description

Single-ended mode configuration structure.

Note
:   extrefsel is only used if refsel == COMP\_NRF\_COMP\_REFSEL\_AREF
:   Hysteresis down in volts = ((th\_down + 1) / 64) \* ref
:   Hysteresis up in volts = ((th\_up + 1) / 64) \* ref

## Field Documentation

## [◆ ](#a48c793942f10f04ec6fa8ea54ae9f8ac)extrefsel

| enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) comp\_nrf\_comp\_se\_config::extrefsel |
| --- |

External reference selection.

## [◆ ](#a3ffb95afd621727dedbc617e3072cfd9)isource

| enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) comp\_nrf\_comp\_se\_config::isource |
| --- |

Current source configuration.

## [◆ ](#ab8508ca57b1a7e3b4c129a6f16a26342)psel

| enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) comp\_nrf\_comp\_se\_config::psel |
| --- |

Positive input selection.

## [◆ ](#a3a7c4e624cb7e34624732dbe4b5ab4f8)refsel

| enum [comp\_nrf\_comp\_refsel](nrf__comp_8h.md#a661d2e37c4acd5551b77e5bf2437b553) comp\_nrf\_comp\_se\_config::refsel |
| --- |

Reference selection.

## [◆ ](#a484cc2b4c38c7b5a8c05e87e560c7b5e)sp\_mode

| enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) comp\_nrf\_comp\_se\_config::sp\_mode |
| --- |

Speed mode selection.

## [◆ ](#ad4c0e1711565c3bd05c08a6eaf593aad)th\_down

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) comp\_nrf\_comp\_se\_config::th\_down |
| --- |

Hysteresis down threshold configuration.

## [◆ ](#a72dcaac8a0508b8859397b7926238112)th\_up

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) comp\_nrf\_comp\_se\_config::th\_up |
| --- |

Hysteresis up threshold configuration.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/comparator/[nrf\_comp.h](nrf__comp_8h_source.md)

- [comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
