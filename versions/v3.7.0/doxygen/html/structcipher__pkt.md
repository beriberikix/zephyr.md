---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcipher__pkt.html
original_path: doxygen/html/structcipher__pkt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cipher\_pkt Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md) » [Cipher](group__crypto__cipher.md)

Structure encoding IO parameters of one cryptographic operation like encrypt/decrypt.
[More...](#details)

`#include <[cipher.h](cipher_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [in\_buf](#a56d2de56d9efc153032eb7f6503748ba) |
|  | Start address of input buffer. |
| int | [in\_len](#ac5c98e7edafb4b61e01f707c785afbea) |
|  | Bytes to be operated upon. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [out\_buf](#ab95bae428d3d3c80b1b8ee6ea03a05d0) |
|  | Start of the output buffer, to be allocated by the application. |
| int | [out\_buf\_max](#a6e51f941334e87cc966f5a37e783d1fc) |
|  | Size of the out\_buf area allocated by the application. |
| int | [out\_len](#abc9588a5f84f9daa13ce4aec965f0a91) |
|  | To be populated by driver on return from cipher\_xxx\_op() and holds the size of the actual result. |
| struct [cipher\_ctx](structcipher__ctx.md) \* | [ctx](#a26fb877d705580648da03ce95264d100) |
|  | Context this packet relates to. |

## Detailed Description

Structure encoding IO parameters of one cryptographic operation like encrypt/decrypt.

The fields which has not been explicitly called out has to be filled up by the app before making the cipher\_xxx\_op() call.

## Field Documentation

## [◆ ](#a26fb877d705580648da03ce95264d100)ctx

| struct [cipher\_ctx](structcipher__ctx.md)\* cipher\_pkt::ctx |
| --- |

Context this packet relates to.

This can be useful to get the session details, especially for async ops. Will be populated by the cipher\_xxx\_op() API based on the ctx parameter.

## [◆ ](#a56d2de56d9efc153032eb7f6503748ba)in\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* cipher\_pkt::in\_buf |
| --- |

Start address of input buffer.

## [◆ ](#ac5c98e7edafb4b61e01f707c785afbea)in\_len

| int cipher\_pkt::in\_len |
| --- |

Bytes to be operated upon.

## [◆ ](#ab95bae428d3d3c80b1b8ee6ea03a05d0)out\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* cipher\_pkt::out\_buf |
| --- |

Start of the output buffer, to be allocated by the application.

Can be NULL for in-place ops. To be populated with contents by the driver on return from op / async callback.

## [◆ ](#a6e51f941334e87cc966f5a37e783d1fc)out\_buf\_max

| int cipher\_pkt::out\_buf\_max |
| --- |

Size of the out\_buf area allocated by the application.

Drivers should not write past the size of output buffer.

## [◆ ](#abc9588a5f84f9daa13ce4aec965f0a91)out\_len

| int cipher\_pkt::out\_len |
| --- |

To be populated by driver on return from cipher\_xxx\_op() and holds the size of the actual result.

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[cipher.h](cipher_8h_source.md)

- [cipher\_pkt](structcipher__pkt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
