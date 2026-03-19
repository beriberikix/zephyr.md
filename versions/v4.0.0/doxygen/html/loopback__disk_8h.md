---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/loopback__disk_8h.html
original_path: doxygen/html/loopback__disk_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loopback\_disk.h File Reference

`#include <[zephyr/drivers/disk.h](disk_8h_source.md)>`  
`#include <[zephyr/fs/fs_interface.h](fs__interface_8h_source.md)>`

[Go to the source code of this file.](loopback__disk_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [loopback\_disk\_access](structloopback__disk__access.md) |
|  | Context object for an active loopback disk device. [More...](structloopback__disk__access.md#details) |

| Functions | |
| --- | --- |
| int | [loopback\_disk\_access\_register](#a17a5f2ad1706fd7c3a8dcdbda2753b9c) (struct [loopback\_disk\_access](structloopback__disk__access.md) \*ctx, const char \*file\_path, const char \*disk\_access\_name) |
|  | Register a loopback disk device. |
| int | [loopback\_disk\_access\_unregister](#af3dca356272ee28c2865592d73d2563d) (struct [loopback\_disk\_access](structloopback__disk__access.md) \*ctx) |
|  | Unregister a previously registered loopback disk device. |

## Function Documentation

## [◆ ](#a17a5f2ad1706fd7c3a8dcdbda2753b9c)loopback\_disk\_access\_register()

| int loopback\_disk\_access\_register | ( | struct [loopback\_disk\_access](structloopback__disk__access.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *file\_path*, |
|  |  | const char \* | *disk\_access\_name* ) |

Register a loopback disk device.

Registers a new loopback disk deviced backed by a file at the specified path.

`All` parameters (ctx, file\_path and disk\_access\_name) must point to data that will remain valid until the disk access is unregistered. This is trivially true for file\_path and disk\_access\_name if they are string literals, but care must be taken for ctx, as well as for file\_path and disk\_access\_name if they are constructed dynamically.

Parameters
:   | ctx | Preallocated context structure |
    | --- | --- |
    | file\_path | Path to backing file |
    | disk\_access\_name | Name of the created disk access (for disk\_access\_\*() functions) |

Return values
:   | 0 | on success; |
    | --- | --- |
    | <0 | negative errno code, depending on file system of the backing file. |

## [◆ ](#af3dca356272ee28c2865592d73d2563d)loopback\_disk\_access\_unregister()

| int loopback\_disk\_access\_unregister | ( | struct [loopback\_disk\_access](structloopback__disk__access.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Unregister a previously registered loopback disk device.

Cleans up resources used by the disk access.

Parameters
:   | ctx | Context structure previously passed to a successful invocation of [loopback\_disk\_access\_register()](#a17a5f2ad1706fd7c3a8dcdbda2753b9c) |
    | --- | --- |

Return values
:   | 0 | on success; |
    | --- | --- |
    | <0 | negative errno code, depending on file system of the backing file. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [loopback\_disk.h](loopback__disk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
