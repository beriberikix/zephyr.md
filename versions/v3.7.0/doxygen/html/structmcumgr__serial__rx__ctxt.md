---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmcumgr__serial__rx__ctxt.html
original_path: doxygen/html/structmcumgr__serial__rx__ctxt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcumgr\_serial\_rx\_ctxt Struct Reference

Maintains state for an incoming mcumgr request packet.
[More...](#details)

`#include <[serial.h](serial_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [nb](#a5fdf2dd95185a49806c1900184c7bdfc) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pkt\_len](#a4ded2b7748334b0f3166f4c18cd1d6b0) |

## Detailed Description

Maintains state for an incoming mcumgr request packet.

## Field Documentation

## [◆ ](#a5fdf2dd95185a49806c1900184c7bdfc)nb

| struct [net\_buf](structnet__buf.md)\* mcumgr\_serial\_rx\_ctxt::nb |
| --- |

## [◆ ](#a4ded2b7748334b0f3166f4c18cd1d6b0)pkt\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mcumgr\_serial\_rx\_ctxt::pkt\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/transport/[serial.h](serial_8h_source.md)

- [mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
