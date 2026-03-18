---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/util__internal_8h.html
original_path: doxygen/html/util__internal_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util\_internal.h File Reference

Misc utilities.
[More...](#details)

`#include "[util_loops.h](util__loops_8h_source.md)"`  
`#include "[util_internal_is_eq.h](util__internal__is__eq_8h_source.md)"`  
`#include "[util_internal_util_inc.h](util__internal__util__inc_8h_source.md)"`  
`#include "[util_internal_util_dec.h](util__internal__util__dec_8h_source.md)"`  
`#include "[util_internal_util_x2.h](util__internal__util__x2_8h_source.md)"`

[Go to the source code of this file.](util__internal_8h_source.md)

| Macros | |
| --- | --- |
| #define | [UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(a, ...) |
| #define | [UTIL\_PRIMITIVE\_CAT](#a333f808696450134a9948dcc9e57e4ae)(a, ...) |
| #define | [UTIL\_CHECK\_N](#a1f1ff51e3bda754ee9561bd6d17277a4)(x, n, ...) |
| #define | [UTIL\_CHECK](#afc586c7e633155a0a3db1614d7c76a83)(...) |
| #define | [UTIL\_NOT](#a5db295294795b2ecad29f585dda49c49)(x) |
| #define | [UTIL\_NOT\_0](#aeb84e257f8e817fc7436d032d579853b)   ~, 1, |
| #define | [UTIL\_COMPL](#ae667bfa8e06a6b3c15266db678934ef3)(b) |
| #define | [UTIL\_COMPL\_0](#af8b84b2dc23d37616d59e8e19a5c94dd)   1 |
| #define | [UTIL\_COMPL\_1](#a69fb8790ad07ef2c00176a783c192390)   0 |
| #define | [UTIL\_BOOL](#a80cbb3a182096676524d761113349bc8)(x) |
| #define | [UTIL\_EVAL](#a56279e773dc8d31b83161cc9526e8c56)(...) |
| #define | [UTIL\_EXPAND](#a4393cb8f894e8a32385a49fbfaf841b2)(...) |
| #define | [UTIL\_REPEAT](#a3c54146013b856ef16ad45471b9fc7d1)(...) |
| #define | [NUM\_VA\_ARGS\_LESS\_1\_IMPL](#a70e3443886f63259dc12b14cc26c365f)( \_ignored, \_0, \_1, \_2, \_3, \_4, \_5, \_6, \_7, \_8, \_9, \_10, \_11, \_12, \_13, \_14, \_15, \_16, \_17, \_18, \_19, \_20, \_21, \_22, \_23, \_24, \_25, \_26, \_27, \_28, \_29, \_30, \_31, \_32, \_33, \_34, \_35, \_36, \_37, \_38, \_39, \_40, \_41, \_42, \_43, \_44, \_45, \_46, \_47, \_48, \_49, \_50, \_51, \_52, \_53, \_54, \_55, \_56, \_57, \_58, \_59, \_60, \_61, \_62, N, ...) |
| #define | [MACRO\_MAP\_CAT\_](#abe4f647ef2c1c706bc9d0d0e737e58bf)(...) |
| #define | [MACRO\_MAP\_CAT\_N\_](#a72d29784bb0a030942e2c6eb2f9d42b9)(N, ...) |
| #define | [MACRO\_MC\_0](#a700a021819a2bc3bd4d9f18ebcc97579)(...) |
| #define | [MACRO\_MC\_1](#aebb6edacecae322c4e5193e5dd50f072)(m, a, ...) |
| #define | [MACRO\_MC\_2](#acac4b3ad7d94e0c3ebf483c056cdd9cb)(m, a, ...) |
| #define | [MACRO\_MC\_3](#aebb08fb4302da40ca6964b9c4576862a)(m, a, ...) |
| #define | [MACRO\_MC\_4](#ac5368a62577d74ca4e307a08bd081db4)(m, a, ...) |
| #define | [MACRO\_MC\_5](#ab1fb261044e3ac3cd905aa2e57eb35c9)(m, a, ...) |
| #define | [MACRO\_MC\_6](#a333330ed553dc76046eac9f5ee75a166)(m, a, ...) |
| #define | [MACRO\_MC\_7](#a9f00d73d613e15afec0bd80b02f4d392)(m, a, ...) |
| #define | [MACRO\_MC\_8](#aba43ed361199ce700b55cfca4c59132c)(m, a, ...) |
| #define | [MACRO\_MC\_9](#a141c582a8152fb8bc3fdd9c963302528)(m, a, ...) |
| #define | [MACRO\_MC\_10](#adcd5dc69004dbcf2e1a1a0f8b1e38e34)(m, a, ...) |
| #define | [MACRO\_MC\_11](#aac114268287177238e8a43e9a631fea9)(m, a, ...) |
| #define | [MACRO\_MC\_12](#abcf2741e7ce67d08eeaa7bfe24e54626)(m, a, ...) |
| #define | [MACRO\_MC\_13](#a479b004b91499c3f580bc75fec26bbac)(m, a, ...) |
| #define | [MACRO\_MC\_14](#af15fc993928b1bfd08778b73daee73cc)(m, a, ...) |
| #define | [MACRO\_MC\_15](#a7e45901b614d203f7824cef9ae57b70e)(m, a, ...) |

## Detailed Description

Misc utilities.

Repetitive or obscure helper macros needed by [sys/util.h](util_8h.md "Misc utilities.").

## Macro Definition Documentation

## [◆ ](#abe4f647ef2c1c706bc9d0d0e737e58bf)MACRO\_MAP\_CAT\_

| #define MACRO\_MAP\_CAT\_ | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

/\* To make sure it works also for 2 arguments in total \*/ \

MACRO\_MAP\_CAT\_N([NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_)

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)

#define NUM\_VA\_ARGS\_LESS\_1(...)

Number of arguments in the variable arguments list minus one.

**Definition** util\_macro.h:629

## [◆ ](#a72d29784bb0a030942e2c6eb2f9d42b9)MACRO\_MAP\_CAT\_N\_

| #define MACRO\_MAP\_CAT\_N\_ | ( |  | *N*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(MACRO\_MC\_, N)(\_\_VA\_ARGS\_\_,)

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

## [◆ ](#a700a021819a2bc3bd4d9f18ebcc97579)MACRO\_MC\_0

| #define MACRO\_MC\_0 | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aebb6edacecae322c4e5193e5dd50f072)MACRO\_MC\_1

| #define MACRO\_MC\_1 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

m(a)

## [◆ ](#adcd5dc69004dbcf2e1a1a0f8b1e38e34)MACRO\_MC\_10

| #define MACRO\_MC\_10 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_9](#a141c582a8152fb8bc3fdd9c963302528)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_9](#a141c582a8152fb8bc3fdd9c963302528)

#define MACRO\_MC\_9(m, a,...)

**Definition** util\_internal.h:153

## [◆ ](#aac114268287177238e8a43e9a631fea9)MACRO\_MC\_11

| #define MACRO\_MC\_11 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_10](#adcd5dc69004dbcf2e1a1a0f8b1e38e34)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_10](#adcd5dc69004dbcf2e1a1a0f8b1e38e34)

#define MACRO\_MC\_10(m, a,...)

**Definition** util\_internal.h:154

## [◆ ](#abcf2741e7ce67d08eeaa7bfe24e54626)MACRO\_MC\_12

| #define MACRO\_MC\_12 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_11](#aac114268287177238e8a43e9a631fea9)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_11](#aac114268287177238e8a43e9a631fea9)

#define MACRO\_MC\_11(m, a,...)

**Definition** util\_internal.h:155

## [◆ ](#a479b004b91499c3f580bc75fec26bbac)MACRO\_MC\_13

| #define MACRO\_MC\_13 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_12](#abcf2741e7ce67d08eeaa7bfe24e54626)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_12](#abcf2741e7ce67d08eeaa7bfe24e54626)

#define MACRO\_MC\_12(m, a,...)

**Definition** util\_internal.h:156

## [◆ ](#af15fc993928b1bfd08778b73daee73cc)MACRO\_MC\_14

| #define MACRO\_MC\_14 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_13](#a479b004b91499c3f580bc75fec26bbac)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_13](#a479b004b91499c3f580bc75fec26bbac)

#define MACRO\_MC\_13(m, a,...)

**Definition** util\_internal.h:157

## [◆ ](#a7e45901b614d203f7824cef9ae57b70e)MACRO\_MC\_15

| #define MACRO\_MC\_15 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_14](#af15fc993928b1bfd08778b73daee73cc)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_14](#af15fc993928b1bfd08778b73daee73cc)

#define MACRO\_MC\_14(m, a,...)

**Definition** util\_internal.h:158

## [◆ ](#acac4b3ad7d94e0c3ebf483c056cdd9cb)MACRO\_MC\_2

| #define MACRO\_MC\_2 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_1](#aebb6edacecae322c4e5193e5dd50f072)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_1](#aebb6edacecae322c4e5193e5dd50f072)

#define MACRO\_MC\_1(m, a,...)

**Definition** util\_internal.h:145

## [◆ ](#aebb08fb4302da40ca6964b9c4576862a)MACRO\_MC\_3

| #define MACRO\_MC\_3 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_2](#acac4b3ad7d94e0c3ebf483c056cdd9cb)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_2](#acac4b3ad7d94e0c3ebf483c056cdd9cb)

#define MACRO\_MC\_2(m, a,...)

**Definition** util\_internal.h:146

## [◆ ](#ac5368a62577d74ca4e307a08bd081db4)MACRO\_MC\_4

| #define MACRO\_MC\_4 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_3](#aebb08fb4302da40ca6964b9c4576862a)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_3](#aebb08fb4302da40ca6964b9c4576862a)

#define MACRO\_MC\_3(m, a,...)

**Definition** util\_internal.h:147

## [◆ ](#ab1fb261044e3ac3cd905aa2e57eb35c9)MACRO\_MC\_5

| #define MACRO\_MC\_5 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_4](#ac5368a62577d74ca4e307a08bd081db4)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_4](#ac5368a62577d74ca4e307a08bd081db4)

#define MACRO\_MC\_4(m, a,...)

**Definition** util\_internal.h:148

## [◆ ](#a333330ed553dc76046eac9f5ee75a166)MACRO\_MC\_6

| #define MACRO\_MC\_6 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_5](#ab1fb261044e3ac3cd905aa2e57eb35c9)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_5](#ab1fb261044e3ac3cd905aa2e57eb35c9)

#define MACRO\_MC\_5(m, a,...)

**Definition** util\_internal.h:149

## [◆ ](#a9f00d73d613e15afec0bd80b02f4d392)MACRO\_MC\_7

| #define MACRO\_MC\_7 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_6](#a333330ed553dc76046eac9f5ee75a166)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_6](#a333330ed553dc76046eac9f5ee75a166)

#define MACRO\_MC\_6(m, a,...)

**Definition** util\_internal.h:150

## [◆ ](#aba43ed361199ce700b55cfca4c59132c)MACRO\_MC\_8

| #define MACRO\_MC\_8 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_7](#a9f00d73d613e15afec0bd80b02f4d392)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_7](#a9f00d73d613e15afec0bd80b02f4d392)

#define MACRO\_MC\_7(m, a,...)

**Definition** util\_internal.h:151

## [◆ ](#a141c582a8152fb8bc3fdd9c963302528)MACRO\_MC\_9

| #define MACRO\_MC\_9 | ( |  | *m*, |
| --- | --- | --- | --- |
|  |  |  | *a*, |
|  |  |  | ... ) |

**Value:**

[UTIL\_CAT](#a7e7766e792d1638bfbbc9d0f328d3d0d)(m(a), [MACRO\_MC\_8](#aba43ed361199ce700b55cfca4c59132c)(m, \_\_VA\_ARGS\_\_,))

[MACRO\_MC\_8](#aba43ed361199ce700b55cfca4c59132c)

#define MACRO\_MC\_8(m, a,...)

**Definition** util\_internal.h:152

## [◆ ](#a70e3443886f63259dc12b14cc26c365f)NUM\_VA\_ARGS\_LESS\_1\_IMPL

| #define NUM\_VA\_ARGS\_LESS\_1\_IMPL | ( |  | *\_ignored*, |
| --- | --- | --- | --- |
|  |  |  | *\_0*, |
|  |  |  | *\_1*, |
|  |  |  | *\_2*, |
|  |  |  | *\_3*, |
|  |  |  | *\_4*, |
|  |  |  | *\_5*, |
|  |  |  | *\_6*, |
|  |  |  | *\_7*, |
|  |  |  | *\_8*, |
|  |  |  | *\_9*, |
|  |  |  | *\_10*, |
|  |  |  | *\_11*, |
|  |  |  | *\_12*, |
|  |  |  | *\_13*, |
|  |  |  | *\_14*, |
|  |  |  | *\_15*, |
|  |  |  | *\_16*, |
|  |  |  | *\_17*, |
|  |  |  | *\_18*, |
|  |  |  | *\_19*, |
|  |  |  | *\_20*, |
|  |  |  | *\_21*, |
|  |  |  | *\_22*, |
|  |  |  | *\_23*, |
|  |  |  | *\_24*, |
|  |  |  | *\_25*, |
|  |  |  | *\_26*, |
|  |  |  | *\_27*, |
|  |  |  | *\_28*, |
|  |  |  | *\_29*, |
|  |  |  | *\_30*, |
|  |  |  | *\_31*, |
|  |  |  | *\_32*, |
|  |  |  | *\_33*, |
|  |  |  | *\_34*, |
|  |  |  | *\_35*, |
|  |  |  | *\_36*, |
|  |  |  | *\_37*, |
|  |  |  | *\_38*, |
|  |  |  | *\_39*, |
|  |  |  | *\_40*, |
|  |  |  | *\_41*, |
|  |  |  | *\_42*, |
|  |  |  | *\_43*, |
|  |  |  | *\_44*, |
|  |  |  | *\_45*, |
|  |  |  | *\_46*, |
|  |  |  | *\_47*, |
|  |  |  | *\_48*, |
|  |  |  | *\_49*, |
|  |  |  | *\_50*, |
|  |  |  | *\_51*, |
|  |  |  | *\_52*, |
|  |  |  | *\_53*, |
|  |  |  | *\_54*, |
|  |  |  | *\_55*, |
|  |  |  | *\_56*, |
|  |  |  | *\_57*, |
|  |  |  | *\_58*, |
|  |  |  | *\_59*, |
|  |  |  | *\_60*, |
|  |  |  | *\_61*, |
|  |  |  | *\_62*, |
|  |  |  | *N*, |
|  |  |  | ... ) |

**Value:**

N

## [◆ ](#a80cbb3a182096676524d761113349bc8)UTIL\_BOOL

| #define UTIL\_BOOL | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_COMPL](#ae667bfa8e06a6b3c15266db678934ef3)([UTIL\_NOT](#a5db295294795b2ecad29f585dda49c49)(x))

[UTIL\_NOT](#a5db295294795b2ecad29f585dda49c49)

#define UTIL\_NOT(x)

**Definition** util\_internal.h:108

[UTIL\_COMPL](#ae667bfa8e06a6b3c15266db678934ef3)

#define UTIL\_COMPL(b)

**Definition** util\_internal.h:110

## [◆ ](#a7e7766e792d1638bfbbc9d0f328d3d0d)UTIL\_CAT

| #define UTIL\_CAT | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

[UTIL\_PRIMITIVE\_CAT](#a333f808696450134a9948dcc9e57e4ae)(a, \_\_VA\_ARGS\_\_)

[UTIL\_PRIMITIVE\_CAT](#a333f808696450134a9948dcc9e57e4ae)

#define UTIL\_PRIMITIVE\_CAT(a,...)

**Definition** util\_internal.h:105

## [◆ ](#afc586c7e633155a0a3db1614d7c76a83)UTIL\_CHECK

| #define UTIL\_CHECK | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CHECK\_N](#a1f1ff51e3bda754ee9561bd6d17277a4)(\_\_VA\_ARGS\_\_, 0,)

[UTIL\_CHECK\_N](#a1f1ff51e3bda754ee9561bd6d17277a4)

#define UTIL\_CHECK\_N(x, n,...)

**Definition** util\_internal.h:106

## [◆ ](#a1f1ff51e3bda754ee9561bd6d17277a4)UTIL\_CHECK\_N

| #define UTIL\_CHECK\_N | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *n*, |
|  |  |  | ... ) |

**Value:**

n

## [◆ ](#ae667bfa8e06a6b3c15266db678934ef3)UTIL\_COMPL

| #define UTIL\_COMPL | ( |  | *b* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_PRIMITIVE\_CAT](#a333f808696450134a9948dcc9e57e4ae)(UTIL\_COMPL\_, b)

## [◆ ](#af8b84b2dc23d37616d59e8e19a5c94dd)UTIL\_COMPL\_0

| #define UTIL\_COMPL\_0   1 |
| --- |

## [◆ ](#a69fb8790ad07ef2c00176a783c192390)UTIL\_COMPL\_1

| #define UTIL\_COMPL\_1   0 |
| --- |

## [◆ ](#a56279e773dc8d31b83161cc9526e8c56)UTIL\_EVAL

| #define UTIL\_EVAL | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_VA\_ARGS\_\_

## [◆ ](#a4393cb8f894e8a32385a49fbfaf841b2)UTIL\_EXPAND

| #define UTIL\_EXPAND | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_VA\_ARGS\_\_

## [◆ ](#a5db295294795b2ecad29f585dda49c49)UTIL\_NOT

| #define UTIL\_NOT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UTIL\_CHECK](#afc586c7e633155a0a3db1614d7c76a83)([UTIL\_PRIMITIVE\_CAT](#a333f808696450134a9948dcc9e57e4ae)(UTIL\_NOT\_, x))

[UTIL\_CHECK](#afc586c7e633155a0a3db1614d7c76a83)

#define UTIL\_CHECK(...)

**Definition** util\_internal.h:107

## [◆ ](#aeb84e257f8e817fc7436d032d579853b)UTIL\_NOT\_0

| #define UTIL\_NOT\_0   ~, 1, |
| --- |

## [◆ ](#a333f808696450134a9948dcc9e57e4ae)UTIL\_PRIMITIVE\_CAT

| #define UTIL\_PRIMITIVE\_CAT | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

a##\_\_VA\_ARGS\_\_

## [◆ ](#a3c54146013b856ef16ad45471b9fc7d1)UTIL\_REPEAT

| #define UTIL\_REPEAT | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

UTIL\_LISTIFY(\_\_VA\_ARGS\_\_)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [util\_internal.h](util__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
