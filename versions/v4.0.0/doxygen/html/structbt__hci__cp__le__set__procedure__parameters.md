---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__cp__le__set__procedure__parameters.html
original_path: doxygen/html/structbt__hci__cp__le__set__procedure__parameters.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_le\_set\_procedure\_parameters Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#ab8a15269255fb7d960ae712a844b9f35) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [config\_id](#a7d2f5d9242df436906b005e66c7bb75d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_len](#a5de9205fdf1b6e342f53a12aa82c10c5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_procedure\_interval](#a22ecbaff0fd48a0716a15d265adc590e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_interval](#ad46165bc5f6d875940ee53a8b98cb5b4) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_count](#ac6bb66fa24aec17a964f27365ca65ec9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_subevent\_len](#a51fb8c789cefce09d5da2b86d5c862ce) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_subevent\_len](#aa9ec99aff85de173ccb2d3f144c85319) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tone\_antenna\_config\_selection](#aa783e0e63c38ceee503c0b73ac873ca7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#afcd4e8b390fd996ee134043ec2930fe8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_power\_delta](#ade09ca9d42b0db682cf677d9ac4326d2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [preferred\_peer\_antenna](#a7a61ff539f68a02ea7aa466f182dc5ab) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [snr\_control\_initiator](#a8524fd01e35094d2b78488c0a2876832) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [snr\_control\_reflector](#aa5a6a677b6e0d57658041e891535d74b) |

## Field Documentation

## [◆ ](#a7d2f5d9242df436906b005e66c7bb75d)config\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::config\_id |
| --- |

## [◆ ](#ab8a15269255fb7d960ae712a844b9f35)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_procedure\_parameters::handle |
| --- |

## [◆ ](#ac6bb66fa24aec17a964f27365ca65ec9)max\_procedure\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_procedure\_count |
| --- |

## [◆ ](#ad46165bc5f6d875940ee53a8b98cb5b4)max\_procedure\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_procedure\_interval |
| --- |

## [◆ ](#a5de9205fdf1b6e342f53a12aa82c10c5)max\_procedure\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_procedure\_len |
| --- |

## [◆ ](#aa9ec99aff85de173ccb2d3f144c85319)max\_subevent\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::max\_subevent\_len[3] |
| --- |

## [◆ ](#a22ecbaff0fd48a0716a15d265adc590e)min\_procedure\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_procedure\_parameters::min\_procedure\_interval |
| --- |

## [◆ ](#a51fb8c789cefce09d5da2b86d5c862ce)min\_subevent\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::min\_subevent\_len[3] |
| --- |

## [◆ ](#afcd4e8b390fd996ee134043ec2930fe8)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::phy |
| --- |

## [◆ ](#a7a61ff539f68a02ea7aa466f182dc5ab)preferred\_peer\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::preferred\_peer\_antenna |
| --- |

## [◆ ](#a8524fd01e35094d2b78488c0a2876832)snr\_control\_initiator

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::snr\_control\_initiator |
| --- |

## [◆ ](#aa5a6a677b6e0d57658041e891535d74b)snr\_control\_reflector

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::snr\_control\_reflector |
| --- |

## [◆ ](#aa783e0e63c38ceee503c0b73ac873ca7)tone\_antenna\_config\_selection

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::tone\_antenna\_config\_selection |
| --- |

## [◆ ](#ade09ca9d42b0db682cf677d9ac4326d2)tx\_power\_delta

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_procedure\_parameters::tx\_power\_delta |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_le\_set\_procedure\_parameters](structbt__hci__cp__le__set__procedure__parameters.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
