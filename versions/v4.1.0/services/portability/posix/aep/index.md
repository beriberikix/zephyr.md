---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/portability/posix/aep/index.html
original_path: services/portability/posix/aep/index.html
---

# POSIX Application Environment Profiles (AEP)

Although inactive, [IEEE 1003.13-2003](https://standards.ieee.org/ieee/1003.13/3322/) defined a number of AEP that inspired the modern
subprofiling options of [IEEE 1003.1-2017](https://standards.ieee.org/ieee/1003.1/7101/). The single-purpose realtime system profiles
are listed below, for reference, in terms that agree with the current POSIX-1 standard. PSE54
is not considered at this time.

## System Interfaces

The required POSIX [System Interfaces](../conformance/index.md#posix-system-interfaces-required) are supported for
each Application Environment Profile.

[![Required System Interfaces](../../../../_images/si.svg)
](../../../../_images/si.svg)

System Interfaces

## Minimal Realtime System Profile (PSE51)

The *Minimal Realtime System Profile* (PSE51) includes all of the
[System Interfaces](../conformance/index.md#posix-system-interfaces-required) along with several additional features.

[![Minimal Realtime System Profile (PSE51)](../../../../_images/aep-pse51.svg)
](../../../../_images/aep-pse51.svg)

Minimal Realtime System Profile (PSE51)

PSE51 System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_AEP\_REALTIME\_MINIMAL | -1 | [`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](../../../../kconfig.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL "CONFIG_POSIX_AEP_REALTIME_MINIMAL") |

PSE51 Option Groups

| Symbol | Support | Remarks |
| --- | --- | --- |
| [POSIX\_C\_LANG\_JUMP](../option_groups/index.md#posix-option-group-c-lang-jump) | yes |  |
| [POSIX\_C\_LANG\_SUPPORT](../option_groups/index.md#posix-option-group-c-lang-support) | yes |  |
| [POSIX\_DEVICE\_IO](../option_groups/index.md#posix-option-group-device-io) | yes | [`CONFIG_POSIX_DEVICE_IO`](../../../../kconfig.md#CONFIG_POSIX_DEVICE_IO "CONFIG_POSIX_DEVICE_IO") |
| [POSIX\_SIGNALS](../option_groups/index.md#posix-option-group-signals) | yes | [`CONFIG_POSIX_SIGNALS`](../../../../kconfig.md#CONFIG_POSIX_SIGNALS "CONFIG_POSIX_SIGNALS") [†](../conformance/index.md#posix-undefined-behaviour) |
| [POSIX\_SINGLE\_PROCESS](../option_groups/index.md#posix-option-group-single-process) | yes | [`CONFIG_POSIX_SINGLE_PROCESS`](../../../../kconfig.md#CONFIG_POSIX_SINGLE_PROCESS "CONFIG_POSIX_SINGLE_PROCESS") |
| [XSI\_THREADS\_EXT](../option_groups/index.md#posix-option-group-xsi-threads-ext) | yes | [`CONFIG_XSI_THREADS_EXT`](../../../../kconfig.md#CONFIG_XSI_THREADS_EXT "CONFIG_XSI_THREADS_EXT") |

PSE51 Option Requirements

| Symbol | Support | Remarks |
| --- | --- | --- |
| [\_POSIX\_FSYNC](../option_groups/index.md#posix-option-fsync) | 200809L | [`CONFIG_POSIX_FSYNC`](../../../../kconfig.md#CONFIG_POSIX_FSYNC "CONFIG_POSIX_FSYNC") |
| [\_POSIX\_MEMLOCK](../option_groups/index.md#posix-option-memlock) | 200809L | [`CONFIG_POSIX_MEMLOCK`](../../../../kconfig.md#CONFIG_POSIX_MEMLOCK "CONFIG_POSIX_MEMLOCK") [†](../conformance/index.md#posix-undefined-behaviour) |
| [\_POSIX\_MEMLOCK\_RANGE](../option_groups/index.md#posix-option-memlock-range) | 200809L | [`CONFIG_POSIX_MEMLOCK_RANGE`](../../../../kconfig.md#CONFIG_POSIX_MEMLOCK_RANGE "CONFIG_POSIX_MEMLOCK_RANGE") |
| [\_POSIX\_MONOTONIC\_CLOCK](../option_groups/index.md#posix-option-monotonic-clock) | 200809L | [`CONFIG_POSIX_MONOTONIC_CLOCK`](../../../../kconfig.md#CONFIG_POSIX_MONOTONIC_CLOCK "CONFIG_POSIX_MONOTONIC_CLOCK") |
| [\_POSIX\_SHARED\_MEMORY\_OBJECTS](../option_groups/index.md#posix-option-shared-memory-objects) | 200809L | [`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](../../../../kconfig.md#CONFIG_POSIX_SHARED_MEMORY_OBJECTS "CONFIG_POSIX_SHARED_MEMORY_OBJECTS") |
| [\_POSIX\_SYNCHRONIZED\_IO](../option_groups/index.md#posix-option-synchronized-io) | 200809L | [`CONFIG_POSIX_SYNCHRONIZED_IO`](../../../../kconfig.md#CONFIG_POSIX_SYNCHRONIZED_IO "CONFIG_POSIX_SYNCHRONIZED_IO") |
| [\_POSIX\_THREAD\_ATTR\_STACKADDR](../option_groups/index.md#posix-option-thread-attr-stackaddr) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKADDR "CONFIG_POSIX_THREAD_ATTR_STACKADDR") |
| [\_POSIX\_THREAD\_ATTR\_STACKSIZE](../option_groups/index.md#posix-option-thread-attr-stacksize) | 200809L | [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](../../../../kconfig.md#CONFIG_POSIX_THREAD_ATTR_STACKSIZE "CONFIG_POSIX_THREAD_ATTR_STACKSIZE") |
| [\_POSIX\_THREAD\_CPUTIME](../option_groups/index.md#posix-option-thread-cputime) | 200809L | [`CONFIG_POSIX_CPUTIME`](../../../../kconfig.md#CONFIG_POSIX_CPUTIME "CONFIG_POSIX_CPUTIME") |
| [\_POSIX\_THREAD\_PRIO\_INHERIT](../option_groups/index.md#posix-option-thread-prio-inherit) | 200809L | [`CONFIG_POSIX_THREAD_PRIO_INHERIT`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIO_INHERIT "CONFIG_POSIX_THREAD_PRIO_INHERIT") |
| [\_POSIX\_THREAD\_PRIO\_PROTECT](../option_groups/index.md#posix-option-thread-prio-protect) | 200809L | [`CONFIG_POSIX_THREAD_PRIO_PROTECT`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIO_PROTECT "CONFIG_POSIX_THREAD_PRIO_PROTECT") |
| [\_POSIX\_THREAD\_PRIORITY\_SCHEDULING](../option_groups/index.md#posix-option-thread-priority-scheduling) | 200809L | [`CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`](../../../../kconfig.md#CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING "CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING") |
| \_POSIX\_THREAD\_SPORADIC\_SERVER | -1 |  |

## Realtime Controller System Profile (PSE52)

The *Realtime Controller System Profile* (PSE52) includes all features from PSE51 and the
[System Interfaces](../conformance/index.md#posix-system-interfaces-required).

[![Realtime Controller System Profile (PSE52)](../../../../_images/aep-pse52.svg)
](../../../../_images/aep-pse52.svg)

Realtime Controller System Profile (PSE52)

PSE52 System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_AEP\_REALTIME\_CONTROLLER | -1 | [`CONFIG_POSIX_AEP_REALTIME_CONTROLLER`](../../../../kconfig.md#CONFIG_POSIX_AEP_REALTIME_CONTROLLER "CONFIG_POSIX_AEP_REALTIME_CONTROLLER") |

PSE52 Option Groups

| Symbol | Support | Remarks |
| --- | --- | --- |
| [POSIX\_C\_LANG\_MATH](../option_groups/index.md#posix-option-group-c-lang-math) | yes |  |
| [POSIX\_FD\_MGMT](../option_groups/index.md#posix-option-group-fd-mgmt) |  | [`CONFIG_POSIX_FD_MGMT`](../../../../kconfig.md#CONFIG_POSIX_FD_MGMT "CONFIG_POSIX_FD_MGMT") |
| [POSIX\_FILE\_SYSTEM](../option_groups/index.md#posix-option-group-file-system) |  | [`CONFIG_POSIX_FILE_SYSTEM`](../../../../kconfig.md#CONFIG_POSIX_FILE_SYSTEM "CONFIG_POSIX_FILE_SYSTEM") |

PSE52 Option Requirements

| Symbol | Support | Remarks |
| --- | --- | --- |
| [\_POSIX\_MESSAGE\_PASSING](../option_groups/index.md#posix-option-message-passing) | 200809L | [`CONFIG_POSIX_MESSAGE_PASSING`](../../../../kconfig.md#CONFIG_POSIX_MESSAGE_PASSING "CONFIG_POSIX_MESSAGE_PASSING") |
| \_POSIX\_TRACE | -1 |  |
| \_POSIX\_TRACE\_EVENT\_FILTER | -1 |  |
| \_POSIX\_TRACE\_LOG | -1 |  |

## Dedicated Realtime System Profile (PSE53)

The *Dedicated Realtime System Profile* (PSE53) includes all features from PSE52, PSE51, and the
[System Interfaces](../conformance/index.md#posix-system-interfaces-required).

[![Dedicated Realtime System Profile (PSE53)](../../../../_images/aep-pse53.svg)
](../../../../_images/aep-pse53.svg)

Dedicated Realtime System Profile (PSE53)

PSE53 System Interfaces

| Symbol | Support | Remarks |
| --- | --- | --- |
| \_POSIX\_AEP\_REALTIME\_DEDICATED | -1 | [`CONFIG_POSIX_AEP_REALTIME_DEDICATED`](../../../../kconfig.md#CONFIG_POSIX_AEP_REALTIME_DEDICATED "CONFIG_POSIX_AEP_REALTIME_DEDICATED") |

PSE53 Option Groups

| Symbol | Support | Remarks |
| --- | --- | --- |
| [POSIX\_MULTI\_PROCESS](../option_groups/index.md#posix-option-group-multi-process) |  | [`CONFIG_POSIX_MULTI_PROCESS`](../../../../kconfig.md#CONFIG_POSIX_MULTI_PROCESS "CONFIG_POSIX_MULTI_PROCESS")[†](../conformance/index.md#posix-undefined-behaviour) |
| [POSIX\_NETWORKING](../option_groups/index.md#posix-option-group-networking) | yes | [`CONFIG_POSIX_NETWORKING`](../../../../kconfig.md#CONFIG_POSIX_NETWORKING "CONFIG_POSIX_NETWORKING") |
| [POSIX\_PIPE](../option_groups/index.md#posix-option-group-pipe) |  |  |
| [POSIX\_SIGNAL\_JUMP](../option_groups/index.md#posix-option-group-signal-jump) |  |  |

PSE53 Option Requirements

| Symbol | Support | Remarks |
| --- | --- | --- |
| [\_POSIX\_CPUTIME](../option_groups/index.md#posix-option-cputime) | 200809L | [`CONFIG_POSIX_CPUTIME`](../../../../kconfig.md#CONFIG_POSIX_CPUTIME "CONFIG_POSIX_CPUTIME") |
| \_POSIX\_PRIORITIZED\_IO | -1 |  |
| [\_POSIX\_PRIORITY\_SCHEDULING](../option_groups/index.md#posix-option-priority-scheduling) | -1 |  |
| [\_POSIX\_RAW\_SOCKETS](../option_groups/index.md#posix-option-raw-sockets) | 200809L | [`CONFIG_POSIX_RAW_SOCKETS`](../../../../kconfig.md#CONFIG_POSIX_RAW_SOCKETS "CONFIG_POSIX_RAW_SOCKETS") |
| \_POSIX\_SPAWN | -1 | [†](../conformance/index.md#posix-undefined-behaviour) |
| \_POSIX\_SPORADIC\_SERVER | -1 | [†](../conformance/index.md#posix-undefined-behaviour) |
