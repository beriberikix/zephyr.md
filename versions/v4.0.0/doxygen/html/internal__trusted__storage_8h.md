---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/internal__trusted__storage_8h.html
original_path: doxygen/html/internal__trusted__storage_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

internal\_trusted\_storage.h File Reference

[Operating System Services](group__os__services.md) » [PSA Secure Storage API](group__psa__secure__storage.md)

The PSA Internal Trusted Storage (ITS) API.
[More...](#details)

`#include <[psa/storage_common.h](storage__common_8h_source.md)>`

[Go to the source code of this file.](internal__trusted__storage_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PSA\_ITS\_API\_VERSION\_MAJOR](#a7eacf1684848e1b3bbe5cdaec2b4572d)   1 |
| #define | [PSA\_ITS\_API\_VERSION\_MINOR](#ad6886b2f339df083e21afe24109d8471)   0 |

| Functions | |
| --- | --- |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_its\_set](#a01e5344273e6d776d1f456c4d54a2ed8) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags) |
|  | Creates a new or modifies an existing entry. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_its\_get](#a387d450b2a21673fba6c56e66c74b5f7) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, void \*p\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*p\_data\_length) |
|  | Retrieves data associated with the provided uid. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_its\_get\_info](#ae4efe6e7f9088fdf8ef4e126045a432b) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info) |
|  | Retrieves the metadata of a given entry. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [psa\_its\_remove](#abd70b9f9bc063e3651f315408f4ae04c) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid) |
|  | Removes the provided uid and its associated data. |

## Detailed Description

The PSA Internal Trusted Storage (ITS) API.

For more information on the ITS, see [The Internal Trusted Storage API](https://arm-software.github.io/psa-api/storage/1.0/overview/architecture.html#the-internal-trusted-storage-api).

## Macro Definition Documentation

## [◆ ](#a7eacf1684848e1b3bbe5cdaec2b4572d)PSA\_ITS\_API\_VERSION\_MAJOR

| #define PSA\_ITS\_API\_VERSION\_MAJOR   1 |
| --- |

## [◆ ](#ad6886b2f339df083e21afe24109d8471)PSA\_ITS\_API\_VERSION\_MINOR

| #define PSA\_ITS\_API\_VERSION\_MINOR   0 |
| --- |

## Function Documentation

## [◆ ](#a387d450b2a21673fba6c56e66c74b5f7)psa\_its\_get()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_its\_get | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
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
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more of the arguments are invalid. This can also happen if data\_offset is larger than the size of the data associated with uid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

## [◆ ](#ae4efe6e7f9088fdf8ef4e126045a432b)psa\_its\_get\_info()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_its\_get\_info | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
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
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more of the arguments are invalid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

## [◆ ](#abd70b9f9bc063e3651f315408f4ae04c)psa\_its\_remove()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_its\_remove | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid* | ) |  |
| --- | --- | --- | --- | --- | --- |

Removes the provided uid and its associated data.

Deletes all the data associated with the entry from internal storage.

Parameters
:   | uid | The identifier of the entry to remove. |
    | --- | --- |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_NOT\_PERMITTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a4d1b8dd8526177a15a210b7afc1accb1) | The entry was created with [PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd "The data associated with the UID will not be able to be modified or deleted."). |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | uid is invalid. |
    | [PSA\_ERROR\_DOES\_NOT\_EXIST](subsys_2secure__storage_2include_2psa_2error_8h.md#a18646babb2ae6cbde02ea3828bbd9141) | The provided uid was not found in the storage. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

## [◆ ](#a01e5344273e6d776d1f456c4d54a2ed8)psa\_its\_set()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) psa\_its\_set | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *p\_data*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | *create\_flags* ) |

Creates a new or modifies an existing entry.

Stores data in the internal storage.

Parameters
:   | uid | The identifier of the data. Must be nonzero. |
    | --- | --- |
    | data\_length | The size in bytes of the data in p\_data to store. |
    | p\_data | A buffer containing the data to store. |
    | create\_flags | Flags indicating the properties of the entry. |

Return values
:   | [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) | The operation completed successfully. |
    | --- | --- |
    | [PSA\_ERROR\_NOT\_PERMITTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a4d1b8dd8526177a15a210b7afc1accb1) | An entry associated with the provided uid already exists and was created with [PSA\_STORAGE\_FLAG\_WRITE\_ONCE](storage__common_8h.md#a15dbec8d862073de6024924bf015dcdd "The data associated with the UID will not be able to be modified or deleted."). |
    | [PSA\_ERROR\_NOT\_SUPPORTED](subsys_2secure__storage_2include_2psa_2error_8h.md#a1dcc6d130633ed5db8942257581b55dd) | One or more of the flags provided in create\_flags are not supported or invalid. |
    | [PSA\_ERROR\_INVALID\_ARGUMENT](subsys_2secure__storage_2include_2psa_2error_8h.md#a798df25a505ebf931f7bec1f80f1f85f) | One or more arguments other than create\_flags are invalid. |
    | [PSA\_ERROR\_INSUFFICIENT\_STORAGE](subsys_2secure__storage_2include_2psa_2error_8h.md#a897a45eb206a6f6b7be7ffbe36f0d766) | There is insufficient space on the storage medium. |
    | [PSA\_ERROR\_STORAGE\_FAILURE](subsys_2secure__storage_2include_2psa_2error_8h.md#add169a1af2707862b95fb9df91dfc37d) | The physical storage has failed (fatal error). |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [psa](dir_d06fbc62883e41d574c8881d2ac75d4f.md)
- [internal\_trusted\_storage.h](internal__trusted__storage_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
