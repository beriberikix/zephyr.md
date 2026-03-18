---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/ps2.html
original_path: hardware/peripherals/ps2.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# PS/2

## Overview

The PS/2 connector first hit the market in 1987 on
IBM’s desktop PC line of the same name before
becoming an industry-wide standard for mouse and
keyboard connections. Starting around 2007, USB
superseded PS/2 and is the modern peripheral device
connection standard. For legacy support on boards
with a PS/2 connector, Zephyr provides these PS/2 driver APIs.

## Configuration Options

Related configuration options:

- [`CONFIG_PS2`](../../kconfig.md#CONFIG_PS2 "CONFIG_PS2")

## API Reference

Related code samples

[PS/2 interface](../../samples/drivers/ps2/README.md#ps2 "Communicate with a PS/2 mouse.")
:   Communicate with a PS/2 mouse.

*group* PS/2 Driver APIs
:   PS/2 Driver APIs.

    Typedefs

    typedef void (\*ps2\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t data)
    :   PS/2 callback called when user types or click a mouse.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param data:
        :   Data byte passed pack to the user.

    Functions

    int ps2\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [ps2\_callback\_t](#c.ps2_callback_t) callback\_isr)
    :   Configure a ps2 instance.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback\_isr** – called when PS/2 devices reply to a configuration command or when a mouse/keyboard send data to the client application.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int ps2\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t value)
    :   Write to PS/2 device.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **value** – Data for the PS2 device.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int ps2\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*value)
    :   Read slave-to-host values from PS/2 device.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **value** – Pointer used for reading the PS/2 device.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int ps2\_enable\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enables callback.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int ps2\_disable\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disables callback.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.
