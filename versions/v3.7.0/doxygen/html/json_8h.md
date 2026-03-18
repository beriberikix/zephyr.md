---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/json_8h.html
original_path: doxygen/html/json_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

json.h File Reference

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](json_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [json\_token](structjson__token.md) |
| struct | [json\_lexer](structjson__lexer.md) |
| struct | [json\_obj](structjson__obj.md) |
| struct | [json\_obj\_token](structjson__obj__token.md) |
| struct | [json\_obj\_descr](structjson__obj__descr.md) |

| Macros | |
| --- | --- |
| #define | [JSON\_OBJ\_DESCR\_PRIM](group__json.md#ga1ed917f5a247ca33f2778afe62ff1a88)(struct\_, field\_name\_, type\_) |
|  | Helper macro to declare a descriptor for supported primitive values. |
| #define | [JSON\_OBJ\_DESCR\_OBJECT](group__json.md#ga4ee365f43cfa86a214973defe81f1e88)(struct\_, field\_name\_, sub\_descr\_) |
|  | Helper macro to declare a descriptor for an object value. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY](group__json.md#ga0b510decbc755c82903b54fcbc4a3b64)(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_type\_) |
|  | Helper macro to declare a descriptor for an array of primitives. |
| #define | [JSON\_OBJ\_DESCR\_OBJ\_ARRAY](group__json.md#gae012264df03546a1c01eec4216b52ffd)(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Helper macro to declare a descriptor for an array of objects. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY\_ARRAY](group__json.md#gaed8189235fd30d2bc041cafee9591ec9)(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Helper macro to declare a descriptor for an array of array. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED](group__json.md#ga9fea9111ac1024c8feb066cd53a4045b)(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Variant of JSON\_OBJ\_DESCR\_ARRAY\_ARRAY that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_PRIM\_NAMED](group__json.md#gaad081c4f8debcb41779bd5879ed8bbd4)(struct\_, json\_field\_name\_, struct\_field\_name\_, type\_) |
|  | Variant of JSON\_OBJ\_DESCR\_PRIM that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_OBJECT\_NAMED](group__json.md#ga8f8d03241e4f69d5f7147792db9a9fe9)(struct\_, json\_field\_name\_, struct\_field\_name\_, sub\_descr\_) |
|  | Variant of JSON\_OBJ\_DESCR\_OBJECT that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY\_NAMED](group__json.md#ga4a5bafd64de8abcbc2b5c039bd59ec84)(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_type\_) |
|  | Variant of JSON\_OBJ\_DESCR\_ARRAY that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED](group__json.md#gaa6602833e59c7e5205d69cc7c4ab2bba)(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Variant of JSON\_OBJ\_DESCR\_OBJ\_ARRAY that can be used when the structure and JSON field names differ. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674)) (const char \*bytes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*data) |
|  | Function pointer type to append bytes to a buffer while encoding JSON data. |

| Enumerations | |
| --- | --- |
| enum | [json\_tokens](group__json.md#ga18a137ac5e2998d375540298670797c4) {     [JSON\_TOK\_NONE](group__json.md#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77) = '\_' , [JSON\_TOK\_OBJECT\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8) = '{' , [JSON\_TOK\_OBJECT\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911) = '}' , [JSON\_TOK\_ARRAY\_START](group__json.md#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd) = '[' ,     [JSON\_TOK\_ARRAY\_END](group__json.md#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9) = ']' , [JSON\_TOK\_STRING](group__json.md#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc) = '"' , [JSON\_TOK\_COLON](group__json.md#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) = ':' , [JSON\_TOK\_COMMA](group__json.md#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) = ',' ,     [JSON\_TOK\_NUMBER](group__json.md#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) = '0' , [JSON\_TOK\_FLOAT](group__json.md#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) = '1' , [JSON\_TOK\_OPAQUE](group__json.md#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) = '2' , [JSON\_TOK\_OBJ\_ARRAY](group__json.md#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) = '3' ,     [JSON\_TOK\_ENCODED\_OBJ](group__json.md#gga18a137ac5e2998d375540298670797c4af1e451cb321c805cff8fcde3561d3e64) = '4' , [JSON\_TOK\_TRUE](group__json.md#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) = 't' , [JSON\_TOK\_FALSE](group__json.md#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) = 'f' , [JSON\_TOK\_NULL](group__json.md#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) = 'n' ,     [JSON\_TOK\_ERROR](group__json.md#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) = '!' , [JSON\_TOK\_EOF](group__json.md#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) = '\0'   } |

| Functions | |
| --- | --- |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [json\_obj\_parse](group__json.md#ga73997fa2154fcbc80f37edd7bcf3477a) (char \*json, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, void \*val) |
|  | Parses the JSON-encoded object pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*. |
| int | [json\_arr\_parse](group__json.md#gab4e6ad4a040c271d74eaa313c580a739) (char \*json, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, void \*val) |
|  | Parses the JSON-encoded array pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*. |
| int | [json\_arr\_separate\_object\_parse\_init](group__json.md#ga6196411958e2e9b3683af4c281214b92) (struct [json\_obj](structjson__obj.md) \*json, char \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Initialize single-object array parsing. |
| int | [json\_arr\_separate\_parse\_object](group__json.md#ga64859a835e7cb88c2499360fb00ca344) (struct [json\_obj](structjson__obj.md) \*json, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, void \*val) |
|  | Parse a single object from array. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [json\_escape](group__json.md#ga43ee6d1fbd3fa8fb2ae052844b465dda) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Escapes the string so it can be used to encode JSON objects. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [json\_calc\_escaped\_len](group__json.md#ga5ef155a3a6444801592badd6a092734c) (const char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Calculates the JSON-escaped string length. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [json\_calc\_encoded\_len](group__json.md#ga41e6e90beef8bae12fca1de2584145bb) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, const void \*val) |
|  | Calculates the string length to fully encode an object. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [json\_calc\_encoded\_arr\_len](group__json.md#gad612b8441a21dca34cfeec6257877509) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val) |
|  | Calculates the string length to fully encode an array. |
| int | [json\_obj\_encode\_buf](group__json.md#gab758ad32cfb6369f4967a6842ac63245) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, const void \*val, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Encodes an object in a contiguous memory location. |
| int | [json\_arr\_encode\_buf](group__json.md#gafd27bbcb898dc902cf1dadd3369cf923) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Encodes an array in a contiguous memory location. |
| int | [json\_obj\_encode](group__json.md#gafec772f687a0280f5211139bd019e582) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, const void \*val, [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data) |
|  | Encodes an object using an arbitrary writer function. |
| int | [json\_arr\_encode](group__json.md#ga4ffccdc602ab98d489499bf6fa4fa6c5) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val, [json\_append\_bytes\_t](group__json.md#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data) |
|  | Encodes an array using an arbitrary writer function. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [json.h](json_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
