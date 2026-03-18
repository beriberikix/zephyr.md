---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/thread__analyzer_8h_source.html
original_path: doxygen/html/thread__analyzer_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_analyzer.h

[Go to the documentation of this file.](thread__analyzer_8h.md)

1/\*

2 \* Copyright (c) 2019 - 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_STACK\_SIZE\_ANALYZER\_H

8#define \_\_STACK\_SIZE\_ANALYZER\_H

9

10#include <stddef.h>

11#include <[zephyr/kernel/thread.h](kernel_2thread_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

25

[ 26](structthread__analyzer__info.md)struct [thread\_analyzer\_info](structthread__analyzer__info.md) {

[ 30](structthread__analyzer__info.md#a972c2f720864788fa657be15c04c9424) const char \*[name](structthread__analyzer__info.md#a972c2f720864788fa657be15c04c9424);

[ 32](structthread__analyzer__info.md#ad4b6eb4a085f1c250314a452f4005e2e) size\_t [stack\_size](structthread__analyzer__info.md#ad4b6eb4a085f1c250314a452f4005e2e);

[ 34](structthread__analyzer__info.md#ac24b93b5fe53d0d1928eb904af6f2a36) size\_t [stack\_used](structthread__analyzer__info.md#ac24b93b5fe53d0d1928eb904af6f2a36);

35

36#ifdef CONFIG\_THREAD\_RUNTIME\_STATS

37 unsigned int utilization;

38#ifdef CONFIG\_SCHED\_THREAD\_USAGE

39 [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) usage;

40#endif

41#endif

42};

43

[ 50](group__thread__analyzer.md#ga7ac3e88ca6d905ba0efe4afe5822485c)typedef void (\*[thread\_analyzer\_cb](group__thread__analyzer.md#ga7ac3e88ca6d905ba0efe4afe5822485c))(struct [thread\_analyzer\_info](structthread__analyzer__info.md) \*info);

51

[ 59](group__thread__analyzer.md#ga21ae4723422fb96bf4f20ddb3cc1bb8d)void [thread\_analyzer\_run](group__thread__analyzer.md#ga21ae4723422fb96bf4f20ddb3cc1bb8d)([thread\_analyzer\_cb](group__thread__analyzer.md#ga7ac3e88ca6d905ba0efe4afe5822485c) cb);

60

[ 66](group__thread__analyzer.md#ga9ff07e2eff100f4b8c79440483c89836)void [thread\_analyzer\_print](group__thread__analyzer.md#ga9ff07e2eff100f4b8c79440483c89836)(void);

67

69

70#ifdef \_\_cplusplus

71}

72#endif

73

74#endif /\* \_\_STACK\_SIZE\_ANALYZER\_H \*/

[thread\_analyzer\_run](group__thread__analyzer.md#ga21ae4723422fb96bf4f20ddb3cc1bb8d)

void thread\_analyzer\_run(thread\_analyzer\_cb cb)

Run the thread analyzer and provide information to the callback.

[thread\_analyzer\_cb](group__thread__analyzer.md#ga7ac3e88ca6d905ba0efe4afe5822485c)

void(\* thread\_analyzer\_cb)(struct thread\_analyzer\_info \*info)

Thread analyzer stack size callback function.

**Definition** thread\_analyzer.h:50

[thread\_analyzer\_print](group__thread__analyzer.md#ga9ff07e2eff100f4b8c79440483c89836)

void thread\_analyzer\_print(void)

Run the thread analyzer and print stack size statistics.

[thread.h](kernel_2thread_8h.md)

[k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)

struct k\_thread\_runtime\_stats k\_thread\_runtime\_stats\_t

[thread\_analyzer\_info](structthread__analyzer__info.md)

**Definition** thread\_analyzer.h:26

[thread\_analyzer\_info::name](structthread__analyzer__info.md#a972c2f720864788fa657be15c04c9424)

const char \* name

The name of the thread or stringified address of the thread handle if name is not set.

**Definition** thread\_analyzer.h:30

[thread\_analyzer\_info::stack\_used](structthread__analyzer__info.md#ac24b93b5fe53d0d1928eb904af6f2a36)

size\_t stack\_used

Stack size in used.

**Definition** thread\_analyzer.h:34

[thread\_analyzer\_info::stack\_size](structthread__analyzer__info.md#ad4b6eb4a085f1c250314a452f4005e2e)

size\_t stack\_size

The total size of the stack.

**Definition** thread\_analyzer.h:32

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [thread\_analyzer.h](thread__analyzer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
