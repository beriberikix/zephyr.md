---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/sensor/triggers.html
original_path: hardware/peripherals/sensor/triggers.html
---

# Sensor Triggers

*Triggers*, enumerated in [`sensor_trigger_type`](../../../doxygen/html/group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd), are sensor
generated events. Typically sensors allow setting up these events to cause
digital line signaling for easy capture by a microcontroller. The events can
then commonly be inspected by reading registers to determine which event caused
the digital line signaling to occur.

There are many kinds of triggers sensors provide, from informative ones such as
data ready to physical events such as taps or steps.
