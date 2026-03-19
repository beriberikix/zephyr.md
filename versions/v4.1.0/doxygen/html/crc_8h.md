---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/crc_8h.html
original_path: doxygen/html/crc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

crc.h File Reference

CRC computation function.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`

[Go to the source code of this file.](crc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CRC8\_CCITT\_INITIAL\_VALUE](#a95b298c826cf96507e7b11a49c75b2cf)   0xFF |
| #define | [CRC8\_ROHC\_INITIAL\_VALUE](#a81e9e87b5f1705b252429981f49608ee)   0xFF |
| #define | [CRC24\_PGP\_INITIAL\_VALUE](#a0f92c37af2ac3af5cbea2c2f259d0639)   0x00B704CEU |
| #define | [CRC24\_FINAL\_VALUE\_MASK](#a9075e7134000a6fd75ea81b0c2b0218b)   0x00FFFFFFU |

| Enumerations | |
| --- | --- |
| enum | [crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) {     [CRC4](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) , [CRC4\_TI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f) , [CRC7\_BE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a) , [CRC8](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) ,     [CRC8\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb) , [CRC8\_ROHC](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5) , [CRC16](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) , [CRC16\_ANSI](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) ,     [CRC16\_CCITT](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30) , [CRC16\_ITU\_T](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c) , [CRC24\_PGP](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43) , [CRC32\_C](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148) ,     [CRC32\_IEEE](group__crc.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8)   } |
|  | CRC algorithm enumeration. [More...](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) |

| Functions | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16](group__crc.md#ga204a779aa0c1a152763ea8edc6fc3a8c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generic function for computing a CRC-16 without input or output reflection. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_reflect](group__crc.md#gaccbcb5b80cf8deaac252474ecc6d9914) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generic function for computing a CRC-16 with input and output reflection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8](group__crc.md#gaa614e73ee7484ca0424fa7d14a54bbb6) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reversed) |
|  | Generic function for computing CRC 8. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_ccitt](group__crc.md#ga74fa5608612c629291d15bc00b1c411c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the checksum of a buffer with polynomial 0x1021, reflecting input and output. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_itu\_t](group__crc.md#ga5502729e443496719de338e8b6692ac1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the checksum of a buffer with polynomial 0x1021, no reflection of input or output. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_ansi](group__crc.md#gaac3ac50c029b656f5cc070e6c742601a) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the ANSI (or Modbus) variant of CRC-16. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc32\_ieee](group__crc.md#gafc24e79ed7f978f5bb813091ef318982) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generate IEEE conform CRC32 checksum. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc32\_ieee\_update](group__crc.md#ga17476d4af14603e322986ef603ce8530) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Update an IEEE conforming CRC32 checksum. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc32\_c](group__crc.md#ga88d510b3958aee0990ca345aba260bc1) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) first\_pkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_pkt) |
|  | Calculate CRC32C (Castagnoli) checksum. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8\_ccitt](group__crc.md#ga9a925de71cd0255a22c769dc4b130da5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute CCITT variant of CRC 8. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8\_rohc](group__crc.md#ga7a8f4387a2d0163165557446d018f041) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute ROHC variant of CRC 8. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc7\_be](group__crc.md#ga1169005fd900b2787035044eeea38af1) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the CRC-7 checksum of a buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc4\_ti](group__crc.md#ga322365098ec65bde3d55b0c059896668) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the CRC-4 checksum of a buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc4](group__crc.md#ga4458d7743f9a3394fb68cddcc100e456) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reversed) |
|  | Generic function for computing CRC 4. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc24\_pgp](group__crc.md#gaebe7a9494dec69568b4f5cc95bf0fac2) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generate an OpenPGP CRC-24 checksum as defined in RFC 4880 section 6.1. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc24\_pgp\_update](group__crc.md#ga4523b3cf8dbc05ea44258d1652fbb969) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Update an OpenPGP CRC-24 checksum. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc\_by\_type](group__crc.md#ga5d7f493210e56fb18b8199c9d8a17f33) (enum [crc\_type](group__crc.md#gabc40e4ffd6da1175eb8ee8573a527edd) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seed, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) poly, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reflect, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) first, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last) |
|  | Compute a CRC checksum, in a generic way. |

## Detailed Description

CRC computation function.

## Macro Definition Documentation

## [◆ ](#a9075e7134000a6fd75ea81b0c2b0218b)CRC24\_FINAL\_VALUE\_MASK

| #define CRC24\_FINAL\_VALUE\_MASK   0x00FFFFFFU |
| --- |

## [◆ ](#a0f92c37af2ac3af5cbea2c2f259d0639)CRC24\_PGP\_INITIAL\_VALUE

| #define CRC24\_PGP\_INITIAL\_VALUE   0x00B704CEU |
| --- |

## [◆ ](#a95b298c826cf96507e7b11a49c75b2cf)CRC8\_CCITT\_INITIAL\_VALUE

| #define CRC8\_CCITT\_INITIAL\_VALUE   0xFF |
| --- |

## [◆ ](#a81e9e87b5f1705b252429981f49608ee)CRC8\_ROHC\_INITIAL\_VALUE

| #define CRC8\_ROHC\_INITIAL\_VALUE   0xFF |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [crc.h](crc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
