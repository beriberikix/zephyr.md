---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/4_2arm__mmu_8h.html
original_path: doxygen/html/4_2arm__mmu_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mmu.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`

[Go to the source code of this file.](4_2arm__mmu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_mmu\_region](structarm__mmu__region.md) |
| struct | [arm\_mmu\_config](structarm__mmu__config.md) |
| struct | [arm\_mmu\_ptables](structarm__mmu__ptables.md) |
| struct | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) |

| Macros | |
| --- | --- |
| #define | [MT\_TYPE\_MASK](#aac0064c36c372d9a62d3a7a4fa8dc72c)   0x7U |
| #define | [MT\_TYPE](#a9018634e807aa322da516bb70b9c5e3e)(attr) |
| #define | [MT\_DEVICE\_nGnRnE](#a362a80b5a2f87e888d742ac4b1e8d7e1)   0U |
| #define | [MT\_DEVICE\_nGnRE](#afb3dda3d3a2b1a147be7ee58366e3f87)   1U |
| #define | [MT\_DEVICE\_GRE](#ada441c0a6171dce9eef0875593ba5e56)   2U |
| #define | [MT\_NORMAL\_NC](#a1a41f294343c4fcb9741c693fc107601)   3U |
| #define | [MT\_NORMAL](#a8b006dab179dfa8965dcef3ac302746d)   4U |
| #define | [MT\_NORMAL\_WT](#ad70c105c395f996ddd2628686e4e956f)   5U |
| #define | [MEMORY\_ATTRIBUTES](#a8b7a2f1ea804a163917486b5e3d2a70a) |
| #define | [MT\_PERM\_SHIFT](#a4796895c7c90277cd1eae3c34fecd96c)   3U |
| #define | [MT\_SEC\_SHIFT](#a4e94c3f3e790bb5c1afaa6ffa1094c8d)   4U |
| #define | [MT\_P\_EXECUTE\_SHIFT](#ac01ddafde6fbc038bfa5994b7335429c)   5U |
| #define | [MT\_U\_EXECUTE\_SHIFT](#a431b40e024ff711208e286a68cc4a88a)   6U |
| #define | [MT\_RW\_AP\_SHIFT](#afe1e276059306bc596102d8cc0eb0db6)   7U |
| #define | [MT\_NO\_OVERWRITE\_SHIFT](#a099fcd188b2d8cb542ead3aff617632c)   8U |
| #define | [MT\_NON\_GLOBAL\_SHIFT](#affc55d3de67afeb18b29b2e4070b12e0)   9U |
| #define | [MT\_RO](#a596089f139287e4696c2fe9c9add4074)   (0U << [MT\_PERM\_SHIFT](#a4796895c7c90277cd1eae3c34fecd96c)) |
| #define | [MT\_RW](#a2f968826efe83004f350f2264fc5b192)   (1U << [MT\_PERM\_SHIFT](#a4796895c7c90277cd1eae3c34fecd96c)) |
| #define | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973)   (1U << [MT\_RW\_AP\_SHIFT](#afe1e276059306bc596102d8cc0eb0db6)) |
| #define | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f)   (0U << [MT\_RW\_AP\_SHIFT](#afe1e276059306bc596102d8cc0eb0db6)) |
| #define | [MT\_SECURE](#a9a2ae47063f7f1b105796d5e3114118f)   (0U << [MT\_SEC\_SHIFT](#a4e94c3f3e790bb5c1afaa6ffa1094c8d)) |
| #define | [MT\_NS](#a2b0dcb4b334e2fd3eb31eb7451dfc005)   (1U << [MT\_SEC\_SHIFT](#a4e94c3f3e790bb5c1afaa6ffa1094c8d)) |
| #define | [MT\_P\_EXECUTE](#a465cd6685380ff25b2223b19844d730a)   (0U << [MT\_P\_EXECUTE\_SHIFT](#ac01ddafde6fbc038bfa5994b7335429c)) |
| #define | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c)   (1U << [MT\_P\_EXECUTE\_SHIFT](#ac01ddafde6fbc038bfa5994b7335429c)) |
| #define | [MT\_U\_EXECUTE](#a5826032cb5c39b30b5727214c0856472)   (0U << [MT\_U\_EXECUTE\_SHIFT](#a431b40e024ff711208e286a68cc4a88a)) |
| #define | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)   (1U << [MT\_U\_EXECUTE\_SHIFT](#a431b40e024ff711208e286a68cc4a88a)) |
| #define | [MT\_NO\_OVERWRITE](#ac636f36db1fba874b86869137adceb8a)   (1U << [MT\_NO\_OVERWRITE\_SHIFT](#a099fcd188b2d8cb542ead3aff617632c)) |
| #define | [MT\_G](#ada37826f9a2df34be98cc2e317d018d0)   (0U << [MT\_NON\_GLOBAL\_SHIFT](#affc55d3de67afeb18b29b2e4070b12e0)) |
| #define | [MT\_NG](#ab34aa4ce7681e17338d581bfd31ff5d1)   (1U << [MT\_NON\_GLOBAL\_SHIFT](#affc55d3de67afeb18b29b2e4070b12e0)) |
| #define | [MT\_P\_RW\_U\_RW](#a7820c2334f7d257ea6bad7207576da7d)   ([MT\_RW](#a2f968826efe83004f350f2264fc5b192) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| #define | [MT\_P\_RW\_U\_NA](#a22971adcbb04ce5c5dd54c318c60b335)   ([MT\_RW](#a2f968826efe83004f350f2264fc5b192) | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| #define | [MT\_P\_RO\_U\_RO](#acf29eaa48accc12214f86cf8c99cf04b)   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| #define | [MT\_P\_RO\_U\_NA](#a779a089d8fef5d7b544ef528d0355164)   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| #define | [MT\_P\_RO\_U\_RX](#a28187ebec00be9a34ce2a40f57337a3d)   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE](#a5826032cb5c39b30b5727214c0856472)) |
| #define | [MT\_P\_RX\_U\_RX](#a6964f6367d4687541502dc9d4bc3b00e)   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE](#a465cd6685380ff25b2223b19844d730a) | [MT\_U\_EXECUTE](#a5826032cb5c39b30b5727214c0856472)) |
| #define | [MT\_P\_RX\_U\_NA](#a927c1d7900d9a38b800118a0751dfc9f)   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f) | [MT\_P\_EXECUTE](#a465cd6685380ff25b2223b19844d730a) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| #define | [MT\_DEFAULT\_SECURE\_STATE](#afc20034b86cd6fefcbc63668e08bf466)   [MT\_SECURE](#a9a2ae47063f7f1b105796d5e3114118f) |
| #define | [VM\_ASID\_BITS](#a9c2e741f0962da342556c5933dcb3e13)   8 |
| #define | [TTBR\_ASID\_SHIFT](#a7a10d540248fccf48bdcaccac98f021c)   48 |
| #define | [PTE\_DESC\_TYPE\_MASK](#a527750258496a95273157359f9a616cd)   3U |
| #define | [PTE\_BLOCK\_DESC](#a88d1df1c276037d073cda2a19ae18333)   1U |
| #define | [PTE\_TABLE\_DESC](#a6bae275d781d6ed862ffcb4243793f78)   3U |
| #define | [PTE\_PAGE\_DESC](#ad06436454a4d3be738e45b49ebdece3a)   3U |
| #define | [PTE\_INVALID\_DESC](#a526197beecdcea0eec10e552a91093e6)   0U |
| #define | [PTE\_BLOCK\_DESC\_MEMTYPE](#a6c70c49e36e7086784aeb67190cb3fe1)(x) |
| #define | [PTE\_BLOCK\_DESC\_NS](#a2e118ef56a9201b03f4a6c1aa714c7a7)   (1ULL << 5) |
| #define | [PTE\_BLOCK\_DESC\_AP\_ELx](#ab98726b07a80272d8c256b3a3fb0962e)   (1ULL << 6) |
| #define | [PTE\_BLOCK\_DESC\_AP\_EL\_HIGHER](#a843a5d300e74d449654775e6f766b5af)   (0ULL << 6) |
| #define | [PTE\_BLOCK\_DESC\_AP\_RO](#a5856f4fe020995aad3806622d15d2658)   (1ULL << 7) |
| #define | [PTE\_BLOCK\_DESC\_AP\_RW](#a76134e521bd7aca4e1d44e6580cc1664)   (0ULL << 7) |
| #define | [PTE\_BLOCK\_DESC\_NON\_SHARE](#a81f8f7fe9bbd4d98ec549f79cacfc171)   (0ULL << 8) |
| #define | [PTE\_BLOCK\_DESC\_OUTER\_SHARE](#a950be651c8f1c2f417e6720ce86ed965)   (2ULL << 8) |
| #define | [PTE\_BLOCK\_DESC\_INNER\_SHARE](#a2a66f774077bf08a56ab756e65a951f6)   (3ULL << 8) |
| #define | [PTE\_BLOCK\_DESC\_AF](#ac297c22c098e84375419e66642f7dd08)   (1ULL << 10) |
| #define | [PTE\_BLOCK\_DESC\_NG](#aeaa1fc48a3425525e814a5757018bd02)   (1ULL << 11) |
| #define | [PTE\_BLOCK\_DESC\_PXN](#abd06d5802f589c9b5304fca4944e560b)   (1ULL << 53) |
| #define | [PTE\_BLOCK\_DESC\_UXN](#a30cbc588212d7a17bf96033bf550b356)   (1ULL << 54) |
| #define | [TCR\_EL1\_IPS\_SHIFT](#afc474e5ad860c2ad3929cfb0e260bbd4)   32U |
| #define | [TCR\_EL2\_PS\_SHIFT](#aec7d4ec2280b0a4bdda23bddf6906de1)   16U |
| #define | [TCR\_EL3\_PS\_SHIFT](#a877cc3e5688433a4054e6bf94da087fa)   16U |
| #define | [TCR\_T0SZ\_SHIFT](#ac1a5b8ca796786488092557cae6ee529)   0U |
| #define | [TCR\_T0SZ](#a517e3ccc657482e5fb7c44f1968f4d47)(x) |
| #define | [TCR\_IRGN\_NC](#a88aeb17c761edada2d6e3aaba7f86048)   (0ULL << 8) |
| #define | [TCR\_IRGN\_WBWA](#a78c51335d078882f3252159b84d5fdb4)   (1ULL << 8) |
| #define | [TCR\_IRGN\_WT](#aec3c547b075756c4d1aa78c831bc0e19)   (2ULL << 8) |
| #define | [TCR\_IRGN\_WBNWA](#ad57f8de92899f6bd54b6c898ce5c1c1e)   (3ULL << 8) |
| #define | [TCR\_IRGN\_MASK](#a89f8bb0c67aee23a0b3c32642513557b)   (3ULL << 8) |
| #define | [TCR\_ORGN\_NC](#acabb0e302d9da4b9ba55ed0e0eea5843)   (0ULL << 10) |
| #define | [TCR\_ORGN\_WBWA](#ae3c8d6de1e936b38893d324eb61f6759)   (1ULL << 10) |
| #define | [TCR\_ORGN\_WT](#a9fc70a55aab31e25e944fc1fa9c9a2f7)   (2ULL << 10) |
| #define | [TCR\_ORGN\_WBNWA](#af693fdf5b28a70fa4f74e37f34bf69df)   (3ULL << 10) |
| #define | [TCR\_ORGN\_MASK](#a266d922348791827670e045082cbecd4)   (3ULL << 10) |
| #define | [TCR\_SHARED\_NON](#ac9476792f28eed670e915a224487e56d)   (0ULL << 12) |
| #define | [TCR\_SHARED\_OUTER](#a8b22083005fdf69673a230483cde6796)   (2ULL << 12) |
| #define | [TCR\_SHARED\_INNER](#ab9b64a7a88537b21703c8ed22a0faf3c)   (3ULL << 12) |
| #define | [TCR\_TG0\_4K](#ae46a532f75ba7e47e002b6a87255d4b6)   (0ULL << 14) |
| #define | [TCR\_TG0\_64K](#a82277d04ea5b90b9cd76a3878731f5a2)   (1ULL << 14) |
| #define | [TCR\_TG0\_16K](#a5933d39b322e440d1d58f5b856bb646b)   (2ULL << 14) |
| #define | [TCR\_EPD1\_DISABLE](#a906790e8cf432a7c37f49663154e2bd9)   (1ULL << 23) |
| #define | [TCR\_TG1\_16K](#a73b851e99df71a05fed2c19fca94d871)   (1ULL << 30) |
| #define | [TCR\_TG1\_4K](#aad679e64b09a1ab7e33804541416db78)   (2ULL << 30) |
| #define | [TCR\_TG1\_64K](#a9eed7a785bd5191422317d2562294e88)   (3ULL << 30) |
| #define | [TCR\_PS\_BITS\_4GB](#a2e03342250af50f33b1936bd44eafd4c)   0x0ULL |
| #define | [TCR\_PS\_BITS\_64GB](#a88543861de395886feeb0ec348a397e9)   0x1ULL |
| #define | [TCR\_PS\_BITS\_1TB](#a31a276f07a891040b399a4f573dd0d16)   0x2ULL |
| #define | [TCR\_PS\_BITS\_4TB](#a3b30b0a4be3d34fcedc4bcd4ee77c0fd)   0x3ULL |
| #define | [TCR\_PS\_BITS\_16TB](#a1c6fe4b7dd9646549208af7eee92638b)   0x4ULL |
| #define | [TCR\_PS\_BITS\_256TB](#a5a7ab516dbd382c58dd408da6a22b88f)   0x5ULL |
| #define | [MMU\_REGION\_ENTRY](#a7ab46a0bcc5d7f2645f98067ed78ac8f)(\_name, \_base\_pa, \_base\_va, \_size, \_attrs) |
| #define | [MMU\_REGION\_FLAT\_ENTRY](#a7a9f450388792a5c053dd227207d255f)(name, adr, sz, attrs) |
| #define | [MMU\_REGION\_DT\_FLAT\_ENTRY](#a345c9537de9d7439c853b7f5c275d0cf)(node\_id, attrs) |
| #define | [MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY](#a3266a39e2c823047ab9a9162be60daf4)(compat, attr) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#a78f9b21aa8b5c894db28328f5a1e2641) |

| Variables | |
| --- | --- |
| const struct [arm\_mmu\_config](structarm__mmu__config.md) | [mmu\_config](#afb6753aab93fd940c3fc43c11a908216) |

## Macro Definition Documentation

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[MT\_P\_RO\_U\_NA](#a779a089d8fef5d7b544ef528d0355164)})

[MT\_P\_RO\_U\_NA](#a779a089d8fef5d7b544ef528d0355164)

#define MT\_P\_RO\_U\_NA

**Definition** arm\_mmu.h:81

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[MT\_P\_RO\_U\_RO](#acf29eaa48accc12214f86cf8c99cf04b)})

[MT\_P\_RO\_U\_RO](#acf29eaa48accc12214f86cf8c99cf04b)

#define MT\_P\_RO\_U\_RO

**Definition** arm\_mmu.h:80

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[MT\_P\_RW\_U\_NA](#a22971adcbb04ce5c5dd54c318c60b335)})

[MT\_P\_RW\_U\_NA](#a22971adcbb04ce5c5dd54c318c60b335)

#define MT\_P\_RW\_U\_NA

**Definition** arm\_mmu.h:79

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[MT\_P\_RW\_U\_RW](#a7820c2334f7d257ea6bad7207576da7d)})

[MT\_P\_RW\_U\_RW](#a7820c2334f7d257ea6bad7207576da7d)

#define MT\_P\_RW\_U\_RW

**Definition** arm\_mmu.h:78

## [◆ ](#a78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{[MT\_P\_RX\_U\_RX](#a6964f6367d4687541502dc9d4bc3b00e)})

[MT\_P\_RX\_U\_RX](#a6964f6367d4687541502dc9d4bc3b00e)

#define MT\_P\_RX\_U\_RX

**Definition** arm\_mmu.h:83

## [◆ ](#a8b7a2f1ea804a163917486b5e3d2a70a)MEMORY\_ATTRIBUTES

| #define MEMORY\_ATTRIBUTES |
| --- |

**Value:**

((0x00 << ([MT\_DEVICE\_nGnRnE](#a362a80b5a2f87e888d742ac4b1e8d7e1) \* 8)) | \

(0x04 << ([MT\_DEVICE\_nGnRE](#afb3dda3d3a2b1a147be7ee58366e3f87) \* 8)) | \

(0x0c << ([MT\_DEVICE\_GRE](#ada441c0a6171dce9eef0875593ba5e56) \* 8)) | \

(0x44 << ([MT\_NORMAL\_NC](#a1a41f294343c4fcb9741c693fc107601) \* 8)) | \

(0xffUL << ([MT\_NORMAL](mmu_2arm__mmu_8h.md#a8b006dab179dfa8965dcef3ac302746d) \* 8)) | \

(0xbbUL << ([MT\_NORMAL\_WT](#ad70c105c395f996ddd2628686e4e956f) \* 8)))

[MT\_NORMAL\_NC](#a1a41f294343c4fcb9741c693fc107601)

#define MT\_NORMAL\_NC

**Definition** arm\_mmu.h:25

[MT\_DEVICE\_nGnRnE](#a362a80b5a2f87e888d742ac4b1e8d7e1)

#define MT\_DEVICE\_nGnRnE

**Definition** arm\_mmu.h:22

[MT\_NORMAL\_WT](#ad70c105c395f996ddd2628686e4e956f)

#define MT\_NORMAL\_WT

**Definition** arm\_mmu.h:27

[MT\_DEVICE\_GRE](#ada441c0a6171dce9eef0875593ba5e56)

#define MT\_DEVICE\_GRE

**Definition** arm\_mmu.h:24

[MT\_DEVICE\_nGnRE](#afb3dda3d3a2b1a147be7ee58366e3f87)

#define MT\_DEVICE\_nGnRE

**Definition** arm\_mmu.h:23

[MT\_NORMAL](mmu_2arm__mmu_8h.md#a8b006dab179dfa8965dcef3ac302746d)

#define MT\_NORMAL

**Definition** arm\_mmu.h:30

## [◆ ](#a3266a39e2c823047ab9a9162be60daf4)MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY

| #define MMU\_REGION\_DT\_COMPAT\_FOREACH\_FLAT\_ENTRY | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *attr* ) |

**Value:**

[DT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)(compat, \

[MMU\_REGION\_DT\_FLAT\_ENTRY](mmu_2arm__mmu_8h.md#a345c9537de9d7439c853b7f5c275d0cf), attr)

[DT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)

#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn,...)

Invokes fn for each status okay node of a compatible with multiple arguments.

**Definition** devicetree.h:3137

[MMU\_REGION\_DT\_FLAT\_ENTRY](mmu_2arm__mmu_8h.md#a345c9537de9d7439c853b7f5c275d0cf)

#define MMU\_REGION\_DT\_FLAT\_ENTRY(node\_id, attrs)

**Definition** arm\_mmu.h:86

## [◆ ](#a345c9537de9d7439c853b7f5c275d0cf)MMU\_REGION\_DT\_FLAT\_ENTRY

| #define MMU\_REGION\_DT\_FLAT\_ENTRY | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *attrs* ) |

**Value:**

[MMU\_REGION\_FLAT\_ENTRY](mmu_2arm__mmu_8h.md#a7a9f450388792a5c053dd227207d255f)([DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)(node\_id), \

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id), \

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)(node\_id), \

attrs),

[DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)

#define DT\_NODE\_FULL\_NAME(node\_id)

Get a devicetree node's name with unit-address as a string literal.

**Definition** devicetree.h:522

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)

#define DT\_REG\_SIZE(node\_id)

Get a node's (only) register block size.

**Definition** devicetree.h:2235

[MMU\_REGION\_FLAT\_ENTRY](mmu_2arm__mmu_8h.md#a7a9f450388792a5c053dd227207d255f)

#define MMU\_REGION\_FLAT\_ENTRY(name, adr, sz, attrs)

**Definition** arm\_mmu.h:67

## [◆ ](#a7ab46a0bcc5d7f2645f98067ed78ac8f)MMU\_REGION\_ENTRY

| #define MMU\_REGION\_ENTRY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_base\_pa*, |
|  |  |  | *\_base\_va*, |
|  |  |  | *\_size*, |
|  |  |  | *\_attrs* ) |

**Value:**

{\

.name = \_name, \

.base\_pa = \_base\_pa, \

.base\_va = \_base\_va, \

.size = \_size, \

.attrs = \_attrs, \

}

## [◆ ](#a7a9f450388792a5c053dd227207d255f)MMU\_REGION\_FLAT\_ENTRY

| #define MMU\_REGION\_FLAT\_ENTRY | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *adr*, |
|  |  |  | *sz*, |
|  |  |  | *attrs* ) |

**Value:**

[MMU\_REGION\_ENTRY](mmu_2arm__mmu_8h.md#a7ab46a0bcc5d7f2645f98067ed78ac8f)(name, adr, adr, sz, attrs)

[MMU\_REGION\_ENTRY](mmu_2arm__mmu_8h.md#a7ab46a0bcc5d7f2645f98067ed78ac8f)

#define MMU\_REGION\_ENTRY(\_name, \_base\_pa, \_base\_va, \_size, \_attrs)

**Definition** arm\_mmu.h:58

## [◆ ](#afc20034b86cd6fefcbc63668e08bf466)MT\_DEFAULT\_SECURE\_STATE

| #define MT\_DEFAULT\_SECURE\_STATE   [MT\_SECURE](#a9a2ae47063f7f1b105796d5e3114118f) |
| --- |

## [◆ ](#ada441c0a6171dce9eef0875593ba5e56)MT\_DEVICE\_GRE

| #define MT\_DEVICE\_GRE   2U |
| --- |

## [◆ ](#afb3dda3d3a2b1a147be7ee58366e3f87)MT\_DEVICE\_nGnRE

| #define MT\_DEVICE\_nGnRE   1U |
| --- |

## [◆ ](#a362a80b5a2f87e888d742ac4b1e8d7e1)MT\_DEVICE\_nGnRnE

| #define MT\_DEVICE\_nGnRnE   0U |
| --- |

## [◆ ](#ada37826f9a2df34be98cc2e317d018d0)MT\_G

| #define MT\_G   (0U << [MT\_NON\_GLOBAL\_SHIFT](#affc55d3de67afeb18b29b2e4070b12e0)) |
| --- |

## [◆ ](#ab34aa4ce7681e17338d581bfd31ff5d1)MT\_NG

| #define MT\_NG   (1U << [MT\_NON\_GLOBAL\_SHIFT](#affc55d3de67afeb18b29b2e4070b12e0)) |
| --- |

## [◆ ](#ac636f36db1fba874b86869137adceb8a)MT\_NO\_OVERWRITE

| #define MT\_NO\_OVERWRITE   (1U << [MT\_NO\_OVERWRITE\_SHIFT](#a099fcd188b2d8cb542ead3aff617632c)) |
| --- |

## [◆ ](#a099fcd188b2d8cb542ead3aff617632c)MT\_NO\_OVERWRITE\_SHIFT

| #define MT\_NO\_OVERWRITE\_SHIFT   8U |
| --- |

## [◆ ](#affc55d3de67afeb18b29b2e4070b12e0)MT\_NON\_GLOBAL\_SHIFT

| #define MT\_NON\_GLOBAL\_SHIFT   9U |
| --- |

## [◆ ](#a8b006dab179dfa8965dcef3ac302746d)MT\_NORMAL

| #define MT\_NORMAL   4U |
| --- |

## [◆ ](#a1a41f294343c4fcb9741c693fc107601)MT\_NORMAL\_NC

| #define MT\_NORMAL\_NC   3U |
| --- |

## [◆ ](#ad70c105c395f996ddd2628686e4e956f)MT\_NORMAL\_WT

| #define MT\_NORMAL\_WT   5U |
| --- |

## [◆ ](#a2b0dcb4b334e2fd3eb31eb7451dfc005)MT\_NS

| #define MT\_NS   (1U << [MT\_SEC\_SHIFT](#a4e94c3f3e790bb5c1afaa6ffa1094c8d)) |
| --- |

## [◆ ](#a465cd6685380ff25b2223b19844d730a)MT\_P\_EXECUTE

| #define MT\_P\_EXECUTE   (0U << [MT\_P\_EXECUTE\_SHIFT](#ac01ddafde6fbc038bfa5994b7335429c)) |
| --- |

## [◆ ](#a968668b91295729a7d462216e91c6d0c)MT\_P\_EXECUTE\_NEVER

| #define MT\_P\_EXECUTE\_NEVER   (1U << [MT\_P\_EXECUTE\_SHIFT](#ac01ddafde6fbc038bfa5994b7335429c)) |
| --- |

## [◆ ](#ac01ddafde6fbc038bfa5994b7335429c)MT\_P\_EXECUTE\_SHIFT

| #define MT\_P\_EXECUTE\_SHIFT   5U |
| --- |

## [◆ ](#a779a089d8fef5d7b544ef528d0355164)MT\_P\_RO\_U\_NA

| #define MT\_P\_RO\_U\_NA   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| --- |

## [◆ ](#acf29eaa48accc12214f86cf8c99cf04b)MT\_P\_RO\_U\_RO

| #define MT\_P\_RO\_U\_RO   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| --- |

## [◆ ](#a28187ebec00be9a34ce2a40f57337a3d)MT\_P\_RO\_U\_RX

| #define MT\_P\_RO\_U\_RX   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE](#a5826032cb5c39b30b5727214c0856472)) |
| --- |

## [◆ ](#a22971adcbb04ce5c5dd54c318c60b335)MT\_P\_RW\_U\_NA

| #define MT\_P\_RW\_U\_NA   ([MT\_RW](#a2f968826efe83004f350f2264fc5b192) | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| --- |

## [◆ ](#a7820c2334f7d257ea6bad7207576da7d)MT\_P\_RW\_U\_RW

| #define MT\_P\_RW\_U\_RW   ([MT\_RW](#a2f968826efe83004f350f2264fc5b192) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE\_NEVER](#a968668b91295729a7d462216e91c6d0c) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| --- |

## [◆ ](#a927c1d7900d9a38b800118a0751dfc9f)MT\_P\_RX\_U\_NA

| #define MT\_P\_RX\_U\_NA   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_EL\_HIGHER](#a9ee77575da6d9e81fc4ec5042b43932f) | [MT\_P\_EXECUTE](#a465cd6685380ff25b2223b19844d730a) | [MT\_U\_EXECUTE\_NEVER](#a8ea94a35ceb0fc2dedd93a6eadadb68c)) |
| --- |

## [◆ ](#a6964f6367d4687541502dc9d4bc3b00e)MT\_P\_RX\_U\_RX

| #define MT\_P\_RX\_U\_RX   ([MT\_RO](#a596089f139287e4696c2fe9c9add4074) | [MT\_RW\_AP\_ELx](#a06edb368943a5fffb03c362df5e00973) | [MT\_P\_EXECUTE](#a465cd6685380ff25b2223b19844d730a) | [MT\_U\_EXECUTE](#a5826032cb5c39b30b5727214c0856472)) |
| --- |

## [◆ ](#a4796895c7c90277cd1eae3c34fecd96c)MT\_PERM\_SHIFT

| #define MT\_PERM\_SHIFT   3U |
| --- |

## [◆ ](#a596089f139287e4696c2fe9c9add4074)MT\_RO

| #define MT\_RO   (0U << [MT\_PERM\_SHIFT](#a4796895c7c90277cd1eae3c34fecd96c)) |
| --- |

## [◆ ](#a2f968826efe83004f350f2264fc5b192)MT\_RW

| #define MT\_RW   (1U << [MT\_PERM\_SHIFT](#a4796895c7c90277cd1eae3c34fecd96c)) |
| --- |

## [◆ ](#a9ee77575da6d9e81fc4ec5042b43932f)MT\_RW\_AP\_EL\_HIGHER

| #define MT\_RW\_AP\_EL\_HIGHER   (0U << [MT\_RW\_AP\_SHIFT](#afe1e276059306bc596102d8cc0eb0db6)) |
| --- |

## [◆ ](#a06edb368943a5fffb03c362df5e00973)MT\_RW\_AP\_ELx

| #define MT\_RW\_AP\_ELx   (1U << [MT\_RW\_AP\_SHIFT](#afe1e276059306bc596102d8cc0eb0db6)) |
| --- |

## [◆ ](#afe1e276059306bc596102d8cc0eb0db6)MT\_RW\_AP\_SHIFT

| #define MT\_RW\_AP\_SHIFT   7U |
| --- |

## [◆ ](#a4e94c3f3e790bb5c1afaa6ffa1094c8d)MT\_SEC\_SHIFT

| #define MT\_SEC\_SHIFT   4U |
| --- |

## [◆ ](#a9a2ae47063f7f1b105796d5e3114118f)MT\_SECURE

| #define MT\_SECURE   (0U << [MT\_SEC\_SHIFT](#a4e94c3f3e790bb5c1afaa6ffa1094c8d)) |
| --- |

## [◆ ](#a9018634e807aa322da516bb70b9c5e3e)MT\_TYPE

| #define MT\_TYPE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(attr & [MT\_TYPE\_MASK](#aac0064c36c372d9a62d3a7a4fa8dc72c))

[MT\_TYPE\_MASK](#aac0064c36c372d9a62d3a7a4fa8dc72c)

#define MT\_TYPE\_MASK

**Definition** arm\_mmu.h:20

## [◆ ](#aac0064c36c372d9a62d3a7a4fa8dc72c)MT\_TYPE\_MASK

| #define MT\_TYPE\_MASK   0x7U |
| --- |

## [◆ ](#a5826032cb5c39b30b5727214c0856472)MT\_U\_EXECUTE

| #define MT\_U\_EXECUTE   (0U << [MT\_U\_EXECUTE\_SHIFT](#a431b40e024ff711208e286a68cc4a88a)) |
| --- |

## [◆ ](#a8ea94a35ceb0fc2dedd93a6eadadb68c)MT\_U\_EXECUTE\_NEVER

| #define MT\_U\_EXECUTE\_NEVER   (1U << [MT\_U\_EXECUTE\_SHIFT](#a431b40e024ff711208e286a68cc4a88a)) |
| --- |

## [◆ ](#a431b40e024ff711208e286a68cc4a88a)MT\_U\_EXECUTE\_SHIFT

| #define MT\_U\_EXECUTE\_SHIFT   6U |
| --- |

## [◆ ](#a88d1df1c276037d073cda2a19ae18333)PTE\_BLOCK\_DESC

| #define PTE\_BLOCK\_DESC   1U |
| --- |

## [◆ ](#ac297c22c098e84375419e66642f7dd08)PTE\_BLOCK\_DESC\_AF

| #define PTE\_BLOCK\_DESC\_AF   (1ULL << 10) |
| --- |

## [◆ ](#a843a5d300e74d449654775e6f766b5af)PTE\_BLOCK\_DESC\_AP\_EL\_HIGHER

| #define PTE\_BLOCK\_DESC\_AP\_EL\_HIGHER   (0ULL << 6) |
| --- |

## [◆ ](#ab98726b07a80272d8c256b3a3fb0962e)PTE\_BLOCK\_DESC\_AP\_ELx

| #define PTE\_BLOCK\_DESC\_AP\_ELx   (1ULL << 6) |
| --- |

## [◆ ](#a5856f4fe020995aad3806622d15d2658)PTE\_BLOCK\_DESC\_AP\_RO

| #define PTE\_BLOCK\_DESC\_AP\_RO   (1ULL << 7) |
| --- |

## [◆ ](#a76134e521bd7aca4e1d44e6580cc1664)PTE\_BLOCK\_DESC\_AP\_RW

| #define PTE\_BLOCK\_DESC\_AP\_RW   (0ULL << 7) |
| --- |

## [◆ ](#a2a66f774077bf08a56ab756e65a951f6)PTE\_BLOCK\_DESC\_INNER\_SHARE

| #define PTE\_BLOCK\_DESC\_INNER\_SHARE   (3ULL << 8) |
| --- |

## [◆ ](#a6c70c49e36e7086784aeb67190cb3fe1)PTE\_BLOCK\_DESC\_MEMTYPE

| #define PTE\_BLOCK\_DESC\_MEMTYPE | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(x << 2)

## [◆ ](#aeaa1fc48a3425525e814a5757018bd02)PTE\_BLOCK\_DESC\_NG

| #define PTE\_BLOCK\_DESC\_NG   (1ULL << 11) |
| --- |

## [◆ ](#a81f8f7fe9bbd4d98ec549f79cacfc171)PTE\_BLOCK\_DESC\_NON\_SHARE

| #define PTE\_BLOCK\_DESC\_NON\_SHARE   (0ULL << 8) |
| --- |

## [◆ ](#a2e118ef56a9201b03f4a6c1aa714c7a7)PTE\_BLOCK\_DESC\_NS

| #define PTE\_BLOCK\_DESC\_NS   (1ULL << 5) |
| --- |

## [◆ ](#a950be651c8f1c2f417e6720ce86ed965)PTE\_BLOCK\_DESC\_OUTER\_SHARE

| #define PTE\_BLOCK\_DESC\_OUTER\_SHARE   (2ULL << 8) |
| --- |

## [◆ ](#abd06d5802f589c9b5304fca4944e560b)PTE\_BLOCK\_DESC\_PXN

| #define PTE\_BLOCK\_DESC\_PXN   (1ULL << 53) |
| --- |

## [◆ ](#a30cbc588212d7a17bf96033bf550b356)PTE\_BLOCK\_DESC\_UXN

| #define PTE\_BLOCK\_DESC\_UXN   (1ULL << 54) |
| --- |

## [◆ ](#a527750258496a95273157359f9a616cd)PTE\_DESC\_TYPE\_MASK

| #define PTE\_DESC\_TYPE\_MASK   3U |
| --- |

## [◆ ](#a526197beecdcea0eec10e552a91093e6)PTE\_INVALID\_DESC

| #define PTE\_INVALID\_DESC   0U |
| --- |

## [◆ ](#ad06436454a4d3be738e45b49ebdece3a)PTE\_PAGE\_DESC

| #define PTE\_PAGE\_DESC   3U |
| --- |

## [◆ ](#a6bae275d781d6ed862ffcb4243793f78)PTE\_TABLE\_DESC

| #define PTE\_TABLE\_DESC   3U |
| --- |

## [◆ ](#afc474e5ad860c2ad3929cfb0e260bbd4)TCR\_EL1\_IPS\_SHIFT

| #define TCR\_EL1\_IPS\_SHIFT   32U |
| --- |

## [◆ ](#aec7d4ec2280b0a4bdda23bddf6906de1)TCR\_EL2\_PS\_SHIFT

| #define TCR\_EL2\_PS\_SHIFT   16U |
| --- |

## [◆ ](#a877cc3e5688433a4054e6bf94da087fa)TCR\_EL3\_PS\_SHIFT

| #define TCR\_EL3\_PS\_SHIFT   16U |
| --- |

## [◆ ](#a906790e8cf432a7c37f49663154e2bd9)TCR\_EPD1\_DISABLE

| #define TCR\_EPD1\_DISABLE   (1ULL << 23) |
| --- |

## [◆ ](#a89f8bb0c67aee23a0b3c32642513557b)TCR\_IRGN\_MASK

| #define TCR\_IRGN\_MASK   (3ULL << 8) |
| --- |

## [◆ ](#a88aeb17c761edada2d6e3aaba7f86048)TCR\_IRGN\_NC

| #define TCR\_IRGN\_NC   (0ULL << 8) |
| --- |

## [◆ ](#ad57f8de92899f6bd54b6c898ce5c1c1e)TCR\_IRGN\_WBNWA

| #define TCR\_IRGN\_WBNWA   (3ULL << 8) |
| --- |

## [◆ ](#a78c51335d078882f3252159b84d5fdb4)TCR\_IRGN\_WBWA

| #define TCR\_IRGN\_WBWA   (1ULL << 8) |
| --- |

## [◆ ](#aec3c547b075756c4d1aa78c831bc0e19)TCR\_IRGN\_WT

| #define TCR\_IRGN\_WT   (2ULL << 8) |
| --- |

## [◆ ](#a266d922348791827670e045082cbecd4)TCR\_ORGN\_MASK

| #define TCR\_ORGN\_MASK   (3ULL << 10) |
| --- |

## [◆ ](#acabb0e302d9da4b9ba55ed0e0eea5843)TCR\_ORGN\_NC

| #define TCR\_ORGN\_NC   (0ULL << 10) |
| --- |

## [◆ ](#af693fdf5b28a70fa4f74e37f34bf69df)TCR\_ORGN\_WBNWA

| #define TCR\_ORGN\_WBNWA   (3ULL << 10) |
| --- |

## [◆ ](#ae3c8d6de1e936b38893d324eb61f6759)TCR\_ORGN\_WBWA

| #define TCR\_ORGN\_WBWA   (1ULL << 10) |
| --- |

## [◆ ](#a9fc70a55aab31e25e944fc1fa9c9a2f7)TCR\_ORGN\_WT

| #define TCR\_ORGN\_WT   (2ULL << 10) |
| --- |

## [◆ ](#a1c6fe4b7dd9646549208af7eee92638b)TCR\_PS\_BITS\_16TB

| #define TCR\_PS\_BITS\_16TB   0x4ULL |
| --- |

## [◆ ](#a31a276f07a891040b399a4f573dd0d16)TCR\_PS\_BITS\_1TB

| #define TCR\_PS\_BITS\_1TB   0x2ULL |
| --- |

## [◆ ](#a5a7ab516dbd382c58dd408da6a22b88f)TCR\_PS\_BITS\_256TB

| #define TCR\_PS\_BITS\_256TB   0x5ULL |
| --- |

## [◆ ](#a2e03342250af50f33b1936bd44eafd4c)TCR\_PS\_BITS\_4GB

| #define TCR\_PS\_BITS\_4GB   0x0ULL |
| --- |

## [◆ ](#a3b30b0a4be3d34fcedc4bcd4ee77c0fd)TCR\_PS\_BITS\_4TB

| #define TCR\_PS\_BITS\_4TB   0x3ULL |
| --- |

## [◆ ](#a88543861de395886feeb0ec348a397e9)TCR\_PS\_BITS\_64GB

| #define TCR\_PS\_BITS\_64GB   0x1ULL |
| --- |

## [◆ ](#ab9b64a7a88537b21703c8ed22a0faf3c)TCR\_SHARED\_INNER

| #define TCR\_SHARED\_INNER   (3ULL << 12) |
| --- |

## [◆ ](#ac9476792f28eed670e915a224487e56d)TCR\_SHARED\_NON

| #define TCR\_SHARED\_NON   (0ULL << 12) |
| --- |

## [◆ ](#a8b22083005fdf69673a230483cde6796)TCR\_SHARED\_OUTER

| #define TCR\_SHARED\_OUTER   (2ULL << 12) |
| --- |

## [◆ ](#a517e3ccc657482e5fb7c44f1968f4d47)TCR\_T0SZ

| #define TCR\_T0SZ | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((64 - (x)) << [TCR\_T0SZ\_SHIFT](#ac1a5b8ca796786488092557cae6ee529))

[TCR\_T0SZ\_SHIFT](#ac1a5b8ca796786488092557cae6ee529)

#define TCR\_T0SZ\_SHIFT

**Definition** arm\_mmu.h:133

## [◆ ](#ac1a5b8ca796786488092557cae6ee529)TCR\_T0SZ\_SHIFT

| #define TCR\_T0SZ\_SHIFT   0U |
| --- |

## [◆ ](#a5933d39b322e440d1d58f5b856bb646b)TCR\_TG0\_16K

| #define TCR\_TG0\_16K   (2ULL << 14) |
| --- |

## [◆ ](#ae46a532f75ba7e47e002b6a87255d4b6)TCR\_TG0\_4K

| #define TCR\_TG0\_4K   (0ULL << 14) |
| --- |

## [◆ ](#a82277d04ea5b90b9cd76a3878731f5a2)TCR\_TG0\_64K

| #define TCR\_TG0\_64K   (1ULL << 14) |
| --- |

## [◆ ](#a73b851e99df71a05fed2c19fca94d871)TCR\_TG1\_16K

| #define TCR\_TG1\_16K   (1ULL << 30) |
| --- |

## [◆ ](#aad679e64b09a1ab7e33804541416db78)TCR\_TG1\_4K

| #define TCR\_TG1\_4K   (2ULL << 30) |
| --- |

## [◆ ](#a9eed7a785bd5191422317d2562294e88)TCR\_TG1\_64K

| #define TCR\_TG1\_64K   (3ULL << 30) |
| --- |

## [◆ ](#a7a10d540248fccf48bdcaccac98f021c)TTBR\_ASID\_SHIFT

| #define TTBR\_ASID\_SHIFT   48 |
| --- |

## [◆ ](#a9c2e741f0962da342556c5933dcb3e13)VM\_ASID\_BITS

| #define VM\_ASID\_BITS   8 |
| --- |

## Variable Documentation

## [◆ ](#afb6753aab93fd940c3fc43c11a908216)mmu\_config

| | const struct [arm\_mmu\_config](structarm__mmu__config.md) mmu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm\_mmu.h](4_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
