---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionshell__cmd__entry.html
original_path: doxygen/html/unionshell__cmd__entry.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_cmd\_entry Union Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

Shell command descriptor.
[More...](#details)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [shell\_dynamic\_get](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008) | [dynamic\_get](#aa76e35866f5df37593705fd1b53e15df) |
|  | Pointer to function returning dynamic commands. |
| const struct [shell\_static\_entry](structshell__static__entry.md) \* | [entry](#a4abb8327df0e62f63432a05cc885f03d) |
|  | Pointer to array of static commands. |

## Detailed Description

Shell command descriptor.

## Field Documentation

## [◆ ](#aa76e35866f5df37593705fd1b53e15df)dynamic\_get

| [shell\_dynamic\_get](group__shell__api.md#gafc042f32bac2fdd4cbde9f943e29b008) shell\_cmd\_entry::dynamic\_get |
| --- |

Pointer to function returning dynamic commands.

## [◆ ](#a4abb8327df0e62f63432a05cc885f03d)entry

| const struct [shell\_static\_entry](structshell__static__entry.md)\* shell\_cmd\_entry::entry |
| --- |

Pointer to array of static commands.

---

The documentation for this union was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_cmd\_entry](unionshell__cmd__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
