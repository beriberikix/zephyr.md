---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/4_2arm__mmu_8h.html
original_path: doxygen/html/4_2arm__mmu_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

**Definition** devicetree.h:3251

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

**Definition** devicetree.h:524

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2276

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)

#define DT\_REG\_SIZE(node\_id)

Get a node's (only) register block size.

**Definition** devicetree.h:2297

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

## Variable Documentation

## [◆ ](#afb6753aab93fd940c3fc43c11a908216)mmu\_config

| | const struct [arm\_mmu\_config](structarm__mmu__config.md) mmu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [arm\_mmu.h](4_2arm__mmu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
