---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/portability/posix/overview/index.html
original_path: services/portability/posix/overview/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Overview

The Portable Operating System Interface (POSIX) is a family of standards specified by the
[IEEE Computer Society](https://www.computer.org/) for maintaining compatibility between operating systems. Zephyr
implements a subset of the standard POSIX API specified by [IEEE 1003.1-2017](https://standards.ieee.org/ieee/1003.1/7101/) (also known as
POSIX-1.2017).

![POSIX Support in Zephyr](../../../../_images/posix.svg)

POSIX support in Zephyr

Note

This page does not document Zephyr’s [POSIX architecture](../../../../boards/posix/doc/arch_soc.md#posix-arch), which is used to
run Zephyr as a native application under the host operating system for prototyping,
test, and diagnostic purposes.

With the POSIX support available in Zephyr, an existing POSIX conformant
application can be ported to run on the Zephyr kernel, and therefore leverage
Zephyr features and functionality. Additionally, a library designed to be
POSIX conformant can be ported to Zephyr kernel based applications with no changes.

The POSIX API is an increasingly popular OSAL (operating system abstraction layer) for IoT and
embedded applications, as can be seen in Zephyr, AWS:FreeRTOS, TI-RTOS, and NuttX.

Benefits of POSIX support in Zephyr include:

- Offering a familiar API to non-embedded programmers, especially from Linux
- Enabling reuse (portability) of existing libraries based on POSIX APIs
- Providing an efficient API subset appropriate for small (MCU) embedded systems

## POSIX Subprofiles

While Zephyr supports running multiple threads <threads\_v2> (possibly in an SMP <smp\_arch>
configuration), as well as Virtual Memory and MMUs <memory\_management\_api>, Zephyr code and data
normally share a common address space. The Zephyr kernel executable code and the application
executable code are typically compiled into the same binary artifact. From that perspective, Zephyr
apps can be seen as running in the context of a single process.

While multi-purpose operating systems (OS) offer full POSIX conformance, Real-Time Operating
Systems (RTOS) such as Zephyr typically serve a fixed-purpose, have limited hardware resources,
and experience limited user interaction. In such systems, full POSIX conformance can be
impractical and unnecessary.

For that reason, POSIX defined the following [Application Environment Profiles (AEP)](../aep/index.md#posix-aep)
as part of [IEEE 1003.13-2003](https://standards.ieee.org/ieee/1003.13/3322/) (also known as POSIX.13-2003).

- Minimal Realtime System Profile ([PSE51](../aep/index.md#posix-aep-pse51))
- Realtime Controller System Profile ([PSE52](../aep/index.md#posix-aep-pse52))
- Dedicated Realtime System Profile ([PSE53](../aep/index.md#posix-aep-pse53))
- Multi-Purpose Realtime System (PSE54)

POSIX.13-2003 AEP were formalized in 2003 via “Units of Functionality” but the specification is now
inactive (for reference only). Nevertheless, the intent is still captured as part of POSIX-1.2017
via [Options](../option_groups/index.md#posix-options) and [Option Groups](../option_groups/index.md#posix-option-groups).

For more information, please see [IEEE 1003.1-2017, Section E, Subprofiling Considerations](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html).

## POSIX Applications in Zephyr

A POSIX app in Zephyr is [built like any other app](../../../../develop/application/index.md#application) and therefore requires the
usual `prj.conf`, `CMakeLists.txt`, and source code. For example, the app below
leverages the `nanosleep()` and `perror()` POSIX functions.

prj.conf for a simple POSIX app in Zephyr

```cfg
 CONFIG_POSIX_API=y
```

A simple app that uses Zephyr’s POSIX API

```c
 #include <stddef.h>
 #include <stdio.h>
 #include <time.h>

 void megasleep(size_t megaseconds)
 {
     struct timespec ts = {
         .tv_sec = megaseconds * 1000000,
         .tv_nsec = 0,
     };

     printf("See you in a while!\n");
     if (nanosleep(&ts, NULL) == -1) {
         perror("nanosleep");
     }
 }

 int main()
 {
     megasleep(42);
     return 0;
 }
```

For more examples of POSIX applications, please see the [POSIX sample applications](../../../../samples/posix/posix.md#posix-samples).

## Configuration

Like most features in Zephyr, POSIX features are
[highly configurable](../../../../introduction/index.md#zephyr-intro-configurability) but disabled by default. Users must
explicitly choose to enable POSIX options via [Kconfig](../../../../build/kconfig/index.md#kconfig) selection. Indeed, there are
[many Kconfig options in Zephyr](../kconfig/index.md#posix-kconfig-options) for the POSIX API to allow for
feature selection at various levels of granularity.

Alternatively, users may enable one of the Kconfig options below as a shortcut to enable multiple
[Option Groups](../option_groups/index.md#posix-option-groups).

- [`CONFIG_POSIX_API`](../../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API")
- [`CONFIG_PTHREAD_IPC`](../../../../kconfig.md#CONFIG_PTHREAD_IPC "CONFIG_PTHREAD_IPC")

Note

Since the POSIX environment in Zephyr is fully configurable via [Kconfig](../../../../build/kconfig/index.md#kconfig),
configurations that require modifying features should not be made if strict compliance is
required (POSIX-1.2017, section 2.1.3.1).
