---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/grant__table_8h.html
original_path: doxygen/html/grant__table_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grant\_table.h File Reference

`#include "[xen.h](xen_8h_source.md)"`

[Go to the source code of this file.](grant__table_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [grant\_entry](structgrant__entry.md) |
| struct | [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) |
| struct | [gnttab\_unmap\_grant\_ref](structgnttab__unmap__grant__ref.md) |
| struct | [gnttab\_setup\_table](structgnttab__setup__table.md) |
| struct | [gnttab\_query\_size](structgnttab__query__size.md) |

| Macros | |
| --- | --- |
| #define | [grant\_entry\_v1](#ae42428f85f6f40af58ce52d7cbb9a7bc)   [grant\_entry](structgrant__entry.md) |
| #define | [grant\_entry\_v1\_t](#ad463d080d89bce70aa065aec9d62a69a)   [grant\_entry\_t](#aebf4abc7c6cd5ce259ff90a874648ea0) |
| #define | [GNTTAB\_NR\_RESERVED\_ENTRIES](#a3f007d8667fc2c664aaf30c70cfb4d40)   8 |
| #define | [GNTTAB\_RESERVED\_CONSOLE](#af66d8799c0f4320ced4788fe30527e6f)   0 |
| #define | [GNTTAB\_RESERVED\_XENSTORE](#a22163820f5f3fa6b8b80f54dc8f44ea7)   1 |
| #define | [GTF\_invalid](#a593da3ddbb1a89c6d5bac76cc0200aa3)   (0U << 0) |
| #define | [GTF\_permit\_access](#abae7c6625c8a57268e21b4ebccc24e42)   (1U << 0) |
| #define | [GTF\_accept\_transfer](#a3eaec7cfe8c1d8f10713872452d4ad2a)   (2U << 0) |
| #define | [GTF\_transitive](#aa3ed0b5c63d22ef4a430fb1598e7b26b)   (3U << 0) |
| #define | [GTF\_type\_mask](#ad8879d52107cc4b8f8a5624e1e0596b2)   (3U << 0) |
| #define | [GTF\_readonly](#ad63f8c1a78d72993230a38bf0629cbee)   (1U << \_GTF\_readonly) |
| #define | [GTF\_reading](#ae259cc06448990822e273039612f2577)   (1U << \_GTF\_reading) |
| #define | [GTF\_writing](#a9c49e42a4da40bca62a629e3fb84cfbf)   (1U << \_GTF\_writing) |
| #define | [GTF\_PWT](#a57cc188dc528a922f99a51ace84e381c)   (1U << \_GTF\_PWT) |
| #define | [GTF\_PCD](#a847aaa27483a22bc2f483175a0c84360)   (1U << \_GTF\_PCD) |
| #define | [GTF\_PAT](#ab9215b09013fc607a5b9b7ea14409f15)   (1U << \_GTF\_PAT) |
| #define | [GTF\_sub\_page](#aee57df4b4bf9c9711efbb0652a47d16b)   (1U << \_GTF\_sub\_page) |
| #define | [GTF\_transfer\_committed](#a3138f5333992b3ddd30297dcd3268350)   (1U << \_GTF\_transfer\_committed) |
| #define | [GTF\_transfer\_completed](#a093e8bcc1ff97e22f80fa4db38826783)   (1U << \_GTF\_transfer\_completed) |
| #define | [GNTTABOP\_map\_grant\_ref](#a0858861609126a45f682483cdb8c3c71)   0 |
| #define | [GNTTABOP\_unmap\_grant\_ref](#ae6b083e36a9b34bec9a00871ef2d8ba1)   1 |
| #define | [GNTTABOP\_setup\_table](#af3334c569ceddf0d578c11d5e3598e21)   2 |
| #define | [GNTTABOP\_dump\_table](#a36c577d4392ab9c2c0d0308ee511fe49)   3 |
| #define | [GNTTABOP\_transfer](#ac7ac76506dd75412a382b6255014a16d)   4 |
| #define | [GNTTABOP\_copy](#aedb6d63bc0e6fe8f2d34363dffbdc6a8)   5 |
| #define | [GNTTABOP\_query\_size](#af6e54f747b849e7c7466b4352c3ea18e)   6 |
| #define | [GNTTABOP\_unmap\_and\_replace](#aa2da39ca5f693bdbb024676a7d0093e9)   7 |
| #define | [GNTMAP\_device\_map](#aae559e2f8155b38e032db211f2fb89fd)   (1<<\_GNTMAP\_device\_map) |
| #define | [GNTMAP\_host\_map](#a12fced9de545a35fe5d8982e8da565e2)   (1<<\_GNTMAP\_host\_map) |
| #define | [GNTMAP\_readonly](#a00a2a7a5e3310500419b9cd0c765f268)   (1<<\_GNTMAP\_readonly) |
| #define | [GNTMAP\_application\_map](#acd1b7e44453bd81909a756e5dd2929d6)   (1<<\_GNTMAP\_application\_map) |
| #define | [GNTMAP\_contains\_pte](#a97e8e1150ee8ae0c6cf9101dd98f8f3d)   (1<<\_GNTMAP\_contains\_pte) |
| #define | [GNTMAP\_guest\_avail\_mask](#ac4d9a6ba14cb3fe5b1a7daa035e6c84e)   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))~0 << \_GNTMAP\_guest\_avail0) |
| #define | [GNTST\_okay](#a8b346596e565a7bfcc84c43dad1b5b4e)   (0) /\* Normal return \*/ |
| #define | [GNTST\_general\_error](#a0f4d62b7f6986db7f1565c4842d44c2c)   (-1) /\* General undefined error \*/ |
| #define | [GNTST\_bad\_domain](#acef8aeb07dfd790b304aee2b8037388d)   (-2) /\* Unrecognsed domain id \*/ |
| #define | [GNTST\_bad\_gntref](#aa95a512fed439a4d77d6b0fea66e7e34)   (-3) /\* Unrecognised or inappropriate gntref \*/ |
| #define | [GNTST\_bad\_handle](#afb88ba813ad01e706cfadf4d44a4e941)   (-4) /\* Unrecognised or inappropriate handle \*/ |
| #define | [GNTST\_bad\_virt\_addr](#a8edfdaba9b072bab54894601f5e53157)   (-5) /\* Inappropriate virtual address to map \*/ |
| #define | [GNTST\_bad\_dev\_addr](#a759747d060b61d7b0c8dbe2bd1772f73)   (-6) /\* Inappropriate [device](structdevice.md) address to unmap \*/ |
| #define | [GNTST\_no\_device\_space](#a12d565fb321125c35c26b6c580bf778a)   (-7) /\* Out of space in I/O MMU \*/ |
| #define | [GNTST\_permission\_denied](#aab89203e7f7f4d18b999ba49167595ae)   (-8) /\* Not enough privilege for operation \*/ |
| #define | [GNTST\_bad\_page](#a669e9b8bed7a88bf0d2f09e5e6a6b011)   (-9) /\* Specified page was invalid for op \*/ |
| #define | [GNTST\_bad\_copy\_arg](#a6e675b4ef4a1477c9b4c6e29a207c900)   (-10) /\* copy arguments cross page boundary \*/ |
| #define | [GNTST\_address\_too\_big](#a514d6b98e5285c4e098aafebddb2597c)   (-11) /\* transfer page address too large \*/ |
| #define | [GNTST\_eagain](#aa6dd5fbc418afb794115441ba78ba92f)   (-12) /\* Operation not done; try again \*/ |
| #define | [GNTTABOP\_error\_msgs](#a164e86151574733f6739c37c8f6b9f70) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [grant\_ref\_t](#aee25f6c8ecefd1d7c52e49e4886aca3e) |
| typedef struct [grant\_entry](structgrant__entry.md) | [grant\_entry\_t](#aebf4abc7c6cd5ce259ff90a874648ea0) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [grant\_handle\_t](#a1eade3c86c0fd0e71217eefaa3b38cd1) |
| typedef struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) | [gnttab\_map\_grant\_ref\_t](#ac6ace01635e3b886a7f74d4e9ae3db78) |
| typedef struct [gnttab\_unmap\_grant\_ref](structgnttab__unmap__grant__ref.md) | [gnttab\_unmap\_grant\_ref\_t](#ab6f946404db417d188cafe0f68580130) |
| typedef struct [gnttab\_setup\_table](structgnttab__setup__table.md) | [gnttab\_setup\_table\_t](#ab7eab2489bbe46dec87a6b8d88ad41f9) |
| typedef struct [gnttab\_query\_size](structgnttab__query__size.md) | [gnttab\_query\_size\_t](#a57729fc78a303aaa52994b1c8893d605) |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a01396c3aadef6f69b8c03735840c8bb9) ([gnttab\_map\_grant\_ref\_t](#ac6ace01635e3b886a7f74d4e9ae3db78)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a35aae9b9d970900cb87ff8ebfc5b720e) ([gnttab\_unmap\_grant\_ref\_t](#ab6f946404db417d188cafe0f68580130)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a58aa81b1014416c6f7665e51c348d015) ([gnttab\_setup\_table\_t](#ab7eab2489bbe46dec87a6b8d88ad41f9)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a729433b8b0944774b0f1e08c99e233ab) ([gnttab\_query\_size\_t](#a57729fc78a303aaa52994b1c8893d605)) |

## Macro Definition Documentation

## [◆ ](#acd1b7e44453bd81909a756e5dd2929d6)GNTMAP\_application\_map

| #define GNTMAP\_application\_map   (1<<\_GNTMAP\_application\_map) |
| --- |

## [◆ ](#a97e8e1150ee8ae0c6cf9101dd98f8f3d)GNTMAP\_contains\_pte

| #define GNTMAP\_contains\_pte   (1<<\_GNTMAP\_contains\_pte) |
| --- |

## [◆ ](#aae559e2f8155b38e032db211f2fb89fd)GNTMAP\_device\_map

| #define GNTMAP\_device\_map   (1<<\_GNTMAP\_device\_map) |
| --- |

## [◆ ](#ac4d9a6ba14cb3fe5b1a7daa035e6c84e)GNTMAP\_guest\_avail\_mask

| #define GNTMAP\_guest\_avail\_mask   (([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))~0 << \_GNTMAP\_guest\_avail0) |
| --- |

## [◆ ](#a12fced9de545a35fe5d8982e8da565e2)GNTMAP\_host\_map

| #define GNTMAP\_host\_map   (1<<\_GNTMAP\_host\_map) |
| --- |

## [◆ ](#a00a2a7a5e3310500419b9cd0c765f268)GNTMAP\_readonly

| #define GNTMAP\_readonly   (1<<\_GNTMAP\_readonly) |
| --- |

## [◆ ](#a514d6b98e5285c4e098aafebddb2597c)GNTST\_address\_too\_big

| #define GNTST\_address\_too\_big   (-11) /\* transfer page address too large \*/ |
| --- |

## [◆ ](#a6e675b4ef4a1477c9b4c6e29a207c900)GNTST\_bad\_copy\_arg

| #define GNTST\_bad\_copy\_arg   (-10) /\* copy arguments cross page boundary \*/ |
| --- |

## [◆ ](#a759747d060b61d7b0c8dbe2bd1772f73)GNTST\_bad\_dev\_addr

| #define GNTST\_bad\_dev\_addr   (-6) /\* Inappropriate [device](structdevice.md) address to unmap \*/ |
| --- |

## [◆ ](#acef8aeb07dfd790b304aee2b8037388d)GNTST\_bad\_domain

| #define GNTST\_bad\_domain   (-2) /\* Unrecognsed domain id \*/ |
| --- |

## [◆ ](#aa95a512fed439a4d77d6b0fea66e7e34)GNTST\_bad\_gntref

| #define GNTST\_bad\_gntref   (-3) /\* Unrecognised or inappropriate gntref \*/ |
| --- |

## [◆ ](#afb88ba813ad01e706cfadf4d44a4e941)GNTST\_bad\_handle

| #define GNTST\_bad\_handle   (-4) /\* Unrecognised or inappropriate handle \*/ |
| --- |

## [◆ ](#a669e9b8bed7a88bf0d2f09e5e6a6b011)GNTST\_bad\_page

| #define GNTST\_bad\_page   (-9) /\* Specified page was invalid for op \*/ |
| --- |

## [◆ ](#a8edfdaba9b072bab54894601f5e53157)GNTST\_bad\_virt\_addr

| #define GNTST\_bad\_virt\_addr   (-5) /\* Inappropriate virtual address to map \*/ |
| --- |

## [◆ ](#aa6dd5fbc418afb794115441ba78ba92f)GNTST\_eagain

| #define GNTST\_eagain   (-12) /\* Operation not done; try again \*/ |
| --- |

## [◆ ](#a0f4d62b7f6986db7f1565c4842d44c2c)GNTST\_general\_error

| #define GNTST\_general\_error   (-1) /\* General undefined error \*/ |
| --- |

## [◆ ](#a12d565fb321125c35c26b6c580bf778a)GNTST\_no\_device\_space

| #define GNTST\_no\_device\_space   (-7) /\* Out of space in I/O MMU \*/ |
| --- |

## [◆ ](#a8b346596e565a7bfcc84c43dad1b5b4e)GNTST\_okay

| #define GNTST\_okay   (0) /\* Normal return \*/ |
| --- |

## [◆ ](#aab89203e7f7f4d18b999ba49167595ae)GNTST\_permission\_denied

| #define GNTST\_permission\_denied   (-8) /\* Not enough privilege for operation \*/ |
| --- |

## [◆ ](#a3f007d8667fc2c664aaf30c70cfb4d40)GNTTAB\_NR\_RESERVED\_ENTRIES

| #define GNTTAB\_NR\_RESERVED\_ENTRIES   8 |
| --- |

## [◆ ](#af66d8799c0f4320ced4788fe30527e6f)GNTTAB\_RESERVED\_CONSOLE

| #define GNTTAB\_RESERVED\_CONSOLE   0 |
| --- |

## [◆ ](#a22163820f5f3fa6b8b80f54dc8f44ea7)GNTTAB\_RESERVED\_XENSTORE

| #define GNTTAB\_RESERVED\_XENSTORE   1 |
| --- |

## [◆ ](#aedb6d63bc0e6fe8f2d34363dffbdc6a8)GNTTABOP\_copy

| #define GNTTABOP\_copy   5 |
| --- |

## [◆ ](#a36c577d4392ab9c2c0d0308ee511fe49)GNTTABOP\_dump\_table

| #define GNTTABOP\_dump\_table   3 |
| --- |

## [◆ ](#a164e86151574733f6739c37c8f6b9f70)GNTTABOP\_error\_msgs

| #define GNTTABOP\_error\_msgs |
| --- |

**Value:**

{ \

"okay", \

"undefined error", \

"unrecognised domain id", \

"invalid grant reference", \

"invalid mapping handle", \

"invalid virtual address", \

"invalid device address", \

"no spare translation slot in the I/O MMU", \

"permission denied", \

"bad page", \

"copy arguments cross page boundary", \

"page address size too large", \

"operation not done; try again" \

}

## [◆ ](#a0858861609126a45f682483cdb8c3c71)GNTTABOP\_map\_grant\_ref

| #define GNTTABOP\_map\_grant\_ref   0 |
| --- |

## [◆ ](#af6e54f747b849e7c7466b4352c3ea18e)GNTTABOP\_query\_size

| #define GNTTABOP\_query\_size   6 |
| --- |

## [◆ ](#af3334c569ceddf0d578c11d5e3598e21)GNTTABOP\_setup\_table

| #define GNTTABOP\_setup\_table   2 |
| --- |

## [◆ ](#ac7ac76506dd75412a382b6255014a16d)GNTTABOP\_transfer

| #define GNTTABOP\_transfer   4 |
| --- |

## [◆ ](#aa2da39ca5f693bdbb024676a7d0093e9)GNTTABOP\_unmap\_and\_replace

| #define GNTTABOP\_unmap\_and\_replace   7 |
| --- |

## [◆ ](#ae6b083e36a9b34bec9a00871ef2d8ba1)GNTTABOP\_unmap\_grant\_ref

| #define GNTTABOP\_unmap\_grant\_ref   1 |
| --- |

## [◆ ](#ae42428f85f6f40af58ce52d7cbb9a7bc)grant\_entry\_v1

| #define grant\_entry\_v1   [grant\_entry](structgrant__entry.md) |
| --- |

## [◆ ](#ad463d080d89bce70aa065aec9d62a69a)grant\_entry\_v1\_t

| #define grant\_entry\_v1\_t   [grant\_entry\_t](#aebf4abc7c6cd5ce259ff90a874648ea0) |
| --- |

## [◆ ](#a3eaec7cfe8c1d8f10713872452d4ad2a)GTF\_accept\_transfer

| #define GTF\_accept\_transfer   (2U << 0) |
| --- |

## [◆ ](#a593da3ddbb1a89c6d5bac76cc0200aa3)GTF\_invalid

| #define GTF\_invalid   (0U << 0) |
| --- |

## [◆ ](#ab9215b09013fc607a5b9b7ea14409f15)GTF\_PAT

| #define GTF\_PAT   (1U << \_GTF\_PAT) |
| --- |

## [◆ ](#a847aaa27483a22bc2f483175a0c84360)GTF\_PCD

| #define GTF\_PCD   (1U << \_GTF\_PCD) |
| --- |

## [◆ ](#abae7c6625c8a57268e21b4ebccc24e42)GTF\_permit\_access

| #define GTF\_permit\_access   (1U << 0) |
| --- |

## [◆ ](#a57cc188dc528a922f99a51ace84e381c)GTF\_PWT

| #define GTF\_PWT   (1U << \_GTF\_PWT) |
| --- |

## [◆ ](#ae259cc06448990822e273039612f2577)GTF\_reading

| #define GTF\_reading   (1U << \_GTF\_reading) |
| --- |

## [◆ ](#ad63f8c1a78d72993230a38bf0629cbee)GTF\_readonly

| #define GTF\_readonly   (1U << \_GTF\_readonly) |
| --- |

## [◆ ](#aee57df4b4bf9c9711efbb0652a47d16b)GTF\_sub\_page

| #define GTF\_sub\_page   (1U << \_GTF\_sub\_page) |
| --- |

## [◆ ](#a3138f5333992b3ddd30297dcd3268350)GTF\_transfer\_committed

| #define GTF\_transfer\_committed   (1U << \_GTF\_transfer\_committed) |
| --- |

## [◆ ](#a093e8bcc1ff97e22f80fa4db38826783)GTF\_transfer\_completed

| #define GTF\_transfer\_completed   (1U << \_GTF\_transfer\_completed) |
| --- |

## [◆ ](#aa3ed0b5c63d22ef4a430fb1598e7b26b)GTF\_transitive

| #define GTF\_transitive   (3U << 0) |
| --- |

## [◆ ](#ad8879d52107cc4b8f8a5624e1e0596b2)GTF\_type\_mask

| #define GTF\_type\_mask   (3U << 0) |
| --- |

## [◆ ](#a9c49e42a4da40bca62a629e3fb84cfbf)GTF\_writing

| #define GTF\_writing   (1U << \_GTF\_writing) |
| --- |

## Typedef Documentation

## [◆ ](#ac6ace01635e3b886a7f74d4e9ae3db78)gnttab\_map\_grant\_ref\_t

| typedef struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) [gnttab\_map\_grant\_ref\_t](#ac6ace01635e3b886a7f74d4e9ae3db78) |
| --- |

## [◆ ](#a57729fc78a303aaa52994b1c8893d605)gnttab\_query\_size\_t

| typedef struct [gnttab\_query\_size](structgnttab__query__size.md) [gnttab\_query\_size\_t](#a57729fc78a303aaa52994b1c8893d605) |
| --- |

## [◆ ](#ab7eab2489bbe46dec87a6b8d88ad41f9)gnttab\_setup\_table\_t

| typedef struct [gnttab\_setup\_table](structgnttab__setup__table.md) [gnttab\_setup\_table\_t](#ab7eab2489bbe46dec87a6b8d88ad41f9) |
| --- |

## [◆ ](#ab6f946404db417d188cafe0f68580130)gnttab\_unmap\_grant\_ref\_t

| typedef struct [gnttab\_unmap\_grant\_ref](structgnttab__unmap__grant__ref.md) [gnttab\_unmap\_grant\_ref\_t](#ab6f946404db417d188cafe0f68580130) |
| --- |

## [◆ ](#aebf4abc7c6cd5ce259ff90a874648ea0)grant\_entry\_t

| typedef struct [grant\_entry](structgrant__entry.md) [grant\_entry\_t](#aebf4abc7c6cd5ce259ff90a874648ea0) |
| --- |

## [◆ ](#a1eade3c86c0fd0e71217eefaa3b38cd1)grant\_handle\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [grant\_handle\_t](#a1eade3c86c0fd0e71217eefaa3b38cd1) |
| --- |

## [◆ ](#aee25f6c8ecefd1d7c52e49e4886aca3e)grant\_ref\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [grant\_ref\_t](#aee25f6c8ecefd1d7c52e49e4886aca3e) |
| --- |

## Function Documentation

## [◆ ](#a01396c3aadef6f69b8c03735840c8bb9)DEFINE\_XEN\_GUEST\_HANDLE() [1/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [gnttab\_map\_grant\_ref\_t](#ac6ace01635e3b886a7f74d4e9ae3db78) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a729433b8b0944774b0f1e08c99e233ab)DEFINE\_XEN\_GUEST\_HANDLE() [2/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [gnttab\_query\_size\_t](#a57729fc78a303aaa52994b1c8893d605) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a58aa81b1014416c6f7665e51c348d015)DEFINE\_XEN\_GUEST\_HANDLE() [3/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [gnttab\_setup\_table\_t](#ab7eab2489bbe46dec87a6b8d88ad41f9) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a35aae9b9d970900cb87ff8ebfc5b720e)DEFINE\_XEN\_GUEST\_HANDLE() [4/4]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [gnttab\_unmap\_grant\_ref\_t](#ab6f946404db417d188cafe0f68580130) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [grant\_table.h](grant__table_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
