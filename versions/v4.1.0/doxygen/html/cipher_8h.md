---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cipher_8h.html
original_path: doxygen/html/cipher_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cipher.h File Reference

Crypto Cipher structure definitions.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](cipher_8h_source.md)

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
| typedef int(\* | [block\_op\_t](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt) |
| typedef int(\* | [cbc\_op\_t](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
| typedef int(\* | [ctr\_op\_t](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ctr) |
| typedef int(\* | [ccm\_op\_t](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
| typedef int(\* | [gcm\_op\_t](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d)) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
| typedef void(\* | [cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd)) (struct [cipher\_pkt](structcipher__pkt.md) \*completed, int status) |

| Enumerations | |
| --- | --- |
| enum | [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) { [CRYPTO\_CIPHER\_ALGO\_AES](group__crypto__cipher.md#ggaa43d9907b508cb28c649aaa524d84424aed0c05202ecbb1496f84ec6c383ddcf0) = 1 } |
|  | Cipher Algorithm. [More...](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) |
| enum | [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) { [CRYPTO\_CIPHER\_OP\_DECRYPT](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a1e1205f695285034b4889ac19a191617) = 0 , [CRYPTO\_CIPHER\_OP\_ENCRYPT](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a71bf6ee186bab1729e24e37c119d0019) = 1 } |
|  | Cipher Operation. [More...](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) |
| enum | [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) {     [CRYPTO\_CIPHER\_MODE\_ECB](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e) = 1 , [CRYPTO\_CIPHER\_MODE\_CBC](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd) = 2 , [CRYPTO\_CIPHER\_MODE\_CTR](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2) = 3 , [CRYPTO\_CIPHER\_MODE\_CCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b) = 4 ,     [CRYPTO\_CIPHER\_MODE\_GCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12) = 5   } |
|  | Possible cipher mode options. [More...](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) |

## Detailed Description

Crypto Cipher structure definitions.

This file contains the Crypto Abstraction layer structures.

[Experimental] Users should note that the Structures can change as a part of ongoing development.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [crypto](dir_8e645738bb65aae54152153b1372b1b2.md)
- [cipher.h](cipher_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
