---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/key__ids_8h.html
original_path: doxygen/html/key__ids_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

key\_ids.h File Reference

This file defines the key ID ranges of the existing users of the PSA Crypto API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](key__ids_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_BEGIN](#a3e8bcbe8554a07e045a7330196c8a003)   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x20000 |
|  | PSA key ID range to be used by OpenThread. |
| #define | [ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_SIZE](#a484d6a1af8ccc3a869b9a2b7753d1c2c)   0x10000 /\* 64 Ki \*/ |
| #define | [ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_BEGIN](#ae4606ebca8aa09c0096897c927981cb6)   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x30000 |
|  | PSA key ID range to be used by Matter. |
| #define | [ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_SIZE](#a6b459be7f0d6d39cd6bf8d482473b23f)   0x10000 /\* 64 Ki \*/ |
| #define | [ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_BEGIN](#a032913d751fddc7a6a0ac3f98229947d)   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x20000000 |
|  | PSA key ID range to be used by Bluetooth Mesh. |
| #define | [ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_SIZE](#a6b1b95861f2a8b9b9f45e0c8dee04007)   0xC000 /\* 48 Ki \*/ |
| #define | [ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_BEGIN](#ac02d47ca235e44f30e5fa32aa5cbfadc)   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x20010000 |
|  | PSA key ID range to be used by Wi-Fi credentials management. |
| #define | [ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_SIZE](#a86a47e671a632befdce9b201a66002d5)   0x100 /\* 256 \*/ |
| #define | [ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_BEGIN](#af0f6e7d2b0798aaaccc3fb3bd12d1b8a)   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x30000000 |
|  | PSA key ID range to be used by the end-user application. |
| #define | [ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_SIZE](#ad222fd0bf1eb32eaa23d6bd52d300125)   0x100000 /\* 1 Mi \*/ |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b) |

## Detailed Description

This file defines the key ID ranges of the existing users of the PSA Crypto API.

In addition to the application, different subsystems store and use persistent keys through the PSA Crypto API. Because they are not aware of each other, collisions are avoided by having them use different ID ranges. This file acts as the registry of all the allocated PSA key ID ranges within Zephyr.

The end-user application also has a dedicated range, [ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_BEGIN](#af0f6e7d2b0798aaaccc3fb3bd12d1b8a).

Some of the IDs below are based on previously existing and used values, while others are chosen to be somewhere in the PSA user key ID range to try to avoid collisions (avoiding, for example, the very beginning of the range).

## Macro Definition Documentation

## [◆ ](#af0f6e7d2b0798aaaccc3fb3bd12d1b8a)ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_BEGIN

| #define ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_BEGIN   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x30000000 |
| --- |

PSA key ID range to be used by the end-user application.

## [◆ ](#ad222fd0bf1eb32eaa23d6bd52d300125)ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_SIZE

| #define ZEPHYR\_PSA\_APPLICATION\_KEY\_ID\_RANGE\_SIZE   0x100000 /\* 1 Mi \*/ |
| --- |

## [◆ ](#a032913d751fddc7a6a0ac3f98229947d)ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_BEGIN

| #define ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_BEGIN   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x20000000 |
| --- |

PSA key ID range to be used by Bluetooth Mesh.

## [◆ ](#a6b1b95861f2a8b9b9f45e0c8dee04007)ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_SIZE

| #define ZEPHYR\_PSA\_BT\_MESH\_KEY\_ID\_RANGE\_SIZE   0xC000 /\* 48 Ki \*/ |
| --- |

## [◆ ](#ae4606ebca8aa09c0096897c927981cb6)ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_BEGIN

| #define ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_BEGIN   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x30000 |
| --- |

PSA key ID range to be used by Matter.

The base ID is equal to the default value upstream: [https://github.com/project-chip/connectedhomeip/blob/v1.4.0.0/src/crypto/CHIPCryptoPALPSA.h#L55](https://github.com/project-chip/connectedhomeip/blob/v1.4.0.0/src/crypto/CHIPCryptoPALPSA.h#L55)

## [◆ ](#a6b459be7f0d6d39cd6bf8d482473b23f)ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_SIZE

| #define ZEPHYR\_PSA\_MATTER\_KEY\_ID\_RANGE\_SIZE   0x10000 /\* 64 Ki \*/ |
| --- |

## [◆ ](#a3e8bcbe8554a07e045a7330196c8a003)ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_BEGIN

| #define ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_BEGIN   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x20000 |
| --- |

PSA key ID range to be used by OpenThread.

The base ID is equal to the default value upstream: [https://github.com/openthread/openthread/blob/thread-reference-20230706/src/core/config/platform.h#L138](https://github.com/openthread/openthread/blob/thread-reference-20230706/src/core/config/platform.h#L138)

## [◆ ](#a484d6a1af8ccc3a869b9a2b7753d1c2c)ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_SIZE

| #define ZEPHYR\_PSA\_OPENTHREAD\_KEY\_ID\_RANGE\_SIZE   0x10000 /\* 64 Ki \*/ |
| --- |

## [◆ ](#ac02d47ca235e44f30e5fa32aa5cbfadc)ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_BEGIN

| #define ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_BEGIN   ([psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b))0x20010000 |
| --- |

PSA key ID range to be used by Wi-Fi credentials management.

## [◆ ](#a86a47e671a632befdce9b201a66002d5)ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_SIZE

| #define ZEPHYR\_PSA\_WIFI\_CREDENTIALS\_KEY\_ID\_RANGE\_SIZE   0x100 /\* 256 \*/ |
| --- |

## Typedef Documentation

## [◆ ](#a11e986351c65bd3dc3c0fe2cd9926e4b)psa\_key\_id\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [psa\_key\_id\_t](#a11e986351c65bd3dc3c0fe2cd9926e4b) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [psa](dir_2e753b890c44631130dcc36a0ce9c9fd.md)
- [key\_ids.h](key__ids_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
