---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__avdtp__stream.html
original_path: doxygen/html/structbt__avdtp__stream.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avdtp\_stream Struct Reference

AVDTP Stream.
[More...](#details)

`#include <[avdtp.h](avdtp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) | [chan](#a1d29697103ce0c7841c8e9f0b7119d46) |
| struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) | [lsep](#ad9fb733cae9f63854ee7e425ab4ee3f0) |
| struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) | [rsep](#a81b7ac4fcfe5d6bdc02548616cbd8a6e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state](#a0ad0e0aa07f3d70ebec105db6356f722) |
| struct [bt\_avdtp\_stream](structbt__avdtp__stream.md) \* | [next](#a9ab341af107de917b20545ae5ac34274) |

## Detailed Description

AVDTP Stream.

## Field Documentation

## [◆ ](#a1d29697103ce0c7841c8e9f0b7119d46)chan

| struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) bt\_avdtp\_stream::chan |
| --- |

## [◆ ](#ad9fb733cae9f63854ee7e425ab4ee3f0)lsep

| struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) bt\_avdtp\_stream::lsep |
| --- |

## [◆ ](#a9ab341af107de917b20545ae5ac34274)next

| struct [bt\_avdtp\_stream](structbt__avdtp__stream.md)\* bt\_avdtp\_stream::next |
| --- |

## [◆ ](#a81b7ac4fcfe5d6bdc02548616cbd8a6e)rsep

| struct [bt\_avdtp\_seid\_info](structbt__avdtp__seid__info.md) bt\_avdtp\_stream::rsep |
| --- |

## [◆ ](#a0ad0e0aa07f3d70ebec105db6356f722)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_stream::state |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[avdtp.h](avdtp_8h_source.md)

- [bt\_avdtp\_stream](structbt__avdtp__stream.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
