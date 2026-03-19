---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/atomic__c_8h_source.html
original_path: doxygen/html/atomic__c_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic\_c.h

[Go to the documentation of this file.](atomic__c_8h.md)

1/\*

2 \* Copyright (c) 1997-2015, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_C\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_C\_H\_

9

10/\* Included from <atomic.h> \*/

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16/\* Simple and correct (but very slow) implementation of atomic

17 \* primitives that require nothing more than kernel interrupt locking.

18 \*/

19

[ 20](atomic__c_8h.md#ab879da5aa1ffcc317adc664c016586f7)\_\_syscall bool [atomic\_cas](atomic__c_8h.md#ab879da5aa1ffcc317adc664c016586f7)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value,

21 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value);

22

[ 23](atomic__c_8h.md#a98f03db5ef2b36ff3412506a7f6d9558)\_\_syscall bool [atomic\_ptr\_cas](atomic__c_8h.md#a98f03db5ef2b36ff3412506a7f6d9558)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value,

24 [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value);

25

[ 26](atomic__c_8h.md#a518c07595daaca29a9e53071ed59c9c0)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_add](atomic__c_8h.md#a518c07595daaca29a9e53071ed59c9c0)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

27

[ 28](atomic__c_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_sub](atomic__c_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

29

[ 30](atomic__c_8h.md#a66487deb6817076501dd9160537fc06a)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_inc](atomic__c_8h.md#a66487deb6817076501dd9160537fc06a)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

31{

32 return [atomic\_add](atomic__c_8h.md#a518c07595daaca29a9e53071ed59c9c0)(target, 1);

33

34}

35

[ 36](atomic__c_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_dec](atomic__c_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

37{

38 return [atomic\_sub](atomic__c_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)(target, 1);

39

40}

41

[ 42](atomic__c_8h.md#a33bb426a17535bd1022895a7e44b32fa)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_get](atomic__c_8h.md#a33bb426a17535bd1022895a7e44b32fa)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

43

[ 44](atomic__c_8h.md#a250c4672ce7749261bdb8b2f0c767da2)[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_get](atomic__c_8h.md#a250c4672ce7749261bdb8b2f0c767da2)(const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target);

45

[ 46](atomic__c_8h.md#a5f0555245d8932c2e7f7e94575e1a095)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_set](atomic__c_8h.md#a5f0555245d8932c2e7f7e94575e1a095)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

47

[ 48](atomic__c_8h.md#a3a57fd7f76f84e0f5800878b8f81fc35)\_\_syscall [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_set](atomic__c_8h.md#a3a57fd7f76f84e0f5800878b8f81fc35)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value);

49

[ 50](atomic__c_8h.md#a45ccf5a7d636206f0673139ac393946f)static inline [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_clear](atomic__c_8h.md#a45ccf5a7d636206f0673139ac393946f)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target)

51{

52 return [atomic\_set](atomic__c_8h.md#a5f0555245d8932c2e7f7e94575e1a095)(target, 0);

53

54}

55

[ 56](atomic__c_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)static inline [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_clear](atomic__c_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target)

57{

58 return [atomic\_ptr\_set](atomic__c_8h.md#a3a57fd7f76f84e0f5800878b8f81fc35)(target, NULL);

59

60}

61

[ 62](atomic__c_8h.md#a1564a44a260e7d0d02e30ae045a99764)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_or](atomic__c_8h.md#a1564a44a260e7d0d02e30ae045a99764)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

63

[ 64](atomic__c_8h.md#a18592bcf38d667fb9b428f81ea691bd4)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_xor](atomic__c_8h.md#a18592bcf38d667fb9b428f81ea691bd4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

65

[ 66](atomic__c_8h.md#a4bc1f6a6f5d98eef742b4541d235811d)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_and](atomic__c_8h.md#a4bc1f6a6f5d98eef742b4541d235811d)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

67

[ 68](atomic__c_8h.md#a3e954286e40de73e45598a00a0a2b864)\_\_syscall [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_nand](atomic__c_8h.md#a3e954286e40de73e45598a00a0a2b864)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

69

70#ifdef \_\_cplusplus

71}

72#endif

73

74#ifdef CONFIG\_ATOMIC\_OPERATIONS\_C

75

76#ifndef DISABLE\_SYSCALL\_TRACING

77/\* Skip defining macros of atomic\_\*() for syscall tracing.

78 \* Compiler does not like "({ ... tracing code ... })" and complains

79 \*

80 \* error: expected identifier or '(' before '{' token

81 \*

82 \* ... even though there is a '(' before '{'.

83 \*/

84#define DISABLE\_SYSCALL\_TRACING

85#define \_REMOVE\_DISABLE\_SYSCALL\_TRACING

86#endif

87

88#include <zephyr/syscalls/atomic\_c.h>

89

90#ifdef \_REMOVE\_DISABLE\_SYSCALL\_TRACING

91#undef DISABLE\_SYSCALL\_TRACING

92#undef \_REMOVE\_DISABLE\_SYSCALL\_TRACING

93#endif

94

95#endif

96

97#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_C\_H\_ \*/

[atomic\_dec](atomic__c_8h.md#a0adecd95c4d47987c404a31e87c1d5c5)

static atomic\_val\_t atomic\_dec(atomic\_t \*target)

**Definition** atomic\_c.h:36

[atomic\_or](atomic__c_8h.md#a1564a44a260e7d0d02e30ae045a99764)

atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)

[atomic\_xor](atomic__c_8h.md#a18592bcf38d667fb9b428f81ea691bd4)

atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)

[atomic\_ptr\_get](atomic__c_8h.md#a250c4672ce7749261bdb8b2f0c767da2)

atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)

[atomic\_get](atomic__c_8h.md#a33bb426a17535bd1022895a7e44b32fa)

atomic\_val\_t atomic\_get(const atomic\_t \*target)

[atomic\_ptr\_set](atomic__c_8h.md#a3a57fd7f76f84e0f5800878b8f81fc35)

atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)

[atomic\_nand](atomic__c_8h.md#a3e954286e40de73e45598a00a0a2b864)

atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)

[atomic\_clear](atomic__c_8h.md#a45ccf5a7d636206f0673139ac393946f)

static atomic\_val\_t atomic\_clear(atomic\_t \*target)

**Definition** atomic\_c.h:50

[atomic\_and](atomic__c_8h.md#a4bc1f6a6f5d98eef742b4541d235811d)

atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)

[atomic\_add](atomic__c_8h.md#a518c07595daaca29a9e53071ed59c9c0)

atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)

[atomic\_set](atomic__c_8h.md#a5f0555245d8932c2e7f7e94575e1a095)

atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)

[atomic\_inc](atomic__c_8h.md#a66487deb6817076501dd9160537fc06a)

static atomic\_val\_t atomic\_inc(atomic\_t \*target)

**Definition** atomic\_c.h:30

[atomic\_sub](atomic__c_8h.md#a84ab58fd0a6dbbf1bf675722b5900bd7)

atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)

[atomic\_ptr\_clear](atomic__c_8h.md#a8b511a7b5bccc7bc6b6e13526f87c0f3)

static atomic\_ptr\_val\_t atomic\_ptr\_clear(atomic\_ptr\_t \*target)

**Definition** atomic\_c.h:56

[atomic\_ptr\_cas](atomic__c_8h.md#a98f03db5ef2b36ff3412506a7f6d9558)

bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t old\_value, atomic\_ptr\_val\_t new\_value)

[atomic\_cas](atomic__c_8h.md#ab879da5aa1ffcc317adc664c016586f7)

bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)

atomic\_ptr\_t atomic\_ptr\_val\_t

**Definition** atomic\_types.h:18

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic\_c.h](atomic__c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
