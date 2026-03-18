---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/tgpio.html
original_path: hardware/peripherals/tgpio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Time-aware General-Purpose Input/Output (TGPIO)

## Overview

## Configuration Options

Related configuration options:

- [`CONFIG_TIMEAWARE_GPIO`](../../kconfig.md#CONFIG_TIMEAWARE_GPIO "CONFIG_TIMEAWARE_GPIO")

## API Reference

Related code samples

[Time-aware GPIO](../../samples/drivers/misc/timeaware_gpio/README.md#timeaware-gpio "Synchronize clocks.")
:   Synchronize clocks.

*group* tgpio\_interface
:   Time-aware GPIO Interface.

    Enums

    enum tgpio\_pin\_polarity
    :   Event polarity.

        *Values:*

        enumerator TGPIO\_RISING\_EDGE = 0

        enumerator TGPIO\_FALLING\_EDGE

        enumerator TGPIO\_TOGGLE\_EDGE

    Functions

    int tgpio\_port\_get\_time(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint64\_t \*current\_time)
    :   Get time from ART timer.

        Parameters:
        :   - **dev** – TGPIO device
            - **current\_time** – Pointer to store timer value in cycles

        Returns:
        :   0 if successful

        Returns:
        :   negative errno code on failure.

    int tgpio\_port\_get\_cycles\_per\_second(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*cycles)
    :   Get current running rate.

        Parameters:
        :   - **dev** – TGPIO device
            - **cycles** – pointer to store current running requency

        Returns:
        :   0 if successful, negative errno code on failure.

    int tgpio\_pin\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t pin)
    :   Disable operation on pin.

        Parameters:
        :   - **dev** – TGPIO device
            - **pin** – TGPIO pin

        Returns:
        :   0 if successful, negative errno code on failure.

    int tgpio\_pin\_config\_ext\_timestamp(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t pin, uint32\_t event\_polarity)
    :   Enable/Continue operation on pin.

        Parameters:
        :   - **dev** – TGPIO device
            - **pin** – TGPIO pin
            - **event\_polarity** – TGPIO pin event polarity

        Returns:
        :   0 if successful, negative errno code on failure.

    int tgpio\_pin\_periodic\_output(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t pin, uint64\_t start\_time, uint64\_t repeat\_interval, bool periodic\_enable)
    :   Enable periodic pulse generation on a pin.

        Parameters:
        :   - **dev** – TGPIO device
            - **pin** – TGPIO pin
            - **start\_time** – start\_time of first pulse in hw cycles
            - **repeat\_interval** – repeat interval between two pulses in hw cycles
            - **periodic\_enable** – enables periodic mode if ‘true’ is passed.

        Returns:
        :   0 if successful, negative errno code on failure.

    int tgpio\_pin\_read\_ts\_ec(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t pin, uint64\_t \*timestamp, uint64\_t \*event\_count)
    :   Read timestamp and event counter from TGPIO.

        Parameters:
        :   - **dev** – TGPIO device
            - **pin** – TGPIO pin
            - **timestamp** – timestamp of the last pulse received
            - **event\_count** – number of pulses received since the pin is enabled

        Returns:
        :   0 if successful, negative errno code on failure.
