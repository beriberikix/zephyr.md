---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/posix__types_8h_source.html
original_path: doxygen/html/posix__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_types.h

[Go to the documentation of this file.](posix__types_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_TYPES\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_TYPES\_H\_

9

10#if !(defined(CONFIG\_ARCH\_POSIX) && defined(CONFIG\_EXTERNAL\_LIBC))

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12#endif

13

14#if !defined(\_CLOCK\_T\_DECLARED) && !defined(\_\_clock\_t\_defined)

[ 15](posix__types_8h.md#a3b55f88f25d2c571de53a365ad658426)typedef unsigned long [clock\_t](posix__types_8h.md#a3b55f88f25d2c571de53a365ad658426);

16#define \_CLOCK\_T\_DECLARED

17#define \_\_clock\_t\_defined

18#endif

19

20#if !defined(\_CLOCKID\_T\_DECLARED) && !defined(\_\_clockid\_t\_defined)

[ 21](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af)typedef unsigned long [clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af);

22#define \_CLOCKID\_T\_DECLARED

23#define \_\_clockid\_t\_defined

24#endif

25

26#ifdef CONFIG\_NEWLIB\_LIBC

27#include <sys/\_pthreadtypes.h>

28#endif

29

30#include <[zephyr/kernel.h](kernel_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

36#if !defined(\_DEV\_T\_DECLARED) && !defined(\_\_dev\_t\_defined)

[ 37](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9)typedef int [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9);

38#define \_DEV\_T\_DECLARED

39#define \_\_dev\_t\_defined

40#endif

41

42#if !defined(\_INO\_T\_DECLARED) && !defined(\_\_ino\_t\_defined)

[ 43](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c)typedef int [ino\_t](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c);

44#define \_INO\_T\_DECLARED

45#define \_\_ino\_t\_defined

46#endif

47

48#if !defined(\_NLINK\_T\_DECLARED) && !defined(\_\_nlink\_t\_defined)

[ 49](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e)typedef unsigned short [nlink\_t](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e);

50#define \_NLINK\_T\_DECLARED

51#define \_\_nlink\_t\_defined

52#endif

53

54#if !defined(\_UID\_T\_DECLARED) && !defined(\_\_uid\_t\_defined)

[ 55](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9)typedef unsigned short [uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9);

56#define \_UID\_T\_DECLARED

57#define \_\_uid\_t\_defined

58#endif

59

60#if !defined(\_GID\_T\_DECLARED) && !defined(\_\_gid\_t\_defined)

[ 61](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)typedef unsigned short [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8);

62#define \_GID\_T\_DECLARED

63#define \_\_gid\_t\_defined

64#endif

65

66#if !defined(\_BLKSIZE\_T\_DECLARED) && !defined(\_\_blksize\_t\_defined)

[ 67](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b)typedef unsigned long [blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b);

68#define \_BLKSIZE\_T\_DECLARED

69#define \_\_blksize\_t\_defined

70#endif

71

72#if !defined(\_BLKCNT\_T\_DECLARED) && !defined(\_\_blkcnt\_t\_defined)

[ 73](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347)typedef unsigned long [blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347);

74#define \_BLKCNT\_T\_DECLARED

75#define \_\_blkcnt\_t\_defined

76#endif

77

78#if !defined(CONFIG\_ARCMWDT\_LIBC)

[ 79](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)typedef int [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df);

80#endif

81

82#ifndef \_\_useconds\_t\_defined

[ 83](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)typedef unsigned long [useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342);

84#endif

85

86/\* time related attributes \*/

87#if !defined(CONFIG\_NEWLIB\_LIBC) && !defined(CONFIG\_ARCMWDT\_LIBC)

88#if !defined(\_\_clockid\_t\_defined) && !defined(\_CLOCKID\_T\_DECLARED)

89typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af);

90#endif

91#endif /\* !CONFIG\_NEWLIB\_LIBC && !CONFIG\_ARCMWDT\_LIBC \*/

92#if !defined(\_\_timer\_t\_defined) && !defined(\_TIMER\_T\_DECLARED)

[ 93](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)typedef unsigned long [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d);

94#endif

95

96/\* Thread attributes \*/

[ 97](structpthread__attr.md)struct [pthread\_attr](structpthread__attr.md) {

[ 98](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc) void \*[stack](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc);

[ 99](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [details](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899)[2];

100};

101

102#if !defined(CONFIG\_NEWLIB\_LIBC)

[ 103](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a)typedef struct [pthread\_attr](structpthread__attr.md) [pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a);

104BUILD\_ASSERT(sizeof([pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a)) >= sizeof(struct [pthread\_attr](structpthread__attr.md)));

105#endif

106

[ 107](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec);

[ 108](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa);

109

110/\* Semaphore \*/

[ 111](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)typedef struct k\_sem [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e);

112

113/\* Mutex \*/

[ 114](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e);

115

[ 116](structpthread__mutexattr.md)struct [pthread\_mutexattr](structpthread__mutexattr.md) {

[ 117](structpthread__mutexattr.md#a2d6345d486a409d7e9942f102e7f0b59) unsigned char [type](structpthread__mutexattr.md#a2d6345d486a409d7e9942f102e7f0b59): 2;

[ 118](structpthread__mutexattr.md#afa55f47ff86cf3931d7bbb65de6697c6) bool [initialized](structpthread__mutexattr.md#afa55f47ff86cf3931d7bbb65de6697c6): 1;

119};

120#if !defined(CONFIG\_NEWLIB\_LIBC)

[ 121](posix__types_8h.md#a2489174ff5737a33443b0959f4278765)typedef struct [pthread\_mutexattr](structpthread__mutexattr.md) [pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765);

122BUILD\_ASSERT(sizeof([pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765)) >= sizeof(struct [pthread\_mutexattr](structpthread__mutexattr.md)));

123#endif

124

125/\* Condition variables \*/

[ 126](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e);

127

[ 128](structpthread__condattr.md)struct [pthread\_condattr](structpthread__condattr.md) {

[ 129](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96) [clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af) [clock](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96);

130};

131

132#if !defined(CONFIG\_NEWLIB\_LIBC)

[ 133](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1)typedef struct [pthread\_condattr](structpthread__condattr.md) [pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1);

134BUILD\_ASSERT(sizeof([pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1)) >= sizeof(struct [pthread\_condattr](structpthread__condattr.md)));

135#endif

136

137/\* Barrier \*/

[ 138](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2);

139

[ 140](structpthread__barrierattr.md)typedef struct [pthread\_barrierattr](structpthread__barrierattr.md) {

[ 141](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86) int [pshared](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86);

[ 142](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)} [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b);

143

[ 144](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f);

145

[ 146](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6);

147

[ 148](structpthread__once.md)struct [pthread\_once](structpthread__once.md) {

[ 149](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46) bool [flag](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46);

150};

151

152#if !defined(CONFIG\_NEWLIB\_LIBC)

[ 153](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911);

[ 154](posix__types_8h.md#a2603a6fda916554839174bc7d8849297)typedef struct [pthread\_once](structpthread__once.md) [pthread\_once\_t](posix__types_8h.md#a2603a6fda916554839174bc7d8849297);

155/\* Newlib typedefs pthread\_once\_t as a struct with two ints \*/

156BUILD\_ASSERT(sizeof([pthread\_once\_t](posix__types_8h.md#a2603a6fda916554839174bc7d8849297)) >= sizeof(struct [pthread\_once](structpthread__once.md)));

157#endif

158

159#ifdef \_\_cplusplus

160}

161#endif

162

163#endif /\* ZEPHYR\_INCLUDE\_POSIX\_TYPES\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9)

int dev\_t

**Definition** posix\_types.h:37

[pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)

uint32\_t pthread\_cond\_t

**Definition** posix\_types.h:126

[useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)

unsigned long useconds\_t

**Definition** posix\_types.h:83

[pthread\_attr\_t](posix__types_8h.md#a1d96fa5809832849f591deef6cc7af7a)

struct pthread\_attr pthread\_attr\_t

**Definition** posix\_types.h:103

[pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)

uint32\_t pthread\_spinlock\_t

**Definition** posix\_types.h:108

[pthread\_mutexattr\_t](posix__types_8h.md#a2489174ff5737a33443b0959f4278765)

struct pthread\_mutexattr pthread\_mutexattr\_t

**Definition** posix\_types.h:121

[pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)

struct pthread\_barrierattr pthread\_barrierattr\_t

[pthread\_once\_t](posix__types_8h.md#a2603a6fda916554839174bc7d8849297)

struct pthread\_once pthread\_once\_t

**Definition** posix\_types.h:154

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:79

[gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)

unsigned short gid\_t

**Definition** posix\_types.h:61

[clock\_t](posix__types_8h.md#a3b55f88f25d2c571de53a365ad658426)

unsigned long clock\_t

**Definition** posix\_types.h:15

[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)

uint32\_t pthread\_t

**Definition** posix\_types.h:107

[pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)

uint32\_t pthread\_mutex\_t

**Definition** posix\_types.h:114

[pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)

uint32\_t pthread\_rwlockattr\_t

**Definition** posix\_types.h:144

[blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b)

unsigned long blksize\_t

**Definition** posix\_types.h:67

[clockid\_t](posix__types_8h.md#a6bb3206700910111f26e946bfbf0f2af)

unsigned long clockid\_t

**Definition** posix\_types.h:21

[uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9)

unsigned short uid\_t

**Definition** posix\_types.h:55

[ino\_t](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c)

int ino\_t

**Definition** posix\_types.h:43

[pthread\_key\_t](posix__types_8h.md#a8fd226393057ab7a8b17ac1c8b061911)

uint32\_t pthread\_key\_t

**Definition** posix\_types.h:153

[nlink\_t](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e)

unsigned short nlink\_t

**Definition** posix\_types.h:49

[pthread\_condattr\_t](posix__types_8h.md#a9f62774a7a4e1634e60fb611765251f1)

struct pthread\_condattr pthread\_condattr\_t

**Definition** posix\_types.h:133

[timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)

unsigned long timer\_t

**Definition** posix\_types.h:93

[blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347)

unsigned long blkcnt\_t

**Definition** posix\_types.h:73

[pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)

uint32\_t pthread\_rwlock\_t

**Definition** posix\_types.h:146

[pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)

uint32\_t pthread\_barrier\_t

**Definition** posix\_types.h:138

[sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)

struct k\_sem sem\_t

**Definition** posix\_types.h:111

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[pthread\_attr](structpthread__attr.md)

**Definition** posix\_types.h:97

[pthread\_attr::stack](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc)

void \* stack

**Definition** posix\_types.h:98

[pthread\_attr::details](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899)

uint32\_t details[2]

**Definition** posix\_types.h:99

[pthread\_barrierattr](structpthread__barrierattr.md)

**Definition** posix\_types.h:140

[pthread\_barrierattr::pshared](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86)

int pshared

**Definition** posix\_types.h:141

[pthread\_condattr](structpthread__condattr.md)

**Definition** posix\_types.h:128

[pthread\_condattr::clock](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96)

clockid\_t clock

**Definition** posix\_types.h:129

[pthread\_mutexattr](structpthread__mutexattr.md)

**Definition** posix\_types.h:116

[pthread\_mutexattr::type](structpthread__mutexattr.md#a2d6345d486a409d7e9942f102e7f0b59)

unsigned char type

**Definition** posix\_types.h:117

[pthread\_mutexattr::initialized](structpthread__mutexattr.md#afa55f47ff86cf3931d7bbb65de6697c6)

bool initialized

**Definition** posix\_types.h:118

[pthread\_once](structpthread__once.md)

**Definition** posix\_types.h:148

[pthread\_once::flag](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46)

bool flag

**Definition** posix\_types.h:149

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [posix\_types.h](posix__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
