---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ead_8h.html
original_path: doxygen/html/ead_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ead.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

[Go to the source code of this file.](ead_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_EAD\_RANDOMIZER\_SIZE](group__bt__ead.md#gae2de6773ee7179ab857f2d0eea168b88)   5 |
|  | Randomizer size in bytes. |
| #define | [BT\_EAD\_KEY\_SIZE](group__bt__ead.md#gab25e457cbc2f81738de82832f61e2353)   16 |
|  | Key size in bytes. |
| #define | [BT\_EAD\_IV\_SIZE](group__bt__ead.md#ga03c2e091e276f522dd6ebbceadb56d72)   8 |
|  | Initialisation Vector size in bytes. |
| #define | [BT\_EAD\_MIC\_SIZE](group__bt__ead.md#ga4f61690f24aae84871dfb461e2d32449)   4 |
|  | MIC size in bytes. |
| #define | [BT\_EAD\_ENCRYPTED\_PAYLOAD\_SIZE](group__bt__ead.md#ga82a48e03dbbffe0e82ca80941a34a2cb)(payload\_size) |
|  | Get the size (in bytes) of the encrypted advertising data for a given payload size in bytes. |
| #define | [BT\_EAD\_DECRYPTED\_PAYLOAD\_SIZE](group__bt__ead.md#ga9dbaf3919a0e47adb89e69ea7f3b89a2)(encrypted\_payload\_size) |
|  | Get the size (in bytes) of the decrypted payload for a given payload size in bytes. |

| Functions | |
| --- | --- |
| int | [bt\_ead\_encrypt](group__bt__ead.md#ga8bed2f85d63b3950fd3e19fe211a8f02) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) session\_key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iv[8], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encrypted\_payload) |
|  | Encrypt and authenticate the given advertising data. |
| int | [bt\_ead\_decrypt](group__bt__ead.md#gaf4005550479008e5f32f5cf15200ea8e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) session\_key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iv[8], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encrypted\_payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) encrypted\_payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload) |
|  | Decrypt and authenticate the given encrypted advertising data. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [ead.h](ead_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
