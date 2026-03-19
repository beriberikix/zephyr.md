---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/usb/device_next/usb_device.html
original_path: connectivity/usb/device_next/usb_device.html
---

# New USB device support

## Overview

USB device support consists of the USB device controller (UDC) drivers
, [USB device controller (UDC) driver API](api/udc.md#udc-api), and USB device stack, [USB device stack (next) API](api/usbd.md#usbd-api).
The [USB device controller (UDC) driver API](api/udc.md#udc-api) provides a generic and vendor independent interface to USB
device controllers, and although, there a is clear separation between these
layers, the purpose of [USB device controller (UDC) driver API](api/udc.md#udc-api) is to serve new Zephyr’s USB device stack
exclusively.

The new device stack supports multiple device controllers, meaning that if a
SoC has multiple controllers, they can be used simultaneously. Full and
high-speed device controllers are supported. It also provides support for
registering multiple function or class instances to a configuration at runtime,
or changing the configuration later. It has built-in support for several USB
classes and provides an API to implement custom USB functions.

The new USB device support is considered experimental and will replace
[USB device support](../device/usb_device.md#usb-device-stack).

### Samples

- [USB HID keyboard](../../../samples/subsys/usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")
- [USB Audio asynchronous explicit feedback sample](../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")
- [USB Audio asynchronous implicit feedback sample](../../../samples/subsys/usb/uac2_implicit_feedback/README.md#uac2-implicit-feedback "USB Audio 2 implicit feedback sample playing stereo and recording mono audio on I2S interface.")

#### Samples ported to new USB device support

To build a sample that supports both the old and new USB device stack, set the
configuration `-DCONF_FILE=usbd_next_prj.conf` either directly or via
`west`.

- [HCI USB](../../../samples/bluetooth/hci_usb/README.md#bluetooth_hci_usb "Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).")
- [USB CDC-ACM](../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")
- [Console over USB CDC ACM](../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")
- [USB Mass Storage](../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")
- [USB HID mouse](../../../samples/subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.")
- [zperf: Network Traffic Generator](../../../samples/net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.") To build the sample for the new device support,
  set the configuration overlay file
  `-DDEXTRA_CONF_FILE=overlay-usbd_next_ecm.conf` and devicetree overlay file
  `-DDTC_OVERLAY_FILE="usbd_next_ecm.overlay` either directly or via `west`.

## How to configure and enable USB device support

For the USB device support samples in the Zephyr project repository, we have a
common file for instantiation, configuration and initialization,
[samples/subsys/usb/common/sample\_usbd\_init.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/common/sample_usbd_init.c). The following code
snippets from this file are used as examples. USB Samples Kconfig options used
in the USB samples and prefixed with `SAMPLE_USBD_` have default values
specific to the Zephyr project and the scope is limited to the project samples.
In the examples below, you will need to replace these Kconfig options and other
defaults with values appropriate for your application or hardware.

The USB device stack requires a context structure to manage its properties and
runtime data. The preferred way to define a device context is to use the
[`USBD_DEVICE_DEFINE`](../../../doxygen/html/group__usbd__api.md#ga26777805f749f29efa882f9bf391473a) macro. This creates a static
[`usbd_context`](../../../doxygen/html/structusbd__context.md) variable with a given name. Any number of contexts may
be instantiated. A USB controller device can be assigned to multiple contexts,
but only one context can be initialized and used at a time. Context properties
must not be directly accessed or manipulated by the application.

```c
/*
 * Instantiate a context named sample_usbd using the default USB device
 * controller, the Zephyr project vendor ID, and the sample product ID.
 * Zephyr project vendor ID must not be used outside of Zephyr samples.
 */
USBD_DEVICE_DEFINE(sample_usbd,
		   DEVICE_DT_GET(DT_NODELABEL(zephyr_udc0)),
		   ZEPHYR_PROJECT_USB_VID, CONFIG_SAMPLE_USBD_PID);
```

Your USB device may have manufacturer, product, and serial number string
descriptors. To instantiate these string descriptors, the application should
use the appropriate [`USBD_DESC_MANUFACTURER_DEFINE`](../../../doxygen/html/group__usbd__api.md#ga18b1321daf1173a3cb0bc61a0d9beb34),
[`USBD_DESC_PRODUCT_DEFINE`](../../../doxygen/html/group__usbd__api.md#gaa5e43f9eac8f91d3896ea5e19baed031), and
[`USBD_DESC_SERIAL_NUMBER_DEFINE`](../../../doxygen/html/group__usbd__api.md#ga26af7f93205dc78eeb60a3c09aa7b2d3) macros. String descriptors also
require a single instantiation of the language descriptor using the
[`USBD_DESC_LANG_DEFINE`](../../../doxygen/html/group__usbd__api.md#gaec816a27118bcb289ab4840fcd22888e) macro.

```c
USBD_DESC_LANG_DEFINE(sample_lang);
USBD_DESC_MANUFACTURER_DEFINE(sample_mfr, CONFIG_SAMPLE_USBD_MANUFACTURER);
USBD_DESC_PRODUCT_DEFINE(sample_product, CONFIG_SAMPLE_USBD_PRODUCT);
USBD_DESC_SERIAL_NUMBER_DEFINE(sample_sn);
```

String descriptors must be added to the device context at runtime before
initializing the USB device with [`usbd_add_descriptor()`](../../../doxygen/html/group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584).

```c
err = usbd_add_descriptor(&sample_usbd, &sample_lang);
if (err) {
	LOG_ERR("Failed to initialize language descriptor (%d)", err);
	return NULL;
}

err = usbd_add_descriptor(&sample_usbd, &sample_mfr);
if (err) {
	LOG_ERR("Failed to initialize manufacturer descriptor (%d)", err);
	return NULL;
}

err = usbd_add_descriptor(&sample_usbd, &sample_product);
if (err) {
	LOG_ERR("Failed to initialize product descriptor (%d)", err);
	return NULL;
}

err = usbd_add_descriptor(&sample_usbd, &sample_sn);
if (err) {
	LOG_ERR("Failed to initialize SN descriptor (%d)", err);
	return NULL;
}
```

USB device requires at least one configuration instance per supported speed.
The application should use [`USBD_CONFIGURATION_DEFINE`](../../../doxygen/html/group__usbd__api.md#ga2d98fd68eff66f36522688f3de527586) to instantiate
a configuration. Later, USB device functions are assigned to a configuration.

```c
static const uint8_t attributes = (IS_ENABLED(CONFIG_SAMPLE_USBD_SELF_POWERED) ?
				   USB_SCD_SELF_POWERED : 0) |
				  (IS_ENABLED(CONFIG_SAMPLE_USBD_REMOTE_WAKEUP) ?
				   USB_SCD_REMOTE_WAKEUP : 0);

/* Full speed configuration */
USBD_CONFIGURATION_DEFINE(sample_fs_config,
			  attributes,
			  CONFIG_SAMPLE_USBD_MAX_POWER, &fs_cfg_desc);

/* High speed configuration */
USBD_CONFIGURATION_DEFINE(sample_hs_config,
			  attributes,
			  CONFIG_SAMPLE_USBD_MAX_POWER, &hs_cfg_desc);
```

Each configuration instance for a specific speed must be added to the device
context at runtime before the USB device is initialized using
[`usbd_add_configuration()`](../../../doxygen/html/group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4). Note [`USBD_SPEED_FS`](../../../doxygen/html/group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7) and
[`USBD_SPEED_HS`](../../../doxygen/html/group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266). The first full-speed or high-speed
configuration will get `bConfigurationValue` one, and then further upward.

```c
err = usbd_add_configuration(&sample_usbd, USBD_SPEED_FS,
			     &sample_fs_config);
if (err) {
	LOG_ERR("Failed to add Full-Speed configuration");
	return NULL;
}
```

Although we have already done a lot, this USB device has no function. A device
can have multiple configurations with different set of functions at different
speeds. A function or class can be registered on a USB device before
it is initialized using [`usbd_register_class()`](../../../doxygen/html/group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960). The desired
configuration is specified using [`USBD_SPEED_FS`](../../../doxygen/html/group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7) or
[`USBD_SPEED_HS`](../../../doxygen/html/group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266) and the configuration number. For simple cases,
[`usbd_register_all_classes()`](../../../doxygen/html/group__usbd__api.md#ga06541b17f5afc917cc5154bd4d816ec3) can be used to register all available
instances.

```c
err = usbd_register_all_classes(&sample_usbd, USBD_SPEED_FS, 1, blocklist);
if (err) {
	LOG_ERR("Failed to add register classes");
	return NULL;
}
```

The last step in the preparation is to initialize the device with
[`usbd_init()`](../../../doxygen/html/group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f). After this, the configuration of the device cannot be
changed. A device can be deinitialized with [`usbd_shutdown()`](../../../doxygen/html/group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0) and all
instances can be reused, but the previous steps must be repeated. So it is
possible to shutdown a device, register another type of configuration or
function, and initialize it again. At the USB controller level,
[`usbd_init()`](../../../doxygen/html/group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f) does only what is necessary to detect VBUS changes. There
are controller types where the next step is only possible if a VBUS signal is
present.

A function or class implementation may require its own specific configuration
steps, which should be performed prior to initializing the USB device.

```c
err = usbd_init(&sample_usbd);
if (err) {
	LOG_ERR("Failed to initialize device support");
	return NULL;
}
```

The final step to enable the USB device is [`usbd_enable()`](../../../doxygen/html/group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68), after that,
if the USB device is connected to a USB host controller, the host can start
enumerating the device. The application can disable the USB device using
[`usbd_disable()`](../../../doxygen/html/group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b).

```c
ret = usbd_enable(sample_usbd);
if (ret) {
	LOG_ERR("Failed to enable device support");
	return ret;
}
```

### USB Message notifications

The application can register a callback using [`usbd_msg_register_cb()`](../../../doxygen/html/group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38) to
receive message notification from the USB device support subsystem. The
messages are mostly about the common device state changes, and a few specific
types from the USB CDC ACM implementation.

```c
err = usbd_msg_register_cb(&sample_usbd, msg_cb);
if (err) {
	LOG_ERR("Failed to register message callback");
	return NULL;
}
```

The helper function [`usbd_msg_type_string()`](../../../doxygen/html/group__usbd__msg__api.md#ga6cf3d874b1516256187bd96cf73ddde4) can be used to convert
`usbd_msg_type` to a human readable form for logging.

If the controller supports VBUS state change detection, the battery-powered
application may want to enable the USB device only when it is connected to a
host. A generic application should use [`usbd_can_detect_vbus()`](../../../doxygen/html/group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c) to check
for this capability.

```c
static void msg_cb(struct usbd_context *const usbd_ctx,
		   const struct usbd_msg *const msg)
{
	LOG_INF("USBD message: %s", usbd_msg_type_string(msg->type));

	if (msg->type == USBD_MSG_CONFIGURATION) {
		LOG_INF("\tConfiguration value %d", msg->status);
	}

	if (usbd_can_detect_vbus(usbd_ctx)) {
		if (msg->type == USBD_MSG_VBUS_READY) {
			if (usbd_enable(usbd_ctx)) {
				LOG_ERR("Failed to enable device support");
			}
		}

		if (msg->type == USBD_MSG_VBUS_REMOVED) {
			if (usbd_disable(usbd_ctx)) {
				LOG_ERR("Failed to disable device support");
			}
		}
	}
}
```

## Built-in functions

The USB device stack has built-in USB functions. Some can be used directly in
the user application through a special API, such as HID or Audio class devices,
while others use a general Zephyr RTOS driver API, such as MSC and CDC class
implementations. The *Identification string* identifies a class or function
instance (`n`) and is used as an argument to the [`usbd_register_class()`](../../../doxygen/html/group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960).

| Class or function | User API (if any) | Identification string |
| --- | --- | --- |
| USB Audio 2 class | [Audio Class 2 device API](api/uac2_device.md#uac2-device) | `uac2_n` |
| USB CDC ACM class | [Universal Asynchronous Receiver-Transmitter (UART)](../../../hardware/peripherals/uart.md#uart-api) | `cdc_acm_n` |
| USB CDC ECM class | Ethernet device | `cdc_ecm_n` |
| USB Mass Storage Class (MSC) | [USB Mass Storage Class device API](api/usbd_msc_device.md#usbd-msc-device) | `msc_n` |
| USB Human Interface Devices (HID) | [HID device API](api/usbd_hid_device.md#usbd-hid-device) | `hid_n` |
| Bluetooth HCI USB transport layer | [HCI RAW channel](../../bluetooth/api/hci_raw.md#bt-hci-raw) | `bt_hci_n` |

### CDC ACM UART

CDC ACM implements a virtual UART controller and provides Interrupt-driven UART
API and Polling UART API.

#### Interrupt-driven UART API

Internally the implementation uses two ringbuffers, these take over the
function of the TX/RX FIFOs (TX/RX buffers) from the [Interrupt-driven API](../../../hardware/peripherals/uart.md#uart-interrupt-api).

As described in the [Interrupt-driven API](../../../hardware/peripherals/uart.md#uart-interrupt-api), the functions
[`uart_irq_update()`](../../../doxygen/html/group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6), [`uart_irq_is_pending()`](../../../doxygen/html/group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a),
[`uart_irq_rx_ready()`](../../../doxygen/html/group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b), [`uart_irq_tx_ready()`](../../../doxygen/html/group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)
[`uart_fifo_read()`](../../../doxygen/html/group__uart__interrupt.md#gab10942076ac47ecff29e924098049398), and [`uart_fifo_fill()`](../../../doxygen/html/group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)
should be called from the interrupt handler, see
[`uart_irq_callback_user_data_set()`](../../../doxygen/html/group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0). To prevent undefined behaviour,
the implementation of these functions checks in what context they are called
and fails if it is not an interrupt handler.

Also, as described in the UART API, [`uart_irq_is_pending()`](../../../doxygen/html/group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)
[`uart_irq_rx_ready()`](../../../doxygen/html/group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b), and [`uart_irq_tx_ready()`](../../../doxygen/html/group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)
can only be called after [`uart_irq_update()`](../../../doxygen/html/group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6).

Simplified, the interrupt handler should look something like:

```c
static void interrupt_handler(const struct device *dev, void *user_data)
{
   while (uart_irq_update(dev) && uart_irq_is_pending(dev)) {
      if (uart_irq_rx_ready(dev)) {
         int len;
         int n;

         /* ... */
         n = uart_fifo_read(dev, buffer, len);
         /* ... */
      }

      if (uart_irq_tx_ready(dev)) {
         int len;
         int n;

         /* ... */
         n = uart_fifo_fill(dev, buffer, len);
        /* ... */
      }
}
```

All these functions are not directly dependent on the status of the USB device.
Filling the TX FIFO does not mean that data is being sent to the host. And
successfully reading the RX FIFO does not mean that the device is still
connected to the host. If there is space in the TX FIFO, and the TX interrupt
is enabled, [`uart_irq_tx_ready()`](../../../doxygen/html/group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638) will succeed. If there is data in the
RX FIFO, and the RX interrupt is enabled, [`uart_irq_rx_ready()`](../../../doxygen/html/group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b) will
succeed. Function [`uart_irq_tx_complete()`](../../../doxygen/html/group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455) is not implemented yet.

#### Polling UART API

The CDC ACM poll out implementation follows [Polling API](../../../hardware/peripherals/uart.md#uart-polling-api) and
blocks when the TX FIFO is full only if the hw-flow-control property is enabled
and called from a non-ISR context.
