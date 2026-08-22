---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/bluetooth_2crypto_8h_source.html
original_path: doxygen/html/bluetooth_2crypto_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crypto.h

[Go to the documentation of this file.](bluetooth_2crypto_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017-2020 Nordic Semiconductor ASA

7 \* Copyright (c) 2015-2017 Intel Corporation

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_CRYPTO\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_CRYPTO\_H\_

13

20

21#include <[stdbool.h](stdbool_8h.md)>

22#include <stddef.h>

23#include <[stdint.h](stdint_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 40](group__bt__crypto.md#ga2c85d3563547017ae97f22993272fb29)int [bt\_rand](group__bt__crypto.md#ga2c85d3563547017ae97f22993272fb29)(void \*buf, size\_t len);

41

[ 54](group__bt__crypto.md#ga54d34c154deaf5b6f1523de15ddec18f)int [bt\_encrypt\_le](group__bt__crypto.md#ga54d34c154deaf5b6f1523de15ddec18f)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plaintext[16],

55 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enc\_data[16]);

56

[ 69](group__bt__crypto.md#gab93f5833e39b39e388bf40ba5c60d60f)int [bt\_encrypt\_be](group__bt__crypto.md#gab93f5833e39b39e388bf40ba5c60d60f)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plaintext[16],

70 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enc\_data[16]);

71

72

[ 93](group__bt__crypto.md#ga413a29883453982f0da13590dd493166)int [bt\_ccm\_decrypt](group__bt__crypto.md#ga413a29883453982f0da13590dd493166)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[13], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*enc\_data,

94 size\_t len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*aad, size\_t aad\_len,

95 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*plaintext, size\_t mic\_size);

96

97

[ 117](group__bt__crypto.md#ga7235be4697031ca6a0e535bdd707d3e1)int [bt\_ccm\_encrypt](group__bt__crypto.md#ga7235be4697031ca6a0e535bdd707d3e1)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[13],

118 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*plaintext, size\_t len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*aad,

119 size\_t aad\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*enc\_data, size\_t mic\_size);

120

121#ifdef \_\_cplusplus

122}

123#endif

127

128#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_CRYPTO\_H\_ \*/

[bt\_rand](group__bt__crypto.md#ga2c85d3563547017ae97f22993272fb29)

int bt\_rand(void \*buf, size\_t len)

Generate random data.

[bt\_ccm\_decrypt](group__bt__crypto.md#ga413a29883453982f0da13590dd493166)

int bt\_ccm\_decrypt(const uint8\_t key[16], uint8\_t nonce[13], const uint8\_t \*enc\_data, size\_t len, const uint8\_t \*aad, size\_t aad\_len, uint8\_t \*plaintext, size\_t mic\_size)

Decrypt big-endian data with AES-CCM.

[bt\_encrypt\_le](group__bt__crypto.md#ga54d34c154deaf5b6f1523de15ddec18f)

int bt\_encrypt\_le(const uint8\_t key[16], const uint8\_t plaintext[16], uint8\_t enc\_data[16])

AES encrypt little-endian data.

[bt\_ccm\_encrypt](group__bt__crypto.md#ga7235be4697031ca6a0e535bdd707d3e1)

int bt\_ccm\_encrypt(const uint8\_t key[16], uint8\_t nonce[13], const uint8\_t \*plaintext, size\_t len, const uint8\_t \*aad, size\_t aad\_len, uint8\_t \*enc\_data, size\_t mic\_size)

Encrypt big-endian data with AES-CCM.

[bt\_encrypt\_be](group__bt__crypto.md#gab93f5833e39b39e388bf40ba5c60d60f)

int bt\_encrypt\_be(const uint8\_t key[16], const uint8\_t plaintext[16], uint8\_t enc\_data[16])

AES encrypt big-endian data.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [crypto.h](bluetooth_2crypto_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
