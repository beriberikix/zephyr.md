---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusb__audio__ops.html
original_path: doxygen/html/structusb__audio__ops.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_audio\_ops Struct Reference

Audio callbacks used to interact with audio devices by user App.
[More...](#details)

`#include <[usb_audio.h](usb__audio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [usb\_audio\_data\_request\_cb\_t](usb__audio_8h.md#a8f289f2b4d0a7d3accdc6308cb5661e8) | [data\_request\_cb](#a6ee19a7aef47561f14981b7e7ebd8ac7) |
|  | Callback called when data could be send. |
| [usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2) | [data\_written\_cb](#a2752018597ba5bd4e9a80d1ae650bf8b) |
|  | Callback called when data were successfully written with sending capable device. |
| [usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2) | [data\_received\_cb](#a483af21f54537bef1a6ae3be2cd3717d) |
|  | Callback called when data were successfully received by receive capable device. |
| [usb\_audio\_feature\_updated\_cb\_t](usb__audio_8h.md#a692362e834622532b7be71d5e0bdc219) | [feature\_update\_cb](#a861823185efb5c9a06b900799adb9efb) |
|  | Callback called when features were modified by the Host. |

## Detailed Description

Audio callbacks used to interact with audio devices by user App.

[usb\_audio\_ops](structusb__audio__ops.md "Audio callbacks used to interact with audio devices by user App.") structure contains all relevant callbacks to interact with USB Audio devices. Each of this callbacks is optional and may be left NULL. This will not break the stack but could make USB Audio device useless. Depending on the device some of those callbacks are necessary to make USB device work as expected sending/receiving data. For more information refer to callback documentation above.

## Field Documentation

## [◆ ](#a483af21f54537bef1a6ae3be2cd3717d)data\_received\_cb

| [usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2) usb\_audio\_ops::data\_received\_cb |
| --- |

Callback called when data were successfully received by receive capable device.

Applicable for headset and headphones. Unused for microphone.

## [◆ ](#a6ee19a7aef47561f14981b7e7ebd8ac7)data\_request\_cb

| [usb\_audio\_data\_request\_cb\_t](usb__audio_8h.md#a8f289f2b4d0a7d3accdc6308cb5661e8) usb\_audio\_ops::data\_request\_cb |
| --- |

Callback called when data could be send.

## [◆ ](#a2752018597ba5bd4e9a80d1ae650bf8b)data\_written\_cb

| [usb\_audio\_data\_completion\_cb\_t](usb__audio_8h.md#a57bc8c499f03323db38f5604f8ebcda2) usb\_audio\_ops::data\_written\_cb |
| --- |

Callback called when data were successfully written with sending capable device.

Applicable for headset and microphone. Unused for headphones.

## [◆ ](#a861823185efb5c9a06b900799adb9efb)feature\_update\_cb

| [usb\_audio\_feature\_updated\_cb\_t](usb__audio_8h.md#a692362e834622532b7be71d5e0bdc219) usb\_audio\_ops::feature\_update\_cb |
| --- |

Callback called when features were modified by the Host.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_audio.h](usb__audio_8h_source.md)

- [usb\_audio\_ops](structusb__audio__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
