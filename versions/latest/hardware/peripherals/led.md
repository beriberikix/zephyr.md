---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/led.html
original_path: hardware/peripherals/led.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Light-Emitting Diode (LED)

## Overview

The LED API provides access to Light Emitting Diodes, both in individual and
strip form.

## Configuration Options

Related configuration options:

- [`CONFIG_LED`](../../kconfig.md#CONFIG_LED "CONFIG_LED")
- [`CONFIG_LED_STRIP`](../../kconfig.md#CONFIG_LED_STRIP "CONFIG_LED_STRIP")

## API Reference

### LED

Related code samples

[Breathing-blinking LED (BBLED)](../../samples/drivers/led_xec/README.md#led-xec "Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.")
:   Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.

[HT16K33 LED driver with keyscan](../../samples/drivers/ht16k33/README.md#ht16k33 "Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.")
:   Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.

[IS31FL3216A LED](../../samples/drivers/led_is31fl3216a/README.md#is31fl3216a "Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.")
:   Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.

[IS31FL3733 LED Matrix](../../samples/drivers/led_is31fl3733/README.md#is31fl3733 "Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.")
:   Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.

[LED PWM](../../samples/drivers/led_pwm/README.md#led-pwm "Control PWM LEDs using the LED API.")
:   Control PWM LEDs using the LED API.

[LP3943 RGBW LED](../../samples/drivers/led_lp3943/README.md#lp3943 "Control up to 16 RGBW LEDs connected to an LP3943 driver chip.")
:   Control up to 16 RGBW LEDs connected to an LP3943 driver chip.

[LP50XX RGB LED](../../samples/drivers/led_lp50xx/README.md#lp50xx "Control up to 12 RGB LEDs connected to an LP50xx driver chip.")
:   Control up to 12 RGB LEDs connected to an LP50xx driver chip.

[LP5562 RGB LED](../../samples/drivers/led_lp5562/README.md#lp5562 "Control 4 RGB LEDs connected to an LP5562 driver chip.")
:   Control 4 RGB LEDs connected to an LP5562 driver chip.

[LP5569 9-channel LED controller](../../samples/drivers/led_lp5569/README.md#lp5569 "Control 9 LEDs connected to an LP5569 driver chip.")
:   Control 9 LEDs connected to an LP5569 driver chip.

[PCA9633 LED](../../samples/drivers/led_pca9633/README.md#pca9633 "Control 4 LEDs connected to a PCA9633 driver chip.")
:   Control 4 LEDs connected to a PCA9633 driver chip.

[SX1509B RGB LED](../../samples/drivers/led_sx1509b_intensity/README.md#sx1509b "Control an RGB LED connected to an SX1509B driver chip.")
:   Control an RGB LED connected to an SX1509B driver chip.

*group* led\_interface
:   LED Interface.

    Typedefs

    typedef int (\*led\_api\_blink)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)
    :   Callback API for blinking an LED.

        See also

        [led\_blink()](#group__led__interface_1ga4f31fecd215e5597999be4d16b0d2dd5) for argument descriptions.

    typedef int (\*led\_api\_get\_info)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, const struct [led\_info](#c.led_info) \*\*info)
    :   Optional API callback to get LED information.

        See also

        [led\_get\_info()](#group__led__interface_1ga9925483b97073354f7be6b40aa2dad1a) for argument descriptions.

    typedef int (\*led\_api\_set\_brightness)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, uint8\_t value)
    :   Callback API for setting brightness of an LED.

        See also

        [led\_set\_brightness()](#group__led__interface_1gaca479fd77518331f4fc84f788e345882) for argument descriptions.

    typedef int (\*led\_api\_set\_color)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)
    :   Optional API callback to set the colors of a LED.

        See also

        [led\_set\_color()](#group__led__interface_1ga94dd46cc96f6ade5cebaa46a5f7ca5ea) for argument descriptions.

    typedef int (\*led\_api\_on)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led)
    :   Callback API for turning on an LED.

        See also

        [led\_on()](#group__led__interface_1gad4daafd7fcab22d1d68745b7264d0f73) for argument descriptions.

    typedef int (\*led\_api\_off)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led)
    :   Callback API for turning off an LED.

        See also

        [led\_off()](#group__led__interface_1ga22c9dbe76f06fec327aebe06448d1542) for argument descriptions.

    typedef int (\*led\_api\_write\_channels)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)
    :   Callback API for writing a strip of LED channels.

        See also

        [led\_api\_write\_channels()](#group__led__interface_1ga66dac12510c3a2281378d532ba6db2ae) for arguments descriptions.

    Functions

    int led\_blink(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)
    :   Blink an LED.

        This optional routine starts blinking a LED forever with the given time period.

        Parameters:
        :   - **dev** – LED device
            - **led** – LED number
            - **delay\_on** – Time period (in milliseconds) an LED should be ON
            - **delay\_off** – Time period (in milliseconds) an LED should be OFF

        Returns:
        :   0 on success, negative on error

    int led\_get\_info(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, const struct [led\_info](#c.led_info) \*\*info)
    :   Get LED information.

        This optional routine provides information about a LED.

        Parameters:
        :   - **dev** – LED device
            - **led** – LED number
            - **info** – Pointer to a pointer filled with LED information

        Returns:
        :   0 on success, negative on error

    int led\_set\_brightness(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, uint8\_t value)
    :   Set LED brightness.

        This optional routine sets the brightness of a LED to the given value. Calling this function after [led\_blink()](#group__led__interface_1ga4f31fecd215e5597999be4d16b0d2dd5) won’t affect blinking.

        LEDs which can only be turned on or off may provide this function. These should simply turn the LED on if `value` is nonzero, and off if `value` is zero.

        Parameters:
        :   - **dev** – LED device
            - **led** – LED number
            - **value** – Brightness value to set in percent

        Returns:
        :   0 on success, negative on error

    int led\_write\_channels(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)
    :   Write/update a strip of LED channels.

        This optional routine writes a strip of LED channels to the given array of levels. Therefore it can be used to configure several LEDs at the same time.

        Calling this function after [led\_blink()](#group__led__interface_1ga4f31fecd215e5597999be4d16b0d2dd5) won’t affect blinking.

        Parameters:
        :   - **dev** – LED device
            - **start\_channel** – Absolute number (i.e. not relative to a LED) of the first channel to update.
            - **num\_channels** – The number of channels to write/update.
            - **buf** – array of values to configure the channels with. num\_channels entries must be provided.

        Returns:
        :   0 on success, negative on error

    int led\_set\_channel(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint8\_t value)
    :   Set a single LED channel.

        This optional routine sets a single LED channel to the given value.

        Calling this function after [led\_blink()](#group__led__interface_1ga4f31fecd215e5597999be4d16b0d2dd5) won’t affect blinking.

        Parameters:
        :   - **dev** – LED device
            - **channel** – Absolute channel number (i.e. not relative to a LED)
            - **value** – Value to configure the channel with

        Returns:
        :   0 on success, negative on error

    int led\_set\_color(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)
    :   Set LED color.

        This routine configures all the color channels of a LED with the given color array.

        Calling this function after [led\_blink()](#group__led__interface_1ga4f31fecd215e5597999be4d16b0d2dd5) won’t affect blinking.

        Parameters:
        :   - **dev** – LED device
            - **led** – LED number
            - **num\_colors** – Number of colors in the array.
            - **color** – Array of colors. It must be ordered following the color mapping of the LED controller. See the the color\_mapping member in struct [led\_info](#structled__info).

        Returns:
        :   0 on success, negative on error

    int led\_on(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led)
    :   Turn on an LED.

        This routine turns on an LED

        Parameters:
        :   - **dev** – LED device
            - **led** – LED number

        Returns:
        :   0 on success, negative on error

    int led\_off(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t led)
    :   Turn off an LED.

        This routine turns off an LED

        Parameters:
        :   - **dev** – LED device
            - **led** – LED number

        Returns:
        :   0 on success, negative on error

    struct led\_info
    :   *#include <led.h>*

        LED information structure.

        This structure gathers useful information about LED controller.

        Public Members

        const char \*label
        :   LED label.

        uint32\_t index
        :   Number of colors per LED.

        uint8\_t num\_colors
        :   Index of the LED on the controller.

        const uint8\_t \*color\_mapping
        :   Mapping of the LED colors.

    struct led\_driver\_api
    :   *#include <led.h>*

        LED driver API.

### LED Strip

Related code samples

[APA102 LED strip](../../samples/drivers/led_apa102/README.md#led-apa102 "Control an LED strip using an APA102, Adafruit DotStar, or compatible driver chip.")
:   Control an LED strip using an APA102, Adafruit DotStar, or compatible driver chip.

[LPD880x LED strip](../../samples/drivers/led_lpd8806/README.md#led-lpd8806 "Control an LED strip using an LPD880x-compatible driver chip.")
:   Control an LED strip using an LPD880x-compatible driver chip.

[WS2812 LED strip](../../samples/drivers/led_ws2812/README.md#led-ws2812 "Control an LED strip using a WS2812 (or compatible) driver chip.")
:   Control an LED strip using a WS2812 (or compatible) driver chip.

*group* led\_strip\_interface
:   LED Strip Interface.

    Typedefs

    typedef int (\*led\_api\_update\_rgb)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [led\_rgb](#c.led_rgb) \*pixels, size\_t num\_pixels)
    :   Callback API for updating an RGB LED strip.

        See also

        [led\_strip\_update\_rgb()](#group__led__strip__interface_1ga6e63331a5be2430968ab8b60692f8d67) for argument descriptions.

    typedef int (\*led\_api\_update\_channels)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*channels, size\_t num\_channels)
    :   Callback API for updating channels without an RGB interpretation.

        See also

        [led\_strip\_update\_channels()](#group__led__strip__interface_1ga846b1d37bc6f7ed2014bea9603788b34) for argument descriptions.

    Functions

    static inline int led\_strip\_update\_rgb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [led\_rgb](#c.led_rgb) \*pixels, size\_t num\_pixels)
    :   Update an LED strip made of RGB pixels.

        Important: This routine may overwrite *pixels*.

        This routine immediately updates the strip display according to the given pixels array.

        Warning

        May overwrite *pixels*

        Parameters:
        :   - **dev** – LED strip device
            - **pixels** – Array of pixel data
            - **num\_pixels** – Length of pixels array

        Returns:
        :   0 on success, negative on error

    static inline int led\_strip\_update\_channels(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*channels, size\_t num\_channels)
    :   Update an LED strip on a per-channel basis.

        Important: This routine may overwrite *channels*.

        This routine immediately updates the strip display according to the given channels array. Each channel byte corresponds to an individually addressable color channel or LED. Channels are updated linearly in strip order.

        Warning

        May overwrite *channels*

        Parameters:
        :   - **dev** – LED strip device
            - **channels** – Array of per-channel data
            - **num\_channels** – Length of channels array

        Returns:
        :   0 on success, negative on error

    struct led\_rgb
    :   *#include <led\_strip.h>*

        Color value for a single RGB LED.

        Individual strip drivers may ignore lower-order bits if their resolution in any channel is less than a full byte.

        Public Members

        uint8\_t r
        :   Red channel.

        uint8\_t g
        :   Green channel.

        uint8\_t b
        :   Blue channel.

    struct led\_strip\_driver\_api
    :   *#include <led\_strip.h>*

        LED strip driver API.

        This is the mandatory API any LED strip driver needs to expose.
