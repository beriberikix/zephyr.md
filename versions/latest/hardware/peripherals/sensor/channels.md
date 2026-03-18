---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/sensor/channels.html
original_path: hardware/peripherals/sensor/channels.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sensor Channels

*Channels*, enumerated in [`sensor_channel`](index.md#c.sensor_channel "sensor_channel"), are quantities that
a sensor device can measure.

Sensors may have multiple channels, either to represent different axes of
the same physical property (e.g. acceleration); or because they can measure
different properties altogether (ambient temperature, pressure and
humidity). Sensors may have multiple channels of the same measurement type to
enable measuring many readings of perhaps temperature, light intensity, amperage,
voltage, or capacitance for example.

A channel is specified in Zephyr using a [`sensor_chan_spec`](index.md#c.sensor_chan_spec "sensor_chan_spec") which is a
pair containing both the channel type ([`sensor_channel`](index.md#c.sensor_channel "sensor_channel")) and channel index.
At times only [`sensor_channel`](index.md#c.sensor_channel "sensor_channel") is used but this should be considered
historical since the introduction of [`sensor_chan_spec`](index.md#c.sensor_chan_spec "sensor_chan_spec") for Zephyr 3.7.
