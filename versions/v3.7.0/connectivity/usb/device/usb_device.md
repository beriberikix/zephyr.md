---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device/usb_device.html
original_path: connectivity/usb/device/usb_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB device support

## [Overview](#id1)

The USB device stack is a hardware independent interface between USB
device controller driver and USB device class drivers or customer applications.
It is a port of the LPCUSB device stack and has been modified and expanded
over time. It provides the following functionalities:

- Uses the [USB device controller driver API](api/usb_dc.md#usb-dc-api) provided by the device controller drivers to interact with
  the USB device controller.
- Responds to standard device requests and returns standard descriptors,
  essentially handling ‘Chapter 9’ processing, specifically the standard
  device requests in table 9-3 from the universal serial bus specification
  revision 2.0.
- Provides a programming interface to be used by USB device classes or
  customer applications. The APIs is described in
  [include/zephyr/usb/usb\_device.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/usb_device.h)

Note

It is planned to deprecate all APIs listed in [USB device support APIs](api/index.md#usb-api) and the
functions that depend on them between Zephyr v3.7.0 and v4.0.0, and remove
them in v4.2.0. The new USB device support, represented by the APIs in
[New USB device support APIs](../device_next/api/index.md#usb-device-next-api), will become the default in Zephyr v4.0.0.

## [Supported USB classes](#id2)

### [Audio](#id3)

There is an experimental implementation of the Audio class. It follows specification
version 1.00 (`bcdADC 0x0100`) and supports synchronous synchronisation type only.
See [USB Audio microphone & headphones](../../../samples/subsys/usb/audio/headphones_microphone/README.md#usb-audio-headphones-microphone "Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.") and
[USB Audio headset](../../../samples/subsys/usb/audio/headset/README.md#usb-audio-headset "Implement a USB Audio headset device with audio IN/OUT loopback.") samples for reference.

### [Bluetooth HCI USB transport layer](#id4)

Bluetooth HCI USB transport layer implementation uses [HCI RAW channel](../../bluetooth/api/hci_raw.md#bt-hci-raw)
to expose HCI interface to the host. It is not fully in line with the description
in the Bluetooth specification and consists only of an interface with the endpoint
configuration:

- HCI commands through control endpoint (host-to-device only)
- HCI events through interrupt IN endpoint
- ACL data through one bulk IN and one bulk OUT endpoints

A second interface for the voice channels has not been implemented as there is
no support for this type in [Bluetooth](../../bluetooth/index.md#bluetooth). It is not a big problem under Linux
if HCI USB transport layer is the only interface that appears in the configuration,
the btusb driver would not try to claim a second (isochronous) interface.
The consequence is that if HCI USB is used in a composite configuration and is
the first interface, then the Linux btusb driver will claim both the first and
the next interface, preventing other composite functions from working.
Because of this problem, HCI USB should not be used in a composite configuration.
This problem is fixed in the implementation for new USB support.

See [Bluetooth: HCI USB](../../../samples/bluetooth/hci_usb/README.md#bluetooth-hci-usb-sample) sample for reference.

### [CDC ACM](#id5)

The CDC ACM class is used as backend for different subsystems in Zephyr.
However, its configuration may not be easy for the inexperienced user.
Below is a description of the different use cases and some pitfalls.

The interface for CDC ACM user is [Universal Asynchronous Receiver-Transmitter (UART)](../../../hardware/peripherals/uart.md#uart-api) driver API.
But there are two important differences in behavior to a real UART controller:

- Data transfer is only possible after the USB device stack has been
  initialized and started, until then any data is discarded
- If device is connected to the host, it still needs an application
  on the host side which requests the data
- The CDC ACM poll out implementation follows the API and blocks when the TX
  ring buffer is full only if the hw-flow-control property is enabled and
  called from a non-ISR context.

The devicetree compatible property for CDC ACM UART is
[`zephyr,cdc-acm-uart`](../../../build/dts/api/bindings/serial/zephyr%2Ccdc-acm-uart.md#std-dtcompatible-zephyr-cdc-acm-uart).
CDC ACM support is automatically selected when USB device support is enabled
and a compatible node in the devicetree sources is present. If necessary,
CDC ACM support can be explicitly disabled by [`CONFIG_USB_CDC_ACM`](../../../kconfig.md#CONFIG_USB_CDC_ACM "CONFIG_USB_CDC_ACM").
About four CDC ACM UART instances can be defined and used,
limited by the maximum number of supported endpoints on the controller.

CDC ACM UART node is supposed to be child of a USB device controller node.
Since the designation of the controller nodes varies from vendor to vendor,
and our samples and application should be as generic as possible,
the default USB device controller is usually assigned an `zephyr_udc0`
node label. Often, CDC ACM UART is described in a devicetree overlay file
and looks like this:

```devicetree
&zephyr_udc0 {
        cdc_acm_uart0: cdc_acm_uart0 {
                compatible = "zephyr,cdc-acm-uart";
                label = "CDC_ACM_0";
        };
};
```

Sample [USB CDC-ACM](../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") has similar overlay files.
And since no special properties are present, it may seem overkill to use
devicetree to describe CDC ACM UART. The motivation behind using devicetree
is the easy interchangeability of a real UART controller and CDC ACM UART
in applications.

#### [Console over CDC ACM UART](#id6)

With the CDC ACM UART node from above and `zephyr,console` property of the
chosen node, we can describe that CDC ACM UART is to be used with the console.
A similar overlay file is used by the [Console over USB CDC ACM](../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.") sample.

```devicetree
/ {
        chosen {
                zephyr,console = &cdc_acm_uart0;
        };
};

&zephyr_udc0 {
        cdc_acm_uart0: cdc_acm_uart0 {
                compatible = "zephyr,cdc-acm-uart";
                label = "CDC_ACM_0";
        };
};
```

Before the application uses the console, it is recommended to wait for
the DTR signal:

```c
const struct device *const dev = DEVICE_DT_GET(DT_CHOSEN(zephyr_console));
uint32_t dtr = 0;

if (usb_enable(NULL)) {
        return;
}

while (!dtr) {
        uart_line_ctrl_get(dev, UART_LINE_CTRL_DTR, &dtr);
        k_sleep(K_MSEC(100));
}

printk("nuqneH\n");
```

#### [CDC ACM UART as backend](#id7)

As for the console sample, it is possible to configure CDC ACM UART as
backend for other subsystems by setting [Chosen nodes](../../../build/dts/api/api.md#devicetree-chosen-nodes)
properties.

List of few Zephyr specific chosen properties which can be used to select
CDC ACM UART as backend for a subsystem or application:

- `zephyr,bt-c2h-uart` used in Bluetooth,
  for example see [Bluetooth: HCI UART](../../../samples/bluetooth/hci_uart/README.md#bluetooth-hci-uart-sample)
- `zephyr,ot-uart` used in OpenThread,
  for example see [OpenThread co-processor](../../../samples/net/openthread/coprocessor/README.md#coprocessor "Build a Thread border-router using OpenThread's co-processor designs.")
- `zephyr,shell-uart` used by shell for serial backend,
  for example see [samples/subsys/shell/shell\_module](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/shell_module)
- `zephyr,uart-mcumgr` used by [SMP server](../../../samples/subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.") sample

#### [POSIX default tty ECHO mitigation](#id8)

POSIX systems, like Linux, default to enabling ECHO on tty devices. Host side
application can disable ECHO by calling `open()` on the tty device and issuing
`ioctl()` (preferably via `tcsetattr()`) to disable echo if it is not desired.
Unfortunately, there is an inherent race between the `open()` and `ioctl()`
where the ECHO is enabled and any characters received (even if host application
does not call `read()`) will be echoed back. This issue is especially visible
when the CDC ACM port is used without any real UART on the other side because
there is no arbitrary delay due to baud rate.

To mitigate the issue, Zephyr CDC ACM implementation arms IN endpoint with ZLP
after device is configured. When the host reads the ZLP, which is pretty much
the best indication that host application has opened the tty device, Zephyr will
force [`CONFIG_CDC_ACM_TX_DELAY_MS`](../../../kconfig.md#CONFIG_CDC_ACM_TX_DELAY_MS "CONFIG_CDC_ACM_TX_DELAY_MS") millisecond delay before real
payload is sent. This should allow sufficient time for first, and only first,
application that opens the tty device to disable ECHO if ECHO is not desired.
If ECHO is not desired at all from CDC ACM device it is best to set up udev rule
to disable ECHO as soon as device is connected.

ECHO is particurarly unwanted when CDC ACM instance is used for Zephyr shell,
because the control characters to set color sent back to shell are interpreted
as (invalid) command and user will see garbage as a result. While minicom does
disable ECHO by default, on exit with reset it will restore the termios settings
to whatever was set on entry. Therefore, if minicom is the first application to
open the tty device, the exit with reset will enable ECHO back and thus set up
a problem for the next application (which cannot be mitigated at Zephyr side).
To prevent the issue it is recommended either to leave minicom without reset or
to disable ECHO before minicom is started.

### [DFU](#id9)

USB DFU class implementation is tightly coupled to [Device Firmware Upgrade](../../../services/device_mgmt/dfu.md#dfu) and [MCUBoot API](../../../services/device_mgmt/dfu.md#mcuboot-api).
This means that the target platform must support the [Flash Image](../../../services/device_mgmt/dfu.md#flash-img-api) API.

See [USB DFU (Device Firmware Upgrade)](../../../samples/subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.") sample for reference.

### [USB Human Interface Devices (HID) support](#id10)

HID support abuses [Device Driver Model](../../../kernel/drivers/index.md#device-model-api) simply to allow applications to use
the [`device_get_binding()`](../../../kernel/drivers/index.md#c.device_get_binding "device_get_binding"). Note that there is no HID device API as such,
instead the interface is provided by [`hid_ops`](api/usb_device_hid.md#c.hid_ops "hid_ops").
The default instance name is `HID_n`, where n can be {0, 1, 2, …} depending on
the [`CONFIG_USB_HID_DEVICE_COUNT`](../../../kconfig.md#CONFIG_USB_HID_DEVICE_COUNT "CONFIG_USB_HID_DEVICE_COUNT").

Each HID instance requires a HID report descriptor. The interface to the core
and the report descriptor must be registered using [`usb_hid_register_device()`](api/usb_device_hid.md#c.usb_hid_register_device "usb_hid_register_device").

As the USB HID specification is not only used by the USB subsystem, the USB HID API
reference is split into two parts, [Human Interface Devices (HID)](../api/hid.md#usb-hid-common) and [USB HID Class API](api/usb_device_hid.md#usb-hid-device).
HID helper macros from [Human Interface Devices (HID)](../api/hid.md#usb-hid-common) should be used to compose a
HID report descriptor. Macro names correspond to those used in the USB HID specification.

For the HID class interface, an IN interrupt endpoint is required for each instance,
an OUT interrupt endpoint is optional. Thus, the minimum implementation requirement
for [`hid_ops`](api/usb_device_hid.md#c.hid_ops "hid_ops") is to provide `int_in_ready` callback.

```c
#define REPORT_ID               1
static bool configured;
static const struct device *hdev;

static void int_in_ready_cb(const struct device *dev)
{
        static uint8_t report[2] = {REPORT_ID, 0};

        if (hid_int_ep_write(hdev, report, sizeof(report), NULL)) {
                LOG_ERR("Failed to submit report");
        } else {
                report[1]++;
        }
}

static void status_cb(enum usb_dc_status_code status, const uint8_t *param)
{
        if (status == USB_DC_RESET) {
                configured = false;
        }

        if (status == USB_DC_CONFIGURED && !configured) {
                int_in_ready_cb(hdev);
                configured = true;
        }
}

static const uint8_t hid_report_desc[] = {
        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),
        HID_USAGE(HID_USAGE_GEN_DESKTOP_UNDEFINED),
        HID_COLLECTION(HID_COLLECTION_APPLICATION),
        HID_LOGICAL_MIN8(0x00),
        HID_LOGICAL_MAX16(0xFF, 0x00),
        HID_REPORT_ID(REPORT_ID),
        HID_REPORT_SIZE(8),
        HID_REPORT_COUNT(1),
        HID_USAGE(HID_USAGE_GEN_DESKTOP_UNDEFINED),
        HID_INPUT(0x02),
        HID_END_COLLECTION,
};

static const struct hid_ops my_ops = {
        .int_in_ready = int_in_ready_cb,
};

int main(void)
{
        int ret;

        hdev = device_get_binding("HID_0");
        if (hdev == NULL) {
                return -ENODEV;
        }

        usb_hid_register_device(hdev, hid_report_desc, sizeof(hid_report_desc),
                                &my_ops);

        ret = usb_hid_init(hdev);
        if (ret) {
                return ret;
        }

        return usb_enable(status_cb);
}
```

If the application wishes to receive output reports via the OUT interrupt endpoint,
it must enable [`CONFIG_ENABLE_HID_INT_OUT_EP`](../../../kconfig.md#CONFIG_ENABLE_HID_INT_OUT_EP "CONFIG_ENABLE_HID_INT_OUT_EP") and provide
`int_out_ready` callback.
The disadvantage of this is that Kconfig options such as
[`CONFIG_ENABLE_HID_INT_OUT_EP`](../../../kconfig.md#CONFIG_ENABLE_HID_INT_OUT_EP "CONFIG_ENABLE_HID_INT_OUT_EP") or
[`CONFIG_HID_INTERRUPT_EP_MPS`](../../../kconfig.md#CONFIG_HID_INTERRUPT_EP_MPS "CONFIG_HID_INTERRUPT_EP_MPS") apply to all instances. This design
issue will be fixed in the HID class implementation for the new USB support.

See [USB HID (Human Interface Device)](../../../samples/subsys/usb/hid/README.md#usb-hid "Use USB HID driver to enumerate as a raw HID device.") or [USB HID mouse](../../../samples/subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.") sample for reference.

### [Mass Storage Class](#id11)

MSC follows Bulk-Only Transport specification and uses [Disk Access](../../../services/storage/disk/access.md#disk-access-api) to
access and expose a RAM disk, emulated block device on a flash partition,
or SD Card to the host. Only one disk instance can be exported at a time.

The disc to be used by the implementation is set by the
[`CONFIG_MASS_STORAGE_DISK_NAME`](../../../kconfig.md#CONFIG_MASS_STORAGE_DISK_NAME "CONFIG_MASS_STORAGE_DISK_NAME") and should be the same as the name
used by the disc access driver that the application wants to expose to the host.
SD card disk drivers use options [`CONFIG_MMC_VOLUME_NAME`](../../../kconfig.md#CONFIG_MMC_VOLUME_NAME "CONFIG_MMC_VOLUME_NAME") or
[`CONFIG_SDMMC_VOLUME_NAME`](../../../kconfig.md#CONFIG_SDMMC_VOLUME_NAME "CONFIG_SDMMC_VOLUME_NAME"), and flash and RAM disk drivers use
node property `disk-name` to set the disk name.

For the emulated block device on a flash partition, the flash partition and
flash disk to be used must be described in the devicetree. If a storage partition
is already described at the board level, application devicetree overlay must also
delete `storage_partition` node first. [`CONFIG_MASS_STORAGE_DISK_NAME`](../../../kconfig.md#CONFIG_MASS_STORAGE_DISK_NAME "CONFIG_MASS_STORAGE_DISK_NAME")
should be the same as `disk-name` property.

```devicetree
/delete-node/ &storage_partition;

&mx25r64 {
        partitions {
                compatible = "fixed-partitions";
                #address-cells = <1>;
                #size-cells = <1>;

                storage_partition: partition@0 {
                        label = "storage";
                        reg = <0x00000000 0x00020000>;
                };
        };
};

/ {
        msc_disk0 {
                compatible = "zephyr,flash-disk";
                partition = <&storage_partition>;
                disk-name = "NAND";
                cache-size = <4096>;
        };
};
```

The `disk-property` “NAND” may be confusing, but it is simply how some file
systems identifies the disc. Therefore, if the application also accesses the
file system on the exposed disc, default names should be used, see
[USB Mass Storage](../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.") sample for reference.

### [Networking](#id12)

There are three implementations that work in a similar way, providing a virtual
Ethernet connection between the remote (USB host) and Zephyr network support.

- CDC ECM class, enabled with [`CONFIG_USB_DEVICE_NETWORK_ECM`](../../../kconfig.md#CONFIG_USB_DEVICE_NETWORK_ECM "CONFIG_USB_DEVICE_NETWORK_ECM")
- CDC EEM class, enabled with [`CONFIG_USB_DEVICE_NETWORK_EEM`](../../../kconfig.md#CONFIG_USB_DEVICE_NETWORK_EEM "CONFIG_USB_DEVICE_NETWORK_EEM")
- RNDIS support, enabled with [`CONFIG_USB_DEVICE_NETWORK_RNDIS`](../../../kconfig.md#CONFIG_USB_DEVICE_NETWORK_RNDIS "CONFIG_USB_DEVICE_NETWORK_RNDIS")

See [zperf: Network Traffic Generator](../../../samples/net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.") or [Dumb HTTP server](../../../samples/net/sockets/dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.") for reference.
Typically, users will need to add a configuration file overlay to the build,
such as [samples/net/zperf/overlay-netusb.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/zperf/overlay-netusb.conf).

Applications using RNDIS support should enable [`CONFIG_USB_DEVICE_OS_DESC`](../../../kconfig.md#CONFIG_USB_DEVICE_OS_DESC "CONFIG_USB_DEVICE_OS_DESC")
for a better user experience on a host running Microsoft Windows OS.

## [Binary Device Object Store (BOS) support](#id13)

BOS handling can be enabled with Kconfig option [`CONFIG_USB_DEVICE_BOS`](../../../kconfig.md#CONFIG_USB_DEVICE_BOS "CONFIG_USB_DEVICE_BOS").
This option also has the effect of changing device descriptor `bcdUSB` to `0210`.
The application should register descriptors such as Capability Descriptor
using [`usb_bos_register_cap()`](api/usb_device.md#c.usb_bos_register_cap "usb_bos_register_cap"). Registered descriptors are added to the root
BOS descriptor and handled by the stack.

See [WebUSB](../../../samples/subsys/usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.") sample for reference.

## [Implementing a non-standard USB class](#id14)

The configuration of USB device is done in the stack layer.

The following structures and callbacks need to be defined:

- Part of USB Descriptor table
- USB Endpoint configuration table
- USB Device configuration structure
- Endpoint callbacks
- Optionally class, vendor and custom handlers

For example, for the USB loopback application:

```c
 1struct usb_loopback_config {
 2	struct usb_if_descriptor if0;
 3	struct usb_ep_descriptor if0_out_ep;
 4	struct usb_ep_descriptor if0_in_ep;
 5} __packed;
 6
 7USBD_CLASS_DESCR_DEFINE(primary, 0) struct usb_loopback_config loopback_cfg = {
 8	/* Interface descriptor 0 */
 9	.if0 = {
10		.bLength = sizeof(struct usb_if_descriptor),
11		.bDescriptorType = USB_DESC_INTERFACE,
12		.bInterfaceNumber = 0,
13		.bAlternateSetting = 0,
14		.bNumEndpoints = 2,
15		.bInterfaceClass = USB_BCC_VENDOR,
16		.bInterfaceSubClass = 0,
17		.bInterfaceProtocol = 0,
18		.iInterface = 0,
19	},
20
21	/* Data Endpoint OUT */
22	.if0_out_ep = {
23		.bLength = sizeof(struct usb_ep_descriptor),
24		.bDescriptorType = USB_DESC_ENDPOINT,
25		.bEndpointAddress = LOOPBACK_OUT_EP_ADDR,
26		.bmAttributes = USB_DC_EP_BULK,
27		.wMaxPacketSize = sys_cpu_to_le16(CONFIG_LOOPBACK_BULK_EP_MPS),
28		.bInterval = 0x00,
29	},
30
31	/* Data Endpoint IN */
32	.if0_in_ep = {
33		.bLength = sizeof(struct usb_ep_descriptor),
34		.bDescriptorType = USB_DESC_ENDPOINT,
35		.bEndpointAddress = LOOPBACK_IN_EP_ADDR,
36		.bmAttributes = USB_DC_EP_BULK,
37		.wMaxPacketSize = sys_cpu_to_le16(CONFIG_LOOPBACK_BULK_EP_MPS),
38		.bInterval = 0x00,
39	},
40};
```

Endpoint configuration:

```c
 1static struct usb_ep_cfg_data ep_cfg[] = {
 2	{
 3		.ep_cb = loopback_out_cb,
 4		.ep_addr = LOOPBACK_OUT_EP_ADDR,
 5	},
 6	{
 7		.ep_cb = loopback_in_cb,
 8		.ep_addr = LOOPBACK_IN_EP_ADDR,
 9	},
10};
```

USB Device configuration structure:

```c
 1USBD_DEFINE_CFG_DATA(loopback_config) = {
 2	.usb_device_description = NULL,
 3	.interface_config = loopback_interface_config,
 4	.interface_descriptor = &loopback_cfg.if0,
 5	.cb_usb_status = loopback_status_cb,
 6	.interface = {
 7		.class_handler = NULL,
 8		.custom_handler = NULL,
 9		.vendor_handler = loopback_vendor_handler,
10	},
11	.num_endpoints = ARRAY_SIZE(ep_cfg),
12	.endpoint = ep_cfg,
13};
```

The vendor device requests are forwarded by the USB stack core driver to the
class driver through the registered vendor handler.

For the loopback class driver, `loopback_vendor_handler()` processes
the vendor requests:

```c
 1static int loopback_vendor_handler(struct usb_setup_packet *setup,
 2				   int32_t *len, uint8_t **data)
 3{
 4	LOG_DBG("Class request: bRequest 0x%x bmRequestType 0x%x len %d",
 5		setup->bRequest, setup->bmRequestType, *len);
 6
 7	if (setup->RequestType.recipient != USB_REQTYPE_RECIPIENT_DEVICE) {
 8		return -ENOTSUP;
 9	}
10
11	if (usb_reqtype_is_to_device(setup) &&
12	    setup->bRequest == 0x5b) {
13		LOG_DBG("Host-to-Device, data %p", *data);
14		/*
15		 * Copy request data in loopback_buf buffer and reuse
16		 * it later in control device-to-host transfer.
17		 */
18		memcpy(loopback_buf, *data,
19		       MIN(sizeof(loopback_buf), setup->wLength));
20		return 0;
21	}
22
23	if ((usb_reqtype_is_to_host(setup)) &&
24	    (setup->bRequest == 0x5c)) {
25		LOG_DBG("Device-to-Host, wLength %d, data %p",
26			setup->wLength, *data);
27		*data = loopback_buf;
28		*len = MIN(sizeof(loopback_buf), setup->wLength);
29		return 0;
30	}
31
32	return -ENOTSUP;
33}
```

The class driver waits for the **USB\_DC\_CONFIGURED** device status code
before transmitting any data.

## [Interface number and endpoint address assignment](#id15)

In USB terminology, a `function` is a device that provides a capability to the
host, such as a HID class device that implements a keyboard. A function
contains a collection of `interfaces`; at least one interface is required. An
interface may contain device `endpoints`; for example, at least one input
endpoint is required to implement a HID class device, and no endpoints are
required to implement a USB DFU class. A USB device that combines functions is
a multifunction USB device, for example, a combination of a HID class device
and a CDC ACM device.

With Zephyr RTOS USB support, various combinations are possible with built-in USB
classes/functions or custom user implementations. The limitation is the number
of available device endpoints. Each device endpoint is uniquely addressable.
The endpoint address is a combination of endpoint direction and endpoint
number, a four-bit value. Endpoint number zero is used for the default control
method to initialize and configure a USB device. By specification, a maximum of
`15 IN` and `15 OUT` device endpoints are also available for use in functions.
The actual number depends on the device controller used. Not all controllers
support the maximum number of endpoints and all endpoint types. For example, a
device controller might support one IN and one OUT isochronous endpoint, but
only for endpoint number 8, resulting in endpoint addresses 0x88 and 0x08.
Also, one controller may be able to have IN/OUT endpoints on the same endpoint
number, interrupt IN endpoint 0x81 and bulk OUT endpoint 0x01, while the other
may only be able to handle one endpoint per endpoint number. Information about
the number of interfaces, interface associations, endpoint types, and addresses
is provided to the host by the interface, interface specific, and endpoint
descriptors.

Host driver for specific function, uses interface and endpoint descriptor to
obtain endpoint addresses, types, and other properties. This allows function
host drivers to be generic, for example, a multi-function device consisting of
one or more CDC ACM and one or more CDC ECM class implementations is possible
and no specific drivers are required.

Interface and endpoint descriptors of built-in USB class/function
implementations in Zephyr RTOS typically have default interface numbers and
endpoint addresses assigned in ascending order. During initialization,
default interface numbers may be reassigned based on the number of interfaces in
a given configuration. Endpoint addresses are reassigned based on controller
capabilities, since certain endpoint combinations are not possible with every
controller, and the number of interfaces in a given configuration. This also
means that the device side class/function in the Zephyr RTOS must check the
actual interface and endpoint descriptor values at runtime.
This mechanism also allows as to provide generic samples and generic
multifunction samples that are limited only by the resources provided by the
controller, such as the number of endpoints and the size of the endpoint FIFOs.

There may be host drivers for a specific function, for example in the Linux
Kernel, where the function driver does not read interface and endpoint
descriptors to check interface numbers or endpoint addresses, but instead uses
hardcoded values. Therefore, the host driver cannot be used in a generic way,
meaning it cannot be used with different device controllers and different
device configurations in combination with other functions. This may also be
because the driver is designed for a specific hardware and is not intended to
be used with a clone of this specific hardware. On the contrary, if the driver
is generic in nature and should work with different hardware variants, then it
must not use hardcoded interface numbers and endpoint addresses.
It is not possible to disable endpoint reassignment in Zephyr RTOS, which may
prevent you from implementing a hardware-clone firmware. Instead, if possible,
the host driver implementation should be fixed to use values from the interface
and endpoint descriptor.

## [Testing over USPIP in native\_sim](#id16)

A virtual USB controller implemented through USBIP might be used to test the USB
device stack. Follow the general build procedure to build the USB sample for
the [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim) configuration.

Run built sample with:

```shell
west build -t run
```

In a terminal window, run the following command to list USB devices:

```shell
$ usbip list -r localhost
Exportable USB devices
======================
 - 127.0.0.1
        1-1: unknown vendor : unknown product (2fe3:0100)
           : /sys/devices/pci0000:00/0000:00:01.2/usb1/1-1
           : (Defined at Interface level) (00/00/00)
           :  0 - Vendor Specific Class / unknown subclass / unknown protocol (ff/00/00)
```

In a terminal window, run the following command to attach the USB device:

```shell
$ sudo usbip attach -r localhost -b 1-1
```

The USB device should be connected to your Linux host, and verified with the
following commands:

```shell
$ sudo usbip port
Imported USB devices
====================
Port 00: <Port in Use> at Full Speed(12Mbps)
       unknown vendor : unknown product (2fe3:0100)
       7-1 -> usbip://localhost:3240/1-1
           -> remote bus/dev 001/002
$ lsusb -d 2fe3:0100
Bus 007 Device 004: ID 2fe3:0100
```

## [USB Vendor and Product identifiers](#id17)

The USB Vendor ID for the Zephyr project is `0x2FE3`.
This USB Vendor ID must not be used when a vendor
integrates Zephyr USB device support into its own product.

Each USB [sample](../../../samples/subsys/usb/usb.md#usb-samples) has its own unique Product ID.
The USB maintainer, if one is assigned, or otherwise the Zephyr Technical
Steering Committee, may allocate other USB Product IDs based on well-motivated
and documented requests.

The following Product IDs are currently used:

| Sample | PID |
| --- | --- |
| [USB CDC-ACM](../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") | 0x0001 |
| [USB CDC-ACM composite](../../../samples/subsys/usb/cdc_acm_composite/README.md#usb-cdc-acm-composite "Implement a composite USB device exposing two serial ports using USB CDC-ACM driver.") | 0x0002 |
| Reserved (previously: usb-hid-cdc) | 0x0003 |
| [Console over USB CDC ACM](../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.") | 0x0004 |
| [USB DFU (Device Firmware Upgrade)](../../../samples/subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.") (Run-Time) | 0x0005 |
| [USB HID (Human Interface Device)](../../../samples/subsys/usb/hid/README.md#usb-hid "Use USB HID driver to enumerate as a raw HID device.") | 0x0006 |
| [USB HID mouse](../../../samples/subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.") | 0x0007 |
| [USB Mass Storage](../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.") | 0x0008 |
| [USB testing application](../../../samples/subsys/usb/testusb/README.md#testusb-app "Test USB device drivers using a loopback function.") | 0x0009 |
| [WebUSB](../../../samples/subsys/usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.") | 0x000A |
| [Bluetooth: HCI USB](../../../samples/bluetooth/hci_usb/README.md#bluetooth-hci-usb-sample) | 0x000B |
| [Bluetooth: HCI H4 over USB](../../../samples/bluetooth/hci_usb_h4/README.md#bluetooth-hci-usb-h4-sample) | 0x000C |
| [802.15.4 USB](../../../samples/net/wpanusb/README.md#wpan-usb "Implement a device that exposes an IEEE 802.15.4 radio over USB.") | 0x000D |
| [USB Audio asynchronous explicit feedback sample](../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.") | 0x000E |
| [USB DFU (Device Firmware Upgrade)](../../../samples/subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.") (DFU Mode) | 0xFFFF |

The USB device descriptor field `bcdDevice` (Device Release Number) represents
the Zephyr kernel major and minor versions as a binary coded decimal value.
