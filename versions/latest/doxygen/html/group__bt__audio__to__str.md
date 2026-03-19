---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__audio__to__str.html
original_path: doxygen/html/group__bt__audio__to__str.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Assigned numbers to string API

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Assigned numbers to string API.
[More...](#details)

| Functions | |
| --- | --- |
| static char \* | [bt\_audio\_context\_bit\_to\_str](#ga26436fc678423ff1cf3543d381359d0f) (enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) context) |
|  | Returns a string representation of a specific [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3 "bt_audio_context") bit. |
| static char \* | [bt\_audio\_parental\_rating\_to\_str](#ga6926c4e8bda0874769177a903276c072) (enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating) |
|  | Returns a string representation of a [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760 "bt_audio_parental_rating") value. |
| static char \* | [bt\_audio\_active\_state\_to\_str](#ga1dd5865429e2438e0d4f88e891eda975) (enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Returns a string representation of a [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f "bt_audio_active_state") value. |
| static char \* | [bt\_audio\_codec\_cap\_freq\_bit\_to\_str](#gadd3bac4f1f1b334cb60f5783fdc15c14) (enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq) |
|  | Returns a string representation of a specific [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4 "bt_audio_codec_cap_freq") bit. |
| static char \* | [bt\_audio\_codec\_cap\_frame\_dur\_bit\_to\_str](#ga6b9cc74dafcf03056862ae9823bce58d) (enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur) |
|  | Returns a string representation of a specific [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5 "bt_audio_codec_cap_frame_dur") bit. |
| static char \* | [bt\_audio\_codec\_cap\_chan\_count\_bit\_to\_str](#ga795742ed8d91e2b675fbcdaeee7a71ec) (enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count) |
|  | Returns a string representation of a specific [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5 "bt_audio_codec_cap_chan_count") bit. |
| static char \* | [bt\_audio\_location\_bit\_to\_str](#gaa1b9f7166fd6e6797da65d9537357324) (enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location) |
|  | Returns a string representation of a specific [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location") bit. |

## Detailed Description

Assigned numbers to string API.

Functions to return string representation of Bluetooth Audio assigned number values.

## Function Documentation

## [◆ ](#ga1dd5865429e2438e0d4f88e891eda975)bt\_audio\_active\_state\_to\_str()

| | char \* bt\_audio\_active\_state\_to\_str | ( | enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) | *state* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f "bt_audio_active_state") value.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The active state value |
    | --- | --- |

Returns
:   String representation of the supplied active state value

## [◆ ](#ga795742ed8d91e2b675fbcdaeee7a71ec)bt\_audio\_codec\_cap\_chan\_count\_bit\_to\_str()

| | char \* bt\_audio\_codec\_cap\_chan\_count\_bit\_to\_str | ( | enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) | *chan\_count* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a specific [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5 "bt_audio_codec_cap_chan_count") bit.

If `chan_count` contains multiple bits, it will return "Unknown channel count"

Parameters
:   | chan\_count | A single frame channel count bit |
    | --- | --- |

Returns
:   String representation of the supplied bit

## [◆ ](#ga6b9cc74dafcf03056862ae9823bce58d)bt\_audio\_codec\_cap\_frame\_dur\_bit\_to\_str()

| | char \* bt\_audio\_codec\_cap\_frame\_dur\_bit\_to\_str | ( | enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) | *frame\_dur* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a specific [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5 "bt_audio_codec_cap_frame_dur") bit.

If `frame_dur` contains multiple bits, it will return "Unknown frame duration"

Parameters
:   | frame\_dur | A single frame duration bit |
    | --- | --- |

Returns
:   String representation of the supplied bit

## [◆ ](#gadd3bac4f1f1b334cb60f5783fdc15c14)bt\_audio\_codec\_cap\_freq\_bit\_to\_str()

| | char \* bt\_audio\_codec\_cap\_freq\_bit\_to\_str | ( | enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) | *freq* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a specific [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4 "bt_audio_codec_cap_freq") bit.

If `freq` contains multiple bits, it will return "Unknown supported frequency"

Parameters
:   | freq | A single frequency bit |
    | --- | --- |

Returns
:   String representation of the supplied bit

## [◆ ](#ga26436fc678423ff1cf3543d381359d0f)bt\_audio\_context\_bit\_to\_str()

| | char \* bt\_audio\_context\_bit\_to\_str | ( | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *context* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a specific [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3 "bt_audio_context") bit.

If `context` contains multiple bits, it will return "Unknown context"

Parameters
:   | context | A single context bit |
    | --- | --- |

Returns
:   String representation of the supplied bit

## [◆ ](#gaa1b9f7166fd6e6797da65d9537357324)bt\_audio\_location\_bit\_to\_str()

| | char \* bt\_audio\_location\_bit\_to\_str | ( | enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) | *location* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a specific [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8 "bt_audio_location") bit.

If `location` contains multiple bits, it will return "Unknown location"

Parameters
:   | location | A single location bit |
    | --- | --- |

Returns
:   String representation of the supplied bit

## [◆ ](#ga6926c4e8bda0874769177a903276c072)bt\_audio\_parental\_rating\_to\_str()

| | char \* bt\_audio\_parental\_rating\_to\_str | ( | enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) | *parental\_rating* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[audio.h](bluetooth_2audio_2audio_8h.md)>`

Returns a string representation of a [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760 "bt_audio_parental_rating") value.

Parameters
:   | parental\_rating | The parental rating value |
    | --- | --- |

Returns
:   String representation of the supplied parental rating value

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
