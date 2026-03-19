---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sys_2util_8h.html
original_path: doxygen/html/sys_2util_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util.h File Reference

Misc utilities.
[More...](#details)

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/time_units.h](time__units_8h_source.md)>`

[Go to the source code of this file.](sys_2util_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NUM\_BITS](#afa27c06d0ad6b949289431ad75f104ab)(t) |
|  | Number of bits that make up a type. |
| #define | [POINTER\_TO\_UINT](group__sys-util.md#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(x) |
|  | Cast `x`, a pointer, to an unsigned integer. |
| #define | [UINT\_TO\_POINTER](group__sys-util.md#gab74ce0513c348e0b257d38473e77e1a1)(x) |
|  | Cast `x`, an unsigned integer, to a void\*. |
| #define | [POINTER\_TO\_INT](group__sys-util.md#ga6e5ec9c46d0140315a7c1d80d1cc3c38)(x) |
|  | Cast `x`, a pointer, to a signed integer. |
| #define | [INT\_TO\_POINTER](group__sys-util.md#gae236ed18fe2ff18ab47c15d2e7eeb417)(x) |
|  | Cast `x`, a signed integer, to a void\*. |
| #define | [BITS\_PER\_BYTE](group__sys-util.md#ga369ecd38b3ab077fc235f892354bb46f)   (\_\_CHAR\_BIT\_\_) |
|  | Number of bits in a byte. |
| #define | [BITS\_PER\_NIBBLE](group__sys-util.md#gae162e1c2f985d37fff7d41f42ed65a6e)   (\_\_CHAR\_BIT\_\_ / 2) |
|  | Number of bits in a nibble. |
| #define | [NIBBLES\_PER\_BYTE](group__sys-util.md#ga310d08124d6b119af05d75fe0ec0eb8c)   ([BITS\_PER\_BYTE](group__sys-util.md#ga369ecd38b3ab077fc235f892354bb46f) / [BITS\_PER\_NIBBLE](group__sys-util.md#gae162e1c2f985d37fff7d41f42ed65a6e)) |
|  | Number of nibbles in a byte. |
| #define | [BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)   (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_\_) |
|  | Number of bits in a long int. |
| #define | [BITS\_PER\_LONG\_LONG](group__sys-util.md#gaeb3fa0f8ac477da6575363a158f36891)   (\_\_CHAR\_BIT\_\_ \* \_\_SIZEOF\_LONG\_LONG\_\_) |
|  | Number of bits in a long long int. |
| #define | [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(h, l) |
|  | Create a contiguous bitmask starting at bit position `l` and ending at position `h`. |
| #define | [GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(h, l) |
|  | Create a contiguous 64-bit bitmask starting at bit position `l` and ending at position `h`. |
| #define | [ZERO\_OR\_COMPILE\_ERROR](group__sys-util.md#ga831cb8468911b8ebdb9b42682778e53d)(cond) |
|  | 0 if `cond` is true-ish; causes a compile error otherwise. |
| #define | [IS\_ARRAY](group__sys-util.md#gaa0be479debd8300ab6b43f4d028ab5da)(array) |
|  | Zero if `array` has an array type, a compile error otherwise. |
| #define | [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(array) |
|  | Number of elements in the given `array`. |
| #define | [FLEXIBLE\_ARRAY\_DECLARE](group__sys-util.md#gac36718df45178ad9de50f6e0b8d75d7e)(type, name) |
|  | Declare a flexible array member. |
| #define | [IS\_ARRAY\_ELEMENT](group__sys-util.md#gad403257ac6868c8bf3415ae771ce0a04)(array, ptr) |
|  | Whether `ptr` is an element of `array`. |
| #define | [ARRAY\_INDEX](group__sys-util.md#ga27c31909224761e41d77118b41212d6b)(array, ptr) |
|  | Index of `ptr` within `array`. |
| #define | [PART\_OF\_ARRAY](group__sys-util.md#ga4fbecf59c021cb60fa1267b7818f90ef)(array, ptr) |
|  | Check if a pointer `ptr` lies within `array`. |
| #define | [ARRAY\_INDEX\_FLOOR](group__sys-util.md#gae0516bf7a39795bcc6f0dfbf3a180c05)(array, ptr) |
|  | Array-index of `ptr` within `array`, rounded down. |
| #define | [ARRAY\_FOR\_EACH](group__sys-util.md#ga7a1647a1d17185f9438ed0e3096e68bc)(array, idx) |
|  | Iterate over members of an array using an index variable. |
| #define | [ARRAY\_FOR\_EACH\_PTR](group__sys-util.md#gafd9d42bbb945424f11b7b023dfd519f9)(array, ptr) |
|  | Iterate over members of an array using a pointer. |
| #define | [SAME\_TYPE](group__sys-util.md#ga78e587047fe4af679141595363c07179)(a, b) |
|  | Validate if two entities have a compatible type. |
| #define | [CONTAINER\_OF\_VALIDATE](group__sys-util.md#gaf2279c11f90f7461a417f9646af7dc5c)(ptr, type, field) |
|  | Validate CONTAINER\_OF parameters, only applies to C mode. |
| #define | [CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(ptr, type, field) |
|  | Get a pointer to a structure containing the element. |
| #define | [SIZEOF\_FIELD](group__sys-util.md#ga78c188c333605984c4c83f80d15092a4)(type, member) |
|  | Report the size of a struct field in bytes. |
| #define | [CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(...) |
|  | Concatenate input arguments. |
| #define | [IS\_ALIGNED](group__sys-util.md#gabf601ce26a569512a4e422a074934660)(ptr, align) |
|  | Check if `ptr` is aligned to `align` alignment. |
| #define | [ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(x, align) |
|  | Value of `x` rounded up to the next multiple of `align`. |
| #define | [ROUND\_DOWN](group__sys-util.md#gad8d2389dbe7ea135eccf237dbafb76dd)(x, align) |
|  | Value of `x` rounded down to the previous multiple of `align`. |
| #define | [WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(x) |
|  | Value of `x` rounded up to the next word boundary. |
| #define | [WB\_DN](group__sys-util.md#gadbc789ee99633a92584387ba2a4f7052)(x) |
|  | Value of `x` rounded down to the previous word boundary. |
| #define | [DIV\_ROUND\_UP](group__sys-util.md#gae664e7492e37d324831caf2321ddda37)(n, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Divide and round up. |
| #define | [DIV\_ROUND\_CLOSEST](group__sys-util.md#ga57fc13eb777500b3e22d3ff457cfd0d7)(n, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Divide and round to the nearest integer. |
| #define | [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)(a, b) |
|  | Obtain the maximum of two values. |
| #define | [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(a, b) |
|  | Obtain the minimum of two values. |
| #define | [CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(val, low, high) |
|  | Clamp a value to a given range. |
| #define | [IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)(val, min, max) |
|  | Checks if a value is within range. |
| #define | [LOG2](group__sys-util.md#ga40805b5dd56ee36df59a7bbe403ddf33)(x) |
|  | Compute log2(x). |
| #define | [LOG2CEIL](group__sys-util.md#gada629edfcec9fa2fc3dc5d7af70abb03)(x) |
|  | Compute ceil(log2(x)). |
| #define | [NHPOT](group__sys-util.md#ga2ab444fed50a82cc1fe0e952fd03127d)(x) |
|  | Compute next highest power of two. |
| #define | [KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)(x) |
|  | Number of bytes in `x` kibibytes. |
| #define | [MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)(x) |
|  | Number of bytes in `x` mebibytes. |
| #define | [GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)(x) |
|  | Number of bytes in `x` gibibytes. |
| #define | [KHZ](group__sys-util.md#gaee55275295c076c6d23c994777623253)(x) |
|  | Number of Hz in `x` kHz. |
| #define | [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(x) |
|  | Number of Hz in `x` MHz. |
| #define | [WAIT\_FOR](group__sys-util.md#ga68eb35df6b4715714312df90209accee)(expr, timeout, delay\_stmt) |
|  | Wait for an expression to return true with a timeout. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_power\_of\_two](group__sys-util.md#gadfe7046eb6c39bb3c84c18d8ac7a230e) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int x) |
|  | Is `x` a power of two? |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_null\_no\_warn](group__sys-util.md#ga611e5bb95e5b4d490a33b9025791d366) (void \*p) |
|  | Is `p` equal to NULL? |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [arithmetic\_shift\_right](group__sys-util.md#ga1ffeb18b8ed73d37c2485c82988ed1ec) ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shift) |
|  | Arithmetic shift right. |
| static void | [bytecpy](group__sys-util.md#ga3379c356de17dbeebfa7588d8c964d5e) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | byte by byte memcpy. |
| static void | [byteswp](group__sys-util.md#ga8624d1e5411703deac1ab8517f132d7b) (void \*a, void \*b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | byte by byte swap. |
| int | [char2hex](group__sys-util.md#gaaf91757f6fe86ab417536d5066ce14e6) (char c, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*x) |
|  | Convert a single character into a hexadecimal nibble. |
| int | [hex2char](group__sys-util.md#ga9ed3bd04d5c0797aebf333733913028c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) x, char \*c) |
|  | Convert a single hexadecimal nibble into a character. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bin2hex](group__sys-util.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen, char \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen) |
|  | Convert a binary array into string representation. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [hex2bin](group__sys-util.md#ga269a01ffa3f1a3485b79d8a54a78a3f1) (const char \*hex, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) hexlen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Convert a hexadecimal string into a binary array. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcd2bin](group__sys-util.md#gaa0f77b877eb5db5a228b79cba110abe4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bcd) |
|  | Convert a binary coded decimal (BCD 8421) value to binary. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bin2bcd](group__sys-util.md#ga6dff7f443aa795258c64cee63b29b591) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bin) |
|  | Convert a binary value to binary coded decimal (BCD 8421). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [u8\_to\_dec](group__sys-util.md#gabd42323692821c970e1038879f8f2f33) (char \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buflen, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Convert a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) into a decimal string representation. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [sign\_extend](group__sys-util.md#gae157c78412a9d4b5b2dbcee3b3104aee) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Sign extend an 8, 16 or 32 bit value using the index bit as sign bit. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [sign\_extend\_64](group__sys-util.md#ga0ba9d4ab383eba522e345594aaa2bb3f) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Sign extend a 64 bit value using the index bit as sign bit. |
| char \* | [utf8\_trunc](group__sys-util.md#ga1bbcfa5d7bfe757afab489d2ce41e30a) (char \*utf8\_str) |
|  | Properly truncate a NULL-terminated UTF-8 string. |
| char \* | [utf8\_lcpy](group__sys-util.md#ga376935d7e6eece7dbdd382de057ec2f9) (char \*dst, const char \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | Copies a UTF-8 encoded string from `src` to `dst`. |
| static void | [mem\_xor\_n](group__sys-util.md#ga8a9d63740a8718de8ab0ce057cfbd4f4) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src1, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src2, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | XOR n bytes. |
| static void | [mem\_xor\_32](group__sys-util.md#ga6f1717e3eeb4a91afa2be14061d52203) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[4], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[4]) |
|  | XOR 32 bits. |
| static void | [mem\_xor\_128](group__sys-util.md#ga64037dd6934130ca6a6dc3e5357b9743) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src1[16], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src2[16]) |
|  | XOR 128 bits. |

## Detailed Description

Misc utilities.

Misc utilities usable by the kernel and application code.

## Macro Definition Documentation

## [◆ ](#afa27c06d0ad6b949289431ad75f104ab)NUM\_BITS

| #define NUM\_BITS | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(sizeof(t) \* 8)

Number of bits that make up a type.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [util.h](sys_2util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
