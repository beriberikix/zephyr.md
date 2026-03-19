---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fs__sys_8h_source.html
original_path: doxygen/html/fs__sys_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_sys.h

[Go to the documentation of this file.](fs__sys_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_FS\_FS\_SYS\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_FS\_SYS\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

18

[ 22](structfs__file__system__t.md)struct [fs\_file\_system\_t](structfs__file__system__t.md) {

[ 35](structfs__file__system__t.md#a40b11c282d3b8c30fe1e2d9cc98edd69) int (\*[open](structfs__file__system__t.md#a40b11c282d3b8c30fe1e2d9cc98edd69))(struct [fs\_file\_t](structfs__file__t.md) \*filp, const char \*fs\_path,

36 [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 45](structfs__file__system__t.md#a8efb04845dbec830f12435a6472b7015) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[read](structfs__file__system__t.md#a8efb04845dbec830f12435a6472b7015))(struct [fs\_file\_t](structfs__file__t.md) \*filp, void \*dest, size\_t nbytes);

[ 54](structfs__file__system__t.md#a1039b25b44bc8be1daea19c0d489c0db) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[write](structfs__file__system__t.md#a1039b25b44bc8be1daea19c0d489c0db))(struct [fs\_file\_t](structfs__file__t.md) \*filp,

55 const void \*src, size\_t nbytes);

[ 64](structfs__file__system__t.md#a05b03f33ec51a2444a3a3f05ace8ba68) int (\*[lseek](structfs__file__system__t.md#a05b03f33ec51a2444a3a3f05ace8ba68))(struct [fs\_file\_t](structfs__file__t.md) \*filp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), int whence);

[ 71](structfs__file__system__t.md#a3bcb76b13290f7fba54d6d7578e66f9c) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) (\*[tell](structfs__file__system__t.md#a3bcb76b13290f7fba54d6d7578e66f9c))(struct [fs\_file\_t](structfs__file__t.md) \*filp);

[ 79](structfs__file__system__t.md#a604aa1045d24ad65e09e524a6adf8809) int (\*[truncate](structfs__file__system__t.md#a604aa1045d24ad65e09e524a6adf8809))(struct [fs\_file\_t](structfs__file__t.md) \*filp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length);

[ 86](structfs__file__system__t.md#ad1a427421f3c122885bed8ef1faa56ea) int (\*[sync](structfs__file__system__t.md#ad1a427421f3c122885bed8ef1faa56ea))(struct [fs\_file\_t](structfs__file__t.md) \*filp);

[ 93](structfs__file__system__t.md#ae1c84b7c651a161e286cfb25aa1bc2fb) int (\*[close](structfs__file__system__t.md#ae1c84b7c651a161e286cfb25aa1bc2fb))(struct [fs\_file\_t](structfs__file__t.md) \*filp);

95

[ 107](structfs__file__system__t.md#a3c0e0a91fffdde30802fb5a1cdc22b60) int (\*[opendir](structfs__file__system__t.md#a3c0e0a91fffdde30802fb5a1cdc22b60))(struct [fs\_dir\_t](structfs__dir__t.md) \*dirp, const char \*fs\_path);

[ 115](structfs__file__system__t.md#ace0bf6d96ddcb61e42bb54eb4388c3dc) int (\*[readdir](structfs__file__system__t.md#ace0bf6d96ddcb61e42bb54eb4388c3dc))(struct [fs\_dir\_t](structfs__dir__t.md) \*dirp, struct [fs\_dirent](structfs__dirent.md) \*entry);

[ 122](structfs__file__system__t.md#ad11c51566b0703f0fd426e37200d7a8e) int (\*[closedir](structfs__file__system__t.md#ad11c51566b0703f0fd426e37200d7a8e))(struct [fs\_dir\_t](structfs__dir__t.md) \*dirp);

124

[ 135](structfs__file__system__t.md#a086f2d11ff432e3d24887b5b3da2afca) int (\*[mount](structfs__file__system__t.md#a086f2d11ff432e3d24887b5b3da2afca))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp);

[ 142](structfs__file__system__t.md#a04659fbb0096ca2cc5e733d483494ae4) int (\*[unmount](structfs__file__system__t.md#a04659fbb0096ca2cc5e733d483494ae4))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp);

[ 150](structfs__file__system__t.md#a3486815c6b1dcf0aef0be7a71a31ffea) int (\*[unlink](structfs__file__system__t.md#a3486815c6b1dcf0aef0be7a71a31ffea))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*name);

[ 159](structfs__file__system__t.md#affc26f28e560d5e5bdaa1868fe81332e) int (\*[rename](structfs__file__system__t.md#affc26f28e560d5e5bdaa1868fe81332e))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*from,

160 const char \*to);

[ 168](structfs__file__system__t.md#aa31880d03633ed35d060ce2e0ee75d15) int (\*[mkdir](structfs__file__system__t.md#aa31880d03633ed35d060ce2e0ee75d15))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*name);

[ 177](structfs__file__system__t.md#a5865d7d64e0ad22a30f1822263f134da) int (\*[stat](structfs__file__system__t.md#a5865d7d64e0ad22a30f1822263f134da))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*path,

178 struct [fs\_dirent](structfs__dirent.md) \*entry);

[ 187](structfs__file__system__t.md#a3bac973eb97ecaa51a567b7d69a35142) int (\*[statvfs](structfs__file__system__t.md#a3bac973eb97ecaa51a567b7d69a35142))(struct [fs\_mount\_t](structfs__mount__t.md) \*mountp, const char \*path,

188 struct [fs\_statvfs](structfs__statvfs.md) \*[stat](structfs__file__system__t.md#a5865d7d64e0ad22a30f1822263f134da));

189#if defined(CONFIG\_FILE\_SYSTEM\_MKFS) || defined(\_\_DOXYGEN\_\_)

[ 201](structfs__file__system__t.md#a1fcddbdc18673a3c8e183fd070e3d3c3) int (\*[mkfs](structfs__file__system__t.md#a1fcddbdc18673a3c8e183fd070e3d3c3))([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dev\_id, void \*cfg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

202#endif

204};

205

209

210#ifdef \_\_cplusplus

211}

212#endif

213

214#endif /\* ZEPHYR\_INCLUDE\_FS\_FS\_SYS\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027)

uint8\_t fs\_mode\_t

**Definition** fs\_interface.h:62

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[fs\_dir\_t](structfs__dir__t.md)

Directory object representing an open directory.

**Definition** fs\_interface.h:90

[fs\_dirent](structfs__dirent.md)

Structure to receive file or directory information.

**Definition** fs.h:117

[fs\_file\_system\_t](structfs__file__system__t.md)

File System interface structure.

**Definition** fs\_sys.h:22

[fs\_file\_system\_t::unmount](structfs__file__system__t.md#a04659fbb0096ca2cc5e733d483494ae4)

int(\* unmount)(struct fs\_mount\_t \*mountp)

Unmounts a file system.

**Definition** fs\_sys.h:142

[fs\_file\_system\_t::lseek](structfs__file__system__t.md#a05b03f33ec51a2444a3a3f05ace8ba68)

int(\* lseek)(struct fs\_file\_t \*filp, off\_t off, int whence)

Moves the file position to a new location in the file.

**Definition** fs\_sys.h:64

[fs\_file\_system\_t::mount](structfs__file__system__t.md#a086f2d11ff432e3d24887b5b3da2afca)

int(\* mount)(struct fs\_mount\_t \*mountp)

Mounts a file system.

**Definition** fs\_sys.h:135

[fs\_file\_system\_t::write](structfs__file__system__t.md#a1039b25b44bc8be1daea19c0d489c0db)

ssize\_t(\* write)(struct fs\_file\_t \*filp, const void \*src, size\_t nbytes)

Writes nbytes number of bytes.

**Definition** fs\_sys.h:54

[fs\_file\_system\_t::mkfs](structfs__file__system__t.md#a1fcddbdc18673a3c8e183fd070e3d3c3)

int(\* mkfs)(uintptr\_t dev\_id, void \*cfg, int flags)

Formats a device to specified file system type.

**Definition** fs\_sys.h:201

[fs\_file\_system\_t::unlink](structfs__file__system__t.md#a3486815c6b1dcf0aef0be7a71a31ffea)

int(\* unlink)(struct fs\_mount\_t \*mountp, const char \*name)

Deletes the specified file or directory.

**Definition** fs\_sys.h:150

[fs\_file\_system\_t::statvfs](structfs__file__system__t.md#a3bac973eb97ecaa51a567b7d69a35142)

int(\* statvfs)(struct fs\_mount\_t \*mountp, const char \*path, struct fs\_statvfs \*stat)

Returns the total and available space on the file system volume.

**Definition** fs\_sys.h:187

[fs\_file\_system\_t::tell](structfs__file__system__t.md#a3bcb76b13290f7fba54d6d7578e66f9c)

off\_t(\* tell)(struct fs\_file\_t \*filp)

Retrieves the current position in the file.

**Definition** fs\_sys.h:71

[fs\_file\_system\_t::opendir](structfs__file__system__t.md#a3c0e0a91fffdde30802fb5a1cdc22b60)

int(\* opendir)(struct fs\_dir\_t \*dirp, const char \*fs\_path)

Opens an existing directory specified by the path.

**Definition** fs\_sys.h:107

[fs\_file\_system\_t::open](structfs__file__system__t.md#a40b11c282d3b8c30fe1e2d9cc98edd69)

int(\* open)(struct fs\_file\_t \*filp, const char \*fs\_path, fs\_mode\_t flags)

Opens or creates a file, depending on flags given.

**Definition** fs\_sys.h:35

[fs\_file\_system\_t::stat](structfs__file__system__t.md#a5865d7d64e0ad22a30f1822263f134da)

int(\* stat)(struct fs\_mount\_t \*mountp, const char \*path, struct fs\_dirent \*entry)

Checks the status of a file or directory specified by the path.

**Definition** fs\_sys.h:177

[fs\_file\_system\_t::truncate](structfs__file__system__t.md#a604aa1045d24ad65e09e524a6adf8809)

int(\* truncate)(struct fs\_file\_t \*filp, off\_t length)

Truncates/expands the file to the new length.

**Definition** fs\_sys.h:79

[fs\_file\_system\_t::read](structfs__file__system__t.md#a8efb04845dbec830f12435a6472b7015)

ssize\_t(\* read)(struct fs\_file\_t \*filp, void \*dest, size\_t nbytes)

Reads nbytes number of bytes.

**Definition** fs\_sys.h:45

[fs\_file\_system\_t::mkdir](structfs__file__system__t.md#aa31880d03633ed35d060ce2e0ee75d15)

int(\* mkdir)(struct fs\_mount\_t \*mountp, const char \*name)

Creates a new directory using specified path.

**Definition** fs\_sys.h:168

[fs\_file\_system\_t::readdir](structfs__file__system__t.md#ace0bf6d96ddcb61e42bb54eb4388c3dc)

int(\* readdir)(struct fs\_dir\_t \*dirp, struct fs\_dirent \*entry)

Reads directory entries of an open directory.

**Definition** fs\_sys.h:115

[fs\_file\_system\_t::closedir](structfs__file__system__t.md#ad11c51566b0703f0fd426e37200d7a8e)

int(\* closedir)(struct fs\_dir\_t \*dirp)

Closes an open directory.

**Definition** fs\_sys.h:122

[fs\_file\_system\_t::sync](structfs__file__system__t.md#ad1a427421f3c122885bed8ef1faa56ea)

int(\* sync)(struct fs\_file\_t \*filp)

Flushes the cache of an open file.

**Definition** fs\_sys.h:86

[fs\_file\_system\_t::close](structfs__file__system__t.md#ae1c84b7c651a161e286cfb25aa1bc2fb)

int(\* close)(struct fs\_file\_t \*filp)

Flushes the associated stream and closes the file.

**Definition** fs\_sys.h:93

[fs\_file\_system\_t::rename](structfs__file__system__t.md#affc26f28e560d5e5bdaa1868fe81332e)

int(\* rename)(struct fs\_mount\_t \*mountp, const char \*from, const char \*to)

Renames a file or directory.

**Definition** fs\_sys.h:159

[fs\_file\_t](structfs__file__t.md)

File object representing an open file.

**Definition** fs\_interface.h:76

[fs\_mount\_t](structfs__mount__t.md)

File system mount info structure.

**Definition** fs.h:91

[fs\_statvfs](structfs__statvfs.md)

Structure to receive volume statistics.

**Definition** fs.h:134

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fs\_sys.h](fs__sys_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
