---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/store_8h.html
original_path: doxygen/html/store_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

store.h File Reference

The secure storage ITS store module.
[More...](#details)

`#include <[zephyr/secure_storage/its/common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2its_2common_8h_source.md)>`

[Go to the source code of this file.](store_8h_source.md)

| Functions | |
| --- | --- |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_store\_set](#aed06855314e4dafb4e935d31b6fb21bb) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_length, const void \*data) |
|  | Writes the data of an ITS entry to the storage medium. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_store\_get](#a22d16815fb645ff5cc014f2fe4e9e987) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_size, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*data\_length) |
|  | Retrieves the data of an ITS entry from the storage medium. |
| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) | [secure\_storage\_its\_store\_remove](#a58eb126f3d92112b3ed19d1920d43fa0) ([secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) uid) |
|  | Removes an ITS entry from the storage medium. |

## Detailed Description

The secure storage ITS store module.

The functions declared in this header implement the ITS store module. They are meant to be called only by the ITS implementation. This header may be included when providing a custom implementation of the ITS store module (

```
CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_CUSTOM
```

).

## Function Documentation

## [◆ ](#a22d16815fb645ff5cc014f2fe4e9e987)secure\_storage\_its\_store\_get()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_store\_get | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_size*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *data\_length* ) |

Retrieves the data of an ITS entry from the storage medium.

Parameters
:   | [in] | uid | The entry's UID. |
    | --- | --- | --- |
    | [in] | data\_size | The size of data in bytes. |
    | [out] | data | The buffer to which the entry's stored data is written. |
    | [out] | data\_length | On success, the number of bytes written to data. May be less than data\_size. |

Return values
:   | `PSA\_SUCCESS` | on success. |
    | --- | --- |
    | `PSA\_ERROR\_DOES\_NOT\_EXIST` | if no entry with the given UID exists. |
    | `PSA\_ERROR\_STORAGE\_FAILURE` | on any other failure. |

## [◆ ](#a58eb126f3d92112b3ed19d1920d43fa0)secure\_storage\_its\_store\_remove()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_store\_remove | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid* | ) |  |
| --- | --- | --- | --- | --- | --- |

Removes an ITS entry from the storage medium.

Parameters
:   | uid | The entry's UID. |
    | --- | --- |

Returns
:   [PSA\_SUCCESS](subsys_2secure__storage_2include_2psa_2error_8h.md#a4cc859e2c66ca381c7418db3527a65e1) on success, anything else on failure.

## [◆ ](#aed06855314e4dafb4e935d31b6fb21bb)secure\_storage\_its\_store\_set()

| [psa\_status\_t](subsys_2secure__storage_2include_2psa_2error_8h.md#a05676e70ba5c6a7565aff3c36677c1f9) secure\_storage\_its\_store\_set | ( | [secure\_storage\_its\_uid\_t](structsecure__storage__its__uid__t.md) | *uid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_length*, |
|  |  | const void \* | *data* ) |

Writes the data of an ITS entry to the storage medium.

Parameters
:   | uid | The entry's UID. |
    | --- | --- |
    | data\_length | The number of bytes in data. |
    | data | The data to store. |

Return values
:   | `PSA\_SUCCESS` | on success. |
    | --- | --- |
    | `PSA\_ERROR\_INSUFFICIENT\_STORAGE` | if there is insufficient storage space. |
    | `PSA\_ERROR\_STORAGE\_FAILURE` | on any other failure. |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [its](dir_8ffdb9b26f60d93440ec7ee1d2751029.md)
- [store.h](store_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
