---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cmsis__types_8h_source.html
original_path: doxygen/html/cmsis__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 20](structcmsis__rtos__thread__cb.md)struct [cmsis\_rtos\_thread\_cb](structcmsis__rtos__thread__cb.md) {

[ 21](structcmsis__rtos__thread__cb.md#a4105af0bf74ca757ded20f1cf8d8a32b) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structcmsis__rtos__thread__cb.md#a4105af0bf74ca757ded20f1cf8d8a32b);

22 struct [k\_thread](structk__thread.md) z\_thread;

[ 23](structcmsis__rtos__thread__cb.md#a1141cf4f98f7942e4b303673ef0c2bb0) struct [k\_poll\_signal](structk__poll__signal.md) [poll\_signal](structcmsis__rtos__thread__cb.md#a1141cf4f98f7942e4b303673ef0c2bb0);

[ 24](structcmsis__rtos__thread__cb.md#a536f754d15b6bc836de9d469ab5cb23a) struct [k\_poll\_event](structk__poll__event.md) [poll\_event](structcmsis__rtos__thread__cb.md#a536f754d15b6bc836de9d469ab5cb23a);

[ 25](structcmsis__rtos__thread__cb.md#af3061152f322434776156246c08651dc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [signal\_results](structcmsis__rtos__thread__cb.md#af3061152f322434776156246c08651dc);

[ 26](structcmsis__rtos__thread__cb.md#aa1aabdd8a7d59b0939e9c3822af26700) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attr\_bits](structcmsis__rtos__thread__cb.md#aa1aabdd8a7d59b0939e9c3822af26700);

27};

28

[ 35](structcmsis__rtos__timer__cb.md)struct [cmsis\_rtos\_timer\_cb](structcmsis__rtos__timer__cb.md) {

36 struct k\_timer z\_timer;

[ 37](structcmsis__rtos__timer__cb.md#a9054df0b4e92854d20c0d202eaeea66c) osTimerType\_t [type](structcmsis__rtos__timer__cb.md#a9054df0b4e92854d20c0d202eaeea66c);

[ 38](structcmsis__rtos__timer__cb.md#a16a1cf8a0bc2eba418b64e1a35782526) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [status](structcmsis__rtos__timer__cb.md#a16a1cf8a0bc2eba418b64e1a35782526);

[ 39](structcmsis__rtos__timer__cb.md#a2148d26c2386672ea72391839826e502) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__timer__cb.md#a2148d26c2386672ea72391839826e502);

[ 40](structcmsis__rtos__timer__cb.md#a3352e817ce98f2f8051b2de81c3a9bb5) const char \*[name](structcmsis__rtos__timer__cb.md#a3352e817ce98f2f8051b2de81c3a9bb5);

[ 41](structcmsis__rtos__timer__cb.md#a8819befff072e0a3cda4bf855e24dbf1) void (\*[callback\_function](structcmsis__rtos__timer__cb.md#a8819befff072e0a3cda4bf855e24dbf1))(void \*argument);

[ 42](structcmsis__rtos__timer__cb.md#a854205b98234c4aeee8056d6bb64c4a3) void \*[arg](structcmsis__rtos__timer__cb.md#a854205b98234c4aeee8056d6bb64c4a3);

43};

44

[ 51](structcmsis__rtos__mutex__cb.md)struct [cmsis\_rtos\_mutex\_cb](structcmsis__rtos__mutex__cb.md) {

52 struct [k\_mutex](structk__mutex.md) z\_mutex;

[ 53](structcmsis__rtos__mutex__cb.md#aa7df7554bcdeb9e14ce38771392482dc) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__mutex__cb.md#aa7df7554bcdeb9e14ce38771392482dc);

[ 54](structcmsis__rtos__mutex__cb.md#a8851d4a4d62db875c9f8c87e8d2a864b) const char \*[name](structcmsis__rtos__mutex__cb.md#a8851d4a4d62db875c9f8c87e8d2a864b);

[ 55](structcmsis__rtos__mutex__cb.md#a43e50207a92b6f5c1f4add8a537352e5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](structcmsis__rtos__mutex__cb.md#a43e50207a92b6f5c1f4add8a537352e5);

56};

57

[ 64](structcmsis__rtos__semaphore__cb.md)struct [cmsis\_rtos\_semaphore\_cb](structcmsis__rtos__semaphore__cb.md) {

65 struct [k\_sem](structk__sem.md) z\_semaphore;

[ 66](structcmsis__rtos__semaphore__cb.md#a375bd0bcaa18d236449a3ceb2e21eeb2) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__semaphore__cb.md#a375bd0bcaa18d236449a3ceb2e21eeb2);

[ 67](structcmsis__rtos__semaphore__cb.md#a4f75190c47aa6cc6a460ffbf7c744e9d) const char \*[name](structcmsis__rtos__semaphore__cb.md#a4f75190c47aa6cc6a460ffbf7c744e9d);

68};

69

[ 76](structcmsis__rtos__mempool__cb.md)struct [cmsis\_rtos\_mempool\_cb](structcmsis__rtos__mempool__cb.md) {

77 struct k\_mem\_slab z\_mslab;

[ 78](structcmsis__rtos__mempool__cb.md#a1a05ccc77a02197729db3e80f235e833) void \*[pool](structcmsis__rtos__mempool__cb.md#a1a05ccc77a02197729db3e80f235e833);

[ 79](structcmsis__rtos__mempool__cb.md#ad8d9c65555e6cba4d3d016ef0decf99f) char [is\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#ad8d9c65555e6cba4d3d016ef0decf99f);

[ 80](structcmsis__rtos__mempool__cb.md#aad9668c546fcbbb232faf0790554cc60) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#aad9668c546fcbbb232faf0790554cc60);

[ 81](structcmsis__rtos__mempool__cb.md#a18f53f02171e508d5b9ecaa73d0fa8ef) const char \*[name](structcmsis__rtos__mempool__cb.md#a18f53f02171e508d5b9ecaa73d0fa8ef);

82};

83

[ 90](structcmsis__rtos__msgq__cb.md)struct [cmsis\_rtos\_msgq\_cb](structcmsis__rtos__msgq__cb.md) {

91 struct [k\_msgq](structk__msgq.md) z\_msgq;

[ 92](structcmsis__rtos__msgq__cb.md#a1909f69f4b0f89a3aad0eec03fce9f7a) void \*[pool](structcmsis__rtos__msgq__cb.md#a1909f69f4b0f89a3aad0eec03fce9f7a);

[ 93](structcmsis__rtos__msgq__cb.md#ab867f14725ef4c114b16d9ff4362b085) char [is\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#ab867f14725ef4c114b16d9ff4362b085);

[ 94](structcmsis__rtos__msgq__cb.md#aba512f3212825e79a291690e7577506e) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#aba512f3212825e79a291690e7577506e);

[ 95](structcmsis__rtos__msgq__cb.md#a948d5494513529f47d44f35b12c503ad) const char \*[name](structcmsis__rtos__msgq__cb.md#a948d5494513529f47d44f35b12c503ad);

96};

97

[ 104](structcmsis__rtos__event__cb.md)struct [cmsis\_rtos\_event\_cb](structcmsis__rtos__event__cb.md) {

[ 105](structcmsis__rtos__event__cb.md#ae9750a0ffc6a3f83916760d67a4edb63) struct [k\_poll\_signal](structk__poll__signal.md) [poll\_signal](structcmsis__rtos__event__cb.md#ae9750a0ffc6a3f83916760d67a4edb63);

[ 106](structcmsis__rtos__event__cb.md#a3b96b29e2866966d1ddd0ff71a1bbfac) struct [k\_poll\_event](structk__poll__event.md) [poll\_event](structcmsis__rtos__event__cb.md#a3b96b29e2866966d1ddd0ff71a1bbfac);

[ 107](structcmsis__rtos__event__cb.md#ab9218a355d3b3a943a1a9eea4656160a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [signal\_results](structcmsis__rtos__event__cb.md#ab9218a355d3b3a943a1a9eea4656160a);

[ 108](structcmsis__rtos__event__cb.md#af1898a60748c3a1f3c2d2839eecaff64) bool [is\_cb\_dynamic\_allocation](structcmsis__rtos__event__cb.md#af1898a60748c3a1f3c2d2839eecaff64);

[ 109](structcmsis__rtos__event__cb.md#adaa7a7ce302215e694c4866f5fbcd991) const char \*[name](structcmsis__rtos__event__cb.md#adaa7a7ce302215e694c4866f5fbcd991);

110};

111

112#endif

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

**Definition** cmsis\_types.h:104

[cmsis\_rtos\_event\_cb::poll\_event](structcmsis__rtos__event__cb.md#a3b96b29e2866966d1ddd0ff71a1bbfac)

struct k\_poll\_event poll\_event

**Definition** cmsis\_types.h:106

[cmsis\_rtos\_event\_cb::signal\_results](structcmsis__rtos__event__cb.md#ab9218a355d3b3a943a1a9eea4656160a)

uint32\_t signal\_results

**Definition** cmsis\_types.h:107

[cmsis\_rtos\_event\_cb::name](structcmsis__rtos__event__cb.md#adaa7a7ce302215e694c4866f5fbcd991)

const char \* name

**Definition** cmsis\_types.h:109

[cmsis\_rtos\_event\_cb::poll\_signal](structcmsis__rtos__event__cb.md#ae9750a0ffc6a3f83916760d67a4edb63)

struct k\_poll\_signal poll\_signal

**Definition** cmsis\_types.h:105

[cmsis\_rtos\_event\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__event__cb.md#af1898a60748c3a1f3c2d2839eecaff64)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:108

[cmsis\_rtos\_mempool\_cb](structcmsis__rtos__mempool__cb.md)

Control block for a CMSIS-RTOSv2 memory pool.

**Definition** cmsis\_types.h:76

[cmsis\_rtos\_mempool\_cb::name](structcmsis__rtos__mempool__cb.md#a18f53f02171e508d5b9ecaa73d0fa8ef)

const char \* name

**Definition** cmsis\_types.h:81

[cmsis\_rtos\_mempool\_cb::pool](structcmsis__rtos__mempool__cb.md#a1a05ccc77a02197729db3e80f235e833)

void \* pool

**Definition** cmsis\_types.h:78

[cmsis\_rtos\_mempool\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#aad9668c546fcbbb232faf0790554cc60)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:80

[cmsis\_rtos\_mempool\_cb::is\_dynamic\_allocation](structcmsis__rtos__mempool__cb.md#ad8d9c65555e6cba4d3d016ef0decf99f)

char is\_dynamic\_allocation

**Definition** cmsis\_types.h:79

[cmsis\_rtos\_msgq\_cb](structcmsis__rtos__msgq__cb.md)

Control block for a CMSIS-RTOSv2 message queue.

**Definition** cmsis\_types.h:90

[cmsis\_rtos\_msgq\_cb::pool](structcmsis__rtos__msgq__cb.md#a1909f69f4b0f89a3aad0eec03fce9f7a)

void \* pool

**Definition** cmsis\_types.h:92

[cmsis\_rtos\_msgq\_cb::name](structcmsis__rtos__msgq__cb.md#a948d5494513529f47d44f35b12c503ad)

const char \* name

**Definition** cmsis\_types.h:95

[cmsis\_rtos\_msgq\_cb::is\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#ab867f14725ef4c114b16d9ff4362b085)

char is\_dynamic\_allocation

**Definition** cmsis\_types.h:93

[cmsis\_rtos\_msgq\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__msgq__cb.md#aba512f3212825e79a291690e7577506e)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:94

[cmsis\_rtos\_mutex\_cb](structcmsis__rtos__mutex__cb.md)

Control block for a CMSIS-RTOSv2 mutex.

**Definition** cmsis\_types.h:51

[cmsis\_rtos\_mutex\_cb::state](structcmsis__rtos__mutex__cb.md#a43e50207a92b6f5c1f4add8a537352e5)

uint32\_t state

**Definition** cmsis\_types.h:55

[cmsis\_rtos\_mutex\_cb::name](structcmsis__rtos__mutex__cb.md#a8851d4a4d62db875c9f8c87e8d2a864b)

const char \* name

**Definition** cmsis\_types.h:54

[cmsis\_rtos\_mutex\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__mutex__cb.md#aa7df7554bcdeb9e14ce38771392482dc)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:53

[cmsis\_rtos\_semaphore\_cb](structcmsis__rtos__semaphore__cb.md)

Control block for a CMSIS-RTOSv2 semaphore.

**Definition** cmsis\_types.h:64

[cmsis\_rtos\_semaphore\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__semaphore__cb.md#a375bd0bcaa18d236449a3ceb2e21eeb2)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:66

[cmsis\_rtos\_semaphore\_cb::name](structcmsis__rtos__semaphore__cb.md#a4f75190c47aa6cc6a460ffbf7c744e9d)

const char \* name

**Definition** cmsis\_types.h:67

[cmsis\_rtos\_thread\_cb](structcmsis__rtos__thread__cb.md)

Control block for a CMSIS-RTOSv2 thread.

**Definition** cmsis\_types.h:20

[cmsis\_rtos\_thread\_cb::poll\_signal](structcmsis__rtos__thread__cb.md#a1141cf4f98f7942e4b303673ef0c2bb0)

struct k\_poll\_signal poll\_signal

**Definition** cmsis\_types.h:23

[cmsis\_rtos\_thread\_cb::node](structcmsis__rtos__thread__cb.md#a4105af0bf74ca757ded20f1cf8d8a32b)

sys\_dnode\_t node

**Definition** cmsis\_types.h:21

[cmsis\_rtos\_thread\_cb::poll\_event](structcmsis__rtos__thread__cb.md#a536f754d15b6bc836de9d469ab5cb23a)

struct k\_poll\_event poll\_event

**Definition** cmsis\_types.h:24

[cmsis\_rtos\_thread\_cb::attr\_bits](structcmsis__rtos__thread__cb.md#aa1aabdd8a7d59b0939e9c3822af26700)

uint32\_t attr\_bits

**Definition** cmsis\_types.h:26

[cmsis\_rtos\_thread\_cb::signal\_results](structcmsis__rtos__thread__cb.md#af3061152f322434776156246c08651dc)

uint32\_t signal\_results

**Definition** cmsis\_types.h:25

[cmsis\_rtos\_timer\_cb](structcmsis__rtos__timer__cb.md)

Control block for a CMSIS-RTOSv2 timer.

**Definition** cmsis\_types.h:35

[cmsis\_rtos\_timer\_cb::status](structcmsis__rtos__timer__cb.md#a16a1cf8a0bc2eba418b64e1a35782526)

uint32\_t status

**Definition** cmsis\_types.h:38

[cmsis\_rtos\_timer\_cb::is\_cb\_dynamic\_allocation](structcmsis__rtos__timer__cb.md#a2148d26c2386672ea72391839826e502)

bool is\_cb\_dynamic\_allocation

**Definition** cmsis\_types.h:39

[cmsis\_rtos\_timer\_cb::name](structcmsis__rtos__timer__cb.md#a3352e817ce98f2f8051b2de81c3a9bb5)

const char \* name

**Definition** cmsis\_types.h:40

[cmsis\_rtos\_timer\_cb::arg](structcmsis__rtos__timer__cb.md#a854205b98234c4aeee8056d6bb64c4a3)

void \* arg

**Definition** cmsis\_types.h:42

[cmsis\_rtos\_timer\_cb::callback\_function](structcmsis__rtos__timer__cb.md#a8819befff072e0a3cda4bf855e24dbf1)

void(\* callback\_function)(void \*argument)

**Definition** cmsis\_types.h:41

[cmsis\_rtos\_timer\_cb::type](structcmsis__rtos__timer__cb.md#a9054df0b4e92854d20c0d202eaeea66c)

osTimerType\_t type

**Definition** cmsis\_types.h:37

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4640

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3070

[k\_poll\_event](structk__poll__event.md)

Poll Event.

**Definition** kernel.h:6146

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:6122

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [portability](dir_01227ef4652825ef85eafb29606f54aa.md)
- [cmsis\_types.h](cmsis__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
