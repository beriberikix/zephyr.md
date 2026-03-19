---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/arch/xtensa.html
original_path: hardware/arch/xtensa.html
---

# Xtensa Developer Guide

## Overview

This page contains information on certain aspects when developing for
Xtensa-based platforms.

## HiFi Audio Engine DSP

The kernel allows threads to use the HiFi Audio Engine DSP registers on boards
that support these registers. The kernel only supports the use of the HiFi
registers by threads and not ISRs.

Note

Presently, only the Intel ADSP ACE hardware platforms are configured for
HiFi support by default.

### Concepts

The kernel can be configured for an application to leverage the services
provided by the Xtensa HiFi Audio Engine DSP. Three modes of operation are
supported, which are described below.

#### No HiFi registers mode

This mode is used when the application has no threads that use the HiFi
registers. It is the kernel’s default HiFi services mode.

#### Unshared HiFi registers mode

This mode is used when the application has only a single thread that uses the
HiFi registers. The HiFi registers are left unchanged whenever a context
switch occurs.

Note

The behavior is undefined, if two or more threads attempt to use
the HiFi registers, as the kernel does not attempt to detect
(nor prevent) multiple threads from using these registers.

#### Shared HiFi registers mode

This mode is used when the application has two or more threads that use HiFi
registers. When enabled, the kernel automatically allows all threads to use the
HiFi registers. During each thread context switch, the kernel saves the outgoing
thread’s HiFi registers and loads the incoming thread’s HiFi registers,
regardless of whether the thread utilizes them or not.

Additional stack space may be required for each thread to account for the extra
registers that must be saved.

### Configuration Options

The unshared HiFi registers mode is selected when configuration option
[`CONFIG_XTENSA_HIFI_SHARING`](../../kconfig.md#CONFIG_XTENSA_HIFI_SHARING "CONFIG_XTENSA_HIFI_SHARING") is disabled but configuration
options [`CONFIG_XTENSA_HIFI3`](../../kconfig.md#CONFIG_XTENSA_HIFI3 "CONFIG_XTENSA_HIFI3") and/or
[`CONFIG_XTENSA_HIFI4`](../../kconfig.md#CONFIG_XTENSA_HIFI4 "CONFIG_XTENSA_HIFI4") are enabled.

The shared HiFi registers mode is selected when the configuration option
[`CONFIG_XTENSA_HIFI_SHARING`](../../kconfig.md#CONFIG_XTENSA_HIFI_SHARING "CONFIG_XTENSA_HIFI_SHARING") is enabled in addition to
configuration options [`CONFIG_XTENSA_HIFI3`](../../kconfig.md#CONFIG_XTENSA_HIFI3 "CONFIG_XTENSA_HIFI3") and/or
[`CONFIG_XTENSA_HIFI4`](../../kconfig.md#CONFIG_XTENSA_HIFI4 "CONFIG_XTENSA_HIFI4"). Threads must have sufficient
stack space for saving the HiFi register values during context switches
as described above.
