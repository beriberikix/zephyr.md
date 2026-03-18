---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__json.html
original_path: doxygen/html/group__json.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

JSON

[Utilities](group__utilities.md)

| Topics | |
| --- | --- |
|  | [JSON Web Token (JWT)](group__jwt.md) |
|  | JSON Web Token (JWT). |

| Data Structures | |
| --- | --- |
| struct | [json\_token](structjson__token.md) |
| struct | [json\_lexer](structjson__lexer.md) |
| struct | [json\_obj](structjson__obj.md) |
| struct | [json\_obj\_token](structjson__obj__token.md) |
| struct | [json\_obj\_descr](structjson__obj__descr.md) |

| Macros | |
| --- | --- |
| #define | [JSON\_OBJ\_DESCR\_PRIM](#ga1ed917f5a247ca33f2778afe62ff1a88)(struct\_, field\_name\_, type\_) |
|  | Helper macro to declare a descriptor for supported primitive values. |
| #define | [JSON\_OBJ\_DESCR\_OBJECT](#ga4ee365f43cfa86a214973defe81f1e88)(struct\_, field\_name\_, sub\_descr\_) |
|  | Helper macro to declare a descriptor for an object value. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY](#ga0b510decbc755c82903b54fcbc4a3b64)(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_type\_) |
|  | Helper macro to declare a descriptor for an array of primitives. |
| #define | [JSON\_OBJ\_DESCR\_OBJ\_ARRAY](#gae012264df03546a1c01eec4216b52ffd)(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Helper macro to declare a descriptor for an array of objects. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY\_ARRAY](#gaed8189235fd30d2bc041cafee9591ec9)(struct\_, field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Helper macro to declare a descriptor for an array of array. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED](#ga9fea9111ac1024c8feb066cd53a4045b)(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Variant of JSON\_OBJ\_DESCR\_ARRAY\_ARRAY that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_PRIM\_NAMED](#gaad081c4f8debcb41779bd5879ed8bbd4)(struct\_, json\_field\_name\_, struct\_field\_name\_, type\_) |
|  | Variant of JSON\_OBJ\_DESCR\_PRIM that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_OBJECT\_NAMED](#ga8f8d03241e4f69d5f7147792db9a9fe9)(struct\_, json\_field\_name\_, struct\_field\_name\_, sub\_descr\_) |
|  | Variant of JSON\_OBJ\_DESCR\_OBJECT that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_ARRAY\_NAMED](#ga4a5bafd64de8abcbc2b5c039bd59ec84)(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_type\_) |
|  | Variant of JSON\_OBJ\_DESCR\_ARRAY that can be used when the structure and JSON field names differ. |
| #define | [JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED](#gaa6602833e59c7e5205d69cc7c4ab2bba)(struct\_, json\_field\_name\_, struct\_field\_name\_, max\_len\_, len\_field\_, elem\_descr\_, elem\_descr\_len\_) |
|  | Variant of JSON\_OBJ\_DESCR\_OBJ\_ARRAY that can be used when the structure and JSON field names differ. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [json\_append\_bytes\_t](#gacb409ebe9c59789a5d9aca02c6c94674)) (const char \*bytes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*data) |
|  | Function pointer type to append bytes to a buffer while encoding JSON data. |

| Enumerations | |
| --- | --- |
| enum | [json\_tokens](#ga18a137ac5e2998d375540298670797c4) {     [JSON\_TOK\_NONE](#gga18a137ac5e2998d375540298670797c4a926d6b0a5458be2e707d51f0b25dbe77) = '\_' , [JSON\_TOK\_OBJECT\_START](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8) = '{' , [JSON\_TOK\_OBJECT\_END](#gga18a137ac5e2998d375540298670797c4a835bc516b25eb0619b3f1a52f1ebc911) = '}' , [JSON\_TOK\_LIST\_START](#gga18a137ac5e2998d375540298670797c4a8f9beceabf104da239f713e23b91d76b) = '[' ,     [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd) = '[' , [JSON\_TOK\_LIST\_END](#gga18a137ac5e2998d375540298670797c4a5e90a7b034a4af48a1b90fad7675a88d) = ']' , [JSON\_TOK\_ARRAY\_END](#gga18a137ac5e2998d375540298670797c4a2483f21d814abcd08b5253e55aef70c9) = ']' , [JSON\_TOK\_STRING](#gga18a137ac5e2998d375540298670797c4ab145f07a93c4fdcf60c9052fbd9a7afc) = '"' ,     [JSON\_TOK\_COLON](#gga18a137ac5e2998d375540298670797c4a4873e5c0c6344323d5d6af158952ca36) = ':' , [JSON\_TOK\_COMMA](#gga18a137ac5e2998d375540298670797c4a736325745f9521f38a68962775e76a50) = ',' , [JSON\_TOK\_NUMBER](#gga18a137ac5e2998d375540298670797c4ae25f16ae591eb17d4074e6dcc2f1e62c) = '0' , [JSON\_TOK\_FLOAT](#gga18a137ac5e2998d375540298670797c4aa842c96d114ed77ab66446bcac1424b5) = '1' ,     [JSON\_TOK\_OPAQUE](#gga18a137ac5e2998d375540298670797c4a94ef68b273a74244acb3bdec99b6a024) = '2' , [JSON\_TOK\_OBJ\_ARRAY](#gga18a137ac5e2998d375540298670797c4a14739d9c36212d3df0007427b7b99e25) = '3' , [JSON\_TOK\_TRUE](#gga18a137ac5e2998d375540298670797c4a87ffb12e4d174bb4427d9a72eabca7e3) = 't' , [JSON\_TOK\_FALSE](#gga18a137ac5e2998d375540298670797c4a8df1b1d0061d7e289f94bae1df35baa7) = 'f' ,     [JSON\_TOK\_NULL](#gga18a137ac5e2998d375540298670797c4a93de1b7e780ac22744c97e922de3b35e) = 'n' , [JSON\_TOK\_ERROR](#gga18a137ac5e2998d375540298670797c4afe9c51f453d7dd02504071330a030e9e) = '!' , [JSON\_TOK\_EOF](#gga18a137ac5e2998d375540298670797c4ad970b7d8553296bf4ed03c831cb6f604) = '\0'   } |

| Functions | |
| --- | --- |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [json\_obj\_parse](#ga73997fa2154fcbc80f37edd7bcf3477a) (char \*json, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, void \*val) |
|  | Parses the JSON-encoded object pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*. |
| int | [json\_arr\_parse](#gab4e6ad4a040c271d74eaa313c580a739) (char \*json, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, void \*val) |
|  | Parses the JSON-encoded array pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*. |
| int | [json\_arr\_separate\_object\_parse\_init](#ga6196411958e2e9b3683af4c281214b92) (struct [json\_obj](structjson__obj.md) \*json, char \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Initialize single-object array parsing. |
| int | [json\_arr\_separate\_parse\_object](#ga64859a835e7cb88c2499360fb00ca344) (struct [json\_obj](structjson__obj.md) \*json, const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, void \*val) |
|  | Parse a single object from array. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [json\_escape](#ga43ee6d1fbd3fa8fb2ae052844b465dda) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Escapes the string so it can be used to encode JSON objects. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [json\_calc\_escaped\_len](#ga5ef155a3a6444801592badd6a092734c) (const char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Calculates the JSON-escaped string length. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [json\_calc\_encoded\_len](#ga41e6e90beef8bae12fca1de2584145bb) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, const void \*val) |
|  | Calculates the string length to fully encode an object. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [json\_calc\_encoded\_arr\_len](#gad612b8441a21dca34cfeec6257877509) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val) |
|  | Calculates the string length to fully encode an array. |
| int | [json\_obj\_encode\_buf](#gab758ad32cfb6369f4967a6842ac63245) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, const void \*val, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Encodes an object in a contiguous memory location. |
| int | [json\_arr\_encode\_buf](#gafd27bbcb898dc902cf1dadd3369cf923) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Encodes an array in a contiguous memory location. |
| int | [json\_obj\_encode](#gafec772f687a0280f5211139bd019e582) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) descr\_len, const void \*val, [json\_append\_bytes\_t](#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data) |
|  | Encodes an object using an arbitrary writer function. |
| int | [json\_arr\_encode](#ga4ffccdc602ab98d489499bf6fa4fa6c5) (const struct [json\_obj\_descr](structjson__obj__descr.md) \*descr, const void \*val, [json\_append\_bytes\_t](#gacb409ebe9c59789a5d9aca02c6c94674) append\_bytes, void \*data) |
|  | Encodes an array using an arbitrary writer function. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0b510decbc755c82903b54fcbc4a3b64)JSON\_OBJ\_DESCR\_ARRAY

| #define JSON\_OBJ\_DESCR\_ARRAY | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *field\_name\_*, |
|  |  |  | *max\_len\_*, |
|  |  |  | *len\_field\_*, |
|  |  |  | *elem\_type\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (#field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(#field\_name\_) - 1, \

.type = [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

.offset = offsetof(struct\_, field\_name\_), \

{ \

.array = { \

.element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

elem\_type\_,), \

.n\_elements = (max\_len\_), \

}, \

}, \

}

[JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd)

@ JSON\_TOK\_ARRAY\_START

**Definition** json.h:37

Helper macro to declare a descriptor for an array of primitives.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | field\_name\_ | Field name in the struct |
    | max\_len\_ | Maximum number of elements in array |
    | len\_field\_ | Field name in the struct for the number of elements in the array |
    | elem\_type\_ | Element type, must be a primitive type |

Here's an example of use:

```
 struct example {
     int32_t foo[10];
     size_t foo_len;
 };

 struct json_obj_descr array[] = {
      JSON_OBJ_DESCR_ARRAY(struct example, foo, 10, foo_len,
                           JSON_TOK_NUMBER)
 };
```

## [◆ ](#gaed8189235fd30d2bc041cafee9591ec9)JSON\_OBJ\_DESCR\_ARRAY\_ARRAY

| #define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *field\_name\_*, |
|  |  |  | *max\_len\_*, |
|  |  |  | *len\_field\_*, |
|  |  |  | *elem\_descr\_*, |
|  |  |  | *elem\_descr\_len\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (#field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(#field\_name\_) - 1, \

.type = [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

.offset = offsetof(struct\_, field\_name\_), \

{ \

.array = { \

.element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

struct\_, len\_field\_, [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

Z\_JSON\_DESCR\_ARRAY( \

elem\_descr\_, \

1 + [ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)(elem\_descr\_len\_ == 1))), \

.n\_elements = (max\_len\_), \

}, \

}, \

}

[ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)

#define ZERO\_OR\_COMPILE\_ERROR(cond)

0 if cond is true-ish; causes a compile error otherwise.

**Definition** util.h:94

Helper macro to declare a descriptor for an array of array.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | field\_name\_ | Field name in the struct containing the array |
    | max\_len\_ | Maximum number of elements in the array |
    | len\_field\_ | Field name in the struct for the number of elements in the array |
    | elem\_descr\_ | Element descriptor, pointer to a descriptor array |
    | elem\_descr\_len\_ | Number of elements in elem\_descr\_ |

Here's an example of use:

```
 struct person_height {
     const char *name;
     int32_t height;
 };

 struct person_heights_array {
     struct person_height heights;
 }

 struct people_heights {
     struct person_height_array heights[10];
     size_t heights_len;
 };

 struct json_obj_descr person_height_descr[] = {
     JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
     JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
 };

 struct json_obj_descr person_height_array_descr[] = {
     JSON_OBJ_DESCR_OBJECT(struct person_heights_array,
                           heights, person_height_descr),
 };

 struct json_obj_descr array_array[] = {
      JSON_OBJ_DESCR_ARRAY_ARRAY(struct people_heights, heights, 10,
                                 heights_len, person_height_array_descr,
                                 ARRAY_SIZE(person_height_array_descr)),
 };
```

## [◆ ](#ga9fea9111ac1024c8feb066cd53a4045b)JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED

| #define JSON\_OBJ\_DESCR\_ARRAY\_ARRAY\_NAMED | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *json\_field\_name\_*, |
|  |  |  | *struct\_field\_name\_*, |
|  |  |  | *max\_len\_*, |
|  |  |  | *len\_field\_*, |
|  |  |  | *elem\_descr\_*, |
|  |  |  | *elem\_descr\_len\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (#json\_field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(#json\_field\_name\_) - 1, \

.type = [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

.offset = offsetof(struct\_, struct\_field\_name\_), \

{ \

.array = { \

.element\_descr = Z\_JSON\_ELEMENT\_DESCR( \

struct\_, len\_field\_, [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

Z\_JSON\_DESCR\_ARRAY( \

elem\_descr\_, \

1 + [ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)(elem\_descr\_len\_ == 1))), \

.n\_elements = (max\_len\_), \

}, \

}, \

}

Variant of JSON\_OBJ\_DESCR\_ARRAY\_ARRAY that can be used when the structure and JSON field names differ.

This is useful when the JSON field is not a valid C identifier.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | json\_field\_name\_ | String, field name in JSON strings |
    | struct\_field\_name\_ | Field name in the struct containing the array |
    | max\_len\_ | Maximum number of elements in the array |
    | len\_field\_ | Field name in the struct for the number of elements in the array |
    | elem\_descr\_ | Element descriptor, pointer to a descriptor array |
    | elem\_descr\_len\_ | Number of elements in elem\_descr\_ |

See also
:   [JSON\_OBJ\_DESCR\_ARRAY\_ARRAY](#gaed8189235fd30d2bc041cafee9591ec9)

## [◆ ](#ga4a5bafd64de8abcbc2b5c039bd59ec84)JSON\_OBJ\_DESCR\_ARRAY\_NAMED

| #define JSON\_OBJ\_DESCR\_ARRAY\_NAMED | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *json\_field\_name\_*, |
|  |  |  | *struct\_field\_name\_*, |
|  |  |  | *max\_len\_*, |
|  |  |  | *len\_field\_*, |
|  |  |  | *elem\_type\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (json\_field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(json\_field\_name\_) - 1, \

.type = [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

.offset = offsetof(struct\_, struct\_field\_name\_), \

{ \

.array = { \

.element\_descr = \

Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, elem\_type\_,), \

.n\_elements = (max\_len\_), \

}, \

}, \

}

Variant of JSON\_OBJ\_DESCR\_ARRAY that can be used when the structure and JSON field names differ.

This is useful when the JSON field is not a valid C identifier.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | json\_field\_name\_ | String, field name in JSON strings |
    | struct\_field\_name\_ | Field name in the struct |
    | max\_len\_ | Maximum number of elements in array |
    | len\_field\_ | Field name in the struct for the number of elements in the array |
    | elem\_type\_ | Element type, must be a primitive type |

See also
:   [JSON\_OBJ\_DESCR\_ARRAY](#ga0b510decbc755c82903b54fcbc4a3b64)

## [◆ ](#gae012264df03546a1c01eec4216b52ffd)JSON\_OBJ\_DESCR\_OBJ\_ARRAY

| #define JSON\_OBJ\_DESCR\_OBJ\_ARRAY | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *field\_name\_*, |
|  |  |  | *max\_len\_*, |
|  |  |  | *len\_field\_*, |
|  |  |  | *elem\_descr\_*, |
|  |  |  | *elem\_descr\_len\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (#field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(#field\_name\_) - 1, \

.type = [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

.offset = offsetof(struct\_, field\_name\_), \

{ \

.array = { \

.element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

[JSON\_TOK\_OBJECT\_START](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8), \

Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

.n\_elements = (max\_len\_), \

}, \

}, \

}

[JSON\_TOK\_OBJECT\_START](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8)

@ JSON\_TOK\_OBJECT\_START

**Definition** json.h:33

Helper macro to declare a descriptor for an array of objects.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | field\_name\_ | Field name in the struct containing the array |
    | max\_len\_ | Maximum number of elements in the array |
    | len\_field\_ | Field name in the struct for the number of elements in the array |
    | elem\_descr\_ | Element descriptor, pointer to a descriptor array |
    | elem\_descr\_len\_ | Number of elements in elem\_descr\_ |

Here's an example of use:

```
 struct person_height {
     const char *name;
     int32_t height;
 };

 struct people_heights {
     struct person_height heights[10];
     size_t heights_len;
 };

 struct json_obj_descr person_height_descr[] = {
      JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
      JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
 };

 struct json_obj_descr array[] = {
      JSON_OBJ_DESCR_OBJ_ARRAY(struct people_heights, heights, 10,
                               heights_len, person_height_descr,
                               ARRAY_SIZE(person_height_descr)),
 };
```

## [◆ ](#gaa6602833e59c7e5205d69cc7c4ab2bba)JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED

| #define JSON\_OBJ\_DESCR\_OBJ\_ARRAY\_NAMED | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *json\_field\_name\_*, |
|  |  |  | *struct\_field\_name\_*, |
|  |  |  | *max\_len\_*, |
|  |  |  | *len\_field\_*, |
|  |  |  | *elem\_descr\_*, |
|  |  |  | *elem\_descr\_len\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = json\_field\_name\_, \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(json\_field\_name\_) - 1, \

.type = [JSON\_TOK\_ARRAY\_START](#gga18a137ac5e2998d375540298670797c4a9856446d3a2aa3155266957b8b1371cd), \

.offset = offsetof(struct\_, struct\_field\_name\_), \

{ \

.array = { \

.element\_descr = Z\_JSON\_ELEMENT\_DESCR(struct\_, len\_field\_, \

[JSON\_TOK\_OBJECT\_START](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8), \

Z\_JSON\_DESCR\_OBJ(elem\_descr\_, elem\_descr\_len\_)), \

.n\_elements = (max\_len\_), \

}, \

}, \

}

Variant of JSON\_OBJ\_DESCR\_OBJ\_ARRAY that can be used when the structure and JSON field names differ.

This is useful when the JSON field is not a valid C identifier.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | json\_field\_name\_ | String, field name of the array in JSON strings |
    | struct\_field\_name\_ | Field name in the struct containing the array |
    | max\_len\_ | Maximum number of elements in the array |
    | len\_field\_ | Field name in the struct for the number of elements in the array |
    | elem\_descr\_ | Element descriptor, pointer to a descriptor array |
    | elem\_descr\_len\_ | Number of elements in elem\_descr\_ |

Here's an example of use:

```
 struct person_height {
     const char *name;
     int32_t height;
 };

 struct people_heights {
     struct person_height heights[10];
     size_t heights_len;
 };

 struct json_obj_descr person_height_descr[] = {
      JSON_OBJ_DESCR_PRIM(struct person_height, name, JSON_TOK_STRING),
      JSON_OBJ_DESCR_PRIM(struct person_height, height, JSON_TOK_NUMBER),
 };

 struct json_obj_descr array[] = {
      JSON_OBJ_DESCR_OBJ_ARRAY_NAMED(struct people_heights,
                                     "people-heights", heights,
                                     10, heights_len,
                                     person_height_descr,
                                     ARRAY_SIZE(person_height_descr)),
 };
```

## [◆ ](#ga4ee365f43cfa86a214973defe81f1e88)JSON\_OBJ\_DESCR\_OBJECT

| #define JSON\_OBJ\_DESCR\_OBJECT | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *field\_name\_*, |
|  |  |  | *sub\_descr\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (#field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = (sizeof(#field\_name\_) - 1), \

.type = [JSON\_TOK\_OBJECT\_START](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8), \

.offset = offsetof(struct\_, field\_name\_), \

{ \

.object = { \

.sub\_descr = sub\_descr\_, \

.sub\_descr\_len = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(sub\_descr\_), \

}, \

}, \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

Helper macro to declare a descriptor for an object value.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | field\_name\_ | Field name in the struct |
    | sub\_descr\_ | Array of [json\_obj\_descr](structjson__obj__descr.md) describing the subobject |

Here's an example of use:

```
 struct nested {
     int32_t foo;
     struct {
        int32_t baz;
     } bar;
 };

 struct json_obj_descr nested_bar[] = {
     { ... declare bar.baz descriptor ... },
 };
 struct json_obj_descr nested[] = {
     { ... declare foo descriptor ... },
     JSON_OBJ_DESCR_OBJECT(struct nested, bar, nested_bar),
 };
```

## [◆ ](#ga8f8d03241e4f69d5f7147792db9a9fe9)JSON\_OBJ\_DESCR\_OBJECT\_NAMED

| #define JSON\_OBJ\_DESCR\_OBJECT\_NAMED | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *json\_field\_name\_*, |
|  |  |  | *struct\_field\_name\_*, |
|  |  |  | *sub\_descr\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (json\_field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = (sizeof(json\_field\_name\_) - 1), \

.type = [JSON\_TOK\_OBJECT\_START](#gga18a137ac5e2998d375540298670797c4a81e303d23da0b3d8504cc4a7ee7d52e8), \

.offset = offsetof(struct\_, struct\_field\_name\_), \

{ \

.object = { \

.sub\_descr = sub\_descr\_, \

.sub\_descr\_len = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(sub\_descr\_), \

}, \

}, \

}

Variant of JSON\_OBJ\_DESCR\_OBJECT that can be used when the structure and JSON field names differ.

This is useful when the JSON field is not a valid C identifier.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | json\_field\_name\_ | String, field name in JSON strings |
    | struct\_field\_name\_ | Field name in the struct |
    | sub\_descr\_ | Array of [json\_obj\_descr](structjson__obj__descr.md) describing the subobject |

See also
:   [JSON\_OBJ\_DESCR\_OBJECT](#ga4ee365f43cfa86a214973defe81f1e88)

## [◆ ](#ga1ed917f5a247ca33f2778afe62ff1a88)JSON\_OBJ\_DESCR\_PRIM

| #define JSON\_OBJ\_DESCR\_PRIM | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *field\_name\_*, |
|  |  |  | *type\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (#field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(#field\_name\_) - 1, \

.type = type\_, \

.offset = offsetof(struct\_, field\_name\_), \

}

Helper macro to declare a descriptor for supported primitive values.

Parameters
:   | struct\_ | Struct packing the values |
    | --- | --- |
    | field\_name\_ | Field name in the struct |
    | type\_ | Token type for JSON value corresponding to a primitive type. Must be one of: JSON\_TOK\_STRING for strings, JSON\_TOK\_NUMBER for numbers, JSON\_TOK\_TRUE (or JSON\_TOK\_FALSE) for booleans. |

Here's an example of use:

```
struct foo {
    int32_t some_int;
};

struct json_obj_descr foo[] = {
    JSON_OBJ_DESCR_PRIM(struct foo, some_int, JSON_TOK_NUMBER),
};
```

## [◆ ](#gaad081c4f8debcb41779bd5879ed8bbd4)JSON\_OBJ\_DESCR\_PRIM\_NAMED

| #define JSON\_OBJ\_DESCR\_PRIM\_NAMED | ( |  | *struct\_*, |
| --- | --- | --- | --- |
|  |  |  | *json\_field\_name\_*, |
|  |  |  | *struct\_field\_name\_*, |
|  |  |  | *type\_* ) |

`#include <[json.h](json_8h.md)>`

**Value:**

{ \

.field\_name = (json\_field\_name\_), \

.align\_shift = Z\_ALIGN\_SHIFT(struct\_), \

.field\_name\_len = sizeof(json\_field\_name\_) - 1, \

.type = type\_, \

.offset = offsetof(struct\_, struct\_field\_name\_), \

}

Variant of JSON\_OBJ\_DESCR\_PRIM that can be used when the structure and JSON field names differ.

This is useful when the JSON field is not a valid C identifier.

Parameters
:   | struct\_ | Struct packing the values. |
    | --- | --- |
    | json\_field\_name\_ | String, field name in JSON strings |
    | struct\_field\_name\_ | Field name in the struct |
    | type\_ | Token type for JSON value corresponding to a primitive type. |

See also
:   [JSON\_OBJ\_DESCR\_PRIM](#ga1ed917f5a247ca33f2778afe62ff1a88)

## Typedef Documentation

## [◆ ](#gacb409ebe9c59789a5d9aca02c6c94674)json\_append\_bytes\_t

| typedef int(\* json\_append\_bytes\_t) (const char \*bytes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*data) |
| --- |

`#include <[json.h](json_8h.md)>`

Function pointer type to append bytes to a buffer while encoding JSON data.

Parameters
:   | bytes | Contents to write to the output |
    | --- | --- |
    | len | Number of bytes to append to output |
    | data | User-provided pointer |

Returns
:   This callback function should return a negative number on error (which will be propagated to the return value of [json\_obj\_encode()](#gafec772f687a0280f5211139bd019e582)), or 0 on success.

## Enumeration Type Documentation

## [◆ ](#ga18a137ac5e2998d375540298670797c4)json\_tokens

| enum [json\_tokens](#ga18a137ac5e2998d375540298670797c4) |
| --- |

`#include <[json.h](json_8h.md)>`

| Enumerator | |
| --- | --- |
| JSON\_TOK\_NONE |  |
| JSON\_TOK\_OBJECT\_START |  |
| JSON\_TOK\_OBJECT\_END |  |
| JSON\_TOK\_LIST\_START |  |
| JSON\_TOK\_ARRAY\_START |  |
| JSON\_TOK\_LIST\_END |  |
| JSON\_TOK\_ARRAY\_END |  |
| JSON\_TOK\_STRING |  |
| JSON\_TOK\_COLON |  |
| JSON\_TOK\_COMMA |  |
| JSON\_TOK\_NUMBER |  |
| JSON\_TOK\_FLOAT |  |
| JSON\_TOK\_OPAQUE |  |
| JSON\_TOK\_OBJ\_ARRAY |  |
| JSON\_TOK\_TRUE |  |
| JSON\_TOK\_FALSE |  |
| JSON\_TOK\_NULL |  |
| JSON\_TOK\_ERROR |  |
| JSON\_TOK\_EOF |  |

## Function Documentation

## [◆ ](#ga4ffccdc602ab98d489499bf6fa4fa6c5)json\_arr\_encode()

| int json\_arr\_encode | ( | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
| --- | --- | --- | --- |
|  |  | const void \* | *val*, |
|  |  | [json\_append\_bytes\_t](#gacb409ebe9c59789a5d9aca02c6c94674) | *append\_bytes*, |
|  |  | void \* | *data* ) |

`#include <[json.h](json_8h.md)>`

Encodes an array using an arbitrary writer function.

Parameters
:   | descr | Pointer to the descriptor array |
    | --- | --- |
    | val | Struct holding the values |
    | append\_bytes | Function to append bytes to the output |
    | data | Data pointer to be passed to the append\_bytes callback function. |

Returns
:   0 if object has been successfully encoded. A negative value indicates an error.

## [◆ ](#gafd27bbcb898dc902cf1dadd3369cf923)json\_arr\_encode\_buf()

| int json\_arr\_encode\_buf | ( | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
| --- | --- | --- | --- |
|  |  | const void \* | *val*, |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_size* ) |

`#include <[json.h](json_8h.md)>`

Encodes an array in a contiguous memory location.

Parameters
:   | descr | Pointer to the descriptor array |
    | --- | --- |
    | val | Struct holding the values |
    | buffer | Buffer to store the JSON data |
    | buf\_size | Size of buffer, in bytes, with space for the terminating NUL character |

Returns
:   0 if object has been successfully encoded. A negative value indicates an error (as defined on [errno.h](errno_8h.md "System error numbers.")).

## [◆ ](#gab4e6ad4a040c271d74eaa313c580a739)json\_arr\_parse()

| int json\_arr\_parse | ( | char \* | *json*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
|  |  | void \* | *val* ) |

`#include <[json.h](json_8h.md)>`

Parses the JSON-encoded array pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*.

Values are stored in a struct pointed to by *val*. Set up the descriptor like this:

struct s { [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) foo; char \*bar; } struct [json\_obj\_descr](structjson__obj__descr.md) descr[] = { [JSON\_OBJ\_DESCR\_PRIM(struct s, foo, JSON\_TOK\_NUMBER)](#ga1ed917f5a247ca33f2778afe62ff1a88), [JSON\_OBJ\_DESCR\_PRIM(struct s, bar, JSON\_TOK\_STRING)](#ga1ed917f5a247ca33f2778afe62ff1a88), }; struct a { struct s baz[10]; size\_t count; } struct [json\_obj\_descr](structjson__obj__descr.md) array[] = { [JSON\_OBJ\_DESCR\_OBJ\_ARRAY(struct a, baz, 10, count,
descr, ARRAY\_SIZE(descr))](#gae012264df03546a1c01eec4216b52ffd), };

Since this parser is designed for machine-to-machine communications, some liberties were taken to simplify the design: (1) strings are not unescaped (but only valid escape sequences are accepted); (2) no UTF-8 validation is performed; and (3) only integer numbers are supported (no strtod() in the minimal libc).

Parameters
:   | [JSON](group__json.md) | Pointer to JSON-encoded array to be parsed |
    | --- | --- |
    | len | Length of JSON-encoded array |
    | descr | Pointer to the descriptor array |
    | val | Pointer to the struct to hold the decoded values |

Returns
:   0 if array has been successfully parsed. A negative value indicates an error (as defined on [errno.h](errno_8h.md "System error numbers.")).

## [◆ ](#ga6196411958e2e9b3683af4c281214b92)json\_arr\_separate\_object\_parse\_init()

| int json\_arr\_separate\_object\_parse\_init | ( | struct [json\_obj](structjson__obj.md) \* | *json*, |
| --- | --- | --- | --- |
|  |  | char \* | *payload*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[json.h](json_8h.md)>`

Initialize single-object array parsing.

JSON-encoded array data is going to be parsed one object at a time. Data is provided by *payload* with the size of *len* bytes.

Function validate that Json Array start is detected and initialize *json* object for Json object parsing separately.

Parameters
:   | [JSON](group__json.md) | Provide storage for parser states. To be used when parsing the array. |
    | --- | --- |
    | payload | Pointer to JSON-encoded array to be parsed |
    | len | Length of JSON-encoded array |

Returns
:   0 if array start is detected and initialization is successful or negative error code in case of failure.

## [◆ ](#ga64859a835e7cb88c2499360fb00ca344)json\_arr\_separate\_parse\_object()

| int json\_arr\_separate\_parse\_object | ( | struct [json\_obj](structjson__obj.md) \* | *json*, |
| --- | --- | --- | --- |
|  |  | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *descr\_len*, |
|  |  | void \* | *val* ) |

`#include <[json.h](json_8h.md)>`

Parse a single object from array.

Parses the JSON-encoded object pointed to by *json* object array, with size *len*, according to the descriptor pointed to by *descr*.

Parameters
:   | [JSON](group__json.md) | Pointer to JSON-object message state |
    | --- | --- |
    | descr | Pointer to the descriptor array |
    | descr\_len | Number of elements in the descriptor array. Must be less than 31. |
    | val | Pointer to the struct to hold the decoded values |

Returns
:   < 0 if error, 0 for end of message, bitmap of decoded fields on success (bit 0 is set if first field in the descriptor has been properly decoded, etc).

## [◆ ](#gad612b8441a21dca34cfeec6257877509)json\_calc\_encoded\_arr\_len()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) json\_calc\_encoded\_arr\_len | ( | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
| --- | --- | --- | --- |
|  |  | const void \* | *val* ) |

`#include <[json.h](json_8h.md)>`

Calculates the string length to fully encode an array.

Parameters
:   | descr | Pointer to the descriptor array |
    | --- | --- |
    | val | Struct holding the values |

Returns
:   Number of bytes necessary to encode the values if >0, an error code is returned.

## [◆ ](#ga41e6e90beef8bae12fca1de2584145bb)json\_calc\_encoded\_len()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) json\_calc\_encoded\_len | ( | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *descr\_len*, |
|  |  | const void \* | *val* ) |

`#include <[json.h](json_8h.md)>`

Calculates the string length to fully encode an object.

Parameters
:   | descr | Pointer to the descriptor array |
    | --- | --- |
    | descr\_len | Number of elements in the descriptor array |
    | val | Struct holding the values |

Returns
:   Number of bytes necessary to encode the values if >0, an error code is returned.

## [◆ ](#ga5ef155a3a6444801592badd6a092734c)json\_calc\_escaped\_len()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) json\_calc\_escaped\_len | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[json.h](json_8h.md)>`

Calculates the JSON-escaped string length.

Parameters
:   | str | The string to analyze |
    | --- | --- |
    | len | String size |

Returns
:   The length str would have if it were escaped

## [◆ ](#ga43ee6d1fbd3fa8fb2ae052844b465dda)json\_escape()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) json\_escape | ( | char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *len*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_size* ) |

`#include <[json.h](json_8h.md)>`

Escapes the string so it can be used to encode JSON objects.

Parameters
:   | str | The string to escape; the escape string is stored the buffer pointed to by this parameter |
    | --- | --- |
    | len | Points to a size\_t containing the size before and after the escaping process |
    | buf\_size | The size of buffer str points to |

Returns
:   0 if string has been escaped properly, or -ENOMEM if there was not enough space to escape the buffer

## [◆ ](#gafec772f687a0280f5211139bd019e582)json\_obj\_encode()

| int json\_obj\_encode | ( | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *descr\_len*, |
|  |  | const void \* | *val*, |
|  |  | [json\_append\_bytes\_t](#gacb409ebe9c59789a5d9aca02c6c94674) | *append\_bytes*, |
|  |  | void \* | *data* ) |

`#include <[json.h](json_8h.md)>`

Encodes an object using an arbitrary writer function.

Parameters
:   | descr | Pointer to the descriptor array |
    | --- | --- |
    | descr\_len | Number of elements in the descriptor array |
    | val | Struct holding the values |
    | append\_bytes | Function to append bytes to the output |
    | data | Data pointer to be passed to the append\_bytes callback function. |

Returns
:   0 if object has been successfully encoded. A negative value indicates an error.

## [◆ ](#gab758ad32cfb6369f4967a6842ac63245)json\_obj\_encode\_buf()

| int json\_obj\_encode\_buf | ( | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *descr\_len*, |
|  |  | const void \* | *val*, |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_size* ) |

`#include <[json.h](json_8h.md)>`

Encodes an object in a contiguous memory location.

Parameters
:   | descr | Pointer to the descriptor array |
    | --- | --- |
    | descr\_len | Number of elements in the descriptor array |
    | val | Struct holding the values |
    | buffer | Buffer to store the JSON data |
    | buf\_size | Size of buffer, in bytes, with space for the terminating NUL character |

Returns
:   0 if object has been successfully encoded. A negative value indicates an error (as defined on [errno.h](errno_8h.md "System error numbers.")).

## [◆ ](#ga73997fa2154fcbc80f37edd7bcf3477a)json\_obj\_parse()

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) json\_obj\_parse | ( | char \* | *json*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | const struct [json\_obj\_descr](structjson__obj__descr.md) \* | *descr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *descr\_len*, |
|  |  | void \* | *val* ) |

`#include <[json.h](json_8h.md)>`

Parses the JSON-encoded object pointed to by *json*, with size *len*, according to the descriptor pointed to by *descr*.

Values are stored in a struct pointed to by *val*. Set up the descriptor like this:

struct s { [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) foo; char \*bar; } struct [json\_obj\_descr](structjson__obj__descr.md) descr[] = { [JSON\_OBJ\_DESCR\_PRIM(struct s, foo, JSON\_TOK\_NUMBER)](#ga1ed917f5a247ca33f2778afe62ff1a88), [JSON\_OBJ\_DESCR\_PRIM(struct s, bar, JSON\_TOK\_STRING)](#ga1ed917f5a247ca33f2778afe62ff1a88), };

Since this parser is designed for machine-to-machine communications, some liberties were taken to simplify the design: (1) strings are not unescaped (but only valid escape sequences are accepted); (2) no UTF-8 validation is performed; and (3) only integer numbers are supported (no strtod() in the minimal libc).

Parameters
:   | [JSON](group__json.md) | Pointer to JSON-encoded value to be parsed |
    | --- | --- |
    | len | Length of JSON-encoded value |
    | descr | Pointer to the descriptor array |
    | descr\_len | Number of elements in the descriptor array. Must be less than 63 due to implementation detail reasons (if more fields are necessary, use two descriptors) |
    | val | Pointer to the struct to hold the decoded values |

Returns
:   < 0 if error, bitmap of decoded fields on success (bit 0 is set if first field in the descriptor has been properly decoded, etc).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
