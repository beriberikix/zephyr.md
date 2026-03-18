---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/jwt_8h.html
original_path: doxygen/html/jwt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

jwt.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](jwt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [jwt\_builder](structjwt__builder.md) |
|  | JWT data tracking. [More...](structjwt__builder.md#details) |

| Functions | |
| --- | --- |
| int | [jwt\_init\_builder](group__jwt.md#gab10ee40ee3c0b3eea98051c2acbb8a75) (struct [jwt\_builder](structjwt__builder.md) \*builder, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Initialize the JWT builder. |
| int | [jwt\_add\_payload](group__jwt.md#ga209dc2bdbaf72b4c9d11be02e0ffe479) (struct [jwt\_builder](structjwt__builder.md) \*builder, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) exp, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) iat, const char \*aud) |
|  | add JWT primary payload. |
| int | [jwt\_sign](group__jwt.md#gaa000189c83e9b9113f401cd7d523cefe) (struct [jwt\_builder](structjwt__builder.md) \*builder, const char \*der\_key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) der\_key\_len) |
|  | Sign the JWT token. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [jwt\_payload\_len](group__jwt.md#gaab49bf586392b0687aff97a27238fe85) (struct [jwt\_builder](structjwt__builder.md) \*builder) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [jwt.h](jwt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
