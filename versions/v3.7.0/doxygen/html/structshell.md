---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell.html
original_path: doxygen/html/structshell.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell Struct Reference

[Operating System Services](group__os__services.md) » [Shell API](group__shell__api.md)

Shell instance internals.
[More...](#details)

`#include <[shell.h](shell_2shell_8h_source.md)>`

| Public Member Functions | |
| --- | --- |
|  | [LOG\_INSTANCE\_PTR\_DECLARE](#a30ad7480b8be019b3b3ed63bf05ad790) (log) |

| Data Fields | |
| --- | --- |
| const char \* | [default\_prompt](#a97c365dfd7202eb091b1ad016014729b) |
|  | shell default prompt. |
| const struct [shell\_transport](structshell__transport.md) \* | [iface](#ac6033c3c2e44c2c4e29791f1f61c566c) |
|  | Transport interface. |
| struct [shell\_ctx](structshell__ctx.md) \* | [ctx](#ac14fde7e5f28615b9eec39a2eb8aa8d4) |
|  | Internal context. |
| struct [shell\_history](structshell__history.md) \* | [history](#a42d2588d15f601baf3f963684d312c86) |
| enum [shell\_flag](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948) | [shell\_flag](#a3a4f58c6151b3cbd1293d36b92c2f470) |
| const struct [shell\_fprintf](structshell__fprintf.md) \* | [fprintf\_ctx](#aba181907e38def0985a4c6ffd459d935) |
| struct [shell\_stats](structshell__stats.md) \* | [stats](#a642e7d8fa92464147329247e1325ad2b) |
| const struct [shell\_log\_backend](structshell__log__backend.md) \* | [log\_backend](#a3daffdb9d38ee8132a2644054126680d) |
| const char \* | [name](#a66eb938dae4f2b0fd873980c1efeb00b) |
| struct [k\_thread](structk__thread.md) \* | [thread](#a01b4739356f2428527f322662a3bf0a7) |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [stack](#ad62262b6b4fa8e56a0e8849f09603b3a) |

## Detailed Description

Shell instance internals.

## Member Function Documentation

## [◆ ](#a30ad7480b8be019b3b3ed63bf05ad790)LOG\_INSTANCE\_PTR\_DECLARE()

| shell::LOG\_INSTANCE\_PTR\_DECLARE | ( | log |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## Field Documentation

## [◆ ](#ac14fde7e5f28615b9eec39a2eb8aa8d4)ctx

| struct [shell\_ctx](structshell__ctx.md)\* shell::ctx |
| --- |

Internal context.

## [◆ ](#a97c365dfd7202eb091b1ad016014729b)default\_prompt

| const char\* shell::default\_prompt |
| --- |

shell default prompt.

## [◆ ](#aba181907e38def0985a4c6ffd459d935)fprintf\_ctx

| const struct [shell\_fprintf](structshell__fprintf.md)\* shell::fprintf\_ctx |
| --- |

## [◆ ](#a42d2588d15f601baf3f963684d312c86)history

| struct [shell\_history](structshell__history.md)\* shell::history |
| --- |

## [◆ ](#ac6033c3c2e44c2c4e29791f1f61c566c)iface

| const struct [shell\_transport](structshell__transport.md)\* shell::iface |
| --- |

Transport interface.

## [◆ ](#a3daffdb9d38ee8132a2644054126680d)log\_backend

| const struct [shell\_log\_backend](structshell__log__backend.md)\* shell::log\_backend |
| --- |

## [◆ ](#a66eb938dae4f2b0fd873980c1efeb00b)name

| const char\* shell::name |
| --- |

## [◆ ](#a3a4f58c6151b3cbd1293d36b92c2f470)shell\_flag

| enum [shell\_flag](group__shell__api.md#ga56bf30741f9ec7a6d94e5c18c2858948) shell::shell\_flag |
| --- |

## [◆ ](#ad62262b6b4fa8e56a0e8849f09603b3a)stack

| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)\* shell::stack |
| --- |

## [◆ ](#a642e7d8fa92464147329247e1325ad2b)stats

| struct [shell\_stats](structshell__stats.md)\* shell::stats |
| --- |

## [◆ ](#a01b4739356f2428527f322662a3bf0a7)thread

| struct [k\_thread](structk__thread.md)\* shell::thread |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell.h](shell_2shell_8h_source.md)

- [shell](structshell.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
