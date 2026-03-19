---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fs_8h.html
original_path: doxygen/html/fs_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/sys/dlist.h](dlist_8h_source.md)>`  
`#include <[zephyr/fs/fs_interface.h](fs__interface_8h_source.md)>`

[Go to the source code of this file.](fs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fs\_mount\_t](structfs__mount__t.md) |
|  | File system mount info structure. [More...](structfs__mount__t.md#details) |
| struct | [fs\_dirent](structfs__dirent.md) |
|  | Structure to receive file or directory information. [More...](structfs__dirent.md#details) |
| struct | [fs\_statvfs](structfs__statvfs.md) |
|  | Structure to receive volume statistics. [More...](structfs__statvfs.md#details) |

| Macros | |
| --- | --- |
| #define | [FS\_MOUNT\_FLAG\_NO\_FORMAT](group__file__system__api.md#ga37b6ee15dc50499516fc51e9cb6287d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag prevents formatting device if requested file system not found. |
| #define | [FS\_MOUNT\_FLAG\_READ\_ONLY](group__file__system__api.md#ga789e7f0fbbbb1c751f9dee9d9ca9693d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag makes mounted file system read-only. |
| #define | [FS\_MOUNT\_FLAG\_AUTOMOUNT](group__file__system__api.md#gac11f7ecef01b7758b6f8f70fdcd7089d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag used in pre-defined mount structures that are to be mounted on startup. |
| #define | [FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS](group__file__system__api.md#gadb6c0761d7d537f73b23b1056d12686e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Flag requests file system driver to use Disk Access API. |
| #define | [FSTAB\_ENTRY\_DT\_MOUNT\_FLAGS](group__file__system__api.md#ga479d34077e909fccbb40f53616499f19)(node\_id) |
|  | Get the common mount flags for an fstab entry. |
| #define | [FS\_FSTAB\_ENTRY](group__file__system__api.md#ga1f50cda8a852400e063ab5b0db94e3fe)(node\_id) |
|  | The name under which a zephyr,fstab entry mount structure is defined. |
| #define | [FS\_FSTAB\_DECLARE\_ENTRY](group__file__system__api.md#ga1a9f475a065f3e77b035b0daf1511387)(node\_id) |
|  | Generate a declaration for the externally defined fstab entry. |
| fs\_open open and creation mode flags | |
| #define | [FS\_O\_READ](group__file__system__api.md#gafd1228407bcf929a175cc18802cda4b2)   0x01 |
|  | Open for read flag. |
| #define | [FS\_O\_WRITE](group__file__system__api.md#ga0e86c5413b46133e824deaa89b16ee8d)   0x02 |
|  | Open for write flag. |
| #define | [FS\_O\_RDWR](group__file__system__api.md#ga24ebd0220844552dd044bc2f16de4bef)   ([FS\_O\_READ](group__file__system__api.md#gafd1228407bcf929a175cc18802cda4b2) | [FS\_O\_WRITE](group__file__system__api.md#ga0e86c5413b46133e824deaa89b16ee8d)) |
|  | Open for read-write flag combination. |
| #define | [FS\_O\_MODE\_MASK](group__file__system__api.md#ga728a9885ecf444cec4a1610671cc68bf)   0x03 |
|  | Bitmask for read and write flags. |
| #define | [FS\_O\_CREATE](group__file__system__api.md#gaa0965d6d26ece16ee1300f815d31b4e8)   0x10 |
|  | Create file if it does not exist. |
| #define | [FS\_O\_APPEND](group__file__system__api.md#ga51d5d3c5df852cbb3699b3a7357dbcb3)   0x20 |
|  | Open/create file for append. |
| #define | [FS\_O\_TRUNC](group__file__system__api.md#ga017c28694e3f4ed9724110d642c795f9)   0x40 |
|  | Truncate the file while opening. |
| #define | [FS\_O\_FLAGS\_MASK](group__file__system__api.md#gabe568c7cd0aef699b0c19385e33266d4)   0x70 |
|  | Bitmask for open/create flags. |
| #define | [FS\_O\_MASK](group__file__system__api.md#gafa921cd65710cfa28f3b7a519a1f6142)   ([FS\_O\_MODE\_MASK](group__file__system__api.md#ga728a9885ecf444cec4a1610671cc68bf) | [FS\_O\_FLAGS\_MASK](group__file__system__api.md#gabe568c7cd0aef699b0c19385e33266d4)) |
|  | Bitmask for open flags. |
| fs\_seek whence parameter values | |
| #define | [FS\_SEEK\_SET](group__file__system__api.md#ga5b33d405a458db1db212d345b21454f8)   0 |
|  | Seek from the beginning of file. |
| #define | [FS\_SEEK\_CUR](group__file__system__api.md#gacf310c560f9076b5b4b6ab4192147211)   1 |
|  | Seek from a current position. |
| #define | [FS\_SEEK\_END](group__file__system__api.md#gaea9734cc236a73aefd3b35444d08d39d)   2 |
|  | Seek from the end of file. |

| Enumerations | |
| --- | --- |
| enum | [fs\_dir\_entry\_type](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb) { [FS\_DIR\_ENTRY\_FILE](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afbae84f63edd56b9a797a219b5382f85e3b) = 0 , [FS\_DIR\_ENTRY\_DIR](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afba443eeda19fcb1164475c2ffd8276e937) } |
|  | Enumeration for directory entry types. [More...](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb) |
| enum | { [FS\_FATFS](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa7f8f37a9e6506d6a2432391aee0fde40) = 0 , [FS\_LITTLEFS](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa18e15403ed6ec492c565e00d86c4a33f) , [FS\_EXT2](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa0f30e2d86ecb55874ff5c6430634bb11) , [FS\_TYPE\_EXTERNAL\_BASE](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa37c6c9e64a57fee8c51884e18facf25f) } |
|  | Enumeration to uniquely identify file system types. [More...](group__file__system__api.md#ga342d09da6adbf7d1576ce7f933c1b4ff) |

| Functions | |
| --- | --- |
| static void | [fs\_file\_t\_init](group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Initialize [fs\_file\_t](structfs__file__t.md "File object representing an open file.") object. |
| static void | [fs\_dir\_t\_init](group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp) |
|  | Initialize [fs\_dir\_t](structfs__dir__t.md "Directory object representing an open directory.") object. |
| int | [fs\_open](group__file__system__api.md#ga9c90031ba3e5a10da8e00e81d53ef63b) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, const char \*file\_name, [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Open or create file. |
| int | [fs\_close](group__file__system__api.md#ga4811679c25021e9f763824e06292e043) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Close file. |
| int | [fs\_unlink](group__file__system__api.md#gab979f963a8372f98080f66e0f32c8df6) (const char \*path) |
|  | Unlink file. |
| int | [fs\_rename](group__file__system__api.md#ga28bb828c6e59bf7e1f0e3edc56a15575) (const char \*from, const char \*to) |
|  | Rename file or directory. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [fs\_read](group__file__system__api.md#gaba7e07127777187eedcd6976d352ab76) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Read file. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [fs\_write](group__file__system__api.md#ga9e0dccc0d4235ff8bc4a745bc697e808) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, const void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write file. |
| int | [fs\_seek](group__file__system__api.md#ga81fc26a759e82d7da7531f9687c1ea50) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, int whence) |
|  | Seek file. |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [fs\_tell](group__file__system__api.md#ga5e97d124edf3ad98c0e2057999745d88) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Get current file position. |
| int | [fs\_truncate](group__file__system__api.md#gae525d9d95f4286f1c6eb0d2ded7febfa) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length) |
|  | Truncate or extend an open file to a given size. |
| int | [fs\_sync](group__file__system__api.md#gabf1951701521cf8d47a29129ec8462dd) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Flush cached write data buffers of an open file. |
| int | [fs\_mkdir](group__file__system__api.md#ga235cef7d5c4df385a40a0f0293574b0c) (const char \*path) |
|  | Directory create. |
| int | [fs\_opendir](group__file__system__api.md#ga00c042be81b3785d868c0c7a680a2fcd) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp, const char \*path) |
|  | Directory open. |
| int | [fs\_readdir](group__file__system__api.md#gab17be11c60221cf65aaf5f70f373a68f) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp, struct [fs\_dirent](structfs__dirent.md) \*entry) |
|  | Directory read entry. |
| int | [fs\_closedir](group__file__system__api.md#gaa2bf80a27f8a142ea1d553631d43b77e) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp) |
|  | Directory close. |
| int | [fs\_mount](group__file__system__api.md#ga46d59d84a1da3ce1d90478397826d793) (struct [fs\_mount\_t](structfs__mount__t.md) \*mp) |
|  | Mount filesystem. |
| int | [fs\_unmount](group__file__system__api.md#gabc20c3ce66340c4c207aba3c88448fbf) (struct [fs\_mount\_t](structfs__mount__t.md) \*mp) |
|  | Unmount filesystem. |
| int | [fs\_readmount](group__file__system__api.md#gab10d479fc27aa73aab2f08342387fc98) (int \*index, const char \*\*name) |
|  | Get path of mount point at index. |
| int | [fs\_stat](group__file__system__api.md#ga890681c0d324b2d184da7b1577ed571e) (const char \*path, struct [fs\_dirent](structfs__dirent.md) \*entry) |
|  | File or directory status. |
| int | [fs\_statvfs](group__file__system__api.md#ga12fc010a1b146e694f121a3a41e85430) (const char \*path, struct fs\_statvfs \*[stat](structstat.md)) |
|  | Retrieves statistics of the file system volume. |
| int | [fs\_mkfs](group__file__system__api.md#ga81f820cf8658d3686b1ed38ad1320c38) (int fs\_type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dev\_id, void \*cfg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Create fresh file system. |
| int | [fs\_register](group__file__system__api.md#ga97f4c377097c96320b32419011eebc5d) (int type, const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*fs) |
|  | Register a file system. |
| int | [fs\_unregister](group__file__system__api.md#ga098db65c6b327182ecbf0bdf44ec9c5b) (int type, const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*fs) |
|  | Unregister a file system. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fs.h](fs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
