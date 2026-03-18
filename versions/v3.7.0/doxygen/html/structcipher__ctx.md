---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcipher__ctx.html
original_path: doxygen/html/structcipher__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cipher\_ctx Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md) » [Cipher](group__crypto__cipher.md)

Structure encoding session parameters.
[More...](#details)

`#include <[cipher.h](cipher_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [cipher\_ops](structcipher__ops.md) | [ops](#ae3eb86d5be42450b761f89114723b682) |
|  | Place for driver to return function pointers to be invoked per cipher operation. |
| union { |  |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [bit\_stream](#abc8f2818fcb3a83c3c00805a55e5805d) |  |
| void \*   [handle](#a81dfa0793e62065a247bd3d5b5bdc903) |  |
| } | [key](#a441096f011ad26e2ba6411bdd98eb0a2) |
|  | To be populated by the app before calling begin\_session(). |
| const struct [device](structdevice.md) \* | [device](#a44842ea8ece2aaea4d757137cdb67b52) |
|  | The device driver instance this crypto context relates to. |
| void \* | [drv\_sessn\_state](#a624cf985cf35b3aa8681c3892fd67429) |
|  | If the driver supports multiple simultaneously crypto sessions, this will identify the specific driver state this crypto session relates to. |
| void \* | [app\_sessn\_state](#a0439c7f7c300a59296d353e76132c028) |
|  | Place for the user app to put info relevant stuff for resuming when completion callback happens for async ops. |
| union { |  |
| struct [ccm\_params](structccm__params.md)   [ccm\_info](#a3b6f3cdda6344880f3dcc3e2c8246b15) |  |
| struct [ctr\_params](structctr__params.md)   [ctr\_info](#a8a7b59087bd474eaad8d996e1600e757) |  |
| struct [gcm\_params](structgcm__params.md)   [gcm\_info](#a995276020bd2ef77451d941fa3b238d2) |  |
| } | [mode\_params](#aa0f89473a5d1d6417a128bb452982db7) |
|  | Cypher mode parameters, which remain constant for all ops in a session. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [keylen](#a10dbfc431a748118c186099c249ed5e4) |
|  | Cryptographic keylength in bytes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#a5745811b9b08e6df51f9b8f8b14ceae7) |
|  | How certain fields are to be interpreted for this session. |

## Detailed Description

Structure encoding session parameters.

Refer to comments for individual fields to know the contract in terms of who fills what and when w.r.t begin\_session() call.

## Field Documentation

## [◆ ](#a0439c7f7c300a59296d353e76132c028)app\_sessn\_state

| void\* cipher\_ctx::app\_sessn\_state |
| --- |

Place for the user app to put info relevant stuff for resuming when completion callback happens for async ops.

Totally managed by the app.

## [◆ ](#abc8f2818fcb3a83c3c00805a55e5805d)bit\_stream

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* cipher\_ctx::bit\_stream |
| --- |

## [◆ ](#a3b6f3cdda6344880f3dcc3e2c8246b15)ccm\_info

| struct [ccm\_params](structccm__params.md) cipher\_ctx::ccm\_info |
| --- |

## [◆ ](#a8a7b59087bd474eaad8d996e1600e757)ctr\_info

| struct [ctr\_params](structctr__params.md) cipher\_ctx::ctr\_info |
| --- |

## [◆ ](#a44842ea8ece2aaea4d757137cdb67b52)device

| const struct [device](structdevice.md)\* cipher\_ctx::device |
| --- |

The device driver instance this crypto context relates to.

Will be populated by the begin\_session() API.

## [◆ ](#a624cf985cf35b3aa8681c3892fd67429)drv\_sessn\_state

| void\* cipher\_ctx::drv\_sessn\_state |
| --- |

If the driver supports multiple simultaneously crypto sessions, this will identify the specific driver state this crypto session relates to.

Since dynamic memory allocation is not possible, it is suggested that at build time drivers allocate space for the max simultaneous sessions they intend to support. To be populated by the driver on return from begin\_session().

## [◆ ](#a5745811b9b08e6df51f9b8f8b14ceae7)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cipher\_ctx::flags |
| --- |

How certain fields are to be interpreted for this session.

(A bitmask of CAP\_\* below.) To be populated by the app before calling begin\_session(). An app can obtain the capability flags supported by a hw/driver by calling [crypto\_query\_hwcaps()](group__crypto.md#gadb2c24136bb56927bb14d4cfffdd5d80 "Query the crypto hardware capabilities.").

## [◆ ](#a995276020bd2ef77451d941fa3b238d2)gcm\_info

| struct [gcm\_params](structgcm__params.md) cipher\_ctx::gcm\_info |
| --- |

## [◆ ](#a81dfa0793e62065a247bd3d5b5bdc903)handle

| void\* cipher\_ctx::handle |
| --- |

## [◆ ](#a441096f011ad26e2ba6411bdd98eb0a2)[union]

| union { ... } cipher\_ctx::key |
| --- |

To be populated by the app before calling begin\_session().

## [◆ ](#a10dbfc431a748118c186099c249ed5e4)keylen

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cipher\_ctx::keylen |
| --- |

Cryptographic keylength in bytes.

To be populated by the app before calling begin\_session()

## [◆ ](#aa0f89473a5d1d6417a128bb452982db7)[union]

| union { ... } cipher\_ctx::mode\_params |
| --- |

Cypher mode parameters, which remain constant for all ops in a session.

To be populated by the app before calling begin\_session().

## [◆ ](#ae3eb86d5be42450b761f89114723b682)ops

| struct [cipher\_ops](structcipher__ops.md) cipher\_ctx::ops |
| --- |

Place for driver to return function pointers to be invoked per cipher operation.

To be populated by crypto driver on return from begin\_session() based on the algo/mode chosen by the app.

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[cipher.h](cipher_8h_source.md)

- [cipher\_ctx](structcipher__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
