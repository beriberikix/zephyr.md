---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device_next/api/usbd_hid_device.html
original_path: connectivity/usb/device_next/api/usbd_hid_device.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# HID device API

HID device specific API defined in [include/zephyr/usb/class/usbd\_hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usbd_hid.h).

## API Reference

Related code samples

[USB HID keyboard](../../../../samples/subsys/usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")
:   Implement a basic HID keyboard device.

*group* USBD HID device API
:   USBD HID Device API.

    Enums

    enum [anonymous]
    :   HID report types Report types used in Get/Set Report requests.

        *Values:*

        enumerator HID\_REPORT\_TYPE\_INPUT = 1

        enumerator HID\_REPORT\_TYPE\_OUTPUT

        enumerator HID\_REPORT\_TYPE\_FEATURE

    Functions

    int hid\_device\_register(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*const rdesc, const uint16\_t rsize, const struct [hid\_device\_ops](#c.hid_device_ops) \*const ops)
    :   Register HID device report descriptor and user callbacks.

        The device must register report descriptor and user callbacks before USB device support is initialized and enabled.

        Parameters:
        :   - **dev** – **[in]** Pointer to HID device
            - **rdesc** – **[in]** Pointer to HID report descriptor
            - **rsize** – **[in]** Size of HID report descriptor
            - **ops** – **[in]** Pointer to HID device callbacks

    int hid\_device\_submit\_report(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t size, const uint8\_t \*const report)
    :   Submit new input report.

        Submit a new input report to be sent via the interrupt IN pipe. If sync is true, the functions will block until the report is sent. If the device does not provide input\_report\_done() callback, [hid\_device\_submit\_report()](#group__usbd__hid__device_1ga547f99b1089a4d65a297faa5d6e8edd8) will be processed synchronously.

        Parameters:
        :   - **dev** – **[in]** Pointer to HID device
            - **size** – **[in]** Size of the input report
            - **report** – **[in]** Input report buffer. Report buffer must be aligned.

        Returns:
        :   0 on success, negative errno code on fail.

    struct hid\_device\_ops
    :   *#include <usbd\_hid.h>*

        HID device user callbacks.

        Each device depends on a user part that handles feature, input, and output report processing according to the device functionality described by the report descriptor. Which callbacks must be implemented depends on the device functionality. The USB device part of the HID device, cannot interpret device specific report descriptor and only handles USB specific parts, transfers and validation of requests, all reports are opaque to it. Callbacks are called from the USB device stack thread and must not block.

        Public Members

        void (\*iface\_ready)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const bool ready)
        :   The interface ready callback is called with the ready argument set to true when the corresponding interface is part of the active configuration and the device can e.g.

            begin submitting input reports, and with the argument set to false when the interface is no longer active. This callback is optional.

        int (\*get\_report)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t type, const uint8\_t id, const uint16\_t len, uint8\_t \*const buf)
        :   This callback is called for the HID Get Report request to get a feature, input, or output report, which is specified by the argument type.

            If there is no report ID in the report descriptor, the id argument is zero. The callback implementation must check the arguments, such as whether the report type is supported and the report length, and return a negative value to indicate an unsupported type or an error, or return the length of the report written to the buffer.

        int (\*set\_report)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t type, const uint8\_t id, const uint16\_t len, const uint8\_t \*const buf)
        :   This callback is called for the HID Set Report request to set a feature, input, or output report, which is specified by the argument type.

            If there is no report ID in the report descriptor, the id argument is zero. The callback implementation must check the arguments, such as whether the report type is supported, and return a nonzero value to indicate an unsupported type or an error.

        void (\*set\_idle)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t id, const uint32\_t duration)
        :   Notification to limit input report frequency.

            The device should mute an input report submission until a new event occurs or until the time specified by the duration value has elapsed. If a report ID is used in the report descriptor, the device must store the duration and handle the specified report accordingly. Duration time resolution is in milliseconds.

        uint32\_t (\*get\_idle)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t id)
        :   If a report ID is used in the report descriptor, the device must implement this callback and return the duration for the specified report ID.

            Duration time resolution is in milliseconds.

        void (\*set\_protocol)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t proto)
        :   Notification that the host has changed the protocol from Boot Protocol(0) to Report Protocol(1) or vice versa.

        void (\*input\_report\_done)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Notification that input report submitted with [hid\_device\_submit\_report()](#group__usbd__hid__device_1ga547f99b1089a4d65a297faa5d6e8edd8) has been sent.

            If the device does not use the callback, [hid\_device\_submit\_report()](#group__usbd__hid__device_1ga547f99b1089a4d65a297faa5d6e8edd8) will be processed synchronously.

        void (\*output\_report)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t len, const uint8\_t \*const buf)
        :   New output report callback.

            Callback will only be called for reports received through the optional interrupt OUT pipe. If there is no interrupt OUT pipe, output reports will be received using [set\_report()](#structhid__device__ops_1add555b9782b763d5b411909d07d952b8). If a report ID is used in the report descriptor, the host places the ID in the buffer first, followed by the report data.

        void (\*sof)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Optional Start of Frame (SoF) event callback.

            There will always be software and hardware dependent jitter and latency. This should be used very carefully, it should not block and the execution time should be quite short.
