---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/kscan.html
original_path: hardware/peripherals/kscan.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Keyboard Scan

## Overview

The kscan driver (keyboard scan matrix) is used for detecting a key press in a
connected matrix keyboard or any device with buttons such as joysticks.
Typically, matrix keyboards are implemented using a two-dimensional
configuration in order to sense several keys. This allows interfacing to
many keys through fewer physical pins. Keyboard matrix
drivers read the rows while applying power through the columns one at a time
with the purpose of detecting key events.
There is no correlation between the physical and electrical layout of keys.
For, example, the physical layout may be one array of 16 or fewer keys, which
may be electrically connected to a 4 x 4 array. In addition, key values are
defined by a keymap provided by the keyboard manufacturer.

## Configuration Options

Related configuration options:

- [`CONFIG_KSCAN`](../../kconfig.md#CONFIG_KSCAN "CONFIG_KSCAN")

## API Reference

Related code samples

[HT16K33 LED driver with keyscan](../../samples/drivers/ht16k33/README.md#ht16k33 "Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.")
:   Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.

[KSCAN](../../samples/drivers/kscan/README.md#kscan "Use the KSCAN API to read key presses and releases on a keyboard matrix.")
:   Use the KSCAN API to read key presses and releases on a keyboard matrix.

*group* kscan\_interface
:   KSCAN APIs.

    Typedefs

    typedef void (\*kscan\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t row, uint32\_t column, bool pressed)
    :   Keyboard scan callback called when user press/release a key on a matrix keyboard.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param row:
        :   Describes row change.

        Param column:
        :   Describes column change.

        Param pressed:
        :   Describes the kind of key event.

    Functions

    int kscan\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [kscan\_callback\_t](#c.kscan_callback_t) callback)
    :   Configure a Keyboard scan instance.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – called when keyboard devices reply to to a keyboard event such as key pressed/released.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int kscan\_enable\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enables callback.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.

    int kscan\_disable\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disables callback.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful.
            - **Negative** – errno code if failure.
