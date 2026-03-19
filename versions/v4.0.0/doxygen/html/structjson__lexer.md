---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structjson__lexer.html
original_path: doxygen/html/structjson__lexer.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

json\_lexer Struct Reference

[Utilities](group__utilities.md) » [JSON](group__json.md)

`#include <[json.h](json_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \*(\* | [state](#ae74beb9d896daf102ec5ffff370830b3) )(struct [json\_lexer](structjson__lexer.md) \*lex) |
| char \* | [start](#aa4d4a29301fb840c691bbfa416474de4) |
| char \* | [pos](#a9b403c5505e9a2cd9e475416b2e7f0ac) |
| char \* | [end](#aeaf5743a9285e0aef9df99f9b3b48320) |
| struct [json\_token](structjson__token.md) | [tok](#ab285bc72bf12a4de31b45ac0fc992620) |

## Field Documentation

## [◆ ](#aeaf5743a9285e0aef9df99f9b3b48320)end

| char\* json\_lexer::end |
| --- |

## [◆ ](#a9b403c5505e9a2cd9e475416b2e7f0ac)pos

| char\* json\_lexer::pos |
| --- |

## [◆ ](#aa4d4a29301fb840c691bbfa416474de4)start

| char\* json\_lexer::start |
| --- |

## [◆ ](#ae74beb9d896daf102ec5ffff370830b3)state

| void \*(\* json\_lexer::state) (struct [json\_lexer](structjson__lexer.md) \*lex) |
| --- |

## [◆ ](#ab285bc72bf12a4de31b45ac0fc992620)tok

| struct [json\_token](structjson__token.md) json\_lexer::tok |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/data/[json.h](json_8h_source.md)

- [json\_lexer](structjson__lexer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
