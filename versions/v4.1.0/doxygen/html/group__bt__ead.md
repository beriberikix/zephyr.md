---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__ead.html
original_path: doxygen/html/group__bt__ead.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Encrypted Advertising Data (EAD)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Encrypted Advertising Data (EAD).
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88)   5 |
|  | Randomizer size in bytes. |
| #define | [BT\_EAD\_KEY\_SIZE](#gab25e457cbc2f81738de82832f61e2353)   16 |
|  | Key size in bytes. |
| #define | [BT\_EAD\_IV\_SIZE](#ga03c2e091e276f522dd6ebbceadb56d72)   8 |
|  | Initialisation Vector size in bytes. |
| #define | [BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449)   4 |
|  | MIC size in bytes. |
| #define | [BT\_EAD\_ENCRYPTED\_PAYLOAD\_SIZE](#ga82a48e03dbbffe0e82ca80941a34a2cb)(payload\_size) |
|  | Get the size (in bytes) of the encrypted advertising data for a given payload size in bytes. |
| #define | [BT\_EAD\_DECRYPTED\_PAYLOAD\_SIZE](#ga9dbaf3919a0e47adb89e69ea7f3b89a2)(encrypted\_payload\_size) |
|  | Get the size (in bytes) of the decrypted payload for a given payload size in bytes. |

| Functions | |
| --- | --- |
| int | [bt\_ead\_encrypt](#ga8bed2f85d63b3950fd3e19fe211a8f02) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) session\_key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iv[8], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encrypted\_payload) |
|  | Encrypt and authenticate the given advertising data. |
| int | [bt\_ead\_decrypt](#gaf4005550479008e5f32f5cf15200ea8e) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) session\_key[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iv[8], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*encrypted\_payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) encrypted\_payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload) |
|  | Decrypt and authenticate the given encrypted advertising data. |

## Detailed Description

Encrypted Advertising Data (EAD).

## Macro Definition Documentation

## [◆ ](#ga9dbaf3919a0e47adb89e69ea7f3b89a2)BT\_EAD\_DECRYPTED\_PAYLOAD\_SIZE

| #define BT\_EAD\_DECRYPTED\_PAYLOAD\_SIZE | ( |  | *encrypted\_payload\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ead.h](ead_8h.md)>`

**Value:**

((encrypted\_payload\_size) - ([BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88) + [BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449)))

[BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449)

#define BT\_EAD\_MIC\_SIZE

MIC size in bytes.

**Definition** ead.h:32

[BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88)

#define BT\_EAD\_RANDOMIZER\_SIZE

Randomizer size in bytes.

**Definition** ead.h:26

Get the size (in bytes) of the decrypted payload for a given payload size in bytes.

## [◆ ](#ga82a48e03dbbffe0e82ca80941a34a2cb)BT\_EAD\_ENCRYPTED\_PAYLOAD\_SIZE

| #define BT\_EAD\_ENCRYPTED\_PAYLOAD\_SIZE | ( |  | *payload\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ead.h](ead_8h.md)>`

**Value:**

((payload\_size) + [BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88) + [BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449))

Get the size (in bytes) of the encrypted advertising data for a given payload size in bytes.

## [◆ ](#ga03c2e091e276f522dd6ebbceadb56d72)BT\_EAD\_IV\_SIZE

| #define BT\_EAD\_IV\_SIZE   8 |
| --- |

`#include <[ead.h](ead_8h.md)>`

Initialisation Vector size in bytes.

## [◆ ](#gab25e457cbc2f81738de82832f61e2353)BT\_EAD\_KEY\_SIZE

| #define BT\_EAD\_KEY\_SIZE   16 |
| --- |

`#include <[ead.h](ead_8h.md)>`

Key size in bytes.

## [◆ ](#ga4f61690f24aae84871dfb461e2d32449)BT\_EAD\_MIC\_SIZE

| #define BT\_EAD\_MIC\_SIZE   4 |
| --- |

`#include <[ead.h](ead_8h.md)>`

MIC size in bytes.

## [◆ ](#gae2de6773ee7179ab857f2d0eea168b88)BT\_EAD\_RANDOMIZER\_SIZE

| #define BT\_EAD\_RANDOMIZER\_SIZE   5 |
| --- |

`#include <[ead.h](ead_8h.md)>`

Randomizer size in bytes.

## Function Documentation

## [◆ ](#gaf4005550479008e5f32f5cf15200ea8e)bt\_ead\_decrypt()

| int bt\_ead\_decrypt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *session\_key*[16], |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *iv*[8], |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *encrypted\_payload*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *encrypted\_payload\_size*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload* ) |

`#include <[ead.h](ead_8h.md)>`

Decrypt and authenticate the given encrypted advertising data.

Note
:   The term advertising structure is used to describe the advertising data with the advertising type and the length of those two.

Parameters
:   | [in] | session\_key | Key of 16 bytes used for the encryption. |
    | --- | --- | --- |
    | [in] | iv | Initialisation Vector used to generate the nonce. |
    | [in] | encrypted\_payload | Encrypted Advertising Data received. This should only contain the advertising data from the received advertising structure, not the length nor the type. |
    | [in] | encrypted\_payload\_size | Size of the received advertising data in bytes. Should be equal to the length field of the received advertising structure, minus the size of the type (1 byte). |
    | [out] | payload | Decrypted advertising payload. Use [BT\_EAD\_DECRYPTED\_PAYLOAD\_SIZE](#ga9dbaf3919a0e47adb89e69ea7f3b89a2) to get the right size. |

Return values
:   | 0 | Data have been correctly decrypted and authenticated. |
    | --- | --- |
    | -EIO | Error occurred during the decryption or the authentication. |
    | -EINVAL | One of the argument is a NULL pointer or `encrypted_payload_size` is less than [BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88) + [BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449). |

## [◆ ](#ga8bed2f85d63b3950fd3e19fe211a8f02)bt\_ead\_encrypt()

| int bt\_ead\_encrypt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *session\_key*[16], |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *iv*[8], |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *payload\_size*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *encrypted\_payload* ) |

`#include <[ead.h](ead_8h.md)>`

Encrypt and authenticate the given advertising data.

The resulting data in `encrypted_payload` will look like that:

- Randomizer is added in the [BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88) first bytes;
- Encrypted payload is added ( `payload_size` bytes);
- MIC is added in the last [BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449) bytes.

Attention
:   The function must be called each time the RPA is updated or the data are modified.

Note
:   The term advertising structure is used to describe the advertising data with the advertising type and the length of those two.

Parameters
:   | [in] | session\_key | Key of [BT\_EAD\_KEY\_SIZE](#gab25e457cbc2f81738de82832f61e2353) bytes used for the encryption. |
    | --- | --- | --- |
    | [in] | iv | Initialisation Vector used to generate the nonce. It must be changed each time the Session Key changes. |
    | [in] | payload | Advertising Data to encrypt. Can be multiple advertising structures that are concatenated. |
    | [in] | payload\_size | Size of the Advertising Data to encrypt. |
    | [out] | encrypted\_payload | Encrypted Ad Data including the Randomizer and the MIC. Size must be at least [BT\_EAD\_RANDOMIZER\_SIZE](#gae2de6773ee7179ab857f2d0eea168b88) + `payload_size` + [BT\_EAD\_MIC\_SIZE](#ga4f61690f24aae84871dfb461e2d32449). Use [BT\_EAD\_ENCRYPTED\_PAYLOAD\_SIZE](#ga82a48e03dbbffe0e82ca80941a34a2cb) to get the right size. |

Return values
:   | 0 | Data have been correctly encrypted and authenticated. |
    | --- | --- |
    | -EIO | Error occurred during the encryption or the authentication. |
    | -EINVAL | One of the argument is a NULL pointer. |
    | -ECANCELED | Error occurred during the random number generation. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
