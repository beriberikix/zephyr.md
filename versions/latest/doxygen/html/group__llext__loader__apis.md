---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__llext__loader__apis.html
original_path: doxygen/html/group__llext__loader__apis.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ELF loader context

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md)

| Data Structures | |
| --- | --- |
| struct | [llext\_buf\_loader](structllext__buf__loader.md) |
|  | Implementation of [llext\_loader](structllext__loader.md "llext_loader") that reads from a memory buffer. [More...](structllext__buf__loader.md#details) |
| struct | [llext\_fs\_loader](structllext__fs__loader.md) |
|  | Implementation of [llext\_loader](structllext__loader.md "llext_loader") that reads from a filesystem. [More...](structllext__fs__loader.md#details) |
| struct | [llext\_loader](structllext__loader.md) |
|  | Linkable loadable extension loader context. [More...](structllext__loader.md#details) |

| Macros | |
| --- | --- |
| #define | [LLEXT\_BUF\_LOADER](#ga9ca06c7c3e57f5284ce44c62f5cc2c02)(\_buf, \_buf\_len) |
|  | Initializer for an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure. |
| #define | [LLEXT\_TEMPORARY\_BUF\_LOADER](#ga8485b4dfecbd2eff3e21b5958d5e8699)(\_buf, \_buf\_len) |
| #define | [LLEXT\_PERSISTENT\_BUF\_LOADER](#ga2c2214bcf1506f1209476619e42114b3)(\_buf, \_buf\_len) |
|  | Initialize an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure for a persistent, read-only buffer. |
| #define | [LLEXT\_WRITABLE\_BUF\_LOADER](#gac726727897e02bca0bf5d32f4c66be55)(\_buf, \_buf\_len) |
|  | Initialize an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure for a persistent, writable buffer. |
| #define | [LLEXT\_FS\_LOADER](#ga25a394fb7f7f93cfe3ab92d8ed4a6bff)(\_filename) |
|  | Initializer for an [llext\_fs\_loader](structllext__fs__loader.md "Implementation of llext_loader that reads from a filesystem.") structure. |

| Enumerations | |
| --- | --- |
| enum | [llext\_storage\_type](#ga8e04f364aef19cf45843cc97cc702f24) { [LLEXT\_STORAGE\_TEMPORARY](#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6) , [LLEXT\_STORAGE\_PERSISTENT](#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0) , [LLEXT\_STORAGE\_WRITABLE](#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b) } |
|  | Storage type for the ELF data to be loaded. [More...](#ga8e04f364aef19cf45843cc97cc702f24) |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga9ca06c7c3e57f5284ce44c62f5cc2c02)LLEXT\_BUF\_LOADER

| #define LLEXT\_BUF\_LOADER | ( |  | *\_buf*, |
| --- | --- | --- | --- |
|  |  |  | *\_buf\_len* ) |

`#include <[zephyr/llext/buf_loader.h](buf__loader_8h.md)>`

**Value:**

Z\_LLEXT\_BUF\_LOADER(\_buf, \_buf\_len, \

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LLEXT\_STORAGE\_WRITABLE) ? \

[LLEXT\_STORAGE\_WRITABLE](#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b) : [LLEXT\_STORAGE\_PERSISTENT](#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0))

[LLEXT\_STORAGE\_WRITABLE](#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b)

@ LLEXT\_STORAGE\_WRITABLE

ELF data is stored in a writable memory buffer that is guaranteed to be always accessible for as long...

**Definition** loader.h:70

[LLEXT\_STORAGE\_PERSISTENT](#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0)

@ LLEXT\_STORAGE\_PERSISTENT

ELF data is stored in a read-only buffer that is guaranteed to be always accessible for as long as th...

**Definition** loader.h:62

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

Initializer for an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure.

The storage type for the provided buffer depends on the value of the `CONFIG_LLEXT_STORAGE_WRITABLE` option: if it is defined, the buffer is assumed to be writable; otherwise it is assumed to be persistent.

Consider using one of the alternative macros instead.

See also
:   [LLEXT\_TEMPORARY\_BUF\_LOADER](#ga8485b4dfecbd2eff3e21b5958d5e8699)
:   [LLEXT\_PERSISTENT\_BUF\_LOADER](#ga2c2214bcf1506f1209476619e42114b3)
:   [LLEXT\_WRITABLE\_BUF\_LOADER](#gac726727897e02bca0bf5d32f4c66be55)

Parameters
:   | \_buf | Buffer containing the ELF binary |
    | --- | --- |
    | \_buf\_len | Buffer length in bytes |

## [◆ ](#ga25a394fb7f7f93cfe3ab92d8ed4a6bff)LLEXT\_FS\_LOADER

| #define LLEXT\_FS\_LOADER | ( |  | *\_filename* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/llext/fs_loader.h](fs__loader_8h.md)>`

**Value:**

{ \

.loader = \

{ \

.prepare = llext\_fs\_prepare, \

.read = llext\_fs\_read, \

.seek = llext\_fs\_seek, \

.peek = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \

.finalize = llext\_fs\_finalize, \

.storage = [LLEXT\_STORAGE\_TEMPORARY](#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6), \

}, \

.is\_open = false, \

.name = (\_filename), \

}

[LLEXT\_STORAGE\_TEMPORARY](#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6)

@ LLEXT\_STORAGE\_TEMPORARY

ELF data is only available during llext\_load(); even if the loader supports directly accessing the me...

**Definition** loader.h:55

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Initializer for an [llext\_fs\_loader](structllext__fs__loader.md "Implementation of llext_loader that reads from a filesystem.") structure.

Parameters
:   | \_filename | Absolute path to the extension file. |
    | --- | --- |

## [◆ ](#ga2c2214bcf1506f1209476619e42114b3)LLEXT\_PERSISTENT\_BUF\_LOADER

| #define LLEXT\_PERSISTENT\_BUF\_LOADER | ( |  | *\_buf*, |
| --- | --- | --- | --- |
|  |  |  | *\_buf\_len* ) |

`#include <[zephyr/llext/buf_loader.h](buf__loader_8h.md)>`

**Value:**

Z\_LLEXT\_BUF\_LOADER(\_buf, \_buf\_len, [LLEXT\_STORAGE\_PERSISTENT](#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0))

Initialize an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure for a persistent, read-only buffer.

ELF data from the specified buffer is guaranteed to be accessible for as long as the extension is loaded. The LLEXT subsystem may directly access the ELF data, as long as no modification is required during loading.

Parameters
:   | \_buf | Buffer containing the ELF binary |
    | --- | --- |
    | \_buf\_len | Buffer length in bytes |

## [◆ ](#ga8485b4dfecbd2eff3e21b5958d5e8699)LLEXT\_TEMPORARY\_BUF\_LOADER

| #define LLEXT\_TEMPORARY\_BUF\_LOADER | ( |  | *\_buf*, |
| --- | --- | --- | --- |
|  |  |  | *\_buf\_len* ) |

`#include <[zephyr/llext/buf_loader.h](buf__loader_8h.md)>`

**Value:**

Z\_LLEXT\_BUF\_LOADER(\_buf, \_buf\_len, [LLEXT\_STORAGE\_TEMPORARY](#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6))

## [◆ ](#gac726727897e02bca0bf5d32f4c66be55)LLEXT\_WRITABLE\_BUF\_LOADER

| #define LLEXT\_WRITABLE\_BUF\_LOADER | ( |  | *\_buf*, |
| --- | --- | --- | --- |
|  |  |  | *\_buf\_len* ) |

`#include <[zephyr/llext/buf_loader.h](buf__loader_8h.md)>`

**Value:**

Z\_LLEXT\_BUF\_LOADER(\_buf, \_buf\_len, [LLEXT\_STORAGE\_WRITABLE](#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b))

Initialize an [llext\_buf\_loader](structllext__buf__loader.md "Implementation of llext_loader that reads from a memory buffer.") structure for a persistent, writable buffer.

ELF data from the specified buffer is guaranteed to be accessible for as long as the extension is loaded. The LLEXT subsystem may directly access and modify the ELF data.

Parameters
:   | \_buf | Buffer containing the ELF binary |
    | --- | --- |
    | \_buf\_len | Buffer length in bytes |

## Enumeration Type Documentation

## [◆ ](#ga8e04f364aef19cf45843cc97cc702f24)llext\_storage\_type

| enum [llext\_storage\_type](#ga8e04f364aef19cf45843cc97cc702f24) |
| --- |

`#include <[zephyr/llext/loader.h](loader_8h.md)>`

Storage type for the ELF data to be loaded.

This enum defines the storage type of the ELF data that will be loaded. The storage type determines which memory optimizations can be tried by the LLEXT subsystem during the load process.

Note
:   Even with the most permissive option, LLEXT might still have to copy ELF data into a separate memory region to comply with other restrictions, such as hardware memory protection and/or alignment rules. Sections such as BSS that have no space in the file will also be allocated in the LLEXT heap.

| Enumerator | |
| --- | --- |
| LLEXT\_STORAGE\_TEMPORARY | ELF data is only available during [llext\_load()](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157 "Load and link an extension."); even if the loader supports directly accessing the memory via llext\_peek(), the buffer contents will be discarded afterwards.  LLEXT will allocate copies of all required data into its heap. |
| LLEXT\_STORAGE\_PERSISTENT | ELF data is stored in a *read-only* buffer that is guaranteed to be always accessible for as long as the extension is loaded.  LLEXT may directly reuse constant data from the buffer, but may still allocate copies if relocations need to be applied. |
| LLEXT\_STORAGE\_WRITABLE | ELF data is stored in a *writable* memory buffer that is guaranteed to be always accessible for as long as the extension is loaded.  LLEXT may freely modify and reuse data in the buffer; so, after the extension is unloaded, the contents should be re-initialized before a subsequent [llext\_load()](group__llext__apis.md#ga0a4c3db30bc3ec7aa8a9b0e076af7157 "Load and link an extension.") call. |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
