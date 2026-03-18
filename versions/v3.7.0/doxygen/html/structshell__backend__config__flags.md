---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__backend__config__flags.html
original_path: doxygen/html/structshell__backend__config__flags.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_backend\_config\_flags Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [insert\_mode](#ab1df6f41078d4ec2a94f158e62bbfada):1 |
|  | Controls insert mode for text introduction. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [echo](#a5745ea5cab202ee446f460b980c5c532):1 |
|  | Controls shell echo. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [obscure](#af794ac9c19b948ed733024a2db5b8bbd):1 |
|  | If echo on, print asterisk instead. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mode\_delete](#a231bc4762cac1c07a6f866c5ecf3a024):1 |
|  | Operation mode of backspace key. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [use\_colors](#af810ff3fba00527cb0561a75b70fec09):1 |
|  | Controls colored syntax. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [use\_vt100](#a0d017df8e9d9609f2830829d8720b9cf):1 |
|  | Controls VT100 commands usage in shell. |

## Field Documentation

## [◆ ](#a5745ea5cab202ee446f460b980c5c532)echo

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_config\_flags::echo |
| --- |

Controls shell echo.

## [◆ ](#ab1df6f41078d4ec2a94f158e62bbfada)insert\_mode

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_config\_flags::insert\_mode |
| --- |

Controls insert mode for text introduction.

## [◆ ](#a231bc4762cac1c07a6f866c5ecf3a024)mode\_delete

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_config\_flags::mode\_delete |
| --- |

Operation mode of backspace key.

## [◆ ](#af794ac9c19b948ed733024a2db5b8bbd)obscure

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_config\_flags::obscure |
| --- |

If echo on, print asterisk instead.

## [◆ ](#af810ff3fba00527cb0561a75b70fec09)use\_colors

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_config\_flags::use\_colors |
| --- |

Controls colored syntax.

## [◆ ](#a0d017df8e9d9609f2830829d8720b9cf)use\_vt100

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_config\_flags::use\_vt100 |
| --- |

Controls VT100 commands usage in shell.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_backend\_config\_flags](structshell__backend__config__flags.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
