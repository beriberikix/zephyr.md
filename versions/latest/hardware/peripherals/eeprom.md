---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/eeprom.html
original_path: hardware/peripherals/eeprom.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Electrically Erasable Programmable Read-Only Memory (EEPROM)

## Overview

The EEPROM API provides read and write access to Electrically Erasable
Programmable Read-Only Memory (EEPROM) devices.

EEPROMs have an erase block size of 1 byte, a long lifetime, and allow
overwriting data on byte-by-byte access.

## Configuration Options

Related configuration options:

- [`CONFIG_EEPROM`](../../kconfig.md#CONFIG_EEPROM "CONFIG_EEPROM")

## API Reference

Related code samples

[EEPROM](../../samples/drivers/eeprom/README.md#eeprom "Store a boot count value in EEPROM.")
:   Store a boot count value in EEPROM.

*group* eeprom\_interface
:   EEPROM Interface.

    Functions

    int eeprom\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, void \*data, size\_t len)
    :   Read data from EEPROM.

        Parameters:
        :   - **dev** – EEPROM device
            - **offset** – Address offset to read from.
            - **data** – Buffer to store read data.
            - **len** – Number of bytes to read.

        Returns:
        :   0 on success, negative errno code on failure.

    int eeprom\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, const void \*data, size\_t len)
    :   Write data to EEPROM.

        Parameters:
        :   - **dev** – EEPROM device
            - **offset** – Address offset to write data to.
            - **data** – Buffer with data to write.
            - **len** – Number of bytes to write.

        Returns:
        :   0 on success, negative errno code on failure.

    size\_t eeprom\_get\_size(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the size of the EEPROM in bytes.

        Parameters:
        :   - **dev** – EEPROM device.

        Returns:
        :   EEPROM size in bytes.
