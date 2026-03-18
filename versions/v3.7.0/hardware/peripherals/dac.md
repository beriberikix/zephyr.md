---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/dac.html
original_path: hardware/peripherals/dac.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Digital-to-Analog Converter (DAC)

## Overview

The DAC API provides access to Digital-to-Analog Converter (DAC) devices.

## Configuration Options

Related configuration options:

- [`CONFIG_DAC`](../../kconfig.md#CONFIG_DAC "CONFIG_DAC")

## API Reference

Related code samples

[Digital-to-Analog Converter (DAC)](../../samples/drivers/dac/README.md#dac "Generate an analog sawtooth signal using the DAC driver API.")
:   Generate an analog sawtooth signal using the DAC driver API.

*group* DAC driver APIs
:   DAC driver APIs.

    **Since**
    :   2.3

    **Version**
    :   0.8.0

    Functions

    int dac\_channel\_setup(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [dac\_channel\_cfg](#c.dac_channel_cfg) \*channel\_cfg)
    :   Configure a DAC channel.

        It is required to call this function and configure each channel before it is selected for a write request.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel\_cfg** – Channel configuration.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If a parameter with an invalid value has been provided.
            - **-ENOTSUP** – If the requested resolution is not supported.

    int dac\_write\_value(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t channel, uint32\_t value)
    :   Write a single value to a DAC channel.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel** – Number of the channel to be used.
            - **value** – Data to be written to DAC output registers.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If a parameter with an invalid value has been provided.

    struct dac\_channel\_cfg
    :   *#include <dac.h>*

        Structure for specifying the configuration of a DAC channel.

        Public Members

        uint8\_t channel\_id
        :   Channel identifier of the DAC that should be configured.

        uint8\_t resolution
        :   Desired resolution of the DAC (depends on device capabilities).

        bool buffered
        :   Enable output buffer for this channel.

            This is relevant for instance if the output is directly connected to the load, without an amplifierin between. The actual details on this are hardware dependent.
