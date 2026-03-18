---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/basic/minimal/README.html
original_path: samples/basic/minimal/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Minimal footprint

## Overview

This sample provides an empty `main()` and various configuration files that
can be used to measure Zephyr’s minimal ROM footprint in different
configurations.

The following configuration files are available:

- `mt.conf`: Enable multithreading
- `no-mt.conf`: Disable multithreading
- `no-preempt.conf`: Disable preemption
- `no-timers.conf`: Disable timers
- `arm.conf`: Arm-specific disabling of features

## Building and measuring ROM size

The following combinations are suggested for comparing ROM sizes in different
configurations. They all target the [reel board](../../../boards/arm/reel_board/doc/index.md#reel-board) (Arm Aarch32 architecture).

- Multithreading enabled

  - Reference ROM size: 7-8KB

  ```shell
  west build -b reel_board -d build/reel_board/mt samples/basic/minimal -- -DCONF_FILE="common.conf mt.conf arm.conf"
  west build -t rom_report -d build/reel_board/mt
  ```
- Multithreading enabled, no preemption

  - Reference ROM size: 7-8KB

  ```shell
  west build -b reel_board -d build/reel_board/mt-no-preempt samples/basic/minimal -- -DCONF_FILE="common.conf mt.conf no-preempt.conf arm.conf"
  west build -t rom_report -d build/reel_board/mt-no-preempt
  ```
- Multithreading enabled, no preemption, timers disabled

  - Reference ROM size: 3-4KB

  ```shell
  west build -b reel_board -d build/reel_board/mt-no-preempt-no-timers samples/basic/minimal -- -DCONF_FILE="common.conf mt.conf no-preempt.conf no-timers.conf arm.conf"
  west build -t rom_report -d build/reel_board/mt-no-preempt-no-timers
  ```
- Multithreading disabled, timers enabled

  - Reference ROM size: 4-5KB

  ```shell
  west build -b reel_board -d build/reel_board/no-mt samples/basic/minimal -- -DCONF_FILE="common.conf no-mt.conf arm.conf"
  west build -t rom_report -d build/reel_board/no-mt
  ```
- Multithreading disabled, timers disabled

  - Reference ROM size: 2-3KB

  ```shell
  west build -b reel_board -d build/reel_board/no-mt-no-timers samples/basic/minimal -- -DCONF_FILE="common.conf no-mt.conf no-timers.conf arm.conf"
  west build -t rom_report -d build/reel_board/no-mt-no-timers
  ```
