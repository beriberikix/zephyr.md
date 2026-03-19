---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__crypto__cipher.html
original_path: doxygen/html/group__crypto__cipher.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Cipher

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md)

Crypto Cipher APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [cipher\_ops](structcipher__ops.md) |
| struct | [ccm\_params](structccm__params.md) |
| struct | [ctr\_params](structctr__params.md) |
| struct | [gcm\_params](structgcm__params.md) |
| struct | [cipher\_ctx](structcipher__ctx.md) |
|  | Structure encoding session parameters. [More...](structcipher__ctx.md#details) |
| struct | [cipher\_pkt](structcipher__pkt.md) |
|  | Structure encoding IO parameters of one cryptographic operation like encrypt/decrypt. [More...](structcipher__pkt.md#details) |
| struct | [cipher\_aead\_pkt](structcipher__aead__pkt.md) |
|  | Structure encoding IO parameters in AEAD (Authenticated Encryption with Associated Data) scenario like in CCM. [More...](structcipher__aead__pkt.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [block\_op\_t](#ga584073236a507f736442dedab87b1e17)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt) |
| typedef int(\* | [cbc\_op\_t](#gaa74d09d409b42b29c4c7045dc77552d2)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
| typedef int(\* | [ctr\_op\_t](#gad1ed48328ca31f8ce2dd7e0a166cacba)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ctr) |
| typedef int(\* | [ccm\_op\_t](#ga55e4d15dde1a5134c695ce0c31dabaf7)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
| typedef int(\* | [gcm\_op\_t](#gad27577142dd49308b2470253a41bd09d)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
| typedef void(\* | [cipher\_completion\_cb](#ga062b07459bcc2990535465a7b9044ecd)) (struct [cipher\_pkt](structcipher__pkt.md) \*completed, int status) |

| Enumerations | |
| --- | --- |
| enum | [cipher\_algo](#gaa43d9907b508cb28c649aaa524d84424) { [CRYPTO\_CIPHER\_ALGO\_AES](#ggaa43d9907b508cb28c649aaa524d84424aed0c05202ecbb1496f84ec6c383ddcf0) = 1 } |
|  | Cipher Algorithm. [More...](#gaa43d9907b508cb28c649aaa524d84424) |
| enum | [cipher\_op](#ga1db3a5604bff0669672af4457aaaee21) { [CRYPTO\_CIPHER\_OP\_DECRYPT](#gga1db3a5604bff0669672af4457aaaee21a1e1205f695285034b4889ac19a191617) = 0 , [CRYPTO\_CIPHER\_OP\_ENCRYPT](#gga1db3a5604bff0669672af4457aaaee21a71bf6ee186bab1729e24e37c119d0019) = 1 } |
|  | Cipher Operation. [More...](#ga1db3a5604bff0669672af4457aaaee21) |
| enum | [cipher\_mode](#gaeedaf8017f8d6518f7dedef365bbae43) {     [CRYPTO\_CIPHER\_MODE\_ECB](#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e) = 1 , [CRYPTO\_CIPHER\_MODE\_CBC](#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd) = 2 , [CRYPTO\_CIPHER\_MODE\_CTR](#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2) = 3 , [CRYPTO\_CIPHER\_MODE\_CCM](#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b) = 4 ,     [CRYPTO\_CIPHER\_MODE\_GCM](#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12) = 5   } |
|  | Possible cipher mode options. [More...](#gaeedaf8017f8d6518f7dedef365bbae43) |

| Functions | |
| --- | --- |
| static int | [cipher\_begin\_session](#ga0720700438ba5819aa826aa37f0c4227) (const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx, enum [cipher\_algo](#gaa43d9907b508cb28c649aaa524d84424) algo, enum [cipher\_mode](#gaeedaf8017f8d6518f7dedef365bbae43) mode, enum [cipher\_op](#ga1db3a5604bff0669672af4457aaaee21) optype) |
|  | Setup a crypto session. |
| static int | [cipher\_free\_session](#gaa818a3de1f2d6319cd21bf6b7caf7cbb) (const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx) |
|  | Cleanup a crypto session. |
| static int | [cipher\_callback\_set](#gaaf0add27d9116f584e7bbc2d8f1eb39b) (const struct [device](structdevice.md) \*dev, [cipher\_completion\_cb](#ga062b07459bcc2990535465a7b9044ecd) cb) |
|  | Registers an async crypto op completion callback with the driver. |
| static int | [cipher\_block\_op](#ga05a2569f8d404593e053ce69817a457e) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt) |
|  | Perform single-block crypto operation (ECB cipher mode). |
| static int | [cipher\_cbc\_op](#ga2c4ac483eb4e11110be939e669040700) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
|  | Perform Cipher Block Chaining (CBC) crypto operation. |
| static int | [cipher\_ctr\_op](#gaeffb9d5dd85bf135eb2cca6d47cb373c) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
|  | Perform Counter (CTR) mode crypto operation. |
| static int | [cipher\_ccm\_op](#ga4886e7e1cc2fcff411066875b35b8b45) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
|  | Perform Counter with CBC-MAC (CCM) mode crypto operation. |
| static int | [cipher\_gcm\_op](#ga3706b034252e40b818a782c28ba5e485) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
|  | Perform Galois/Counter Mode (GCM) crypto operation. |

## Detailed Description

Crypto Cipher APIs.

## Typedef Documentation

## [◆ ](#ga584073236a507f736442dedab87b1e17)block\_op\_t

| typedef int(\* block\_op\_t) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

## [◆ ](#gaa74d09d409b42b29c4c7045dc77552d2)cbc\_op\_t

| typedef int(\* cbc\_op\_t) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

## [◆ ](#ga55e4d15dde1a5134c695ce0c31dabaf7)ccm\_op\_t

| typedef int(\* ccm\_op\_t) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

## [◆ ](#ga062b07459bcc2990535465a7b9044ecd)cipher\_completion\_cb

| typedef void(\* cipher\_completion\_cb) (struct [cipher\_pkt](structcipher__pkt.md) \*completed, int status) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

## [◆ ](#gad1ed48328ca31f8ce2dd7e0a166cacba)ctr\_op\_t

| typedef int(\* ctr\_op\_t) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ctr) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

## [◆ ](#gad27577142dd49308b2470253a41bd09d)gcm\_op\_t

| typedef int(\* gcm\_op\_t) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gaa43d9907b508cb28c649aaa524d84424)cipher\_algo

| enum [cipher\_algo](#gaa43d9907b508cb28c649aaa524d84424) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

Cipher Algorithm.

| Enumerator | |
| --- | --- |
| CRYPTO\_CIPHER\_ALGO\_AES |  |

## [◆ ](#gaeedaf8017f8d6518f7dedef365bbae43)cipher\_mode

| enum [cipher\_mode](#gaeedaf8017f8d6518f7dedef365bbae43) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

Possible cipher mode options.

More to be added as required.

| Enumerator | |
| --- | --- |
| CRYPTO\_CIPHER\_MODE\_ECB |  |
| CRYPTO\_CIPHER\_MODE\_CBC |  |
| CRYPTO\_CIPHER\_MODE\_CTR |  |
| CRYPTO\_CIPHER\_MODE\_CCM |  |
| CRYPTO\_CIPHER\_MODE\_GCM |  |

## [◆ ](#ga1db3a5604bff0669672af4457aaaee21)cipher\_op

| enum [cipher\_op](#ga1db3a5604bff0669672af4457aaaee21) |
| --- |

`#include <[cipher.h](cipher_8h.md)>`

Cipher Operation.

| Enumerator | |
| --- | --- |
| CRYPTO\_CIPHER\_OP\_DECRYPT |  |
| CRYPTO\_CIPHER\_OP\_ENCRYPT |  |

## Function Documentation

## [◆ ](#ga0720700438ba5819aa826aa37f0c4227)cipher\_begin\_session()

| | int cipher\_begin\_session | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx*, | |  |  | enum [cipher\_algo](#gaa43d9907b508cb28c649aaa524d84424) | *algo*, | |  |  | enum [cipher\_mode](#gaeedaf8017f8d6518f7dedef365bbae43) | *mode*, | |  |  | enum [cipher\_op](#ga1db3a5604bff0669672af4457aaaee21) | *optype* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Setup a crypto session.

Initializes one time parameters, like the session key, algorithm and cipher mode which may remain constant for all operations in the session. The state may be cached in hardware and/or driver data state variables.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ctx | Pointer to the context structure. Various one time parameters like key, keylength, etc. are supplied via this structure. The structure documentation specifies which fields are to be populated by the app before making this call. |
    | algo | The crypto algorithm to be used in this session. e.g AES |
    | mode | The cipher mode to be used in this session. e.g CBC, CTR |
    | optype | Whether we should encrypt or decrypt in this session |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga05a2569f8d404593e053ce69817a457e)cipher\_block\_op()

| | int cipher\_block\_op | ( | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [cipher\_pkt](structcipher__pkt.md) \* | *pkt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform single-block crypto operation (ECB cipher mode).

This should not be overloaded to operate on multiple blocks for security reasons.

Parameters
:   | ctx | Pointer to the crypto context of this op. |
    | --- | --- |
    | pkt | Structure holding the input/output buffer pointers. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaaf0add27d9116f584e7bbc2d8f1eb39b)cipher\_callback\_set()

| | int cipher\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [cipher\_completion\_cb](#ga062b07459bcc2990535465a7b9044ecd) | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Registers an async crypto op completion callback with the driver.

The application can register an async crypto op completion callback handler to be invoked by the driver, on completion of a prior request submitted via cipher\_do\_op(). Based on crypto device hardware semantics, this is likely to be invoked from an ISR context.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | cb | Pointer to application callback to be called by the driver. |

Returns
:   0 on success, -ENOTSUP if the driver does not support async op, negative errno code on other error.

## [◆ ](#ga2c4ac483eb4e11110be939e669040700)cipher\_cbc\_op()

| | int cipher\_cbc\_op | ( | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [cipher\_pkt](structcipher__pkt.md) \* | *pkt*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *iv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform Cipher Block Chaining (CBC) crypto operation.

Parameters
:   | ctx | Pointer to the crypto context of this op. |
    | --- | --- |
    | pkt | Structure holding the input/output buffer pointers. |
    | iv | Initialization Vector (IV) for the operation. Same IV value should not be reused across multiple operations (within a session context) for security. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga4886e7e1cc2fcff411066875b35b8b45)cipher\_ccm\_op()

| | int cipher\_ccm\_op | ( | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \* | *pkt*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *nonce* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform Counter with CBC-MAC (CCM) mode crypto operation.

Parameters
:   | ctx | Pointer to the crypto context of this op. |
    | --- | --- |
    | pkt | Structure holding the input/output, Associated Data (AD) and auth tag buffer pointers. |
    | nonce | Nonce for the operation. Same nonce value should not be reused across multiple operations (within a session context) for security. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaeffb9d5dd85bf135eb2cca6d47cb373c)cipher\_ctr\_op()

| | int cipher\_ctr\_op | ( | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [cipher\_pkt](structcipher__pkt.md) \* | *pkt*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *iv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform Counter (CTR) mode crypto operation.

Parameters
:   | ctx | Pointer to the crypto context of this op. |
    | --- | --- |
    | pkt | Structure holding the input/output buffer pointers. |
    | iv | Initialization Vector (IV) for the operation. We use a split counter formed by appending IV and ctr. Consequently ivlen = keylen - ctrlen. 'ctrlen' is specified during session setup through the 'ctx.mode\_params.ctr\_params.ctr\_len' parameter. IV should not be reused across multiple operations (within a session context) for security. The non-IV part of the split counter is transparent to the caller and is fully managed by the crypto provider. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaa818a3de1f2d6319cd21bf6b7caf7cbb)cipher\_free\_session()

| | int cipher\_free\_session | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Cleanup a crypto session.

Clears the hardware and/or driver state of a previous session.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ctx | Pointer to the crypto context structure of the session to be freed. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga3706b034252e40b818a782c28ba5e485)cipher\_gcm\_op()

| | int cipher\_gcm\_op | ( | struct [cipher\_ctx](structcipher__ctx.md) \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \* | *pkt*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *nonce* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crypto.h](crypto_2crypto_8h.md)>`

Perform Galois/Counter Mode (GCM) crypto operation.

Parameters
:   | ctx | Pointer to the crypto context of this op. |
    | --- | --- |
    | pkt | Structure holding the input/output, Associated Data (AD) and auth tag buffer pointers. |
    | nonce | Nonce for the operation. Same nonce value should not be reused across multiple operations (within a session context) for security. |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
