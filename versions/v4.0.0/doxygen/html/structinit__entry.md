---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structinit__entry.html
original_path: doxygen/html/structinit__entry.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

init\_entry Struct Reference

[Operating System Services](group__os__services.md) » [System Initialization](group__sys__init.md)

Structure to store initialization entry information.
[More...](#details)

`#include <[init.h](init_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union [init\_function](unioninit__function.md) | [init\_fn](#a2b2155a753096b51e80a1ef7752d05fb) |
|  | Initialization function. |
| union { |  |
| const struct [device](structdevice.md) \*   [dev](#af03b5e4991da3a75059bc4b254a3e21e) |  |
| }; |  |
|  | If the init entry belongs to a device, this fields stores a reference to it, otherwise it is set to NULL. |

## Detailed Description

Structure to store initialization entry information.

## Field Documentation

## [◆ ](#a56a878c7b77c07914761bd49b912c34f)[union]

| union { ... } [init\_entry](structinit__entry.md) |
| --- |

If the init entry belongs to a device, this fields stores a reference to it, otherwise it is set to NULL.

## [◆ ](#af03b5e4991da3a75059bc4b254a3e21e)dev

| const struct [device](structdevice.md)\* init\_entry::dev |
| --- |

## [◆ ](#a2b2155a753096b51e80a1ef7752d05fb)init\_fn

| union [init\_function](unioninit__function.md) init\_entry::init\_fn |
| --- |

Initialization function.

---

The documentation for this struct was generated from the following file:

- zephyr/[init.h](init_8h_source.md)

- [init\_entry](structinit__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
