---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/portability/posix/conformance/index.html
original_path: services/portability/posix/conformance/index.html
---

# POSIX Conformance

As per [IEEE 1003.1-2017](https://standards.ieee.org/ieee/1003.1/7101/), this section details Zephyr’s POSIX conformance.

## POSIX System Interfaces

POSIX System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_CHOWN\_RESTRICTED | 0 |  |
| \_POSIX\_NO\_TRUNC | 0 |  |
| \_POSIX\_VDISABLE | `'\0'` |  |

POSIX System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_VERSION | 200809L |  |
| [\_POSIX\_ASYNCHRONOUS\_IO](../option_groups/index.md#posix-option-asynchronous-io) | 200809L | [`CONFIG_POSIX_ASYNCHRONOUS_IO`](../../../../kconfig.md#CONFIG_POSIX_ASYNCHRONOUS_IO "CONFIG_POSIX_ASYNCHRONOUS_IO")[†](#posix-undefined-behaviour) |
| [\_POSIX\_BARRIERS](../option_groups/index.md#posix-option-group-barriers) | 200809L | [`CONFIG_POSIX_BARRIERS`](../../../../kconfig.md#CONFIG_POSIX_BARRIERS "CONFIG_POSIX_BARRIERS") |
| [\_POSIX\_CLOCK\_SELECTION](../option_groups/index.md#posix-option-group-clock-selection) | 200809L | [`CONFIG_POSIX_CLOCK_SELECTION`](../../../../kconfig.md#CONFIG_POSIX_CLOCK_SELECTION "CONFIG_POSIX_CLOCK_SELECTION") |
| [\_POSIX\_MAPPED\_FILES](../option_groups/index.md#posix-option-group-mapped-files) | 200809L | [`CONFIG_POSIX_MAPPED_FILES`](../../../../kconfig.md#CONFIG_POSIX_MAPPED_FILES "CONFIG_POSIX_MAPPED_FILES") |
| [\_POSIX\_MEMORY\_PROTECTION](../option_groups/index.md#posix-option-group-memory-protection) | 200809L | [`CONFIG_POSIX_MEMORY_PROTECTION`](../../../../kconfig.md#CONFIG_POSIX_MEMORY_PROTECTION "CONFIG_POSIX_MEMORY_PROTECTION") [†](#posix-undefined-behaviour) |
| [\_POSIX\_READER\_WRITER\_LOCKS](../option_groups/index.md#posix-option-reader-writer-locks) | 200809L | [`CONFIG_POSIX_READER_WRITER_LOCKS`](../../../../kconfig.md#CONFIG_POSIX_READER_WRITER_LOCKS "CONFIG_POSIX_READER_WRITER_LOCKS") |
| [\_POSIX\_REALTIME\_SIGNALS](../option_groups/index.md#posix-option-group-realtime-signals) | -1 | [`CONFIG_POSIX_REALTIME_SIGNALS`](../../../../kconfig.md#CONFIG_POSIX_REALTIME_SIGNALS "CONFIG_POSIX_REALTIME_SIGNALS") |
| [\_POSIX\_SEMAPHORES](../option_groups/index.md#posix-option-group-semaphores) | 200809L | [`CONFIG_POSIX_SEMAPHORES`](../../../../kconfig.md#CONFIG_POSIX_SEMAPHORES "CONFIG_POSIX_SEMAPHORES") |
| [\_POSIX\_SPIN\_LOCKS](../option_groups/index.md#posix-option-group-spin-locks) | 200809L | [`CONFIG_POSIX_SPIN_LOCKS`](../../../../kconfig.md#CONFIG_POSIX_SPIN_LOCKS "CONFIG_POSIX_SPIN_LOCKS") |
| [\_POSIX\_THREAD\_SAFE\_FUNCTIONS](../option_groups/index.md#posix-option-thread-safe-functions) | -1 | [`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](../../../../kconfig.md#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS "CONFIG_POSIX_THREAD_SAFE_FUNCTIONS") |
| [\_POSIX\_THREADS](../option_groups/index.md#posix-option-group-threads-base) | -1 | [`CONFIG_POSIX_THREADS`](../../../../kconfig.md#CONFIG_POSIX_THREADS "CONFIG_POSIX_THREADS") |
| [\_POSIX\_TIMEOUTS](../option_groups/index.md#posix-option-timeouts) | 200809L | [`CONFIG_POSIX_TIMEOUTS`](../../../../kconfig.md#CONFIG_POSIX_TIMEOUTS "CONFIG_POSIX_TIMEOUTS") |
| [\_POSIX\_TIMERS](../option_groups/index.md#posix-option-group-timers) | 200809L | [`CONFIG_POSIX_TIMERS`](../../../../kconfig.md#CONFIG_POSIX_TIMERS "CONFIG_POSIX_TIMERS") |
| \_POSIX2\_C\_BIND | 200809L |  |

POSIX System Interfaces (Unsupported)

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_JOB\_CONTROL | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_REGEXP | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_SAVED\_IDS | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_SHELL | -1 | [†](#posix-undefined-behaviour) |

POSIX System Interfaces (Optional)

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_ADVISORY\_INFO | -1 |  |
| [\_POSIX\_CPUTIME](../option_groups/index.md#posix-option-cputime) | 200809L | [`CONFIG_POSIX_CPUTIME`](../../../../kconfig.md#CONFIG_POSIX_CPUTIME "CONFIG_POSIX_CPUTIME") |
| [\_POSIX\_FSYNC](../option_groups/index.md#posix-option-fsync) | 200809L | [`CONFIG_POSIX_FSYNC`](../../../../kconfig.md#CONFIG_POSIX_FSYNC "CONFIG_POSIX_FSYNC") |
| [\_POSIX\_IPV6](../option_groups/index.md#posix-option-ipv6) | 200809L | [`CONFIG_POSIX_IPV6`](../../../../kconfig.md#CONFIG_POSIX_IPV6 "CONFIG_POSIX_IPV6") |
| [\_POSIX\_MEMLOCK](../option_groups/index.md#posix-option-memlock) | 200809L | [`CONFIG_POSIX_MEMLOCK`](../../../../kconfig.md#CONFIG_POSIX_MEMLOCK "CONFIG_POSIX_MEMLOCK") [†](#posix-undefined-behaviour) |
| [\_POSIX\_MEMLOCK\_RANGE](../option_groups/index.md#posix-option-memlock-range) | 200809L | [`CONFIG_POSIX_MEMLOCK_RANGE`](../../../../kconfig.md#CONFIG_POSIX_MEMLOCK_RANGE "CONFIG_POSIX_MEMLOCK_RANGE") |
| [\_POSIX\_MESSAGE\_PASSING](../option_groups/index.md#posix-option-message-passing) | 200809L | [`CONFIG_POSIX_MESSAGE_PASSING`](../../../../kconfig.md#CONFIG_POSIX_MESSAGE_PASSING "CONFIG_POSIX_MESSAGE_PASSING") |
| [\_POSIX\_MONOTONIC\_CLOCK](../option_groups/index.md#posix-option-monotonic-clock) | 200809L | [`CONFIG_POSIX_MONOTONIC_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_MONOTONIC_CLOCK "CONFIG_POSIX_MONOTONIC_CLOCK") |
| \_POSIX\_PRIORITIZED\_IO | -1 |  |
| [\_POSIX\_PRIORITY\_SCHEDULING](../option_groups/index.md#posix-option-priority-scheduling) | 200809L | [`CONFIG_POSIX_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_PRIORITY_SCHEDULING "CONFIG_POSIX_PRIORITY_SCHEDULING") |
| [\_POSIX\_RAW\_SOCKETS](../option_groups/index.md#posix-option-raw-sockets) | 200809L | [`CONFIG_POSIX_RAW_SOCKETS`](../../../../kconfig.md#CONFIG_POSIX_RAW_SOCKETS "CONFIG_POSIX_RAW_SOCKETS") |
| [\_POSIX\_SHARED\_MEMORY\_OBJECTS](../option_groups/index.md#posix-shared-memory-objects) | 200809L | [`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](../../../../kconfig.md#CONFIG_POSIX_SHARED_MEMORY_OBJECTS "CONFIG_POSIX_SHARED_MEMORY_OBJECTS") |
| \_POSIX\_SPAWN | -1 | [†](#posix-undefined-behaviour) |
| \_POSIX\_SPORADIC\_SERVER | -1 | [†](#posix-undefined-behaviour) |
| [\_POSIX\_SYNCHRONIZED\_IO](../option_groups/index.md#posix-option-synchronized-io) | 200809L | [`CONFIG_POSIX_SYNCHRONIZED_IO`](../../../../kconfig.md#CONFIG_POSIX_SYNCHRONIZED_IO "CONFIG_POSIX_SYNCHRONIZED_IO") |
| [\_POSIX\_THREAD\_ATTR\_STACKADDR](../option_groups/index.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKADDR "CONFIG_POSIX_THREAD_ATTR_STACKADDR") |
| [\_POSIX\_THREAD\_ATTR\_STACKSIZE](../option_groups/index.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKSIZE "CONFIG_POSIX_THREAD_ATTR_STACKSIZE") |
| [\_POSIX\_THREAD\_CPUTIME](../option_groups/index.md#posix-option-thread-cputime) | 200809L | [`CONFIG_POSIX_CPUTIME`](../../../../kconfig.md#CONFIG_POSIX_CPUTIME "CONFIG_POSIX_CPUTIME") |
| [\_POSIX\_THREAD\_PRIO\_INHERIT](../option_groups/index.md#posix-option-thread-prio-inherit) | 200809L | [`CONFIG_POSIX_THREAD_PRIO_INHERIT`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIO_INHERIT "CONFIG_POSIX_THREAD_PRIO_INHERIT") |
| [\_POSIX\_THREAD\_PRIO\_PROTECT](../option_groups/index.md#posix-option-thread-prio-protect) | 200809L | [`CONFIG_POSIX_THREAD_PRIO_PROTECT`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIO_PROTECT "CONFIG_POSIX_THREAD_PRIO_PROTECT") |
| [\_POSIX\_THREAD\_PRIORITY\_SCHEDULING](../option_groups/index.md#posix-option-thread-priority-scheduling) | 200809L | [`CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING "CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING") |
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
| [\_XOPEN\_STREAMS](../option_groups/index.md#posix-option-xopen-streams) | 200809L | [`CONFIG_XOPEN_STREAMS`](../../../../kconfig.md#CONFIG_XOPEN_STREAMS "CONFIG_XOPEN_STREAMS") |
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

## X/Open System Interfaces

X/Open System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| [\_POSIX\_FSYNC](../option_groups/index.md#posix-option-fsync) | 200809L | [`CONFIG_POSIX_FSYNC`](../../../../kconfig.md#CONFIG_POSIX_FSYNC "CONFIG_POSIX_FSYNC") |
| [\_POSIX\_THREAD\_ATTR\_STACKADDR](../option_groups/index.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKADDR "CONFIG_POSIX_THREAD_ATTR_STACKADDR") |
| [\_POSIX\_THREAD\_ATTR\_STACKSIZE](../option_groups/index.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKSIZE "CONFIG_POSIX_THREAD_ATTR_STACKSIZE") |
| \_POSIX\_THREAD\_PROCESS\_SHARED | -1 |  |

Note

Some features may exhibit undefined behaviour as they fall beyond the scope of Zephyr’s current
design and capabilities. For example, multi-processing, ad-hoc memory-mapping, multiple users,
or regular expressions are features that are uncommon in low-footprint embedded systems.
Such undefined behaviour is denoted with the † (obelus) symbol. Additional details
[here](../option_groups/index.md#posix-option-groups).

Note

Features listed in various POSIX Options or Option Groups may be provided in whole or in part
by a conformant C library implementation. This includes (but is not limited to) POSIX
Extensions to the ISO C Standard ([CX](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap01.html)).
