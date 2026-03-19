---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__thread__analyzer.html
original_path: doxygen/html/group__thread__analyzer.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Thread analyzer

[Operating System Services](group__os__services.md)

Module for analyzing threads.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [thread\_analyzer\_info](structthread__analyzer__info.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [thread\_analyzer\_cb](#ga7ac3e88ca6d905ba0efe4afe5822485c)) (struct [thread\_analyzer\_info](structthread__analyzer__info.md) \*info) |
|  | Thread analyzer stack size callback function. |

| Functions | |
| --- | --- |
| void | [thread\_analyzer\_run](#gad95f59d773da7db0ffa16b06b155f655) ([thread\_analyzer\_cb](#ga7ac3e88ca6d905ba0efe4afe5822485c) cb, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cpu) |
|  | Run the thread analyzer and provide information to the callback. |
| void | [thread\_analyzer\_print](#ga4b7e9fb25842e55d7072c271b54e2769) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int cpu) |
|  | Run the thread analyzer and print stack size statistics. |

## Detailed Description

Module for analyzing threads.

This module implements functions and the configuration that simplifies thread analysis.

## Typedef Documentation

## [◆ ](#ga7ac3e88ca6d905ba0efe4afe5822485c)thread\_analyzer\_cb

| typedef void(\* thread\_analyzer\_cb) (struct [thread\_analyzer\_info](structthread__analyzer__info.md) \*info) |
| --- |

`#include <[thread_analyzer.h](thread__analyzer_8h.md)>`

Thread analyzer stack size callback function.

Callback function with thread analysis information.

Parameters
:   | info | Thread analysis information. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga4b7e9fb25842e55d7072c271b54e2769)thread\_analyzer\_print()

| void thread\_analyzer\_print | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cpu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[thread_analyzer.h](thread__analyzer_8h.md)>`

Run the thread analyzer and print stack size statistics.

This function runs the thread analyzer and prints the output in standard form. In the special case when Kconfig option THREAD\_ANALYZER\_AUTO\_SEPARATE\_CORES is set, the function analyzes only the threads running on the specified cpu.

Parameters
:   | cpu | cpu to analyze, ignored if THREAD\_ANALYZER\_AUTO\_SEPARATE\_CORES=n |
    | --- | --- |

## [◆ ](#gad95f59d773da7db0ffa16b06b155f655)thread\_analyzer\_run()

| void thread\_analyzer\_run | ( | [thread\_analyzer\_cb](#ga7ac3e88ca6d905ba0efe4afe5822485c) | *cb*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *cpu* ) |

`#include <[thread_analyzer.h](thread__analyzer_8h.md)>`

Run the thread analyzer and provide information to the callback.

This function analyzes the current state for all threads and calls a given callback on every thread found. In the special case when Kconfig option THREAD\_ANALYZER\_AUTO\_SEPARATE\_CORES is set, the function analyzes only the threads running on the specified cpu.

Parameters
:   | cb | The callback function handler |
    | --- | --- |
    | cpu | cpu to analyze, ignored if THREAD\_ANALYZER\_AUTO\_SEPARATE\_CORES=n |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
