---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/parser_8h.html
original_path: doxygen/html/parser_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

parser.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/net/http/method.h](method_8h_source.md)>`  
`#include <[zephyr/net/http/parser_state.h](parser__state_8h_source.md)>`  
`#include <[zephyr/net/http/parser_url.h](parser__url_8h_source.md)>`

[Go to the source code of this file.](parser_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http\_parser](structhttp__parser.md) |
| struct | [http\_parser\_settings](structhttp__parser__settings.md) |

| Macros | |
| --- | --- |
| #define | [HTTP\_PARSER\_VERSION\_MAJOR](#abfeef6f3e39791acc311791feda09d27)   2 |
| #define | [HTTP\_PARSER\_VERSION\_MINOR](#ab8479153443ca4fe95b3de5adb0224de)   7 |
| #define | [HTTP\_PARSER\_VERSION\_PATCH](#afb999672cce2ebd7f952bd3f28d8f5e5)   1 |
| #define | [HTTP\_MAX\_HEADER\_SIZE](#a6272a7f92e0f1b66e07680f32f6f21b6)   (80 \* 1024) |
| #define | [HTTP\_PARSER\_ERRNO](#a356ebaa93536e6f94c2948a1416697c7)(p) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [http\_data\_cb](#a1aab76595c275d0615cbea1cee1807c8)) (struct [http\_parser](structhttp__parser.md) \*, const char \*at, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
| typedef int(\* | [http\_cb](#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)) (struct [http\_parser](structhttp__parser.md) \*) |

| Enumerations | |
| --- | --- |
| enum | [http\_parser\_type](#af9d6d304f8c255158175951b434cfa7a) { [HTTP\_REQUEST](#af9d6d304f8c255158175951b434cfa7aa9f727b57e9e9c1651ee0df29aa1b1713) , [HTTP\_RESPONSE](#af9d6d304f8c255158175951b434cfa7aa132597b93208763e8e81c4a4a0e8a642) , [HTTP\_BOTH](#af9d6d304f8c255158175951b434cfa7aadac18fbd072752213fd5308bb5fc8684) } |
| enum | [flags](#ab6b306ef981f5e21bb41ea2c2dbe8cd9) {     [F\_CHUNKED](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a092619f8f7babc8fc3fa7533e78c3c29) = 1 << 0 , [F\_CONNECTION\_KEEP\_ALIVE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a5c5e8921e5747d1128ad9611a6d4a782) = 1 << 1 , [F\_CONNECTION\_CLOSE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a133e98dc07339e6c1605f32fc4fd6c78) = 1 << 2 , [F\_CONNECTION\_UPGRADE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9af0eea4f6920c6ff5c68cdd1f2e27d044) = 1 << 3 ,     [F\_TRAILING](#ab6b306ef981f5e21bb41ea2c2dbe8cd9aa75b5b1dcec2decaa7386264d4e1dc29) = 1 << 4 , [F\_UPGRADE](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a600ff486c803dcf2ec13453bdaf1100c) = 1 << 5 , [F\_SKIPBODY](#ab6b306ef981f5e21bb41ea2c2dbe8cd9ae71592851a69f477b80b1947399c1740) = 1 << 6 , [F\_CONTENTLENGTH](#ab6b306ef981f5e21bb41ea2c2dbe8cd9a9b2f205685c9ce94d3d73148de48decb) = 1 << 7   } |
| enum | [http\_errno](#a14687aec2341ce0e62db2e543dd1da64) {     [HPE\_OK](#a14687aec2341ce0e62db2e543dd1da64adf532f653497f3085108a5e1f097aa8e) , [HPE\_CB\_message\_begin](#a14687aec2341ce0e62db2e543dd1da64a5b44995fcd173cf38a88fc3ceaf0cb41) , [HPE\_CB\_url](#a14687aec2341ce0e62db2e543dd1da64ae15b73f73f8aad8c5e39d03b29414f9b) , [HPE\_CB\_header\_field](#a14687aec2341ce0e62db2e543dd1da64ade6f685cd47ad03c836aeee97efff1ed) ,     [HPE\_CB\_header\_value](#a14687aec2341ce0e62db2e543dd1da64aceed4040be7acf32b6bceb3aace8405e) , [HPE\_CB\_headers\_complete](#a14687aec2341ce0e62db2e543dd1da64a5d82bb467f93eed296d892408c44816a) , [HPE\_CB\_body](#a14687aec2341ce0e62db2e543dd1da64a5dc4b0888f48cd87fc3ded374ffac8a2) , [HPE\_CB\_message\_complete](#a14687aec2341ce0e62db2e543dd1da64ae0f56ef0ecc6638fb0594d130a1ee490) ,     [HPE\_CB\_status](#a14687aec2341ce0e62db2e543dd1da64a9adad03852eddb1f361abe9d856a1a0f) , [HPE\_CB\_chunk\_header](#a14687aec2341ce0e62db2e543dd1da64a69ccadce5be8074b104b19aa74dce556) , [HPE\_CB\_chunk\_complete](#a14687aec2341ce0e62db2e543dd1da64a008e232118d6133c4dbdd9770d926694) , [HPE\_INVALID\_EOF\_STATE](#a14687aec2341ce0e62db2e543dd1da64a4103809c185fee62b11c188ff0eab39a) ,     [HPE\_HEADER\_OVERFLOW](#a14687aec2341ce0e62db2e543dd1da64a5270cdc2f8af1802ccf3a2f33fde9307) , [HPE\_CLOSED\_CONNECTION](#a14687aec2341ce0e62db2e543dd1da64a7fbc6a25f20237b1cc795db489312e8e) , [HPE\_INVALID\_VERSION](#a14687aec2341ce0e62db2e543dd1da64a5a1b7ae13c36ef37fd52b2b68112b501) , [HPE\_INVALID\_STATUS](#a14687aec2341ce0e62db2e543dd1da64aa4a2007f1dc03bf22aff5ca8885f6b59) ,     [HPE\_INVALID\_METHOD](#a14687aec2341ce0e62db2e543dd1da64ac031cfd48285e22ddec18964f6281f6e) , [HPE\_INVALID\_URL](#a14687aec2341ce0e62db2e543dd1da64ad92573bf62e7b0a13d398926a984fa9d) , [HPE\_INVALID\_HOST](#a14687aec2341ce0e62db2e543dd1da64a6391e880280eda55707145bda1170294) , [HPE\_INVALID\_PORT](#a14687aec2341ce0e62db2e543dd1da64a3e7c3b8a95f34bbd40ea047fcd43ffa5) ,     [HPE\_INVALID\_PATH](#a14687aec2341ce0e62db2e543dd1da64a69e17a8b5a35b9f93ea914224c2d4f2a) , [HPE\_INVALID\_QUERY\_STRING](#a14687aec2341ce0e62db2e543dd1da64a383ef24f0ac59de1c128ca776d813865) , [HPE\_INVALID\_FRAGMENT](#a14687aec2341ce0e62db2e543dd1da64afa80e3a0c0dd1c93cf0a11cacbd59079) , [HPE\_LF\_EXPECTED](#a14687aec2341ce0e62db2e543dd1da64af9f23325bd502239af0326a0b407b41d) ,     [HPE\_INVALID\_HEADER\_TOKEN](#a14687aec2341ce0e62db2e543dd1da64ac0348f1ca04bf4d882affcd0249336b5) , [HPE\_INVALID\_CONTENT\_LENGTH](#a14687aec2341ce0e62db2e543dd1da64a18b873c41a1d7aa9ee9486f719aa7509) , [HPE\_UNEXPECTED\_CONTENT\_LENGTH](#a14687aec2341ce0e62db2e543dd1da64a2406df24d500b1228fc5ef4a8d60e7c3) , [HPE\_INVALID\_CHUNK\_SIZE](#a14687aec2341ce0e62db2e543dd1da64a36842cc306c491da8c42023be68585e9) ,     [HPE\_INVALID\_CONSTANT](#a14687aec2341ce0e62db2e543dd1da64a1b9ec4aeef6f168f9d711c27a0c6faa8) , [HPE\_INVALID\_INTERNAL\_STATE](#a14687aec2341ce0e62db2e543dd1da64abb98b653c0972e3e22bc5ff8b57d0d55) , [HPE\_STRICT](#a14687aec2341ce0e62db2e543dd1da64a7f92de0f01b2d0e37209854069183f16) , [HPE\_PAUSED](#a14687aec2341ce0e62db2e543dd1da64aed64f2a65634183e8f708ac80af3f6f2) ,     [HPE\_UNKNOWN](#a14687aec2341ce0e62db2e543dd1da64a36cb81d8c40b00602b558f82a38eaecc)   } |

| Functions | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [http\_parser\_version](#a2559b4d373c7f0d85c77a2a3c308a5ee) (void) |
| void | [http\_parser\_init](#ab8ae8e721c5c9f7309e94c174c72a940) (struct [http\_parser](structhttp__parser.md) \*parser, enum [http\_parser\_type](#af9d6d304f8c255158175951b434cfa7a) type) |
| void | [http\_parser\_settings\_init](#a76d2e1f7225617f6941042fc95d888fe) (struct [http\_parser\_settings](structhttp__parser__settings.md) \*settings) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [http\_parser\_execute](#a54f1346f15b326f6308a3ff7f0f75b52) (struct [http\_parser](structhttp__parser.md) \*parser, const struct [http\_parser\_settings](structhttp__parser__settings.md) \*settings, const char \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int | [http\_should\_keep\_alive](#a903c39c3abea292860780856ba90d560) (const struct [http\_parser](structhttp__parser.md) \*parser) |
| const char \* | [http\_method\_str](#abb207665b6ff41700e5bbb260b580cb6) (enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) m) |
| const char \* | [http\_errno\_name](#acce1b9056442d75d4d609e797bcce2fd) (enum [http\_errno](#a14687aec2341ce0e62db2e543dd1da64) err) |
| const char \* | [http\_errno\_description](#a88adfab20d97366aac1fe05aa7dde7da) (enum [http\_errno](#a14687aec2341ce0e62db2e543dd1da64) err) |
| void | [http\_parser\_pause](#aa3764343ba4d2bb13fe39b05425633ba) (struct [http\_parser](structhttp__parser.md) \*parser, int paused) |
| int | [http\_body\_is\_final](#a5156a631a251516a6e78b17e1faadbb2) (const struct [http\_parser](structhttp__parser.md) \*parser) |

## Macro Definition Documentation

## [◆ ](#a6272a7f92e0f1b66e07680f32f6f21b6)HTTP\_MAX\_HEADER\_SIZE

| #define HTTP\_MAX\_HEADER\_SIZE   (80 \* 1024) |
| --- |

## [◆ ](#a356ebaa93536e6f94c2948a1416697c7)HTTP\_PARSER\_ERRNO

| #define HTTP\_PARSER\_ERRNO | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((enum [http\_errno](#a14687aec2341ce0e62db2e543dd1da64)) (p)->http\_errno)

[http\_errno](#a14687aec2341ce0e62db2e543dd1da64)

http\_errno

**Definition** parser.h:107

## [◆ ](#abfeef6f3e39791acc311791feda09d27)HTTP\_PARSER\_VERSION\_MAJOR

| #define HTTP\_PARSER\_VERSION\_MAJOR   2 |
| --- |

## [◆ ](#ab8479153443ca4fe95b3de5adb0224de)HTTP\_PARSER\_VERSION\_MINOR

| #define HTTP\_PARSER\_VERSION\_MINOR   7 |
| --- |

## [◆ ](#afb999672cce2ebd7f952bd3f28d8f5e5)HTTP\_PARSER\_VERSION\_PATCH

| #define HTTP\_PARSER\_VERSION\_PATCH   1 |
| --- |

## Typedef Documentation

## [◆ ](#aa0f8424a6e7d3dd0b2f3b6358b57f1a1)http\_cb

| typedef int(\* http\_cb) (struct [http\_parser](structhttp__parser.md) \*) |
| --- |

## [◆ ](#a1aab76595c275d0615cbea1cee1807c8)http\_data\_cb

| typedef int(\* http\_data\_cb) (struct [http\_parser](structhttp__parser.md) \*, const char \*at, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
| --- |

## Enumeration Type Documentation

## [◆ ](#ab6b306ef981f5e21bb41ea2c2dbe8cd9)flags

| enum [flags](#ab6b306ef981f5e21bb41ea2c2dbe8cd9) |
| --- |

| Enumerator | |
| --- | --- |
| F\_CHUNKED |  |
| F\_CONNECTION\_KEEP\_ALIVE |  |
| F\_CONNECTION\_CLOSE |  |
| F\_CONNECTION\_UPGRADE |  |
| F\_TRAILING |  |
| F\_UPGRADE |  |
| F\_SKIPBODY |  |
| F\_CONTENTLENGTH |  |

## [◆ ](#a14687aec2341ce0e62db2e543dd1da64)http\_errno

| enum [http\_errno](#a14687aec2341ce0e62db2e543dd1da64) |
| --- |

| Enumerator | |
| --- | --- |
| HPE\_OK |  |
| HPE\_CB\_message\_begin |  |
| HPE\_CB\_url |  |
| HPE\_CB\_header\_field |  |
| HPE\_CB\_header\_value |  |
| HPE\_CB\_headers\_complete |  |
| HPE\_CB\_body |  |
| HPE\_CB\_message\_complete |  |
| HPE\_CB\_status |  |
| HPE\_CB\_chunk\_header |  |
| HPE\_CB\_chunk\_complete |  |
| HPE\_INVALID\_EOF\_STATE |  |
| HPE\_HEADER\_OVERFLOW |  |
| HPE\_CLOSED\_CONNECTION |  |
| HPE\_INVALID\_VERSION |  |
| HPE\_INVALID\_STATUS |  |
| HPE\_INVALID\_METHOD |  |
| HPE\_INVALID\_URL |  |
| HPE\_INVALID\_HOST |  |
| HPE\_INVALID\_PORT |  |
| HPE\_INVALID\_PATH |  |
| HPE\_INVALID\_QUERY\_STRING |  |
| HPE\_INVALID\_FRAGMENT |  |
| HPE\_LF\_EXPECTED |  |
| HPE\_INVALID\_HEADER\_TOKEN |  |
| HPE\_INVALID\_CONTENT\_LENGTH |  |
| HPE\_UNEXPECTED\_CONTENT\_LENGTH |  |
| HPE\_INVALID\_CHUNK\_SIZE |  |
| HPE\_INVALID\_CONSTANT |  |
| HPE\_INVALID\_INTERNAL\_STATE |  |
| HPE\_STRICT |  |
| HPE\_PAUSED |  |
| HPE\_UNKNOWN |  |

## [◆ ](#af9d6d304f8c255158175951b434cfa7a)http\_parser\_type

| enum [http\_parser\_type](#af9d6d304f8c255158175951b434cfa7a) |
| --- |

| Enumerator | |
| --- | --- |
| HTTP\_REQUEST |  |
| HTTP\_RESPONSE |  |
| HTTP\_BOTH |  |

## Function Documentation

## [◆ ](#a5156a631a251516a6e78b17e1faadbb2)http\_body\_is\_final()

| int http\_body\_is\_final | ( | const struct [http\_parser](structhttp__parser.md) \* | *parser* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a88adfab20d97366aac1fe05aa7dde7da)http\_errno\_description()

| const char \* http\_errno\_description | ( | enum [http\_errno](#a14687aec2341ce0e62db2e543dd1da64) | *err* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#acce1b9056442d75d4d609e797bcce2fd)http\_errno\_name()

| const char \* http\_errno\_name | ( | enum [http\_errno](#a14687aec2341ce0e62db2e543dd1da64) | *err* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#abb207665b6ff41700e5bbb260b580cb6)http\_method\_str()

| const char \* http\_method\_str | ( | enum [http\_method](group__http__methods.md#gaacd5f203e33ac338ca5cb8f02a3ff3b8) | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a54f1346f15b326f6308a3ff7f0f75b52)http\_parser\_execute()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_parser\_execute | ( | struct [http\_parser](structhttp__parser.md) \* | *parser*, |
| --- | --- | --- | --- |
|  |  | const struct [http\_parser\_settings](structhttp__parser__settings.md) \* | *settings*, |
|  |  | const char \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

## [◆ ](#ab8ae8e721c5c9f7309e94c174c72a940)http\_parser\_init()

| void http\_parser\_init | ( | struct [http\_parser](structhttp__parser.md) \* | *parser*, |
| --- | --- | --- | --- |
|  |  | enum [http\_parser\_type](#af9d6d304f8c255158175951b434cfa7a) | *type* ) |

## [◆ ](#aa3764343ba4d2bb13fe39b05425633ba)http\_parser\_pause()

| void http\_parser\_pause | ( | struct [http\_parser](structhttp__parser.md) \* | *parser*, |
| --- | --- | --- | --- |
|  |  | int | *paused* ) |

## [◆ ](#a76d2e1f7225617f6941042fc95d888fe)http\_parser\_settings\_init()

| void http\_parser\_settings\_init | ( | struct [http\_parser\_settings](structhttp__parser__settings.md) \* | *settings* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2559b4d373c7f0d85c77a2a3c308a5ee)http\_parser\_version()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long http\_parser\_version | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a903c39c3abea292860780856ba90d560)http\_should\_keep\_alive()

| int http\_should\_keep\_alive | ( | const struct [http\_parser](structhttp__parser.md) \* | *parser* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [parser.h](parser_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
