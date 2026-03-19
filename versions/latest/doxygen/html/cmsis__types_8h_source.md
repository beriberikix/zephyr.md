---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cmsis__types_8h_source.html
original_path: doxygen/html/cmsis__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_types.h

[Go to the documentation of this file.](cmsis__types_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_CMSIS\_TYPES\_H\_

8#define ZEPHYR\_INCLUDE\_CMSIS\_TYPES\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <zephyr/portability/cmsis\_os2.h>

13

[ 15](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)#define CMSIS\_OBJ\_NAME\_MAX\_LEN 16

16

[ 23](structcmsis__rtos__thread__cb.md)struct [cmsis\_rtos\_thread\_cb](structcmsis__rtos__thread__cb.md) {

[ 24](structcmsis__rtos__thread__cb.md#a4105af0bf74ca757ded20f1cf8d8a32b) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structcmsis__rtos__thread__cb.md#a4105af0bf74ca757ded20f1cf8d8a32b);

25 struct [k\_thread](structk__thread.md) z\_thread;

[ 26](structcmsis__rtos__thread__cb.md#a1141cf4f98f7942e4b303673ef0c2bb0) struct [k\_poll\_signal](structk__poll__signal.md) [poll\_signal](structcmsis__rtos__thread__cb.md#a1141cf4f98f7942e4b303673ef0c2bb0);

[ 27](structcmsis__rtos__thread__cb.md#a536f754d15b6bc836de9d469ab5cb23a) struct [k\_poll\_event](structk__poll__event.md) [poll\_event](structcmsis__rtos__thread__cb.md#a536f754d15b6bc836de9d469ab5cb23a);

[ 28](structcmsis__rtos__thread__cb.md#af3061152f322434776156246c08651dc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [signal\_results](structcmsis__rtos__thread__cb.md#af3061152f322434776156246c08651dc);

[ 29](structcmsis__rtos__thread__cb.md#ac97e3f4f2aa71804a578392f154fc942) char [name](structcmsis__rtos__thread__cb.md#ac97e3f4f2aa71804a578392f154fc942)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

[ 30](structcmsis__rtos__thread__cb.md#aa1aabdd8a7d59b0939e9c3822af26700) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attr\_bits](structcmsis__rtos__thread__cb.md#aa1aabdd8a7d59b0939e9c3822af26700);

[ 31](structcmsis__rtos__thread__cb.md#ac07201f80219ef4e8d6bb4244de7d82f) struct k\_sem [join\_guard](structcmsis__rtos__thread__cb.md#ac07201f80219ef4e8d6bb4244de7d82f);

[ 32](structcmsis__rtos__thread__cb.md#a39207f4007b39e9295507e63b1194c04) char [has\_joined](structcmsis__rtos__thread__cb.md#a39207f4007b39e9295507e63b1194c04);

33};

34

[ 41](structcmsis__rtos__timer__cb.md)struct [cmsis\_rtos\_timer\_cb](structcmsis__rtos__timer__cb.md) {

42 struct k\_timer z\_timer;

[ 43](structcmsis__rtos__timer__cb.md#a9054df0b4e92854d20c0d202eaeea66c) osTimerType\_t [type](structcmsis__rtos__timer__cb.md#a9054df0b4e92854d20c0d202eaeea66c);

[ 44](structcmsis__rtos__timer__cb.md#a16a1cf8a0bc2eba418b64e1a35782526) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [status](structcmsis__rtos__timer__cb.md#a16a1cf8a0bc2eba418b64e1a35782526);

[ 45](structcmsis__rtos__timer__cb.md#a2148d26c2386672ea72391839826e502) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__timer__cb.md#a2148d26c2386672ea72391839826e502);

[ 46](structcmsis__rtos__timer__cb.md#aeea9a9cb04879526375d5eb51733dfe5) char [name](structcmsis__rtos__timer__cb.md#aeea9a9cb04879526375d5eb51733dfe5)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

[ 47](structcmsis__rtos__timer__cb.md#a8819befff072e0a3cda4bf855e24dbf1) void (\*[callback\_function](structcmsis__rtos__timer__cb.md#a8819befff072e0a3cda4bf855e24dbf1))(void \*argument);

[ 48](structcmsis__rtos__timer__cb.md#a854205b98234c4aeee8056d6bb64c4a3) void \*[arg](structcmsis__rtos__timer__cb.md#a854205b98234c4aeee8056d6bb64c4a3);

49};

50

[ 57](structcmsis__rtos__mutex__cb.md)struct [cmsis\_rtos\_mutex\_cb](structcmsis__rtos__mutex__cb.md) {

58 struct [k\_mutex](structk__mutex.md) z\_mutex;

[ 59](structcmsis__rtos__mutex__cb.md#aa7df7554bcdeb9e14ce38771392482dc) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__mutex__cb.md#aa7df7554bcdeb9e14ce38771392482dc);

[ 60](structcmsis__rtos__mutex__cb.md#a007a75f7c1f6913922f05c63218eadff) char [name](structcmsis__rtos__mutex__cb.md#a007a75f7c1f6913922f05c63218eadff)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

[ 61](structcmsis__rtos__mutex__cb.md#a43e50207a92b6f5c1f4add8a537352e5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](structcmsis__rtos__mutex__cb.md#a43e50207a92b6f5c1f4add8a537352e5);

62};

63

[ 70](structcmsis__rtos__semaphore__cb.md)struct [cmsis\_rtos\_semaphore\_cb](structcmsis__rtos__semaphore__cb.md) {

71 struct k\_sem z\_semaphore;

[ 72](structcmsis__rtos__semaphore__cb.md#a375bd0bcaa18d236449a3ceb2e21eeb2) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__semaphore__cb.md#a375bd0bcaa18d236449a3ceb2e21eeb2);

[ 73](structcmsis__rtos__semaphore__cb.md#a0fcd03ebf15c9bccb348180c601daa6a) char [name](structcmsis__rtos__semaphore__cb.md#a0fcd03ebf15c9bccb348180c601daa6a)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

74};

75

[ 82](structcmsis__rtos__mempool__cb.md)struct [cmsis\_rtos\_mempool\_cb](structcmsis__rtos__mempool__cb.md) {

83 struct k\_mem\_slab z\_mslab;

[ 84](structcmsis__rtos__mempool__cb.md#a1a05ccc77a02197729db3e80f235e833) void \*[pool](structcmsis__rtos__mempool__cb.md#a1a05ccc77a02197729db3e80f235e833);

[ 85](structcmsis__rtos__mempool__cb.md#ad8d9c65555e6cba4d3d016ef0decf99f) char [is\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#ad8d9c65555e6cba4d3d016ef0decf99f);

[ 86](structcmsis__rtos__mempool__cb.md#aad9668c546fcbbb232faf0790554cc60) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#aad9668c546fcbbb232faf0790554cc60);

[ 87](structcmsis__rtos__mempool__cb.md#ac2ea885600f6fb48b2e0e17c068cce65) char [name](structcmsis__rtos__mempool__cb.md#ac2ea885600f6fb48b2e0e17c068cce65)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

88};

89

[ 96](structcmsis__rtos__msgq__cb.md)struct [cmsis\_rtos\_msgq\_cb](structcmsis__rtos__msgq__cb.md) {

97 struct [k\_msgq](structk__msgq.md) z\_msgq;

[ 98](structcmsis__rtos__msgq__cb.md#a1909f69f4b0f89a3aad0eec03fce9f7a) void \*[pool](structcmsis__rtos__msgq__cb.md#a1909f69f4b0f89a3aad0eec03fce9f7a);

[ 99](structcmsis__rtos__msgq__cb.md#ab867f14725ef4c114b16d9ff4362b085) char [is\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#ab867f14725ef4c114b16d9ff4362b085);

[ 100](structcmsis__rtos__msgq__cb.md#aba512f3212825e79a291690e7577506e) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#aba512f3212825e79a291690e7577506e);

[ 101](structcmsis__rtos__msgq__cb.md#ad366606b20635db344f004bd60effd5f) char [name](structcmsis__rtos__msgq__cb.md#ad366606b20635db344f004bd60effd5f)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

102};

103

[ 110](structcmsis__rtos__event__cb.md)struct [cmsis\_rtos\_event\_cb](structcmsis__rtos__event__cb.md) {

[ 111](structcmsis__rtos__event__cb.md#ae9750a0ffc6a3f83916760d67a4edb63) struct [k\_poll\_signal](structk__poll__signal.md) [poll\_signal](structcmsis__rtos__event__cb.md#ae9750a0ffc6a3f83916760d67a4edb63);

[ 112](structcmsis__rtos__event__cb.md#a3b96b29e2866966d1ddd0ff71a1bbfac) struct [k\_poll\_event](structk__poll__event.md) [poll\_event](structcmsis__rtos__event__cb.md#a3b96b29e2866966d1ddd0ff71a1bbfac);

[ 113](structcmsis__rtos__event__cb.md#ab9218a355d3b3a943a1a9eea4656160a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [signal\_results](structcmsis__rtos__event__cb.md#ab9218a355d3b3a943a1a9eea4656160a);

[ 114](structcmsis__rtos__event__cb.md#af1898a60748c3a1f3c2d2839eecaff64) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__event__cb.md#af1898a60748c3a1f3c2d2839eecaff64);

[ 115](structcmsis__rtos__event__cb.md#ac22399c14a5fbe5a86246b985d59c8f1) char [name](structcmsis__rtos__event__cb.md#ac22399c14a5fbe5a86246b985d59c8f1)[[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)];

116};

117

118#endif

[CMSIS\_OBJ\_NAME\_MAX\_LEN](cmsis__types_8h.md#a3df1d8e10c95ee9d6ac04e757327e051)

#define CMSIS\_OBJ\_NAME\_MAX\_LEN

Size for names of RTOS objects.

**Definition** cmsis\_types.h:15

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[cmsis\_rtos\_event\_cb](structcmsis__rtos__event__cb.md)

Control block for a CMSIS-RTOSv2 event flag.

**Definition** cmsis\_types.h:110

[cmsis\_rtos\_event\_cb::poll\_event](structcmsis__rtos__event__cb.md#a3b96b29e2866966d1ddd0ff71a1bbfac)

struct k\_poll\_event poll\_event

**Definition** cmsis\_types.h:112

[cmsis\_rtos\_event\_cb::signal\_results](structcmsis__rtos__event__cb.md#ab9218a355d3b3a943a1a9eea4656160a)

uint32\_t signal\_results

**Definition** cmsis\_types.h:113

[cmsis\_rtos\_event\_cb::name](structcmsis__rtos__event__cb.md#ac22399c14a5fbe5a86246b985d59c8f1)

char name[16]

**Definition** cmsis\_types.h:115

[cmsis\_rtos\_event\_cb::poll\_signal](structcmsis__rtos__event__cb.md#ae9750a0ffc6a3f83916760d67a4edb63)

struct k\_poll\_signal poll\_signal

**Definition** cmsis\_types.h:111

[cmsis\_rtos\_event\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__event__cb.md#af1898a60748c3a1f3c2d2839eecaff64)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:114

[cmsis\_rtos\_mempool\_cb](structcmsis__rtos__mempool__cb.md)

Control block for a CMSIS-RTOSv2 memory pool.

**Definition** cmsis\_types.h:82

[cmsis\_rtos\_mempool\_cb::pool](structcmsis__rtos__mempool__cb.md#a1a05ccc77a02197729db3e80f235e833)

void \* pool

**Definition** cmsis\_types.h:84

[cmsis\_rtos\_mempool\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#aad9668c546fcbbb232faf0790554cc60)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:86

[cmsis\_rtos\_mempool\_cb::name](structcmsis__rtos__mempool__cb.md#ac2ea885600f6fb48b2e0e17c068cce65)

char name[16]

**Definition** cmsis\_types.h:87

[cmsis\_rtos\_mempool\_cb::is\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#ad8d9c65555e6cba4d3d016ef0decf99f)

char is\_dynamic\_allocation

**Definition** cmsis\_types.h:85

[cmsis\_rtos\_msgq\_cb](structcmsis__rtos__msgq__cb.md)

Control block for a CMSIS-RTOSv2 message queue.

**Definition** cmsis\_types.h:96

[cmsis\_rtos\_msgq\_cb::pool](structcmsis__rtos__msgq__cb.md#a1909f69f4b0f89a3aad0eec03fce9f7a)

void \* pool

**Definition** cmsis\_types.h:98

[cmsis\_rtos\_msgq\_cb::is\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#ab867f14725ef4c114b16d9ff4362b085)

char is\_dynamic\_allocation

**Definition** cmsis\_types.h:99

[cmsis\_rtos\_msgq\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#aba512f3212825e79a291690e7577506e)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:100

[cmsis\_rtos\_msgq\_cb::name](structcmsis__rtos__msgq__cb.md#ad366606b20635db344f004bd60effd5f)

char name[16]

**Definition** cmsis\_types.h:101

[cmsis\_rtos\_mutex\_cb](structcmsis__rtos__mutex__cb.md)

Control block for a CMSIS-RTOSv2 mutex.

**Definition** cmsis\_types.h:57

[cmsis\_rtos\_mutex\_cb::name](structcmsis__rtos__mutex__cb.md#a007a75f7c1f6913922f05c63218eadff)

char name[16]

**Definition** cmsis\_types.h:60

[cmsis\_rtos\_mutex\_cb::state](structcmsis__rtos__mutex__cb.md#a43e50207a92b6f5c1f4add8a537352e5)

uint32\_t state

**Definition** cmsis\_types.h:61

[cmsis\_rtos\_mutex\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__mutex__cb.md#aa7df7554bcdeb9e14ce38771392482dc)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:59

[cmsis\_rtos\_semaphore\_cb](structcmsis__rtos__semaphore__cb.md)

Control block for a CMSIS-RTOSv2 semaphore.

**Definition** cmsis\_types.h:70

[cmsis\_rtos\_semaphore\_cb::name](structcmsis__rtos__semaphore__cb.md#a0fcd03ebf15c9bccb348180c601daa6a)

char name[16]

**Definition** cmsis\_types.h:73

[cmsis\_rtos\_semaphore\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__semaphore__cb.md#a375bd0bcaa18d236449a3ceb2e21eeb2)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:72

[cmsis\_rtos\_thread\_cb](structcmsis__rtos__thread__cb.md)

Control block for a CMSIS-RTOSv2 thread.

**Definition** cmsis\_types.h:23

[cmsis\_rtos\_thread\_cb::poll\_signal](structcmsis__rtos__thread__cb.md#a1141cf4f98f7942e4b303673ef0c2bb0)

struct k\_poll\_signal poll\_signal

**Definition** cmsis\_types.h:26

[cmsis\_rtos\_thread\_cb::has\_joined](structcmsis__rtos__thread__cb.md#a39207f4007b39e9295507e63b1194c04)

char has\_joined

**Definition** cmsis\_types.h:32

[cmsis\_rtos\_thread\_cb::node](structcmsis__rtos__thread__cb.md#a4105af0bf74ca757ded20f1cf8d8a32b)

sys\_dnode\_t node

**Definition** cmsis\_types.h:24

[cmsis\_rtos\_thread\_cb::poll\_event](structcmsis__rtos__thread__cb.md#a536f754d15b6bc836de9d469ab5cb23a)

struct k\_poll\_event poll\_event

**Definition** cmsis\_types.h:27

[cmsis\_rtos\_thread\_cb::attr\_bits](structcmsis__rtos__thread__cb.md#aa1aabdd8a7d59b0939e9c3822af26700)

uint32\_t attr\_bits

**Definition** cmsis\_types.h:30

[cmsis\_rtos\_thread\_cb::join\_guard](structcmsis__rtos__thread__cb.md#ac07201f80219ef4e8d6bb4244de7d82f)

struct k\_sem join\_guard

**Definition** cmsis\_types.h:31

[cmsis\_rtos\_thread\_cb::name](structcmsis__rtos__thread__cb.md#ac97e3f4f2aa71804a578392f154fc942)

char name[16]

**Definition** cmsis\_types.h:29

[cmsis\_rtos\_thread\_cb::signal\_results](structcmsis__rtos__thread__cb.md#af3061152f322434776156246c08651dc)

uint32\_t signal\_results

**Definition** cmsis\_types.h:28

[cmsis\_rtos\_timer\_cb](structcmsis__rtos__timer__cb.md)

Control block for a CMSIS-RTOSv2 timer.

**Definition** cmsis\_types.h:41

[cmsis\_rtos\_timer\_cb::status](structcmsis__rtos__timer__cb.md#a16a1cf8a0bc2eba418b64e1a35782526)

uint32\_t status

**Definition** cmsis\_types.h:44

[cmsis\_rtos\_timer\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__timer__cb.md#a2148d26c2386672ea72391839826e502)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:45

[cmsis\_rtos\_timer\_cb::arg](structcmsis__rtos__timer__cb.md#a854205b98234c4aeee8056d6bb64c4a3)

void \* arg

**Definition** cmsis\_types.h:48

[cmsis\_rtos\_timer\_cb::callback\_function](structcmsis__rtos__timer__cb.md#a8819befff072e0a3cda4bf855e24dbf1)

void(\* callback\_function)(void \*argument)

**Definition** cmsis\_types.h:47

[cmsis\_rtos\_timer\_cb::type](structcmsis__rtos__timer__cb.md#a9054df0b4e92854d20c0d202eaeea66c)

osTimerType\_t type

**Definition** cmsis\_types.h:43

[cmsis\_rtos\_timer\_cb::name](structcmsis__rtos__timer__cb.md#aeea9a9cb04879526375d5eb51733dfe5)

char name[16]

**Definition** cmsis\_types.h:46

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4552

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_poll\_event](structk__poll__event.md)

Poll Event.

**Definition** kernel.h:5988

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5964

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [portability](dir_01227ef4652825ef85eafb29606f54aa.md)
- [cmsis\_types.h](cmsis__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
