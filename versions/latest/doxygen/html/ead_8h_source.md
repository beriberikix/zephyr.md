---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ead_8h_source.html
original_path: doxygen/html/ead_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ead.h

[Go to the documentation of this file.](ead_8h.md)

1/\* Copyright (c) 2023 Nordic Semiconductor ASA

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

5#include <stddef.h>

6#include <[stdint.h](stdint_8h.md)>

7

8#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_EAD\_H\_

9#define ZEPHYR\_INCLUDE\_BLUETOOTH\_EAD\_H\_

10

11#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

12#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 26](group__bt__ead.md#gae2de6773ee7179ab857f2d0eea168b88)#define BT\_EAD\_RANDOMIZER\_SIZE 5

[ 28](group__bt__ead.md#gab25e457cbc2f81738de82832f61e2353)#define BT\_EAD\_KEY\_SIZE 16

[ 30](group__bt__ead.md#ga03c2e091e276f522dd6ebbceadb56d72)#define BT\_EAD\_IV\_SIZE 8

[ 32](group__bt__ead.md#ga4f61690f24aae84871dfb461e2d32449)#define BT\_EAD\_MIC\_SIZE 4

33

[ 37](group__bt__ead.md#ga82a48e03dbbffe0e82ca80941a34a2cb)#define BT\_EAD\_ENCRYPTED\_PAYLOAD\_SIZE(payload\_size) \

38 ((payload\_size) + BT\_EAD\_RANDOMIZER\_SIZE + BT\_EAD\_MIC\_SIZE)

39

[ 43](group__bt__ead.md#ga9dbaf3919a0e47adb89e69ea7f3b89a2)#define BT\_EAD\_DECRYPTED\_PAYLOAD\_SIZE(encrypted\_payload\_size) \

44 ((encrypted\_payload\_size) - (BT\_EAD\_RANDOMIZER\_SIZE + BT\_EAD\_MIC\_SIZE))

45

[ 77](group__bt__ead.md#ga8bed2f85d63b3950fd3e19fe211a8f02)int [bt\_ead\_encrypt](group__bt__ead.md#ga8bed2f85d63b3950fd3e19fe211a8f02)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) session\_key[[BT\_EAD\_KEY\_SIZE](group__bt__ead.md#gab25e457cbc2f81738de82832f61e2353)], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iv[[BT\_EAD\_IV\_SIZE](group__bt__ead.md#ga03c2e091e276f522dd6ebbceadb56d72)],

78 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, size\_t payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encrypted\_payload);

79

[ 103](group__bt__ead.md#gaf4005550479008e5f32f5cf15200ea8e)int [bt\_ead\_decrypt](group__bt__ead.md#gaf4005550479008e5f32f5cf15200ea8e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) session\_key[[BT\_EAD\_KEY\_SIZE](group__bt__ead.md#gab25e457cbc2f81738de82832f61e2353)], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iv[[BT\_EAD\_IV\_SIZE](group__bt__ead.md#ga03c2e091e276f522dd6ebbceadb56d72)],

104 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encrypted\_payload, size\_t encrypted\_payload\_size,

105 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload);

106

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_EAD\_H\_ \*/

[bluetooth.h](bluetooth_8h.md)

Bluetooth subsystem core APIs.

[BT\_EAD\_IV\_SIZE](group__bt__ead.md#ga03c2e091e276f522dd6ebbceadb56d72)

#define BT\_EAD\_IV\_SIZE

Initialisation Vector size in bytes.

**Definition** ead.h:30

[bt\_ead\_encrypt](group__bt__ead.md#ga8bed2f85d63b3950fd3e19fe211a8f02)

int bt\_ead\_encrypt(const uint8\_t session\_key[16], const uint8\_t iv[8], const uint8\_t \*payload, size\_t payload\_size, uint8\_t \*encrypted\_payload)

Encrypt and authenticate the given advertising data.

[BT\_EAD\_KEY\_SIZE](group__bt__ead.md#gab25e457cbc2f81738de82832f61e2353)

#define BT\_EAD\_KEY\_SIZE

Key size in bytes.

**Definition** ead.h:28

[bt\_ead\_decrypt](group__bt__ead.md#gaf4005550479008e5f32f5cf15200ea8e)

int bt\_ead\_decrypt(const uint8\_t session\_key[16], const uint8\_t iv[8], const uint8\_t \*encrypted\_payload, size\_t encrypted\_payload\_size, uint8\_t \*payload)

Decrypt and authenticate the given encrypted advertising data.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [ead.h](ead_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
