---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structudc__ep__stat.html
original_path: doxygen/html/structudc__ep__stat.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_ep\_stat Struct Reference

USB device controller endpoint status.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [enabled](#a448c82eb3884dba20e1bdf0980d3a2b3): 1 |
|  | Endpoint is enabled. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [halted](#af245db473a046885e4f97b00493718e2): 1 |
|  | Endpoint is halted (returning STALL PID). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data1](#a30b66675236f30c75837c446b87ced91): 1 |
|  | Last submitted PID is DATA1. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [odd](#a0a437fb1e4b9a79eea7e4c6b0316c450): 1 |
|  | If double buffering is supported, last used buffer is odd. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [busy](#ad515a667ffd705408617dd28700db1e9): 1 |
|  | Endpoint is busy. |

## Detailed Description

USB device controller endpoint status.

## Field Documentation

## [◆ ](#ad515a667ffd705408617dd28700db1e9)busy

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_stat::busy |
| --- |

Endpoint is busy.

## [◆ ](#a30b66675236f30c75837c446b87ced91)data1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_stat::data1 |
| --- |

Last submitted PID is DATA1.

## [◆ ](#a448c82eb3884dba20e1bdf0980d3a2b3)enabled

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_stat::enabled |
| --- |

Endpoint is enabled.

## [◆ ](#af245db473a046885e4f97b00493718e2)halted

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_stat::halted |
| --- |

Endpoint is halted (returning STALL PID).

## [◆ ](#a0a437fb1e4b9a79eea7e4c6b0316c450)odd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) udc\_ep\_stat::odd |
| --- |

If double buffering is supported, last used buffer is odd.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_ep\_stat](structudc__ep__stat.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
