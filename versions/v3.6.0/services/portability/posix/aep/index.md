---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/portability/posix/aep/index.html
original_path: services/portability/posix/aep/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# POSIX Application Environment Profiles (AEP)

Although inactive, [IEEE 1003.13-2003](https://standards.ieee.org/ieee/1003.13/3322/) defined a number of AEP that inspired the modern
subprofiling options of [IEEE 1003.1-2017](https://standards.ieee.org/ieee/1003.1/7101/). The single-purpose realtime system profiles
are listed below, for reference, in terms that agree with the current POSIX-1 standard. PSE54
is not considered at this time.

## Minimal Realtime System Profile (PSE51)

PSE51 System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_AEP\_REALTIME\_MINIMAL | -1 |  |

PSE51 Option Groups

| Symbol | Support | Remarks |
| --- | --- | --- |
| POSIX\_C\_LANG\_JUMP | yes | [POSIX\_C\_LANG\_JUMP](../option_groups/index.md#posix-option-group-c-lang-jump) |
| POSIX\_C\_LANG\_SUPPORT | yes | [POSIX\_C\_LANG\_SUPPORT](../option_groups/index.md#posix-option-group-c-lang-support) |
| POSIX\_DEVICE\_IO |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_FILE\_LOCKING |  |  |
| POSIX\_SIGNALS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_SINGLE\_PROCESS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_THREADS\_BASE | yes | [†](../conformance/index.md#posix-undefined-behaviour) |
| XSI\_THREADS\_EXT | yes | [†](../conformance/index.md#posix-undefined-behaviour) |

PSE51 Option Requirements

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_CLOCK\_SELECTION | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_FSYNC | -1 |  |
| \_POSIX\_MEMLOCK | -1 |  |
| \_POSIX\_MEMLOCK\_RANGE | -1 |  |
| \_POSIX\_MONOTONIC\_CLOCK | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_REALTIME\_SIGNALS | -1 |  |
| \_POSIX\_SEMAPHORES | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_SHARED\_MEMORY\_OBJECTS | -1 |  |
| \_POSIX\_SYNCHRONIZED\_IO | -1 |  |
| \_POSIX\_THREAD\_ATTR\_STACKADDR | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_ATTR\_STACKSIZE | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_CPUTIME | -1 |  |
| \_POSIX\_THREAD\_PRIO\_INHERIT | 200809L | [`CONFIG_PTHREAD_MUTEX`](../../../../kconfig.md#CONFIG_PTHREAD_MUTEX "CONFIG_PTHREAD_MUTEX") |
| \_POSIX\_THREAD\_PRIO\_PROTECT | -1 |  |
| \_POSIX\_THREAD\_PRIORITY\_SCHEDULING | -1 | [`CONFIG_POSIX_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_PRIORITY_SCHEDULING "CONFIG_POSIX_PRIORITY_SCHEDULING") (will fail with `ENOSYS`[†](../conformance/index.md#posix-undefined-behaviour)) |
| \_POSIX\_THREAD\_SPORADIC\_SERVER | -1 |  |
| \_POSIX\_TIMEOUTS | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_TIMERS | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |

## Realtime Controller System Profile (PSE52)

PSE52 System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_AEP\_REALTIME\_CONTROLLER | -1 |  |

PSE52 Option Groups

| Symbol | Support | Remarks |
| --- | --- | --- |
| POSIX\_C\_LANG\_JUMP | yes | [POSIX\_C\_LANG\_JUMP](../option_groups/index.md#posix-option-group-c-lang-jump) |
| POSIX\_C\_LANG\_MATH | yes | [POSIX\_C\_LANG\_MATH](../option_groups/index.md#posix-option-group-c-lang-math) |
| POSIX\_C\_LANG\_SUPPORT | yes | [POSIX\_C\_LANG\_SUPPORT](../option_groups/index.md#posix-option-group-c-lang-support) |
| POSIX\_DEVICE\_IO |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_FD\_MGMT |  |  |
| POSIX\_FILE\_LOCKING |  |  |
| POSIX\_FILE\_SYSTEM |  |  |
| POSIX\_SIGNALS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_SINGLE\_PROCESS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_THREADS\_BASE | yes | [†](../conformance/index.md#posix-undefined-behaviour) |
| XSI\_THREADS\_EXT | yes | [†](../conformance/index.md#posix-undefined-behaviour) |

PSE52 Option Requirements

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_CLOCK\_SELECTION | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_FSYNC | -1 |  |
| \_POSIX\_MAPPED\_FILES | -1 |  |
| \_POSIX\_MEMLOCK | -1 |  |
| \_POSIX\_MEMLOCK\_RANGE | -1 |  |
| \_POSIX\_MESSAGE\_PASSING | 200809L | [`CONFIG_POSIX_MQUEUE`](../../../../kconfig.md#CONFIG_POSIX_MQUEUE "CONFIG_POSIX_MQUEUE") |
| \_POSIX\_MONOTONIC\_CLOCK | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_REALTIME\_SIGNALS | -1 |  |
| \_POSIX\_SEMAPHORES | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_SHARED\_MEMORY\_OBJECTS | -1 |  |
| \_POSIX\_SYNCHRONIZED\_IO | -1 |  |
| \_POSIX\_THREAD\_ATTR\_STACKADDR | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_ATTR\_STACKSIZE | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_CPUTIME | -1 |  |
| \_POSIX\_THREAD\_PRIO\_INHERIT | 200809L | [`CONFIG_PTHREAD_MUTEX`](../../../../kconfig.md#CONFIG_PTHREAD_MUTEX "CONFIG_PTHREAD_MUTEX") |
| \_POSIX\_THREAD\_PRIO\_PROTECT | -1 |  |
| \_POSIX\_THREAD\_PRIORITY\_SCHEDULING | -1 |  |
| \_POSIX\_THREAD\_SPORADIC\_SERVER | -1 |  |
| \_POSIX\_TIMEOUTS | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_TIMERS | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_TRACE | -1 |  |
| \_POSIX\_TRACE\_EVENT\_FILTER | -1 |  |
| \_POSIX\_TRACE\_LOG | -1 |  |

## Dedicated Realtime System Profile (PSE53)

PSE53 System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_AEP\_REALTIME\_DEDICATED | -1 |  |

PSE53 Option Groups

| Symbol | Support | Remarks |
| --- | --- | --- |
| POSIX\_C\_LANG\_JUMP | yes | [POSIX\_C\_LANG\_JUMP](../option_groups/index.md#posix-option-group-c-lang-jump) |
| POSIX\_C\_LANG\_MATH | yes | [POSIX\_C\_LANG\_MATH](../option_groups/index.md#posix-option-group-c-lang-math) |
| POSIX\_C\_LANG\_SUPPORT | yes | [POSIX\_C\_LANG\_SUPPORT](../option_groups/index.md#posix-option-group-c-lang-support) |
| POSIX\_DEVICE\_IO |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_FD\_MGMT |  |  |
| POSIX\_FILE\_LOCKING |  |  |
| POSIX\_FILE\_SYSTEM |  |  |
| POSIX\_MULTI\_PROCESS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_NETWORKING | yes | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_PIPE |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_SIGNALS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_SIGNAL\_JUMP |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_SINGLE\_PROCESS |  | [†](../conformance/index.md#posix-undefined-behaviour) |
| POSIX\_THREADS\_BASE | yes | [†](../conformance/index.md#posix-undefined-behaviour) |
| XSI\_THREADS\_EXT | yes | [†](../conformance/index.md#posix-undefined-behaviour) |

PSE53 Option Requirements

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_ASYNCHRONOUS\_IO | -1 |  |
| \_POSIX\_CLOCK\_SELECTION | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_CPUTIME | -1 |  |
| \_POSIX\_FSYNC | -1 |  |
| \_POSIX\_MAPPED\_FILES | -1 |  |
| \_POSIX\_MEMLOCK | -1 |  |
| \_POSIX\_MEMLOCK\_RANGE | -1 |  |
| \_POSIX\_MEMORY\_PROTECTION | -1 |  |
| \_POSIX\_MESSAGE\_PASSING | 200809L | [`CONFIG_POSIX_MQUEUE`](../../../../kconfig.md#CONFIG_POSIX_MQUEUE "CONFIG_POSIX_MQUEUE") |
| \_POSIX\_MONOTONIC\_CLOCK | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_PRIORITIZED\_IO | -1 |  |
| \_POSIX\_PRIORITY\_SCHEDULING | -1 |  |
| \_POSIX\_RAW\_SOCKETS | 200809L | [`CONFIG_NET_SOCKETS`](../../../../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS") |
| \_POSIX\_REALTIME\_SIGNALS | -1 |  |
| \_POSIX\_SEMAPHORES | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_SHARED\_MEMORY\_OBJECTS | -1 |  |
| \_POSIX\_SPAWN | -1 |  |
| \_POSIX\_SPORADIC\_SERVER | -1 |  |
| \_POSIX\_SYNCHRONIZED\_IO | -1 |  |
| \_POSIX\_THREAD\_ATTR\_STACKADDR | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_ATTR\_STACKSIZE | 200809L | [`CONFIG_PTHREAD`](../../../../kconfig.md#CONFIG_PTHREAD "CONFIG_PTHREAD") |
| \_POSIX\_THREAD\_CPUTIME | -1 |  |
| \_POSIX\_THREAD\_PRIO\_INHERIT | 200809L | [`CONFIG_PTHREAD_MUTEX`](../../../../kconfig.md#CONFIG_PTHREAD_MUTEX "CONFIG_PTHREAD_MUTEX") |
| \_POSIX\_THREAD\_PRIO\_PROTECT | -1 |  |
| \_POSIX\_THREAD\_PRIORITY\_SCHEDULING | -1 |  |
| \_POSIX\_THREAD\_PROCESS\_SHARED | -1 |  |
| \_POSIX\_THREAD\_SPORADIC\_SERVER | -1 |  |
| \_POSIX\_TIMEOUTS | 200809L | [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC") |
| \_POSIX\_TIMERS | 200809L | [`CONFIG_POSIX_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK") |
| \_POSIX\_TRACE | -1 |  |
| \_POSIX\_TRACE\_EVENT\_FILTER | -1 |  |
| \_POSIX\_TRACE\_LOG | -1 |  |
