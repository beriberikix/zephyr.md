---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structshell__backend__ctx__flags.html
original_path: doxygen/html/structshell__backend__ctx__flags.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_backend\_ctx\_flags Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [processing](#a7dc2cd17fb1dd9d538dbde3ad7bbe8e9):1 |
|  | Shell is executing process function. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_rdy](#a662cf22a29856d07ec64b72db004582f):1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [history\_exit](#a85b0069c7b0df219cefec0f73cb313d3):1 |
|  | Request to exit history mode. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [last\_nl](#a7f597db455b0875c9ff11c4ce50cfd92):8 |
|  | Last received new line character. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cmd\_ctx](#adfa22b07dc65e72e24be400d95da11c8):1 |
|  | Shell is executing command. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [print\_noinit](#a18b3c018f2da6a925f50266bda095483):1 |
|  | Print request from not initialized shell. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sync\_mode](#a2d6c2561aa6ed28a3978e3b70d079008):1 |
|  | Shell in synchronous mode. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [handle\_log](#a735602bed33c01e8e548200656fd7ff4):1 |
|  | Shell is handling logger backend. |

## Field Documentation

## [◆ ](#adfa22b07dc65e72e24be400d95da11c8)cmd\_ctx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::cmd\_ctx |
| --- |

Shell is executing command.

## [◆ ](#a735602bed33c01e8e548200656fd7ff4)handle\_log

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::handle\_log |
| --- |

Shell is handling logger backend.

## [◆ ](#a85b0069c7b0df219cefec0f73cb313d3)history\_exit

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::history\_exit |
| --- |

Request to exit history mode.

## [◆ ](#a7f597db455b0875c9ff11c4ce50cfd92)last\_nl

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::last\_nl |
| --- |

Last received new line character.

## [◆ ](#a18b3c018f2da6a925f50266bda095483)print\_noinit

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::print\_noinit |
| --- |

Print request from not initialized shell.

## [◆ ](#a7dc2cd17fb1dd9d538dbde3ad7bbe8e9)processing

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::processing |
| --- |

Shell is executing process function.

## [◆ ](#a2d6c2561aa6ed28a3978e3b70d079008)sync\_mode

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::sync\_mode |
| --- |

Shell in synchronous mode.

## [◆ ](#a662cf22a29856d07ec64b72db004582f)tx\_rdy

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shell\_backend\_ctx\_flags::tx\_rdy |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_backend\_ctx\_flags](structshell__backend__ctx__flags.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
