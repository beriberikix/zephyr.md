---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/comparator_2mcux__acmp_8h.html
original_path: doxygen/html/comparator_2mcux__acmp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_acmp.h File Reference

`#include <[zephyr/drivers/comparator.h](comparator_8h_source.md)>`

[Go to the source code of this file.](comparator_2mcux__acmp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [comp\_mcux\_acmp\_mode\_config](structcomp__mcux__acmp__mode__config.md) |
| struct | [comp\_mcux\_acmp\_input\_config](structcomp__mcux__acmp__input__config.md) |
| struct | [comp\_mcux\_acmp\_filter\_config](structcomp__mcux__acmp__filter__config.md) |
| struct | [comp\_mcux\_acmp\_dac\_config](structcomp__mcux__acmp__dac__config.md) |
| struct | [comp\_mcux\_acmp\_dm\_config](structcomp__mcux__acmp__dm__config.md) |

| Enumerations | |
| --- | --- |
| enum | [comp\_mcux\_acmp\_offset\_mode](#a0aa19032738a4896dfa965c768e80d1a) { [COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL0](#a0aa19032738a4896dfa965c768e80d1aa4875ab09cf32c9efb7ef6ff0a50b4dcb) = 0 , [COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL1](#a0aa19032738a4896dfa965c768e80d1aa42db178d2cd8011dbb9268ba9f68fa28) } |
| enum | [comp\_mcux\_acmp\_hysteresis\_mode](#adc9b7e82b83503bcd3ba4038873f61e4) { [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL0](#adc9b7e82b83503bcd3ba4038873f61e4a32511e4b00c2ebd8d94274d23b0ab68c) = 0 , [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL1](#adc9b7e82b83503bcd3ba4038873f61e4ab030cc0482444fd9708cca879856f505) , [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL2](#adc9b7e82b83503bcd3ba4038873f61e4a416170b9857dbd7facb4ec2c47c93309) , [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL3](#adc9b7e82b83503bcd3ba4038873f61e4a2142add933ef4ec6a1184579d3ee1a10) } |
| enum | [comp\_mcux\_acmp\_mux\_input](#a0492419f3fd81bc5f773b688070eb5d3) {     [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN0](#a0492419f3fd81bc5f773b688070eb5d3ae66ddfcc7428df449f77d7403d854aed) = 0 , [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN1](#a0492419f3fd81bc5f773b688070eb5d3a222a536a9d0d358f151beea3c5dca85a) , [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN2](#a0492419f3fd81bc5f773b688070eb5d3ad93a4f7606dab63cb5c038e47c4057d6) , [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN3](#a0492419f3fd81bc5f773b688070eb5d3ac72c54e0e564773dfe5c1d610f92e044) ,     [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN4](#a0492419f3fd81bc5f773b688070eb5d3a080e839262220380b90e63ce2e5aded7) , [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN5](#a0492419f3fd81bc5f773b688070eb5d3a3f8ae7b0222bac88917784df2db230bb) , [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN6](#a0492419f3fd81bc5f773b688070eb5d3a4b0a916f650db858811f1a380021010a) , [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN7](#a0492419f3fd81bc5f773b688070eb5d3aac0f390fe34f46986c7b1b8e46bc7edc)   } |
| enum | [comp\_mcux\_acmp\_port\_input](#a0c4dda8b42ee7358c269ee0758ca2619) { [COMP\_MCUX\_ACMP\_PORT\_INPUT\_DAC](#a0c4dda8b42ee7358c269ee0758ca2619a6bd5cb01f180608522b85b19dab13eba) = 0 , [COMP\_MCUX\_ACMP\_PORT\_INPUT\_MUX](#a0c4dda8b42ee7358c269ee0758ca2619a4cf0087765eecb5e90a96d0f8a171fdb) } |
| enum | [comp\_mcux\_acmp\_dac\_vref\_source](#adee95c9485e970d2eb5659b539e25622) { [COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN1](#adee95c9485e970d2eb5659b539e25622a41fbf3bf10d813c3ef7f1a55217efba8) = 0 , [COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN2](#adee95c9485e970d2eb5659b539e25622ad25d18fdef06d865b974323ed26144dc) } |
| enum | [comp\_mcux\_acmp\_dm\_clock](#af46bc66f0da831b473d8cd5a89d95016) { [COMP\_MCUX\_ACMP\_DM\_CLOCK\_SLOW](#af46bc66f0da831b473d8cd5a89d95016ae92b237fa2ef27ce8b3d05103d5ed0f8) = 0 , [COMP\_MCUX\_ACMP\_DM\_CLOCK\_FAST](#af46bc66f0da831b473d8cd5a89d95016a9bf9046f15baba71f9e033fa9a9cc5da) } |
| enum | [comp\_mcux\_acmp\_dm\_sample\_time](#a02663ed256e65d9428cece7020009b8b) {     [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T1](#a02663ed256e65d9428cece7020009b8ba7dbdcf7da47ff80e70bd18d9794d47b6) = 0 , [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T2](#a02663ed256e65d9428cece7020009b8ba25c027d23e992f9f0fb34b340930044f) , [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T4](#a02663ed256e65d9428cece7020009b8ba919b804030945459440c3258633b869c) , [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T8](#a02663ed256e65d9428cece7020009b8ba2673615d9e57489cd3d2476b75de201e) ,     [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T16](#a02663ed256e65d9428cece7020009b8ba420354c489651267a87ee708350cc64c) , [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T32](#a02663ed256e65d9428cece7020009b8bac1602e91186c1a55c4aa9fd82055108e) , [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T64](#a02663ed256e65d9428cece7020009b8ba738a689942adba583e702731bf839593) , [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T256](#a02663ed256e65d9428cece7020009b8baede31b32311f2101ec6b1bc71d4817b6)   } |
| enum | [comp\_mcux\_acmp\_dm\_phase\_time](#af2dfa67590cbbeccd0b6f67645b0441d) {     [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT0](#af2dfa67590cbbeccd0b6f67645b0441da1a55dd59fb842eedb08d813f2f28993d) = 0 , [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT1](#af2dfa67590cbbeccd0b6f67645b0441dacac4f7d8ce8a2e645a78ed6b447d5dc3) , [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT2](#af2dfa67590cbbeccd0b6f67645b0441da3a05245ed3f35737068767b2eb9a149c) , [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT3](#af2dfa67590cbbeccd0b6f67645b0441da9faaac53149adac3c8bbf89f899b8c38) ,     [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT4](#af2dfa67590cbbeccd0b6f67645b0441da3cbadc09466807a764a13a54bb4558c3) , [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT5](#af2dfa67590cbbeccd0b6f67645b0441dadf8fcb8a99892c71b8ce13d95b3898f3) , [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT6](#af2dfa67590cbbeccd0b6f67645b0441da5f5427fcdf807a1809a84c08f652ef26) , [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT7](#af2dfa67590cbbeccd0b6f67645b0441da0a1e8f175ba8e526863a01d0b2061645)   } |

| Functions | |
| --- | --- |
| int | [comp\_mcux\_acmp\_set\_mode\_config](#a6142f56ad1d713b0962a0d649c7bff2a) (const struct [device](structdevice.md) \*dev, const struct [comp\_mcux\_acmp\_mode\_config](structcomp__mcux__acmp__mode__config.md) \*config) |
| int | [comp\_mcux\_acmp\_set\_input\_config](#a2e8108f9260c3c190fc6faf58ceb6444) (const struct [device](structdevice.md) \*dev, const struct [comp\_mcux\_acmp\_input\_config](structcomp__mcux__acmp__input__config.md) \*config) |
| int | [comp\_mcux\_acmp\_set\_filter\_config](#a31447a8ce5f944733c56807503771fed) (const struct [device](structdevice.md) \*dev, const struct [comp\_mcux\_acmp\_filter\_config](structcomp__mcux__acmp__filter__config.md) \*config) |
| int | [comp\_mcux\_acmp\_set\_dac\_config](#ac08860be4538436c3ceef42ac040248b) (const struct [device](structdevice.md) \*dev, const struct [comp\_mcux\_acmp\_dac\_config](structcomp__mcux__acmp__dac__config.md) \*config) |
| int | [comp\_mcux\_acmp\_set\_dm\_config](#a933c1e1316294d6235f7ce186cd71806) (const struct [device](structdevice.md) \*dev, const struct [comp\_mcux\_acmp\_dm\_config](structcomp__mcux__acmp__dm__config.md) \*config) |
| int | [comp\_mcux\_acmp\_set\_window\_mode](#abb98c68803d17bee32e4fe6fe2480b7d) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |

## Enumeration Type Documentation

## [◆ ](#adee95c9485e970d2eb5659b539e25622)comp\_mcux\_acmp\_dac\_vref\_source

| enum [comp\_mcux\_acmp\_dac\_vref\_source](#adee95c9485e970d2eb5659b539e25622) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN1 |  |
| COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN2 |  |

## [◆ ](#af46bc66f0da831b473d8cd5a89d95016)comp\_mcux\_acmp\_dm\_clock

| enum [comp\_mcux\_acmp\_dm\_clock](#af46bc66f0da831b473d8cd5a89d95016) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_DM\_CLOCK\_SLOW |  |
| COMP\_MCUX\_ACMP\_DM\_CLOCK\_FAST |  |

## [◆ ](#af2dfa67590cbbeccd0b6f67645b0441d)comp\_mcux\_acmp\_dm\_phase\_time

| enum [comp\_mcux\_acmp\_dm\_phase\_time](#af2dfa67590cbbeccd0b6f67645b0441d) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT0 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT1 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT2 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT3 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT4 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT5 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT6 |  |
| COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT7 |  |

## [◆ ](#a02663ed256e65d9428cece7020009b8b)comp\_mcux\_acmp\_dm\_sample\_time

| enum [comp\_mcux\_acmp\_dm\_sample\_time](#a02663ed256e65d9428cece7020009b8b) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T1 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T2 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T4 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T8 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T16 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T32 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T64 |  |
| COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T256 |  |

## [◆ ](#adc9b7e82b83503bcd3ba4038873f61e4)comp\_mcux\_acmp\_hysteresis\_mode

| enum [comp\_mcux\_acmp\_hysteresis\_mode](#adc9b7e82b83503bcd3ba4038873f61e4) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL0 |  |
| COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL1 |  |
| COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL2 |  |
| COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL3 |  |

## [◆ ](#a0492419f3fd81bc5f773b688070eb5d3)comp\_mcux\_acmp\_mux\_input

| enum [comp\_mcux\_acmp\_mux\_input](#a0492419f3fd81bc5f773b688070eb5d3) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN0 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN1 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN2 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN3 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN4 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN5 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN6 |  |
| COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN7 |  |

## [◆ ](#a0aa19032738a4896dfa965c768e80d1a)comp\_mcux\_acmp\_offset\_mode

| enum [comp\_mcux\_acmp\_offset\_mode](#a0aa19032738a4896dfa965c768e80d1a) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL0 |  |
| COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL1 |  |

## [◆ ](#a0c4dda8b42ee7358c269ee0758ca2619)comp\_mcux\_acmp\_port\_input

| enum [comp\_mcux\_acmp\_port\_input](#a0c4dda8b42ee7358c269ee0758ca2619) |
| --- |

| Enumerator | |
| --- | --- |
| COMP\_MCUX\_ACMP\_PORT\_INPUT\_DAC |  |
| COMP\_MCUX\_ACMP\_PORT\_INPUT\_MUX |  |

## Function Documentation

## [◆ ](#ac08860be4538436c3ceef42ac040248b)comp\_mcux\_acmp\_set\_dac\_config()

| int comp\_mcux\_acmp\_set\_dac\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_mcux\_acmp\_dac\_config](structcomp__mcux__acmp__dac__config.md) \* | *config* ) |

## [◆ ](#a933c1e1316294d6235f7ce186cd71806)comp\_mcux\_acmp\_set\_dm\_config()

| int comp\_mcux\_acmp\_set\_dm\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_mcux\_acmp\_dm\_config](structcomp__mcux__acmp__dm__config.md) \* | *config* ) |

## [◆ ](#a31447a8ce5f944733c56807503771fed)comp\_mcux\_acmp\_set\_filter\_config()

| int comp\_mcux\_acmp\_set\_filter\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_mcux\_acmp\_filter\_config](structcomp__mcux__acmp__filter__config.md) \* | *config* ) |

## [◆ ](#a2e8108f9260c3c190fc6faf58ceb6444)comp\_mcux\_acmp\_set\_input\_config()

| int comp\_mcux\_acmp\_set\_input\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_mcux\_acmp\_input\_config](structcomp__mcux__acmp__input__config.md) \* | *config* ) |

## [◆ ](#a6142f56ad1d713b0962a0d649c7bff2a)comp\_mcux\_acmp\_set\_mode\_config()

| int comp\_mcux\_acmp\_set\_mode\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_mcux\_acmp\_mode\_config](structcomp__mcux__acmp__mode__config.md) \* | *config* ) |

## [◆ ](#abb98c68803d17bee32e4fe6fe2480b7d)comp\_mcux\_acmp\_set\_window\_mode()

| int comp\_mcux\_acmp\_set\_window\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [mcux\_acmp.h](comparator_2mcux__acmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
