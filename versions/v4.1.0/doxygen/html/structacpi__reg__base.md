---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structacpi__reg__base.html
original_path: doxygen/html/structacpi__reg__base.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

acpi\_reg\_base Struct Reference

`#include <[acpi.h](acpi_2acpi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [acpi\_res\_type](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5b) | [type](#a416f2ff166b33add65eba5e7787c3ef5) |
| union { |  |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)   [mmio](#ada6ffb943e406068271d56b5a129b717) |  |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)   [port](#ab845df09e3b4b9734103605ea7c65d1e) |  |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [length](#aaca25908e4e16a71627c48208c55d0ef) |

## Field Documentation

## [◆ ](#ad56cc48ac58fbc87410fe2960192cbac)[union]

| union { ... } [acpi\_reg\_base](structacpi__reg__base.md) |
| --- |

## [◆ ](#aaca25908e4e16a71627c48208c55d0ef)length

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) acpi\_reg\_base::length |
| --- |

## [◆ ](#ada6ffb943e406068271d56b5a129b717)mmio

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) acpi\_reg\_base::mmio |
| --- |

## [◆ ](#ab845df09e3b4b9734103605ea7c65d1e)port

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) acpi\_reg\_base::port |
| --- |

## [◆ ](#a416f2ff166b33add65eba5e7787c3ef5)type

| enum [acpi\_res\_type](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5b) acpi\_reg\_base::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/acpi/[acpi.h](acpi_2acpi_8h_source.md)

- [acpi\_reg\_base](structacpi__reg__base.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
