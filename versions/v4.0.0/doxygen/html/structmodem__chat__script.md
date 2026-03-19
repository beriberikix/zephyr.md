---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmodem__chat__script.html
original_path: doxygen/html/structmodem__chat__script.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_chat\_script Struct Reference

Modem chat script.
[More...](#details)

`#include <[chat.h](chat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#aca3b75a494273d8c06cf943153dd7dc8) |
|  | Name of script. |
| const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \* | [script\_chats](#a5f329ecadd721d88e423074f00005114) |
|  | Array of script chats. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [script\_chats\_size](#a3ac30e3ba1842cf53747721592f16cd4) |
|  | Elements in array of script chats. |
| const struct [modem\_chat\_match](structmodem__chat__match.md) \* | [abort\_matches](#a2b586e1ff80c22d8ff45829f3e2e7b17) |
|  | Array of abort matches. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [abort\_matches\_size](#aa56bdf520b0f385bc6410b2c6aa2e8d4) |
|  | Number of elements in array of abort matches. |
| [modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e) | [callback](#a73f4c3892052f827c10ea466c9a75954) |
|  | Callback called when script execution terminates. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timeout](#a0b9a9d3d44a8624728e16922cbdfd662) |
|  | Timeout in seconds within which the script execution must terminate. |

## Detailed Description

Modem chat script.

## Field Documentation

## [◆ ](#a2b586e1ff80c22d8ff45829f3e2e7b17)abort\_matches

| const struct [modem\_chat\_match](structmodem__chat__match.md)\* modem\_chat\_script::abort\_matches |
| --- |

Array of abort matches.

## [◆ ](#aa56bdf520b0f385bc6410b2c6aa2e8d4)abort\_matches\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_script::abort\_matches\_size |
| --- |

Number of elements in array of abort matches.

## [◆ ](#a73f4c3892052f827c10ea466c9a75954)callback

| [modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e) modem\_chat\_script::callback |
| --- |

Callback called when script execution terminates.

## [◆ ](#aca3b75a494273d8c06cf943153dd7dc8)name

| const char\* modem\_chat\_script::name |
| --- |

Name of script.

## [◆ ](#a5f329ecadd721d88e423074f00005114)script\_chats

| const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md)\* modem\_chat\_script::script\_chats |
| --- |

Array of script chats.

## [◆ ](#a3ac30e3ba1842cf53747721592f16cd4)script\_chats\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat\_script::script\_chats\_size |
| --- |

Elements in array of script chats.

## [◆ ](#a0b9a9d3d44a8624728e16922cbdfd662)timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modem\_chat\_script::timeout |
| --- |

Timeout in seconds within which the script execution must terminate.

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[chat.h](chat_8h_source.md)

- [modem\_chat\_script](structmodem__chat__script.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
