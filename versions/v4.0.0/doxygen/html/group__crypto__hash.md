---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__crypto__hash.html
original_path: doxygen/html/group__crypto__hash.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hash

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md)

Crypto Hash APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [hash\_ctx](structhash__ctx.md) |
|  | Structure encoding session parameters. [More...](structhash__ctx.md#details) |
| struct | [hash\_pkt](structhash__pkt.md) |
|  | Structure encoding IO parameters of a hash operation. [More...](structhash__pkt.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [hash\_op\_t](#ga955369c6da6aa70ded229d8861292070)) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) finish) |
| typedef void(\* | [hash\_completion\_cb](#ga1f49008c35d9f04b66e587d1b43404bd)) (struct [hash\_pkt](structhash__pkt.md) \*completed, int status) |

| Enumerations | |
| --- | --- |
| enum | [hash\_algo](#gaaea88501aa8243eacc8c57ac0914ac7a) { [CRYPTO\_HASH\_ALGO\_SHA224](#ggaaea88501aa8243eacc8c57ac0914ac7aaa49fd348b98d55eca407ae88e3626265) = 1 , [CRYPTO\_HASH\_ALGO\_SHA256](#ggaaea88501aa8243eacc8c57ac0914ac7aa1b0b60a3270618fd492491668dc2ad43) = 2 , [CRYPTO\_HASH\_ALGO\_SHA384](#ggaaea88501aa8243eacc8c57ac0914ac7aabba9e518a333ce75825957fde1993dd5) = 3 , [CRYPTO\_HASH\_ALGO\_SHA512](#ggaaea88501aa8243eacc8c57ac0914ac7aa72a129765ae9e15f456c295c3917bf3f) = 4 } |
|  | Hash algorithm. [More...](#gaaea88501aa8243eacc8c57ac0914ac7a) |

| Functions | |
| --- | --- |
| static int | [hash\_begin\_session](#ga9b736d047cbfb7530ffa0bc4b64d6ad1) (const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx, enum [hash\_algo](#gaaea88501aa8243eacc8c57ac0914ac7a) algo) |
|  | Setup a hash session. |
| static int | [hash\_free\_session](#gadafcd2ad79e0695245c8884b6b282508) (const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx) |
|  | Cleanup a hash session. |
| static int | [hash\_callback\_set](#gaa69bbf41cc150dae0d97b215862729cf) (const struct [device](structdevice.md) \*dev, [hash\_completion\_cb](#ga1f49008c35d9f04b66e587d1b43404bd) cb) |
|  | Registers an async hash completion callback with the driver. |
| static int | [hash\_compute](#ga761e5d0bda9937d7fa4550c876a1c387) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt) |
|  | Perform a cryptographic hash function. |
| static int | [hash\_update](#gaf54ee20fb1ca58764f6f301739c3ba93) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt) |
|  | Perform a cryptographic multipart hash operation. |

## Detailed Description

Crypto Hash APIs.

## Typedef Documentation

## [◆ ](#ga1f49008c35d9f04b66e587d1b43404bd)hash\_completion\_cb

| typedef void(\* hash\_completion\_cb) (struct [hash\_pkt](structhash__pkt.md) \*completed, int status) |
| --- |

`#include <[hash.h](hash_8h.md)>`

## [◆ ](#ga955369c6da6aa70ded229d8861292070)hash\_op\_t

| typedef int(\* hash\_op\_t) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) finish) |
| --- |

`#include <[hash.h](hash_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gaaea88501aa8243eacc8c57ac0914ac7a)hash\_algo

| enum [hash\_algo](#gaaea88501aa8243eacc8c57ac0914ac7a) |
| --- |

`#include <[hash.h](hash_8h.md)>`

Hash algorithm.

| Enumerator | |
| --- | --- |
| CRYPTO\_HASH\_ALGO\_SHA224 |  |
| CRYPTO\_HASH\_ALGO\_SHA256 |  |
| CRYPTO\_HASH\_ALGO\_SHA384 |  |
| CRYPTO\_HASH\_ALGO\_SHA512 |  |

## Function Documentation

## [◆ ](#ga9b736d047cbfb7530ffa0bc4b64d6ad1)hash\_begin\_session()

| | int hash\_begin\_session | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [hash\_ctx](structhash__ctx.md) \* | *ctx*, | |  |  | enum [hash\_algo](#gaaea88501aa8243eacc8c57ac0914ac7a) | *algo* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Setup a hash session.

Initializes one time parameters, like the algorithm which may remain constant for all operations in the session. The state may be cached in hardware and/or driver data state variables.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ctx | Pointer to the context structure. Various one time parameters like session capabilities and algorithm are supplied via this structure. The structure documentation specifies which fields are to be populated by the app before making this call. |
    | algo | The hash algorithm to be used in this session. e.g sha256 |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaa69bbf41cc150dae0d97b215862729cf)hash\_callback\_set()

| | int hash\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [hash\_completion\_cb](#ga1f49008c35d9f04b66e587d1b43404bd) | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Registers an async hash completion callback with the driver.

The application can register an async hash completion callback handler to be invoked by the driver, on completion of a prior request submitted via [hash\_compute()](#ga761e5d0bda9937d7fa4550c876a1c387). Based on crypto device hardware semantics, this is likely to be invoked from an ISR context.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cb | Pointer to application callback to be called by the driver. |

Returns
:   0 on success, -ENOTSUP if the driver does not support async op, negative errno code on other error.

## [◆ ](#ga761e5d0bda9937d7fa4550c876a1c387)hash\_compute()

| | int hash\_compute | ( | struct [hash\_ctx](structhash__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [hash\_pkt](structhash__pkt.md) \* | *pkt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform a cryptographic hash function.

Parameters
:   | ctx | Pointer to the hash context of this op. |
    | --- | --- |
    | pkt | Structure holding the input/output. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gadafcd2ad79e0695245c8884b6b282508)hash\_free\_session()

| | int hash\_free\_session | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [hash\_ctx](structhash__ctx.md) \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Cleanup a hash session.

Clears the hardware and/or driver state of a session.

See also
:   [hash\_begin\_session](#ga9b736d047cbfb7530ffa0bc4b64d6ad1)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ctx | Pointer to the crypto hash context structure of the session to be freed. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaf54ee20fb1ca58764f6f301739c3ba93)hash\_update()

| | int hash\_update | ( | struct [hash\_ctx](structhash__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [hash\_pkt](structhash__pkt.md) \* | *pkt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform a cryptographic multipart hash operation.

This function can be called zero or more times, passing a slice of the data. The hash is calculated using all the given pieces. To calculate the hash call `[hash_compute()](#ga761e5d0bda9937d7fa4550c876a1c387)`.

Parameters
:   | ctx | Pointer to the hash context of this op. |
    | --- | --- |
    | pkt | Structure holding the input. |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
