---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcomp__nrf__lpcomp__config.html
original_path: doxygen/html/structcomp__nrf__lpcomp__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

comp\_nrf\_lpcomp\_config Struct Reference

Configuration structure.
[More...](#details)

`#include <[nrf_lpcomp.h](nrf__lpcomp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [comp\_nrf\_lpcomp\_psel](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582) | [psel](#aa39efb6f9cb0ad0720d04cefb4ba0513) |
|  | Positive input selection. |
| enum [comp\_nrf\_lpcomp\_extrefsel](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21) | [extrefsel](#a4b69733d3fc9a20f9958a027d3898ec3) |
|  | External reference selection. |
| enum [comp\_nrf\_lpcomp\_refsel](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04) | [refsel](#ad1022de6c772909a4f8c3d90e0748fe7) |
|  | Reference selection. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_hyst](#ac561f00056c9faabb61a4a67b628f963) |
|  | Hysteresis configuration. |

## Detailed Description

Configuration structure.

Note
:   extrefsel is only used if refsel == COMP\_NRF\_LPCOMP\_REFSEL\_AREF

## Field Documentation

## [◆ ](#ac561f00056c9faabb61a4a67b628f963)enable\_hyst

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) comp\_nrf\_lpcomp\_config::enable\_hyst |
| --- |

Hysteresis configuration.

## [◆ ](#a4b69733d3fc9a20f9958a027d3898ec3)extrefsel

| enum [comp\_nrf\_lpcomp\_extrefsel](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21) comp\_nrf\_lpcomp\_config::extrefsel |
| --- |

External reference selection.

## [◆ ](#aa39efb6f9cb0ad0720d04cefb4ba0513)psel

| enum [comp\_nrf\_lpcomp\_psel](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582) comp\_nrf\_lpcomp\_config::psel |
| --- |

Positive input selection.

## [◆ ](#ad1022de6c772909a4f8c3d90e0748fe7)refsel

| enum [comp\_nrf\_lpcomp\_refsel](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04) comp\_nrf\_lpcomp\_config::refsel |
| --- |

Reference selection.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/comparator/[nrf\_lpcomp.h](nrf__lpcomp_8h_source.md)

- [comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
