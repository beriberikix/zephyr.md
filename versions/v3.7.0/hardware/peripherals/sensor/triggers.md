---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/sensor/triggers.html
original_path: hardware/peripherals/sensor/triggers.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Sensor Triggers

*Triggers*, enumerated in [`sensor_trigger_type`](index.md#c.sensor_trigger_type "sensor_trigger_type"), are sensor
generated events. Typically sensors allow setting up these events to cause
digital line signaling for easy capture by a micro controller. The events can
then commonly be inspected by reading registers to determine which event caused
the digital line signaling to occur.

There are many kinds of triggers sensors provide, from informative ones such as
data ready to physical events such as taps or steps.
