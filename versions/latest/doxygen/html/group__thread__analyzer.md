---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__thread__analyzer.html
original_path: doxygen/html/group__thread__analyzer.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| void | [thread\_analyzer\_run](#ga21ae4723422fb96bf4f20ddb3cc1bb8d) ([thread\_analyzer\_cb](#ga7ac3e88ca6d905ba0efe4afe5822485c) cb) |
|  | Run the thread analyzer and provide information to the callback. |
| void | [thread\_analyzer\_print](#ga9ff07e2eff100f4b8c79440483c89836) (void) |
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

## [◆ ](#ga9ff07e2eff100f4b8c79440483c89836)thread\_analyzer\_print()

| void thread\_analyzer\_print | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[thread_analyzer.h](thread__analyzer_8h.md)>`

Run the thread analyzer and print stack size statistics.

This function runs the thread analyzer and prints the output in standard form.

## [◆ ](#ga21ae4723422fb96bf4f20ddb3cc1bb8d)thread\_analyzer\_run()

| void thread\_analyzer\_run | ( | [thread\_analyzer\_cb](#ga7ac3e88ca6d905ba0efe4afe5822485c) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[thread_analyzer.h](thread__analyzer_8h.md)>`

Run the thread analyzer and provide information to the callback.

This function analyzes the current state for all threads and calls a given callback on every thread found.

Parameters
:   | cb | The callback function handler |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
