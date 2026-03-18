---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ipm__console_8h_source.html
original_path: doxygen/html/ipm__console_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm\_console.h

[Go to the documentation of this file.](ipm__console_8h.md)

1/\* ipm\_console.c - Console messages to/from another processor \*/

2

3/\*

4 \* Copyright (c) 2015 Intel Corporation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_IPM\_CONSOLE\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_IPM\_CONSOLE\_H\_

11

12#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

13#include <[zephyr/device.h](device_8h.md)>

14#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 20](ipm__console_8h.md#accdeb68d3bf39e9fe88ddc13defe8807)#define IPM\_CONSOLE\_STDOUT (BIT(0))

[ 21](ipm__console_8h.md#ac0d474a4aa232f26194bd897a4611ed7)#define IPM\_CONSOLE\_PRINTK (BIT(1))

22

23/\*

24 \* Good way to determine these numbers other than trial-and-error?

25 \* using printf() in the thread seems to require a lot more stack space

26 \*/

[ 27](ipm__console_8h.md#a4280a85493aa4df9b591cc3d98c1d4af)#define IPM\_CONSOLE\_STACK\_SIZE CONFIG\_IPM\_CONSOLE\_STACK\_SIZE

[ 28](ipm__console_8h.md#a4d4cc0be8ad727fc09a5d9c694f06a71)#define IPM\_CONSOLE\_PRI 2

29

[ 30](structipm__console__receiver__config__info.md)struct [ipm\_console\_receiver\_config\_info](structipm__console__receiver__config__info.md) {

[ 32](structipm__console__receiver__config__info.md#ac57741917d3d869680bb4b78446ed269) char \*[bind\_to](structipm__console__receiver__config__info.md#ac57741917d3d869680bb4b78446ed269);

33

[ 38](structipm__console__receiver__config__info.md#a924802d5b239f37b25f519c4c9e0be5f) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[thread\_stack](structipm__console__receiver__config__info.md#a924802d5b239f37b25f519c4c9e0be5f);

39

[ 44](structipm__console__receiver__config__info.md#aab7bf2a943d620d3fe4a85a08423335b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[ring\_buf\_data](structipm__console__receiver__config__info.md#aab7bf2a943d620d3fe4a85a08423335b);

45

[ 47](structipm__console__receiver__config__info.md#a2ba6b50f7f949b21eb25031ad74699e6) unsigned int [rb\_size32](structipm__console__receiver__config__info.md#a2ba6b50f7f949b21eb25031ad74699e6);

48

[ 54](structipm__console__receiver__config__info.md#a340991c90102acee70fc7ca3fdcf932f) char \*[line\_buf](structipm__console__receiver__config__info.md#a340991c90102acee70fc7ca3fdcf932f);

55

[ 57](structipm__console__receiver__config__info.md#ac7456fac5c924586f2a7f9ffa55f7d82) unsigned int [lb\_size](structipm__console__receiver__config__info.md#ac7456fac5c924586f2a7f9ffa55f7d82);

58

[ 63](structipm__console__receiver__config__info.md#ab41bc0fddbb023f7269be72864084e61) unsigned int [flags](structipm__console__receiver__config__info.md#ab41bc0fddbb023f7269be72864084e61);

64};

65

[ 66](structipm__console__receiver__runtime__data.md)struct [ipm\_console\_receiver\_runtime\_data](structipm__console__receiver__runtime__data.md) {

[ 68](structipm__console__receiver__runtime__data.md#ae80a0417e9367be13b1882700da1787e) struct [ring\_buf](structring__buf.md) [rb](structipm__console__receiver__runtime__data.md#ae80a0417e9367be13b1882700da1787e);

69

[ 71](structipm__console__receiver__runtime__data.md#a533b6ede3eb1d26ee435b3d8c060ef5a) struct k\_sem [sem](structipm__console__receiver__runtime__data.md#a533b6ede3eb1d26ee435b3d8c060ef5a);

72

[ 74](structipm__console__receiver__runtime__data.md#a18851d2abe3e8fc6b0baf65ad95785c8) const struct [device](structdevice.md) \*[ipm\_device](structipm__console__receiver__runtime__data.md#a18851d2abe3e8fc6b0baf65ad95785c8);

75

[ 79](structipm__console__receiver__runtime__data.md#a52e52921cb31c30ef78e27c7359855e9) int [channel\_disabled](structipm__console__receiver__runtime__data.md#a52e52921cb31c30ef78e27c7359855e9);

80

[ 82](structipm__console__receiver__runtime__data.md#a614fc792b330f4145bd149f2a968681d) struct [k\_thread](structk__thread.md) [rx\_thread](structipm__console__receiver__runtime__data.md#a614fc792b330f4145bd149f2a968681d);

83};

84

[ 85](structipm__console__sender__config__info.md)struct [ipm\_console\_sender\_config\_info](structipm__console__sender__config__info.md) {

[ 87](structipm__console__sender__config__info.md#aed3d8f396e858ddd9c4ea55e647feb34) char \*[bind\_to](structipm__console__sender__config__info.md#aed3d8f396e858ddd9c4ea55e647feb34);

88

[ 93](structipm__console__sender__config__info.md#a95e4bf553f053ff389ae9e85f3d86ef3) int [flags](structipm__console__sender__config__info.md#a95e4bf553f053ff389ae9e85f3d86ef3);

94};

95

96#if CONFIG\_IPM\_CONSOLE\_RECEIVER

97int ipm\_console\_receiver\_init(const struct [device](structdevice.md) \*[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417));

98#endif

99

100#if CONFIG\_IPM\_CONSOLE\_SENDER

101int ipm\_console\_sender\_init(const struct [device](structdevice.md) \*[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417));

102#endif

103

104#ifdef \_\_cplusplus

105}

106#endif

107

108#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_IPM\_CONSOLE\_H\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:45

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[device.h](device_8h.md)

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[ring\_buffer.h](ring__buffer_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[ipm\_console\_receiver\_config\_info](structipm__console__receiver__config__info.md)

**Definition** ipm\_console.h:30

[ipm\_console\_receiver\_config\_info::rb\_size32](structipm__console__receiver__config__info.md#a2ba6b50f7f949b21eb25031ad74699e6)

unsigned int rb\_size32

Size of ring\_buf\_data in 32-bit chunks.

**Definition** ipm\_console.h:47

[ipm\_console\_receiver\_config\_info::line\_buf](structipm__console__receiver__config__info.md#a340991c90102acee70fc7ca3fdcf932f)

char \* line\_buf

Line buffer for incoming messages, characters accumulate here and then are sent to printk() once full...

**Definition** ipm\_console.h:54

[ipm\_console\_receiver\_config\_info::thread\_stack](structipm__console__receiver__config__info.md#a924802d5b239f37b25f519c4c9e0be5f)

k\_thread\_stack\_t \* thread\_stack

Stack for the receiver's thread, which prints out messages as they come in.

**Definition** ipm\_console.h:38

[ipm\_console\_receiver\_config\_info::ring\_buf\_data](structipm__console__receiver__config__info.md#aab7bf2a943d620d3fe4a85a08423335b)

uint32\_t \* ring\_buf\_data

Ring buffer data area for stashing characters from the interrupt callback.

**Definition** ipm\_console.h:44

[ipm\_console\_receiver\_config\_info::flags](structipm__console__receiver__config__info.md#ab41bc0fddbb023f7269be72864084e61)

unsigned int flags

Destination for received console messages, one of IPM\_CONSOLE\_STDOUT or IPM\_CONSOLE\_PRINTK.

**Definition** ipm\_console.h:63

[ipm\_console\_receiver\_config\_info::bind\_to](structipm__console__receiver__config__info.md#ac57741917d3d869680bb4b78446ed269)

char \* bind\_to

Name of the low-level IPM driver to bind to.

**Definition** ipm\_console.h:32

[ipm\_console\_receiver\_config\_info::lb\_size](structipm__console__receiver__config__info.md#ac7456fac5c924586f2a7f9ffa55f7d82)

unsigned int lb\_size

Size in bytes of the line buffer.

**Definition** ipm\_console.h:57

[ipm\_console\_receiver\_runtime\_data](structipm__console__receiver__runtime__data.md)

**Definition** ipm\_console.h:66

[ipm\_console\_receiver\_runtime\_data::ipm\_device](structipm__console__receiver__runtime__data.md#a18851d2abe3e8fc6b0baf65ad95785c8)

const struct device \* ipm\_device

pointer to the bound low-level IPM device

**Definition** ipm\_console.h:74

[ipm\_console\_receiver\_runtime\_data::channel\_disabled](structipm__console__receiver__runtime__data.md#a52e52921cb31c30ef78e27c7359855e9)

int channel\_disabled

Indicator that the channel is temporarily disabled due to full buffer.

**Definition** ipm\_console.h:79

[ipm\_console\_receiver\_runtime\_data::sem](structipm__console__receiver__runtime__data.md#a533b6ede3eb1d26ee435b3d8c060ef5a)

struct k\_sem sem

Semaphore to wake up the thread to print out messages.

**Definition** ipm\_console.h:71

[ipm\_console\_receiver\_runtime\_data::rx\_thread](structipm__console__receiver__runtime__data.md#a614fc792b330f4145bd149f2a968681d)

struct k\_thread rx\_thread

Receiver worker thread.

**Definition** ipm\_console.h:82

[ipm\_console\_receiver\_runtime\_data::rb](structipm__console__receiver__runtime__data.md#ae80a0417e9367be13b1882700da1787e)

struct ring\_buf rb

Buffer for received bytes from the low-level IPM device.

**Definition** ipm\_console.h:68

[ipm\_console\_sender\_config\_info](structipm__console__sender__config__info.md)

**Definition** ipm\_console.h:85

[ipm\_console\_sender\_config\_info::flags](structipm__console__sender__config__info.md#a95e4bf553f053ff389ae9e85f3d86ef3)

int flags

Source of messages to forward, hooks will be installed.

**Definition** ipm\_console.h:93

[ipm\_console\_sender\_config\_info::bind\_to](structipm__console__sender__config__info.md#aed3d8f396e858ddd9c4ea55e647feb34)

char \* bind\_to

Name of the low-level driver to bind to.

**Definition** ipm\_console.h:87

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:41

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [ipm\_console.h](ipm__console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
