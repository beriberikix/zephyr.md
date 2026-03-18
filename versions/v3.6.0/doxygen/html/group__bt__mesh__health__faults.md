---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__health__faults.html
original_path: doxygen/html/group__bt__mesh__health__faults.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Health faults

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

List of specification defined Health fault values.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_HEALTH\_FAULT\_NO\_FAULT](#ga5fe6993bb219f6547b67e6720f7bf526)   0x00 |
|  | No fault has occurred. |
| #define | [BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_WARNING](#gaa75f0a4d758476e2fdeaa94b1ad98b55)   0x01 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_ERROR](#gaaa682f49f35e6764af0429690aebf20e)   0x02 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_WARNING](#ga0a77dbd3aa3bddeab0cbcf434d36f791)   0x03 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_ERROR](#gab64bbf32cda9d9cd8e82a05f7c9924a1)   0x04 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_WARNING](#ga7838991d14a19ef401a41d96bec76287)   0x05 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_ERROR](#ga86d34960a167c0c3f8a1f320d1843702)   0x06 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_WARNING](#ga326ce2242e409c9577d324388509b7b7)   0x07 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_ERROR](#gaf1fff982760290c80424b87a60bff822)   0x08 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_WARNING](#gab92ab13dbc9799476e6e627a81080e14)   0x09 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_ERROR](#ga29b5e94269715a8301bc363cb66db370)   0x0A |
| #define | [BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_WARNING](#gacd14cc12794077cc517d5fefa748c9c6)   0x0B |
| #define | [BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_ERROR](#gafafa715a04011e80944199d93ee6c51b)   0x0C |
| #define | [BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_WARNING](#gac737fc53f2184bd1664f0da5388148ac)   0x0D |
| #define | [BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_ERROR](#ga1c47ccb73f94cee4db7d300679972300)   0x0E |
| #define | [BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_WARNING](#ga95fd40c6066a37417ebfc9916b06db7c)   0x0F |
| #define | [BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_ERROR](#ga3da2c495908e3b4aac524e5d91c58189)   0x10 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_WARNING](#ga7fb07118fea783803bfa8f419441740f)   0x11 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_ERROR](#ga1b9f51d2760530bc170a81ff29435cf3)   0x12 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_WARNING](#ga4e46ae0ebd52722c1600f2025a2fb190)   0x13 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_ERROR](#ga03ee761cb0a2d5cbf3509a719e658621)   0x14 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_WARNING](#ga0e50ab22bffb357f02acf4860664d535)   0x15 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_ERROR](#gaa612dbc60cc9ab0fe4978a0992499009)   0x16 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_MEMORY\_WARNING](#gabf766439091f937438a0e736ddc892b4)   0x17 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_MEMORY\_ERROR](#ga358d3351b1935b3a4c259060902033db)   0x18 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_WARNING](#ga8d60f38c1560c269fdfd18de35daf5d6)   0x19 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_ERROR](#ga75214891137e1045bcc83c4c54458e77)   0x1A |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_WARNING](#ga124bb981c3ab2c41eda2ddf3bc85b5f2)   0x1B |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_ERROR](#ga33c5b4f773c6afe73f64a14411033b3f)   0x1C |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_WARNING](#gae3c188075202eeff7292ab56e03e31a9)   0x1D |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_ERROR](#gad42b0f690836deae1dcbb4757e885c02)   0x1E |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_WARNING](#ga5a1ba1561e93574e0d4598bd90c386b8)   0x1F |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_ERROR](#ga3789605186fe9c172d3320a22a21ead6)   0x20 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_WARNING](#gaf51ad764a78b425cda29720c4e063221)   0x21 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_ERROR](#ga0493f52939a375fcebe33d45451b618c)   0x22 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_WARNING](#ga03cfae918863f10dd5aaab6fd3a82b07)   0x23 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_ERROR](#ga7308395342cc226ef17584aebfa78d2c)   0x24 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_TAMPER\_WARNING](#ga66d4e92380a42b0491848a261a36246b)   0x25 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_TAMPER\_ERROR](#ga69b7755dd511f30864272ad1465f2965)   0x26 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_WARNING](#ga1494db7b9a0fbab15119a65da0b6b0d0)   0x27 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_ERROR](#ga482eb25cfcfd943342f8d30ed976bc24)   0x28 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_WARNING](#ga7f158981cf1282acaca0839244e3c6cb)   0x29 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_ERROR](#ga2d0909640905067168ba45bea0523618)   0x2A |
| #define | [BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_WARNING](#ga95d30649750b543650c3a21cc8719c3e)   0x2B |
| #define | [BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_ERROR](#ga63b9b85427e0efa31e8a1496065b3dc9)   0x2C |
| #define | [BT\_MESH\_HEALTH\_FAULT\_EMPTY\_WARNING](#gada2400efbf70229ce8328a9ace7fcccf)   0x2D |
| #define | [BT\_MESH\_HEALTH\_FAULT\_EMPTY\_ERROR](#ga0b0414621784d1a3c872077e0b578d0d)   0x2E |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_WARNING](#ga534b85b4f805b585c4c4d29e6abe782a)   0x2F |
| #define | [BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_ERROR](#ga54b4657666c01dca9417d58e302ff738)   0x30 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_WARNING](#gae1113f6fcaae95b1a7cfe2dd95c287ab)   0x31 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_ERROR](#gaa6ccb4569d63b6eb0dc53ec7211f2f98)   0x32 |
| #define | [BT\_MESH\_HEALTH\_FAULT\_VENDOR\_SPECIFIC\_START](#gae0b8ecef9c11e17a02ede6a4b416c3b8)   0x80 |
|  | Start of the vendor specific fault values. |

## Detailed Description

List of specification defined Health fault values.

## Macro Definition Documentation

## [◆ ](#ga0493f52939a375fcebe33d45451b618c)BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_ERROR   0x22 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gaf51ad764a78b425cda29720c4e063221)BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_WARNING   0x21 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gaaa682f49f35e6764af0429690aebf20e)BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_ERROR   0x02 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gaa75f0a4d758476e2fdeaa94b1ad98b55)BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_WARNING   0x01 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga3da2c495908e3b4aac524e5d91c58189)BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_ERROR   0x10 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga95fd40c6066a37417ebfc9916b06db7c)BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_WARNING   0x0F |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga03ee761cb0a2d5cbf3509a719e658621)BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_ERROR   0x14 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga4e46ae0ebd52722c1600f2025a2fb190)BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_WARNING   0x13 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga2d0909640905067168ba45bea0523618)BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_ERROR   0x2A |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga7f158981cf1282acaca0839244e3c6cb)BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_WARNING   0x29 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga482eb25cfcfd943342f8d30ed976bc24)BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_ERROR   0x28 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga1494db7b9a0fbab15119a65da0b6b0d0)BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_WARNING   0x27 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gaa612dbc60cc9ab0fe4978a0992499009)BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_ERROR   0x16 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga0e50ab22bffb357f02acf4860664d535)BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_WARNING   0x15 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga0b0414621784d1a3c872077e0b578d0d)BT\_MESH\_HEALTH\_FAULT\_EMPTY\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_EMPTY\_ERROR   0x2E |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gada2400efbf70229ce8328a9ace7fcccf)BT\_MESH\_HEALTH\_FAULT\_EMPTY\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_EMPTY\_WARNING   0x2D |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga7308395342cc226ef17584aebfa78d2c)BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_ERROR   0x24 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga03cfae918863f10dd5aaab6fd3a82b07)BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_WARNING   0x23 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga3789605186fe9c172d3320a22a21ead6)BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_ERROR   0x20 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga5a1ba1561e93574e0d4598bd90c386b8)BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_WARNING   0x1F |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gad42b0f690836deae1dcbb4757e885c02)BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_ERROR   0x1E |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gae3c188075202eeff7292ab56e03e31a9)BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_WARNING   0x1D |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga33c5b4f773c6afe73f64a14411033b3f)BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_ERROR   0x1C |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga124bb981c3ab2c41eda2ddf3bc85b5f2)BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_WARNING   0x1B |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga54b4657666c01dca9417d58e302ff738)BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_ERROR   0x30 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga534b85b4f805b585c4c4d29e6abe782a)BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_WARNING   0x2F |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gaa6ccb4569d63b6eb0dc53ec7211f2f98)BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_ERROR   0x32 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gae1113f6fcaae95b1a7cfe2dd95c287ab)BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_WARNING   0x31 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga358d3351b1935b3a4c259060902033db)BT\_MESH\_HEALTH\_FAULT\_MEMORY\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_MEMORY\_ERROR   0x18 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gabf766439091f937438a0e736ddc892b4)BT\_MESH\_HEALTH\_FAULT\_MEMORY\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_MEMORY\_WARNING   0x17 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga5fe6993bb219f6547b67e6720f7bf526)BT\_MESH\_HEALTH\_FAULT\_NO\_FAULT

| #define BT\_MESH\_HEALTH\_FAULT\_NO\_FAULT   0x00 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

No fault has occurred.

## [◆ ](#ga29b5e94269715a8301bc363cb66db370)BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_ERROR   0x0A |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gab92ab13dbc9799476e6e627a81080e14)BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_WARNING   0x09 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga63b9b85427e0efa31e8a1496065b3dc9)BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_ERROR   0x2C |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga95d30649750b543650c3a21cc8719c3e)BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_WARNING   0x2B |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga1c47ccb73f94cee4db7d300679972300)BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_ERROR   0x0E |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gac737fc53f2184bd1664f0da5388148ac)BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_WARNING   0x0D |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gafafa715a04011e80944199d93ee6c51b)BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_ERROR   0x0C |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gacd14cc12794077cc517d5fefa748c9c6)BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_WARNING   0x0B |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gaf1fff982760290c80424b87a60bff822)BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_ERROR   0x08 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga326ce2242e409c9577d324388509b7b7)BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_WARNING   0x07 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga75214891137e1045bcc83c4c54458e77)BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_ERROR   0x1A |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga8d60f38c1560c269fdfd18de35daf5d6)BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_WARNING   0x19 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga86d34960a167c0c3f8a1f320d1843702)BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_ERROR   0x06 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga7838991d14a19ef401a41d96bec76287)BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_WARNING   0x05 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gab64bbf32cda9d9cd8e82a05f7c9924a1)BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_ERROR   0x04 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga0a77dbd3aa3bddeab0cbcf434d36f791)BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_WARNING   0x03 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga69b7755dd511f30864272ad1465f2965)BT\_MESH\_HEALTH\_FAULT\_TAMPER\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_TAMPER\_ERROR   0x26 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga66d4e92380a42b0491848a261a36246b)BT\_MESH\_HEALTH\_FAULT\_TAMPER\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_TAMPER\_WARNING   0x25 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#gae0b8ecef9c11e17a02ede6a4b416c3b8)BT\_MESH\_HEALTH\_FAULT\_VENDOR\_SPECIFIC\_START

| #define BT\_MESH\_HEALTH\_FAULT\_VENDOR\_SPECIFIC\_START   0x80 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

Start of the vendor specific fault values.

All values below this are reserved for the Bluetooth Specification.

## [◆ ](#ga1b9f51d2760530bc170a81ff29435cf3)BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_ERROR

| #define BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_ERROR   0x12 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

## [◆ ](#ga7fb07118fea783803bfa8f419441740f)BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_WARNING

| #define BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_WARNING   0x11 |
| --- |

`#include <[health_faults.h](health__faults_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
