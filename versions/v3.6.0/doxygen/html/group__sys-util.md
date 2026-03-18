---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__sys-util.html
original_path: doxygen/html/group__sys-util.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Utility Functions

[Utilities](group__utilities.md)

| Macros | |
| --- | --- |
| #define | [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(x) |
|  | Cast `x`, a pointer, to an unsigned integer. |
| #define | [UINT\_TO\_POINTER](#gab74ce0513c348e0b257d38473e77e1a1)(x) |
|  | Cast `x`, an unsigned integer, to a void\*. |
| #define | [POINTER\_TO\_INT](#ga6e5ec9c46d0140315a7c1d80d1cc3c38)(x) |
|  | Cast `x`, a pointer, to a signed integer. |
| #define | [INT\_TO\_POINTER](#gae236ed18fe2ff18ab47c15d2e7eeb417)(x) |
|  | Cast `x`, a signed integer, to a void\*. |
| #define | [BITS\_PER\_LONG](#ga2f660aa23a5dbc0f4b8df48b4302b8c3)   (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_\_) |
|  | Number of bits in a long int. |
| #define | [BITS\_PER\_LONG\_LONG](#gaeb3fa0f8ac477da6575363a158f36891)   (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_LONG\_\_) |
|  | Number of bits in a long long int. |
| #define | [GENMASK](#ga58530d20924859d16358c7400c37738d)(h, l) |
|  | Create a contiguous bitmask starting at bit position `l` and ending at position `h`. |
| #define | [GENMASK64](#gab631f8a0ecb6fde5b22df40607868f04)(h, l) |
|  | Create a contiguous 64-bit bitmask starting at bit position `l` and ending at position `h`. |
| #define | [LSB\_GET](#ga92235ab2e350fbdc01ddf0f894e5e4c0)(value) |
|  | Extract the Least Significant Bit from `value`. |
| #define | [FIELD\_GET](#gaa49a456f06f7bdbedfcf3517e461947e)(mask, value) |
|  | Extract a bitfield element from `value` corresponding to the field mask `mask`. |
| #define | [FIELD\_PREP](#gaa03c8b31bf67a097dd9f8153a04ef86b)(mask, value) |
|  | Prepare a bitfield element using `value` with `mask` representing its field position and width. |
| #define | [ZERO\_OR\_COMPILE\_ERROR](#ga831cb8468911b8ebdb9b42682778e53d)(cond) |
|  | 0 if `cond` is true-ish; causes a compile error otherwise. |
| #define | [IS\_ARRAY](#gaa0be479debd8300ab6b43f4d028ab5da)(array) |
|  | Zero if `array` has an array type, a compile error otherwise. |
| #define | [ARRAY\_SIZE](#ga70c57aae3eb654e205459b4362c8089a)(array) |
|  | Number of elements in the given `array`. |
| #define | [IS\_ARRAY\_ELEMENT](#gad403257ac6868c8bf3415ae771ce0a04)(array, ptr) |
|  | Whether `ptr` is an element of `array`. |
| #define | [ARRAY\_INDEX](#ga27c31909224761e41d77118b41212d6b)(array, ptr) |
|  | Index of `ptr` within `array`. |
| #define | [PART\_OF\_ARRAY](#ga4fbecf59c021cb60fa1267b7818f90ef)(array, ptr) |
|  | Check if a pointer `ptr` lies within `array`. |
| #define | [ARRAY\_INDEX\_FLOOR](#gae0516bf7a39795bcc6f0dfbf3a180c05)(array, ptr) |
|  | Array-index of `ptr` within `array`, rounded down. |
| #define | [ARRAY\_FOR\_EACH](#ga7a1647a1d17185f9438ed0e3096e68bc)(array, idx) |
|  | Iterate over members of an array using an index variable. |
| #define | [ARRAY\_FOR\_EACH\_PTR](#gafd9d42bbb945424f11b7b023dfd519f9)(array, ptr) |
|  | Iterate over members of an array using a pointer. |
| #define | [SAME\_TYPE](#ga78e587047fe4af679141595363c07179)(a, b) |
|  | Validate if two entities have a compatible type. |
| #define | [CONTAINER\_OF\_VALIDATE](#gaf2279c11f90f7461a417f9646af7dc5c)(ptr, type, field) |
|  | Validate CONTAINER\_OF parameters, only applies to C mode. |
| #define | [CONTAINER\_OF](#gac5bc561d1bfd1bf68877fe577779bd2f)(ptr, type, field) |
|  | Get a pointer to a structure containing the element. |
| #define | [CONCAT](#ga770b921e59b3151931ee939a1ecf450e)(...) |
|  | Concatenate input arguments. |
| #define | [ROUND\_UP](#gaada5610108b15d85c65d863b0c646ef3)(x, align) |
|  | Value of `x` rounded up to the next multiple of `align`. |
| #define | [ROUND\_DOWN](#gad8d2389dbe7ea135eccf237dbafb76dd)(x, align) |
|  | Value of `x` rounded down to the previous multiple of `align`. |
| #define | [WB\_UP](#ga8b16b3a76faa15ea544e4b0edb3e62c7)(x) |
|  | Value of `x` rounded up to the next word boundary. |
| #define | [WB\_DN](#gadbc789ee99633a92584387ba2a4f7052)(x) |
|  | Value of `x` rounded down to the previous word boundary. |
| #define | [DIV\_ROUND\_UP](#gae664e7492e37d324831caf2321ddda37)(n, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Divide and round up. |
| #define | [DIV\_ROUND\_CLOSEST](#ga57fc13eb777500b3e22d3ff457cfd0d7)(n, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Divide and round to the nearest integer. |
| #define | [ceiling\_fraction](#gaad408461e7ab356650bcd5c83bc0ed39)(numerator, divider) |
|  | Ceiling function applied to `numerator` / `divider` as a fraction. |
| #define | [MAX](#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(a, b) |
|  | Obtain the maximum of two values. |
| #define | [MIN](#ga3acffbd305ee72dcd4593c0d8af64a4f)(a, b) |
|  | Obtain the minimum of two values. |
| #define | [CLAMP](#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(val, low, high) |
|  | Clamp a value to a given range. |
| #define | [IN\_RANGE](#gaea00fb0c11b73f77da8884374e2121b4)(val, min, max) |
|  | Checks if a value is within range. |
| #define | [LOG2](#ga40805b5dd56ee36df59a7bbe403ddf33)(x) |
|  | Compute log2(x). |
| #define | [LOG2CEIL](#gada629edfcec9fa2fc3dc5d7af70abb03)(x) |
|  | Compute ceil(log2(x)). |
| #define | [NHPOT](#ga2ab444fed50a82cc1fe0e952fd03127d)(x) |
|  | Compute next highest power of two. |
| #define | [KB](#ga5c723c0cc71b83224ead557db3ab74dd)(x) |
|  | Number of bytes in `x` kibibytes. |
| #define | [MB](#ga44d2b171cc92225ec0a76ef70fc9b531)(x) |
|  | Number of bytes in `x` mebibytes. |
| #define | [GB](#gaf207e8203eedc05adcf341a24bfa6cbb)(x) |
|  | Number of bytes in `x` gibibytes. |
| #define | [KHZ](#gaee55275295c076c6d23c994777623253)(x) |
|  | Number of Hz in `x` kHz. |
| #define | [MHZ](#gab7b18750ddf0850461f926ae151ca7fa)(x) |
|  | Number of Hz in `x` MHz. |
| #define | [WAIT\_FOR](#ga68eb35df6b4715714312df90209accee)(expr, timeout, delay\_stmt) |
|  | Wait for an expression to return true with a timeout. |
| #define | [BIT](#ga3a8ea58898cb58fc96013383d39f482c)(n) |
|  | Unsigned integer with bit position `n` set (signed in assembly language). |
| #define | [BIT64](#gacfdade52af3ced2d87472cec47d14a76)(\_n) |
|  | 64-bit unsigned integer with bit position `_n` set. |
| #define | [WRITE\_BIT](#ga23a900e882ecb48455e70f01fd45b246)(var, bit, set) |
|  | Set or clear a bit depending on a boolean value. |
| #define | [BIT\_MASK](#ga3c12c6d36ad0aa481a3436923d21f4f8)(n) |
|  | Bit mask with bits 0 through n-1 (inclusive) set, or 0 if `n` is 0. |
| #define | [BIT64\_MASK](#ga1a138896caafcb2429a6483ea7412d12)(n) |
|  | 64-bit bit mask with bits 0 through n-1 (inclusive) set, or 0 if `n` is 0. |
| #define | [IS\_POWER\_OF\_TWO](#ga52d277cbf33f76350b2fcb21c24640ee)(x) |
|  | Check if a `x` is a power of two. |
| #define | [IS\_SHIFTED\_BIT\_MASK](#ga406b5955c2803cdd9d9f19c90f242662)(m, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Check if bits are set continuously from the specified bit. |
| #define | [IS\_BIT\_MASK](#ga6d4b02e5da10bf93c4697dd6bf239ffd)(m) |
|  | Check if bits are set continuously from the LSB. |
| #define | [IS\_ENABLED](#ga111fe4e9d63758262fc6810a782cb32a)(config\_macro) |
|  | Check for macro definition in compiler-visible expressions. |
| #define | [COND\_CODE\_1](#ga358bc3e7669c860a98839a51cd526b20)(\_flag, \_if\_1\_code, \_else\_code) |
|  | Insert code depending on whether `_flag` expands to 1 or not. |
| #define | [COND\_CODE\_0](#ga5483ea38af79bc6c4509936288705377)(\_flag, \_if\_0\_code, \_else\_code) |
|  | Like [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20) except tests if `_flag` is 0. |
| #define | [IF\_ENABLED](#gae67ffe50e848951dbde309ed569ea925)(\_flag, \_code) |
|  | Insert code if `_flag` is defined and equals 1. |
| #define | [IF\_DISABLED](#gaa65e031f24a2c0fb4eae240e2c60b36a)(\_flag, \_code) |
|  | Insert code if `_flag` is not defined as 1. |
| #define | [IS\_EMPTY](#gab9487eea703d51cb1f235432dab4a1c7)(...) |
|  | Check if a macro has a replacement expression. |
| #define | [IS\_EQ](#gaa35a6894bca38a8ffb558c2c22a1eee1)(a, b) |
|  | Like a == b, but does evaluation and short-circuiting at C preprocessor time. |
| #define | [LIST\_DROP\_EMPTY](#gab9762d5128988f7f4f5d51213ea52025)(...) |
|  | Remove empty arguments from list. |
| #define | [EMPTY](#ga2b7cf2a3641be7b89138615764d60ba3) |
|  | Macro with an empty expansion. |
| #define | [IDENTITY](#gaaed493c6115c04272077a0f3854b9a83)(V) |
|  | Macro that expands to its argument. |
| #define | [GET\_ARG\_N](#gabbe04a4d59a495b2b86196304b937ec6)(N, ...) |
|  | Get nth argument from argument list. |
| #define | [GET\_ARGS\_LESS\_N](#ga01e1dc9b92e5be6895528d1da5f0c88b)(N, ...) |
|  | Strips n first arguments from the argument list. |
| #define | [UTIL\_OR](#ga50cfdf948906976562c3f0625c84c2b2)(a, b) |
|  | Like a || b, but does evaluation and short-circuiting at C preprocessor time. |
| #define | [UTIL\_AND](#ga26179b776b4a03143e8be1612ef6d853)(a, b) |
|  | Like a && b, but does evaluation and short-circuiting at C preprocessor time. |
| #define | [UTIL\_INC](#ga90a54212306c3e210ac87fd0bd7b32da)(x) |
|  | [UTIL\_INC(x)](#ga90a54212306c3e210ac87fd0bd7b32da) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x+1. |
| #define | [UTIL\_DEC](#gaa7623e1e33316024217094698e4d8258)(x) |
|  | [UTIL\_DEC(x)](#gaa7623e1e33316024217094698e4d8258) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x-1. |
| #define | [UTIL\_X2](#gab23deac75762adfb6bdde2c15d51f158)(y) |
|  | [UTIL\_X2(y)](#gab23deac75762adfb6bdde2c15d51f158) for an integer literal y from 0 to 4095 expands to an integer literal whose value is 2y. |
| #define | [LISTIFY](#ga81cbc0233cf73048d65b76f716653af6)(LEN, F, sep, ...) |
|  | Generates a sequence of code with configurable separator. |
| #define | [FOR\_EACH](#ga278c8b7cbbea2f585e371d3568f3cb12)(F, sep, ...) |
|  | Call a macro `F` on each provided argument with a given separator between each call. |
| #define | [FOR\_EACH\_NONEMPTY\_TERM](#ga24b3862161d725f5503b1bb08f4e339f)(F, term, ...) |
|  | Like [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12), but with a terminator instead of a separator, and drops empty elements from the argument list. |
| #define | [FOR\_EACH\_IDX](#ga069f709e18eeafb8d276b5ff4fc09d31)(F, sep, ...) |
|  | Call macro `F` on each provided argument, with the argument's index as an additional parameter. |
| #define | [FOR\_EACH\_FIXED\_ARG](#ga1a2b2aa21d7cc37f33e6a62abd2ae340)(F, sep, fixed\_arg, ...) |
|  | Call macro `F` on each provided argument, with an additional fixed argument as a parameter. |
| #define | [FOR\_EACH\_IDX\_FIXED\_ARG](#ga2ab7377f5493123ffd29ebd1286457a9)(F, sep, fixed\_arg, ...) |
|  | Calls macro `F` for each variable argument with an index and fixed argument. |
| #define | [REVERSE\_ARGS](#ga58de032c2ed7b4094c447c512dfd3784)(...) |
|  | Reverse arguments order. |
| #define | [NUM\_VA\_ARGS\_LESS\_1](#ga8a0e9835e0a8f864ffc2359b9c419cc2)(...) |
|  | Number of arguments in the variable arguments list minus one. |
| #define | [MACRO\_MAP\_CAT](#gaf82371bd6bf317add5276fc6cbd66662)(...) |
|  | Mapping macro that pastes results together. |
| #define | [MACRO\_MAP\_CAT\_N](#ga58eba1f911e21da46b8beea264934d55)(N, ...) |
|  | Mapping macro that pastes a fixed number of results together. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_power\_of\_two](#gadfe7046eb6c39bb3c84c18d8ac7a230e) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int x) |
|  | Is `x` a power of two? |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [arithmetic\_shift\_right](#ga1ffeb18b8ed73d37c2485c82988ed1ec) ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift) |
|  | Arithmetic shift right. |
| static void | [bytecpy](#ga3379c356de17dbeebfa7588d8c964d5e) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | byte by byte memcpy. |
| static void | [byteswp](#ga8624d1e5411703deac1ab8517f132d7b) (void \*a, void \*b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | byte by byte swap. |
| int | [char2hex](#gaaf91757f6fe86ab417536d5066ce14e6) (char c, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*x) |
|  | Convert a single character into a hexadecimal nibble. |
| int | [hex2char](#ga9ed3bd04d5c0797aebf333733913028c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x, char \*c) |
|  | Convert a single hexadecimal nibble into a character. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bin2hex](#gaf8f2ab98cc3f045ba834dbbb13a5dfd7) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen, char \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen) |
|  | Convert a binary array into string representation. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [hex2bin](#ga269a01ffa3f1a3485b79d8a54a78a3f1) (const char \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Convert a hexadecimal string into a binary array. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcd2bin](#gaa0f77b877eb5db5a228b79cba110abe4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bcd) |
|  | Convert a binary coded decimal (BCD 8421) value to binary. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bin2bcd](#ga6dff7f443aa795258c64cee63b29b591) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bin) |
|  | Convert a binary value to binary coded decimal (BCD 8421). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [u8\_to\_dec](#gabd42323692821c970e1038879f8f2f33) (char \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buflen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Convert a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) into a decimal string representation. |
| char \* | [utf8\_trunc](#ga1bbcfa5d7bfe757afab489d2ce41e30a) (char \*utf8\_str) |
|  | Properly truncate a NULL-terminated UTF-8 string. |
| char \* | [utf8\_lcpy](#ga376935d7e6eece7dbdd382de057ec2f9) (char \*dst, const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | Copies a UTF-8 encoded string from `src` to `dst`. |
| static void | [mem\_xor\_n](#ga8a9d63740a8718de8ab0ce057cfbd4f4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src2, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | XOR n bytes. |
| static void | [mem\_xor\_32](#ga6f1717e3eeb4a91afa2be14061d52203) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[4]) |
|  | XOR 32 bits. |
| static void | [mem\_xor\_128](#ga64037dd6934130ca6a6dc3e5357b9743) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[16]) |
|  | XOR 128 bits. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga7a1647a1d17185f9438ed0e3096e68bc)ARRAY\_FOR\_EACH

| #define ARRAY\_FOR\_EACH | ( |  | *array*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

for (size\_t idx = 0; (idx) < [ARRAY\_SIZE](#ga70c57aae3eb654e205459b4362c8089a)(array); ++(idx))

[ARRAY\_SIZE](#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:124

Iterate over members of an array using an index variable.

Parameters
:   | array | the array in question |
    | --- | --- |
    | idx | name of array index variable |

## [◆ ](#gafd9d42bbb945424f11b7b023dfd519f9)ARRAY\_FOR\_EACH\_PTR

| #define ARRAY\_FOR\_EACH\_PTR | ( |  | *array*, |
| --- | --- | --- | --- |
|  |  |  | *ptr* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

for (\_\_typeof\_\_(\*(array)) \*ptr = (array); ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9))((ptr) - (array)) < [ARRAY\_SIZE](#ga70c57aae3eb654e205459b4362c8089a)(array); \

++(ptr))

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

Iterate over members of an array using a pointer.

Parameters
:   | array | the array in question |
    | --- | --- |
    | ptr | pointer to an element of `array` |

## [◆ ](#ga27c31909224761e41d77118b41212d6b)ARRAY\_INDEX

| #define ARRAY\_INDEX | ( |  | *array*, |
| --- | --- | --- | --- |
|  |  |  | *ptr* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

({ \

\_\_ASSERT\_NO\_MSG([IS\_ARRAY\_ELEMENT](#gad403257ac6868c8bf3415ae771ce0a04)(array, ptr)); \

(\_\_typeof\_\_((array)[0]) \*)(ptr) - (array); \

})

[IS\_ARRAY\_ELEMENT](#gad403257ac6868c8bf3415ae771ce0a04)

#define IS\_ARRAY\_ELEMENT(array, ptr)

Whether ptr is an element of array.

**Definition** util.h:143

Index of `ptr` within `array`.

With CONFIG\_ASSERT=y, this macro will trigger a runtime assertion when `ptr` does not fall into the range of `array` or when `ptr` is not aligned to an array-element boundary of `array`.

In C, passing a pointer as `array` causes a compile error.

Parameters
:   | array | the array in question |
    | --- | --- |
    | ptr | pointer to an element of `array` |

Returns
:   the array index of `ptr` within `array`, on success

## [◆ ](#gae0516bf7a39795bcc6f0dfbf3a180c05)ARRAY\_INDEX\_FLOOR

| #define ARRAY\_INDEX\_FLOOR | ( |  | *array*, |
| --- | --- | --- | --- |
|  |  |  | *ptr* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

({ \

\_\_ASSERT\_NO\_MSG([PART\_OF\_ARRAY](#ga4fbecf59c021cb60fa1267b7818f90ef)(array, ptr)); \

([POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(ptr) - [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(array)) / sizeof((array)[0]); \

})

[PART\_OF\_ARRAY](#ga4fbecf59c021cb60fa1267b7818f90ef)

#define PART\_OF\_ARRAY(array, ptr)

Check if a pointer ptr lies within array.

**Definition** util.h:178

[POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)

#define POINTER\_TO\_UINT(x)

Cast x, a pointer, to an unsigned integer.

**Definition** util.h:45

Array-index of `ptr` within `array`, rounded down.

This macro behaves much like [ARRAY\_INDEX](#ga27c31909224761e41d77118b41212d6b) with the notable difference that it accepts any `ptr` in the range of `array` rather than exclusively a `ptr` aligned to an array-element boundary of `array`.

With CONFIG\_ASSERT=y, this macro will trigger a runtime assertion when `ptr` does not fall into the range of `array`.

In C, passing a pointer as `array` causes a compile error.

Parameters
:   | array | the array in question |
    | --- | --- |
    | ptr | pointer to an element of `array` |

Returns
:   the array index of `ptr` within `array`, on success

## [◆ ](#ga70c57aae3eb654e205459b4362c8089a)ARRAY\_SIZE

| #define ARRAY\_SIZE | ( |  | *array* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

(([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)) ([IS\_ARRAY](#gaa0be479debd8300ab6b43f4d028ab5da)(array) + (sizeof(array) / sizeof((array)[0]))))

[IS\_ARRAY](#gaa0be479debd8300ab6b43f4d028ab5da)

#define IS\_ARRAY(array)

Zero if array has an array type, a compile error otherwise.

**Definition** util.h:110

Number of elements in the given `array`.

In C++, due to language limitations, this will accept as `array` any type that implements operator[]. The results may not be particularly meaningful in this case.

In C, passing a pointer as `array` causes a compile error.

## [◆ ](#ga3a8ea58898cb58fc96013383d39f482c)BIT

| #define BIT | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

(1UL << (n))

Unsigned integer with bit position `n` set (signed in assembly language).

## [◆ ](#gacfdade52af3ced2d87472cec47d14a76)BIT64

| #define BIT64 | ( |  | *\_n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

(1ULL << (\_n))

64-bit unsigned integer with bit position `_n` set.

## [◆ ](#ga1a138896caafcb2429a6483ea7412d12)BIT64\_MASK

| #define BIT64\_MASK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

([BIT64](#gacfdade52af3ced2d87472cec47d14a76)(n) - 1ULL)

[BIT64](#gacfdade52af3ced2d87472cec47d14a76)

#define BIT64(\_n)

64-bit unsigned integer with bit position \_n set.

**Definition** util\_macro.h:49

64-bit bit mask with bits 0 through n-1 (inclusive) set, or 0 if `n` is 0.

## [◆ ](#ga3c12c6d36ad0aa481a3436923d21f4f8)BIT\_MASK

| #define BIT\_MASK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

([BIT](#ga3a8ea58898cb58fc96013383d39f482c)(n) - 1UL)

[BIT](#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if `n` is 0.

## [◆ ](#ga2f660aa23a5dbc0f4b8df48b4302b8c3)BITS\_PER\_LONG

| #define BITS\_PER\_LONG   (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_\_) |
| --- |

`#include <[util.h](util_8h.md)>`

Number of bits in a long int.

## [◆ ](#gaeb3fa0f8ac477da6575363a158f36891)BITS\_PER\_LONG\_LONG

| #define BITS\_PER\_LONG\_LONG   (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_LONG\_\_) |
| --- |

`#include <[util.h](util_8h.md)>`

Number of bits in a long long int.

## [◆ ](#gaad408461e7ab356650bcd5c83bc0ed39)ceiling\_fraction

| #define ceiling\_fraction | ( |  | *numerator*, |
| --- | --- | --- | --- |
|  |  |  | *divider* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

\_\_DEPRECATED\_MACRO \

DIV\_ROUND\_UP(numerator, divider)

Ceiling function applied to `numerator` / `divider` as a fraction.

**[Deprecated](deprecated.md#_deprecated000069)**
:   Use [DIV\_ROUND\_UP()](#gae664e7492e37d324831caf2321ddda37) instead.

## [◆ ](#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)CLAMP

| #define CLAMP | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *low*, |
|  |  |  | *high* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((val) <= (low)) ? (low) : [MIN](#ga3acffbd305ee72dcd4593c0d8af64a4f)(val, high))

[MIN](#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:373

Clamp a value to a given range.

Note
:   Arguments are evaluated multiple times. Use Z\_CLAMP for a GCC-only, single evaluation version.

Parameters
:   | val | Value to be clamped. |
    | --- | --- |
    | low | Lowest allowed value (inclusive). |
    | high | Highest allowed value (inclusive). |

Returns
:   Clamped value.

## [◆ ](#ga770b921e59b3151931ee939a1ecf450e)CONCAT

| #define CONCAT | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(\_CONCAT\_, [NUM\_VA\_ARGS\_LESS\_1](#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_))(\_\_VA\_ARGS\_\_)

[NUM\_VA\_ARGS\_LESS\_1](#ga8a0e9835e0a8f864ffc2359b9c419cc2)

#define NUM\_VA\_ARGS\_LESS\_1(...)

Number of arguments in the variable arguments list minus one.

**Definition** util\_macro.h:629

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Concatenate input arguments.

Concatenate provided tokens into a combined token during the preprocessor pass. This can be used to, for ex., build an identifier out of multiple parts, where one of those parts may be, for ex, a number, another macro, or a macro argument.

Parameters
:   | ... | Tokens to concatencate |
    | --- | --- |

Returns
:   Concatenated token.

## [◆ ](#ga5483ea38af79bc6c4509936288705377)COND\_CODE\_0

| #define COND\_CODE\_0 | ( |  | *\_flag*, |
| --- | --- | --- | --- |
|  |  |  | *\_if\_0\_code*, |
|  |  |  | *\_else\_code* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code)

Like [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20) except tests if `_flag` is 0.

This is like [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20), except that it tests whether `_flag` expands to the integer literal 0. It expands to `_if_0_code` if so, and `_else_code` otherwise; both of these must be enclosed in parentheses.

Parameters
:   | \_flag | evaluated flag |
    | --- | --- |
    | \_if\_0\_code | result if `_flag` expands to 0; must be in parentheses |
    | \_else\_code | result otherwise; must be in parentheses |

See also
:   [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20)

## [◆ ](#ga358bc3e7669c860a98839a51cd526b20)COND\_CODE\_1

| #define COND\_CODE\_1 | ( |  | *\_flag*, |
| --- | --- | --- | --- |
|  |  |  | *\_if\_1\_code*, |
|  |  |  | *\_else\_code* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether `_flag` expands to 1 or not.

This relies on similar tricks as [IS\_ENABLED()](#ga111fe4e9d63758262fc6810a782cb32a), but as the result of `_flag` expansion, results in either `_if_1_code` or `_else_code` is expanded.

To prevent the preprocessor from treating commas as argument separators, the `_if_1_code` and `_else_code` expressions must be inside brackets/parentheses: (). These are stripped away during macro expansion.

Example:

```
COND_CODE_1(CONFIG_FLAG, (uint32_t x;), (there_is_no_flag();))
```

If `CONFIG_FLAG` is defined to 1, this expands to:

```
uint32_t x;
```

It expands to there\_is\_no\_flag(); otherwise.

This could be used as an alternative to:

```
#if defined(CONFIG_FLAG) && (CONFIG_FLAG == 1)
#define MAYBE_DECLARE(x) uint32_t x
#else
#define MAYBE_DECLARE(x) there_is_no_flag()
#endif

MAYBE_DECLARE(x);
```

However, the advantage of [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20) is that code is resolved in place where it is used, while the `#if` method defines `MAYBE_DECLARE` on two lines and requires it to be invoked again on a separate line. This makes [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20) more concise and also sometimes more useful when used within another macro's expansion.

Note
:   `_flag` can be the result of preprocessor expansion, e.g. an expression involving [NUM\_VA\_ARGS\_LESS\_1(...)](#ga8a0e9835e0a8f864ffc2359b9c419cc2). However, `_if_1_code` is only expanded if `_flag` expands to the integer literal 1. Integer expressions that evaluate to 1, e.g. after doing some arithmetic, will not work.

Parameters
:   | \_flag | evaluated flag |
    | --- | --- |
    | \_if\_1\_code | result if `_flag` expands to 1; must be in parentheses |
    | \_else\_code | result otherwise; must be in parentheses |

## [◆ ](#gac5bc561d1bfd1bf68877fe577779bd2f)CONTAINER\_OF

| #define CONTAINER\_OF | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *field* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

({ \

CONTAINER\_OF\_VALIDATE(ptr, type, field) \

((type \*)(((char \*)(ptr)) - offsetof(type, field))); \

})

Get a pointer to a structure containing the element.

Example:

```
 struct foo {
    int bar;
 };

 struct foo my_foo;
 int *ptr = &my_foo.bar;

 struct foo *container = CONTAINER_OF(ptr, struct foo, bar);
```

Above, `container` points at `my_foo`.

Parameters
:   | ptr | pointer to a structure element |
    | --- | --- |
    | type | name of the type that `ptr` is an element of |
    | field | the name of the field within the struct `ptr` points to |

Returns
:   a pointer to the structure that contains `ptr`

## [◆ ](#gaf2279c11f90f7461a417f9646af7dc5c)CONTAINER\_OF\_VALIDATE

| #define CONTAINER\_OF\_VALIDATE | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *field* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

BUILD\_ASSERT([SAME\_TYPE](#ga78e587047fe4af679141595363c07179)(\*(ptr), ((type \*)0)->field) || \

[SAME\_TYPE](#ga78e587047fe4af679141595363c07179)(\*(ptr), void), \

"pointer type mismatch in CONTAINER\_OF");

[SAME\_TYPE](#ga78e587047fe4af679141595363c07179)

#define SAME\_TYPE(a, b)

Validate if two entities have a compatible type.

**Definition** util.h:230

Validate CONTAINER\_OF parameters, only applies to C mode.

## [◆ ](#ga57fc13eb777500b3e22d3ff457cfd0d7)DIV\_ROUND\_CLOSEST

| #define DIV\_ROUND\_CLOSEST | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

((((n) < 0) ^ (([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) < 0)) ? ((n) - (([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) / 2)) / ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) : \

((n) + (([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) / 2)) / ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)))

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

Divide and round to the nearest integer.

Example:

[DIV\_ROUND\_CLOSEST](#ga57fc13eb777500b3e22d3ff457cfd0d7)(5, 2); // 3

[DIV\_ROUND\_CLOSEST](#ga57fc13eb777500b3e22d3ff457cfd0d7)(5, -2); // -3

[DIV\_ROUND\_CLOSEST](#ga57fc13eb777500b3e22d3ff457cfd0d7)(5, 3); // 2

[DIV\_ROUND\_CLOSEST](#ga57fc13eb777500b3e22d3ff457cfd0d7)

#define DIV\_ROUND\_CLOSEST(n, d)

Divide and round to the nearest integer.

**Definition** util.h:335

Parameters
:   | n | Numerator. |
    | --- | --- |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Denominator. |

Returns
:   The result of `n` / `d`, rounded to the nearest integer.

## [◆ ](#gae664e7492e37d324831caf2321ddda37)DIV\_ROUND\_UP

| #define DIV\_ROUND\_UP | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((n) + ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) - 1) / ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)))

Divide and round up.

Example:

[DIV\_ROUND\_UP](#gae664e7492e37d324831caf2321ddda37)(1, 2); // 1

[DIV\_ROUND\_UP](#gae664e7492e37d324831caf2321ddda37)(3, 2); // 2

[DIV\_ROUND\_UP](#gae664e7492e37d324831caf2321ddda37)

#define DIV\_ROUND\_UP(n, d)

Divide and round up.

**Definition** util.h:318

Parameters
:   | n | Numerator. |
    | --- | --- |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Denominator. |

Returns
:   The result of `n` / `d`, rounded up.

## [◆ ](#ga2b7cf2a3641be7b89138615764d60ba3)EMPTY

| #define EMPTY |
| --- |

`#include <[util_macro.h](util__macro_8h.md)>`

Macro with an empty expansion.

This trivial definition is provided for readability when a macro should expand to an empty result, which e.g. is sometimes needed to silence checkpatch.

Example:

```
 #define LIST_ITEM(n) , item##n
```

The above would cause checkpatch to complain, but:

```
 #define LIST_ITEM(n) EMPTY, item##n
```

would not.

## [◆ ](#gaa49a456f06f7bdbedfcf3517e461947e)FIELD\_GET

| #define FIELD\_GET | ( |  | *mask*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((value) & (mask)) / [LSB\_GET](#ga92235ab2e350fbdc01ddf0f894e5e4c0)(mask))

[LSB\_GET](#ga92235ab2e350fbdc01ddf0f894e5e4c0)

#define LSB\_GET(value)

Extract the Least Significant Bit from value.

**Definition** util.h:78

Extract a bitfield element from `value` corresponding to the field mask `mask`.

## [◆ ](#gaa03c8b31bf67a097dd9f8153a04ef86b)FIELD\_PREP

| #define FIELD\_PREP | ( |  | *mask*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((value) \* [LSB\_GET](#ga92235ab2e350fbdc01ddf0f894e5e4c0)(mask)) & (mask))

Prepare a bitfield element using `value` with `mask` representing its field position and width.

The result should be combined with other fields using a logical OR.

## [◆ ](#ga278c8b7cbbea2f585e371d3568f3cb12)FOR\_EACH

| #define FOR\_EACH | ( |  | *F*, |
| --- | --- | --- | --- |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_FOR\_EACH(F, sep, [REVERSE\_ARGS](#ga58de032c2ed7b4094c447c512dfd3784)(\_\_VA\_ARGS\_\_))

[REVERSE\_ARGS](#ga58de032c2ed7b4094c447c512dfd3784)

#define REVERSE\_ARGS(...)

Reverse arguments order.

**Definition** util\_macro.h:620

Call a macro `F` on each provided argument with a given separator between each call.

Example:

```
#define F(x) int a##x
FOR_EACH(F, (;), 4, 5, 6);
```

This expands to:

```
int a4;
int a5;
int a6;
```

Parameters
:   | F | Macro to invoke |
    | --- | --- |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | Variable argument list. The macro `F` is invoked as F(element) for each element in the list. |

## [◆ ](#ga1a2b2aa21d7cc37f33e6a62abd2ae340)FOR\_EACH\_FIXED\_ARG

| #define FOR\_EACH\_FIXED\_ARG | ( |  | *F*, |
| --- | --- | --- | --- |
|  |  |  | *sep*, |
|  |  |  | *fixed\_arg*, |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg, [REVERSE\_ARGS](#ga58de032c2ed7b4094c447c512dfd3784)(\_\_VA\_ARGS\_\_))

Call macro `F` on each provided argument, with an additional fixed argument as a parameter.

This is like [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12), except `F` should be a macro which takes two arguments: F(variable\_arg, fixed\_arg).

Example:

```
static void func(int val, void *dev);
FOR_EACH_FIXED_ARG(func, (;), dev, 4, 5, 6);
```

This expands to:

```
func(4, dev);
func(5, dev);
func(6, dev);
```

Parameters
:   | F | Macro to invoke |
    | --- | --- |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | fixed\_arg | Fixed argument passed to `F` as the second macro parameter. |
    | ... | Variable argument list. The macro `F` is invoked as F(element, fixed\_arg) for each element in the list. |

## [◆ ](#ga069f709e18eeafb8d276b5ff4fc09d31)FOR\_EACH\_IDX

| #define FOR\_EACH\_IDX | ( |  | *F*, |
| --- | --- | --- | --- |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_FOR\_EACH\_IDX(F, sep, [REVERSE\_ARGS](#ga58de032c2ed7b4094c447c512dfd3784)(\_\_VA\_ARGS\_\_))

Call macro `F` on each provided argument, with the argument's index as an additional parameter.

This is like [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12), except `F` should be a macro which takes two arguments: F(index, variable\_arg).

Example:

```
#define F(idx, x) int a##idx = x
FOR_EACH_IDX(F, (;), 4, 5, 6);
```

This expands to:

```
int a0 = 4;
int a1 = 5;
int a2 = 6;
```

Parameters
:   | F | Macro to invoke |
    | --- | --- |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | Variable argument list. The macro `F` is invoked as F(index, element) for each element in the list. |

## [◆ ](#ga2ab7377f5493123ffd29ebd1286457a9)FOR\_EACH\_IDX\_FIXED\_ARG

| #define FOR\_EACH\_IDX\_FIXED\_ARG | ( |  | *F*, |
| --- | --- | --- | --- |
|  |  |  | *sep*, |
|  |  |  | *fixed\_arg*, |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_FOR\_EACH\_IDX\_FIXED\_ARG(F, sep, fixed\_arg, [REVERSE\_ARGS](#ga58de032c2ed7b4094c447c512dfd3784)(\_\_VA\_ARGS\_\_))

Calls macro `F` for each variable argument with an index and fixed argument.

This is like the combination of [FOR\_EACH\_IDX()](#ga069f709e18eeafb8d276b5ff4fc09d31) with [FOR\_EACH\_FIXED\_ARG()](#ga1a2b2aa21d7cc37f33e6a62abd2ae340).

Example:

```
#define F(idx, x, fixed_arg) int fixed_arg##idx = x
FOR_EACH_IDX_FIXED_ARG(F, (;), a, 4, 5, 6);
```

This expands to:

```
int a0 = 4;
int a1 = 5;
int a2 = 6;
```

Parameters
:   | F | Macro to invoke |
    | --- | --- |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; This is required to enable providing a comma as separator. |
    | fixed\_arg | Fixed argument passed to `F` as the third macro parameter. |
    | ... | Variable list of arguments. The macro `F` is invoked as F(index, element, fixed\_arg) for each element in the list. |

## [◆ ](#ga24b3862161d725f5503b1bb08f4e339f)FOR\_EACH\_NONEMPTY\_TERM

| #define FOR\_EACH\_NONEMPTY\_TERM | ( |  | *F*, |
| --- | --- | --- | --- |
|  |  |  | *term*, |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[COND\_CODE\_0](#ga5483ea38af79bc6c4509936288705377)( \

/\* are there zero non-empty arguments ? \*/ \

[NUM\_VA\_ARGS\_LESS\_1](#ga8a0e9835e0a8f864ffc2359b9c419cc2)([LIST\_DROP\_EMPTY](#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_, \_)), \

/\* if so, expand to nothing \*/ \

(), \

/\* otherwise, expand to: \*/ \

(/\* FOR\_EACH() on nonempty elements, \*/ \

[FOR\_EACH](#ga278c8b7cbbea2f585e371d3568f3cb12)(F, term, [LIST\_DROP\_EMPTY](#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_)) \

/\* plus a final terminator \*/ \

\_\_DEBRACKET term \

))

[FOR\_EACH](#ga278c8b7cbbea2f585e371d3568f3cb12)

#define FOR\_EACH(F, sep,...)

Call a macro F on each provided argument with a given separator between each call.

**Definition** util\_macro.h:465

[COND\_CODE\_0](#ga5483ea38af79bc6c4509936288705377)

#define COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code)

Like COND\_CODE\_1() except tests if \_flag is 0.

**Definition** util\_macro.h:195

[LIST\_DROP\_EMPTY](#gab9762d5128988f7f4f5d51213ea52025)

#define LIST\_DROP\_EMPTY(...)

Remove empty arguments from list.

**Definition** util\_macro.h:315

Like [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12), but with a terminator instead of a separator, and drops empty elements from the argument list.

The `sep` argument to [FOR\_EACH(F, (sep), a, b)](#ga278c8b7cbbea2f585e371d3568f3cb12) is a separator which is placed between calls to `F`, like this:

```
FOR_EACH(F, (sep), a, b) // F(a) sep F(b)
                         //               ^^^ no sep here!
```

By contrast, the `term` argument to [FOR\_EACH\_NONEMPTY\_TERM(F, (term),
a, b)](#ga24b3862161d725f5503b1bb08f4e339f) is added after each time `F` appears in the expansion:

```
FOR_EACH_NONEMPTY_TERM(F, (term), a, b) // F(a) term F(b) term
                                        //                ^^^^
```

Further, any empty elements are dropped:

```
FOR_EACH_NONEMPTY_TERM(F, (term), a, EMPTY, b) // F(a) term F(b) term
```

This is more convenient in some cases, because [FOR\_EACH\_NONEMPTY\_TERM()](#ga24b3862161d725f5503b1bb08f4e339f) expands to nothing when given an empty argument list, and it's often cumbersome to write a macro `F` that does the right thing even when given an empty argument.

One example is when \_\_VA\_ARGS\_\_ may or may not be empty, and the results are embedded in a larger initializer:

```
#define SQUARE(x) ((x)*(x))

int my_array[] = {
        FOR_EACH_NONEMPTY_TERM(SQUARE, (,), FOO(...))
        FOR_EACH_NONEMPTY_TERM(SQUARE, (,), BAR(...))
        FOR_EACH_NONEMPTY_TERM(SQUARE, (,), BAZ(...))
};
```

This is more convenient than:

1. figuring out whether the `FOO`, `BAR`, and `BAZ` expansions are empty and adding a comma manually (or not) between [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12) calls
2. rewriting SQUARE so it reacts appropriately when "x" is empty (which would be necessary if e.g. `FOO` expands to nothing)

Parameters
:   | F | Macro to invoke on each nonempty element of the variable arguments |
    | --- | --- |
    | term | Terminator (e.g. comma or semicolon) placed after each invocation of F. Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | Variable argument list. The macro `F` is invoked as F(element) for each nonempty element in the list. |

## [◆ ](#gaf207e8203eedc05adcf341a24bfa6cbb)GB

| #define GB | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

([MB](#ga44d2b171cc92225ec0a76ef70fc9b531)(x) << 10)

[MB](#ga44d2b171cc92225ec0a76ef70fc9b531)

#define MB(x)

Number of bytes in x mebibytes.

**Definition** util.h:723

Number of bytes in `x` gibibytes.

## [◆ ](#ga58530d20924859d16358c7400c37738d)GENMASK

| #define GENMASK | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *l* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((~0UL) - (1UL << (l)) + 1) & (~0UL >> ([BITS\_PER\_LONG](#ga2f660aa23a5dbc0f4b8df48b4302b8c3) - 1 - (h))))

[BITS\_PER\_LONG](#ga2f660aa23a5dbc0f4b8df48b4302b8c3)

#define BITS\_PER\_LONG

Number of bits in a long int.

**Definition** util.h:58

Create a contiguous bitmask starting at bit position `l` and ending at position `h`.

## [◆ ](#gab631f8a0ecb6fde5b22df40607868f04)GENMASK64

| #define GENMASK64 | ( |  | *h*, |
| --- | --- | --- | --- |
|  |  |  | *l* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((~0ULL) - (1ULL << (l)) + 1) & (~0ULL >> ([BITS\_PER\_LONG\_LONG](#gaeb3fa0f8ac477da6575363a158f36891) - 1 - (h))))

[BITS\_PER\_LONG\_LONG](#gaeb3fa0f8ac477da6575363a158f36891)

#define BITS\_PER\_LONG\_LONG

Number of bits in a long long int.

**Definition** util.h:61

Create a contiguous 64-bit bitmask starting at bit position `l` and ending at position `h`.

## [◆ ](#gabbe04a4d59a495b2b86196304b937ec6)GET\_ARG\_N

| #define GET\_ARG\_N | ( |  | *N*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_GET\_ARG\_##N(\_\_VA\_ARGS\_\_)

Get nth argument from argument list.

Parameters
:   | N | Argument index to fetch. Counter from 1. |
    | --- | --- |
    | ... | Variable list of arguments from which one argument is returned. |

Returns
:   Nth argument.

## [◆ ](#ga01e1dc9b92e5be6895528d1da5f0c88b)GET\_ARGS\_LESS\_N

| #define GET\_ARGS\_LESS\_N | ( |  | *N*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_GET\_ARGS\_LESS\_##N(\_\_VA\_ARGS\_\_)

Strips n first arguments from the argument list.

Parameters
:   | N | Number of arguments to discard. |
    | --- | --- |
    | ... | Variable list of arguments. |

Returns
:   argument list without N first arguments.

## [◆ ](#gaaed493c6115c04272077a0f3854b9a83)IDENTITY

| #define IDENTITY | ( |  | *V* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

V

Macro that expands to its argument.

This is useful in macros like `[FOR_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12)` when there is no transformation required on the list elements.

Parameters
:   | V | any value |
    | --- | --- |

## [◆ ](#gaa65e031f24a2c0fb4eae240e2c60b36a)IF\_DISABLED

| #define IF\_DISABLED | ( |  | *\_flag*, |
| --- | --- | --- | --- |
|  |  |  | *\_code* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[COND\_CODE\_1](#ga358bc3e7669c860a98839a51cd526b20)(\_flag, (), \_code)

[COND\_CODE\_1](#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Insert code if `_flag` is not defined as 1.

This expands to nothing if `_flag` is defined and equal to 1; it expands to `_code` otherwise.

Example:

```
IF_DISABLED(CONFIG_FLAG, (uint32_t foo;))
```

If `CONFIG_FLAG` isn't defined or different than 1, this expands to:

```
uint32_t foo;
```

and to nothing otherwise.

IF\_DISABLED does the opposite of IF\_ENABLED.

Parameters
:   | \_flag | evaluated flag |
    | --- | --- |
    | \_code | result if `_flag` does not expand to 1; must be in parentheses |

## [◆ ](#gae67ffe50e848951dbde309ed569ea925)IF\_ENABLED

| #define IF\_ENABLED | ( |  | *\_flag*, |
| --- | --- | --- | --- |
|  |  |  | *\_code* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[COND\_CODE\_1](#ga358bc3e7669c860a98839a51cd526b20)(\_flag, \_code, ())

Insert code if `_flag` is defined and equals 1.

Like [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20), this expands to `_code` if `_flag` is defined to 1; it expands to nothing otherwise.

Example:

```
IF_ENABLED(CONFIG_FLAG, (uint32_t foo;))
```

If `CONFIG_FLAG` is defined to 1, this expands to:

```
uint32_t foo;
```

and to nothing otherwise.

It can be considered as a more compact alternative to:

```
#if defined(CONFIG_FLAG) && (CONFIG_FLAG == 1)
uint32_t foo;
#endif
```

Parameters
:   | \_flag | evaluated flag |
    | --- | --- |
    | \_code | result if `_flag` expands to 1; must be in parentheses |

## [◆ ](#gaea00fb0c11b73f77da8884374e2121b4)IN\_RANGE

| #define IN\_RANGE | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *min*, |
|  |  |  | *max* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

((val) >= (min) && (val) <= (max))

Checks if a value is within range.

Note
:   `val` is evaluated twice.

Parameters
:   | val | Value to be checked. |
    | --- | --- |
    | min | Lower bound (inclusive). |
    | max | Upper bound (inclusive). |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If value is within range |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the value is not within range |

## [◆ ](#gae236ed18fe2ff18ab47c15d2e7eeb417)INT\_TO\_POINTER

| #define INT\_TO\_POINTER | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((void \*) ([intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)) (x))

[intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)

\_\_INTPTR\_TYPE\_\_ intptr\_t

**Definition** stdint.h:104

Cast `x`, a signed integer, to a void\*.

## [◆ ](#gaa0be479debd8300ab6b43f4d028ab5da)IS\_ARRAY

| #define IS\_ARRAY | ( |  | *array* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

[ZERO\_OR\_COMPILE\_ERROR](#ga831cb8468911b8ebdb9b42682778e53d)( \

!\_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(array), \

\_\_typeof\_\_(&(array)[0])))

[ZERO\_OR\_COMPILE\_ERROR](#ga831cb8468911b8ebdb9b42682778e53d)

#define ZERO\_OR\_COMPILE\_ERROR(cond)

0 if cond is true-ish; causes a compile error otherwise.

**Definition** util.h:94

Zero if `array` has an array type, a compile error otherwise.

This macro is available only from C, not C++.

## [◆ ](#gad403257ac6868c8bf3415ae771ce0a04)IS\_ARRAY\_ELEMENT

| #define IS\_ARRAY\_ELEMENT | ( |  | *array*, |
| --- | --- | --- | --- |
|  |  |  | *ptr* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

((ptr) && [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(array) <= [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(ptr) && \

POINTER\_TO\_UINT(ptr) < [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(&(array)[[ARRAY\_SIZE](#ga70c57aae3eb654e205459b4362c8089a)(array)]) && \

([POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(ptr) - [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(array)) % sizeof((array)[0]) == 0)

Whether `ptr` is an element of `array`.

This macro can be seen as a slightly stricter version of [PART\_OF\_ARRAY](#ga4fbecf59c021cb60fa1267b7818f90ef) in that it also ensures that `ptr` is aligned to an array-element boundary of `array`.

In C, passing a pointer as `array` causes a compile error.

Parameters
:   | array | the array in question |
    | --- | --- |
    | ptr | the pointer to check |

Returns
:   1 if `ptr` is part of `array`, 0 otherwise

## [◆ ](#ga6d4b02e5da10bf93c4697dd6bf239ffd)IS\_BIT\_MASK

| #define IS\_BIT\_MASK | ( |  | *m* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[IS\_SHIFTED\_BIT\_MASK](#ga406b5955c2803cdd9d9f19c90f242662)(m, 0)

[IS\_SHIFTED\_BIT\_MASK](#ga406b5955c2803cdd9d9f19c90f242662)

#define IS\_SHIFTED\_BIT\_MASK(m, s)

Check if bits are set continuously from the specified bit.

**Definition** util\_macro.h:87

Check if bits are set continuously from the LSB.

Parameters
:   | m | Check whether the bits are set continuously from LSB. |
    | --- | --- |

## [◆ ](#gab9487eea703d51cb1f235432dab4a1c7)IS\_EMPTY

| #define IS\_EMPTY | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_IS\_EMPTY\_(\_\_VA\_ARGS\_\_)

Check if a macro has a replacement expression.

If `a` is a macro defined to a nonempty value, this will return true, otherwise it will return false. It only works with defined macros, so an additional `#ifdef` test may be needed in some cases.

This macro may be used with [COND\_CODE\_1()](#ga358bc3e7669c860a98839a51cd526b20) and [COND\_CODE\_0()](#ga5483ea38af79bc6c4509936288705377) while processing \_\_VA\_ARGS\_\_ to avoid processing empty arguments.

Example:

```
 #define EMPTY
 #define NON_EMPTY  1
 #undef  UNDEFINED
 IS_EMPTY(EMPTY)
 IS_EMPTY(NON_EMPTY)
 IS_EMPTY(UNDEFINED)
 #if defined(EMPTY) && IS_EMPTY(EMPTY) == true
 some_conditional_code
 #endif
```

In above examples, the invocations of [IS\_EMPTY(...)](#gab9487eea703d51cb1f235432dab4a1c7) return `true`, `false`, and `true`; `some_conditional_code` is included.

Parameters
:   | ... | macro to check for emptiness (may be \_\_VA\_ARGS\_\_) |
    | --- | --- |

## [◆ ](#ga111fe4e9d63758262fc6810a782cb32a)IS\_ENABLED

| #define IS\_ENABLED | ( |  | *config\_macro* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_IS\_ENABLED1(config\_macro)

Check for macro definition in compiler-visible expressions.

This trick was pioneered in Linux as the config\_enabled() macro. It has the effect of taking a macro value that may be defined to "1" or may not be defined at all and turning it into a literal expression that can be handled by the C compiler instead of just the preprocessor. It is often used with a `CONFIG_FOO` macro which may be defined to 1 via Kconfig, or left undefined.

That is, it works similarly to #if defined(CONFIG\_FOO) except that its expansion is a C expression. Thus, much #ifdef usage can be replaced with equivalents like:

```
if (IS_ENABLED(CONFIG_FOO)) {
        do_something_with_foo
}
```

This is cleaner since the compiler can generate errors and warnings for `do_something_with_foo` even when `CONFIG_FOO` is undefined.

Note: Use of IS\_ENABLED in a #if statement is discouraged as it doesn't provide any benefit vs plain #if defined()

Parameters
:   | config\_macro | Macro to check |
    | --- | --- |

Returns
:   1 if `config_macro` is defined to 1, 0 otherwise (including if `config_macro` is not defined)

## [◆ ](#gaa35a6894bca38a8ffb558c2c22a1eee1)IS\_EQ

| #define IS\_EQ | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_IS\_EQ(a, b)

Like a == b, but does evaluation and short-circuiting at C preprocessor time.

This however only works for integer literal from 0 to 4095.

## [◆ ](#ga52d277cbf33f76350b2fcb21c24640ee)IS\_POWER\_OF\_TWO

| #define IS\_POWER\_OF\_TWO | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

(((x) != 0U) && (((x) & ((x) - 1U)) == 0U))

Check if a `x` is a power of two.

## [◆ ](#ga406b5955c2803cdd9d9f19c90f242662)IS\_SHIFTED\_BIT\_MASK

| #define IS\_SHIFTED\_BIT\_MASK | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

(!(((m) >> ([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))) & (((m) >> ([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))) + 1U)))

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

Check if bits are set continuously from the specified bit.

The macro is not dependent on the bit-width.

Parameters
:   | m | Check whether the bits are set continuously or not. |
    | --- | --- |
    | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Specify the lowest bit for that is continuously set bits. |

## [◆ ](#ga5c723c0cc71b83224ead557db3ab74dd)KB

| #define KB | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((x) << 10)

Number of bytes in `x` kibibytes.

## [◆ ](#gaee55275295c076c6d23c994777623253)KHZ

| #define KHZ | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((x) \* 1000)

Number of Hz in `x` kHz.

## [◆ ](#gab9762d5128988f7f4f5d51213ea52025)LIST\_DROP\_EMPTY

| #define LIST\_DROP\_EMPTY | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_LIST\_DROP\_FIRST([FOR\_EACH](#ga278c8b7cbbea2f585e371d3568f3cb12)(Z\_LIST\_NO\_EMPTIES, (), \_\_VA\_ARGS\_\_))

Remove empty arguments from list.

During macro expansion, \_\_VA\_ARGS\_\_ and other preprocessor generated lists may contain empty elements, e.g.:

```
 #define LIST ,a,b,,d,
```

Using EMPTY to show each empty element, LIST contains:

```
 EMPTY, a, b, EMPTY, d
```

When processing such lists, e.g. using [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12), all empty elements will be processed, and may require filtering out. To make that process easier, it is enough to invoke LIST\_DROP\_EMPTY which will remove all empty elements.

Example:

```
 LIST_DROP_EMPTY(LIST)
```

expands to:

```
 a, b, d
```

Parameters
:   | ... | list to be processed |
    | --- | --- |

## [◆ ](#ga81cbc0233cf73048d65b76f716653af6)LISTIFY

| #define LISTIFY | ( |  | *LEN*, |
| --- | --- | --- | --- |
|  |  |  | *F*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(Z\_UTIL\_LISTIFY\_, LEN)(F, sep, \_\_VA\_ARGS\_\_)

Generates a sequence of code with configurable separator.

Example:

```
#define FOO(i, _) MY_PWM ## i
{ LISTIFY(PWM_COUNT, FOO, (,)) }
```

The above two lines expand to:

{ MY\_PWM0 , MY\_PWM1 }

Parameters
:   | LEN | The length of the sequence. Must be an integer literal less than 4095. |
    | --- | --- |
    | F | A macro function that accepts at least two arguments: F(i, ...). `F` is called repeatedly in the expansion. Its first argument `i` is the index in the sequence, and the variable list of arguments passed to LISTIFY are passed through to `F`. |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

Note
:   Calling LISTIFY with undefined arguments has undefined behavior.

## [◆ ](#ga40805b5dd56ee36df59a7bbe403ddf33)LOG2

| #define LOG2 | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((x) < 1 ? -1 : \_\_z\_log2(x))

Compute log2(x).

Note
:   This macro expands its argument multiple times (to permit use in constant expressions), which must not have side effects.

Parameters
:   | x | An unsigned integral value to compute logarithm of (positive only) |
    | --- | --- |

Returns
:   log2(x) when 1 <= x <= max(x), -1 when x < 1

## [◆ ](#gada629edfcec9fa2fc3dc5d7af70abb03)LOG2CEIL

| #define LOG2CEIL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((x) < 1 ? 0 : \_\_z\_log2((x)-1) + 1)

Compute ceil(log2(x)).

Note
:   This macro expands its argument multiple times (to permit use in constant expressions), which must not have side effects.

Parameters
:   | x | An unsigned integral value |
    | --- | --- |

Returns
:   ceil(log2(x)) when 1 <= x <= max(type(x)), 0 when x < 1

## [◆ ](#ga92235ab2e350fbdc01ddf0f894e5e4c0)LSB\_GET

| #define LSB\_GET | ( |  | *value* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((value) & -(value))

Extract the Least Significant Bit from `value`.

## [◆ ](#gaf82371bd6bf317add5276fc6cbd66662)MACRO\_MAP\_CAT

| #define MACRO\_MAP\_CAT | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[MACRO\_MAP\_CAT\_](util__internal_8h.md#abe4f647ef2c1c706bc9d0d0e737e58bf)(\_\_VA\_ARGS\_\_)

[MACRO\_MAP\_CAT\_](util__internal_8h.md#abe4f647ef2c1c706bc9d0d0e737e58bf)

#define MACRO\_MAP\_CAT\_(...)

**Definition** util\_internal.h:140

Mapping macro that pastes results together.

This is similar to [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12) in that it invokes a macro repeatedly on each element of \_\_VA\_ARGS\_\_. However, unlike [FOR\_EACH()](#ga278c8b7cbbea2f585e371d3568f3cb12), [MACRO\_MAP\_CAT()](#gaf82371bd6bf317add5276fc6cbd66662) pastes the results together into a single token.

For example, with this macro FOO:

```
#define FOO(x) item_##x##_
```

[MACRO\_MAP\_CAT(FOO, a, b, c)](#gaf82371bd6bf317add5276fc6cbd66662), expands to the token:

```
item_a_item_b_item_c_
```

Parameters
:   | ... | Macro to expand on each argument, followed by its arguments. (The macro should take exactly one argument.) |
    | --- | --- |

Returns
:   The results of expanding the macro on each argument, all pasted together

## [◆ ](#ga58eba1f911e21da46b8beea264934d55)MACRO\_MAP\_CAT\_N

| #define MACRO\_MAP\_CAT\_N | ( |  | *N*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[MACRO\_MAP\_CAT\_N\_](util__internal_8h.md#a72d29784bb0a030942e2c6eb2f9d42b9)(N, \_\_VA\_ARGS\_\_)

[MACRO\_MAP\_CAT\_N\_](util__internal_8h.md#a72d29784bb0a030942e2c6eb2f9d42b9)

#define MACRO\_MAP\_CAT\_N\_(N,...)

**Definition** util\_internal.h:143

Mapping macro that pastes a fixed number of results together.

Similar to [MACRO\_MAP\_CAT()](#gaf82371bd6bf317add5276fc6cbd66662), but expects a fixed number of arguments. If more arguments are given than are expected, the rest are ignored.

Parameters
:   | N | Number of arguments to map |
    | --- | --- |
    | ... | Macro to expand on each argument, followed by its arguments. (The macro should take exactly one argument.) |

Returns
:   The results of expanding the macro on each argument, all pasted together

## [◆ ](#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)MAX

| #define MAX | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((a) > (b)) ? (a) : (b))

Obtain the maximum of two values.

Note
:   Arguments are evaluated twice. Use Z\_MAX for a GCC-only, single evaluation version

Parameters
:   | a | First value. |
    | --- | --- |
    | b | Second value. |

Returns
:   Maximum value of `a` and `b`.

## [◆ ](#ga44d2b171cc92225ec0a76ef70fc9b531)MB

| #define MB | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

([KB](#ga5c723c0cc71b83224ead557db3ab74dd)(x) << 10)

[KB](#ga5c723c0cc71b83224ead557db3ab74dd)

#define KB(x)

Number of bytes in x kibibytes.

**Definition** util.h:718

Number of bytes in `x` mebibytes.

## [◆ ](#gab7b18750ddf0850461f926ae151ca7fa)MHZ

| #define MHZ | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

([KHZ](#gaee55275295c076c6d23c994777623253)(x) \* 1000)

[KHZ](#gaee55275295c076c6d23c994777623253)

#define KHZ(x)

Number of Hz in x kHz.

**Definition** util.h:728

Number of Hz in `x` MHz.

## [◆ ](#ga3acffbd305ee72dcd4593c0d8af64a4f)MIN

| #define MIN | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((a) < (b)) ? (a) : (b))

Obtain the minimum of two values.

Note
:   Arguments are evaluated twice. Use Z\_MIN for a GCC-only, single evaluation version

Parameters
:   | a | First value. |
    | --- | --- |
    | b | Second value. |

Returns
:   Minimum value of `a` and `b`.

## [◆ ](#ga2ab444fed50a82cc1fe0e952fd03127d)NHPOT

| #define NHPOT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((x) < 1 ? 1 : ((x) > (1ULL<<63) ? 0 : 1ULL << [LOG2CEIL](#gada629edfcec9fa2fc3dc5d7af70abb03)(x)))

[LOG2CEIL](#gada629edfcec9fa2fc3dc5d7af70abb03)

#define LOG2CEIL(x)

Compute ceil(log2(x)).

**Definition** util.h:633

Compute next highest power of two.

Equivalent to 2^ceil(log2(x))

Note
:   This macro expands its argument multiple times (to permit use in constant expressions), which must not have side effects.

Parameters
:   | x | An unsigned integral value |
    | --- | --- |

Returns
:   2^ceil(log2(x)) or 0 if 2^ceil(log2(x)) would saturate 64-bits

## [◆ ](#ga8a0e9835e0a8f864ffc2359b9c419cc2)NUM\_VA\_ARGS\_LESS\_1

| #define NUM\_VA\_ARGS\_LESS\_1 | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[NUM\_VA\_ARGS\_LESS\_1\_IMPL](util__internal_8h.md#a70e3443886f63259dc12b14cc26c365f)(\_\_VA\_ARGS\_\_, 63, 62, 61, \

60, 59, 58, 57, 56, 55, 54, 53, 52, 51, \

50, 49, 48, 47, 46, 45, 44, 43, 42, 41, \

40, 39, 38, 37, 36, 35, 34, 33, 32, 31, \

30, 29, 28, 27, 26, 25, 24, 23, 22, 21, \

20, 19, 18, 17, 16, 15, 14, 13, 12, 11, \

10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, ~)

[NUM\_VA\_ARGS\_LESS\_1\_IMPL](util__internal_8h.md#a70e3443886f63259dc12b14cc26c365f)

#define NUM\_VA\_ARGS\_LESS\_1\_IMPL( \_ignored, \_0, \_1, \_2, \_3, \_4, \_5, \_6, \_7, \_8, \_9, \_10, \_11, \_12, \_13, \_14, \_15, \_16, \_17, \_18, \_19, \_20, \_21, \_22, \_23, \_24, \_25, \_26, \_27, \_28, \_29, \_30, \_31, \_32, \_33, \_34, \_35, \_36, \_37, \_38, \_39, \_40, \_41, \_42, \_43, \_44, \_45, \_46, \_47, \_48, \_49, \_50, \_51, \_52, \_53, \_54, \_55, \_56, \_57, \_58, \_59, \_60, \_61, \_62, N,...)

**Definition** util\_internal.h:129

Number of arguments in the variable arguments list minus one.

Parameters
:   | ... | List of arguments |
    | --- | --- |

Returns
:   Number of variadic arguments in the argument list, minus one

## [◆ ](#ga4fbecf59c021cb60fa1267b7818f90ef)PART\_OF\_ARRAY

| #define PART\_OF\_ARRAY | ( |  | *array*, |
| --- | --- | --- | --- |
|  |  |  | *ptr* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

((ptr) && [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(array) <= [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(ptr) && \

POINTER\_TO\_UINT(ptr) < [POINTER\_TO\_UINT](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(&(array)[[ARRAY\_SIZE](#ga70c57aae3eb654e205459b4362c8089a)(array)]))

Check if a pointer `ptr` lies within `array`.

In C but not C++, this causes a compile error if `array` is not an array (e.g. if `ptr` and `array` are mixed up).

Parameters
:   | array | an array |
    | --- | --- |
    | ptr | a pointer |

Returns
:   1 if `ptr` is part of `array`, 0 otherwise

## [◆ ](#ga6e5ec9c46d0140315a7c1d80d1cc3c38)POINTER\_TO\_INT

| #define POINTER\_TO\_INT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

(([intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)) (x))

Cast `x`, a pointer, to a signed integer.

## [◆ ](#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)POINTER\_TO\_UINT

| #define POINTER\_TO\_UINT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) (x))

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

Cast `x`, a pointer, to an unsigned integer.

## [◆ ](#ga58de032c2ed7b4094c447c512dfd3784)REVERSE\_ARGS

| #define REVERSE\_ARGS | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

Z\_FOR\_EACH\_ENGINE(Z\_FOR\_EACH\_EXEC, (,), Z\_BYPASS, \_, \_\_VA\_ARGS\_\_)

Reverse arguments order.

Parameters
:   | ... | Variable argument list. |
    | --- | --- |

## [◆ ](#gad8d2389dbe7ea135eccf237dbafb76dd)ROUND\_DOWN

| #define ROUND\_DOWN | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *align* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

(((unsigned long)(x) / (unsigned long)(align)) \* (unsigned long)(align))

Value of `x` rounded down to the previous multiple of `align`.

## [◆ ](#gaada5610108b15d85c65d863b0c646ef3)ROUND\_UP

| #define ROUND\_UP | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *align* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

((((unsigned long)(x) + ((unsigned long)(align) - 1)) / \

(unsigned long)(align)) \* (unsigned long)(align))

Value of `x` rounded up to the next multiple of `align`.

## [◆ ](#ga78e587047fe4af679141595363c07179)SAME\_TYPE

| #define SAME\_TYPE | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

\_\_builtin\_types\_compatible\_p(\_\_typeof\_\_(a), \_\_typeof\_\_(b))

Validate if two entities have a compatible type.

Parameters
:   | a | the first entity to be compared |
    | --- | --- |
    | b | the second entity to be compared |

Returns
:   1 if the two elements are compatible, 0 if they are not

## [◆ ](#gab74ce0513c348e0b257d38473e77e1a1)UINT\_TO\_POINTER

| #define UINT\_TO\_POINTER | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((void \*) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)) (x))

Cast `x`, an unsigned integer, to a void\*.

## [◆ ](#ga26179b776b4a03143e8be1612ef6d853)UTIL\_AND

| #define UTIL\_AND | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[COND\_CODE\_1](#ga358bc3e7669c860a98839a51cd526b20)([UTIL\_BOOL](util__internal_8h.md#a80cbb3a182096676524d761113349bc8)(a), (b), (0))

[UTIL\_BOOL](util__internal_8h.md#a80cbb3a182096676524d761113349bc8)

#define UTIL\_BOOL(x)

**Definition** util\_internal.h:113

Like a && b, but does evaluation and short-circuiting at C preprocessor time.

This is not the same as the binary `&&`, however; in particular, `a` should expand to an integer literal 0 or 1. However, `b` can be any value.

This can be useful when `b` is an expression that would cause a build error when `a` is 0.

## [◆ ](#gaa7623e1e33316024217094698e4d8258)UTIL\_DEC

| #define UTIL\_DEC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[UTIL\_PRIMITIVE\_CAT](util__internal_8h.md#a333f808696450134a9948dcc9e57e4ae)(Z\_UTIL\_DEC\_, x)

[UTIL\_PRIMITIVE\_CAT](util__internal_8h.md#a333f808696450134a9948dcc9e57e4ae)

#define UTIL\_PRIMITIVE\_CAT(a,...)

**Definition** util\_internal.h:105

[UTIL\_DEC(x)](#gaa7623e1e33316024217094698e4d8258) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x-1.

See also
:   [UTIL\_INC(x)](#ga90a54212306c3e210ac87fd0bd7b32da)

## [◆ ](#ga90a54212306c3e210ac87fd0bd7b32da)UTIL\_INC

| #define UTIL\_INC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[UTIL\_PRIMITIVE\_CAT](util__internal_8h.md#a333f808696450134a9948dcc9e57e4ae)(Z\_UTIL\_INC\_, x)

[UTIL\_INC(x)](#ga90a54212306c3e210ac87fd0bd7b32da) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x+1.

See also
:   [UTIL\_DEC(x)](#gaa7623e1e33316024217094698e4d8258)

## [◆ ](#ga50cfdf948906976562c3f0625c84c2b2)UTIL\_OR

| #define UTIL\_OR | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[COND\_CODE\_1](#ga358bc3e7669c860a98839a51cd526b20)([UTIL\_BOOL](util__internal_8h.md#a80cbb3a182096676524d761113349bc8)(a), (a), (b))

Like a || b, but does evaluation and short-circuiting at C preprocessor time.

This is not the same as the binary `||` operator; in particular, `a` should expand to an integer literal 0 or 1. However, `b` can be any value.

This can be useful when `b` is an expression that would cause a build error when `a` is 1.

## [◆ ](#gab23deac75762adfb6bdde2c15d51f158)UTIL\_X2

| #define UTIL\_X2 | ( |  | *y* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

[UTIL\_PRIMITIVE\_CAT](util__internal_8h.md#a333f808696450134a9948dcc9e57e4ae)(Z\_UTIL\_X2\_, y)

[UTIL\_X2(y)](#gab23deac75762adfb6bdde2c15d51f158) for an integer literal y from 0 to 4095 expands to an integer literal whose value is 2y.

## [◆ ](#ga68eb35df6b4715714312df90209accee)WAIT\_FOR

| #define WAIT\_FOR | ( |  | *expr*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *delay\_stmt* ) |

`#include <[util.h](util_8h.md)>`

**Value:**

({ \

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_wf\_cycle\_count = [k\_us\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#ga689a3f97643be5362c8c70c6d9d81051)(timeout); \

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_wf\_start = [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)(); \

while (!(expr) && (\_wf\_cycle\_count > ([k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)() - \_wf\_start))) { \

delay\_stmt; \

Z\_SPIN\_DELAY(10); \

} \

(expr); \

})

[k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)

static uint32\_t k\_cycle\_get\_32(void)

Read the hardware clock.

**Definition** kernel.h:1805

[k\_us\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#ga689a3f97643be5362c8c70c6d9d81051)

#define k\_us\_to\_cyc\_ceil32(t)

Convert microseconds to hardware cycles.

**Definition** time\_units.h:594

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Wait for an expression to return true with a timeout.

Spin on an expression with a timeout and optional delay between iterations

Commonly needed when waiting on hardware to complete an asynchronous request to read/write/initialize/reset, but useful for any expression.

Parameters
:   | expr | Truth expression upon which to poll, e.g.: XYZREG & XYZREG\_EN |
    | --- | --- |
    | timeout | Timeout to wait for in microseconds, e.g.: 1000 (1ms) |
    | delay\_stmt | Delay statement to perform each poll iteration e.g.: NULL, [k\_yield()](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295 "Yield the current thread."), k\_msleep(1) or k\_busy\_wait(1) |

Return values
:   | expr | As a boolean return, if false then it has timed out. |
    | --- | --- |

## [◆ ](#gadbc789ee99633a92584387ba2a4f7052)WB\_DN

| #define WB\_DN | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

[ROUND\_DOWN](#gad8d2389dbe7ea135eccf237dbafb76dd)(x, sizeof(void \*))

[ROUND\_DOWN](#gad8d2389dbe7ea135eccf237dbafb76dd)

#define ROUND\_DOWN(x, align)

Value of x rounded down to the previous multiple of align.

**Definition** util.h:295

Value of `x` rounded down to the previous word boundary.

## [◆ ](#ga8b16b3a76faa15ea544e4b0edb3e62c7)WB\_UP

| #define WB\_UP | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

[ROUND\_UP](#gaada5610108b15d85c65d863b0c646ef3)(x, sizeof(void \*))

[ROUND\_UP](#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:288

Value of `x` rounded up to the next word boundary.

## [◆ ](#ga23a900e882ecb48455e70f01fd45b246)WRITE\_BIT

| #define WRITE\_BIT | ( |  | *var*, |
| --- | --- | --- | --- |
|  |  |  | *bit*, |
|  |  |  | *set* ) |

`#include <[util_macro.h](util__macro_8h.md)>`

**Value:**

((var) = (set) ? ((var) | [BIT](#ga3a8ea58898cb58fc96013383d39f482c)(bit)) : ((var) & [~BIT](#ga3a8ea58898cb58fc96013383d39f482c)(bit)))

Set or clear a bit depending on a boolean value.

The argument `var` is a variable whose value is written to as a side effect.

Parameters
:   | var | Variable to be altered |
    | --- | --- |
    | bit | Bit number |
    | set | if 0, clears `bit` in `var`; any other value sets `bit` |

## [◆ ](#ga831cb8468911b8ebdb9b42682778e53d)ZERO\_OR\_COMPILE\_ERROR

| #define ZERO\_OR\_COMPILE\_ERROR | ( |  | *cond* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

**Value:**

((int) sizeof(char[1 - 2 \* !(cond)]) - 1)

0 if `cond` is true-ish; causes a compile error otherwise.

## Function Documentation

## [◆ ](#ga1ffeb18b8ed73d37c2485c82988ed1ec)arithmetic\_shift\_right()

| | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) arithmetic\_shift\_right | ( | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | *value*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *shift* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

Arithmetic shift right.

Parameters
:   | value | value to shift |
    | --- | --- |
    | shift | number of bits to shift |

Returns
:   `value` shifted right by `shift`; opened bit positions are filled with the sign bit

## [◆ ](#gaa0f77b877eb5db5a228b79cba110abe4)bcd2bin()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bcd2bin | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bcd* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

Convert a binary coded decimal (BCD 8421) value to binary.

Parameters
:   | bcd | BCD 8421 value to convert. |
    | --- | --- |

Returns
:   Binary representation of input value.

## [◆ ](#ga6dff7f443aa795258c64cee63b29b591)bin2bcd()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bin2bcd | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *bin* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

Convert a binary value to binary coded decimal (BCD 8421).

Parameters
:   | bin | Binary value to convert. |
    | --- | --- |

Returns
:   BCD 8421 representation of input value.

## [◆ ](#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)bin2hex()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bin2hex | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen*, |
|  |  | char \* | *hex*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *hexlen* ) |

`#include <[util.h](util_8h.md)>`

Convert a binary array into string representation.

Parameters
:   | buf | The binary array to convert |
    | --- | --- |
    | buflen | The length of the binary array to convert |
    | hex | Address of where to store the string representation. |
    | hexlen | Size of the storage area for string representation. |

Returns
:   The length of the converted string, or 0 if an error occurred.

## [◆ ](#ga3379c356de17dbeebfa7588d8c964d5e)bytecpy()

| | void bytecpy | ( | void \* | *dst*, | | --- | --- | --- | --- | |  |  | const void \* | *src*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

byte by byte memcpy.

Copy size bytes of src into dest. This is guaranteed to be done byte by byte.

Parameters
:   | dst | Pointer to the destination memory. |
    | --- | --- |
    | src | Pointer to the source of the data. |
    | size | The number of bytes to copy. |

## [◆ ](#ga8624d1e5411703deac1ab8517f132d7b)byteswp()

| | void byteswp | ( | void \* | *a*, | | --- | --- | --- | --- | |  |  | void \* | *b*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

byte by byte swap.

Swap *size* bytes between memory regions *a* and *b*. This is guaranteed to be done byte by byte.

Parameters
:   | a | Pointer to the the first memory region. |
    | --- | --- |
    | b | Pointer to the the second memory region. |
    | size | The number of bytes to swap. |

## [◆ ](#gaaf91757f6fe86ab417536d5066ce14e6)char2hex()

| int char2hex | ( | char | *c*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *x* ) |

`#include <[util.h](util_8h.md)>`

Convert a single character into a hexadecimal nibble.

Parameters
:   | c | The character to convert |
    | --- | --- |
    | x | The address of storage for the converted number. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga269a01ffa3f1a3485b79d8a54a78a3f1)hex2bin()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hex2bin | ( | const char \* | *hex*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *hexlen*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen* ) |

`#include <[util.h](util_8h.md)>`

Convert a hexadecimal string into a binary array.

Parameters
:   | hex | The hexadecimal string to convert |
    | --- | --- |
    | hexlen | The length of the hexadecimal string to convert. |
    | buf | Address of where to store the binary data |
    | buflen | Size of the storage area for binary data |

Returns
:   The length of the binary array, or 0 if an error occurred.

## [◆ ](#ga9ed3bd04d5c0797aebf333733913028c)hex2char()

| int hex2char | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *x*, |
| --- | --- | --- | --- |
|  |  | char \* | *c* ) |

`#include <[util.h](util_8h.md)>`

Convert a single hexadecimal nibble into a character.

Parameters
:   | c | The number to convert |
    | --- | --- |
    | x | The address of storage for the converted character. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gadfe7046eb6c39bb3c84c18d8ac7a230e)is\_power\_of\_two()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_power\_of\_two | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

Is `x` a power of two?

Parameters
:   | x | value to check |
    | --- | --- |

Returns
:   true if `x` is a power of two, false otherwise

## [◆ ](#ga64037dd6934130ca6a6dc3e5357b9743)mem\_xor\_128()

| | void mem\_xor\_128 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[16], | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src1*[16], | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src2*[16] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

XOR 128 bits.

Parameters
:   | dst | Destination of where to store result. Shall be 128 bits. |
    | --- | --- |
    | src1 | First source. Shall be 128 bits. |
    | src2 | Second source. Shall be 128 bits. |

## [◆ ](#ga6f1717e3eeb4a91afa2be14061d52203)mem\_xor\_32()

| | void mem\_xor\_32 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[4], | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src1*[4], | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src2*[4] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

XOR 32 bits.

Parameters
:   | dst | Destination of where to store result. Shall be 32 bits. |
    | --- | --- |
    | src1 | First source. Shall be 32 bits. |
    | src2 | Second source. Shall be 32 bits. |

## [◆ ](#ga8a9d63740a8718de8ab0ce057cfbd4f4)mem\_xor\_n()

| | void mem\_xor\_n | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dst*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src1*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src2*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

XOR n bytes.

Parameters
:   | dst | Destination of where to store result. Shall be `len` bytes. |
    | --- | --- |
    | src1 | First source. Shall be `len` bytes. |
    | src2 | Second source. Shall be `len` bytes. |
    | len | Number of bytes to XOR. |

## [◆ ](#gabd42323692821c970e1038879f8f2f33)u8\_to\_dec()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) u8\_to\_dec | ( | char \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *buflen*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

`#include <[util.h](util_8h.md)>`

Convert a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) into a decimal string representation.

Convert a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value into its ASCII decimal string representation. The string is terminated if there is enough space in buf.

Parameters
:   | buf | Address of where to store the string representation. |
    | --- | --- |
    | buflen | Size of the storage area for string representation. |
    | value | The value to convert to decimal string |

Returns
:   The length of the converted string (excluding terminator if any), or 0 if an error occurred.

## [◆ ](#ga376935d7e6eece7dbdd382de057ec2f9)utf8\_lcpy()

| char \* utf8\_lcpy | ( | char \* | *dst*, |
| --- | --- | --- | --- |
|  |  | const char \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *n* ) |

`#include <[util.h](util_8h.md)>`

Copies a UTF-8 encoded string from `src` to `dst`.

The resulting `dst` will always be NULL terminated if `n` is larger than 0, and the `dst` string will always be properly UTF-8 truncated.

Parameters
:   | dst | The destination of the UTF-8 string. |
    | --- | --- |
    | src | The source string |
    | n | The size of the `dst` buffer. Maximum number of characters copied is `n` - 1. If 0 nothing will be done, and the `dst` will not be NULL terminated. |

Returns
:   Pointer to the `dst`

## [◆ ](#ga1bbcfa5d7bfe757afab489d2ce41e30a)utf8\_trunc()

| char \* utf8\_trunc | ( | char \* | *utf8\_str* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[util.h](util_8h.md)>`

Properly truncate a NULL-terminated UTF-8 string.

Take a NULL-terminated UTF-8 string and ensure that if the string has been truncated (by setting the NULL terminator) earlier by other means, that the string ends with a properly formatted UTF-8 character (1-4 bytes).

Example:
char test\_str[] = "€€€";
char trunc\_utf8[8];
printf("Original : %s\n", test\_str); // €€€
strncpy(trunc\_utf8, test\_str, sizeof(trunc\_utf8));
trunc\_utf8[sizeof(trunc\_utf8) - 1] = '\0';
printf("Bad : %s\n", trunc\_utf8); // €€�
utf8\_trunc(trunc\_utf8);
printf("Truncated: %s\n", trunc\_utf8); // €€

Parameters
:   | utf8\_str | NULL-terminated string |
    | --- | --- |

Returns
:   Pointer to the `utf8_str`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
