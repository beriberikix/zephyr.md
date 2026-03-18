---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcrypto__driver__api.html
original_path: doxygen/html/structcrypto__driver__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crypto\_driver\_api Struct Reference

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md)

Crypto driver API definition.
[More...](#details)

`#include <[crypto.h](crypto_2crypto_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [query\_hw\_caps](#a19859cdd9185f5d333fe6893efc27967) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [cipher\_begin\_session](#af2ddc3aa1447dbef500715e1ea4dd780) )(const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx, enum [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) algo, enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) mode, enum [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) op\_type) |
| int(\* | [cipher\_free\_session](#a77f9e6ab2b527c4433ddf5cbcf6b8dca) )(const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx) |
| int(\* | [cipher\_async\_callback\_set](#a2c59735e94df3e8740611937c6ed1c2f) )(const struct [device](structdevice.md) \*dev, [cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd) cb) |
| int(\* | [hash\_begin\_session](#a48845d14ff94ff16633227d10f971f57) )(const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx, enum [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) algo) |
| int(\* | [hash\_free\_session](#aa3033ec374a10abd180af38f6fdc080b) )(const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx) |
| int(\* | [hash\_async\_callback\_set](#a87d5891e9ce4a76ed50c7591ae7a27ff) )(const struct [device](structdevice.md) \*dev, [hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd) cb) |

## Detailed Description

Crypto driver API definition.

## Field Documentation

## [◆ ](#a2c59735e94df3e8740611937c6ed1c2f)cipher\_async\_callback\_set

| int(\* crypto\_driver\_api::cipher\_async\_callback\_set) (const struct [device](structdevice.md) \*dev, [cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd) cb) |
| --- |

## [◆ ](#af2ddc3aa1447dbef500715e1ea4dd780)cipher\_begin\_session

| int(\* crypto\_driver\_api::cipher\_begin\_session) (const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx, enum [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) algo, enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) mode, enum [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) op\_type) |
| --- |

## [◆ ](#a77f9e6ab2b527c4433ddf5cbcf6b8dca)cipher\_free\_session

| int(\* crypto\_driver\_api::cipher\_free\_session) (const struct [device](structdevice.md) \*dev, struct [cipher\_ctx](structcipher__ctx.md) \*ctx) |
| --- |

## [◆ ](#a87d5891e9ce4a76ed50c7591ae7a27ff)hash\_async\_callback\_set

| int(\* crypto\_driver\_api::hash\_async\_callback\_set) (const struct [device](structdevice.md) \*dev, [hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd) cb) |
| --- |

## [◆ ](#a48845d14ff94ff16633227d10f971f57)hash\_begin\_session

| int(\* crypto\_driver\_api::hash\_begin\_session) (const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx, enum [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) algo) |
| --- |

## [◆ ](#aa3033ec374a10abd180af38f6fdc080b)hash\_free\_session

| int(\* crypto\_driver\_api::hash\_free\_session) (const struct [device](structdevice.md) \*dev, struct [hash\_ctx](structhash__ctx.md) \*ctx) |
| --- |

## [◆ ](#a19859cdd9185f5d333fe6893efc27967)query\_hw\_caps

| int(\* crypto\_driver\_api::query\_hw\_caps) (const struct [device](structdevice.md) \*dev) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/crypto/[crypto.h](crypto_2crypto_8h_source.md)

- [crypto\_driver\_api](structcrypto__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
