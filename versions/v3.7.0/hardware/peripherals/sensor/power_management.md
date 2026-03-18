---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/sensor/power_management.html
original_path: hardware/peripherals/sensor/power_management.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Power Management

Power management of sensors is often a non-trivial task as sensors may have multiple power states
for various channels. Some sensors may allow for low noise, low power, or suspending channels
potentially saving quite a bit of power at the cost of noise or sampling speed performance. In very
low power states sensors may lose their state, turning off even the digital logic portion of the device.

All this is to say that power management of sensors is typically application specific! Often the
channel states are mutable using [Sensor Attributes](attributes.md#sensor-attribute). While total device suspending and resume
can be done using the power management ref counting APIs if the device implements the necessary
functionality.

Most likely the API sensors should use for their fully suspended/resume power states is
[Device Runtime Power Management](../../../services/pm/device_runtime.md#pm-device-runtime) using explicit calls at an application level to [`pm_device_runtime_get()`](../../../services/pm/api/index.md#c.pm_device_runtime_get "pm_device_runtime_get")
and [`pm_device_runtime_put()`](../../../services/pm/api/index.md#c.pm_device_runtime_put "pm_device_runtime_put").

In the future, with [Read and Decode](read_and_decode.md#sensor-read-and-decode) its possible that automatic management of device power management
would be possible in the streaming case as the application informs the driver of usage at all times
through requests to read on given events.
