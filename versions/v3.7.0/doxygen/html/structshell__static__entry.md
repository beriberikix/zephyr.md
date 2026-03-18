---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__static__entry.html
original_path: doxygen/html/structshell__static__entry.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_static\_entry Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [syntax](#ad87defa749ee7481f6d29d8c9084fb91) |
|  | Command syntax strings. |
| const char \* | [help](#ac8fb0fc23957a49d9a3664b5baa08704) |
|  | Command help string. |
| const union [shell\_cmd\_entry](unionshell__cmd__entry.md) \* | [subcmd](#a14534428d81f5ffeb303a5320766cd0a) |
|  | Pointer to subcommand. |
| [shell\_cmd\_handler](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338) | [handler](#a3147eb0cc1fea698dd433127acb1f220) |
|  | Command handler. |
| struct [shell\_static\_args](structshell__static__args.md) | [args](#a73951d31712342c0c0545a142059d367) |
|  | Command arguments. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [padding](#a1ca7de0e195f0f840cd04e4c69b20f80) [0] |

## Field Documentation

## [◆ ](#a73951d31712342c0c0545a142059d367)args

| struct [shell\_static\_args](structshell__static__args.md) shell\_static\_entry::args |
| --- |

Command arguments.

## [◆ ](#a3147eb0cc1fea698dd433127acb1f220)handler

| [shell\_cmd\_handler](group__shell__api.md#ga331e7d19b9b0755486596f5ffc598338) shell\_static\_entry::handler |
| --- |

Command handler.

## [◆ ](#ac8fb0fc23957a49d9a3664b5baa08704)help

| const char\* shell\_static\_entry::help |
| --- |

Command help string.

## [◆ ](#a1ca7de0e195f0f840cd04e4c69b20f80)padding

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_static\_entry::padding[0] |
| --- |

## [◆ ](#a14534428d81f5ffeb303a5320766cd0a)subcmd

| const union [shell\_cmd\_entry](unionshell__cmd__entry.md)\* shell\_static\_entry::subcmd |
| --- |

Pointer to subcommand.

## [◆ ](#ad87defa749ee7481f6d29d8c9084fb91)syntax

| const char\* shell\_static\_entry::syntax |
| --- |

Command syntax strings.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell\_static\_entry](structshell__static__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
