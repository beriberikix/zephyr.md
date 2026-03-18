---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/mipi_dbi.html
original_path: hardware/peripherals/mipi_dbi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# MIPI Display Bus Interface (DBI)

The MIPI DBI driver class implements support for MIPI DBI compliant display
controllers.

MIPI DBI defines 3 interface types:

- Type A: Motorola 6800 parallel bus
- Type B: Intel 8080 parallel bus
- Type C: SPI Type serial bit bus with 3 options:

  1. 9 write clocks per byte, final bit is command/data selection bit
  2. Same as above, but 16 write clocks per byte
  3. 8 write clocks per byte. Command/data selected via GPIO pin

Currently, the API only supports Type C controllers, options 1 and 3.

## API Reference

*group* MIPI-DBI driver APIs
:   MIPI-DBI driver APIs.

    **Since**
    :   3.6

    **Version**
    :   0.1.0

    Defines

    MIPI\_DBI\_SPI\_CONFIG\_DT(node\_id, operation\_, delay\_)
    :   initialize a MIPI DBI SPI configuration struct from devicetree

        This helper allows drivers to initialize a MIPI DBI SPI configuration structure using devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the MIPI DBI device whose struct [spi\_config](spi.md#structspi__config) to create an initializer for
            - **operation\_** – the desired operation field in the struct [spi\_config](spi.md#structspi__config)
            - **delay\_** – the desired delay field in the struct [spi\_config](spi.md#structspi__config)’s [spi\_cs\_control](spi.md#structspi__cs__control), if there is one

    MIPI\_DBI\_SPI\_CONFIG\_DT\_INST(inst, operation\_, delay\_)
    :   Initialize a MIPI DBI SPI configuration from devicetree instance.

        This helper initializes a MIPI DBI SPI configuration from a devicetree instance. It is equivalent to [MIPI\_DBI\_SPI\_CONFIG\_DT(DT\_DRV\_INST(inst))](#group__mipi__dbi__interface_1ga9e05938ce1cd2b647cb00a77b773ad1d)

        Parameters:
        :   - **inst** – Instance number to initialize configuration from
            - **operation\_** – the desired operation field in the struct [spi\_config](spi.md#structspi__config)
            - **delay\_** – the desired delay field in the struct [spi\_config](spi.md#structspi__config)’s [spi\_cs\_control](spi.md#structspi__cs__control), if there is one

    MIPI\_DBI\_CONFIG\_DT(node\_id, operation\_, delay\_)
    :   Initialize a MIPI DBI configuration from devicetree.

        This helper allows drivers to initialize a MIPI DBI configuration structure from devicetree. It sets the MIPI DBI mode, as well as configuration fields in the SPI configuration structure

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the MIPI DBI device to initialize
            - **operation\_** – the desired operation field in the struct [spi\_config](spi.md#structspi__config)
            - **delay\_** – the desired delay field in the struct [spi\_config](spi.md#structspi__config)’s [spi\_cs\_control](spi.md#structspi__cs__control), if there is one

    MIPI\_DBI\_CONFIG\_DT\_INST(inst, operation\_, delay\_)
    :   Initialize a MIPI DBI configuration from device instance.

        Equivalent to [MIPI\_DBI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)](#group__mipi__dbi__interface_1ga94aed5adf0dc393556b2c8c9976aeddf)

        Parameters:
        :   - **inst** – Instance of the device to initialize a MIPI DBI configuration for
            - **operation\_** – the desired operation field in the struct [spi\_config](spi.md#structspi__config)
            - **delay\_** – the desired delay field in the struct [spi\_config](spi.md#structspi__config)’s [spi\_cs\_control](spi.md#structspi__cs__control), if there is one

    MIPI\_DBI\_MODE\_SPI\_3WIRE
    :   SPI 3 wire (Type C1).

        Uses 9 write clocks to send a byte of data. The bit sent on the 9th clock indicates whether the byte is a command or data byte

        ```text
              .---.   .---.   .---.   .---.   .---.   .---.   .---.   .---.
        SCK  -'   '---'   '---'   '---'   '---'   '---'   '---'   '---'   '---

             -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.
        DOUT  |D/C| D7| D6| D5| D4| D3| D2| D1| D0|D/C| D7| D6| D5| D4|...|
             -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'
              | Word 1                            | Word n

             -.                                                              .--
        CS    '-----------------------------------------------------------'
        ```

    MIPI\_DBI\_MODE\_SPI\_4WIRE
    :   SPI 4 wire (Type C3).

        Uses 8 write clocks to send a byte of data. an additional C/D pin will be use to indicate whether the byte is a command or data byte

        ```text
              .---.   .---.   .---.   .---.   .---.   .---.   .---.   .---.
        SCK  -'   '---'   '---'   '---'   '---'   '---'   '---'   '---'   '---

             -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.
        DOUT  | D7| D6| D5| D4| D3| D2| D1| D0| D7| D6| D5| D4| D3| D2| D1| D0|
             -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'
              | Word 1                        | Word n

             -.                                                                  .--
        CS    '---------------------------------------------------------------'

             -.-------------------------------.-------------------------------.-
        CD    |             D/C               |             D/C               |
             -'-------------------------------'-------------------------------'-
        ```

    MIPI\_DBI\_MODE\_6800\_BUS\_16\_BIT
    :   Parallel Bus protocol for MIPI DBI Type A based on Motorola 6800 bus.

        ```text
                 -.   .--------.      .------------------------
        CS        '---'        '---'

                 -------------------------------------------
        RESX

                      .--------------------------------
        D/CX     ----------'

        R/WX     -------------------------------------------

                 -------------------------------------------
        E

                  .--------.   .--------------------------.
        D[15:0]/ -| COMMAND|---|  DATA                    |
        D[8:0]/   '--------'   '--------------------------'
        D[7:0]
        ```

        Please refer to the MIPI DBI specification for a detailed cycle diagram.

    MIPI\_DBI\_MODE\_6800\_BUS\_9\_BIT

    MIPI\_DBI\_MODE\_6800\_BUS\_8\_BIT

    MIPI\_DBI\_MODE\_8080\_BUS\_16\_BIT
    :   Parallel Bus protocol for MIPI DBI Type B based on Intel 8080 bus.

        ```text
                 -.                                  .-
        CS        '---------------------------------------'

                 -------------------------------------------
        RESX

                 --.              .----------------------------
        D/CX       '-----------'

                 ---.   .--------.   .----------------------
        WRX         '---'   '---'

                 -------------------------------------------
        RDX

                    .--------.   .--------------------------.
        D[15:0]/ ---| COMMAND|---|  DATA                    |
        D[8:0]/     '--------'   '--------------------------'
        D[7:0]
        ```

        Please refer to the MIPI DBI specification for a detailed cycle diagram.

    MIPI\_DBI\_MODE\_8080\_BUS\_9\_BIT

    MIPI\_DBI\_MODE\_8080\_BUS\_8\_BIT

    Functions

    static inline int mipi\_dbi\_command\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [mipi\_dbi\_config](#c.mipi_dbi_config) \*config, uint8\_t cmd, const uint8\_t \*data, size\_t len)
    :   Write a command to the display controller.

        Writes a command, along with an optional data buffer to the display. If data buffer and buffer length are NULL and 0 respectively, then only a command will be sent. Note that if the SPI configuration passed to this function locks the SPI bus, it is the caller’s responsibility to release it with [mipi\_dbi\_release()](#group__mipi__dbi__interface_1gade0b635bcd4f16fb3ec5d122d1b09161)

        Parameters:
        :   - **dev** – mipi dbi controller
            - **config** – MIPI DBI configuration
            - **cmd** – command to write to display controller
            - **data** – optional data buffer to write after command
            - **len** – size of data buffer in bytes. Set to 0 to skip sending data.

        Return values:
        :   - **0** – command write succeeded
            - **-EIO** – I/O error
            - **-ETIMEDOUT** – transfer timed out
            - **-EBUSY** – controller is busy
            - **-ENOSYS** – not implemented

    static inline int mipi\_dbi\_command\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [mipi\_dbi\_config](#c.mipi_dbi_config) \*config, uint8\_t \*cmds, size\_t num\_cmd, uint8\_t \*response, size\_t len)
    :   Read a command response from the display controller.

        Reads a command response from the display controller.

        Parameters:
        :   - **dev** – mipi dbi controller
            - **config** – MIPI DBI configuration
            - **cmds** – array of one byte commands to send to display controller
            - **num\_cmd** – number of commands to write to display controller
            - **response** – response buffer, filled with display controller response
            - **len** – size of response buffer in bytes.

        Return values:
        :   - **0** – command read succeeded
            - **-EIO** – I/O error
            - **-ETIMEDOUT** – transfer timed out
            - **-EBUSY** – controller is busy
            - **-ENOSYS** – not implemented

    static inline int mipi\_dbi\_write\_display(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [mipi\_dbi\_config](#c.mipi_dbi_config) \*config, const uint8\_t \*framebuf, struct [display\_buffer\_descriptor](display/index.md#c.display_buffer_descriptor "display_buffer_descriptor") \*desc, enum [display\_pixel\_format](display/index.md#c.display_pixel_format "display_pixel_format") pixfmt)
    :   Write a display buffer to the display controller.

        Writes a display buffer to the controller. If the controller requires a “Write memory” command before writing display data, this should be sent with [mipi\_dbi\_command\_write](#group__mipi__dbi__interface_1gad36e3d57fd931236c4ed4e58dfef1cca)

        Parameters:
        :   - **dev** – mipi dbi controller
            - **config** – MIPI DBI configuration
            - **framebuf** – framebuffer to write to display
            - **desc** – descriptor of framebuffer to write. Note that the pitch must be equal to width. “buf\_size” field determines how many bytes will be written.
            - **pixfmt** – pixel format of framebuffer data

        Return values:
        :   - **0** – buffer write succeeded.
            - **-EIO** – I/O error
            - **-ETIMEDOUT** – transfer timed out
            - **-EBUSY** – controller is busy
            - **-ENOSYS** – not implemented

    static inline int mipi\_dbi\_reset(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t delay)
    :   Resets attached display controller.

        Resets the attached display controller.

        Parameters:
        :   - **dev** – mipi dbi controller
            - **delay** – duration to set reset signal for, in milliseconds

        Return values:
        :   - **0** – reset succeeded
            - **-EIO** – I/O error
            - **-ENOSYS** – not implemented
            - **-ENOTSUP** – not supported

    static inline int mipi\_dbi\_release(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [mipi\_dbi\_config](#c.mipi_dbi_config) \*config)
    :   Releases a locked MIPI DBI device.

        Releases a lock on a MIPI DBI device and/or the device’s CS line if and only if the given config parameter was the last one to be used in any of the above functions, and if it has the SPI\_LOCK\_ON bit set and/or the SPI\_HOLD\_ON\_CS bit set into its operation bits field. This lock functions exactly like the SPI lock, and can be used if the caller needs to keep CS asserted for multiple transactions, or the MIPI DBI device locked.

        Parameters:
        :   - **dev** – mipi dbi controller
            - **config** – MIPI DBI configuration

        Return values:
        :   - **0** – reset succeeded
            - **-EIO** – I/O error
            - **-ENOSYS** – not implemented
            - **-ENOTSUP** – not supported

    struct mipi\_dbi\_config
    :   *#include <mipi\_dbi.h>*

        MIPI DBI controller configuration.

        Configuration for MIPI DBI controller write

        Public Members

        uint8\_t mode
        :   MIPI DBI mode (SPI 3 wire or 4 wire).

        struct [spi\_config](spi.md#c.spi_config "spi_config") config
        :   SPI configuration.

    struct mipi\_dbi\_driver\_api
    :   *#include <mipi\_dbi.h>*

        MIPI-DBI host driver API.
