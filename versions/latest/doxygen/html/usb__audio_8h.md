---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usb__audio_8h.html
original_path: doxygen/html/usb__audio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_audio.h File Reference

USB Audio Device Class public header.
[More...](#details)

`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](usb__audio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usb\_audio\_fu\_evt](structusb__audio__fu__evt.md) |
|  | Feature Unit event structure. [More...](structusb__audio__fu__evt.md#details) |
| struct | [usb\_audio\_ops](structusb__audio__ops.md) |
|  | Audio callbacks used to interact with audio devices by user App. [More...](structusb__audio__ops.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usb\_audio\_data\_request\_cb\_t](#a8f289f2b4d0a7d3accdc6308cb5661e8)) (const struct [device](structdevice.md) \*dev) |
|  | Callback type used to inform the app that data were requested from the device and may be send to the Host. |
| typedef void(\* | [usb\_audio\_data\_completion\_cb\_t](#a57bc8c499f03323db38f5604f8ebcda2)) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Callback type used to inform the app that data were successfully send/received. |
| typedef void(\* | [usb\_audio\_feature\_updated\_cb\_t](#a692362e834622532b7be71d5e0bdc219)) (const struct [device](structdevice.md) \*dev, const struct [usb\_audio\_fu\_evt](structusb__audio__fu__evt.md) \*evt) |
|  | Callback type used to inform the app that Host has changed one of the features configured for the device. |

| Enumerations | |
| --- | --- |
| enum | [usb\_audio\_int\_subclass\_codes](#a4885d280ebe68e42cf068524038ec582) { [USB\_AUDIO\_SUBCLASS\_UNDEFINED](#a4885d280ebe68e42cf068524038ec582aba82b7b28c0ad0ecf125695bd1f35db2) = 0x00 , [USB\_AUDIO\_AUDIOCONTROL](#a4885d280ebe68e42cf068524038ec582aabd72d1d6016fbe1e37788f37c1c8cac) = 0x01 , [USB\_AUDIO\_AUDIOSTREAMING](#a4885d280ebe68e42cf068524038ec582a8f451ebdab0c5a1d930ce5808b6f0892) = 0x02 , [USB\_AUDIO\_MIDISTREAMING](#a4885d280ebe68e42cf068524038ec582a589d9e4883f109f787517a017d6187b2) = 0x03 } |
|  | Audio Interface Subclass Codes. [More...](#a4885d280ebe68e42cf068524038ec582) |
| enum | [usb\_audio\_cs\_ac\_int\_desc\_subtypes](#ab5e6c883af53c089c7fcdee4d2249d9a) {     [USB\_AUDIO\_AC\_DESCRIPTOR\_UNDEFINED](#ab5e6c883af53c089c7fcdee4d2249d9aa2eee02b3652783891eb878bd0a02227d) = 0x00 , [USB\_AUDIO\_HEADER](#ab5e6c883af53c089c7fcdee4d2249d9aa533df0f1df0cd0ba91f05922780c3f51) = 0x01 , [USB\_AUDIO\_INPUT\_TERMINAL](#ab5e6c883af53c089c7fcdee4d2249d9aa80b350d862e1fe02fb04572481ae6343) = 0x02 , [USB\_AUDIO\_OUTPUT\_TERMINAL](#ab5e6c883af53c089c7fcdee4d2249d9aa357c88ef81ee69875f4cbbf5610fd48f) = 0x03 ,     [USB\_AUDIO\_MIXER\_UNIT](#ab5e6c883af53c089c7fcdee4d2249d9aa10f58b16088a3218eb4ed8c31ffd9dfe) = 0x04 , [USB\_AUDIO\_SELECTOR\_UNIT](#ab5e6c883af53c089c7fcdee4d2249d9aab01072ed5bad284a34cf9a2e8b2098e5) = 0x05 , [USB\_AUDIO\_FEATURE\_UNIT](#ab5e6c883af53c089c7fcdee4d2249d9aad06ebbc1c9c35ec35dca8c7bb95c52c7) = 0x06 , [USB\_AUDIO\_PROCESSING\_UNIT](#ab5e6c883af53c089c7fcdee4d2249d9aae5e4af543ede652cda987db1ca5b10ab) = 0x07 ,     [USB\_AUDIO\_EXTENSION\_UNIT](#ab5e6c883af53c089c7fcdee4d2249d9aad1f55fd97d0217453704ba61a7357ca1) = 0x08   } |
|  | Audio Class-Specific AC Interface Descriptor Subtypes. [More...](#ab5e6c883af53c089c7fcdee4d2249d9a) |
| enum | [usb\_audio\_cs\_as\_int\_desc\_subtypes](#ade80a3c7e04049fd27e4e39269baaeeb) { [USB\_AUDIO\_AS\_DESCRIPTOR\_UNDEFINED](#ade80a3c7e04049fd27e4e39269baaeeba6ac0131cbfcbe01e06cde15e6fdb4e5e) = 0x00 , [USB\_AUDIO\_AS\_GENERAL](#ade80a3c7e04049fd27e4e39269baaeeba8cefa4d87a243d6ee01b0c72bc39fe84) = 0x01 , [USB\_AUDIO\_FORMAT\_TYPE](#ade80a3c7e04049fd27e4e39269baaeebab7df49ec3cb5b7a7f19c7f0ec9161de4) = 0x02 , [USB\_AUDIO\_FORMAT\_SPECIFIC](#ade80a3c7e04049fd27e4e39269baaeebada7521b50fd74ef8bfb77485976e0e0a) = 0x03 } |
|  | Audio Class-Specific AS Interface Descriptor Subtypes Refer to Table A-6 from audio10.pdf. [More...](#ade80a3c7e04049fd27e4e39269baaeeb) |
| enum | [usb\_audio\_cs\_req\_codes](#ad6eb1c3ec75aef329ea973d1cb4dc6ad) {     [USB\_AUDIO\_REQUEST\_CODE\_UNDEFINED](#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e5e1dd7fd6292ba8bcc4564223b8220) = 0x00 , [USB\_AUDIO\_SET\_CUR](#ad6eb1c3ec75aef329ea973d1cb4dc6ada1088106727c5c6d850dd2ab98a7b454d) = 0x01 , [USB\_AUDIO\_GET\_CUR](#ad6eb1c3ec75aef329ea973d1cb4dc6ada8d2d8fdf1663f9691f566245062b2cf6) = 0x81 , [USB\_AUDIO\_SET\_MIN](#ad6eb1c3ec75aef329ea973d1cb4dc6ada6f5faa411e92cdeacdc521bd05b4bfab) = 0x02 ,     [USB\_AUDIO\_GET\_MIN](#ad6eb1c3ec75aef329ea973d1cb4dc6ada2e921e391ec9f89345e6b63ad1fd5da6) = 0x82 , [USB\_AUDIO\_SET\_MAX](#ad6eb1c3ec75aef329ea973d1cb4dc6ada96ac36a0735d03e3addf0fe540903707) = 0x03 , [USB\_AUDIO\_GET\_MAX](#ad6eb1c3ec75aef329ea973d1cb4dc6adac027c9e016ad88a9c135a0c1050921bb) = 0x83 , [USB\_AUDIO\_SET\_RES](#ad6eb1c3ec75aef329ea973d1cb4dc6ada1945ba97faeff43f68bd4918be76a4e7) = 0x04 ,     [USB\_AUDIO\_GET\_RES](#ad6eb1c3ec75aef329ea973d1cb4dc6ada4ce3135409f73b58295898087e9ff485) = 0x84 , [USB\_AUDIO\_SET\_MEM](#ad6eb1c3ec75aef329ea973d1cb4dc6adae89a907671d2940da6bb4c58cf9a7fd0) = 0x05 , [USB\_AUDIO\_GET\_MEM](#ad6eb1c3ec75aef329ea973d1cb4dc6ada6e3db81f03ab284c82c254952c3f7259) = 0x85 , [USB\_AUDIO\_GET\_STAT](#ad6eb1c3ec75aef329ea973d1cb4dc6ada229701fae8fdc58a530ffcdd1cdea109) = 0xFF   } |
|  | Audio Class-Specific Request Codes Refer to Table A-9 from audio10.pdf. [More...](#ad6eb1c3ec75aef329ea973d1cb4dc6ad) |
| enum | [usb\_audio\_fucs](#a4d49f239cc36daf8bd0cfa36c5fb75d2) {     [USB\_AUDIO\_FU\_CONTROL\_UNDEFINED](#a4d49f239cc36daf8bd0cfa36c5fb75d2a08d27821af6c7d875351ec8f58082794) = 0x00 , [USB\_AUDIO\_FU\_MUTE\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2adb4f2720ad78a26d22279a45df56b43d) = 0x01 , [USB\_AUDIO\_FU\_VOLUME\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2a6d258289b44ddeb1153168fafb92c0d8) = 0x02 , [USB\_AUDIO\_FU\_BASS\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2a2b14e19e39d96c31764f89128b393efc) = 0x03 ,     [USB\_AUDIO\_FU\_MID\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2acfcc2072d11863eaedb68f87a93eb601) = 0x04 , [USB\_AUDIO\_FU\_TREBLE\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2a657b1e5689be60c2f1ce6d3d2cb68f89) = 0x05 , [USB\_AUDIO\_FU\_GRAPHIC\_EQUALIZER\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2a26c439798671f4efe7b6469f3dcd37c5) = 0x06 , [USB\_AUDIO\_FU\_AUTOMATIC\_GAIN\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2a9e9d8f03326339a9a5e212aad42f984f) = 0x07 ,     [USB\_AUDIO\_FU\_DELAY\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2aef98729fa59119eb0e0cbed2e6a992da) = 0x08 , [USB\_AUDIO\_FU\_BASS\_BOOST\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2a1c23bc45ef27b6acf87da3c68281d2a3) = 0x09 , [USB\_AUDIO\_FU\_LOUDNESS\_CONTROL](#a4d49f239cc36daf8bd0cfa36c5fb75d2adae061d51c1df5d03cc47b7b2c412f1d) = 0x0A   } |
|  | Feature Unit Control Selectors Refer to Table A-11 from audio10.pdf. [More...](#a4d49f239cc36daf8bd0cfa36c5fb75d2) |
| enum | [usb\_audio\_terminal\_types](#ad73e9e9b72475496b6c483f78605e79e) {     [USB\_AUDIO\_USB\_UNDEFINED](#ad73e9e9b72475496b6c483f78605e79eaa0fbe557eba975cb5e368e199ea4f6d4) = 0x0100 , [USB\_AUDIO\_USB\_STREAMING](#ad73e9e9b72475496b6c483f78605e79eaad81dbd6f39554f52c3912755643d661) = 0x0101 , [USB\_AUDIO\_USB\_VENDOR\_SPEC](#ad73e9e9b72475496b6c483f78605e79ea64205001486011d22c1ec0abd382a486) = 0x01FF , [USB\_AUDIO\_IN\_UNDEFINED](#ad73e9e9b72475496b6c483f78605e79eaf85af15795d80c07cdff711ac172be57) = 0x0200 ,     [USB\_AUDIO\_IN\_MICROPHONE](#ad73e9e9b72475496b6c483f78605e79ea699cefac29e9d9c60f53562c7ad7050d) = 0x0201 , [USB\_AUDIO\_IN\_DESKTOP\_MIC](#ad73e9e9b72475496b6c483f78605e79ea3140dd357e3093db21f581226a6b000a) = 0x0202 , [USB\_AUDIO\_IN\_PERSONAL\_MIC](#ad73e9e9b72475496b6c483f78605e79ea3cace6841265454e604513ebba78f749) = 0x0203 , [USB\_AUDIO\_IN\_OM\_DIR\_MIC](#ad73e9e9b72475496b6c483f78605e79ea456a90d55e1b271698516d89e8ba7f5b) = 0x0204 ,     [USB\_AUDIO\_IN\_MIC\_ARRAY](#ad73e9e9b72475496b6c483f78605e79ea2eaf530492705b7e493e5d746752c262) = 0x0205 , [USB\_AUDIO\_IN\_PROC\_MIC\_ARRAY](#ad73e9e9b72475496b6c483f78605e79eac565b3d090c71949c1e1423bb8529c86) = 0x0205 , [USB\_AUDIO\_OUT\_UNDEFINED](#ad73e9e9b72475496b6c483f78605e79ea64f43c7efb785a88f72302d2ad8d00f0) = 0x0300 , [USB\_AUDIO\_OUT\_SPEAKER](#ad73e9e9b72475496b6c483f78605e79ea349881bce5285d61f886aec8fc2bf84c) = 0x0301 ,     [USB\_AUDIO\_OUT\_HEADPHONES](#ad73e9e9b72475496b6c483f78605e79eac551e3ea3e21ddf057062fe7d05b3ec9) = 0x0302 , [USB\_AUDIO\_OUT\_HEAD\_AUDIO](#ad73e9e9b72475496b6c483f78605e79eaed594545b8a4e2c0e0703b4b9d3ebb73) = 0x0303 , [USB\_AUDIO\_OUT\_DESKTOP\_SPEAKER](#ad73e9e9b72475496b6c483f78605e79eacf6fe169bd54e6178dc74bd7c504f795) = 0x0304 , [USB\_AUDIO\_OUT\_ROOM\_SPEAKER](#ad73e9e9b72475496b6c483f78605e79eae6581df62f5da9ab88149ec8049d7213) = 0x0305 ,     [USB\_AUDIO\_OUT\_COMM\_SPEAKER](#ad73e9e9b72475496b6c483f78605e79eaff9805f63bd75e000dd08652c6dc913b) = 0x0306 , [USB\_AUDIO\_OUT\_LOW\_FREQ\_SPEAKER](#ad73e9e9b72475496b6c483f78605e79ea8b48c4993389b7f5a08d55b68b924480) = 0x0307 , [USB\_AUDIO\_IO\_UNDEFINED](#ad73e9e9b72475496b6c483f78605e79eac740f1b3cfcfba8c4def54e1ca81a3d8) = 0x0400 , [USB\_AUDIO\_IO\_HANDSET](#ad73e9e9b72475496b6c483f78605e79ea24f6c5657c301871089dc8eac3b5d207) = 0x0401 ,     [USB\_AUDIO\_IO\_HEADSET](#ad73e9e9b72475496b6c483f78605e79eaf75bca3db10d28611a9ffa8637a4488e) = 0x0402 , [USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_NONE](#ad73e9e9b72475496b6c483f78605e79ea232edf193a4f755d8821c51001d11f1d) = 0x0403 , [USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_SUP](#ad73e9e9b72475496b6c483f78605e79eab7f8515fb0154f5b0e038f485bdadaf6) = 0x0404 , [USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_CAN](#ad73e9e9b72475496b6c483f78605e79ea319eef3f2a59242b0c8dd5ca50212e14) = 0x0405   } |
|  | USB Terminal Types Refer to Table 2-1 - Table 2-4 from termt10.pdf. [More...](#ad73e9e9b72475496b6c483f78605e79e) |
| enum | [usb\_audio\_direction](#acbdc8b284d108983fb204cbd679043bb) { [USB\_AUDIO\_IN](#acbdc8b284d108983fb204cbd679043bbab2ce7b1140be0d960ab2754bc8e262dd) = 0x00 , [USB\_AUDIO\_OUT](#acbdc8b284d108983fb204cbd679043bba0f0e91f9580d03853432259d74f108ba) = 0x01 } |
|  | Audio device direction. [More...](#acbdc8b284d108983fb204cbd679043bb) |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [usb\_audio\_get\_in\_frame\_size](#af314d5beb1d16377855313d46148a86c) (const struct [device](structdevice.md) \*dev) |
|  | Get the frame size that is accepted by the Host. |
| void | [usb\_audio\_register](#a6a69824dadab0c36bb6a6ce378da8ba5) (const struct [device](structdevice.md) \*dev, const struct [usb\_audio\_ops](structusb__audio__ops.md) \*ops) |
|  | Register the USB Audio device and make it usable. |
| int | [usb\_audio\_send](#af1874c929638325e9e2a44da0e613041) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data using USB Audio device. |

## Detailed Description

USB Audio Device Class public header.

Header follows below documentation:

- USB Device Class Definition for Audio Devices (audio10.pdf)

Additional documentation considered a part of USB Audio v1.0:

- USB Device Class Definition for Audio Data Formats (frmts10.pdf)
- USB Device Class Definition for Terminal Types (termt10.pdf)

## Typedef Documentation

## [◆ ](#a57bc8c499f03323db38f5604f8ebcda2)usb\_audio\_data\_completion\_cb\_t

| typedef void(\* usb\_audio\_data\_completion\_cb\_t) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

Callback type used to inform the app that data were successfully send/received.

Parameters
:   | dev | The device for which the callback was called. |
    | --- | --- |
    | buffer | Pointer to the [net\_buf](structnet__buf.md "Network buffer representation.") data chunk that was successfully send/received. If the application uses data\_written\_cb and/or data\_received\_cb callbacks it is responsible for freeing the buffer by itself. |
    | size | Amount of data that were successfully send/received. |

## [◆ ](#a8f289f2b4d0a7d3accdc6308cb5661e8)usb\_audio\_data\_request\_cb\_t

| typedef void(\* usb\_audio\_data\_request\_cb\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

Callback type used to inform the app that data were requested from the device and may be send to the Host.

For sending the data [usb\_audio\_send()](#af1874c929638325e9e2a44da0e613041) API function should be used.

Note
:   User may not use this callback and may try to send in 1ms task instead. Sending every 1ms may be unsuccessful and may return -EAGAIN if Host did not required data.

Parameters
:   | dev | The device for which data were requested by the Host. |
    | --- | --- |

## [◆ ](#a692362e834622532b7be71d5e0bdc219)usb\_audio\_feature\_updated\_cb\_t

| typedef void(\* usb\_audio\_feature\_updated\_cb\_t) (const struct [device](structdevice.md) \*dev, const struct [usb\_audio\_fu\_evt](structusb__audio__fu__evt.md) \*evt) |
| --- |

Callback type used to inform the app that Host has changed one of the features configured for the device.

Applicable for all devices.

Warning
:   Host may not use all of configured features.

Parameters
:   | dev | USB Audio device |
    | --- | --- |
    | evt | Pointer to an event to be parsed by the App. Pointer struct is temporary and is valid only during the execution of this callback. |

## Enumeration Type Documentation

## [◆ ](#ab5e6c883af53c089c7fcdee4d2249d9a)usb\_audio\_cs\_ac\_int\_desc\_subtypes

| enum [usb\_audio\_cs\_ac\_int\_desc\_subtypes](#ab5e6c883af53c089c7fcdee4d2249d9a) |
| --- |

Audio Class-Specific AC Interface Descriptor Subtypes.

Refer to Table A-5 from audio10.pdf

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_AC\_DESCRIPTOR\_UNDEFINED |  |
| USB\_AUDIO\_HEADER |  |
| USB\_AUDIO\_INPUT\_TERMINAL |  |
| USB\_AUDIO\_OUTPUT\_TERMINAL |  |
| USB\_AUDIO\_MIXER\_UNIT |  |
| USB\_AUDIO\_SELECTOR\_UNIT |  |
| USB\_AUDIO\_FEATURE\_UNIT |  |
| USB\_AUDIO\_PROCESSING\_UNIT |  |
| USB\_AUDIO\_EXTENSION\_UNIT |  |

## [◆ ](#ade80a3c7e04049fd27e4e39269baaeeb)usb\_audio\_cs\_as\_int\_desc\_subtypes

| enum [usb\_audio\_cs\_as\_int\_desc\_subtypes](#ade80a3c7e04049fd27e4e39269baaeeb) |
| --- |

Audio Class-Specific AS Interface Descriptor Subtypes Refer to Table A-6 from audio10.pdf.

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_AS\_DESCRIPTOR\_UNDEFINED |  |
| USB\_AUDIO\_AS\_GENERAL |  |
| USB\_AUDIO\_FORMAT\_TYPE |  |
| USB\_AUDIO\_FORMAT\_SPECIFIC |  |

## [◆ ](#ad6eb1c3ec75aef329ea973d1cb4dc6ad)usb\_audio\_cs\_req\_codes

| enum [usb\_audio\_cs\_req\_codes](#ad6eb1c3ec75aef329ea973d1cb4dc6ad) |
| --- |

Audio Class-Specific Request Codes Refer to Table A-9 from audio10.pdf.

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_REQUEST\_CODE\_UNDEFINED |  |
| USB\_AUDIO\_SET\_CUR |  |
| USB\_AUDIO\_GET\_CUR |  |
| USB\_AUDIO\_SET\_MIN |  |
| USB\_AUDIO\_GET\_MIN |  |
| USB\_AUDIO\_SET\_MAX |  |
| USB\_AUDIO\_GET\_MAX |  |
| USB\_AUDIO\_SET\_RES |  |
| USB\_AUDIO\_GET\_RES |  |
| USB\_AUDIO\_SET\_MEM |  |
| USB\_AUDIO\_GET\_MEM |  |
| USB\_AUDIO\_GET\_STAT |  |

## [◆ ](#acbdc8b284d108983fb204cbd679043bb)usb\_audio\_direction

| enum [usb\_audio\_direction](#acbdc8b284d108983fb204cbd679043bb) |
| --- |

Audio device direction.

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_IN |  |
| USB\_AUDIO\_OUT |  |

## [◆ ](#a4d49f239cc36daf8bd0cfa36c5fb75d2)usb\_audio\_fucs

| enum [usb\_audio\_fucs](#a4d49f239cc36daf8bd0cfa36c5fb75d2) |
| --- |

Feature Unit Control Selectors Refer to Table A-11 from audio10.pdf.

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_FU\_CONTROL\_UNDEFINED |  |
| USB\_AUDIO\_FU\_MUTE\_CONTROL |  |
| USB\_AUDIO\_FU\_VOLUME\_CONTROL |  |
| USB\_AUDIO\_FU\_BASS\_CONTROL |  |
| USB\_AUDIO\_FU\_MID\_CONTROL |  |
| USB\_AUDIO\_FU\_TREBLE\_CONTROL |  |
| USB\_AUDIO\_FU\_GRAPHIC\_EQUALIZER\_CONTROL |  |
| USB\_AUDIO\_FU\_AUTOMATIC\_GAIN\_CONTROL |  |
| USB\_AUDIO\_FU\_DELAY\_CONTROL |  |
| USB\_AUDIO\_FU\_BASS\_BOOST\_CONTROL |  |
| USB\_AUDIO\_FU\_LOUDNESS\_CONTROL |  |

## [◆ ](#a4885d280ebe68e42cf068524038ec582)usb\_audio\_int\_subclass\_codes

| enum [usb\_audio\_int\_subclass\_codes](#a4885d280ebe68e42cf068524038ec582) |
| --- |

Audio Interface Subclass Codes.

Refer to Table A-2 from audio10.pdf

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_SUBCLASS\_UNDEFINED |  |
| USB\_AUDIO\_AUDIOCONTROL |  |
| USB\_AUDIO\_AUDIOSTREAMING |  |
| USB\_AUDIO\_MIDISTREAMING |  |

## [◆ ](#ad73e9e9b72475496b6c483f78605e79e)usb\_audio\_terminal\_types

| enum [usb\_audio\_terminal\_types](#ad73e9e9b72475496b6c483f78605e79e) |
| --- |

USB Terminal Types Refer to Table 2-1 - Table 2-4 from termt10.pdf.

| Enumerator | |
| --- | --- |
| USB\_AUDIO\_USB\_UNDEFINED | USB undefined. |
| USB\_AUDIO\_USB\_STREAMING | USB streaming. |
| USB\_AUDIO\_USB\_VENDOR\_SPEC | USB vendor specific. |
| USB\_AUDIO\_IN\_UNDEFINED | Input undefined. |
| USB\_AUDIO\_IN\_MICROPHONE | Microphone. |
| USB\_AUDIO\_IN\_DESKTOP\_MIC | Desktop microphone. |
| USB\_AUDIO\_IN\_PERSONAL\_MIC | Personal microphone. |
| USB\_AUDIO\_IN\_OM\_DIR\_MIC | Omni directional microphone. |
| USB\_AUDIO\_IN\_MIC\_ARRAY | Microphone array. |
| USB\_AUDIO\_IN\_PROC\_MIC\_ARRAY | Processing microphone array. |
| USB\_AUDIO\_OUT\_UNDEFINED | Output undefined. |
| USB\_AUDIO\_OUT\_SPEAKER | Speaker. |
| USB\_AUDIO\_OUT\_HEADPHONES | Headphones. |
| USB\_AUDIO\_OUT\_HEAD\_AUDIO | Head mounted display audio. |
| USB\_AUDIO\_OUT\_DESKTOP\_SPEAKER | Desktop speaker. |
| USB\_AUDIO\_OUT\_ROOM\_SPEAKER | Room speaker. |
| USB\_AUDIO\_OUT\_COMM\_SPEAKER | Communication speaker. |
| USB\_AUDIO\_OUT\_LOW\_FREQ\_SPEAKER | Low frequency effects speaker. |
| USB\_AUDIO\_IO\_UNDEFINED | Bidirectional undefined. |
| USB\_AUDIO\_IO\_HANDSET | Handset. |
| USB\_AUDIO\_IO\_HEADSET | Headset. |
| USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_NONE | Speakerphone, no echo reduction. |
| USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_SUP | Speakerphone, echo reduction. |
| USB\_AUDIO\_IO\_SPEAKERPHONE\_ECHO\_CAN | Speakerphone, echo cancellation. |

## Function Documentation

## [◆ ](#af314d5beb1d16377855313d46148a86c)usb\_audio\_get\_in\_frame\_size()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) usb\_audio\_get\_in\_frame\_size | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the frame size that is accepted by the Host.

This function returns the frame size for Input Devices that is expected by the Host. Returned value rely on Input Device configuration:

- number of channels
- sampling frequency
- sample resolution Device configuration is done via DT overlay.

Parameters
:   | dev | The Input device that is asked for frame size. |
    | --- | --- |

Warning
:   Do not use with OUT only devices (Headphones). For OUT only devices this function shall return 0.

## [◆ ](#a6a69824dadab0c36bb6a6ce378da8ba5)usb\_audio\_register()

| void usb\_audio\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [usb\_audio\_ops](structusb__audio__ops.md) \* | *ops* ) |

Register the USB Audio device and make it usable.

This must be called in order to make the device work and respond to all relevant requests.

Parameters
:   | dev | USB Audio device |
    | --- | --- |
    | ops | USB audio callback structure. Callback are used to inform the user about what is happening |

## [◆ ](#af1874c929638325e9e2a44da0e613041)usb\_audio\_send()

| int usb\_audio\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

Send data using USB Audio device.

Parameters
:   | dev | USB Audio device which will send the data over its ISO IN endpoint |
    | --- | --- |
    | buffer | Pointer to the buffer that should be send. User is responsible for managing the buffer for Input devices. In case of sending error user must decide if the buffer should be dropped or retransmitted. After the buffer was sent successfully it is passed to the data\_written\_cb callback if the application uses one or automatically freed otherwise. User must provide proper [net\_buf](structnet__buf.md "Network buffer representation.") chunk especially when it comes to its size. This information can be obtained using [usb\_audio\_get\_in\_frame\_size()](#af314d5beb1d16377855313d46148a86c) API function. |
    | len | Length of the data to be send |

Returns
:   0 on success, negative error on fail

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_audio.h](usb__audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
