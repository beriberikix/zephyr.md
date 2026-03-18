---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smf_8h_source.html
original_path: doxygen/html/smf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smf.h

[Go to the documentation of this file.](smf_8h.md)

1/\*

2 \* Copyright 2021 The Chromium OS Authors

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\* State Machine Framework \*/

8

9#ifndef ZEPHYR\_INCLUDE\_SMF\_H\_

10#define ZEPHYR\_INCLUDE\_SMF\_H\_

11

12#ifdef CONFIG\_SMF\_ANCESTOR\_SUPPORT

21#define SMF\_CREATE\_STATE(\_entry, \_run, \_exit, \_parent) \

22{ \

23 .entry = \_entry, \

24 .run = \_run, \

25 .exit = \_exit, \

26 .parent = \_parent \

27}

28

29#else

30

[ 38](smf_8h.md#a7bcef10d761c099633867066ecef49f6)#define SMF\_CREATE\_STATE(\_entry, \_run, \_exit) \

39{ \

40 .entry = \_entry, \

41 .run = \_run, \

42 .exit = \_exit \

43}

44

45#endif /\* CONFIG\_SMF\_ANCESTOR\_SUPPORT \*/

46

[ 53](smf_8h.md#a0bccd3bf96e0887e8a610c1b06e22237)#define SMF\_CTX(o) ((struct smf\_ctx \*)o)

54

55#ifdef \_\_cplusplus

56extern "C" {

57#endif

58

59#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

60

[ 66](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6)typedef void (\*[state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6))(void \*obj);

67

[ 69](structsmf__state.md)struct [smf\_state](structsmf__state.md) {

[ 71](structsmf__state.md#a63ea395c90fa8118cf355e55e60cee26) const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) [entry](structsmf__state.md#a63ea395c90fa8118cf355e55e60cee26);

[ 76](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911) const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) [run](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911);

[ 78](structsmf__state.md#a2df810ca49fbb9438ee78317feaaf09b) const [state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6) [exit](structsmf__state.md#a2df810ca49fbb9438ee78317feaaf09b);

[ 89](structsmf__state.md#ac4267b2d8279d9c2d4897d97357b8e25) const struct [smf\_state](structsmf__state.md) \*[parent](structsmf__state.md#ac4267b2d8279d9c2d4897d97357b8e25);

90};

91

[ 93](structsmf__ctx.md)struct [smf\_ctx](structsmf__ctx.md) {

[ 95](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a) const struct [smf\_state](structsmf__state.md) \*[current](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a);

[ 97](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418) const struct [smf\_state](structsmf__state.md) \*[previous](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418);

[ 104](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [terminate\_val](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd);

[ 109](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [internal](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8);

110};

111

[ 118](smf_8h.md#a4389086c6aa3167e8c49226323ae208d)void [smf\_set\_initial](smf_8h.md#a4389086c6aa3167e8c49226323ae208d)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*init\_state);

119

[ 128](smf_8h.md#a3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)void [smf\_set\_state](smf_8h.md#a3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, const struct [smf\_state](structsmf__state.md) \*new\_state);

129

[ 137](smf_8h.md#aae28c66f0652c99ba8e843eeaf02aaf7)void [smf\_set\_terminate](smf_8h.md#aae28c66f0652c99ba8e843eeaf02aaf7)(struct [smf\_ctx](structsmf__ctx.md) \*ctx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val);

138

[ 148](smf_8h.md#a8399cfa9e793a7f188b4ed4fec9f4f90)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [smf\_run\_state](smf_8h.md#a8399cfa9e793a7f188b4ed4fec9f4f90)(struct [smf\_ctx](structsmf__ctx.md) \*ctx);

149

150#ifdef \_\_cplusplus

151}

152#endif

153

154#endif /\* ZEPHYR\_INCLUDE\_SMF\_H\_ \*/

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[smf\_set\_state](smf_8h.md#a3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)

void smf\_set\_state(struct smf\_ctx \*ctx, const struct smf\_state \*new\_state)

Changes a state machines state.

[smf\_set\_initial](smf_8h.md#a4389086c6aa3167e8c49226323ae208d)

void smf\_set\_initial(struct smf\_ctx \*ctx, const struct smf\_state \*init\_state)

Initializes the state machine and sets its initial state.

[smf\_run\_state](smf_8h.md#a8399cfa9e793a7f188b4ed4fec9f4f90)

int32\_t smf\_run\_state(struct smf\_ctx \*ctx)

Runs one iteration of a state machine (including any parent states).

[smf\_set\_terminate](smf_8h.md#aae28c66f0652c99ba8e843eeaf02aaf7)

void smf\_set\_terminate(struct smf\_ctx \*ctx, int32\_t val)

Terminate a state machine.

[state\_execution](smf_8h.md#aff08e9a57d55107fd8d13ffe86295ca6)

void(\* state\_execution)(void \*obj)

Function pointer that implements a portion of a state.

**Definition** smf.h:66

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[smf\_ctx](structsmf__ctx.md)

Defines the current context of the state machine.

**Definition** smf.h:93

[smf\_ctx::terminate\_val](structsmf__ctx.md#a1018c3dc6d7cc94ac2b64f95e5c053cd)

int32\_t terminate\_val

This value is set by the set\_terminate function and should terminate the state machine when its set t...

**Definition** smf.h:104

[smf\_ctx::previous](structsmf__ctx.md#a2cebcd02bfc6b36278c20fe8e0f95418)

const struct smf\_state \* previous

Previous state the state machine executed.

**Definition** smf.h:97

[smf\_ctx::current](structsmf__ctx.md#a48736dbfad38f0b25e4ab2a36d2f482a)

const struct smf\_state \* current

Current state the state machine is executing.

**Definition** smf.h:95

[smf\_ctx::internal](structsmf__ctx.md#afb094c0e87d42ec7ca780a2859be7bf8)

uint32\_t internal

The state machine casts this to a "struct internal\_ctx" and it's used to track state machine context.

**Definition** smf.h:109

[smf\_state](structsmf__state.md)

General state that can be used in multiple state machines.

**Definition** smf.h:69

[smf\_state::exit](structsmf__state.md#a2df810ca49fbb9438ee78317feaaf09b)

const state\_execution exit

Optional method that will be run when this state exists.

**Definition** smf.h:78

[smf\_state::entry](structsmf__state.md#a63ea395c90fa8118cf355e55e60cee26)

const state\_execution entry

Optional method that will be run when this state is entered.

**Definition** smf.h:71

[smf\_state::run](structsmf__state.md#a94adbcd4e1a8bce8f3b30082874f1911)

const state\_execution run

Optional method that will be run repeatedly during state machine loop.

**Definition** smf.h:76

[smf\_state::parent](structsmf__state.md#ac4267b2d8279d9c2d4897d97357b8e25)

const struct smf\_state \* parent

Optional parent state that contains common entry/run/exit implementation among various child states.

**Definition** smf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [smf.h](smf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
