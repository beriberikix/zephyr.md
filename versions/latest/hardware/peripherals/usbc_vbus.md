---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/usbc_vbus.html
original_path: hardware/peripherals/usbc_vbus.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# USB-C VBUS

## Overview

USB-C VBUS is the line in a USB Type-C connection that delivers power from a
Source to a Sink device.

### USB-C VBUS API

The USB-C VBUS device driver presents an API that’s used to control and measure
VBUS.

## Configuration Options

Related configuration options:

- [`CONFIG_USBC_VBUS_DRIVER`](../../kconfig.md#CONFIG_USBC_VBUS_DRIVER "CONFIG_USBC_VBUS_DRIVER")

## API Reference

*group* usbc\_vbus\_api
:   USB-C VBUS API.

    Functions

    static inline bool usbc\_vbus\_check\_level(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [tc\_vbus\_level](tcpc.md#c.tc_vbus_level "tc_vbus_level") level)
    :   Checks if VBUS is at a particular level.

        Parameters:
        :   - **dev** – Runtime device structure
            - **level** – The level voltage to check against

        Return values:
        :   - **true** – if VBUS is at the level voltage
            - **false** – if VBUS is not at that level voltage

    static inline int usbc\_vbus\_measure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int \*meas)
    :   Reads and returns VBUS measured in mV.

        Parameters:
        :   - **dev** – Runtime device structure
            - **meas** – pointer where the measured VBUS voltage is stored

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure

    static inline int usbc\_vbus\_discharge(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Controls a pin that discharges VBUS.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – Discharge VBUS when true

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOENT** – if discharge pin isn’t defined

    static inline int usbc\_vbus\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Controls a pin that enables VBUS measurments.

        Parameters:
        :   - **dev** – Runtime device structure
            - **enable** – enable VBUS measurments when true

        Return values:
        :   - **0** – on success
            - **-EIO** – on failure
            - **-ENOENT** – if enable pin isn’t defined

    struct usbc\_vbus\_driver\_api
    :   *#include <usbc\_vbus.h>*
