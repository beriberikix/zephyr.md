---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/mipi_dbi.html
original_path: hardware/peripherals/mipi_dbi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MIPI Display Bus Interface (DBI)

The MIPI DBI driver class implements support for MIPI DBI compliant display
controllers.

MIPI DBI defines 3 interface types:
\* Type A: Motorola 6800 parallel bus

- Type B: Intel 8080 parallel bus
- Type C: SPI Type serial bit bus with 3 options:

  1. 9 write clocks per byte, final bit is command/data selection bit
  2. Same as above, but 16 write clocks per byte
  3. 8 write clocks per byte. Command/data selected via GPIO pin

Currently, the API only supports Type C controllers, options 1 and 3.

## API Reference

*group* mipi\_dbi\_interface
:   MIPI-DBI driver APIs.

    Defines

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

    MIPI\_DBI\_SPI\_CONFIG\_DT(node\_id, operation\_, delay\_)
    :   initialize a MIPI DBI SPI configuration struct from devicetree

        This helper allows drivers to initialize a MIPI DBI SPI configuration structure using devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the MIPI DBI device whose struct [spi\_config](spi.md#structspi__config) to create an initializer for
            - **operation\_** – the desired operation field in the struct [spi\_config](spi.md#structspi__config)
            - **delay\_** – the desired delay field in the struct [spi\_config](spi.md#structspi__config)’s [spi\_cs\_control](spi.md#structspi__cs__control), if there is one

    Functions

    static inline int mipi\_dbi\_command\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [mipi\_dbi\_config](#c.mipi_dbi_config) \*config, uint8\_t cmd, const uint8\_t \*data, size\_t len)
    :   Write a command to the display controller.

        Writes a command, along with an optional data buffer to the display. If data buffer and buffer length are NULL and 0 respectively, then only a command will be sent.

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
