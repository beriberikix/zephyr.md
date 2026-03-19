---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__zms__high__level__api.html
original_path: doxygen/html/group__zms__high__level__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ZMS API

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Zephyr Memory Storage (ZMS)](group__zms.md)

| Functions | |
| --- | --- |
| int | [zms\_mount](#ga962625b12f21cf030a35c944a2de380e) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Mount a ZMS file system onto the device specified in fs. |
| int | [zms\_clear](#gafe06d28af34fbecf2bd666ef11095ed1) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Clear the ZMS file system from device. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_write](#ga327d83b5cdc6dbd12fc7b0d0f4ea4ee8) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write an entry to the file system. |
| int | [zms\_delete](#gacc98554728353b2d3a2e55c23a8f4746) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Delete an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_read](#ga99d451d07e5603a22996ac7960fed196) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read an entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_read\_hist](#ga1b899562d98bf088c05d9fd8b5904d81) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Read a history entry from the file system. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_get\_data\_length](#gafcc5b2f75f19c042b0f08192fac16b4a) (struct [zms\_fs](structzms__fs.md) \*fs, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Gets the length of the data that is stored in an entry with a given id. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zms\_calc\_free\_space](#ga02be33c18632687133f53557b5ee8bc2) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Calculate the available free space in the file system. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [zms\_active\_sector\_free\_space](#gab9ace837cff289d4ec492541dba298fa) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Tell how much contiguous free space remains in the currently active ZMS sector. |
| int | [zms\_sector\_use\_next](#ga90a6f8c47f02641ca33ee42a7c709750) (struct [zms\_fs](structzms__fs.md) \*fs) |
|  | Close the currently active sector and switch to the next one. |

## Detailed Description

## Function Documentation

## [◆ ](#gab9ace837cff289d4ec492541dba298fa)zms\_active\_sector\_free\_space()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) zms\_active\_sector\_free\_space | ( | struct [zms\_fs](structzms__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zms.h](zms_8h.md)>`

Tell how much contiguous free space remains in the currently active ZMS sector.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |

Return values
:   | >=0 | Number of free bytes in the currently active sector |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |

## [◆ ](#ga02be33c18632687133f53557b5ee8bc2)zms\_calc\_free\_space()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zms\_calc\_free\_space | ( | struct [zms\_fs](structzms__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zms.h](zms_8h.md)>`

Calculate the available free space in the file system.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |

Returns
:   Number of free bytes. On success, it will be equal to the number of bytes that can still be written to the file system. Calculating the free space is a time-consuming operation, especially on SPI flash. On error, returns negative value of error codes defined in [errno.h](errno_8h.md "System error numbers.").

Return values
:   | Number | of free bytes (>= 0) on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -EIO | if there is a memory read/write error. |

## [◆ ](#gafe06d28af34fbecf2bd666ef11095ed1)zms\_clear()

| int zms\_clear | ( | struct [zms\_fs](structzms__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zms.h](zms_8h.md)>`

Clear the ZMS file system from device.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EACCES | if fs is not mounted. |
    | -ENXIO | if there is a device error. |
    | -EIO | if there is a memory read/write error. |

## [◆ ](#gacc98554728353b2d3a2e55c23a8f4746)zms\_delete()

| int zms\_delete | ( | struct [zms\_fs](structzms__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[zms.h](zms_8h.md)>`

Delete an entry from the file system.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |
    | id | ID of the entry to be deleted. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -ENXIO | if there is a device error. |
    | -EIO | if there is a memory read/write error. |

## [◆ ](#gafcc5b2f75f19c042b0f08192fac16b4a)zms\_get\_data\_length()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zms\_get\_data\_length | ( | struct [zms\_fs](structzms__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id* ) |

`#include <[zms.h](zms_8h.md)>`

Gets the length of the data that is stored in an entry with a given id.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |
    | id | ID of the entry whose data length to retrieve. |

Returns
:   Data length contained in the ATE. On success, it will be equal to the number of bytes in the ATE. On error, returns negative value of error codes defined in [errno.h](errno_8h.md "System error numbers.").

Return values
:   | Length | of the entry with the given id (> 0) on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -EIO | if there is a memory read/write error. |
    | -ENOENT | if there is no entry with the given id and history counter. |

## [◆ ](#ga962625b12f21cf030a35c944a2de380e)zms\_mount()

| int zms\_mount | ( | struct [zms\_fs](structzms__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zms.h](zms_8h.md)>`

Mount a ZMS file system onto the device specified in fs.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOTSUP | if the detected file system is not ZMS. |
    | -EPROTONOSUPPORT | if the ZMS version is not supported. |
    | -EINVAL | if any of the flash parameters or the sector layout is invalid. |
    | -ENXIO | if there is a device error. |
    | -EIO | if there is a memory read/write error. |

## [◆ ](#ga99d451d07e5603a22996ac7960fed196)zms\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zms\_read | ( | struct [zms\_fs](structzms__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[zms.h](zms_8h.md)>`

Read an entry from the file system.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |
    | id | ID of the entry to be read. |
    | data | Pointer to data buffer. |
    | len | Number of bytes to read at most. |

Returns
:   Number of bytes read. On success, it will be equal to the number of bytes requested to be read or less than that if the stored data has a smaller size than the requested one. On error, returns negative value of error codes defined in [errno.h](errno_8h.md "System error numbers.").

Return values
:   | Number | of bytes read (> 0) on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -EIO | if there is a memory read/write error. |
    | -ENOENT | if there is no entry with the given id. |

## [◆ ](#ga1b899562d98bf088c05d9fd8b5904d81)zms\_read\_hist()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zms\_read\_hist | ( | struct [zms\_fs](structzms__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cnt* ) |

`#include <[zms.h](zms_8h.md)>`

Read a history entry from the file system.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |
    | id | ID of the entry to be read. |
    | data | Pointer to data buffer. |
    | len | Number of bytes to be read. |
    | cnt | History counter: 0: latest entry, 1: one before latest ... |

Returns
:   Number of bytes read. On success, it will be equal to the number of bytes requested to be read. When the return value is larger than the number of bytes requested to read this indicates not all bytes were read, and more data is available. On error, returns negative value of error codes defined in [errno.h](errno_8h.md "System error numbers.").

Return values
:   | Number | of bytes read (> 0) on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -EIO | if there is a memory read/write error. |
    | -ENOENT | if there is no entry with the given id and history counter. |

## [◆ ](#ga90a6f8c47f02641ca33ee42a7c709750)zms\_sector\_use\_next()

| int zms\_sector\_use\_next | ( | struct [zms\_fs](structzms__fs.md) \* | *fs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zms.h](zms_8h.md)>`

Close the currently active sector and switch to the next one.

Note
:   The garbage collector is called on the new sector.

Warning
:   This routine is made available for specific use cases. It collides with ZMS's goal of avoiding any unnecessary flash erase operations. Using this routine extensively can result in premature failure of the flash device.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -EIO | if there is a memory read/write error. |

## [◆ ](#ga327d83b5cdc6dbd12fc7b0d0f4ea4ee8)zms\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zms\_write | ( | struct [zms\_fs](structzms__fs.md) \* | *fs*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *id*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[zms.h](zms_8h.md)>`

Write an entry to the file system.

Note
:   When the len parameter is equal to 0 the entry is effectively removed (it is equivalent to calling [zms\_delete()](#gacc98554728353b2d3a2e55c23a8f4746)). It is not possible to distinguish between a deleted entry and an entry with data of length 0.

Parameters
:   | fs | Pointer to the file system. |
    | --- | --- |
    | id | ID of the entry to be written. |
    | data | Pointer to the data to be written. |
    | len | Number of bytes to be written (maximum 64 KiB). |

Returns
:   Number of bytes written. On success, it will be equal to the number of bytes requested to be written or 0. When a rewrite of the same data already stored is attempted, nothing is written to flash, thus 0 is returned. On error, returns negative value of error codes defined in [errno.h](errno_8h.md "System error numbers.").

Return values
:   | Number | of bytes written (len or 0) on success. |
    | --- | --- |
    | -EACCES | if ZMS is still not initialized. |
    | -ENXIO | if there is a device error. |
    | -EIO | if there is a memory read/write error. |
    | -EINVAL | if len is invalid. |
    | -ENOSPC | if no space is left on the device. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
