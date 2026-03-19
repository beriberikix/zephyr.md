---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/transform_8h.html
original_path: doxygen/html/transform_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

transform.h File Reference

The secure storage ITS transform module.
[More...](#details)

`#include <[zephyr/secure_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.md)>`

[Go to the source code of this file.](transform_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SECURE\_STORAGE\_ITS\_TRANSFORM\_DATA\_SIZE](#a88f73da6f6fa94b828c589c5669164aa)(stored\_data\_len) |

| Enumerations | |
| --- | --- |
| enum | { [SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff) } |
|  | The maximum size, in bytes, of an entry's data after it has been transformed for storage. [More...](#ad83834ce1354aa3a4f9429c21ba8cf25) |

| Functions | |
| --- | --- |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_transform\_to\_store](#ac976a23f8049c4e2e5b95bf867b9ea24) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len, const void \*data, [secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd) create\_flags, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stored\_data[static [SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*stored\_data\_len) |
|  | Transforms the data of an ITS entry for storage. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_transform\_from\_store](#a25353d53a0bce5dea8fc4d42bba8988e) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stored\_data\_len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stored\_data[static [SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*data\_len, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) \*create\_flags) |
|  | Transforms and validates the stored data of an ITS entry for use. |

## Detailed Description

The secure storage ITS transform module.

The functions declared in this header implement the ITS transform module. They are meant to be called only by the ITS implementation. This header may be included when providing a custom implementation of the ITS transform module (`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_IMPLEMENTATION_CUSTOM`).

## Macro Definition Documentation

## [◆ ](#a88f73da6f6fa94b828c589c5669164aa)SECURE\_STORAGE\_ITS\_TRANSFORM\_DATA\_SIZE

| #define SECURE\_STORAGE\_ITS\_TRANSFORM\_DATA\_SIZE | ( |  | *stored\_data\_len* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(stored\_data\_len - ([SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff) \

- CONFIG\_SECURE\_STORAGE\_ITS\_MAX\_DATA\_SIZE))

[SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE](#ad83834ce1354aa3a4f9429c21ba8cf25ac2a08f5f72fa4cebf21739b8952d13ff)

@ SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE

**Definition** transform.h:17

## Enumeration Type Documentation

## [◆ ](#ad83834ce1354aa3a4f9429c21ba8cf25)anonymous enum

| anonymous enum |
| --- |

The maximum size, in bytes, of an entry's data after it has been transformed for storage.

| Enumerator | |
| --- | --- |
| SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE |  |

## Function Documentation

## [◆ ](#a25353d53a0bce5dea8fc4d42bba8988e)secure\_storage\_its\_transform\_from\_store()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_transform\_from\_store | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stored\_data\_len*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *stored\_data*[static SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_size*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *data\_len*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) \* | *create\_flags* ) |

Transforms and validates the stored data of an ITS entry for use.

Parameters
:   | [in] | uid | The entry's UID. |
    | --- | --- | --- |
    | [in] | stored\_data\_len | The number of bytes in stored\_data. |
    | [in] | stored\_data | The stored data to transform for use. |
    | [in] | data\_size | The size of data in bytes. |
    | [out] | data | The buffer to which the transformed data is written. |
    | [out] | data\_len | On success, the number of bytes written to stored\_data. |
    | [out] | create\_flags | On success, the entry's create flags. |

Returns
:   [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) on success, anything else on failure.

## [◆ ](#ac976a23f8049c4e2e5b95bf867b9ea24)secure\_storage\_its\_transform\_to\_store()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_transform\_to\_store | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len*, |
|  |  | const void \* | *data*, |
|  |  | [secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd) | *create\_flags*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *stored\_data*[static SECURE\_STORAGE\_ITS\_TRANSFORM\_MAX\_STORED\_DATA\_SIZE], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *stored\_data\_len* ) |

Transforms the data of an ITS entry for storage.

Parameters
:   | [in] | uid | The entry's UID. |
    | --- | --- | --- |
    | [in] | data\_len | The number of bytes in data. |
    | [in] | data | The data to transform for storage. |
    | [in] | create\_flags | The entry's create flags. It must contain only valid PSA\_STORAGE\_FLAG\_\* values. It gets stored as part of stored\_data. |
    | [out] | stored\_data | The buffer to which the transformed data is written. |
    | [out] | stored\_data\_len | On success, the number of bytes written to stored\_data. |

Returns
:   [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) on success, anything else on failure.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [transform.h](transform_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
