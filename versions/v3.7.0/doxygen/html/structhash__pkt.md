---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhash__pkt.html
original_path: doxygen/html/structhash__pkt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_pkt Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md) » [Hash](group__crypto__hash.md)

Structure encoding IO parameters of a hash operation.
[More...](#details)

`#include <[hash.h](hash_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [in\_buf](#a80d73d3c64718a62213a7fb857e3c5ce) |
|  | Start address of input buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [in\_len](#a06c516ec59f233a2090fb37eb0476652) |
|  | Bytes to be operated upon. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [out\_buf](#ac86c2221c6ebe7c3e568c6d72b91ff43) |
|  | Start of the output buffer, to be allocated by the application. |
| struct [hash\_ctx](structhash__ctx.md) \* | [ctx](#ab5b3ffd87a11ce3838178b2e652d49b9) |
|  | Context this packet relates to. |

## Detailed Description

Structure encoding IO parameters of a hash operation.

The fields which has not been explicitly called out has to be filled up by the app before calling [hash\_compute()](group__crypto__hash.md#ga761e5d0bda9937d7fa4550c876a1c387 "Perform a cryptographic hash function.").

## Field Documentation

## [◆ ](#ab5b3ffd87a11ce3838178b2e652d49b9)ctx

| struct [hash\_ctx](structhash__ctx.md)\* hash\_pkt::ctx |
| --- |

Context this packet relates to.

This can be useful to get the session details, especially for async ops.

## [◆ ](#a80d73d3c64718a62213a7fb857e3c5ce)in\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* hash\_pkt::in\_buf |
| --- |

Start address of input buffer.

## [◆ ](#a06c516ec59f233a2090fb37eb0476652)in\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hash\_pkt::in\_len |
| --- |

Bytes to be operated upon.

## [◆ ](#ac86c2221c6ebe7c3e568c6d72b91ff43)out\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* hash\_pkt::out\_buf |
| --- |

Start of the output buffer, to be allocated by the application.

Can be NULL for in-place ops. To be populated with contents by the driver on return from op / async callback.

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[hash.h](hash_8h_source.md)

- [hash\_pkt](structhash__pkt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
