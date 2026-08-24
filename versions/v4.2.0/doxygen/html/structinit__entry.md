---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structinit__entry.html
original_path: doxygen/html/structinit__entry.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

init\_entry Struct Reference

[Operating System Services](group__os__services.md) » [System Initialization](group__sys__init.md)

Structure to store initialization entry information.
[More...](#details)

`#include <[zephyr/init.h](init_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init\_fn](#ac0b2a7ee85ad51e462b557bcb3faf6b9) )(void) |
|  | If the init function belongs to a SYS\_INIT, this field stored the initialization function, otherwise it is set to NULL. |
| const struct [device](structdevice.md) \* | [dev](#af03b5e4991da3a75059bc4b254a3e21e) |
|  | If the init entry belongs to a device, this fields stores a reference to it, otherwise it is set to NULL. |

## Detailed Description

Structure to store initialization entry information.

## Field Documentation

## [◆ ](#af03b5e4991da3a75059bc4b254a3e21e)dev

| const struct [device](structdevice.md)\* init\_entry::dev |
| --- |

If the init entry belongs to a device, this fields stores a reference to it, otherwise it is set to NULL.

## [◆ ](#ac0b2a7ee85ad51e462b557bcb3faf6b9)init\_fn

| int(\* init\_entry::init\_fn) (void) |
| --- |

If the init function belongs to a SYS\_INIT, this field stored the initialization function, otherwise it is set to NULL.

---

The documentation for this struct was generated from the following file:

- zephyr/[init.h](init_8h_source.md)

- [init\_entry](structinit__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
