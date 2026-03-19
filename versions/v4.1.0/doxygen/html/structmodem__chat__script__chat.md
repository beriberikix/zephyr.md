---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmodem__chat__script__chat.html
original_path: doxygen/html/structmodem__chat__script__chat.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_chat\_script\_chat Struct Reference

Modem chat script chat.
[More...](#details)

`#include <[chat.h](chat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [request](#a92c038d56623b4f4b26c64b537e7ce8a) |
|  | Request to send to modem. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [request\_size](#ad87948ff4e6441c118ee269bf6458aa0) |
|  | Size of request. |
| const struct [modem\_chat\_match](structmodem__chat__match.md) \* | [response\_matches](#a5cab9c3a31624c8ffb490b70285f86ee) |
|  | Expected responses to request. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [response\_matches\_size](#afaaa9a7bc1842dfb65156fff2d91cfa0) |
|  | Number of elements in expected responses. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a21647c746e9b2da52b7093afccf08268) |
|  | Timeout before chat script may continue to next step in milliseconds. |

## Detailed Description

Modem chat script chat.

## Field Documentation

## [◆ ](#a92c038d56623b4f4b26c64b537e7ce8a)request

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat\_script\_chat::request |
| --- |

Request to send to modem.

## [◆ ](#ad87948ff4e6441c118ee269bf6458aa0)request\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_script\_chat::request\_size |
| --- |

Size of request.

## [◆ ](#a5cab9c3a31624c8ffb490b70285f86ee)response\_matches

| const struct [modem\_chat\_match](structmodem__chat__match.md)\* modem\_chat\_script\_chat::response\_matches |
| --- |

Expected responses to request.

## [◆ ](#afaaa9a7bc1842dfb65156fff2d91cfa0)response\_matches\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_script\_chat::response\_matches\_size |
| --- |

Number of elements in expected responses.

## [◆ ](#a21647c746e9b2da52b7093afccf08268)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_script\_chat::timeout |
| --- |

Timeout before chat script may continue to next step in milliseconds.

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[chat.h](chat_8h_source.md)

- [modem\_chat\_script\_chat](structmodem__chat__script__chat.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
