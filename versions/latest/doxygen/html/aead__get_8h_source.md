---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/aead__get_8h_source.html
original_path: doxygen/html/aead__get_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aead\_get.h

[Go to the documentation of this file.](aead__get_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_GET\_H

5#define SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_GET\_H

6

15#include <[zephyr/secure\_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)>

16#include <psa/crypto\_types.h>

17

[ 23](aead__get_8h.md#abf498c228e9c8d6f32432d859b5d225e)void [secure\_storage\_its\_transform\_aead\_get\_scheme](aead__get_8h.md#abf498c228e9c8d6f32432d859b5d225e)(psa\_key\_type\_t \*key\_type, psa\_algorithm\_t \*alg);

24

[ 32](aead__get_8h.md#a2a8cf814d206a63fd4c850da478b0077)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_transform\_aead\_get\_key](aead__get_8h.md#a2a8cf814d206a63fd4c850da478b0077)(

33 [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid,

34 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_KEY\_SIZE]);

35

[ 42](aead__get_8h.md#a2d29f8a15b7314e1b2211bbb93d5a1b2)[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) [secure\_storage\_its\_transform\_aead\_get\_nonce](aead__get_8h.md#a2d29f8a15b7314e1b2211bbb93d5a1b2)(

43 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_NONCE\_SIZE]);

44

45#endif

[secure\_storage\_its\_transform\_aead\_get\_key](aead__get_8h.md#a2a8cf814d206a63fd4c850da478b0077)

psa\_status\_t secure\_storage\_its\_transform\_aead\_get\_key(secure\_storage\_its\_uid\_t uid, uint8\_t key[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_KEY\_SIZE])

Returns the encryption key to use for an ITS entry's AEAD operations.

[secure\_storage\_its\_transform\_aead\_get\_nonce](aead__get_8h.md#a2d29f8a15b7314e1b2211bbb93d5a1b2)

psa\_status\_t secure\_storage\_its\_transform\_aead\_get\_nonce(uint8\_t nonce[static CONFIG\_SECURE\_STORAGE\_ITS\_TRANSFORM\_AEAD\_NONCE\_SIZE])

Generates a nonce for an AEAD operation.

[secure\_storage\_its\_transform\_aead\_get\_scheme](aead__get_8h.md#abf498c228e9c8d6f32432d859b5d225e)

void secure\_storage\_its\_transform\_aead\_get\_scheme(psa\_key\_type\_t \*key\_type, psa\_algorithm\_t \*alg)

Returns the key type and algorithm to use for the AEAD operations.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md)

The UID (caller + entry IDs) of an ITS entry.

**Definition** common.h:26

[common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h.md)

Common definitions of the secure storage subsystem's ITS APIs.

[psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9)

int32\_t psa\_status\_t

**Definition** error.h:13

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
