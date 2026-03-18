---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__nvs__high__level__api.html
original_path: doxygen/html/group__nvs__high__level__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Non-volatile Storage APIs

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Non-volatile Storage (NVS)](group__nvs.md)

Non-volatile Storage APIs.
[More...](#details)

| Functions | |
| --- | --- |
| int | [nvs\_mount](#gab932ea2d6e933825c2378bef8c30b065) (struct [nvs\_fs](structnvs__fs.md) \*fs) |
|  | Mount an NVS file system onto the flash device specified in `fs`. |
| int | [nvs\_clear](#ga42ee9fd0d98f89dcabc5888f8b4600f0) (struct [nvs\_fs](structnvs__fs.md) \*fs) |
|  | Clear the NVS file system from flash. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_write](#ga34d40e9f63ba514d7915b72c4fef0b82) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write an entry to the file system. |
| int | [nvs\_delete](#ga5fd4175a4976e6d3ee8621ed95e0ee9e) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Delete an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_read](#ga341fd2ad029709cbb6eafde1ae88603f) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_read\_hist](#ga8e525038e353045ad6cd90607e887b0d) (struct [nvs\_fs](structnvs__fs.md) \*fs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cnt) |
|  | Read a history entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nvs\_calc\_free\_space](#ga37e5a55f0b9209c7c0c95db9e1e84715) (struct [nvs\_fs](structnvs__fs.md) \*fs) |
|  | Calculate the available free space in the file system. |

## Detailed Description

Non-volatile Storage APIs.

## Function Documentation

## [◆ ](#ga37e5a55f0b9209c7c0c95db9e1e84715)nvs\_calc\_free\_space()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) nvs\_calc\_free\_space | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[nvs.h](nvs_8h.md)>`

Calculate the available free space in the file system.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |

Returns
:   Number of bytes free. On success, it will be equal to the number of bytes that can still be written to the file system. Calculating the free space is a time consuming operation, especially on spi flash. On error, returns negative value of [errno.h](errno_8h.md "System error numbers.") defined error codes.

## [◆ ](#ga42ee9fd0d98f89dcabc5888f8b4600f0)nvs\_clear()

| int nvs\_clear | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[nvs.h](nvs_8h.md)>`

Clear the NVS file system from flash.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ERRNO | errno code if error |

## [◆ ](#ga5fd4175a4976e6d3ee8621ed95e0ee9e)nvs\_delete()

| int nvs\_delete | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* ) |

`#include <[nvs.h](nvs_8h.md)>`

Delete an entry from the file system.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |
    | id | Id of the entry to be deleted |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ERRNO | errno code if error |

## [◆ ](#gab932ea2d6e933825c2378bef8c30b065)nvs\_mount()

| int nvs\_mount | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[nvs.h](nvs_8h.md)>`

Mount an NVS file system onto the flash device specified in `fs`.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ERRNO | errno code if error |

## [◆ ](#ga341fd2ad029709cbb6eafde1ae88603f)nvs\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) nvs\_read | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[nvs.h](nvs_8h.md)>`

Read an entry from the file system.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |
    | id | Id of the entry to be read |
    | data | Pointer to data buffer |
    | len | Number of bytes to be read |

Returns
:   Number of bytes read. On success, it will be equal to the number of bytes requested to be read. When the return value is larger than the number of bytes requested to read this indicates not all bytes were read, and more data is available. On error, returns negative value of [errno.h](errno_8h.md "System error numbers.") defined error codes.

## [◆ ](#ga8e525038e353045ad6cd90607e887b0d)nvs\_read\_hist()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) nvs\_read\_hist | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cnt* ) |

`#include <[nvs.h](nvs_8h.md)>`

Read a history entry from the file system.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |
    | id | Id of the entry to be read |
    | data | Pointer to data buffer |
    | len | Number of bytes to be read |
    | cnt | History counter: 0: latest entry, 1: one before latest ... |

Returns
:   Number of bytes read. On success, it will be equal to the number of bytes requested to be read. When the return value is larger than the number of bytes requested to read this indicates not all bytes were read, and more data is available. On error, returns negative value of [errno.h](errno_8h.md "System error numbers.") defined error codes.

## [◆ ](#ga34d40e9f63ba514d7915b72c4fef0b82)nvs\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) nvs\_write | ( | struct [nvs\_fs](structnvs__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[nvs.h](nvs_8h.md)>`

Write an entry to the file system.

Note
:   When `len` parameter is equal to `0` then entry is effectively removed (it is equivalent to calling of nvs\_delete). Any calls to nvs\_read for entries with data of length `0` will return error.  
    It is not possible to distinguish between deleted entry and entry with data of length 0.

Parameters
:   | fs | Pointer to file system |
    | --- | --- |
    | id | Id of the entry to be written |
    | data | Pointer to the data to be written |
    | len | Number of bytes to be written |

Returns
:   Number of bytes written. On success, it will be equal to the number of bytes requested to be written. When a rewrite of the same data already stored is attempted, nothing is written to flash, thus 0 is returned. On error, returns negative value of [errno.h](errno_8h.md "System error numbers.") defined error codes.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
