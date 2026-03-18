---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/posix__types_8h_source.html
original_path: doxygen/html/posix__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

14#ifdef CONFIG\_NEWLIB\_LIBC

15#include <sys/\_pthreadtypes.h>

16#endif

17

18#include <[zephyr/kernel.h](kernel_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

24#if !defined(CONFIG\_ARCMWDT\_LIBC)

[ 25](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)typedef int [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df);

26#endif

27

28#ifndef \_\_useconds\_t\_defined

[ 29](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)typedef unsigned long [useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342);

30#endif

31

32/\* time related attributes \*/

33#if !defined(CONFIG\_NEWLIB\_LIBC) && !defined(CONFIG\_ARCMWDT\_LIBC)

34#ifndef \_\_clockid\_t\_defined

[ 35](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea);

36#endif

37#endif /\* !CONFIG\_NEWLIB\_LIBC && !CONFIG\_ARCMWDT\_LIBC \*/

38#ifndef \_\_timer\_t\_defined

[ 39](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)typedef unsigned long [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d);

40#endif

41

42/\* Thread attributes \*/

[ 43](structpthread__attr.md)struct [pthread\_attr](structpthread__attr.md) {

[ 44](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc) void \*[stack](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc);

[ 45](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [details](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899)[2];

46};

47

48#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

49 || defined(CONFIG\_ARCMWDT\_LIBC)

50typedef struct [pthread\_attr](structpthread__attr.md) pthread\_attr\_t;

51#endif

52

53BUILD\_ASSERT(sizeof(pthread\_attr\_t) >= sizeof(struct [pthread\_attr](structpthread__attr.md)));

54

[ 55](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec);

[ 56](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa);

57

58/\* Semaphore \*/

[ 59](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)typedef struct k\_sem [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e);

60

61/\* Mutex \*/

[ 62](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e);

63

[ 64](structpthread__mutexattr.md)struct [pthread\_mutexattr](structpthread__mutexattr.md) {

[ 65](structpthread__mutexattr.md#a2d6345d486a409d7e9942f102e7f0b59) unsigned char [type](structpthread__mutexattr.md#a2d6345d486a409d7e9942f102e7f0b59): 2;

[ 66](structpthread__mutexattr.md#afa55f47ff86cf3931d7bbb65de6697c6) bool [initialized](structpthread__mutexattr.md#afa55f47ff86cf3931d7bbb65de6697c6): 1;

67};

68#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

69 || defined(CONFIG\_ARCMWDT\_LIBC)

70typedef struct [pthread\_mutexattr](structpthread__mutexattr.md) pthread\_mutexattr\_t;

71#endif

72BUILD\_ASSERT(sizeof(pthread\_mutexattr\_t) >= sizeof(struct [pthread\_mutexattr](structpthread__mutexattr.md)));

73

74/\* Condition variables \*/

[ 75](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e);

76

[ 77](structpthread__condattr.md)struct [pthread\_condattr](structpthread__condattr.md) {

[ 78](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96) [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) [clock](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96);

79};

80

81#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

82 || defined(CONFIG\_ARCMWDT\_LIBC)

83typedef struct [pthread\_condattr](structpthread__condattr.md) pthread\_condattr\_t;

84#endif

85BUILD\_ASSERT(sizeof(pthread\_condattr\_t) >= sizeof(struct [pthread\_condattr](structpthread__condattr.md)));

86

87/\* Barrier \*/

[ 88](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2);

89

[ 90](structpthread__barrierattr.md)typedef struct [pthread\_barrierattr](structpthread__barrierattr.md) {

[ 91](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86) int [pshared](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86);

[ 92](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)} [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b);

93

[ 94](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f);

95

[ 96](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6);

97

[ 98](structpthread__once.md)struct [pthread\_once](structpthread__once.md) {

[ 99](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46) bool [flag](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46);

100};

101

102#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

103 || defined(CONFIG\_ARCMWDT\_LIBC)

104typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pthread\_key\_t;

105typedef struct [pthread\_once](structpthread__once.md) pthread\_once\_t;

106#endif

107

108/\* Newlib typedefs pthread\_once\_t as a struct with two ints \*/

109BUILD\_ASSERT(sizeof(pthread\_once\_t) >= sizeof(struct [pthread\_once](structpthread__once.md)));

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* ZEPHYR\_INCLUDE\_POSIX\_TYPES\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)

uint32\_t pthread\_cond\_t

**Definition** posix\_types.h:75

[useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)

unsigned long useconds\_t

**Definition** posix\_types.h:29

[pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)

uint32\_t pthread\_spinlock\_t

**Definition** posix\_types.h:56

[pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)

struct pthread\_barrierattr pthread\_barrierattr\_t

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:25

[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)

uint32\_t pthread\_t

**Definition** posix\_types.h:55

[pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)

uint32\_t pthread\_mutex\_t

**Definition** posix\_types.h:62

[pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)

uint32\_t pthread\_rwlockattr\_t

**Definition** posix\_types.h:94

[timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)

unsigned long timer\_t

**Definition** posix\_types.h:39

[clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea)

uint32\_t clockid\_t

**Definition** posix\_types.h:35

[pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)

uint32\_t pthread\_rwlock\_t

**Definition** posix\_types.h:96

[pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)

uint32\_t pthread\_barrier\_t

**Definition** posix\_types.h:88

[sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)

struct k\_sem sem\_t

**Definition** posix\_types.h:59

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[pthread\_attr](structpthread__attr.md)

**Definition** posix\_types.h:43

[pthread\_attr::stack](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc)

void \* stack

**Definition** posix\_types.h:44

[pthread\_attr::details](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899)

uint32\_t details[2]

**Definition** posix\_types.h:45

[pthread\_barrierattr](structpthread__barrierattr.md)

**Definition** posix\_types.h:90

[pthread\_barrierattr::pshared](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86)

int pshared

**Definition** posix\_types.h:91

[pthread\_condattr](structpthread__condattr.md)

**Definition** posix\_types.h:77

[pthread\_condattr::clock](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96)

clockid\_t clock

**Definition** posix\_types.h:78

[pthread\_mutexattr](structpthread__mutexattr.md)

**Definition** posix\_types.h:64

[pthread\_mutexattr::type](structpthread__mutexattr.md#a2d6345d486a409d7e9942f102e7f0b59)

unsigned char type

**Definition** posix\_types.h:65

[pthread\_mutexattr::initialized](structpthread__mutexattr.md#afa55f47ff86cf3931d7bbb65de6697c6)

bool initialized

**Definition** posix\_types.h:66

[pthread\_once](structpthread__once.md)

**Definition** posix\_types.h:98

[pthread\_once::flag](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46)

bool flag

**Definition** posix\_types.h:99

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [posix\_types.h](posix__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
