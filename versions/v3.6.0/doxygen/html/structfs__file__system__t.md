---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structfs__file__system__t.html
original_path: doxygen/html/structfs__file__system__t.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_file\_system\_t Struct Reference

[Operating System Services](group__os__services.md) » [File System APIs](group__file__system__api.md)

File System interface structure.
[More...](#details)

`#include <[fs_sys.h](fs__sys_8h_source.md)>`

| Data Fields | |
| --- | --- |
| File operations | |
| int(\* | [open](#a40b11c282d3b8c30fe1e2d9cc98edd69) )(struct [fs\_file\_t](structfs__file__t.md) \*filp, const char \*fs\_path, [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Opens or creates a file, depending on flags given. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [read](#a8efb04845dbec830f12435a6472b7015) )(struct [fs\_file\_t](structfs__file__t.md) \*filp, void \*dest, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nbytes) |
|  | Reads nbytes number of bytes. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [write](#a1039b25b44bc8be1daea19c0d489c0db) )(struct [fs\_file\_t](structfs__file__t.md) \*filp, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nbytes) |
|  | Writes nbytes number of bytes. |
| int(\* | [lseek](#a05b03f33ec51a2444a3a3f05ace8ba68) )(struct [fs\_file\_t](structfs__file__t.md) \*filp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), int whence) |
|  | Moves the file position to a new location in the file. |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)(\* | [tell](#a3bcb76b13290f7fba54d6d7578e66f9c) )(struct [fs\_file\_t](structfs__file__t.md) \*filp) |
|  | Retrieves the current position in the file. |
| int(\* | [truncate](#a604aa1045d24ad65e09e524a6adf8809) )(struct [fs\_file\_t](structfs__file__t.md) \*filp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length) |
|  | Truncates/expands the file to the new length. |
| int(\* | [sync](#ad1a427421f3c122885bed8ef1faa56ea) )(struct [fs\_file\_t](structfs__file__t.md) \*filp) |
|  | Flushes the cache of an open file. |
| int(\* | [close](#ae1c84b7c651a161e286cfb25aa1bc2fb) )(struct [fs\_file\_t](structfs__file__t.md) \*filp) |
|  | Flushes the associated stream and closes the file. |
| Directory operations | |
| int(\* | [opendir](#a3c0e0a91fffdde30802fb5a1cdc22b60) )(struct [fs\_dir\_t](structfs__dir__t.md) \*dirp, const char \*fs\_path) |
|  | Opens an existing directory specified by the path. |
| int(\* | [readdir](#ace0bf6d96ddcb61e42bb54eb4388c3dc) )(struct [fs\_dir\_t](structfs__dir__t.md) \*dirp, struct [fs\_dirent](structfs__dirent.md) \*entry) |
|  | Reads directory entries of an open directory. |
| int(\* | [closedir](#ad11c51566b0703f0fd426e37200d7a8e) )(struct [fs\_dir\_t](structfs__dir__t.md) \*dirp) |
|  | Closes an open directory. |
| File system level operations | |
| int(\* | [mount](#a086f2d11ff432e3d24887b5b3da2afca) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp) |
|  | Mounts a file system. |
| int(\* | [unmount](#a04659fbb0096ca2cc5e733d483494ae4) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp) |
|  | Unmounts a file system. |
| int(\* | [unlink](#a3486815c6b1dcf0aef0be7a71a31ffea) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*name) |
|  | Deletes the specified file or directory. |
| int(\* | [rename](#affc26f28e560d5e5bdaa1868fe81332e) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*from, const char \*to) |
|  | Renames a file or directory. |
| int(\* | [mkdir](#aa31880d03633ed35d060ce2e0ee75d15) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*name) |
|  | Creates a new directory using specified path. |
| int(\* | [stat](#a5865d7d64e0ad22a30f1822263f134da) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*path, struct [fs\_dirent](structfs__dirent.md) \*entry) |
|  | Checks the status of a file or directory specified by the path. |
| int(\* | [statvfs](#a3bac973eb97ecaa51a567b7d69a35142) )(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*path, struct [fs\_statvfs](structfs__statvfs.md) \*[stat](structstat.md)) |
|  | Returns the total and available space on the file system volume. |
| int(\* | [mkfs](#a1fcddbdc18673a3c8e183fd070e3d3c3) )([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dev\_id, void \*cfg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Formats a device to specified file system type. |

## Detailed Description

File System interface structure.

## Field Documentation

## [◆ ](#ae1c84b7c651a161e286cfb25aa1bc2fb)close

| int(\* fs\_file\_system\_t::close) (struct [fs\_file\_t](structfs__file__t.md) \*filp) |
| --- |

Flushes the associated stream and closes the file.

Parameters
:   | filp | File to close. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ad11c51566b0703f0fd426e37200d7a8e)closedir

| int(\* fs\_file\_system\_t::closedir) (struct [fs\_dir\_t](structfs__dir__t.md) \*dirp) |
| --- |

Closes an open directory.

Parameters
:   | dirp | Directory to close. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a05b03f33ec51a2444a3a3f05ace8ba68)lseek

| int(\* fs\_file\_system\_t::lseek) (struct [fs\_file\_t](structfs__file__t.md) \*filp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), int whence) |
| --- |

Moves the file position to a new location in the file.

Parameters
:   | filp | File to move. |
    | --- | --- |
    | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Relative offset from the position specified by whence. |
    | whence | Position in the file. Possible values: SEEK\_CUR, SEEK\_SET, SEEK\_END. |

Returns
:   New position in the file or negative errno code on fail.

## [◆ ](#aa31880d03633ed35d060ce2e0ee75d15)mkdir

| int(\* fs\_file\_system\_t::mkdir) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*name) |
| --- |

Creates a new directory using specified path.

Parameters
:   | mountp | Mount point. |
    | --- | --- |
    | name | Path to the directory to create. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a1fcddbdc18673a3c8e183fd070e3d3c3)mkfs

| int(\* fs\_file\_system\_t::mkfs) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dev\_id, void \*cfg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

Formats a device to specified file system type.

Available only if `CONFIG_FILE_SYSTEM_MKFS` is enabled.

Parameters
:   | dev\_id | Device identifier. |
    | --- | --- |
    | cfg | File system configuration. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Formatting flags. |

Returns
:   0 on success, negative errno code on fail.

Note
:   This operation destroys existing data on the target device.

## [◆ ](#a086f2d11ff432e3d24887b5b3da2afca)mount

| int(\* fs\_file\_system\_t::mount) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp) |
| --- |

Mounts a file system.

Parameters
:   | mountp | Mount point. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a40b11c282d3b8c30fe1e2d9cc98edd69)open

| int(\* fs\_file\_system\_t::open) (struct [fs\_file\_t](structfs__file__t.md) \*filp, const char \*fs\_path, [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

Opens or creates a file, depending on flags given.

Parameters
:   | filp | File to open/create. |
    | --- | --- |
    | fs\_path | Path to the file. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for opening/creating the file. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a3c0e0a91fffdde30802fb5a1cdc22b60)opendir

| int(\* fs\_file\_system\_t::opendir) (struct [fs\_dir\_t](structfs__dir__t.md) \*dirp, const char \*fs\_path) |
| --- |

Opens an existing directory specified by the path.

Parameters
:   | dirp | Directory to open. |
    | --- | --- |
    | fs\_path | Path to the directory. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a8efb04845dbec830f12435a6472b7015)read

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fs\_file\_system\_t::read) (struct [fs\_file\_t](structfs__file__t.md) \*filp, void \*dest, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nbytes) |
| --- |

Reads nbytes number of bytes.

Parameters
:   | filp | File to read from. |
    | --- | --- |
    | dest | Destination buffer. |
    | nbytes | Number of bytes to read. |

Returns
:   Number of bytes read on success, negative errno code on fail.

## [◆ ](#ace0bf6d96ddcb61e42bb54eb4388c3dc)readdir

| int(\* fs\_file\_system\_t::readdir) (struct [fs\_dir\_t](structfs__dir__t.md) \*dirp, struct [fs\_dirent](structfs__dirent.md) \*entry) |
| --- |

Reads directory entries of an open directory.

Parameters
:   | dirp | Directory to read from. |
    | --- | --- |
    | entry | Next directory entry in the dirp directory. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#affc26f28e560d5e5bdaa1868fe81332e)rename

| int(\* fs\_file\_system\_t::rename) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*from, const char \*to) |
| --- |

Renames a file or directory.

Parameters
:   | mountp | Mount point. |
    | --- | --- |
    | from | Path to the file or directory to rename. |
    | to | New name of the file or directory. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a5865d7d64e0ad22a30f1822263f134da)stat

| int(\* fs\_file\_system\_t::stat) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*path, struct [fs\_dirent](structfs__dirent.md) \*entry) |
| --- |

Checks the status of a file or directory specified by the path.

Parameters
:   | mountp | Mount point. |
    | --- | --- |
    | path | Path to the file or directory. |
    | entry | Directory entry. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a3bac973eb97ecaa51a567b7d69a35142)statvfs

| int(\* fs\_file\_system\_t::statvfs) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*path, struct [fs\_statvfs](structfs__statvfs.md) \*[stat](structstat.md)) |
| --- |

Returns the total and available space on the file system volume.

Parameters
:   | mountp | Mount point. |
    | --- | --- |
    | path | Path to the file or directory. |
    | [stat](structstat.md) | File system statistics. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ad1a427421f3c122885bed8ef1faa56ea)sync

| int(\* fs\_file\_system\_t::sync) (struct [fs\_file\_t](structfs__file__t.md) \*filp) |
| --- |

Flushes the cache of an open file.

Parameters
:   | filp | File to flush. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a3bcb76b13290f7fba54d6d7578e66f9c)tell

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)(\* fs\_file\_system\_t::tell) (struct [fs\_file\_t](structfs__file__t.md) \*filp) |
| --- |

Retrieves the current position in the file.

Parameters
:   | filp | File to get the current position from. |
    | --- | --- |

Returns
:   Current position in the file or negative errno code on fail.

## [◆ ](#a604aa1045d24ad65e09e524a6adf8809)truncate

| int(\* fs\_file\_system\_t::truncate) (struct [fs\_file\_t](structfs__file__t.md) \*filp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length) |
| --- |

Truncates/expands the file to the new length.

Parameters
:   | filp | File to truncate/expand. |
    | --- | --- |
    | length | New length of the file. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a3486815c6b1dcf0aef0be7a71a31ffea)unlink

| int(\* fs\_file\_system\_t::unlink) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*name) |
| --- |

Deletes the specified file or directory.

Parameters
:   | mountp | Mount point. |
    | --- | --- |
    | name | Path to the file or directory to delete. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a04659fbb0096ca2cc5e733d483494ae4)unmount

| int(\* fs\_file\_system\_t::unmount) (struct [fs\_mount\_t](structfs__mount__t.md) \*mountp) |
| --- |

Unmounts a file system.

Parameters
:   | mountp | Mount point. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#a1039b25b44bc8be1daea19c0d489c0db)write

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fs\_file\_system\_t::write) (struct [fs\_file\_t](structfs__file__t.md) \*filp, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nbytes) |
| --- |

Writes nbytes number of bytes.

Parameters
:   | filp | File to write to. |
    | --- | --- |
    | src | Source buffer. |
    | nbytes | Number of bytes to write. |

Returns
:   Number of bytes written on success, negative errno code on fail.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fs\_sys.h](fs__sys_8h_source.md)

- [fs\_file\_system\_t](structfs__file__system__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
