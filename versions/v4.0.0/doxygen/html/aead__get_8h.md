---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/aead__get_8h.html
original_path: doxygen/html/aead__get_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aead\_get.h File Reference

The AEAD ITS transform module API.
[More...](#details)

`#include <[zephyr/secure_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.md)>`  
`#include <psa/crypto_types.h>`

[Go to the source code of this file.](aead__get_8h_source.md)

| Functions | |
| --- | --- |
| void | [secure\_storage\_its\_transform\_aead\_get\_scheme](#abf498c228e9c8d6f32432d859b5d225e) (psa\_key\_type\_t \*key\_type, psa\_algorithm\_t \*alg) |
|  | Returns the key type and algorithm to use for the AEAD operations. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_transform\_aead\_get\_key](#a2a8cf814d206a63fd4c850da478b0077) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_KEY\_SIZE]) |
|  | Returns the encryption key to use for an ITS entry's AEAD operations. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_transform\_aead\_get\_nonce](#a2d29f8a15b7314e1b2211bbb93d5a1b2) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_NONCE\_SIZE]) |
|  | Generates a nonce for an AEAD operation. |

## Detailed Description

The AEAD ITS transform module API.

The functions declared in this header allow customization of the AEAD implementation of the ITS transform module. They are not meant to be called directly other than by the AEAD ITS transform module. This header may be included when providing a custom implementation of one or more of these functions (

```
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_*_CUSTOM
```

).

## Function Documentation

## [◆ ](#a2a8cf814d206a63fd4c850da478b0077)secure\_storage\_its\_transform\_aead\_get\_key()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_transform\_aead\_get\_key | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_KEY\_SIZE] ) |

Returns the encryption key to use for an ITS entry's AEAD operations.

Parameters
:   | [in] | uid | The UID of the ITS entry for whom the returned key is used. |
    | --- | --- | --- |
    | [out] | key | The encryption key. |

Returns
:   [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) on success, anything else on failure.

## [◆ ](#a2d29f8a15b7314e1b2211bbb93d5a1b2)secure\_storage\_its\_transform\_aead\_get\_nonce()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_transform\_aead\_get\_nonce | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *nonce*[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_NONCE\_SIZE] | ) |  |
| --- | --- | --- | --- | --- | --- |

Generates a nonce for an AEAD operation.

Parameters
:   | [out] | nonce | The generated nonce. |
    | --- | --- | --- |

Returns
:   [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) on success, anything else on failure.

## [◆ ](#abf498c228e9c8d6f32432d859b5d225e)secure\_storage\_its\_transform\_aead\_get\_scheme()

| void secure\_storage\_its\_transform\_aead\_get\_scheme | ( | psa\_key\_type\_t \* | *key\_type*, |
| --- | --- | --- | --- |
|  |  | psa\_algorithm\_t \* | *alg* ) |

Returns the key type and algorithm to use for the AEAD operations.

Parameters
:   | [out] | key\_type | The key type to use. |
    | --- | --- | --- |
    | [out] | alg | The algorithm to use. |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [transform](dir_1da836f1fbec1e542f554678ae49852f.md)
- [aead\_get.h](aead__get_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
