---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/sensor/channels.html
original_path: hardware/peripherals/sensor/channels.html
---

# Sensor Channels

*Channels*, enumerated in [`sensor_channel`](../../../doxygen/html/group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934), are quantities that
a sensor device can measure.

Sensors may have multiple channels, either to represent different axes of
the same physical property (e.g. acceleration); or because they can measure
different properties altogether (ambient temperature, pressure and
humidity). Sensors may have multiple channels of the same measurement type to
enable measuring many readings of perhaps temperature, light intensity, amperage,
voltage, or capacitance for example.

A channel is specified in Zephyr using a [`sensor_chan_spec`](../../../doxygen/html/structsensor__chan__spec.md) which is a
pair containing both the channel type ([`sensor_channel`](../../../doxygen/html/group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)) and channel index.
At times only [`sensor_channel`](../../../doxygen/html/group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) is used but this should be considered
historical since the introduction of [`sensor_chan_spec`](../../../doxygen/html/structsensor__chan__spec.md) for Zephyr 3.7.
