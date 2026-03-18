---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmodem__chat__match.html
original_path: doxygen/html/structmodem__chat__match.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_chat\_match Struct Reference

Modem chat match.
[More...](#details)

`#include <[chat.h](chat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [match](#ad1bed20d70285a465663d9babc3fb3e2) |
|  | Match array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [match\_size](#afe00a3c87a68d9f7f889f7a0d3cc4150) |
|  | Size of match. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [separators](#a7fd423890bea11c65f326ace831233fc) |
|  | Separators array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [separators\_size](#a7c80555e1bf33504cef7be6c0f9db383) |
|  | Size of separators array. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [wildcards](#a0e08870ad8dd3b781b8f20ed5fb230ca): 1 |
|  | Set if modem chat instance shall use wildcards when matching. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [partial](#aeb52b41db39ac21f5991524add42f8e3): 1 |
|  | Set if script shall not continue to next step in case of match. |
| [modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd) | [callback](#a11f6e35cd2fd2166ac95adace6ec5c54) |
|  | Type of modem chat instance. |

## Detailed Description

Modem chat match.

## Field Documentation

## [◆ ](#a11f6e35cd2fd2166ac95adace6ec5c54)callback

| [modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd) modem\_chat\_match::callback |
| --- |

Type of modem chat instance.

## [◆ ](#ad1bed20d70285a465663d9babc3fb3e2)match

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat\_match::match |
| --- |

Match array.

## [◆ ](#afe00a3c87a68d9f7f889f7a0d3cc4150)match\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat\_match::match\_size |
| --- |

Size of match.

## [◆ ](#aeb52b41db39ac21f5991524add42f8e3)partial

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat\_match::partial |
| --- |

Set if script shall not continue to next step in case of match.

## [◆ ](#a7fd423890bea11c65f326ace831233fc)separators

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat\_match::separators |
| --- |

Separators array.

## [◆ ](#a7c80555e1bf33504cef7be6c0f9db383)separators\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat\_match::separators\_size |
| --- |

Size of separators array.

## [◆ ](#a0e08870ad8dd3b781b8f20ed5fb230ca)wildcards

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat\_match::wildcards |
| --- |

Set if modem chat instance shall use wildcards when matching.

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[chat.h](chat_8h_source.md)

- [modem\_chat\_match](structmodem__chat__match.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
