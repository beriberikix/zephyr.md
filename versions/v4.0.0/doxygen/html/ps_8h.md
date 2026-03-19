---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ps_8h.html
original_path: doxygen/html/ps_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ps.h File Reference

The secure storage PS implementation.
[More...](#details)

`#include <[psa/storage_common.h](storage__common_8h_source.md)>`

[Go to the source code of this file.](ps_8h_source.md)

| Functions | |
| --- | --- |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_ps\_set](#ab0be3c9374c1db65b45c43fdc6c05825) (const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*p\_data, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags) |
|  | See [psa\_ps\_set()](protected__storage_8h.md#ac27f8fc33b69e0a9ed09b73195b42eab "Creates a new or modifies an existing entry."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_ps\_get](#a0387828802c41350b9572a1555ecdeac) (const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, void \*p\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*p\_data\_length) |
|  | See [psa\_ps\_get()](protected__storage_8h.md#a2ad1b8347d8cf174c028f0c485a66db6 "Retrieves data associated with the provided uid."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_ps\_get\_info](#af6c6741b58d91798e2a9c2b3644f0bf1) (const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \*p\_info) |
|  | See [psa\_ps\_get\_info()](protected__storage_8h.md#af716b24d0761837d1c7b70042bd4966f "Retrieves the metadata of a given entry."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_ps\_remove](#aef4fa69c85d80640a909868ad1749e8c) (const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid) |
|  | See [psa\_ps\_remove()](protected__storage_8h.md#a147a92d8387de36c32a8ede10d6d9a02 "Removes the provided uid and its associated data."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_ps\_create](#ae044a9d36445840539578b9ea3a1e4d0) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) capacity, [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) create\_flags) |
|  | See [psa\_ps\_create()](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508 "Reserves storage for the provided uid."), to which this function is analogous. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_ps\_set\_extended](#ab1612b91d341295578e16eb64d7035c4) ([psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*p\_data) |
|  | See [psa\_ps\_set\_extended()](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a "Writes part of the data associated with the provided uid."), to which this function is analogous. |

## Detailed Description

The secure storage PS implementation.

The functions declared in this header implement the PSA PS API when the secure storage subsystem is enabled. They must not be called directly, and this header must not be included other than when providing a custom implementation (

```
CONFIG_SECURE_STORAGE_PS_IMPLEMENTATION_CUSTOM
```

).

## Function Documentation

## [◆ ](#ae044a9d36445840539578b9ea3a1e4d0)secure\_storage\_ps\_create()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_ps\_create | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *capacity*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | *create\_flags* ) |

See [psa\_ps\_create()](protected__storage_8h.md#aa2c4d67afd77676a95becad71e902508 "Reserves storage for the provided uid."), to which this function is analogous.

## [◆ ](#a0387828802c41350b9572a1555ecdeac)secure\_storage\_ps\_get()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_ps\_get | ( | const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | void \* | *p\_data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *p\_data\_length* ) |

See [psa\_ps\_get()](protected__storage_8h.md#a2ad1b8347d8cf174c028f0c485a66db6 "Retrieves data associated with the provided uid."), to which this function is analogous.

## [◆ ](#af6c6741b58d91798e2a9c2b3644f0bf1)secure\_storage\_ps\_get\_info()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_ps\_get\_info | ( | const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | struct [psa\_storage\_info\_t](structpsa__storage__info__t.md) \* | *p\_info* ) |

See [psa\_ps\_get\_info()](protected__storage_8h.md#af716b24d0761837d1c7b70042bd4966f "Retrieves the metadata of a given entry."), to which this function is analogous.

## [◆ ](#aef4fa69c85d80640a909868ad1749e8c)secure\_storage\_ps\_remove()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_ps\_remove | ( | const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid* | ) |  |
| --- | --- | --- | --- | --- | --- |

See [psa\_ps\_remove()](protected__storage_8h.md#a147a92d8387de36c32a8ede10d6d9a02 "Removes the provided uid and its associated data."), to which this function is analogous.

## [◆ ](#ab0be3c9374c1db65b45c43fdc6c05825)secure\_storage\_ps\_set()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_ps\_set | ( | const [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *p\_data*, |
|  |  | [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | *create\_flags* ) |

See [psa\_ps\_set()](protected__storage_8h.md#ac27f8fc33b69e0a9ed09b73195b42eab "Creates a new or modifies an existing entry."), to which this function is analogous.

## [◆ ](#ab1612b91d341295578e16eb64d7035c4)secure\_storage\_ps\_set\_extended()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_ps\_set\_extended | ( | [psa\_storage\_uid\_t](storage__common_8h.md#ae9154910f4f350c3b467b55d541a21a6) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *p\_data* ) |

See [psa\_ps\_set\_extended()](protected__storage_8h.md#a1630b75fce6941c4d619256822d5de9a "Writes part of the data associated with the provided uid."), to which this function is analogous.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [ps.h](ps_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
