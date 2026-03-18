---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/sensor/fetch_and_get.html
original_path: hardware/peripherals/sensor/fetch_and_get.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Fetch and Get

The stable and long existing APIs for reading sensor data and handling triggers
are:

- [`sensor_sample_fetch()`](index.md#c.sensor_sample_fetch "sensor_sample_fetch")
- [`sensor_sample_fetch_chan()`](index.md#c.sensor_sample_fetch_chan "sensor_sample_fetch_chan")
- [`sensor_channel_get()`](index.md#c.sensor_channel_get "sensor_channel_get")
- [`sensor_trigger_set()`](index.md#c.sensor_trigger_set "sensor_trigger_set")

These functions work together. The fetch APIs block the calling context which
must be a thread until the requested [`sensor_channel`](index.md#c.sensor_channel "sensor_channel") (or all channels)
has been obtained and stored into the driver instance’s private data.

The channel data most recently fetched can then be obtained as a
[`sensor_value`](index.md#c.sensor_value "sensor_value") by calling [`sensor_channel_get()`](index.md#c.sensor_channel_get "sensor_channel_get") for each channel
type.

Warning

It should be noted that calling fetch and get from multiple contexts without
a locking mechanism is undefined and most sensor drivers do not attempt to
internally provide exclusive access to the device during or between these
calls.

## Polling

Using fetch and get sensor can be read in a polling manner from software threads.

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/sys/printk.h>
#include <stdio.h>

int main(void)
{
	const struct device *const dev = DEVICE_DT_GET(DT_ALIAS(magn0));
	struct sensor_value value_x, value_y, value_z;
	int ret;

	if (!device_is_ready(dev)) {
		printk("sensor: device not ready.\n");
		return 0;
	}

	printk("Polling magnetometer data from %s.\n", dev->name);

	while (1) {
		ret = sensor_sample_fetch(dev);
		if (ret) {
			printk("sensor_sample_fetch failed ret %d\n", ret);
			return 0;
		}

		ret = sensor_channel_get(dev, SENSOR_CHAN_MAGN_X, &value_x);
		ret = sensor_channel_get(dev, SENSOR_CHAN_MAGN_Y, &value_y);
		ret = sensor_channel_get(dev, SENSOR_CHAN_MAGN_Z, &value_z);
		printf("( x y z ) = ( %f  %f  %f )\n",
		       sensor_value_to_double(&value_x),
		       sensor_value_to_double(&value_y),
		       sensor_value_to_double(&value_z));

		k_sleep(K_MSEC(500));
	}
	return 0;
}
```

## Triggers

Triggers in the stable API require enabling triggers with a device
specific Kconfig. The device specific Kconfig typically allows selecting the
context the trigger runs. The application then needs to register a callback with
a function signature matching [`sensor_trigger_handler_t`](index.md#c.sensor_trigger_handler_t "sensor_trigger_handler_t") using
[`sensor_trigger_set()`](index.md#c.sensor_trigger_set "sensor_trigger_set") for the specific triggers (events) to listen for.

Note

Triggers may not be set from user mode threads, and the callback is not
run in a user mode context.

There are typically two options provided for each driver where to run trigger
handlers. Either the trigger handler is run using the system work queue thread
([Workqueue Threads](../../../kernel/services/threads/workqueue.md#workqueues-v2)) or a dedicated thread. A great example can be found in
the BMI160 driver which has Kconfig options for selecting a trigger mode.
See [`CONFIG_BMI160_TRIGGER_NONE`](../../../kconfig.md#CONFIG_BMI160_TRIGGER_NONE "CONFIG_BMI160_TRIGGER_NONE"),
[`CONFIG_BMI160_TRIGGER_GLOBAL_THREAD`](../../../kconfig.md#CONFIG_BMI160_TRIGGER_GLOBAL_THREAD "CONFIG_BMI160_TRIGGER_GLOBAL_THREAD") (work queue),
[`CONFIG_BMI160_TRIGGER_OWN_THREAD`](../../../kconfig.md#CONFIG_BMI160_TRIGGER_OWN_THREAD "CONFIG_BMI160_TRIGGER_OWN_THREAD") (dedicated thread).

Some notable attributes of using a driver dedicated thread vs the system work
queue.

- Driver dedicated threads have dedicated stack (RAM) which only gets used for
  that single trigger handler function.
- Driver dedicated threads *do* get their own priority typically which lets you
  prioritize trigger handling among other threads.
- Driver dedicated threads will not have head of line blocking if the driver
  needs time to handle the trigger.

Note

In all cases it’s very likely there will be variable delays from the actual
interrupt to your callback function being run. In the work queue
(GLOBAL\_THREAD) case the work queue itself can be the source of variable
latency!

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/drivers/sensor.h>

const struct device *const accel0 = DEVICE_DT_GET(DT_ALIAS(accel0));

static struct tap_count_state {
	struct sensor_trigger trig;
	uint32_t count;
} tap_count_state = {
	.trig = {
		.chan = SENSOR_CHAN_ACCEL_XYZ,
		.type = SENSOR_TRIG_TAP,
	},
	.count = 0,
};

void tap_handler(const struct device *dev, const struct sensor_trigger *trig)
{
	struct tap_count_state *state = CONTAINER_OF(trig, struct tap_count_state, trig);

	state->count++;

	printk("Tap! Total Taps: %u\n", state->count);
}

int main(void)
{
	int rc;

	printk("Tap Counter Example (%s)\n", CONFIG_ARCH);

	rc = sensor_trigger_set(accel0, &tap_count_state.trig, tap_handler);

	if (rc != 0) {
		printk("Failed to set trigger handler for taps, error %d\n", rc);
		return rc;
	}

	return rc;
}
```
