---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structtty__serial.html
original_path: doxygen/html/structtty__serial.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tty\_serial Struct Reference

`#include <[tty.h](console_2tty_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [uart\_dev](#a6264c52c87ee712552dc5278bfd2cade) |
| struct k\_sem | [rx\_sem](#a7a3e934bc78b098cbe65789c58dd6076) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [rx\_ringbuf](#a21484e1aa96bdf6281fdca4abbcc076e) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_ringbuf\_sz](#a6a05698de6e3a1e1e17b74e3f2c976ea) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_get](#a6fb2a066e70acd11257f525909463997) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_put](#a4c86a08aa09213f67b4695644d9379b6) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [rx\_timeout](#a78c894c6cf667bd81db68d4cfbac76fe) |
| struct k\_sem | [tx\_sem](#adf19fb8b5d7446037ae316ec1f72e759) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [tx\_ringbuf](#ad06fda068fe0cc27be516e6533ecef83) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_ringbuf\_sz](#a37e46e6176c0726465b558bedadfd890) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_get](#a71d580fe2224a5c68ba02eb089df3bad) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_put](#a63f204b21deb4381157d7f6b46e0d922) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [tx\_timeout](#ac3c6954da53e2e89bc6fa56af80ef8b3) |

## Field Documentation

## [◆ ](#a6fb2a066e70acd11257f525909463997)rx\_get

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tty\_serial::rx\_get |
| --- |

## [◆ ](#a4c86a08aa09213f67b4695644d9379b6)rx\_put

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tty\_serial::rx\_put |
| --- |

## [◆ ](#a21484e1aa96bdf6281fdca4abbcc076e)rx\_ringbuf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* tty\_serial::rx\_ringbuf |
| --- |

## [◆ ](#a6a05698de6e3a1e1e17b74e3f2c976ea)rx\_ringbuf\_sz

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tty\_serial::rx\_ringbuf\_sz |
| --- |

## [◆ ](#a7a3e934bc78b098cbe65789c58dd6076)rx\_sem

| struct k\_sem tty\_serial::rx\_sem |
| --- |

## [◆ ](#a78c894c6cf667bd81db68d4cfbac76fe)rx\_timeout

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) tty\_serial::rx\_timeout |
| --- |

## [◆ ](#a71d580fe2224a5c68ba02eb089df3bad)tx\_get

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tty\_serial::tx\_get |
| --- |

## [◆ ](#a63f204b21deb4381157d7f6b46e0d922)tx\_put

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tty\_serial::tx\_put |
| --- |

## [◆ ](#ad06fda068fe0cc27be516e6533ecef83)tx\_ringbuf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* tty\_serial::tx\_ringbuf |
| --- |

## [◆ ](#a37e46e6176c0726465b558bedadfd890)tx\_ringbuf\_sz

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tty\_serial::tx\_ringbuf\_sz |
| --- |

## [◆ ](#adf19fb8b5d7446037ae316ec1f72e759)tx\_sem

| struct k\_sem tty\_serial::tx\_sem |
| --- |

## [◆ ](#ac3c6954da53e2e89bc6fa56af80ef8b3)tx\_timeout

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) tty\_serial::tx\_timeout |
| --- |

## [◆ ](#a6264c52c87ee712552dc5278bfd2cade)uart\_dev

| const struct [device](structdevice.md)\* tty\_serial::uart\_dev |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/console/[tty.h](console_2tty_8h_source.md)

- [tty\_serial](structtty__serial.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
