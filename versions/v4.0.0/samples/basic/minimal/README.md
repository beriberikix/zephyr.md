---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/basic/minimal/README.html
original_path: samples/basic/minimal/README.html
---

# Minimal footprint

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/minimal/README.rst/..)

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
configurations. They all target the [reel board](../../../boards/phytec/reel_board/doc/index.md#reel-board) (Arm Aarch32 architecture).

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
