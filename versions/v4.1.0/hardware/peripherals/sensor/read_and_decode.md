---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/hardware/peripherals/sensor/read_and_decode.html
original_path: hardware/peripherals/sensor/read_and_decode.html
---

# Read and Decode

The quickly stabilizing experimental APIs for reading sensor data are:

- [`sensor_read()`](../../../doxygen/html/group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)
- [`sensor_read_async_mempool()`](../../../doxygen/html/group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)
- [`sensor_get_decoder()`](../../../doxygen/html/group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)
- [`sensor_decode()`](../../../doxygen/html/group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)

## Benefits over [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get)

These APIs allow for a wider usage of sensors, sensor types, and data flows with
sensors. These are the future looking APIs in Zephyr and solve many issues
that have been run into with [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get).

[`sensor_read()`](../../../doxygen/html/group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976) and similar functions acquire sensor encoded data into
a buffer provided by the caller. Decode ([`sensor_decode()`](../../../doxygen/html/group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)) then
decodes the sensor specific encoded data into fixed point [`q31_t`](../../../doxygen/html/group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) values
as vectors per channel. This allows further processing using fixed point DSP
functions that work on vectors of data to be done (e.g. low-pass filters, FFT,
fusion, etc).

Reading is by default asynchronous in its implementation and takes advantage of
[Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) to enable chaining asynchronous requests, or starting requests
against many sensors simultaneously from a single call context.

This enables incredibly useful code flows when working with sensors such as:

- Obtaining the raw sensor data, decoding never, later, or on a separate
  processor (e.g. a phone).
- Starting a read for sensors directly from an interrupt handler. No dedicated
  thread needed saving precious stack space. No work queue needed introducing
  variable latency. Starting a read for multiple sensors simultaneously from a
  single call context (interrupt/thread/work queue).
- Requesting multiple reads to the same device for Ping-Pong (double buffering)
  setups.
- Creating entire pipelines of data flow from sensors allowing for software
  defined virtual sensors ([Sensing Subsystem](../../../services/sensing/index.md#sensing)) all from a single thread with DAG
  process ordering.
- Potentially pre-programming DMAs to trigger on GPIO events, leaving the CPU
  entirely out of the loop in handling sensor events like FIFO watermarks.

Additionally, other shortcomings of [Fetch and Get](fetch_and_get.md#sensor-fetch-and-get) related to memory
and trigger handling are solved.

- Triggers result in enqueued events, not callbacks.
- Triggers can be setup to automatically fetch data. Potentially
  enabling pre-programmed DMA transfers on GPIO interrupts.
- Far less likely triggers are missed due to long held interrupt masks from
  callbacks and context swapping.
- Sensor FIFOs supported by wiring up FIFO triggers to read data into
  mempool allocated buffers.
- All sensor processing can be done in user mode (memory protected) threads.
- Multiple sensor channels of the same type are better supported.

Note

For [Read and Decode](#read-and-decode) benefits to be fully realized requires
[Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) compliant communication access to the sensor. Typically this means
an [Real Time I/O (RTIO)](../../../services/rtio/index.md#rtio) enabled bus driver for SPI or I2C.

## Polling Read

Polling reads with [Read and Decode](#read-and-decode) can be accomplished by instantiating a
polling I/O device (akin to a file descriptor) for the sensor with the desired
channels to poll. Requesting either blocking or non-blocking reads, then
optionally decoding the data into fixed point values.

Polling a temperature sensor and printing its readout is likely the simplest
sample to show how this all works.

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/drivers/sensor.h>

#define TEMP_CHANNEL {SENSOR_CHAN_AMBIENT_TEMP, 0}

const struct device *const temp0 = DEVICE_DT_GET(DT_ALIAS(temp0));

SENSOR_DT_READ_IODEV(temp_iodev, DT_ALIAS(temp0), {TEMP_CHANNEL});
RTIO_DEFINE(temp_ctx, 1, 1);

int main(void)
{
	int rc;
	uint8_t buf[8];
	uint32_t temp_frame_iter = 0;
	struct sensor_q31_data temp_data = {0};
	struct sensor_decode_context temp_decoder = SENSOR_DECODE_CONTEXT_INIT(
		SENSOR_DECODER_DT_GET(DT_ALIAS(temp0)), buf, SENSOR_CHAN_AMBIENT_TEMP, 0);

	while (1) {
		/* Blocking read */
		rc = sensor_read(temp_iodev, &temp_ctx, buf, sizeof(buf));

		if (rc != 0) {
			printk("sensor_read() failed %d\n", rc);
		}

		/* Decode the data into a single q31 */
		sensor_decode(&temp_decoder, &temp_data, 1);

		printk("Temperature " PRIsensor_q31_data "\n",
		       PRIsensor_q31_data_arg(temp_data, 0));

		k_msleep(1);
	}
}
```

## Polling Read with Multiple Sensors

One of the benefits of Read and Decode is the ability to concurrently read many
sensors with many channels in one thread. Effectively read requests are started
asynchronously for all sensors and their channels. When each read completes we
then decode the sensor data. Examples speak loudly and so a sample showing how
this might work with multiple temperature sensors with multiple temperature
channels:

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/drivers/sensor.h>

#define TEMP_CHANNELS				\
	{ SENSOR_CHAN_AMBIENT_TEMP, 0 },	\
	{ SENSOR_CHAN_AMBIENT_TEMP, 1 }
#define TEMP_ALIAS(id) DT_ALIAS(CONCAT(temp, id))
#define TEMP_IODEV_SYM(id) CONCAT(temp_iodev, id)
#define TEMP_IODEV_PTR(id) &TEMP_IODEV_SYM(id)
#define TEMP_DEFINE_IODEV(id)			\
	SENSOR_DT_READ_IODEV(			\
		TEMP_IODEV_SYM(id),		\
		TEMP_ALIAS(id),			\
		TEMP_CHANNELS			\
		);

#define NUM_SENSORS 2

LISTIFY(NUM_SENSORS, TEMP_DEFINE_IODEV, (;));

struct sensor_iodev *iodevs[NUM_SENSORS] = { LISTIFY(NUM_SENSORS, TEMP_IODEV_PTR, (,)) };

RTIO_DEFINE_WITH_MEMPOOL(temp_ctx, NUM_SENSORS, NUM_SENSORS, NUM_SENSORS, 8, sizeof(void *));

int main(void)
{
	int rc;
	uint32_t temp_frame_iter = 0;
	struct sensor_q31_data temp_data[2] = {0};
	struct sensor_decoder_api *decoder;
	struct rtio_cqe *cqe;
	uint8_t *buf;
	uint32_t buf_len;

	while (1) {
		/* Non-Blocking read for each sensor */
		for (int i = 0; i < NUM_SENSORS; i++) {
			rc = sensor_read_async_mempool(iodevs[i], &temp_ctx, iodevs[i]);

			if (rc != 0) {
				printk("sensor_read() failed %d\n", rc);
				return;
			}
		}

		/* Wait for read completions */
		for (int i = 0; i < NUM_SENSORS; i++) {
			cqe = rtio_cqe_consume_block(&temp_ctx);

			if (cqe->result != 0) {
				printk("async read failed %d\n", cqe->result);
				return;
			}

			/* Get the associated mempool buffer with the completion */
			rc = rtio_cqe_get_mempool_buffer(&temp_ctx, cqe, &buf, &buf_len);

			if (rc != 0) {
				printk("get mempool buffer failed %d\n", rc);
				return;
			}

			struct device *sensor = ((struct sensor_read_config *)
				((struct rtio_iodev *)cqe->userdata)->data)->sensor;

			/* Done with the completion event, release it */
			rtio_cqe_release(&temp_ctx, cqe);

			rc = sensor_get_decoder(sensor, &decoder);
			if (rc != 0) {
				printk("sensor_get_decoder failed %d\n", rc);
				return;
			}

			/* Frame iterators, one per channel we are decoding */
			uint32_t temp_fits[2] = { 0, 0 };

			decoder->decode(buf, {SENSOR_CHAN_AMBIENT_TEMP, 0},
					&temp_fits[0], 1, &temp_data[0]);
			decoder->decode(buf, {SENSOR_CHAN_AMBIENT_TEMP, 1},
					&temp_fits[1], 1, &temp_data[1]);

			/* Done with the buffer, release it */
			rtio_release_buffer(&temp_ctx, buf, buf_len);

			printk("Temperature for %s channel 0 " PRIsensor_q31_data ", channel 1 "
			    PRIsensor_q31_data "\n",
			    dev->name,
			    PRIsensor_q31_data_arg(temp_data[0], 0),
			    PRIsensor_q31_data_arg(temp_data[1], 0));
		}
	}

	k_msleep(1);
}
```

## Streaming

Handling triggers with [Read and Decode](#read-and-decode) works by setting up a stream I/O device
configuration. A stream specifies the set of triggers to capture and if data
should be captured with the event.

```c
/*
 * Copyright (c) 2024 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/drivers/sensor.h>

#define ACCEL_TRIGGERS						\
	{ SENSOR_TRIG_DRDY, SENSOR_STREAM_DATA_INCLUDE },	\
	{ SENSOR_TRIG_TAP, SENSOR_STREAM_DATA_NOP }
#define ACCEL_ALIAS(id) DT_ALIAS(CONCAT(accel, id))
#define ACCEL_IODEV_SYM(id) CONCAT(accel_iodev, id)
#define ACCEL_IODEV_PTR(id) &ACCEL_IODEV_SYM(id)
#define ACCEL_DEFINE_IODEV(id)					\
	SENSOR_DT_STREAM_IODEV(					\
		ACCEL_IODEV_SYM(id),				\
		ACCEL_ALIAS(id),				\
		ACCEL_TRIGGERS					\
		);

#define NUM_SENSORS 2

LISTIFY(NUM_SENSORS, ACCEL_DEFINE_IODEV, (;));

struct sensor_iodev *iodevs[NUM_SENSORS] = { LISTIFY(NUM_SENSORS, ACCEL_IODEV_PTR, (,)) };

RTIO_DEFINE_WITH_MEMPOOL(accel_ctx, NUM_SENSORS, NUM_SENSORS, NUM_SENSORS, 16, sizeof(void *));

int main(void)
{
	int rc;
	uint32_t accel_frame_iter = 0;
	struct sensor_three_axis_data accel_data[2] = {0};
	struct sensor_decoder_api *decoder;
	struct rtio_cqe *cqe;
	uint8_t *buf;
	uint32_t buf_len;
	struct rtio_sqe *handles[2];

	/* Start the streams */
	for (int i = 0; i < NUM_SENSORS; i++) {
		sensor_stream(iodevs[i], &accel_ctx, NULL, &handles[i]);
	}

	while (1) {
		cqe = rtio_cqe_consume_block(&accel_ctx);

		if (cqe->result != 0) {
			printk("async read failed %d\n", cqe->result);
			return;
		}

		rc = rtio_cqe_get_mempool_buffer(&accel_ctx, cqe, &buf, &buf_len);

		if (rc != 0) {
			printk("get mempool buffer failed %d\n", rc);
			return;
		}

		struct device *sensor = ((struct sensor_read_config *)
					 ((struct rtio_iodev *)cqe->userdata)->data)->sensor;

		rtio_cqe_release(&accel_ctx, cqe);

		rc = sensor_get_decoder(sensor, &decoder);

		if (rc != 0) {
			printk("sensor_get_decoder failed %d\n", rc);
			return;
		}

		/* Frame iterator values when data comes from a FIFO */
		uint32_t accel_fit = 0;

		/* Number of accelerometer data frames */
		uint32_t frame_count;

		rc = decoder->get_frame_count(buf, {SENSOR_CHAN_ACCEL_XYZ, 0},
					      &frame_count);
		if (rc != 0) {
			printk("sensor_get_decoder failed %d\n", rc);
			return;
		}

		/* If a tap has occurred lets print it out */
		if (decoder->has_trigger(buf, SENSOR_TRIG_TAP)) {
			printk("Tap! Sensor %s\n", dev->name);
		}

		/* Decode all available accelerometer sample frames */
		for (int i = 0; i < frame_count; i++) {
			decoder->decode(buf, {SENSOR_CHAN_ACCEL_XYZ, 0},
					accel_fit, 1, &accel_data);
			printk("Accel data for %s " PRIsensor_three_axis_data "\n",
			       dev->name,
			       PRIsensor_three_axis_data_arg(accel_data, 0));
		}

		rtio_release_buffer(&accel_ctx, buf, buf_len);
	}
}
```
