---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/posix__types_8h_source.html
original_path: doxygen/html/posix__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

18#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)typedef int [pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df);

25

26#ifndef \_\_useconds\_t\_defined

[ 27](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)typedef unsigned long [useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342);

28#endif

29

30/\* time related attributes \*/

31#if !defined(CONFIG\_NEWLIB\_LIBC) && !defined(CONFIG\_ARCMWDT\_LIBC)

32#ifndef \_\_clockid\_t\_defined

[ 33](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea);

34#endif

35#endif /\* !CONFIG\_NEWLIB\_LIBC && !CONFIG\_ARCMWDT\_LIBC \*/

36#ifndef \_\_timer\_t\_defined

[ 37](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)typedef unsigned long [timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d);

38#endif

39

40/\* Thread attributes \*/

[ 41](structpthread__attr.md)struct [pthread\_attr](structpthread__attr.md) {

[ 42](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc) void \*[stack](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc);

[ 43](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [details](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899)[2];

44};

45

46#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

47 || defined(CONFIG\_ARCMWDT\_LIBC)

48typedef struct [pthread\_attr](structpthread__attr.md) pthread\_attr\_t;

49#endif

50

51BUILD\_ASSERT(sizeof(pthread\_attr\_t) >= sizeof(struct [pthread\_attr](structpthread__attr.md)));

52

[ 53](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec);

[ 54](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa);

55

56/\* Semaphore \*/

[ 57](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)typedef struct k\_sem [sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e);

58

59/\* Mutex \*/

[ 60](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e);

61

[ 62](structpthread__mutexattr.md)struct [pthread\_mutexattr](structpthread__mutexattr.md) {

[ 63](structpthread__mutexattr.md#afaa0cd4d509e30112666bd89890ed030) int [type](structpthread__mutexattr.md#afaa0cd4d509e30112666bd89890ed030);

64};

65#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

66 || defined(CONFIG\_ARCMWDT\_LIBC)

67typedef struct [pthread\_mutexattr](structpthread__mutexattr.md) pthread\_mutexattr\_t;

68#endif

69BUILD\_ASSERT(sizeof(pthread\_mutexattr\_t) >= sizeof(struct [pthread\_mutexattr](structpthread__mutexattr.md)));

70

71/\* Condition variables \*/

[ 72](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e);

73

[ 74](structpthread__condattr.md)struct [pthread\_condattr](structpthread__condattr.md) {

[ 75](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96) [clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea) [clock](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96);

76};

77

78#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

79 || defined(CONFIG\_ARCMWDT\_LIBC)

80typedef struct [pthread\_condattr](structpthread__condattr.md) pthread\_condattr\_t;

81#endif

82BUILD\_ASSERT(sizeof(pthread\_condattr\_t) >= sizeof(struct [pthread\_condattr](structpthread__condattr.md)));

83

84/\* Barrier \*/

[ 85](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2);

86

[ 87](structpthread__barrierattr.md)typedef struct [pthread\_barrierattr](structpthread__barrierattr.md) {

[ 88](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86) int [pshared](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86);

[ 89](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)} [pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b);

90

[ 91](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f);

92

[ 93](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6);

94

[ 95](structpthread__once.md)struct [pthread\_once](structpthread__once.md) {

[ 96](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46) bool [flag](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46);

97};

98

99#if defined(CONFIG\_MINIMAL\_LIBC) || defined(CONFIG\_PICOLIBC) || defined(CONFIG\_ARMCLANG\_STD\_LIBC) \

100 || defined(CONFIG\_ARCMWDT\_LIBC)

101typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pthread\_key\_t;

102typedef struct [pthread\_once](structpthread__once.md) pthread\_once\_t;

103#endif

104

105/\* Newlib typedefs pthread\_once\_t as a struct with two ints \*/

106BUILD\_ASSERT(sizeof(pthread\_once\_t) >= sizeof(struct [pthread\_once](structpthread__once.md)));

107

108#ifdef \_\_cplusplus

109}

110#endif

111

112#endif /\* ZEPHYR\_INCLUDE\_POSIX\_TYPES\_H\_ \*/

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[pthread\_cond\_t](posix__types_8h.md#a1b893f49dfdf497be09c04a0e40f425e)

uint32\_t pthread\_cond\_t

**Definition** posix\_types.h:72

[useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)

unsigned long useconds\_t

**Definition** posix\_types.h:27

[pthread\_spinlock\_t](posix__types_8h.md#a1d9c308dd59bf38ff0a7a45020d0aefa)

uint32\_t pthread\_spinlock\_t

**Definition** posix\_types.h:54

[pthread\_barrierattr\_t](posix__types_8h.md#a24d58850626c8022bf4bbd5d2628615b)

struct pthread\_barrierattr pthread\_barrierattr\_t

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:24

[pthread\_t](posix__types_8h.md#a405938c67e9c568fde9993c7e14d58ec)

uint32\_t pthread\_t

**Definition** posix\_types.h:53

[pthread\_mutex\_t](posix__types_8h.md#a465eb2b962de164efdc8ce957025de7e)

uint32\_t pthread\_mutex\_t

**Definition** posix\_types.h:60

[pthread\_rwlockattr\_t](posix__types_8h.md#a4e92e3fbb4be682babbb6796af90b50f)

uint32\_t pthread\_rwlockattr\_t

**Definition** posix\_types.h:91

[timer\_t](posix__types_8h.md#aa37fa84abebf94371f0c8426c2fc614d)

unsigned long timer\_t

**Definition** posix\_types.h:37

[clockid\_t](posix__types_8h.md#aac50bafb9f9a838df14fab213146caea)

uint32\_t clockid\_t

**Definition** posix\_types.h:33

[pthread\_rwlock\_t](posix__types_8h.md#acd12f65541fede33b6226f646e900ea6)

uint32\_t pthread\_rwlock\_t

**Definition** posix\_types.h:93

[pthread\_barrier\_t](posix__types_8h.md#aeb637552f63e4c249e7aaeb2905f3db2)

uint32\_t pthread\_barrier\_t

**Definition** posix\_types.h:85

[sem\_t](posix__types_8h.md#afb4edc6a51d66a7a352424942b631a1e)

struct k\_sem sem\_t

**Definition** posix\_types.h:57

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[pthread\_attr](structpthread__attr.md)

**Definition** posix\_types.h:41

[pthread\_attr::stack](structpthread__attr.md#a71b91b602b93019a612a1b83eec974cc)

void \* stack

**Definition** posix\_types.h:42

[pthread\_attr::details](structpthread__attr.md#af30d7716808f52200a0b52cdd3bec899)

uint32\_t details[2]

**Definition** posix\_types.h:43

[pthread\_barrierattr](structpthread__barrierattr.md)

**Definition** posix\_types.h:87

[pthread\_barrierattr::pshared](structpthread__barrierattr.md#a50ef34671e6743cc59c895dd878c4a86)

int pshared

**Definition** posix\_types.h:88

[pthread\_condattr](structpthread__condattr.md)

**Definition** posix\_types.h:74

[pthread\_condattr::clock](structpthread__condattr.md#ac8f29de493f72c650ea59c71305c3e96)

clockid\_t clock

**Definition** posix\_types.h:75

[pthread\_mutexattr](structpthread__mutexattr.md)

**Definition** posix\_types.h:62

[pthread\_mutexattr::type](structpthread__mutexattr.md#afaa0cd4d509e30112666bd89890ed030)

int type

**Definition** posix\_types.h:63

[pthread\_once](structpthread__once.md)

**Definition** posix\_types.h:95

[pthread\_once::flag](structpthread__once.md#a9b9825a6d106c358fc4f2e399418de46)

bool flag

**Definition** posix\_types.h:96

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [posix\_types.h](posix__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
