---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bluetooth_2crypto_8h.html
original_path: doxygen/html/bluetooth_2crypto_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crypto.h File Reference

Bluetooth subsystem crypto APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](bluetooth_2crypto_8h_source.md)

| Functions | |
| --- | --- |
| int | [bt\_rand](group__bt__crypto.md#ga2c85d3563547017ae97f22993272fb29) (void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generate random data. |
| int | [bt\_encrypt\_le](group__bt__crypto.md#ga54d34c154deaf5b6f1523de15ddec18f) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plaintext[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enc\_data[16]) |
|  | AES encrypt little-endian data. |
| int | [bt\_encrypt\_be](group__bt__crypto.md#gab93f5833e39b39e388bf40ba5c60d60f) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plaintext[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) enc\_data[16]) |
|  | AES encrypt big-endian data. |
| int | [bt\_ccm\_decrypt](group__bt__crypto.md#ga413a29883453982f0da13590dd493166) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[13], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*enc\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*aad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) aad\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*plaintext, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mic\_size) |
|  | Decrypt big-endian data with AES-CCM. |
| int | [bt\_ccm\_encrypt](group__bt__crypto.md#ga7235be4697031ca6a0e535bdd707d3e1) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) nonce[13], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*plaintext, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*aad, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) aad\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*enc\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mic\_size) |
|  | Encrypt big-endian data with AES-CCM. |

## Detailed Description

Bluetooth subsystem crypto APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [crypto.h](bluetooth_2crypto_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
