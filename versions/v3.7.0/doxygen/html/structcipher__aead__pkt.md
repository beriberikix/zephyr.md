---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcipher__aead__pkt.html
original_path: doxygen/html/structcipher__aead__pkt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cipher\_aead\_pkt Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md) » [Cipher](group__crypto__cipher.md)

Structure encoding IO parameters in AEAD (Authenticated Encryption with Associated Data) scenario like in CCM.
[More...](#details)

`#include <[cipher.h](cipher_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [cipher\_pkt](structcipher__pkt.md) \* | [pkt](#a4953711ca04b1c1d17980fff03561d03) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [ad](#a1b00939c8409041b8202ae90ee01a41c) |
|  | Start address for Associated Data. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ad\_len](#a2964d6ffbe02b7088be9a2d5c21a2f9c) |
|  | Size of Associated Data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [tag](#a3c7a3e72c7d21ec574dd777ac0bdf3c4) |
|  | Start address for the auth hash. |

## Detailed Description

Structure encoding IO parameters in AEAD (Authenticated Encryption with Associated Data) scenario like in CCM.

App has to furnish valid contents prior to making [cipher\_ccm\_op()](group__crypto__cipher.md#ga4886e7e1cc2fcff411066875b35b8b45 "Perform Counter with CBC-MAC (CCM) mode crypto operation.") call.

## Field Documentation

## [◆ ](#a1b00939c8409041b8202ae90ee01a41c)ad

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* cipher\_aead\_pkt::ad |
| --- |

Start address for Associated Data.

This has to be supplied by app.

## [◆ ](#a2964d6ffbe02b7088be9a2d5c21a2f9c)ad\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cipher\_aead\_pkt::ad\_len |
| --- |

Size of Associated Data.

This has to be supplied by the app.

## [◆ ](#a4953711ca04b1c1d17980fff03561d03)pkt

| struct [cipher\_pkt](structcipher__pkt.md)\* cipher\_aead\_pkt::pkt |
| --- |

## [◆ ](#a3c7a3e72c7d21ec574dd777ac0bdf3c4)tag

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* cipher\_aead\_pkt::tag |
| --- |

Start address for the auth hash.

For an encryption op this will be populated by the driver when it returns from cipher\_ccm\_op call. For a decryption op this has to be supplied by the app.

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[cipher.h](cipher_8h_source.md)

- [cipher\_aead\_pkt](structcipher__aead__pkt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
