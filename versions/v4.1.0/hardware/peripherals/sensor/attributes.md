---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/sensor/attributes.html
original_path: hardware/peripherals/sensor/attributes.html
---

# Sensor Attributes

*Attributes*, enumerated in [`sensor_attribute`](../../../doxygen/html/group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b), are immutable and
mutable properties of a sensor and its channels.

Attributes allow for obtaining metadata and changing configuration of a sensor.
Common configuration parameters like channel scale, sampling frequency, adjusting
channel offsets, signal filtering, power modes, on chip buffers, and event
handling options are very common. Attributes provide a flexible API for
inspecting and manipulating such device properties.

Attributes are specified using [`sensor_attribute`](../../../doxygen/html/group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) which can be used with
[`sensor_attr_get()`](../../../doxygen/html/group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a) and [`sensor_attr_set()`](../../../doxygen/html/group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5) to get and set a sensors
attributes.

A quick example…

```c
const struct device *accel_dev = DEVICE_DT_GET(DT_ALIAS(accel0));
struct sensor_value accel_sample_rate;
int rc;

rc = sensor_attr_get(accel_dev, SENSOR_CHAN_ACCEL_XYZ, SENSOR_ATTR_SAMPLING_FREQUENCY, &accel_sample_rate);
if (rc != 0) {
             printk("Failed to get sampling frequency\n");
}

printk("Sample rate for accel %p is %d.06%d\n", accel_dev, accel_sample_rate.val1, accel_sample_rate.val2*1000000);

accel_sample_rate.val1 = 2000;

rc = sensor_attr_set(accel_dev, SENSOR_CHAN_ACCEL_XYZ, SENSOR_ATTR_SAMPLING_FREQUENCY, accel_sample_rate);
if (rc != 0) {
             printk("Failed to set sampling frequency\n");
}
```
