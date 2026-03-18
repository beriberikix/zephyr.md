---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/glossary.html
original_path: glossary.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Glossary of Terms

API
:   (Application Program Interface) A defined set of routines and protocols for
    building application software.

application
:   The set of user-supplied files that the Zephyr build system uses
    to build an application image for a specified board configuration.
    It can contain application-specific code, kernel configuration settings,
    and at least one CMakeLists.txt file.
    The application’s kernel configuration settings direct the build system
    to create a custom kernel that makes efficient use of the board’s
    resources.
    An application can sometimes be built for more than one type of board
    configuration (including boards with different CPU architectures),
    if it does not require any board-specific capabilities.

application image
:   A binary file that is loaded and executed by the board for which
    it was built.
    Each application image contains both the application’s code and the
    Zephyr kernel code needed to support it. They are compiled as a single,
    fully-linked binary.
    Once an application image is loaded onto a board, the image takes control
    of the system, initializes it, and runs as the system’s sole application.
    Both application code and kernel code execute as privileged code
    within a single shared address space.

architecture
:   An instruction set architecture (ISA) along with a programming model.

board
:   A target system with a defined set of devices and capabilities,
    which can load and execute an application image. It may be an actual
    hardware system or a simulated system running under QEMU. A board can
    contain one or more [SoCs](#term-SoC).
    The Zephyr kernel supports a [variety of boards](boards/index.md#boards).

board configuration
:   A set of kernel configuration options that specify how the devices
    present on a board are used by the kernel.
    The Zephyr build system defines one or more board configurations
    for each board it supports. The kernel configuration settings that are
    specified by the build system can be over-ridden by the application,
    if desired.

board name
:   The human-readable name of a [board](#term-board). Uniquely and descriptively
    identifies a particular system, but does not include additional
    information that may be required to actually build a Zephyr image for it.
    See [Board terminology](hardware/porting/board_porting.md#board-terminology) for additional details.

board qualifiers
:   The set of additional tokens, separated by a forward slash (/) that
    follow the [board name](#term-board-name) (and optionally [board revision](#term-board-revision)) to
    form the [board target](#term-board-target). The currently accepted qualifiers are
    [SoC](#term-SoC), [CPU cluster](#term-CPU-cluster) and [variant](#term-variant).
    See [Board terminology](hardware/porting/board_porting.md#board-terminology) for additional details.

board revision
:   An optional version string that identifies a particular revision of a
    hardware system. This is useful to avoid duplication of board files
    whenever small changes are introduced to a hardware system.
    See [Multiple board revisions](hardware/porting/board_porting.md#porting-board-revisions) and [Building for a board revision](develop/application/index.md#application-board-version)
    for more information.

board target
:   The full string that can be provided to any of the Zephyr build tools to
    compile and link an image for a particular hardware system. This string
    uniquely identifies the combination of [board name](#term-board-name), [board
    revision](#term-board-revision) and [board qualifiers](#term-board-qualifiers).
    See [Board terminology](hardware/porting/board_porting.md#board-terminology) for additional details.

CPU cluster
:   A group of one or more [CPU cores](#term-CPU-core), all executing the same image
    within the same address space and in a symmetrical (SMP) configuration.
    Only [CPU cores](#term-CPU-core) of the same [architecture](#term-architecture) can be in a single
    cluster. Multiple CPU clusters (each of one or more cores) can coexist in
    the same [SoC](#term-SoC).

CPU core
:   A single processing unit, with its own Program Counter, executing program
    instructions sequentially. CPU cores are part of a [CPU cluster](#term-CPU-cluster),
    which can contain one or more cores.

device runtime power management
:   Device Runtime Power Management (PM) refers the capability of devices to
    save energy independently of the system power state. Devices will keep
    reference of their usage and will automatically be suspended or resumed.
    This feature is enabled via the [`CONFIG_PM_DEVICE_RUNTIME`](kconfig.md#CONFIG_PM_DEVICE_RUNTIME "CONFIG_PM_DEVICE_RUNTIME")
    Kconfig option.

idle thread
:   A system thread that runs when there are no other threads ready to run.

IDT
:   (Interrupt Descriptor Table) a data structure used by the x86
    architecture to implement an interrupt vector table. The IDT is used
    to determine the correct response to interrupts and exceptions.

ISR
:   (Interrupt Service Routine) Also known as an interrupt handler, an ISR
    is a callback function whose execution is triggered by a hardware
    interrupt (or software interrupt instructions) and is used to handle
    high-priority conditions that require interrupting the current code
    executing on the processor.

kernel
:   The set of Zephyr-supplied files that implement the Zephyr kernel,
    including its core services, device drivers, network stack, and so on.

power domain
:   A power domain is a collection of devices for which power is
    applied and removed collectively in a single action. Power
    domains are represented by [`device`](kernel/drivers/index.md#c.device "device").

power gating
:   Power gating reduces power consumption by shutting off areas of an
    integrated circuit that are not in use.

SoC
:   A [System on a chip](https://en.wikipedia.org/wiki/System_on_a_chip), that is, an integrated circuit that contains at
    least one [CPU cluster](#term-CPU-cluster) (in turn with at least one [CPU core](#term-CPU-core)),
    as well as peripherals and memory.

SoC family
:   One or more [SoCs](#term-SoC) or [SoC series](#term-SoC-series) that share enough
    in common to consider them related and under a single family denomination.

SoC series
:   A number of different [SoCs](#term-SoC) that share similar characteristics and
    features, and that the vendor typically names and markets together.

subsystem
:   A subsystem refers to a logically distinct part of the operating system
    that handles specific functionality or provides certain services.

system power state
:   System power states describe the power consumption of the system as a
    whole. System power states are represented by [`pm_state`](services/pm/api/index.md#c.pm_state "pm_state").

variant
:   In the context of [board qualifiers](#term-board-qualifiers), a variant designates a
    particular type or configuration of a build for a combination of [SoC](#term-SoC)
    and [CPU cluster](#term-CPU-cluster). Common uses of the variant concept include
    introducing both secure and non-secure builds for platforms with Trusted
    Execution Environment support, or selecting the type of RAM used in a
    build.

west
:   A multi-repo meta-tool developed for the Zephyr project. See [West (Zephyr’s meta-tool)](develop/west/index.md#west).

west installation
:   An obsolete term for a [west workspace](#term-west-workspace) used prior to west 0.7.

west manifest
:   A YAML file, usually named `west.yml`, which describes projects, or
    the Git repositories which make up a [west workspace](#term-west-workspace), along with
    additional metadata. See [Basics](develop/west/basics.md#west-basics) for general information
    and [West Manifests](develop/west/manifest.md#west-manifests) for details.

west manifest repository
:   The Git repository in a [west workspace](#term-west-workspace) which contains the
    [west manifest](#term-west-manifest). Its location is given by the [manifest.path
    configuration option](develop/west/config.md#west-config-index). See [Basics](develop/west/basics.md#west-basics).

west project
:   Each of the entries in a [west manifest](#term-west-manifest), which describe a Git
    repository that will be cloned and managed by west when working with the
    corresponding [west manifest repository](#term-west-manifest-repository). Note that a west project
    is different from a [zephyr module](#term-zephyr-module), although many projects are also
    modules. See [Projects](develop/west/manifest.md#west-manifests-projects) for additional information.

west workspace
:   A folder on your system with a `.west` subdirectory and a
    [west manifest repository](#term-west-manifest-repository) in it. You clone the Zephyr source code,
    as well as that of its [west projects](#term-west-project) onto your
    system by creating a west workspace using the `west init` command. See
    [Basics](develop/west/basics.md#west-basics).

XIP
:   (eXecute In Place) a method of executing programs directly from long
    term storage rather than copying it into RAM, saving writable memory for
    dynamic data and not the static program code.

zephyr module
:   A Git repository containing a `zephyr/module.yml` file, used by the
    Zephyr build system to integrate the source code and configuration files
    of the module into a regular Zephyr build. Zephyr modules may be west
    projects, but they do not have to. See [Modules (External projects)](develop/modules.md#modules) for additional
    details.
