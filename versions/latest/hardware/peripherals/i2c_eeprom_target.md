---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/i2c_eeprom_target.html
original_path: hardware/peripherals/i2c_eeprom_target.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# I2C EEPROM Target

## Overview

## API Reference

*group* i2c\_eeprom\_target\_api
:   I2C EEPROM Target Driver API.

    Functions

    int eeprom\_target\_program(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*eeprom\_data, unsigned int length)
    :   Program memory of the virtual EEPROM.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **eeprom\_data** – Pointer of data to program into the virtual eeprom memory
            - **length** – Length of data to program into the virtual eeprom memory

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – Invalid data size

    int eeprom\_target\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*eeprom\_data, unsigned int offset)
    :   Read single byte of virtual EEPROM memory.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **eeprom\_data** – Pointer of byte where to store the virtual eeprom memory
            - **offset** – Offset into EEPROM memory where to read the byte

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – Invalid data pointer or offset

    int eeprom\_target\_set\_addr(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t addr)
    :   Change the address of eeprom taget at runtime.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **addr** – New address to assign to the eeprom target devide

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid
            - **-EIO** – General input / output error during i2c\_taget\_register
            - **-ENOSYS** – If target mode is not implemented
