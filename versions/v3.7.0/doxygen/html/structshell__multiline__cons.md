---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__multiline__cons.html
original_path: doxygen/html/structshell__multiline__cons.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_multiline\_cons Struct Reference

`#include <[shell_types.h](shell__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cur\_x](#a52a43a16f9d2e30d82dfe019384b0f7b) |
|  | horizontal cursor position in edited command line. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cur\_x\_end](#a54a051c1e085644e6cd1e86284fabf0d) |
|  | horizontal cursor position at the end of command. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cur\_y](#a0ee84724f4b26ee2933c88b170445d93) |
|  | vertical cursor position in edited command. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cur\_y\_end](#a0a07e8991006b34f111d068e22800d28) |
|  | vertical cursor position at the end of command. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [terminal\_hei](#ae65c3c25e87841be58347cf54b5c36d8) |
|  | terminal screen height. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [terminal\_wid](#a48b37c8d0cc4584ab05299be34008575) |
|  | terminal screen width. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [name\_len](#aa4ed5794533137992a2a9d3e7eb12f6a) |
|  | console name length. |

## Field Documentation

## [◆ ](#a52a43a16f9d2e30d82dfe019384b0f7b)cur\_x

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_multiline\_cons::cur\_x |
| --- |

horizontal cursor position in edited command line.

## [◆ ](#a54a051c1e085644e6cd1e86284fabf0d)cur\_x\_end

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_multiline\_cons::cur\_x\_end |
| --- |

horizontal cursor position at the end of command.

## [◆ ](#a0ee84724f4b26ee2933c88b170445d93)cur\_y

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_multiline\_cons::cur\_y |
| --- |

vertical cursor position in edited command.

## [◆ ](#a0a07e8991006b34f111d068e22800d28)cur\_y\_end

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_multiline\_cons::cur\_y\_end |
| --- |

vertical cursor position at the end of command.

## [◆ ](#aa4ed5794533137992a2a9d3e7eb12f6a)name\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_multiline\_cons::name\_len |
| --- |

console name length.

## [◆ ](#ae65c3c25e87841be58347cf54b5c36d8)terminal\_hei

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_multiline\_cons::terminal\_hei |
| --- |

terminal screen height.

## [◆ ](#a48b37c8d0cc4584ab05299be34008575)terminal\_wid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) shell\_multiline\_cons::terminal\_wid |
| --- |

terminal screen width.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_types.h](shell__types_8h_source.md)

- [shell\_multiline\_cons](structshell__multiline__cons.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
