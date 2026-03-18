---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structusb__audio__fu__evt.html
original_path: doxygen/html/structusb__audio__fu__evt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_audio\_fu\_evt Struct Reference

Feature Unit event structure.
[More...](#details)

`#include <[usb_audio.h](usb__audio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [usb\_audio\_direction](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bb) | [dir](#a5baf5d4e2a39337dc9c21c4465d5ad8e) |
|  | The device direction that has been changed. |
| enum [usb\_audio\_fucs](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2) | [cs](#a1cb4849aae8b9a4e667ed126e9bce26b) |
|  | Control selector feature that has been changed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel](#a9313b39f178c8a86d680a950ce505713) |
|  | Device channel that has been changed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [val\_len](#a6ef19bf7d37c3d636edba243dac8ecb2) |
|  | Length of the val field. |
| const void \* | [val](#a47c6c7c00fac32a04bffd251d715dc39) |
|  | Value of the feature that has been set. |

## Detailed Description

Feature Unit event structure.

The event structure is used by feature\_update\_cb in order to inform the App whenever the Host has modified one of the device features.

## Field Documentation

## [◆ ](#a9313b39f178c8a86d680a950ce505713)channel

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_audio\_fu\_evt::channel |
| --- |

Device channel that has been changed.

If 0xFF, then all channels have been changed.

## [◆ ](#a1cb4849aae8b9a4e667ed126e9bce26b)cs

| enum [usb\_audio\_fucs](usb__audio_8h.md#a4d49f239cc36daf8bd0cfa36c5fb75d2) usb\_audio\_fu\_evt::cs |
| --- |

Control selector feature that has been changed.

## [◆ ](#a5baf5d4e2a39337dc9c21c4465d5ad8e)dir

| enum [usb\_audio\_direction](usb__audio_8h.md#acbdc8b284d108983fb204cbd679043bb) usb\_audio\_fu\_evt::dir |
| --- |

The device direction that has been changed.

Applicable for Headset device only.

## [◆ ](#a47c6c7c00fac32a04bffd251d715dc39)val

| const void\* usb\_audio\_fu\_evt::val |
| --- |

Value of the feature that has been set.

## [◆ ](#a6ef19bf7d37c3d636edba243dac8ecb2)val\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_audio\_fu\_evt::val\_len |
| --- |

Length of the val field.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/class/[usb\_audio.h](usb__audio_8h_source.md)

- [usb\_audio\_fu\_evt](structusb__audio__fu__evt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
