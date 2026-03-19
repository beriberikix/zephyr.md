---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcomp__nrf__comp__diff__config.html
original_path: doxygen/html/structcomp__nrf__comp__diff__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

comp\_nrf\_comp\_diff\_config Struct Reference

Differential mode configuration structure.
[More...](#details)

`#include <[nrf_comp.h](nrf__comp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) | [psel](#ae3807c40d36de257f2bae07787cc6cd7) |
|  | Positive input selection. |
| enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) | [sp\_mode](#a9a9b95f993a1a193292eb940c0550e1f) |
|  | Speed mode selection. |
| enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) | [isource](#ac1aada8c9bceab130cd6ffdf294ce52f) |
|  | Current source configuration. |
| enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) | [extrefsel](#a9ea88f6afb084054ad8579d32b2ed947) |
|  | Negative input selection. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_hyst](#ae597d46f83c77923541e73cf254bc4ee) |
|  | Hysteresis configuration. |

## Detailed Description

Differential mode configuration structure.

## Field Documentation

## [◆ ](#ae597d46f83c77923541e73cf254bc4ee)enable\_hyst

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) comp\_nrf\_comp\_diff\_config::enable\_hyst |
| --- |

Hysteresis configuration.

## [◆ ](#a9ea88f6afb084054ad8579d32b2ed947)extrefsel

| enum [comp\_nrf\_comp\_extrefsel](nrf__comp_8h.md#a3f3b16a44f7144021081965686af2270) comp\_nrf\_comp\_diff\_config::extrefsel |
| --- |

Negative input selection.

## [◆ ](#ac1aada8c9bceab130cd6ffdf294ce52f)isource

| enum [comp\_nrf\_comp\_isource](nrf__comp_8h.md#a74444aeafb5a2bf633ffd706cc6b9010) comp\_nrf\_comp\_diff\_config::isource |
| --- |

Current source configuration.

## [◆ ](#ae3807c40d36de257f2bae07787cc6cd7)psel

| enum [comp\_nrf\_comp\_psel](nrf__comp_8h.md#a939aadd5e7172aa0b5e128c1aaf9d9bd) comp\_nrf\_comp\_diff\_config::psel |
| --- |

Positive input selection.

## [◆ ](#a9a9b95f993a1a193292eb940c0550e1f)sp\_mode

| enum [comp\_nrf\_comp\_sp\_mode](nrf__comp_8h.md#ad13baf7c262d5fb2321ea5140180b3b1) comp\_nrf\_comp\_diff\_config::sp\_mode |
| --- |

Speed mode selection.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/comparator/[nrf\_comp.h](nrf__comp_8h_source.md)

- [comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
