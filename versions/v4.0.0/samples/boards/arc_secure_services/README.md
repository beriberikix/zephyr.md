---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/boards/arc_secure_services/README.html
original_path: samples/boards/arc_secure_services/README.html
---

# ARC Secure Service

## Overview

This sample implements a simple secure service based on ARC SecureShield to
demonstrate how a secure zephyr application runs together with a normal
Zephyr application.

In this sample:

- Secure application will be in the secure memory space defined in
  `arc_mpu_regions.c`. Half of RAM and ROM is allocated to secure world,
  the other half is allocated to normal world.
- Memory not allocated to the secure application is allocated to
  the normal application.
- By default, all the peripheral space is normal mode accessible, i.e.,
  the peripherals are shared between normal mode and secure mode. If some
  peripherals are required by secure world, it can be done by adding static
  mpu entry in `arc_mpu_regions.c`.
- The interrupts of two internal timers are configure as normal interrupts,
  so the normal zephyr’s kernel tick can work correctly.
- Secure interrupts priority > secure threads priority > normal interrupts
  priority > normal threads priority.

## Requirements

To use this sample, ARC processor should be equipped with ARC SecureShield. In
Zephyr, the following board configurations are supported:

- em\_starterkit\_em7d
  \* secure application: em\_starterkit\_em7d\_secure
  \* normal application: em\_starterkit\_em7d\_normal
- nsim\_sem
  \* secure application: nsim\_sem
  \* normal application: nsim\_sem\_normal

## Building and Running

### Building

#### Secure application

First, you should build the secure application.

```shell
west build -b em_starterkit_em7d_secure nsim_sem samples/boards/arc_secure_services
```

#### Normal application

Currently, in normal application, MPU is not accessible, so no user space and
mpu-based stack checking. Please copy the specific dts file and def\_config
file to the specific board dir to build normal application.

Here,take [Dining Philosophers](../../philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.") as an example for normal
application.

```shell
west build -b em_starterkit_em7d_normal nsim_sem_normal samples/philosophers
```

### Running

- Run using the bootloader

The bootloader should load the secure and normal application into the correct place,
then jump to the entry of the secure application. The entry of normal application
is hardcoded in secure application. Secure application will boot normal application.

- Run using the debugger (recommended)

Use the gdb debugger to load and run the two applications.

For em starter kit, run the following commands

```shell
# load secure application first
$ cd samples/boards/arc_secure_services/build
$ west debug
# load normal application
$ monitor load_image ../../../philosophers/build/zephyr/zephyr.elf
$ c
```

For nsim sem, you need two consoles: one for application output, and one for
debugger.

In the console for output:

```shell
# open debug server
$ cd samples/boards/arc_secure_services/build
$ west debugserver
```

In the console for debugger:

```shell
# open debug server
$ cd samples/boards/arc_secure_services/build
$ arc-elf32-gdb zephyr/zephyr.elf
$ target remote :3333
# load normal application
$ load ../../../philosophers/build/zephyr/zephyr.elf
# load secure application
$ load
$ c
```
