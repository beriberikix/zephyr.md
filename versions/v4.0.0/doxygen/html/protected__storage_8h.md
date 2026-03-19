---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/protected__storage_8h.html
original_path: doxygen/html/protected__storage_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

protected\_storage.h File Reference

[Operating System Services](group__os__services.md) » [PSA Secure Storage API](group__psa__secure__storage.md)

The PSA Protected Storage (PS) API.
[More...](#details)

`#include <[psa/storage_common.h](storage__common_8h_source.md)>`

[Go to the source code of this file.](protected__storage_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PSA\_PS\_API\_VERSION\_MAJOR](#a97b66d0647ab7536fba2d6267e8fccef)   1 |
| #define | [PSA\_PS\_API\_VERSION\_MINOR](#adf9faa1eb9f9ed6fa8595c6718f89a5d)   0 |

| Functions | |
| --- | --- |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_ps\_set](#ac27f8fc33b69e0a9ed09b73195b42eab) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags) |
|  | Creates a new or modifies an existing entry. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_ps\_get](#a2ad1b8347d8cf174c028f0c485a66db6) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, void \*p\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*p\_data\_length) |
|  | Retrieves data associated with the provided uid. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_ps\_get\_info](#af716b24d0761837d1c7b70042bd4966f) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info) |
|  | Retrieves the metadata of a given entry. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_ps\_remove](#a147a92d8387de36c32a8ede10d6d9a02) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid) |
|  | Removes the provided uid and its associated data. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_ps\_create](#aa2c4d67afd77676a95becad71e902508) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) capacity, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags) |
|  | Reserves storage for the provided uid. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_ps\_set\_extended](#a1630b75fce6941c4d619256822d5de9a) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*p\_data) |
|  | Writes part of the data associated with the provided uid. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [psa\_ps\_get\_support](#a7e1725cb412be305bd21e3e1af8c2312) (void) |
|  | Lists optional features. |

## Detailed Description

The PSA Protected Storage (PS) API.

For more information on the PS, see [The Protected Storage API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-protected-storage-api).

## Macro Definition Documentation

## [◆ ](#a97b66d0647ab7536fba2d6267e8fccef)PSA\_PS\_API\_VERSION\_MAJOR

| #define PSA\_PS\_API\_VERSION\_MAJOR   1 |
| --- |

## [◆ ](#adf9faa1eb9f9ed6fa8595c6718f89a5d)PSA\_PS\_API\_VERSION\_MINOR

| #define PSA\_PS\_API\_VERSION\_MINOR   0 |
| --- |

## Function Documentation

## [◆ ](#aa2c4d67afd77676a95becad71e902508)psa\_ps\_create()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_ps\_create | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *capacity*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | *create\_flags* ) |

Reserves storage for the provided uid.

Upon success, the capacity of the storage for uid will be capacity, and the size will be 0. It is only necessary to call this function for data that will be written with the [psa\_ps\_set\_extended()](#a1630b75fce6941c4d619256822d5de9a) function. If only the [psa\_ps\_set()](#ac27f8fc33b69e0a9ed09b73195b42eab) function is used, calls to this function are redundant. This function cannot be used to replace or resize an existing entry.

Parameters
:   | uid | The identifier of the entry to reserve storage for. |
    | --- | --- |
    | capacity | The capacity, in bytes, to allocate. |
    | create\_flags | Flags indicating the properties of the entry. |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_GENERIC\_ERROR](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f) | An unspecified internal failure happened. |
    | [PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd) | The implementation doesn't support this function or one or more of the flags provided in create\_flags are not supported or invalid. |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | uid is invalid. |
    | [PSA\_ERROR\_ALREADY\_EXISTS](subsys_2secure__storage_2include_2psa_2error_8h.md#af2b34cc87edc72f3ba90071a08210d20) | An entry with the provided uid already exists. |
    | [PSA\_ERROR\_INSUFFICIENT\_STORAGE](subsys_2secure__storage_2include_2psa_2error_8h.md#a897a45eb206a6f6b7be7ffbe36f0d766) | There is insufficient space on the storage medium. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

## [◆ ](#a2ad1b8347d8cf174c028f0c485a66db6)psa\_ps\_get()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_ps\_get | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_size*, |
|  |  | void \* | *p\_data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *p\_data\_length* ) |

Retrieves data associated with the provided uid.

Parameters
:   | [in] | uid | The identifier of the data. |
    | --- | --- | --- |
    | [in] | data\_offset | The offset, in bytes, from which to start reading the data. |
    | [in] | data\_size | The number of bytes to read. |
    | [out] | p\_data | The buffer where the data will be placed on success. Must be at least data\_size bytes long. |
    | [out] | p\_data\_length | On success, the number of bytes placed in p\_data. |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_GENERIC\_ERROR](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f) | An unspecified internal failure happened. |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more of the arguments are invalid. This can also happen if data\_offset is larger than the size of the data associated with uid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |
    | [PSA\_ERROR\_INVALID\_SIGNATURE](subsys_2secure__storage_2include_2psa_2error_8h.md#a35927f755d232c4766de600f2c49e9f2) | The data associated with uid failed authentication. |
    | [PSA\_ERROR\_DATA\_CORRUPT](subsys_2secure__storage_2include_2psa_2error_8h.md#a9febb81a44bdeb4c6c42bf4f697b13bf) | The data associated with uid is corrupt. |

## [◆ ](#af716b24d0761837d1c7b70042bd4966f)psa\_ps\_get\_info()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_ps\_get\_info | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \* | *p\_info* ) |

Retrieves the metadata of a given entry.

Parameters
:   | [in] | uid | The identifier of the entry. |
    | --- | --- | --- |
    | [out] | p\_info | A pointer to a [psa\_storage\_info\_t](structpsa__storage__info__t.md "Metadata associated with a specific entry.") struct that will be populated with the metadata on success. |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_GENERIC\_ERROR](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f) | An unspecified internal failure happened. |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more of the arguments are invalid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |
    | [PSA\_ERROR\_INVALID\_SIGNATURE](subsys_2secure__storage_2include_2psa_2error_8h.md#a35927f755d232c4766de600f2c49e9f2) | The data associated with uid failed authentication. |
    | [PSA\_ERROR\_DATA\_CORRUPT](subsys_2secure__storage_2include_2psa_2error_8h.md#a9febb81a44bdeb4c6c42bf4f697b13bf) | The data associated with uid is corrupt. |

## [◆ ](#a7e1725cb412be305bd21e3e1af8c2312)psa\_ps\_get\_support()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) psa\_ps\_get\_support | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Lists optional features.

Returns
:   A bitmask with flags set for the optional features supported by the implementation. Currently defined flags are limited to [PSA\_STORAGE\_SUPPORT\_SET\_EXTENDED](storage__common_8h.md#ad9f16fc478036752ffb2ce9e50b2a710 "Flag indicating that psa_ps_create() and psa_ps_set_extended() are supported.").

## [◆ ](#a147a92d8387de36c32a8ede10d6d9a02)psa\_ps\_remove()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_ps\_remove | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid* | ) |  |
| --- | --- | --- | --- | --- | --- |

Removes the provided uid and its associated data.

Deletes previously stored data and any associated metadata, including rollback protection data.

Parameters
:   | uid | The identifier of the entry to remove. |
    | --- | --- |

Returns
:   A status indicating the success/failure of the operation

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_GENERIC\_ERROR](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f) | An unspecified internal failure happened. |
    | [PSA\_ERROR\_NOT\_PERMITTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a4d1b8dd8526177a15a210b7afc1accb1) | The entry was created with [PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd "The data associated with the UID will not be able to be modified or deleted."). |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | uid is invalid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

## [◆ ](#ac27f8fc33b69e0a9ed09b73195b42eab)psa\_ps\_set()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_ps\_set | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *p\_data*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | *create\_flags* ) |

Creates a new or modifies an existing entry.

Parameters
:   | uid | The identifier of the data. Must be nonzero. |
    | --- | --- |
    | data\_length | The size in bytes of the data in p\_data to store. |
    | p\_data | A buffer containing the data to store. |
    | create\_flags | Flags indicating the properties of the entry. |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_GENERIC\_ERROR](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f) | An unspecified internal failure happened. |
    | [PSA\_ERROR\_NOT\_PERMITTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a4d1b8dd8526177a15a210b7afc1accb1) | An entry associated with the provided uid already exists and was created with [PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd "The data associated with the UID will not be able to be modified or deleted."). |
    | [PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd) | One or more of the flags provided in create\_flags are not supported or invalid. |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more arguments other than create\_flags are invalid. |
    | [PSA\_ERROR\_INSUFFICIENT\_STORAGE](subsys_2secure__storage_2include_2psa_2error_8h.md#a897a45eb206a6f6b7be7ffbe36f0d766) | There is insufficient space on the storage medium. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

## [◆ ](#a1630b75fce6941c4d619256822d5de9a)psa\_ps\_set\_extended()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_ps\_set\_extended | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *p\_data* ) |

Writes part of the data associated with the provided uid.

Before calling this function, storage must have been reserved with a call to [psa\_ps\_create()](#aa2c4d67afd77676a95becad71e902508). This function can also be used to overwrite data that was written with [psa\_ps\_set()](#ac27f8fc33b69e0a9ed09b73195b42eab). This function can overwrite existing data and/or extend it up to the capacity of the entry specified in [psa\_ps\_create()](#aa2c4d67afd77676a95becad71e902508), but cannot create gaps.

Parameters
:   | uid | The identifier of the entry to write. |
    | --- | --- |
    | data\_offset | The offset, in bytes, from which to start writing the data. Can be at most the current size of the data. |
    | data\_length | The size in bytes of the data in p\_data to write. data\_offset  - data\_length can be at most the capacity of the entry. |
    | p\_data | A buffer containing the data to write. |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_GENERIC\_ERROR](subsys_2secure__storage_2include_2psa_2error_8h.md#a8bfafd6baac18ce5d3192d1de256238f) | An unspecified internal failure happened. |
    | [PSA\_ERROR\_NOT\_PERMITTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a4d1b8dd8526177a15a210b7afc1accb1) | The entry was created with [PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd "The data associated with the UID will not be able to be modified or deleted."). |
    | [PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd) | The implementation doesn't support this function. |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more of the arguments are invalid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |
    | [PSA\_ERROR\_INVALID\_SIGNATURE](subsys_2secure__storage_2include_2psa_2error_8h.md#a35927f755d232c4766de600f2c49e9f2) | The data associated with uid failed authentication. |
    | [PSA\_ERROR\_DATA\_CORRUPT](subsys_2secure__storage_2include_2psa_2error_8h.md#a9febb81a44bdeb4c6c42bf4f697b13bf) | The data associated with uid is corrupt. |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [protected\_storage.h](protected__storage_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
