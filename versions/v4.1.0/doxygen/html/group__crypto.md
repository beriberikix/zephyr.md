---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__crypto.html
original_path: doxygen/html/group__crypto.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Crypto

[Operating System Services](group__os__services.md)

Crypto APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Cipher](group__crypto__cipher.md) |
|  | Crypto Cipher APIs. |
|  | [Hash](group__crypto__hash.md) |
|  | Crypto Hash APIs. |
|  | [Random Function APIs](group__random__api.md) |
|  | Random Function APIs. |

| Data Structures | |
| --- | --- |
| struct | [crypto\_driver\_api](structcrypto__driver__api.md) |
|  | Crypto driver API definition. [More...](structcrypto__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [CAP\_OPAQUE\_KEY\_HNDL](#ga821c2629510aad5d591a565767d8abbd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAP\_RAW\_KEY](#ga95fd2a144207a575b2e0d24d5d6bf85a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAP\_KEY\_LOADING\_API](#ga18aeace031f8b9bb4241b44f8b36f056)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAP\_INPLACE\_OPS](#ga4c00d0513306fbc511fb4828108d37c8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Whether the output is placed in separate buffer or not. |
| #define | [CAP\_SEPARATE\_IO\_BUFS](#ga858150378de8f024e96614a6c2f138a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAP\_SYNC\_OPS](#ga469bae7c354d17ba9b22c7ce4d8e076a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | These denotes if the output (completion of a cipher\_xxx\_op) is conveyed by the op function returning, or it is conveyed by an async notification. |
| #define | [CAP\_ASYNC\_OPS](#ga62492a4ce9c9274c78f3a7a915a66983)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAP\_AUTONONCE](#ga6574dce552f5ba3b6f347e260a57d2f5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Whether the hardware/driver supports autononce feature. |
| #define | [CAP\_NO\_IV\_PREFIX](#ga8fa14517853a8a1c4f134b5772f7d308)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Don't prefix IV to cipher blocks. |

| Functions | |
| --- | --- |
| static int | [crypto\_query\_hwcaps](#gadb2c24136bb56927bb14d4cfffdd5d80) (const struct [device](structdevice.md) \*dev) |
|  | Query the crypto hardware capabilities. |

## Detailed Description

Crypto APIs.

Since
:   1.7

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga62492a4ce9c9274c78f3a7a915a66983)CAP\_ASYNC\_OPS

| #define CAP\_ASYNC\_OPS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

## [◆ ](#ga6574dce552f5ba3b6f347e260a57d2f5)CAP\_AUTONONCE

| #define CAP\_AUTONONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Whether the hardware/driver supports autononce feature.

## [◆ ](#ga4c00d0513306fbc511fb4828108d37c8)CAP\_INPLACE\_OPS

| #define CAP\_INPLACE\_OPS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Whether the output is placed in separate buffer or not.

## [◆ ](#ga18aeace031f8b9bb4241b44f8b36f056)CAP\_KEY\_LOADING\_API

| #define CAP\_KEY\_LOADING\_API   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

## [◆ ](#ga8fa14517853a8a1c4f134b5772f7d308)CAP\_NO\_IV\_PREFIX

| #define CAP\_NO\_IV\_PREFIX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Don't prefix IV to cipher blocks.

## [◆ ](#ga821c2629510aad5d591a565767d8abbd)CAP\_OPAQUE\_KEY\_HNDL

| #define CAP\_OPAQUE\_KEY\_HNDL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

## [◆ ](#ga95fd2a144207a575b2e0d24d5d6bf85a)CAP\_RAW\_KEY

| #define CAP\_RAW\_KEY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

## [◆ ](#ga858150378de8f024e96614a6c2f138a2)CAP\_SEPARATE\_IO\_BUFS

| #define CAP\_SEPARATE\_IO\_BUFS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

## [◆ ](#ga469bae7c354d17ba9b22c7ce4d8e076a)CAP\_SYNC\_OPS

| #define CAP\_SYNC\_OPS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

These denotes if the output (completion of a cipher\_xxx\_op) is conveyed by the op function returning, or it is conveyed by an async notification.

## Function Documentation

## [◆ ](#gadb2c24136bb56927bb14d4cfffdd5d80)crypto\_query\_hwcaps()

| | int crypto\_query\_hwcaps | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Query the crypto hardware capabilities.

This API is used by the app to query the capabilities supported by the crypto device. Based on this the app can specify a subset of the supported options to be honored for a session during [cipher\_begin\_session()](group__crypto__cipher.md#ga0720700438ba5819aa826aa37f0c4227 "Setup a crypto session.").

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   bitmask of supported options.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
