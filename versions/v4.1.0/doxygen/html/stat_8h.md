---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stat_8h.html
original_path: doxygen/html/stat_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat.h File Reference

`#include <[time.h](include_2zephyr_2posix_2sys_2time_8h_source.md)>`  
`#include <[sys/cdefs.h](cdefs_8h_source.md)>`  
`#include <[zephyr/posix/posix_types.h](posix__types_8h_source.md)>`

[Go to the source code of this file.](stat_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [stat](structstat.md) |

| Macros | |
| --- | --- |
| #define | [st\_atime](#a4ce306737c3153a7e2e99272c0a92ec5)   st\_atim.tv\_sec |
| #define | [st\_ctime](#a2dd9b364b84aee095dc6208ff18de4f5)   st\_ctim.tv\_sec |
| #define | [st\_mtime](#aecd62777ab7c6c1d6d23e4967632c5ef)   st\_mtim.tv\_sec |
| #define | [S\_BLKSIZE](#a7906181b09581ff1e44f07891a1a627b)   1024 /\* size of a block \*/ |
| #define | [S\_ISUID](#a30384a8cd2feb1615efd5eadc243684b)   0004000 /\* set user id on execution \*/ |
| #define | [S\_ISGID](#a9c9e4cc0a8acc43c99ae6c3d972ae2d8)   0002000 /\* set [group](structgroup.md) id on execution \*/ |
| #define | [S\_ISVTX](#a97b5e445a72c99b37dc5b8d620fbd14e)   0001000 /\* save swapped text even after use \*/ |
| #define | [S\_IFMT](#ab5bee51e9ee68b83ab11d4b340f7200b)   \_IFMT |
| #define | [S\_IFDIR](#a11fb0652b963a735f3377eb1c9239f2d)   \_IFDIR |
| #define | [S\_IFCHR](#aef3a1d1ba22c83e30b5c834dd343b2a8)   \_IFCHR |
| #define | [S\_IFBLK](#a5c5b74a1cb1a1ae83572500b94e1938f)   \_IFBLK |
| #define | [S\_IFREG](#a1aaa48b192a5dd3b6d7ee91fc98cd17d)   \_IFREG |
| #define | [S\_IFLNK](#afef163ce62372757e84bd9fc88c07aad)   \_IFLNK |
| #define | [S\_IFSOCK](#a28e80cd43106882904be148b2a397d42)   \_IFSOCK |
| #define | [S\_IFIFO](#a4966f25d9f03a7a06bc47ac729fd86cf)   \_IFIFO |
| #define | [S\_IRWXU](#afe3da42e762f6362c93454682fad5eb5)   ([S\_IRUSR](#a84c7dbf5cf2fdfb690f76348b60a8cb7) | [S\_IWUSR](#ad70001754261c15a1bdc8e876c6d09d7) | [S\_IXUSR](#af10a35e3950795d6ee4e07157d000131)) |
| #define | [S\_IRUSR](#a84c7dbf5cf2fdfb690f76348b60a8cb7)   0000400 /\* read permission, owner \*/ |
| #define | [S\_IWUSR](#ad70001754261c15a1bdc8e876c6d09d7)   0000200 /\* write permission, owner \*/ |
| #define | [S\_IXUSR](#af10a35e3950795d6ee4e07157d000131)   0000100 /\* execute/search permission, owner \*/ |
| #define | [S\_IRWXG](#a230c642d2bb81f15f85c122b1883de5c)   ([S\_IRGRP](#a4f5f280b929768113739fb34d6f7be8a) | [S\_IWGRP](#ae6774871a90d9442f00abe18b87fee6e) | [S\_IXGRP](#a042e69ac0e7dd56e5cfcd9e97d010323)) |
| #define | [S\_IRGRP](#a4f5f280b929768113739fb34d6f7be8a)   0000040 /\* read permission, [group](structgroup.md) \*/ |
| #define | [S\_IWGRP](#ae6774871a90d9442f00abe18b87fee6e)   0000020 /\* write permission, grougroup \*/ |
| #define | [S\_IXGRP](#a042e69ac0e7dd56e5cfcd9e97d010323)   0000010 /\* execute/search permission, [group](structgroup.md) \*/ |
| #define | [S\_IRWXO](#a5b93e0da7fe32bbd4926626bffad96b1)   ([S\_IROTH](#a071147a0cb995036967c80f64b1f74b9) | [S\_IWOTH](#a5303f49f26293acdb9533756c78322fb) | [S\_IXOTH](#a40223db1b95a04f5b28cceb3c34cfebd)) |
| #define | [S\_IROTH](#a071147a0cb995036967c80f64b1f74b9)   0000004 /\* read permission, other \*/ |
| #define | [S\_IWOTH](#a5303f49f26293acdb9533756c78322fb)   0000002 /\* write permission, other \*/ |
| #define | [S\_IXOTH](#a40223db1b95a04f5b28cceb3c34cfebd)   0000001 /\* execute/search permission, other \*/ |
| #define | [S\_ISBLK](#a722eba7370eb3b0aafb3272182e08520)(m) |
| #define | [S\_ISCHR](#a767b5d0691f435f8a9b7f5e0fa97a645)(m) |
| #define | [S\_ISDIR](#a70b64ed67c0ab484b4ba09487da34e91)(m) |
| #define | [S\_ISFIFO](#a777b706bbe9e7920c091aaa2b547b093)(m) |
| #define | [S\_ISREG](#abf68371159fa46b5cc47d0f3ac9ab723)(m) |
| #define | [S\_ISLNK](#a835359614ec43fbd96f53993cde84ef2)(m) |
| #define | [S\_ISSOCK](#a765304585be8c05f7fa72495e6d5881f)(m) |

| Functions | |
| --- | --- |
| int | [chmod](#aa0a896031839c30189c42617ebc5aaeb) (const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode) |
| int | [fchmod](#a6a5c46cd35365436fb3bb5e034be78e2) (int \_\_fd, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode) |
| int | [fstat](#a276d3b2ba668bdc06f78fccc16b956fe) (int \_\_fd, struct [stat](structstat.md) \*\_\_sbuf) |
| int | [mkdir](#afa4a4f346213cdc5ae4cfc9aedf7ef2e) (const char \*\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode) |
| int | [mkfifo](#acce8c726e07337e0581d74699e2324fe) (const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode) |
| int | [stat](#a0f949e7f97dc8e3e4ea1142cda8be155) (const char \*\_\_restrict \_\_path, struct stat \*\_\_restrict \_\_sbuf) |
| [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | [umask](#a90e6dc0189b82ecf0e2da52d74d2a149) ([mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mask) |

## Macro Definition Documentation

## [◆ ](#a7906181b09581ff1e44f07891a1a627b)S\_BLKSIZE

| #define S\_BLKSIZE   1024 /\* size of a block \*/ |
| --- |

## [◆ ](#a5c5b74a1cb1a1ae83572500b94e1938f)S\_IFBLK

| #define S\_IFBLK   \_IFBLK |
| --- |

## [◆ ](#aef3a1d1ba22c83e30b5c834dd343b2a8)S\_IFCHR

| #define S\_IFCHR   \_IFCHR |
| --- |

## [◆ ](#a11fb0652b963a735f3377eb1c9239f2d)S\_IFDIR

| #define S\_IFDIR   \_IFDIR |
| --- |

## [◆ ](#a4966f25d9f03a7a06bc47ac729fd86cf)S\_IFIFO

| #define S\_IFIFO   \_IFIFO |
| --- |

## [◆ ](#afef163ce62372757e84bd9fc88c07aad)S\_IFLNK

| #define S\_IFLNK   \_IFLNK |
| --- |

## [◆ ](#ab5bee51e9ee68b83ab11d4b340f7200b)S\_IFMT

| #define S\_IFMT   \_IFMT |
| --- |

## [◆ ](#a1aaa48b192a5dd3b6d7ee91fc98cd17d)S\_IFREG

| #define S\_IFREG   \_IFREG |
| --- |

## [◆ ](#a28e80cd43106882904be148b2a397d42)S\_IFSOCK

| #define S\_IFSOCK   \_IFSOCK |
| --- |

## [◆ ](#a4f5f280b929768113739fb34d6f7be8a)S\_IRGRP

| #define S\_IRGRP   0000040 /\* read permission, [group](structgroup.md) \*/ |
| --- |

## [◆ ](#a071147a0cb995036967c80f64b1f74b9)S\_IROTH

| #define S\_IROTH   0000004 /\* read permission, other \*/ |
| --- |

## [◆ ](#a84c7dbf5cf2fdfb690f76348b60a8cb7)S\_IRUSR

| #define S\_IRUSR   0000400 /\* read permission, owner \*/ |
| --- |

## [◆ ](#a230c642d2bb81f15f85c122b1883de5c)S\_IRWXG

| #define S\_IRWXG   ([S\_IRGRP](#a4f5f280b929768113739fb34d6f7be8a) | [S\_IWGRP](#ae6774871a90d9442f00abe18b87fee6e) | [S\_IXGRP](#a042e69ac0e7dd56e5cfcd9e97d010323)) |
| --- |

## [◆ ](#a5b93e0da7fe32bbd4926626bffad96b1)S\_IRWXO

| #define S\_IRWXO   ([S\_IROTH](#a071147a0cb995036967c80f64b1f74b9) | [S\_IWOTH](#a5303f49f26293acdb9533756c78322fb) | [S\_IXOTH](#a40223db1b95a04f5b28cceb3c34cfebd)) |
| --- |

## [◆ ](#afe3da42e762f6362c93454682fad5eb5)S\_IRWXU

| #define S\_IRWXU   ([S\_IRUSR](#a84c7dbf5cf2fdfb690f76348b60a8cb7) | [S\_IWUSR](#ad70001754261c15a1bdc8e876c6d09d7) | [S\_IXUSR](#af10a35e3950795d6ee4e07157d000131)) |
| --- |

## [◆ ](#a722eba7370eb3b0aafb3272182e08520)S\_ISBLK

| #define S\_ISBLK | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFBLK)

## [◆ ](#a767b5d0691f435f8a9b7f5e0fa97a645)S\_ISCHR

| #define S\_ISCHR | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFCHR)

## [◆ ](#a70b64ed67c0ab484b4ba09487da34e91)S\_ISDIR

| #define S\_ISDIR | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFDIR)

## [◆ ](#a777b706bbe9e7920c091aaa2b547b093)S\_ISFIFO

| #define S\_ISFIFO | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFIFO)

## [◆ ](#a9c9e4cc0a8acc43c99ae6c3d972ae2d8)S\_ISGID

| #define S\_ISGID   0002000 /\* set [group](structgroup.md) id on execution \*/ |
| --- |

## [◆ ](#a835359614ec43fbd96f53993cde84ef2)S\_ISLNK

| #define S\_ISLNK | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFLNK)

## [◆ ](#abf68371159fa46b5cc47d0f3ac9ab723)S\_ISREG

| #define S\_ISREG | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFREG)

## [◆ ](#a765304585be8c05f7fa72495e6d5881f)S\_ISSOCK

| #define S\_ISSOCK | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((m)&\_IFMT) == \_IFSOCK)

## [◆ ](#a30384a8cd2feb1615efd5eadc243684b)S\_ISUID

| #define S\_ISUID   0004000 /\* set user id on execution \*/ |
| --- |

## [◆ ](#a97b5e445a72c99b37dc5b8d620fbd14e)S\_ISVTX

| #define S\_ISVTX   0001000 /\* save swapped text even after use \*/ |
| --- |

## [◆ ](#ae6774871a90d9442f00abe18b87fee6e)S\_IWGRP

| #define S\_IWGRP   0000020 /\* write permission, grougroup \*/ |
| --- |

## [◆ ](#a5303f49f26293acdb9533756c78322fb)S\_IWOTH

| #define S\_IWOTH   0000002 /\* write permission, other \*/ |
| --- |

## [◆ ](#ad70001754261c15a1bdc8e876c6d09d7)S\_IWUSR

| #define S\_IWUSR   0000200 /\* write permission, owner \*/ |
| --- |

## [◆ ](#a042e69ac0e7dd56e5cfcd9e97d010323)S\_IXGRP

| #define S\_IXGRP   0000010 /\* execute/search permission, [group](structgroup.md) \*/ |
| --- |

## [◆ ](#a40223db1b95a04f5b28cceb3c34cfebd)S\_IXOTH

| #define S\_IXOTH   0000001 /\* execute/search permission, other \*/ |
| --- |

## [◆ ](#af10a35e3950795d6ee4e07157d000131)S\_IXUSR

| #define S\_IXUSR   0000100 /\* execute/search permission, owner \*/ |
| --- |

## [◆ ](#a4ce306737c3153a7e2e99272c0a92ec5)st\_atime

| #define st\_atime   st\_atim.tv\_sec |
| --- |

## [◆ ](#a2dd9b364b84aee095dc6208ff18de4f5)st\_ctime

| #define st\_ctime   st\_ctim.tv\_sec |
| --- |

## [◆ ](#aecd62777ab7c6c1d6d23e4967632c5ef)st\_mtime

| #define st\_mtime   st\_mtim.tv\_sec |
| --- |

## Function Documentation

## [◆ ](#aa0a896031839c30189c42617ebc5aaeb)chmod()

| int chmod | ( | const char \* | *\_\_path*, |
| --- | --- | --- | --- |
|  |  | [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | *\_\_mode* ) |

## [◆ ](#a6a5c46cd35365436fb3bb5e034be78e2)fchmod()

| int fchmod | ( | int | *\_\_fd*, |
| --- | --- | --- | --- |
|  |  | [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | *\_\_mode* ) |

## [◆ ](#a276d3b2ba668bdc06f78fccc16b956fe)fstat()

| int fstat | ( | int | *\_\_fd*, |
| --- | --- | --- | --- |
|  |  | struct [stat](structstat.md) \* | *\_\_sbuf* ) |

## [◆ ](#afa4a4f346213cdc5ae4cfc9aedf7ef2e)mkdir()

| int mkdir | ( | const char \* | *\_path*, |
| --- | --- | --- | --- |
|  |  | [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | *\_\_mode* ) |

## [◆ ](#acce8c726e07337e0581d74699e2324fe)mkfifo()

| int mkfifo | ( | const char \* | *\_\_path*, |
| --- | --- | --- | --- |
|  |  | [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | *\_\_mode* ) |

## [◆ ](#a0f949e7f97dc8e3e4ea1142cda8be155)stat()

| int stat | ( | const char \*\_\_restrict | *\_\_path*, |
| --- | --- | --- | --- |
|  |  | struct stat \*\_\_restrict | *\_\_sbuf* ) |

## [◆ ](#a90e6dc0189b82ecf0e2da52d74d2a149)umask()

| [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) umask | ( | [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | *\_\_mask* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [stat.h](stat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
