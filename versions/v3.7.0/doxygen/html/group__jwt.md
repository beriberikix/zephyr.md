---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__jwt.html
original_path: doxygen/html/group__jwt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

JSON Web Token (JWT)

[Utilities](group__utilities.md) » [JSON](group__json.md)

JSON Web Token (JWT).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [jwt\_builder](structjwt__builder.md) |
|  | JWT data tracking. [More...](structjwt__builder.md#details) |

| Functions | |
| --- | --- |
| int | [jwt\_init\_builder](#gab10ee40ee3c0b3eea98051c2acbb8a75) (struct [jwt\_builder](structjwt__builder.md) \*builder, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Initialize the JWT builder. |
| int | [jwt\_add\_payload](#ga209dc2bdbaf72b4c9d11be02e0ffe479) (struct [jwt\_builder](structjwt__builder.md) \*builder, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) exp, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) iat, const char \*aud) |
|  | add JWT primary payload. |
| int | [jwt\_sign](#gaa000189c83e9b9113f401cd7d523cefe) (struct [jwt\_builder](structjwt__builder.md) \*builder, const char \*der\_key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) der\_key\_len) |
|  | Sign the JWT token. |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [jwt\_payload\_len](#gaab49bf586392b0687aff97a27238fe85) (struct [jwt\_builder](structjwt__builder.md) \*builder) |

## Detailed Description

JSON Web Token (JWT).

## Function Documentation

## [◆ ](#ga209dc2bdbaf72b4c9d11be02e0ffe479)jwt\_add\_payload()

| int jwt\_add\_payload | ( | struct [jwt\_builder](structjwt__builder.md) \* | *builder*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *exp*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *iat*, |
|  |  | const char \* | *aud* ) |

`#include <[jwt.h](jwt_8h.md)>`

add JWT primary payload.

## [◆ ](#gab10ee40ee3c0b3eea98051c2acbb8a75)jwt\_init\_builder()

| int jwt\_init\_builder | ( | struct [jwt\_builder](structjwt__builder.md) \* | *builder*, |
| --- | --- | --- | --- |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buffer\_size* ) |

`#include <[jwt.h](jwt_8h.md)>`

Initialize the JWT builder.

Initialize the given JWT builder for the creation of a fresh token. The buffer size should at least be as long as JWT\_BUILDER\_MAX\_SIZE returns.

Parameters
:   | builder | The builder to initialize. |
    | --- | --- |
    | buffer | The buffer to write the token to. |
    | buffer\_size | The size of this buffer. The token will be NULL terminated, which needs to be allowed for in this size. |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOSPC | Buffer is insufficient to initialize |

## [◆ ](#gaab49bf586392b0687aff97a27238fe85)jwt\_payload\_len()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) jwt\_payload\_len | ( | struct [jwt\_builder](structjwt__builder.md) \* | *builder* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[jwt.h](jwt_8h.md)>`

## [◆ ](#gaa000189c83e9b9113f401cd7d523cefe)jwt\_sign()

| int jwt\_sign | ( | struct [jwt\_builder](structjwt__builder.md) \* | *builder*, |
| --- | --- | --- | --- |
|  |  | const char \* | *der\_key*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *der\_key\_len* ) |

`#include <[jwt.h](jwt_8h.md)>`

Sign the JWT token.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
