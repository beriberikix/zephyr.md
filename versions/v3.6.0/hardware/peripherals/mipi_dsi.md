---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/mipi_dsi.html
original_path: hardware/peripherals/mipi_dsi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MIPI Display Serial Interface (DSI)

## API Reference

*group* mipi\_dsi\_interface
:   MIPI-DSI driver APIs.

    MIPI-DSI Device mode flags.

    MIPI\_DSI\_MODE\_VIDEO
    :   Video mode.

    MIPI\_DSI\_MODE\_VIDEO\_BURST
    :   Video burst mode.

    MIPI\_DSI\_MODE\_VIDEO\_SYNC\_PULSE
    :   Video pulse mode.

    MIPI\_DSI\_MODE\_VIDEO\_AUTO\_VERT
    :   Enable auto vertical count mode.

    MIPI\_DSI\_MODE\_VIDEO\_HSE
    :   Enable hsync-end packets in vsync-pulse and v-porch area.

    MIPI\_DSI\_MODE\_VIDEO\_HFP
    :   Disable hfront-porch area.

    MIPI\_DSI\_MODE\_VIDEO\_HBP
    :   Disable hback-porch area.

    MIPI\_DSI\_MODE\_VIDEO\_HSA
    :   Disable hsync-active area.

    MIPI\_DSI\_MODE\_VSYNC\_FLUSH
    :   Flush display FIFO on vsync pulse.

    MIPI\_DSI\_MODE\_EOT\_PACKET
    :   Disable EoT packets in HS mode.

    MIPI\_DSI\_CLOCK\_NON\_CONTINUOUS
    :   Device supports non-continuous clock behavior (DSI spec 5.6.1).

    MIPI\_DSI\_MODE\_LPM
    :   Transmit data in low power.

    MIPI-DSI Pixel formats.

    MIPI\_DSI\_PIXFMT\_RGB888
    :   RGB888 (24bpp).

    MIPI\_DSI\_PIXFMT\_RGB666
    :   RGB666 (24bpp).

    MIPI\_DSI\_PIXFMT\_RGB666\_PACKED
    :   Packed RGB666 (18bpp).

    MIPI\_DSI\_PIXFMT\_RGB565
    :   RGB565 (16bpp).

    Defines

    MIPI\_DSI\_MSG\_USE\_LPM

    Functions

    static inline int mipi\_dsi\_attach(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, const struct [mipi\_dsi\_device](#c.mipi_dsi_device) \*mdev)
    :   Attach a new device to the MIPI-DSI bus.

        Parameters:
        :   - **dev** – MIPI-DSI host device.
            - **channel** – Device channel (VID).
            - **mdev** – MIPI-DSI device description.

        Returns:
        :   0 on success, negative on error

    static inline ssize\_t mipi\_dsi\_transfer(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, struct [mipi\_dsi\_msg](#c.mipi_dsi_msg) \*msg)
    :   Transfer data to/from a device attached to the MIPI-DSI bus.

        Parameters:
        :   - **dev** – MIPI-DSI device.
            - **channel** – Device channel (VID).
            - **msg** – Message.

        Returns:
        :   Size of the transferred data on success, negative on error.

    ssize\_t mipi\_dsi\_generic\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, const void \*params, size\_t nparams, void \*buf, size\_t len)
    :   MIPI-DSI generic read.

        Parameters:
        :   - **dev** – MIPI-DSI host device.
            - **channel** – Device channel (VID).
            - **params** – Buffer containing request parameters.
            - **nparams** – Number of parameters.
            - **buf** – Buffer where read data will be stored.
            - **len** – Length of the reception buffer.

        Returns:
        :   Size of the read data on success, negative on error.

    ssize\_t mipi\_dsi\_generic\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, const void \*buf, size\_t len)
    :   MIPI-DSI generic write.

        Parameters:
        :   - **dev** – MIPI-DSI host device.
            - **channel** – Device channel (VID).
            - **buf** – Transmission buffer.
            - **len** – Length of the transmission buffer

        Returns:
        :   Size of the written data on success, negative on error.

    ssize\_t mipi\_dsi\_dcs\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, uint8\_t cmd, void \*buf, size\_t len)
    :   MIPI-DSI DCS read.

        Parameters:
        :   - **dev** – MIPI-DSI host device.
            - **channel** – Device channel (VID).
            - **cmd** – DCS command.
            - **buf** – Buffer where read data will be stored.
            - **len** – Length of the reception buffer.

        Returns:
        :   Size of the read data on success, negative on error.

    ssize\_t mipi\_dsi\_dcs\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, uint8\_t cmd, const void \*buf, size\_t len)
    :   MIPI-DSI DCS write.

        Parameters:
        :   - **dev** – MIPI-DSI host device.
            - **channel** – Device channel (VID).
            - **cmd** – DCS command.
            - **buf** – Transmission buffer.
            - **len** – Length of the transmission buffer

        Returns:
        :   Size of the written data on success, negative on error.

    static inline int mipi\_dsi\_detach(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, const struct [mipi\_dsi\_device](#c.mipi_dsi_device) \*mdev)
    :   Detach a device from the MIPI-DSI bus.

        Parameters:
        :   - **dev** – MIPI-DSI host device.
            - **channel** – Device channel (VID).
            - **mdev** – MIPI-DSI device description.

        Returns:
        :   0 on success, negative on error

    struct mipi\_dsi\_timings
    :   *#include <mipi\_dsi.h>*

        MIPI-DSI display timings.

        Public Members

        uint32\_t hactive
        :   Horizontal active video.

        uint32\_t hfp
        :   Horizontal front porch.

        uint32\_t hbp
        :   Horizontal back porch.

        uint32\_t hsync
        :   Horizontal sync length.

        uint32\_t vactive
        :   Vertical active video.

        uint32\_t vfp
        :   Vertical front porch.

        uint32\_t vbp
        :   Vertical back porch.

        uint32\_t vsync
        :   Vertical sync length.

    struct mipi\_dsi\_device
    :   *#include <mipi\_dsi.h>*

        MIPI-DSI device.

        Public Members

        uint8\_t data\_lanes
        :   Number of data lanes.

        struct [mipi\_dsi\_timings](#c.mipi_dsi_timings) timings
        :   Display timings.

        uint32\_t pixfmt
        :   Pixel format.

        uint32\_t mode\_flags
        :   Mode flags.

    struct mipi\_dsi\_msg
    :   *#include <mipi\_dsi.h>*

        MIPI-DSI read/write message.

        Public Members

        uint8\_t type
        :   Payload data type.

        uint16\_t flags
        :   Flags controlling message transmission.

        uint8\_t cmd
        :   Command (only for DCS).

        size\_t tx\_len
        :   Transmission buffer length.

        const void \*tx\_buf
        :   Transmission buffer.

        size\_t rx\_len
        :   Reception buffer length.

        void \*rx\_buf
        :   Reception buffer.

    struct mipi\_dsi\_driver\_api
    :   *#include <mipi\_dsi.h>*

        MIPI-DSI host driver API.
