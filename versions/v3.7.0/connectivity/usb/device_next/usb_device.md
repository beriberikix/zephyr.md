---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device_next/usb_device.html
original_path: connectivity/usb/device_next/usb_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

### Built-in functions

The USB device stack has built-in USB functions. Some can be used directly in
the user application through a special API, such as HID or Audio class devices,
while others use a general Zephyr RTOS driver API, such as MSC and CDC class
implementations. The *Identification string* identifies a class or function
instance (n) and is used as an argument to the [`usbd_register_class()`](api/usbd.md#c.usbd_register_class "usbd_register_class").

| Class or function | User API (if any) | Identification string |
| --- | --- | --- |
| USB Audio 2 class | [Audio Class 2 device API](api/uac2_device.md#uac2-device) | `uac2_n` |
| USB CDC ACM class | [Universal Asynchronous Receiver-Transmitter (UART)](../../../hardware/peripherals/uart.md#uart-api) | `cdc_acm_n` |
| USB CDC ECM class | Ethernet device | `cdc_ecm_n` |
| USB Mass Storage Class (MSC) | [USB Mass Storage Class device API](api/usbd_msc_device.md#usbd-msc-device) | `msc_n` |
| USB Human Interface Devices (HID) | [HID device API](api/usbd_hid_device.md#usbd-hid-device) | `hid_n` |
| Bluetooth HCI USB transport layer | [HCI RAW channel](../../bluetooth/api/hci_raw.md#bt-hci-raw) | `bt_hci_n` |

### Samples

- [USB HID keyboard](../../../samples/subsys/usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")
- [USB Audio asynchronous explicit feedback sample](../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")

#### Samples ported to new USB device support

To build a sample that supports both the old and new USB device stack, set the
configuration `-DCONF_FILE=usbd_next_prj.conf` either directly or via
`west`.

- [Bluetooth: HCI USB](../../../samples/bluetooth/hci_usb/README.md#bluetooth-hci-usb-sample)
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
[`USBD_DEVICE_DEFINE`](api/usbd.md#c.USBD_DEVICE_DEFINE "USBD_DEVICE_DEFINE") macro. This creates a static
[`usbd_context`](api/usbd.md#c.usbd_context "usbd_context") variable with a given name. Any number of contexts may
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
use the appropriate [`USBD_DESC_MANUFACTURER_DEFINE`](api/usbd.md#c.USBD_DESC_MANUFACTURER_DEFINE "USBD_DESC_MANUFACTURER_DEFINE"),
[`USBD_DESC_PRODUCT_DEFINE`](api/usbd.md#c.USBD_DESC_PRODUCT_DEFINE "USBD_DESC_PRODUCT_DEFINE"), and
[`USBD_DESC_SERIAL_NUMBER_DEFINE`](api/usbd.md#c.USBD_DESC_SERIAL_NUMBER_DEFINE "USBD_DESC_SERIAL_NUMBER_DEFINE") macros. String descriptors also
require a single instantiation of the language descriptor using the
[`USBD_DESC_LANG_DEFINE`](api/usbd.md#c.USBD_DESC_LANG_DEFINE "USBD_DESC_LANG_DEFINE") macro.

```c
USBD_DESC_LANG_DEFINE(sample_lang);
USBD_DESC_MANUFACTURER_DEFINE(sample_mfr, CONFIG_SAMPLE_USBD_MANUFACTURER);
USBD_DESC_PRODUCT_DEFINE(sample_product, CONFIG_SAMPLE_USBD_PRODUCT);
USBD_DESC_SERIAL_NUMBER_DEFINE(sample_sn);
```

String descriptors must be added to the device context at runtime before
initializing the USB device with [`usbd_add_descriptor()`](api/usbd.md#c.usbd_add_descriptor "usbd_add_descriptor").

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
The application should use [`USBD_CONFIGURATION_DEFINE`](api/usbd.md#c.USBD_CONFIGURATION_DEFINE "USBD_CONFIGURATION_DEFINE") to instantiate
a configuration. Later, USB device functions are assigned to a configuration.

```c
static const uint8_t attributes = (IS_ENABLED(CONFIG_SAMPLE_USBD_SELF_POWERED) ?
				   USB_SCD_SELF_POWERED : 0) |
				  (IS_ENABLED(CONFIG_SAMPLE_USBD_REMOTE_WAKEUP) ?
				   USB_SCD_REMOTE_WAKEUP : 0);

/* Full speed configuration */
USBD_CONFIGURATION_DEFINE(sample_fs_config,
			  attributes,
			  CONFIG_SAMPLE_USBD_MAX_POWER);

/* High speed configuration */
USBD_CONFIGURATION_DEFINE(sample_hs_config,
			  attributes,
			  CONFIG_SAMPLE_USBD_MAX_POWER);
```

Each configuration instance for a specific speed must be added to the device
context at runtime before the USB device is initialized using
[`usbd_add_configuration()`](api/usbd.md#c.usbd_add_configuration "usbd_add_configuration"). Note [`USBD_SPEED_FS`](api/usbd.md#c.usbd_speed.USBD_SPEED_FS "USBD_SPEED_FS") and
[`USBD_SPEED_HS`](api/usbd.md#c.usbd_speed.USBD_SPEED_HS "USBD_SPEED_HS"). The first full-speed or high-speed
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
it is initialized using [`usbd_register_class()`](api/usbd.md#c.usbd_register_class "usbd_register_class"). The desired
configuration is specified using [`USBD_SPEED_FS`](api/usbd.md#c.usbd_speed.USBD_SPEED_FS "USBD_SPEED_FS") or
[`USBD_SPEED_HS`](api/usbd.md#c.usbd_speed.USBD_SPEED_HS "USBD_SPEED_HS") and the configuration number. For simple cases,
[`usbd_register_all_classes()`](api/usbd.md#c.usbd_register_all_classes "usbd_register_all_classes") can be used to register all available
instances.

```c
err = usbd_register_all_classes(&sample_usbd, USBD_SPEED_FS, 1);
if (err) {
	LOG_ERR("Failed to add register classes");
	return NULL;
}
```

The last step in the preparation is to initialize the device with
[`usbd_init()`](api/usbd.md#c.usbd_init "usbd_init"). After this, the configuration of the device cannot be
changed. A device can be deinitialized with [`usbd_shutdown()`](api/usbd.md#c.usbd_shutdown "usbd_shutdown") and all
instances can be reused, but the previous steps must be repeated. So it is
possible to shutdown a device, register another type of configuration or
function, and initialize it again. At the USB controller level,
[`usbd_init()`](api/usbd.md#c.usbd_init "usbd_init") does only what is necessary to detect VBUS changes. There
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

The final step to enable the USB device is [`usbd_enable()`](api/usbd.md#c.usbd_enable "usbd_enable"), after that,
if the USB device is connected to a USB host controller, the host can start
enumerating the device. The application can disable the USB device using
[`usbd_disable()`](api/usbd.md#c.usbd_disable "usbd_disable").

```c
ret = usbd_enable(sample_usbd);
if (ret) {
	LOG_ERR("Failed to enable device support");
	return ret;
}
```

### USB Message notifications

The application can register a callback using [`usbd_msg_register_cb()`](api/usbd.md#c.usbd_msg_register_cb "usbd_msg_register_cb") to
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

The helper function [`usbd_msg_type_string()`](api/usbd.md#c.usbd_msg_type_string "usbd_msg_type_string") can be used to convert
[`usbd_msg_type`](api/usbd.md#c.usbd_msg_type "usbd_msg_type") to a human readable form for logging.

If the controller supports VBUS state change detection, the battery-powered
application may want to enable the USB device only when it is connected to a
host. A generic application should use [`usbd_can_detect_vbus()`](api/usbd.md#c.usbd_can_detect_vbus "usbd_can_detect_vbus") to check
for this capability.

```c
static void msg_cb(struct usbd_context *const usbd_ctx,
		   const struct usbd_msg *const msg)
{
	LOG_INF("USBD message: %s", usbd_msg_type_string(msg->type));

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
