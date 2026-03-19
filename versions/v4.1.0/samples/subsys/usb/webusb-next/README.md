---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/usb/webusb-next/README.html
original_path: samples/subsys/usb/webusb-next/README.html
---

# WebUSB-next

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/usb/webusb-next/README.rst/..)

## Overview

This sample demonstrates how to use the Binary Device Object Store (BOS),
Microsoft OS 2.0 descriptors, and WebUSB descriptors to implement a WebUSB
sample application. The sample USB function receives the data and echoes back
to the WebUSB API based application running in the browser on your local host.
This sample can be found at [samples/subsys/usb/webusb-next](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/webusb-next) in the
Zephyr project tree.

## Requirements

This project requires a USB device controller driver using the UDC API.
On your host computer, this project requires a web browser that supports the
WebUSB API, such as Chromium or a Chromium-based browser.

## Building and Running

Build and flash webusb sample with:

```shell
west build -b <board to use> samples/subsys/usb/webusb-next
west flash
```

## Demonstration

The sample includes a simple WebUSB API application and can be found in the
sample directory: [samples/subsys/usb/webusb-next/index.html](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/webusb-next/index.html).

There are two ways to access this sample page:

- Using browser go to [WebUSB HTML Demo App](demo.md)
- Start a web server in the sample directory:

  ```shell
  $ python -m http.server
  ```

Then follow these steps:

1. Connect the board to your host.
2. Once the device has booted, you may see a notification from the browser: “Go
   to localhost to connect”. Click on the notification to open the demo page. If
   there is no notification from the browser, open the URL [http://localhost:8001/](http://localhost:8001/)
   in your browser.
3. Click on the Connect button to connect to the device.
4. Send some text to the device by clicking on the Send button.
   The demo application will receive the same text from the device and display
   it in the text area.

## References

WebUSB API Specification:
[https://wicg.github.io/webusb/](https://wicg.github.io/webusb/)

Chrome for Developers, “Access USB Devices on the Web”:
[https://developer.chrome.com/docs/capabilities/usb](https://developer.chrome.com/docs/capabilities/usb)

## See also

[USB device core API](../../../../doxygen/html/group__usbd__api.md)
