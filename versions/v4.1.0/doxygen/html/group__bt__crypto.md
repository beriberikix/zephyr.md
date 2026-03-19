---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__crypto.html
original_path: doxygen/html/group__bt__crypto.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Cryptography

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Cryptography.
[More...](#details)

| Functions | |
| --- | --- |
| int | [bt\_rand](#ga2c85d3563547017ae97f22993272fb29) (void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generate random data. |
| int | [bt\_encrypt\_le](#ga54d34c154deaf5b6f1523de15ddec18f) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plaintext[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enc\_data[16]) |
|  | AES encrypt little-endian data. |
| int | [bt\_encrypt\_be](#gab93f5833e39b39e388bf40ba5c60d60f) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plaintext[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enc\_data[16]) |
|  | AES encrypt big-endian data. |
| int | [bt\_ccm\_decrypt](#ga413a29883453982f0da13590dd493166) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[13], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*enc\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*aad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) aad\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*plaintext, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mic\_size) |
|  | Decrypt big-endian data with AES-CCM. |
| int | [bt\_ccm\_encrypt](#ga7235be4697031ca6a0e535bdd707d3e1) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[13], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*plaintext, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*aad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) aad\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*enc\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mic\_size) |
|  | Encrypt big-endian data with AES-CCM. |

## Detailed Description

Cryptography.

## Function Documentation

## [◆ ](#ga413a29883453982f0da13590dd493166)bt\_ccm\_decrypt()

| int bt\_ccm\_decrypt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16], |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *nonce*[13], |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *enc\_data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *aad*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *aad\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *plaintext*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *mic\_size* ) |

`#include <[crypto.h](bluetooth_2crypto_8h.md)>`

Decrypt big-endian data with AES-CCM.

Decrypts and authorizes `enc_data` with AES-CCM, as described in [https://tools.ietf.org/html/rfc3610](https://tools.ietf.org/html/rfc3610).

Assumes that the MIC follows directly after the encrypted data.

Parameters
:   | key | 128 bit MS byte first key |
    | --- | --- |
    | nonce | 13 byte MS byte first nonce |
    | enc\_data | Encrypted data |
    | len | Length of the encrypted data |
    | aad | Additional authenticated data |
    | aad\_len | Additional authenticated data length |
    | plaintext | Plaintext buffer to place result in |
    | mic\_size | Size of the trailing MIC (in bytes) |

Return values
:   | 0 | Successfully decrypted the data. |
    | --- | --- |
    | -EINVAL | Invalid parameters. |
    | -EBADMSG | Authentication failed. |

## [◆ ](#ga7235be4697031ca6a0e535bdd707d3e1)bt\_ccm\_encrypt()

| int bt\_ccm\_encrypt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16], |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *nonce*[13], |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *plaintext*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *aad*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *aad\_len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *enc\_data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *mic\_size* ) |

`#include <[crypto.h](bluetooth_2crypto_8h.md)>`

Encrypt big-endian data with AES-CCM.

Encrypts and generates a MIC from `plaintext` with AES-CCM, as described in [https://tools.ietf.org/html/rfc3610](https://tools.ietf.org/html/rfc3610).

Places the MIC directly after the encrypted data.

Parameters
:   | key | 128 bit MS byte first key |
    | --- | --- |
    | nonce | 13 byte MS byte first nonce |
    | plaintext | Plaintext buffer to encrypt |
    | len | Length of the encrypted data |
    | aad | Additional authenticated data |
    | aad\_len | Additional authenticated data length |
    | enc\_data | Buffer to place encrypted data in |
    | mic\_size | Size of the trailing MIC (in bytes) |

Return values
:   | 0 | Successfully encrypted the data. |
    | --- | --- |
    | -EINVAL | Invalid parameters. |

## [◆ ](#gab93f5833e39b39e388bf40ba5c60d60f)bt\_encrypt\_be()

| int bt\_encrypt\_be | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16], |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *plaintext*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *enc\_data*[16] ) |

`#include <[crypto.h](bluetooth_2crypto_8h.md)>`

AES encrypt big-endian data.

An AES encrypt helper is used to request the Bluetooth controller's own hardware to encrypt the plaintext using the key and returns the encrypted data.

Parameters
:   | key | 128 bit MS byte first key for the encryption of the plaintext |
    | --- | --- |
    | plaintext | 128 bit MS byte first plaintext data block to be encrypted |
    | enc\_data | 128 bit MS byte first encrypted data block |

Returns
:   Zero on success or error code otherwise.

## [◆ ](#ga54d34c154deaf5b6f1523de15ddec18f)bt\_encrypt\_le()

| int bt\_encrypt\_le | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16], |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *plaintext*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *enc\_data*[16] ) |

`#include <[crypto.h](bluetooth_2crypto_8h.md)>`

AES encrypt little-endian data.

An AES encrypt helper is used to request the Bluetooth controller's own hardware to encrypt the plaintext using the key and returns the encrypted data.

Parameters
:   | key | 128 bit LS byte first key for the encryption of the plaintext |
    | --- | --- |
    | plaintext | 128 bit LS byte first plaintext data block to be encrypted |
    | enc\_data | 128 bit LS byte first encrypted data block |

Returns
:   Zero on success or error code otherwise.

## [◆ ](#ga2c85d3563547017ae97f22993272fb29)bt\_rand()

| int bt\_rand | ( | void \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crypto.h](bluetooth_2crypto_8h.md)>`

Generate random data.

A random number generation helper which utilizes the Bluetooth controller's own RNG.

Parameters
:   | buf | Buffer to insert the random data |
    | --- | --- |
    | len | Length of random data to generate |

Returns
:   Zero on success or error code otherwise, positive in case of protocol error or negative (POSIX) in case of stack internal error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
