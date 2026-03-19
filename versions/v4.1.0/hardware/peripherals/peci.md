---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/peci.html
original_path: hardware/peripherals/peci.html
---

# Platform Environment Control Interface (PECI)

## Overview

The Platform Environment Control Interface, abbreviated as PECI,
is a thermal management standard introduced in 2006
with the Intel Core 2 Duo Microprocessors.
The PECI interface allows external devices to read processor temperature,
perform processor manageability functions, and manage processor interface
tuning and diagnostics.
The PECI bus driver APIs enable the interaction between Embedded
Microcontrollers and CPUs.

## Configuration Options

Related configuration options:

- [`CONFIG_PECI`](../../kconfig.md#CONFIG_PECI "CONFIG_PECI")

## API Reference

[PECI Interface](../../doxygen/html/group__peci__interface.md)

Related code samples

- [PECI interface](../../samples/drivers/peci/README.md#peci "Monitor CPU temperature using PECI.")Monitor CPU temperature using PECI.
