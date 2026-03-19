---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/modem_2backend_2tty_8h_source.html
original_path: doxygen/html/modem_2backend_2tty_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tty.h

[Go to the documentation of this file.](modem_2backend_2tty_8h.md)

1/\*

2 \* Copyright (c) 2022 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/kernel.h](kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/device.h](device_8h.md)>

10#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

11#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

12

13#include <[zephyr/modem/pipe.h](pipe_8h.md)>

14

15#ifndef ZEPHYR\_MODEM\_BACKEND\_TTY\_

[ 16](modem_2backend_2tty_8h.md#a69a30337ca00de462fc67e47401334f4)#define ZEPHYR\_MODEM\_BACKEND\_TTY\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 22](structmodem__backend__tty.md)struct [modem\_backend\_tty](structmodem__backend__tty.md) {

[ 23](structmodem__backend__tty.md#af6a76d369957f01f9d44c7f4bba67642) const char \*[tty\_path](structmodem__backend__tty.md#af6a76d369957f01f9d44c7f4bba67642);

[ 24](structmodem__backend__tty.md#abf93189b2640afa8bad440089bb1a863) int [tty\_fd](structmodem__backend__tty.md#abf93189b2640afa8bad440089bb1a863);

[ 25](structmodem__backend__tty.md#abe654bb7b24f23417e60bc8af7b73d36) struct modem\_pipe [pipe](structmodem__backend__tty.md#abe654bb7b24f23417e60bc8af7b73d36);

[ 26](structmodem__backend__tty.md#ad454321f08f334b028bb63cbb0d8e8f6) struct [k\_thread](structk__thread.md) [thread](structmodem__backend__tty.md#ad454321f08f334b028bb63cbb0d8e8f6);

[ 27](structmodem__backend__tty.md#a23afe812c5951bfa41251610056aa3aa) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structmodem__backend__tty.md#a23afe812c5951bfa41251610056aa3aa);

[ 28](structmodem__backend__tty.md#a2ea8d323973de8423f558a7a2e6b8984) size\_t [stack\_size](structmodem__backend__tty.md#a2ea8d323973de8423f558a7a2e6b8984);

[ 29](structmodem__backend__tty.md#a7f85f1f41fbcdf69ad1846a3af1b0b1e) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](structmodem__backend__tty.md#a7f85f1f41fbcdf69ad1846a3af1b0b1e);

30};

31

[ 32](structmodem__backend__tty__config.md)struct [modem\_backend\_tty\_config](structmodem__backend__tty__config.md) {

[ 33](structmodem__backend__tty__config.md#a139e7e96f3b021f560fa5ef8aa4d9e9f) const char \*[tty\_path](structmodem__backend__tty__config.md#a139e7e96f3b021f560fa5ef8aa4d9e9f);

[ 34](structmodem__backend__tty__config.md#ae8dd6da28163e6f97549e13e750d939d) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack](structmodem__backend__tty__config.md#ae8dd6da28163e6f97549e13e750d939d);

[ 35](structmodem__backend__tty__config.md#a74cb7ee08a116261b19d834000db5242) size\_t [stack\_size](structmodem__backend__tty__config.md#a74cb7ee08a116261b19d834000db5242);

36};

37

[ 38](modem_2backend_2tty_8h.md#a507f79d94144e3e4a75ec7fed1501f80)struct modem\_pipe \*[modem\_backend\_tty\_init](modem_2backend_2tty_8h.md#a507f79d94144e3e4a75ec7fed1501f80)(struct [modem\_backend\_tty](structmodem__backend__tty.md) \*backend,

39 const struct [modem\_backend\_tty\_config](structmodem__backend__tty__config.md) \*config);

40

41#ifdef \_\_cplusplus

42}

43#endif

44

45#endif /\* ZEPHYR\_MODEM\_BACKEND\_TTY\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[modem\_backend\_tty\_init](modem_2backend_2tty_8h.md#a507f79d94144e3e4a75ec7fed1501f80)

struct modem\_pipe \* modem\_backend\_tty\_init(struct modem\_backend\_tty \*backend, const struct modem\_backend\_tty\_config \*config)

[pipe.h](pipe_8h.md)

[ring\_buffer.h](ring__buffer_8h.md)

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[modem\_backend\_tty\_config](structmodem__backend__tty__config.md)

**Definition** tty.h:32

[modem\_backend\_tty\_config::tty\_path](structmodem__backend__tty__config.md#a139e7e96f3b021f560fa5ef8aa4d9e9f)

const char \* tty\_path

**Definition** tty.h:33

[modem\_backend\_tty\_config::stack\_size](structmodem__backend__tty__config.md#a74cb7ee08a116261b19d834000db5242)

size\_t stack\_size

**Definition** tty.h:35

[modem\_backend\_tty\_config::stack](structmodem__backend__tty__config.md#ae8dd6da28163e6f97549e13e750d939d)

k\_thread\_stack\_t \* stack

**Definition** tty.h:34

[modem\_backend\_tty](structmodem__backend__tty.md)

**Definition** tty.h:22

[modem\_backend\_tty::stack](structmodem__backend__tty.md#a23afe812c5951bfa41251610056aa3aa)

k\_thread\_stack\_t \* stack

**Definition** tty.h:27

[modem\_backend\_tty::stack\_size](structmodem__backend__tty.md#a2ea8d323973de8423f558a7a2e6b8984)

size\_t stack\_size

**Definition** tty.h:28

[modem\_backend\_tty::state](structmodem__backend__tty.md#a7f85f1f41fbcdf69ad1846a3af1b0b1e)

atomic\_t state

**Definition** tty.h:29

[modem\_backend\_tty::pipe](structmodem__backend__tty.md#abe654bb7b24f23417e60bc8af7b73d36)

struct modem\_pipe pipe

**Definition** tty.h:25

[modem\_backend\_tty::tty\_fd](structmodem__backend__tty.md#abf93189b2640afa8bad440089bb1a863)

int tty\_fd

**Definition** tty.h:24

[modem\_backend\_tty::thread](structmodem__backend__tty.md#ad454321f08f334b028bb63cbb0d8e8f6)

struct k\_thread thread

**Definition** tty.h:26

[modem\_backend\_tty::tty\_path](structmodem__backend__tty.md#af6a76d369957f01f9d44c7f4bba67642)

const char \* tty\_path

**Definition** tty.h:23

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [backend](dir_ff046e227e385bf86f987d0152997f69.md)
- [tty.h](modem_2backend_2tty_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
