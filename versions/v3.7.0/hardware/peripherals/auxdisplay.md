---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/auxdisplay.html
original_path: hardware/peripherals/auxdisplay.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Auxiliary Display (auxdisplay)

## Overview

Auxiliary Displays are text-based displays that have simple interfaces for
displaying textual, numeric or alphanumeric data, as opposed to the
[Display Interface](display/index.md#display-api), auxiliary displays do not support custom
graphical output to displays (and most often monochrome), the most
advanced custom feature supported is generation of custom characters.
These inexpensive displays are commonly found with various configurations
and sizes, a common display size is 16 characters by 2 lines.

This API is unstable and subject to change.

## Configuration Options

Related configuration options:

- [`CONFIG_AUXDISPLAY`](../../kconfig.md#CONFIG_AUXDISPLAY "CONFIG_AUXDISPLAY")
- [`CONFIG_AUXDISPLAY_INIT_PRIORITY`](../../kconfig.md#CONFIG_AUXDISPLAY_INIT_PRIORITY "CONFIG_AUXDISPLAY_INIT_PRIORITY")

## API Reference

Related code samples

[Auxiliary display](../../samples/drivers/auxdisplay/README.md#auxdisplay "Output "Hello World" to an auxiliary display.")
:   Output "Hello World" to an auxiliary display.

*group* Text Display Interface
:   Auxiliary (Text) Display Interface.

    **Since**
    :   3.4

    **Version**
    :   0.1.0

    Defines

    AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED
    :   Used for minimum and maximum brightness/backlight values if not supported.

    Typedefs

    typedef uint32\_t auxdisplay\_mode\_t
    :   Used to describe the mode of an auxiliary (text) display.

    Enums

    enum auxdisplay\_position
    :   Used for moving the cursor or display position.

        *Values:*

        enumerator AUXDISPLAY\_POSITION\_ABSOLUTE = 0
        :   Moves to specified X,Y position.

        enumerator AUXDISPLAY\_POSITION\_RELATIVE
        :   Shifts current position by +/- X,Y position, does not take display direction into consideration.

        enumerator AUXDISPLAY\_POSITION\_RELATIVE\_DIRECTION
        :   Shifts current position by +/- X,Y position, takes display direction into consideration.

        enumerator AUXDISPLAY\_POSITION\_COUNT

    enum auxdisplay\_direction
    :   Used for setting character append position.

        *Values:*

        enumerator AUXDISPLAY\_DIRECTION\_RIGHT = 0
        :   Each character will be placed to the right of existing characters.

        enumerator AUXDISPLAY\_DIRECTION\_LEFT
        :   Each character will be placed to the left of existing characters.

        enumerator AUXDISPLAY\_DIRECTION\_COUNT

    Functions

    int auxdisplay\_display\_on(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Turn display on.

        Parameters:
        :   - **dev** – Auxiliary display device instance

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_display\_off(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Turn display off.

        Parameters:
        :   - **dev** – Auxiliary display device instance

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_cursor\_set\_enabled(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enabled)
    :   Set cursor enabled status on an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **enabled** – True to enable cursor, false to disable

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_position\_blinking\_set\_enabled(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enabled)
    :   Set cursor blinking status on an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **enabled** – Set to true to enable blinking position, false to disable

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_cursor\_shift\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t direction, bool display\_shift)
    :   Set cursor shift after character write and display shift.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **direction** – Sets the direction of the display when characters are written
            - **display\_shift** – If true, will shift the display when characters are written (which makes it look like the display is moving, not the cursor)

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_cursor\_position\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [auxdisplay\_position](#c.auxdisplay_position) type, int16\_t x, int16\_t y)
    :   Set cursor (and write position) on an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **type** – Type of move, absolute or offset
            - **x** – Exact or offset X position
            - **y** – Exact or offset Y position

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_cursor\_position\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int16\_t \*x, int16\_t \*y)
    :   Get current cursor on an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **x** – Will be updated with the exact X position
            - **y** – Will be updated with the exact Y position

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_display\_position\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [auxdisplay\_position](#c.auxdisplay_position) type, int16\_t x, int16\_t y)
    :   Set display position on an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **type** – Type of move, absolute or offset
            - **x** – Exact or offset X position
            - **y** – Exact or offset Y position

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_display\_position\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int16\_t \*x, int16\_t \*y)
    :   Get current display position on an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **x** – Will be updated with the exact X position
            - **y** – Will be updated with the exact Y position

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_capabilities\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [auxdisplay\_capabilities](#c.auxdisplay_capabilities) \*capabilities)
    :   Fetch capabilities (and details) of auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **capabilities** – Will be updated with the details of the auxiliary display

        Return values:
        :   - **0** – on success.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_clear(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clear display of auxiliary display and return to home position (note that this does not reset the display configuration, e.g.

        custom characters and display mode will persist).

        Parameters:
        :   - **dev** – Auxiliary display device instance

        Return values:
        :   - **0** – on success.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_brightness\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*brightness)
    :   Get the current brightness level of an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **brightness** – Will be updated with the current brightness

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_brightness\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t brightness)
    :   Update the brightness level of an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **brightness** – The brightness level to set

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_backlight\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*backlight)
    :   Get the backlight level details of an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **backlight** – Will be updated with the current backlight level

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_backlight\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t backlight)
    :   Update the backlight level of an auxiliary display.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **backlight** – The backlight level to set

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_is\_busy(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if an auxiliary display driver is busy.

        Parameters:
        :   - **dev** – Auxiliary display device instance

        Return values:
        :   - **1** – on success and display busy.
            - **0** – on success and display not busy.
            - **-ENOSYS** – if not supported/implemented.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_custom\_character\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [auxdisplay\_character](#c.auxdisplay_character) \*character)
    :   Sets a custom character in the display, the custom character struct must contain the pixel data for the custom character to add and valid custom character index, if successful then the character\_code variable in the struct will be set to the character code that can be used with the [auxdisplay\_write()](#group__auxdisplay__interface_1ga231dd862cda34ea4c0c8870675556f8d) function to show it.

        A character must be valid for a display consisting of a uint8 array of size character width by character height, values should be 0x00 for pixel off or 0xff for pixel on, if a display supports shades then values between 0x00 and 0xff may be used (display driver dependent).

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **character** – Pointer to custom character structure

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*data, uint16\_t len)
    :   Write data to auxiliary display screen at current position.

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **data** – Text data to write
            - **len** – Length of text data to write

        Return values:
        :   - **0** – on success.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    int auxdisplay\_custom\_command(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [auxdisplay\_custom\_data](#c.auxdisplay_custom_data) \*data)
    :   Send a custom command to the display (if supported by driver).

        Parameters:
        :   - **dev** – Auxiliary display device instance
            - **data** – Custom command structure (this may be extended by specific drivers)

        Return values:
        :   - **0** – on success.
            - **-ENOSYS** – if not supported/implemented.
            - **-EINVAL** – if provided argument is invalid.
            - **-errno** – Negative errno code on other failure.

    struct auxdisplay\_light
    :   *#include <auxdisplay.h>*

        Light levels for brightness and/or backlight.

        If not supported by a display/driver, both minimum and maximum will be AUXDISPLAY\_LIGHT\_NOT\_SUPPORTED.

        Public Members

        uint8\_t minimum
        :   Minimum light level supported.

        uint8\_t maximum
        :   Maximum light level supported.

    struct auxdisplay\_capabilities
    :   *#include <auxdisplay.h>*

        Structure holding display capabilities.

        Public Members

        uint16\_t columns
        :   Number of character columns.

        uint16\_t rows
        :   Number of character rows.

        [auxdisplay\_mode\_t](#c.auxdisplay_mode_t) mode
        :   Display-specific data (e.g.

            4-bit or 8-bit mode for HD44780-based displays)

        struct [auxdisplay\_light](#c.auxdisplay_light) brightness
        :   Brightness details for display (if supported).

        struct [auxdisplay\_light](#c.auxdisplay_light) backlight
        :   Backlight details for display (if supported).

        uint8\_t custom\_characters
        :   Number of custom characters supported by display (0 if unsupported).

        uint8\_t custom\_character\_width
        :   Width (in pixels) of a custom character, supplied custom characters should match.

        uint8\_t custom\_character\_height
        :   Height (in pixels) of a custom character, supplied custom characters should match.

    struct auxdisplay\_custom\_data
    :   *#include <auxdisplay.h>*

        Structure for a custom command.

        This may be extended by specific drivers.

        Public Members

        uint8\_t \*data
        :   Raw command data to be sent.

        uint16\_t len
        :   Length of supplied data.

        uint32\_t options
        :   Display-driver specific options for command.

    struct auxdisplay\_character
    :   *#include <auxdisplay.h>*

        Structure for a custom character.

        Public Members

        uint8\_t index
        :   Custom character index on the display.

        uint8\_t \*data
        :   Custom character pixel data, a character must be valid for a display consisting of a uint8 array of size character width by character height, values should be 0x00 for pixel off or 0xff for pixel on, if a display supports shades then values between 0x00 and 0xff may be used (display driver dependent).

        uint8\_t character\_code
        :   Will be updated with custom character index to use in the display write function to disaplay this custom character.
