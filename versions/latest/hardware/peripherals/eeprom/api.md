---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/eeprom/api.html
original_path: hardware/peripherals/eeprom/api.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# EEPROM API

## Overview

The EEPROM API provides read and write access to Electrically Erasable
Programmable Read-Only Memory (EEPROM) devices.

## Configuration Options

Related configuration options:

- [`CONFIG_EEPROM`](../../../kconfig.md#CONFIG_EEPROM "CONFIG_EEPROM")

## API Reference

Related code samples

[EEPROM](../../../samples/drivers/eeprom/README.md#eeprom "Store a boot count value in EEPROM.")
:   Store a boot count value in EEPROM.

*group* EEPROM Interface
:   EEPROM Interface.

    **Since**
    :   2.1

    **Version**
    :   1.0.0

    Functions

    int eeprom\_read(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, void \*data, size\_t len)
    :   Read data from EEPROM.

        Parameters:
        :   - **dev** – EEPROM device
            - **offset** – Address offset to read from.
            - **data** – Buffer to store read data.
            - **len** – Number of bytes to read.

        Returns:
        :   0 on success, negative errno code on failure.

    int eeprom\_write(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, off\_t offset, const void \*data, size\_t len)
    :   Write data to EEPROM.

        Parameters:
        :   - **dev** – EEPROM device
            - **offset** – Address offset to write data to.
            - **data** – Buffer with data to write.
            - **len** – Number of bytes to write.

        Returns:
        :   0 on success, negative errno code on failure.

    size\_t eeprom\_get\_size(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the size of the EEPROM in bytes.

        Parameters:
        :   - **dev** – EEPROM device.

        Returns:
        :   EEPROM size in bytes.
