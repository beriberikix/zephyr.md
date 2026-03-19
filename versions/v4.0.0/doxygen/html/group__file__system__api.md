---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__file__system__api.html
original_path: doxygen/html/group__file__system__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

File System APIs

[Operating System Services](group__os__services.md)

File System APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [fs\_mount\_t](structfs__mount__t.md) |
|  | File system mount info structure. [More...](structfs__mount__t.md#details) |
| struct | [fs\_dirent](structfs__dirent.md) |
|  | Structure to receive file or directory information. [More...](structfs__dirent.md#details) |
| struct | [fs\_statvfs](structfs__statvfs.md) |
|  | Structure to receive volume statistics. [More...](structfs__statvfs.md#details) |
| struct | [fs\_file\_t](structfs__file__t.md) |
|  | File object representing an open file. [More...](structfs__file__t.md#details) |
| struct | [fs\_dir\_t](structfs__dir__t.md) |
|  | Directory object representing an open directory. [More...](structfs__dir__t.md#details) |
| struct | [fs\_file\_system\_t](structfs__file__system__t.md) |
|  | File System interface structure. [More...](structfs__file__system__t.md#details) |

| Macros | |
| --- | --- |
| #define | [FS\_MOUNT\_FLAG\_NO\_FORMAT](#ga37b6ee15dc50499516fc51e9cb6287d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag prevents formatting device if requested file system not found. |
| #define | [FS\_MOUNT\_FLAG\_READ\_ONLY](#ga789e7f0fbbbb1c751f9dee9d9ca9693d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag makes mounted file system read-only. |
| #define | [FS\_MOUNT\_FLAG\_AUTOMOUNT](#gac11f7ecef01b7758b6f8f70fdcd7089d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag used in pre-defined mount structures that are to be mounted on startup. |
| #define | [FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS](#gadb6c0761d7d537f73b23b1056d12686e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Flag requests file system driver to use Disk Access API. |
| #define | [FSTAB\_ENTRY\_DT\_MOUNT\_FLAGS](#ga479d34077e909fccbb40f53616499f19)(node\_id) |
|  | Get the common mount flags for an fstab entry. |
| #define | [FS\_FSTAB\_ENTRY](#ga1f50cda8a852400e063ab5b0db94e3fe)(node\_id) |
|  | The name under which a zephyr,fstab entry mount structure is defined. |
| #define | [FS\_FSTAB\_DECLARE\_ENTRY](#ga1a9f475a065f3e77b035b0daf1511387)(node\_id) |
|  | Generate a declaration for the externally defined fstab entry. |

| Enumerations | |
| --- | --- |
| enum | [fs\_dir\_entry\_type](#ga79f37397a1590284fae2c4b456f26afb) { [FS\_DIR\_ENTRY\_FILE](#gga79f37397a1590284fae2c4b456f26afbae84f63edd56b9a797a219b5382f85e3b) = 0 , [FS\_DIR\_ENTRY\_DIR](#gga79f37397a1590284fae2c4b456f26afba443eeda19fcb1164475c2ffd8276e937) } |
|  | Enumeration for directory entry types. [More...](#ga79f37397a1590284fae2c4b456f26afb) |
| enum | { [FS\_FATFS](#gga342d09da6adbf7d1576ce7f933c1b4ffa7f8f37a9e6506d6a2432391aee0fde40) = 0 , [FS\_LITTLEFS](#gga342d09da6adbf7d1576ce7f933c1b4ffa18e15403ed6ec492c565e00d86c4a33f) , [FS\_EXT2](#gga342d09da6adbf7d1576ce7f933c1b4ffa0f30e2d86ecb55874ff5c6430634bb11) , [FS\_TYPE\_EXTERNAL\_BASE](#gga342d09da6adbf7d1576ce7f933c1b4ffa37c6c9e64a57fee8c51884e18facf25f) } |
|  | Enumeration to uniquely identify file system types. [More...](#ga342d09da6adbf7d1576ce7f933c1b4ff) |

| Functions | |
| --- | --- |
| static void | [fs\_file\_t\_init](#gad44be87cbda3ddc48021ed16d515f564) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Initialize [fs\_file\_t](structfs__file__t.md "File object representing an open file.") object. |
| static void | [fs\_dir\_t\_init](#gacd31440cd0b10308e55a0484828ea2f3) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp) |
|  | Initialize [fs\_dir\_t](structfs__dir__t.md "Directory object representing an open directory.") object. |
| int | [fs\_open](#ga9c90031ba3e5a10da8e00e81d53ef63b) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, const char \*file\_name, [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Open or create file. |
| int | [fs\_close](#ga4811679c25021e9f763824e06292e043) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Close file. |
| int | [fs\_unlink](#gab979f963a8372f98080f66e0f32c8df6) (const char \*path) |
|  | Unlink file. |
| int | [fs\_rename](#ga28bb828c6e59bf7e1f0e3edc56a15575) (const char \*from, const char \*to) |
|  | Rename file or directory. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [fs\_read](#gaba7e07127777187eedcd6976d352ab76) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Read file. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [fs\_write](#ga9e0dccc0d4235ff8bc4a745bc697e808) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, const void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write file. |
| int | [fs\_seek](#ga81fc26a759e82d7da7531f9687c1ea50) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, int whence) |
|  | Seek file. |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [fs\_tell](#ga5e97d124edf3ad98c0e2057999745d88) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Get current file position. |
| int | [fs\_truncate](#gae525d9d95f4286f1c6eb0d2ded7febfa) (struct [fs\_file\_t](structfs__file__t.md) \*zfp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length) |
|  | Truncate or extend an open file to a given size. |
| int | [fs\_sync](#gabf1951701521cf8d47a29129ec8462dd) (struct [fs\_file\_t](structfs__file__t.md) \*zfp) |
|  | Flush cached write data buffers of an open file. |
| int | [fs\_mkdir](#ga235cef7d5c4df385a40a0f0293574b0c) (const char \*path) |
|  | Directory create. |
| int | [fs\_opendir](#ga00c042be81b3785d868c0c7a680a2fcd) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp, const char \*path) |
|  | Directory open. |
| int | [fs\_readdir](#gab17be11c60221cf65aaf5f70f373a68f) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp, struct [fs\_dirent](structfs__dirent.md) \*entry) |
|  | Directory read entry. |
| int | [fs\_closedir](#gaa2bf80a27f8a142ea1d553631d43b77e) (struct [fs\_dir\_t](structfs__dir__t.md) \*zdp) |
|  | Directory close. |
| int | [fs\_mount](#ga46d59d84a1da3ce1d90478397826d793) (struct [fs\_mount\_t](structfs__mount__t.md) \*mp) |
|  | Mount filesystem. |
| int | [fs\_unmount](#gabc20c3ce66340c4c207aba3c88448fbf) (struct [fs\_mount\_t](structfs__mount__t.md) \*mp) |
|  | Unmount filesystem. |
| int | [fs\_readmount](#gab10d479fc27aa73aab2f08342387fc98) (int \*index, const char \*\*name) |
|  | Get path of mount point at index. |
| int | [fs\_stat](#ga890681c0d324b2d184da7b1577ed571e) (const char \*path, struct [fs\_dirent](structfs__dirent.md) \*entry) |
|  | File or directory status. |
| int | [fs\_statvfs](#ga12fc010a1b146e694f121a3a41e85430) (const char \*path, struct fs\_statvfs \*[stat](structstat.md)) |
|  | Retrieves statistics of the file system volume. |
| int | [fs\_mkfs](#ga81f820cf8658d3686b1ed38ad1320c38) (int fs\_type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dev\_id, void \*cfg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Create fresh file system. |
| int | [fs\_register](#ga97f4c377097c96320b32419011eebc5d) (int type, const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*fs) |
|  | Register a file system. |
| int | [fs\_unregister](#ga098db65c6b327182ecbf0bdf44ec9c5b) (int type, const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*fs) |
|  | Unregister a file system. |

| fs\_open open and creation mode flags | |
| --- | --- |
| #define | [FS\_O\_READ](#gafd1228407bcf929a175cc18802cda4b2)   0x01 |
|  | Open for read flag. |
| #define | [FS\_O\_WRITE](#ga0e86c5413b46133e824deaa89b16ee8d)   0x02 |
|  | Open for write flag. |
| #define | [FS\_O\_RDWR](#ga24ebd0220844552dd044bc2f16de4bef)   ([FS\_O\_READ](#gafd1228407bcf929a175cc18802cda4b2) | [FS\_O\_WRITE](#ga0e86c5413b46133e824deaa89b16ee8d)) |
|  | Open for read-write flag combination. |
| #define | [FS\_O\_MODE\_MASK](#ga728a9885ecf444cec4a1610671cc68bf)   0x03 |
|  | Bitmask for read and write flags. |
| #define | [FS\_O\_CREATE](#gaa0965d6d26ece16ee1300f815d31b4e8)   0x10 |
|  | Create file if it does not exist. |
| #define | [FS\_O\_APPEND](#ga51d5d3c5df852cbb3699b3a7357dbcb3)   0x20 |
|  | Open/create file for append. |
| #define | [FS\_O\_TRUNC](#ga017c28694e3f4ed9724110d642c795f9)   0x40 |
|  | Truncate the file while opening. |
| #define | [FS\_O\_FLAGS\_MASK](#gabe568c7cd0aef699b0c19385e33266d4)   0x70 |
|  | Bitmask for open/create flags. |
| #define | [FS\_O\_MASK](#gafa921cd65710cfa28f3b7a519a1f6142)   ([FS\_O\_MODE\_MASK](#ga728a9885ecf444cec4a1610671cc68bf) | [FS\_O\_FLAGS\_MASK](#gabe568c7cd0aef699b0c19385e33266d4)) |
|  | Bitmask for open flags. |

| fs\_seek whence parameter values | |
| --- | --- |
| #define | [FS\_SEEK\_SET](#ga5b33d405a458db1db212d345b21454f8)   0 |
|  | Seek from the beginning of file. |
| #define | [FS\_SEEK\_CUR](#gacf310c560f9076b5b4b6ab4192147211)   1 |
|  | Seek from a current position. |
| #define | [FS\_SEEK\_END](#gaea9734cc236a73aefd3b35444d08d39d)   2 |
|  | Seek from the end of file. |

## Detailed Description

File System APIs.

Since
:   1.5

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga1a9f475a065f3e77b035b0daf1511387)FS\_FSTAB\_DECLARE\_ENTRY

| #define FS\_FSTAB\_DECLARE\_ENTRY | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

**Value:**

extern struct [fs\_mount\_t](structfs__mount__t.md) [FS\_FSTAB\_ENTRY](#ga1f50cda8a852400e063ab5b0db94e3fe)(node\_id)

[FS\_FSTAB\_ENTRY](#ga1f50cda8a852400e063ab5b0db94e3fe)

#define FS\_FSTAB\_ENTRY(node\_id)

The name under which a zephyr,fstab entry mount structure is defined.

**Definition** fs.h:215

[fs\_mount\_t](structfs__mount__t.md)

File system mount info structure.

**Definition** fs.h:91

Generate a declaration for the externally defined fstab entry.

This will evaluate to the name of a struct [fs\_mount\_t](structfs__mount__t.md "File system mount info structure.") object.

Parameters
:   | node\_id | the node identifier for a child entry in a zephyr,fstab node. |
    | --- | --- |

## [◆ ](#ga1f50cda8a852400e063ab5b0db94e3fe)FS\_FSTAB\_ENTRY

| #define FS\_FSTAB\_ENTRY | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

**Value:**

\_CONCAT(z\_fsmp\_, node\_id)

The name under which a zephyr,fstab entry mount structure is defined.

Parameters
:   | node\_id | the node identifier for a child entry in a zephyr,fstab node. |
    | --- | --- |

## [◆ ](#gac11f7ecef01b7758b6f8f70fdcd7089d)FS\_MOUNT\_FLAG\_AUTOMOUNT

| #define FS\_MOUNT\_FLAG\_AUTOMOUNT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Flag used in pre-defined mount structures that are to be mounted on startup.

This flag has no impact in user-defined mount structures.

## [◆ ](#ga37b6ee15dc50499516fc51e9cb6287d5)FS\_MOUNT\_FLAG\_NO\_FORMAT

| #define FS\_MOUNT\_FLAG\_NO\_FORMAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Flag prevents formatting device if requested file system not found.

## [◆ ](#ga789e7f0fbbbb1c751f9dee9d9ca9693d)FS\_MOUNT\_FLAG\_READ\_ONLY

| #define FS\_MOUNT\_FLAG\_READ\_ONLY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Flag makes mounted file system read-only.

## [◆ ](#gadb6c0761d7d537f73b23b1056d12686e)FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS

| #define FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Flag requests file system driver to use Disk Access API.

When the flag is set to the [fs\_mount\_t.flags](structfs__mount__t.md#ac5bd11869b64cfe1794b446d388c7116 "Mount flags.") prior to fs\_mount call, a file system needs to use the Disk Access API, otherwise mount callback for the driver should return -ENOSUP; when the flag is not set the file system driver should use Flash API by default, unless it only supports Disc Access API. When file system will use Disk Access API and the flag is not set, the mount callback for the file system should set the flag on success.

## [◆ ](#ga51d5d3c5df852cbb3699b3a7357dbcb3)FS\_O\_APPEND

| #define FS\_O\_APPEND   0x20 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Open/create file for append.

## [◆ ](#gaa0965d6d26ece16ee1300f815d31b4e8)FS\_O\_CREATE

| #define FS\_O\_CREATE   0x10 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Create file if it does not exist.

## [◆ ](#gabe568c7cd0aef699b0c19385e33266d4)FS\_O\_FLAGS\_MASK

| #define FS\_O\_FLAGS\_MASK   0x70 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Bitmask for open/create flags.

## [◆ ](#gafa921cd65710cfa28f3b7a519a1f6142)FS\_O\_MASK

| #define FS\_O\_MASK   ([FS\_O\_MODE\_MASK](#ga728a9885ecf444cec4a1610671cc68bf) | [FS\_O\_FLAGS\_MASK](#gabe568c7cd0aef699b0c19385e33266d4)) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Bitmask for open flags.

## [◆ ](#ga728a9885ecf444cec4a1610671cc68bf)FS\_O\_MODE\_MASK

| #define FS\_O\_MODE\_MASK   0x03 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Bitmask for read and write flags.

## [◆ ](#ga24ebd0220844552dd044bc2f16de4bef)FS\_O\_RDWR

| #define FS\_O\_RDWR   ([FS\_O\_READ](#gafd1228407bcf929a175cc18802cda4b2) | [FS\_O\_WRITE](#ga0e86c5413b46133e824deaa89b16ee8d)) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Open for read-write flag combination.

## [◆ ](#gafd1228407bcf929a175cc18802cda4b2)FS\_O\_READ

| #define FS\_O\_READ   0x01 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Open for read flag.

## [◆ ](#ga017c28694e3f4ed9724110d642c795f9)FS\_O\_TRUNC

| #define FS\_O\_TRUNC   0x40 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Truncate the file while opening.

## [◆ ](#ga0e86c5413b46133e824deaa89b16ee8d)FS\_O\_WRITE

| #define FS\_O\_WRITE   0x02 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Open for write flag.

## [◆ ](#gacf310c560f9076b5b4b6ab4192147211)FS\_SEEK\_CUR

| #define FS\_SEEK\_CUR   1 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Seek from a current position.

## [◆ ](#gaea9734cc236a73aefd3b35444d08d39d)FS\_SEEK\_END

| #define FS\_SEEK\_END   2 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Seek from the end of file.

## [◆ ](#ga5b33d405a458db1db212d345b21454f8)FS\_SEEK\_SET

| #define FS\_SEEK\_SET   0 |
| --- |

`#include <[fs.h](fs_8h.md)>`

Seek from the beginning of file.

## [◆ ](#ga479d34077e909fccbb40f53616499f19)FSTAB\_ENTRY\_DT\_MOUNT\_FLAGS

| #define FSTAB\_ENTRY\_DT\_MOUNT\_FLAGS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

**Value:**

(([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, automount) ? [FS\_MOUNT\_FLAG\_AUTOMOUNT](#gac11f7ecef01b7758b6f8f70fdcd7089d) : 0) \

| ([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, read\_only) ? [FS\_MOUNT\_FLAG\_READ\_ONLY](#ga789e7f0fbbbb1c751f9dee9d9ca9693d) : 0) \

| ([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, no\_format) ? [FS\_MOUNT\_FLAG\_NO\_FORMAT](#ga37b6ee15dc50499516fc51e9cb6287d5) : 0) \

| ([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, disk\_access) ? [FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS](#gadb6c0761d7d537f73b23b1056d12686e) : 0))

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:745

[FS\_MOUNT\_FLAG\_NO\_FORMAT](#ga37b6ee15dc50499516fc51e9cb6287d5)

#define FS\_MOUNT\_FLAG\_NO\_FORMAT

Flag prevents formatting device if requested file system not found.

**Definition** fs.h:69

[FS\_MOUNT\_FLAG\_READ\_ONLY](#ga789e7f0fbbbb1c751f9dee9d9ca9693d)

#define FS\_MOUNT\_FLAG\_READ\_ONLY

Flag makes mounted file system read-only.

**Definition** fs.h:71

[FS\_MOUNT\_FLAG\_AUTOMOUNT](#gac11f7ecef01b7758b6f8f70fdcd7089d)

#define FS\_MOUNT\_FLAG\_AUTOMOUNT

Flag used in pre-defined mount structures that are to be mounted on startup.

**Definition** fs.h:77

[FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS](#gadb6c0761d7d537f73b23b1056d12686e)

#define FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS

Flag requests file system driver to use Disk Access API.

**Definition** fs.h:86

Get the common mount flags for an fstab entry.

Parameters
:   | node\_id | the node identifier for a child entry in a zephyr,fstab node. |
    | --- | --- |

Returns
:   a value suitable for initializing an [fs\_mount\_t](structfs__mount__t.md "File system mount info structure.") flags member.

## Enumeration Type Documentation

## [◆ ](#ga342d09da6adbf7d1576ce7f933c1b4ff)anonymous enum

| anonymous enum |
| --- |

`#include <[fs.h](fs_8h.md)>`

Enumeration to uniquely identify file system types.

Zephyr supports in-tree file systems and external ones. Each requires a unique identifier used to register the file system implementation and to associate a mount point with the file system type. This anonymous enum defines global identifiers for the in-tree file systems.

External file systems should be registered using unique identifiers starting at `FS_TYPE_EXTERNAL_BASE`. It is the responsibility of applications that use external file systems to ensure that these identifiers are unique if multiple file system implementations are used by the application.

| Enumerator | |
| --- | --- |
| FS\_FATFS | Identifier for in-tree FatFS file system. |
| FS\_LITTLEFS | Identifier for in-tree LittleFS file system. |
| FS\_EXT2 | Identifier for in-tree Ext2 file system. |
| FS\_TYPE\_EXTERNAL\_BASE | Base identifier for external file systems. |

## [◆ ](#ga79f37397a1590284fae2c4b456f26afb)fs\_dir\_entry\_type

| enum [fs\_dir\_entry\_type](#ga79f37397a1590284fae2c4b456f26afb) |
| --- |

`#include <[fs.h](fs_8h.md)>`

Enumeration for directory entry types.

| Enumerator | |
| --- | --- |
| FS\_DIR\_ENTRY\_FILE | Identifier for file entry. |
| FS\_DIR\_ENTRY\_DIR | Identifier for directory entry. |

## Function Documentation

## [◆ ](#ga4811679c25021e9f763824e06292e043)fs\_close()

| int fs\_close | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Close file.

Flushes the associated stream and closes the file.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | a negative errno code on error. |

## [◆ ](#gaa2bf80a27f8a142ea1d553631d43b77e)fs\_closedir()

| int fs\_closedir | ( | struct [fs\_dir\_t](structfs__dir__t.md) \* | *zdp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Directory close.

Closes an open directory.

Parameters
:   | zdp | Pointer to the directory object |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | a negative errno code on error. |

## [◆ ](#gacd31440cd0b10308e55a0484828ea2f3)fs\_dir\_t\_init()

| | void fs\_dir\_t\_init | ( | struct [fs\_dir\_t](structfs__dir__t.md) \* | *zdp* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Initialize [fs\_dir\_t](structfs__dir__t.md "Directory object representing an open directory.") object.

Initializes the [fs\_dir\_t](structfs__dir__t.md "Directory object representing an open directory.") object; the function needs to be invoked on object before first use with fs\_opendir.

Parameters
:   | zdp | Pointer to file object |
    | --- | --- |

## [◆ ](#gad44be87cbda3ddc48021ed16d515f564)fs\_file\_t\_init()

| | void fs\_file\_t\_init | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Initialize [fs\_file\_t](structfs__file__t.md "File object representing an open file.") object.

Initializes the [fs\_file\_t](structfs__file__t.md "File object representing an open file.") object; the function needs to be invoked on object before first use with fs\_open.

Parameters
:   | zfp | Pointer to file object |
    | --- | --- |

## [◆ ](#ga235cef7d5c4df385a40a0f0293574b0c)fs\_mkdir()

| int fs\_mkdir | ( | const char \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Directory create.

Creates a new directory using specified path.

Parameters
:   | path | Path to the directory to create |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EEXIST | if entry of given name exists; |
    | -EROFS | if `path` is within read-only directory, or when file system has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | an other negative errno code on error |

## [◆ ](#ga81f820cf8658d3686b1ed38ad1320c38)fs\_mkfs()

| int fs\_mkfs | ( | int | *fs\_type*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *dev\_id*, |
|  |  | void \* | *cfg*, |
|  |  | int | *flags* ) |

`#include <[fs.h](fs_8h.md)>`

Create fresh file system.

Parameters
:   | fs\_type | Type of file system to create. |
    | --- | --- |
    | dev\_id | Id of storage device. |
    | cfg | Backend dependent init object. If NULL then default configuration is used. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Additional flags for file system implementation. |

Return values
:   | 0 | on success; |
    | --- | --- |
    | <0 | negative errno code on error. |

## [◆ ](#ga46d59d84a1da3ce1d90478397826d793)fs\_mount()

| int fs\_mount | ( | struct [fs\_mount\_t](structfs__mount__t.md) \* | *mp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Mount filesystem.

Perform steps needed for mounting a file system like calling the file system specific mount function and adding the mount point to mounted file system list.

Note
:   Current implementation of ELM FAT driver allows only following mount points: "/RAM:","/NAND:","/CF:","/SD:","/SD2:","/USB:","/USB2:","/USB3:" or mount points that consist of single digit, e.g: "/0:", "/1:" and so forth.

Parameters
:   | mp | Pointer to the [fs\_mount\_t](structfs__mount__t.md "File system mount info structure.") structure. Referenced object is not changed if the mount operation failed. A reference is captured in the fs infrastructure if the mount operation succeeds, and the application must not mutate the structure contents until fs\_unmount is successfully invoked on the same pointer. |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -ENOENT | when file system type has not been registered; |
    | -ENOTSUP | when not supported by underlying file system driver; when `FS_MOUNT_FLAG_USE_DISK_ACCESS` is set but driver does not support it. |
    | -EROFS | if system requires formatting but `FS_MOUNT_FLAG_READ_ONLY` has been set; |
    | <0 | an other negative errno code on error. |

## [◆ ](#ga9c90031ba3e5a10da8e00e81d53ef63b)fs\_open()

| int fs\_open | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp*, |
| --- | --- | --- | --- |
|  |  | const char \* | *file\_name*, |
|  |  | [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) | *flags* ) |

`#include <[fs.h](fs_8h.md)>`

Open or create file.

Opens or possibly creates a file and associates a stream with it. Successfully opened file, when no longer in use, should be closed with [fs\_close()](#ga4811679c25021e9f763824e06292e043).

`flags` can be 0 or a binary combination of one or more of the following identifiers:

- `FS_O_READ` open for read
- `FS_O_WRITE` open for write
- `FS_O_RDWR` open for read/write ([FS\_O\_READ](#gafd1228407bcf929a175cc18802cda4b2) | [FS\_O\_WRITE](#ga0e86c5413b46133e824deaa89b16ee8d))
- `FS_O_CREATE` create file if it does not exist
- `FS_O_APPEND` move to end of file before each write
- `FS_O_TRUNC` truncate the file

Warning
:   If `flags` are set to 0 the function will open file, if it exists and is accessible, but you will have no read/write access to it.

Parameters
:   | zfp | Pointer to a file object |
    | --- | --- |
    | file\_name | The name of a file to open |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | The mode flags |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EBUSY | when zfp is already used; |
    | -EINVAL | when a bad file name is given; |
    | -EROFS | when opening read-only file for write, or attempting to create a file on a system that has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag; |
    | -ENOENT | when the file does not exist at the path; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | -EACCES | when trying to truncate a file without opening it for write. |
    | <0 | an other negative errno code, depending on a file system back-end. |

## [◆ ](#ga00c042be81b3785d868c0c7a680a2fcd)fs\_opendir()

| int fs\_opendir | ( | struct [fs\_dir\_t](structfs__dir__t.md) \* | *zdp*, |
| --- | --- | --- | --- |
|  |  | const char \* | *path* ) |

`#include <[fs.h](fs_8h.md)>`

Directory open.

Opens an existing directory specified by the path.

Parameters
:   | zdp | Pointer to the directory object |
    | --- | --- |
    | path | Path to the directory to open |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | when a bad directory path is given; |
    | -EBUSY | when zdp is already used; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | a negative errno code on error. |

## [◆ ](#gaba7e07127777187eedcd6976d352ab76)fs\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) fs\_read | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp*, |
| --- | --- | --- | --- |
|  |  | void \* | *ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[fs.h](fs_8h.md)>`

Read file.

Reads up to `size` bytes of data to `ptr` pointed buffer, returns number of bytes read. A returned value may be lower than `size` if there were fewer bytes available than requested.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |
    | ptr | Pointer to the data buffer |
    | size | Number of bytes to be read |

Return values
:   | >=0 | a number of bytes read, on success; |
    | --- | --- |
    | -EBADF | when invoked on zfp that represents unopened/closed file; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | a negative errno code on error. |

## [◆ ](#gab17be11c60221cf65aaf5f70f373a68f)fs\_readdir()

| int fs\_readdir | ( | struct [fs\_dir\_t](structfs__dir__t.md) \* | *zdp*, |
| --- | --- | --- | --- |
|  |  | struct [fs\_dirent](structfs__dirent.md) \* | *entry* ) |

`#include <[fs.h](fs_8h.md)>`

Directory read entry.

Reads directory entries of an open directory. In end-of-dir condition, the function will return 0 and set the entry->name[0] to 0.

Note
:   : Most existing underlying file systems do not generate POSIX special directory entries "." or "..". For consistency the abstraction layer will remove these from lower layer results so higher layers see consistent results.

Parameters
:   | zdp | Pointer to the directory object |
    | --- | --- |
    | entry | Pointer to zfs\_dirent structure to read the entry into |

Return values
:   | 0 | on success or end-of-dir; |
    | --- | --- |
    | -ENOENT | when no such directory found; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | a negative errno code on error. |

## [◆ ](#gab10d479fc27aa73aab2f08342387fc98)fs\_readmount()

| int fs\_readmount | ( | int \* | *index*, |
| --- | --- | --- | --- |
|  |  | const char \*\* | *name* ) |

`#include <[fs.h](fs_8h.md)>`

Get path of mount point at index.

This function iterates through the list of mount points and returns the directory name of the mount point at the given `index`. On success `index` is incremented and `name` is set to the mount directory name. If a mount point with the given `index` does not exist, `name` will be set to `NULL`.

Parameters
:   | index | Pointer to mount point index |
    | --- | --- |
    | name | Pointer to pointer to path name |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -ENOENT | if there is no mount point with given index. |

## [◆ ](#ga97f4c377097c96320b32419011eebc5d)fs\_register()

| int fs\_register | ( | int | *type*, |
| --- | --- | --- | --- |
|  |  | const struct [fs\_file\_system\_t](structfs__file__system__t.md) \* | *fs* ) |

`#include <[fs.h](fs_8h.md)>`

Register a file system.

Register file system with virtual file system. Number of allowed file system types to be registered is controlled with the CONFIG\_FILE\_SYSTEM\_MAX\_TYPES Kconfig option.

Parameters
:   | type | Type of file system (ex: `FS_FATFS`) |
    | --- | --- |
    | fs | Pointer to File system |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EALREADY | when a file system of a given type has already been registered; |
    | -ENOSCP | when there is no space left, in file system registry, to add this file system type. |

## [◆ ](#ga28bb828c6e59bf7e1f0e3edc56a15575)fs\_rename()

| int fs\_rename | ( | const char \* | *from*, |
| --- | --- | --- | --- |
|  |  | const char \* | *to* ) |

`#include <[fs.h](fs_8h.md)>`

Rename file or directory.

Performs a rename and / or move of the specified source path to the specified destination. The source path can refer to either a file or a directory. All intermediate directories in the destination path must already exist. If the source path refers to a file, the destination path must contain a full filename path, rather than just the new parent directory. If an object already exists at the specified destination path, this function causes it to be unlinked prior to the rename (i.e., the destination gets clobbered).

Note
:   Current implementation does not allow moving files between mount points.

Parameters
:   | from | The source path |
    | --- | --- |
    | to | The destination path |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | when a bad file name is given, or when rename would cause move between mount points; |
    | -EROFS | if file is read-only, or when file system has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | an other negative errno code on error. |

## [◆ ](#ga81fc26a759e82d7da7531f9687c1ea50)fs\_seek()

| int fs\_seek | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | int | *whence* ) |

`#include <[fs.h](fs_8h.md)>`

Seek file.

Moves the file position to a new location in the file. The `offset` is added to file position based on the `whence` parameter.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |
    | offset | Relative location to move the file pointer to |
    | whence | Relative location from where offset is to be calculated.  - `FS_SEEK_SET` for the beginning of the file; - `FS_SEEK_CUR` for the current position; - `FS_SEEK_END` for the end of the file. |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EBADF | when invoked on zfp that represents unopened/closed file; |
    | -ENOTSUP | if not supported by underlying file system driver; |
    | <0 | an other negative errno code on error. |

## [◆ ](#ga890681c0d324b2d184da7b1577ed571e)fs\_stat()

| int fs\_stat | ( | const char \* | *path*, |
| --- | --- | --- | --- |
|  |  | struct [fs\_dirent](structfs__dirent.md) \* | *entry* ) |

`#include <[fs.h](fs_8h.md)>`

File or directory status.

Checks the status of a file or directory specified by the `path`.

Note
:   The file on a storage device may not be updated until it is closed.

Parameters
:   | path | Path to the file or directory |
    | --- | --- |
    | entry | Pointer to the zfs\_dirent structure to fill if the file or directory exists. |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | when a bad directory or file name is given; |
    | -ENOENT | when no such directory or file is found; |
    | -ENOTSUP | when not supported by underlying file system driver; |
    | <0 | negative errno code on error. |

## [◆ ](#ga12fc010a1b146e694f121a3a41e85430)fs\_statvfs()

| int fs\_statvfs | ( | const char \* | *path*, |
| --- | --- | --- | --- |
|  |  | struct fs\_statvfs \* | *stat* ) |

`#include <[fs.h](fs_8h.md)>`

Retrieves statistics of the file system volume.

Returns the total and available space in the file system volume.

Parameters
:   | path | Path to the mounted directory |
    | --- | --- |
    | [stat](structstat.md) | Pointer to the zfs\_statvfs structure to receive the fs statistics. |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | when a bad path to a directory, or a file, is given; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | an other negative errno code on error. |

## [◆ ](#gabf1951701521cf8d47a29129ec8462dd)fs\_sync()

| int fs\_sync | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Flush cached write data buffers of an open file.

The function flushes the cache of an open file; it can be invoked to ensure data gets written to the storage media immediately, e.g. to avoid data loss in case if power is removed unexpectedly.

Note
:   Closing a file will cause caches to be flushed correctly so the function need not be called when the file is being closed.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EBADF | when invoked on zfp that represents unopened/closed file; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | a negative errno code on error. |

## [◆ ](#ga5e97d124edf3ad98c0e2057999745d88)fs\_tell()

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) fs\_tell | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Get current file position.

Retrieves and returns the current position in the file stream.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |

Return values
:   | >= | 0 a current position in file; |
    | --- | --- |
    | -EBADF | when invoked on zfp that represents unopened/closed file; |
    | -ENOTSUP | if not supported by underlying file system driver; |
    | <0 | an other negative errno code on error. |

The current revision does not validate the file object.

## [◆ ](#gae525d9d95f4286f1c6eb0d2ded7febfa)fs\_truncate()

| int fs\_truncate | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *length* ) |

`#include <[fs.h](fs_8h.md)>`

Truncate or extend an open file to a given size.

Truncates the file to the new length if it is shorter than the current size of the file. Expands the file if the new length is greater than the current size of the file. The expanded region would be filled with zeroes.

Note
:   In the case of expansion, if the volume got full during the expansion process, the function will expand to the maximum possible length and return success. Caller should check if the expanded size matches the requested length.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |
    | length | New size of the file in bytes |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EBADF | when invoked on zfp that represents unopened/closed file; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | an other negative errno code on error. |

## [◆ ](#gab979f963a8372f98080f66e0f32c8df6)fs\_unlink()

| int fs\_unlink | ( | const char \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Unlink file.

Deletes the specified file or directory

Parameters
:   | path | Path to the file or directory to delete |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | when a bad file name is given; |
    | -EROFS | if file is read-only, or when file system has been mounted with the FS\_MOUNT\_FLAG\_READ\_ONLY flag; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | an other negative errno code on error. |

## [◆ ](#gabc20c3ce66340c4c207aba3c88448fbf)fs\_unmount()

| int fs\_unmount | ( | struct [fs\_mount\_t](structfs__mount__t.md) \* | *mp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fs.h](fs_8h.md)>`

Unmount filesystem.

Perform steps needed to unmount a file system like calling the file system specific unmount function and removing the mount point from mounted file system list.

Parameters
:   | mp | Pointer to the [fs\_mount\_t](structfs__mount__t.md "File system mount info structure.") structure |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | if no system has been mounted at given mount point; |
    | -ENOTSUP | when not supported by underlying file system driver; |
    | <0 | an other negative errno code on error. |

## [◆ ](#ga098db65c6b327182ecbf0bdf44ec9c5b)fs\_unregister()

| int fs\_unregister | ( | int | *type*, |
| --- | --- | --- | --- |
|  |  | const struct [fs\_file\_system\_t](structfs__file__system__t.md) \* | *fs* ) |

`#include <[fs.h](fs_8h.md)>`

Unregister a file system.

Unregister file system from virtual file system.

Parameters
:   | type | Type of file system (ex: `FS_FATFS`) |
    | --- | --- |
    | fs | Pointer to File system |

Return values
:   | 0 | on success; |
    | --- | --- |
    | -EINVAL | when file system of a given type has not been registered. |

## [◆ ](#ga9e0dccc0d4235ff8bc4a745bc697e808)fs\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) fs\_write | ( | struct [fs\_file\_t](structfs__file__t.md) \* | *zfp*, |
| --- | --- | --- | --- |
|  |  | const void \* | *ptr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[fs.h](fs_8h.md)>`

Write file.

Attempts to write `size` number of bytes to the specified file. If a negative value is returned from the function, the file pointer has not been advanced. If the function returns a non-negative number that is lower than `size`, the global `errno` variable should be checked for an error code, as the device may have no free space for data.

Parameters
:   | zfp | Pointer to the file object |
    | --- | --- |
    | ptr | Pointer to the data buffer |
    | size | Number of bytes to be written |

Return values
:   | >=0 | a number of bytes written, on success; |
    | --- | --- |
    | -EBADF | when invoked on zfp that represents unopened/closed file; |
    | -ENOTSUP | when not implemented by underlying file system driver; |
    | <0 | an other negative errno code on error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
