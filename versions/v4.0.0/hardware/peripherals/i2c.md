---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/peripherals/i2c.html
original_path: hardware/peripherals/i2c.html
---

# Inter-Integrated Circuit (I2C) Bus

## Overview

Note

The terminology used in Zephyr I2C APIs follows that of the
[NXP I2C Bus Specification Rev 7.0](https://www.nxp.com/docs/en/user-guide/UM10204.pdf). These changed
from previous revisions as of its release October 1, 2021.

[I2C](https://www.nxp.com/docs/en/user-guide/UM10204.pdf) (Inter-Integrated Circuit, pronounced “eye
squared see”) is a commonly-used two-signal shared peripheral interface
bus. Many system-on-chip solutions provide controllers that communicate
on an I2C bus. Devices on the bus can operate in two roles: as a
“controller” that initiates transactions and controls the clock, or as a
“target” that responds to transaction commands. A I2C controller on a
given SoC will generally support the controller role, and some will also
support the target mode. Zephyr has API for both roles.

### I2C Controller API

Zephyr’s I2C controller API is used when an I2C peripheral controls the bus,
particularly the start and stop conditions and the clock. This is
the most common mode, used to interact with I2C devices like sensors and
serial memory.

This API is supported in all in-tree I2C peripheral drivers and is
considered stable.

### I2C Target API

Zephyr’s I2C target API is used when an I2C peripheral responds to
transactions initiated by a different controller on the bus. It might
be used for a Zephyr application with transducer roles that are
controlled by another device such as a host processor.

This API is supported in very few in-tree I2C peripheral drivers. The
API is considered experimental, as it is not compatible with the
capabilities of all I2C peripherals supported in controller mode.

## Configuration Options

Related configuration options:

- [`CONFIG_I2C`](../../kconfig.md#CONFIG_I2C "CONFIG_I2C")

## API Reference

[I2C Interface](../../doxygen/html/group__i2c__interface.md)

Related code samples

- [I2C Custom Target](../../samples/drivers/i2c/custom_target/README.md#i2c-custom-target "Setup a custom I2C target on the I2C interface.")Setup a custom I2C target on the I2C interface.
- [I2C Target](../../samples/drivers/i2c/target_eeprom/README.md#i2c-eeprom-target "Setup an I2C target on the I2C interface.")Setup an I2C target on the I2C interface.
- [I2C V2 timings](../../samples/boards/st/i2c_timing/README.md#stm32_i2c_v2_timings "Retrieve I2C V2 timings at runtime.")Retrieve I2C V2 timings at runtime.
