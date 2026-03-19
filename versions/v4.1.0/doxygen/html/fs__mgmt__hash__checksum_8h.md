---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fs__mgmt__hash__checksum_8h.html
original_path: doxygen/html/fs__mgmt__hash__checksum_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt\_hash\_checksum.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/fs/fs.h](fs_8h_source.md)>`

[Go to the source code of this file.](fs__mgmt__hash__checksum_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) |
|  | A collection of handlers for an entire hash/checksum group. [More...](structfs__mgmt__hash__checksum__group.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [fs\_mgmt\_hash\_checksum\_handler\_fn](#a1a3db209871cb21f90c7feb5fda4db62)) (struct [fs\_file\_t](structfs__file__t.md) \*file, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*out\_len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Function that gets called to generate a hash or checksum. |
| typedef void(\* | [fs\_mgmt\_hash\_checksum\_list\_cb](#a97669e080a8bdaee3bb8f2593ba99639)) (const struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md), void \*user\_data) |
|  | Function that gets called with hash/checksum details. |

| Functions | |
| --- | --- |
| void | [fs\_mgmt\_hash\_checksum\_register\_group](#a0f429c6e46361838794a2fe733f4e2cb) (struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md)) |
|  | Registers a full hash/checksum group. |
| void | [fs\_mgmt\_hash\_checksum\_unregister\_group](#a5f97144885d0a72dcab02de690511452) (struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md)) |
|  | Unregisters a full hash/checksum group. |
| const struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \* | [fs\_mgmt\_hash\_checksum\_find\_handler](#a5066ea99fe3f80652c364f9f779630d7) (const char \*name) |
|  | Finds a registered hash/checksum handler. |
| void | [fs\_mgmt\_hash\_checksum\_find\_handlers](#a5b299016aa5dab661395dbfb655af16c) ([fs\_mgmt\_hash\_checksum\_list\_cb](#a97669e080a8bdaee3bb8f2593ba99639) cb, void \*user\_data) |
|  | Runs a callback with all supported hash/checksum types. |

## Typedef Documentation

## [◆ ](#a1a3db209871cb21f90c7feb5fda4db62)fs\_mgmt\_hash\_checksum\_handler\_fn

| typedef int(\* fs\_mgmt\_hash\_checksum\_handler\_fn) (struct [fs\_file\_t](structfs__file__t.md) \*file, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*out\_len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Function that gets called to generate a hash or checksum.

Parameters
:   | file | Opened file context |
    | --- | --- |
    | output | Output buffer for hash/checksum |
    | out\_len | Updated with size of input data |
    | len | Maximum length of data to perform hash/checksum on |

Returns
:   0 on success, negative error code on failure.

## [◆ ](#a97669e080a8bdaee3bb8f2593ba99639)fs\_mgmt\_hash\_checksum\_list\_cb

| typedef void(\* fs\_mgmt\_hash\_checksum\_list\_cb) (const struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md), void \*user\_data) |
| --- |

Function that gets called with hash/checksum details.

Parameters
:   | [group](structgroup.md "Group structure.") | Details about a supported hash/checksum |
    | --- | --- |
    | user\_data | User-supplied value to calling function |

## Function Documentation

## [◆ ](#a5066ea99fe3f80652c364f9f779630d7)fs\_mgmt\_hash\_checksum\_find\_handler()

| const struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \* fs\_mgmt\_hash\_checksum\_find\_handler | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

Finds a registered hash/checksum handler.

Parameters
:   | name | The name of the hash/checksum group to find. |
    | --- | --- |

Returns
:   The requested hash/checksum handler on success; NULL on failure.

## [◆ ](#a5b299016aa5dab661395dbfb655af16c)fs\_mgmt\_hash\_checksum\_find\_handlers()

| void fs\_mgmt\_hash\_checksum\_find\_handlers | ( | [fs\_mgmt\_hash\_checksum\_list\_cb](#a97669e080a8bdaee3bb8f2593ba99639) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

Runs a callback with all supported hash/checksum types.

Parameters
:   | cb | The callback function to call with each hash/checksum type. |
    | --- | --- |
    | user\_data | Data to pass back with the callback function. |

## [◆ ](#a0f429c6e46361838794a2fe733f4e2cb)fs\_mgmt\_hash\_checksum\_register\_group()

| void fs\_mgmt\_hash\_checksum\_register\_group | ( | struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \* | *group* | ) |  |
| --- | --- | --- | --- | --- | --- |

Registers a full hash/checksum group.

Parameters
:   | [group](structgroup.md "Group structure.") | The group to register. |
    | --- | --- |

## [◆ ](#a5f97144885d0a72dcab02de690511452)fs\_mgmt\_hash\_checksum\_unregister\_group()

| void fs\_mgmt\_hash\_checksum\_unregister\_group | ( | struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \* | *group* | ) |  |
| --- | --- | --- | --- | --- | --- |

Unregisters a full hash/checksum group.

Parameters
:   | [group](structgroup.md "Group structure.") | The group to register. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [fs\_mgmt](dir_c1d9e91ec7be14b6f800d54e568d432d.md)
- [fs\_mgmt\_hash\_checksum.h](fs__mgmt__hash__checksum_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
