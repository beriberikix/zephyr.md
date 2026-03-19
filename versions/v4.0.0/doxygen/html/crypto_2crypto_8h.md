---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/crypto_2crypto_8h.html
original_path: doxygen/html/crypto_2crypto_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crypto.h File Reference

Crypto Cipher APIs.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/crypto/hash.h](hash_8h_source.md)>`  
`#include "[cipher.h](cipher_8h_source.md)"`

[Go to the source code of this file.](crypto_2crypto_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [crypto\_driver\_api](structcrypto__driver__api.md) |
|  | Crypto driver API definition. [More...](structcrypto__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [CAP\_OPAQUE\_KEY\_HNDL](group__crypto.md#ga821c2629510aad5d591a565767d8abbd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAP\_RAW\_KEY](group__crypto.md#ga95fd2a144207a575b2e0d24d5d6bf85a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAP\_KEY\_LOADING\_API](group__crypto.md#ga18aeace031f8b9bb4241b44f8b36f056)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAP\_INPLACE\_OPS](group__crypto.md#ga4c00d0513306fbc511fb4828108d37c8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Whether the output is placed in separate buffer or not. |
| #define | [CAP\_SEPARATE\_IO\_BUFS](group__crypto.md#ga858150378de8f024e96614a6c2f138a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAP\_SYNC\_OPS](group__crypto.md#ga469bae7c354d17ba9b22c7ce4d8e076a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | These denotes if the output (completion of a cipher\_xxx\_op) is conveyed by the op function returning, or it is conveyed by an async notification. |
| #define | [CAP\_ASYNC\_OPS](group__crypto.md#ga62492a4ce9c9274c78f3a7a915a66983)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAP\_AUTONONCE](group__crypto.md#ga6574dce552f5ba3b6f347e260a57d2f5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Whether the hardware/driver supports autononce feature. |
| #define | [CAP\_NO\_IV\_PREFIX](group__crypto.md#ga8fa14517853a8a1c4f134b5772f7d308)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Don't prefix IV to cipher blocks. |

| Functions | |
| --- | --- |
| static int | [crypto\_query\_hwcaps](group__crypto.md#gadb2c24136bb56927bb14d4cfffdd5d80) (const struct [device](structdevice.md) \*dev) |
|  | Query the crypto hardware capabilities. |
| static int | [cipher\_begin\_session](group__crypto__cipher.md#ga0720700438ba5819aa826aa37f0c4227) (const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx, enum [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) algo, enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) mode, enum [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) optype) |
|  | Setup a crypto session. |
| static int | [cipher\_free\_session](group__crypto__cipher.md#gaa818a3de1f2d6319cd21bf6b7caf7cbb) (const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx) |
|  | Cleanup a crypto session. |
| static int | [cipher\_callback\_set](group__crypto__cipher.md#gaaf0add27d9116f584e7bbc2d8f1eb39b) (const struct [device](structdevice.md) \*dev, [cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd) cb) |
|  | Registers an async crypto op completion callback with the driver. |
| static int | [cipher\_block\_op](group__crypto__cipher.md#ga05a2569f8d404593e053ce69817a457e) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt) |
|  | Perform single-block crypto operation (ECB cipher mode). |
| static int | [cipher\_cbc\_op](group__crypto__cipher.md#ga2c4ac483eb4e11110be939e669040700) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
|  | Perform Cipher Block Chaining (CBC) crypto operation. |
| static int | [cipher\_ctr\_op](group__crypto__cipher.md#gaeffb9d5dd85bf135eb2cca6d47cb373c) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv) |
|  | Perform Counter (CTR) mode crypto operation. |
| static int | [cipher\_ccm\_op](group__crypto__cipher.md#ga4886e7e1cc2fcff411066875b35b8b45) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
|  | Perform Counter with CBC-MAC (CCM) mode crypto operation. |
| static int | [cipher\_gcm\_op](group__crypto__cipher.md#ga3706b034252e40b818a782c28ba5e485) (struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce) |
|  | Perform Galois/Counter Mode (GCM) crypto operation. |
| static int | [hash\_begin\_session](group__crypto__hash.md#ga9b736d047cbfb7530ffa0bc4b64d6ad1) (const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx, enum [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) algo) |
|  | Setup a hash session. |
| static int | [hash\_free\_session](group__crypto__hash.md#gadafcd2ad79e0695245c8884b6b282508) (const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx) |
|  | Cleanup a hash session. |
| static int | [hash\_callback\_set](group__crypto__hash.md#gaa69bbf41cc150dae0d97b215862729cf) (const struct [device](structdevice.md) \*dev, [hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd) cb) |
|  | Registers an async hash completion callback with the driver. |
| static int | [hash\_compute](group__crypto__hash.md#ga761e5d0bda9937d7fa4550c876a1c387) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt) |
|  | Perform a cryptographic hash function. |
| static int | [hash\_update](group__crypto__hash.md#gaf54ee20fb1ca58764f6f301739c3ba93) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt) |
|  | Perform a cryptographic multipart hash operation. |

## Detailed Description

Crypto Cipher APIs.

This file contains the Crypto Abstraction layer APIs.

[Experimental] Users should note that the APIs can change as a part of ongoing development.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [crypto](dir_8e645738bb65aae54152153b1372b1b2.md)
- [crypto.h](crypto_2crypto_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
