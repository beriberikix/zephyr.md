---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/portability/posix/conformance/index.html
original_path: services/portability/posix/conformance/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# POSIX Conformance

As per IEEE 1003.1-2017, this section details Zephyr’s POSIX conformance.

Note

As per POSIX 1003.13, single process mode is supported directly by both PSE51 and PSE52
profiles. While Zephyr includes support for many features found in PSE53, PSE53 itself requires
supporting multiple processes. Since supporting multiple processes is beyond the scope of
Zephyr’s current design, some features requiring multi-process capabilities may exhibit
undefined behaviour, which we denote with the † (obelus) symbol.

Note

Features listed in various POSIX Options or Option Groups may be provided in whole or in part
by a conformant C library implementation. This includes (but is not limited to) POSIX
Extensions to the ISO C Standard ([CX](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap01.html)).

## POSIX System Interfaces

POSIX System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_CHOWN\_RESTRICTED | 0 |  |
| \_POSIX\_NO\_TRUNC | 0 |  |
| \_POSIX\_VDISABLE | 0 |  |

POSIX System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_JOB\_CONTROL | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_REGEXP | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_SAVED\_IDS | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_SHELL | -1 | [†](#posix-undefined-behaviour) |

POSIX System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_VERSION | 200809L |  |
| \_POSIX\_ASYNCHRONOUS\_IO | -1 | [†](#posix-undefined-behaviour) |
| [\_POSIX\_BARRIERS](../option_groups/index.md#posix-option-group-barriers) | 200809L | [`CONFIG_PTHREAD_BARRIER`](../../../../kconfig.md#CONFIG_PTHREAD_BARRIER "CONFIG_PTHREAD_BARRIER") |
| [\_POSIX\_CLOCK\_SELECTION](../option_groups/index.md#posix-option-group-clock-selection) | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_MAPPED\_FILES | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_MEMORY\_PROTECTION | -1 | [†](#posix-undefined-behaviour) |
| [\_POSIX\_READER\_WRITER\_LOCKS](../option_groups/index.md#posix-option-reader-writer-locks) | -1 | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_REALTIME\_SIGNALS | -1 | [†](#posix-undefined-behaviour) |
| [\_POSIX\_SEMAPHORES](../option_groups/index.md#posix-option-group-semaphores) | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| [\_POSIX\_SPIN\_LOCKS](../option_groups/index.md#posix-option-group-spin-locks) | 200809L | [`CONFIG_PTHREAD_SPINLOCK`](../../../../kconfig.md#CONFIG_PTHREAD_SPINLOCK "CONFIG_PTHREAD_SPINLOCK") |
| [\_POSIX\_THREAD\_SAFE\_FUNCTIONS](../option_groups/index.md#posix-thread-safe-functions) | -1 |  |
| [\_POSIX\_THREADS](../option_groups/index.md#posix-option-group-threads-base) | -1 | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| [\_POSIX\_TIMEOUTS](../option_groups/index.md#posix-option-timeouts) | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| [\_POSIX\_TIMERS](../option_groups/index.md#posix-option-group-timers) | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX2\_C\_BIND | 200809L |  |

POSIX System Interfaces (Optional)

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_ADVISORY\_INFO | -1 |  |
| \_POSIX\_CPUTIME | -1 |  |
| \_POSIX\_FSYNC | -1 |  |
| \_POSIX\_IPV6 | 200809L | [`CONFIG_NET_IPV6`](../../../../kconfig.md#CONFIG_NET_IPV6 "CONFIG_NET_IPV6") |
| \_POSIX\_MEMLOCK | -1 |  |
| \_POSIX\_MEMLOCK\_RANGE | -1 |  |
| [\_POSIX\_MESSAGE\_PASSING](../option_groups/index.md#posix-option-message-passing) | 200809L | [`CONFIG_POSIX_MQUEUE`](../../../../kconfig.md#CONFIG_POSIX_MQUEUE "CONFIG_POSIX_MQUEUE") |
| \_POSIX\_MONOTONIC\_CLOCK | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_PRIORITIZED\_IO | -1 |  |
| [\_POSIX\_PRIORITY\_SCHEDULING](../option_groups/index.md#posix-option-priority-scheduling) | -1 | [`CONFIG_POSIX_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_PRIORITY_SCHEDULING "CONFIG_POSIX_PRIORITY_SCHEDULING") (will fail with `ENOSYS`[†](#posix-undefined-behaviour)) |
| \_POSIX\_RAW\_SOCKETS | 200809L | [`CONFIG_NET_SOCKETS`](../../../../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS") |
| \_POSIX\_SHARED\_MEMORY\_OBJECTS | -1 |  |
| \_POSIX\_SPAWN | -1 |  |
| \_POSIX\_SPORADIC\_SERVER | -1 |  |
| \_POSIX\_SYNCHRONIZED\_IO | -1 |  |
| [\_POSIX\_THREAD\_ATTR\_STACKADDR](../option_groups/index.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_CPUTIME | -1 |  |
| [\_POSIX\_THREAD\_ATTR\_STACKSIZE](../option_groups/index.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_PRIO\_INHERIT | 200809L | [`CONFIG_PTHREAD_MUTEX`](../../../../kconfig.md#CONFIG_PTHREAD_MUTEX "CONFIG_PTHREAD_MUTEX") |
| \_POSIX\_THREAD\_PRIO\_PROTECT | -1 |  |
| [\_POSIX\_THREAD\_PRIORITY\_SCHEDULING](../option_groups/index.md#posix-option-thread-priority-scheduling) | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_PROCESS\_SHARED | -1 |  |
| \_POSIX\_THREAD\_SPORADIC\_SERVER | -1 |  |
| \_POSIX\_TRACE | -1 |  |
| \_POSIX\_TRACE\_EVENT\_FILTER | -1 |  |
| \_POSIX\_TRACE\_INHERIT | -1 |  |
| \_POSIX\_TRACE\_LOG | -1 |  |
| \_POSIX\_TYPED\_MEMORY\_OBJECTS | -1 |  |
| \_XOPEN\_CRYPT | -1 |  |
| \_XOPEN\_REALTIME | -1 |  |
| \_XOPEN\_REALTIME\_THREADS | -1 |  |
| [\_XOPEN\_STREAMS](../option_groups/index.md#posix-option-xopen-streams) | -1 | [`CONFIG_NET_SOCKETS`](../../../../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS") |
| \_XOPEN\_UNIX | -1 |  |

## POSIX Shell and Utilities

Zephyr does not support a POSIX shell or utilities at this time.

POSIX Shell and Utilities

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX2\_C\_DEV | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_CHAR\_TERM | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_FORT\_DEV | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_FORT\_RUN | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_LOCALEDEF | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_PBS | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_PBS\_ACCOUNTING | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_PBS\_LOCATE | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_PBS\_MESSAGE | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_PBS\_TRACK | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_SW\_DEV | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_UPE | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_UNIX | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX2\_UUCP | -1 | [†](#posix-undefined-behaviour) |

# XSI Conformance

## XSI System Interfaces

XSI System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_FSYNC | -1 | [†](#posix-undefined-behaviour) |
| [\_POSIX\_THREAD\_ATTR\_STACKADDR](../option_groups/index.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| [\_POSIX\_THREAD\_ATTR\_STACKSIZE](../option_groups/index.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_PROCESS\_SHARED | -1 |  |
