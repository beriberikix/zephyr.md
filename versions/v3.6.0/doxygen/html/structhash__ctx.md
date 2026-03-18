---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structhash__ctx.html
original_path: doxygen/html/structhash__ctx.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_ctx Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md) » [Hash](group__crypto__hash.md)

Structure encoding session parameters.
[More...](#details)

`#include <[hash.h](hash_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [device](#abe1e70bd23305296e54564b5966ff310) |
|  | The device driver instance this crypto context relates to. |
| void \* | [drv\_sessn\_state](#ad9c9bb4472975ba6999986bb6c01b501) |
|  | If the driver supports multiple simultaneously crypto sessions, this will identify the specific driver state this crypto session relates to. |
| [hash\_op\_t](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070) | [hash\_hndlr](#a72a2e7af667bed1ee1dabb8411b01e40) |
|  | Hash handler set up when the session begins. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [started](#a33dbeb54cd8663f1f5391988d8ee642e) |
|  | If it has started a multipart hash operation. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#ab550711912423a0eb03c410aef491854) |
|  | How certain fields are to be interpreted for this session. |

## Detailed Description

Structure encoding session parameters.

Refer to comments for individual fields to know the contract in terms of who fills what and when w.r.t begin\_session() call.

## Field Documentation

## [◆ ](#abe1e70bd23305296e54564b5966ff310)device

| const struct [device](structdevice.md)\* hash\_ctx::device |
| --- |

The device driver instance this crypto context relates to.

Will be populated by the begin\_session() API.

## [◆ ](#ad9c9bb4472975ba6999986bb6c01b501)drv\_sessn\_state

| void\* hash\_ctx::drv\_sessn\_state |
| --- |

If the driver supports multiple simultaneously crypto sessions, this will identify the specific driver state this crypto session relates to.

Since dynamic memory allocation is not possible, it is suggested that at build time drivers allocate space for the max simultaneous sessions they intend to support. To be populated by the driver on return from begin\_session().

## [◆ ](#ab550711912423a0eb03c410aef491854)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hash\_ctx::flags |
| --- |

How certain fields are to be interpreted for this session.

(A bitmask of CAP\_\* below.) To be populated by the app before calling [hash\_begin\_session()](group__crypto__hash.md#ga9b736d047cbfb7530ffa0bc4b64d6ad1 "Setup a hash session."). An app can obtain the capability flags supported by a hw/driver by calling [crypto\_query\_hwcaps()](group__crypto.md#gadb2c24136bb56927bb14d4cfffdd5d80 "Query the crypto hardware capabilities.").

## [◆ ](#a72a2e7af667bed1ee1dabb8411b01e40)hash\_hndlr

| [hash\_op\_t](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070) hash\_ctx::hash\_hndlr |
| --- |

Hash handler set up when the session begins.

## [◆ ](#a33dbeb54cd8663f1f5391988d8ee642e)started

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) hash\_ctx::started |
| --- |

If it has started a multipart hash operation.

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[hash.h](hash_8h_source.md)

- [hash\_ctx](structhash__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
