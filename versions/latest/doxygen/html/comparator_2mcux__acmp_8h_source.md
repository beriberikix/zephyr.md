---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/comparator_2mcux__acmp_8h_source.html
original_path: doxygen/html/comparator_2mcux__acmp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_acmp.h

[Go to the documentation of this file.](comparator_2mcux__acmp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_MCUX\_ACMP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_MCUX\_ACMP\_H\_

9

10#include <[zephyr/drivers/comparator.h](comparator_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1a)enum [comp\_mcux\_acmp\_offset\_mode](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1a) {

[ 17](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1aa4875ab09cf32c9efb7ef6ff0a50b4dcb) [COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL0](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1aa4875ab09cf32c9efb7ef6ff0a50b4dcb) = 0,

[ 18](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1aa42db178d2cd8011dbb9268ba9f68fa28) [COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL1](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1aa42db178d2cd8011dbb9268ba9f68fa28),

19};

20

[ 21](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4)enum [comp\_mcux\_acmp\_hysteresis\_mode](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4) {

[ 22](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a32511e4b00c2ebd8d94274d23b0ab68c) [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL0](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a32511e4b00c2ebd8d94274d23b0ab68c) = 0,

[ 23](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4ab030cc0482444fd9708cca879856f505) [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL1](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4ab030cc0482444fd9708cca879856f505),

[ 24](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a416170b9857dbd7facb4ec2c47c93309) [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL2](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a416170b9857dbd7facb4ec2c47c93309),

[ 25](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a2142add933ef4ec6a1184579d3ee1a10) [COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL3](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a2142add933ef4ec6a1184579d3ee1a10),

26};

27

[ 28](structcomp__mcux__acmp__mode__config.md)struct [comp\_mcux\_acmp\_mode\_config](structcomp__mcux__acmp__mode__config.md) {

[ 29](structcomp__mcux__acmp__mode__config.md#ada67419325548375d8614b12381a5a53) enum [comp\_mcux\_acmp\_offset\_mode](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1a) [offset\_mode](structcomp__mcux__acmp__mode__config.md#ada67419325548375d8614b12381a5a53);

[ 30](structcomp__mcux__acmp__mode__config.md#a29ea0aa9a9cb6917a439e14e8885bad2) enum [comp\_mcux\_acmp\_hysteresis\_mode](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4) [hysteresis\_mode](structcomp__mcux__acmp__mode__config.md#a29ea0aa9a9cb6917a439e14e8885bad2);

[ 31](structcomp__mcux__acmp__mode__config.md#ada307019451f3d5f84c96e28aa7b9f1e) bool [enable\_high\_speed\_mode](structcomp__mcux__acmp__mode__config.md#ada307019451f3d5f84c96e28aa7b9f1e);

[ 32](structcomp__mcux__acmp__mode__config.md#ab53147aa215e4fa7659fab56ed8562e6) bool [invert\_output](structcomp__mcux__acmp__mode__config.md#ab53147aa215e4fa7659fab56ed8562e6);

[ 33](structcomp__mcux__acmp__mode__config.md#a2dbf53606d7d7768fa257fa7a63eb9fc) bool [use\_unfiltered\_output](structcomp__mcux__acmp__mode__config.md#a2dbf53606d7d7768fa257fa7a63eb9fc);

[ 34](structcomp__mcux__acmp__mode__config.md#a640d6a9458545003da53a2793dbacd17) bool [enable\_pin\_output](structcomp__mcux__acmp__mode__config.md#a640d6a9458545003da53a2793dbacd17);

35};

36

[ 37](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3)enum [comp\_mcux\_acmp\_mux\_input](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3) {

[ 38](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ae66ddfcc7428df449f77d7403d854aed) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN0](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ae66ddfcc7428df449f77d7403d854aed) = 0,

[ 39](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a222a536a9d0d358f151beea3c5dca85a) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN1](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a222a536a9d0d358f151beea3c5dca85a),

[ 40](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ad93a4f7606dab63cb5c038e47c4057d6) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN2](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ad93a4f7606dab63cb5c038e47c4057d6),

[ 41](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ac72c54e0e564773dfe5c1d610f92e044) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN3](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ac72c54e0e564773dfe5c1d610f92e044),

[ 42](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a080e839262220380b90e63ce2e5aded7) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN4](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a080e839262220380b90e63ce2e5aded7),

[ 43](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a3f8ae7b0222bac88917784df2db230bb) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN5](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a3f8ae7b0222bac88917784df2db230bb),

[ 44](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a4b0a916f650db858811f1a380021010a) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN6](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a4b0a916f650db858811f1a380021010a),

[ 45](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3aac0f390fe34f46986c7b1b8e46bc7edc) [COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN7](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3aac0f390fe34f46986c7b1b8e46bc7edc),

46};

47

[ 48](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619)enum [comp\_mcux\_acmp\_port\_input](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619) {

[ 49](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619a6bd5cb01f180608522b85b19dab13eba) [COMP\_MCUX\_ACMP\_PORT\_INPUT\_DAC](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619a6bd5cb01f180608522b85b19dab13eba) = 0,

[ 50](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619a4cf0087765eecb5e90a96d0f8a171fdb) [COMP\_MCUX\_ACMP\_PORT\_INPUT\_MUX](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619a4cf0087765eecb5e90a96d0f8a171fdb),

51};

52

[ 53](structcomp__mcux__acmp__input__config.md)struct [comp\_mcux\_acmp\_input\_config](structcomp__mcux__acmp__input__config.md) {

[ 54](structcomp__mcux__acmp__input__config.md#ab1dd34f2d00a041171c91d3253d0786e) enum [comp\_mcux\_acmp\_mux\_input](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3) [positive\_mux\_input](structcomp__mcux__acmp__input__config.md#ab1dd34f2d00a041171c91d3253d0786e);

[ 55](structcomp__mcux__acmp__input__config.md#a1b7553e4cc5d6bc541c0bce40592660b) enum [comp\_mcux\_acmp\_mux\_input](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3) [negative\_mux\_input](structcomp__mcux__acmp__input__config.md#a1b7553e4cc5d6bc541c0bce40592660b);

[ 56](structcomp__mcux__acmp__input__config.md#abed61ab47d6e9f985860674a4d75d623) enum [comp\_mcux\_acmp\_port\_input](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619) [positive\_port\_input](structcomp__mcux__acmp__input__config.md#abed61ab47d6e9f985860674a4d75d623);

[ 57](structcomp__mcux__acmp__input__config.md#ad4a8e5b0707fa7fa130c02627030cef1) enum [comp\_mcux\_acmp\_port\_input](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619) [negative\_port\_input](structcomp__mcux__acmp__input__config.md#ad4a8e5b0707fa7fa130c02627030cef1);

58};

59

[ 60](structcomp__mcux__acmp__filter__config.md)struct [comp\_mcux\_acmp\_filter\_config](structcomp__mcux__acmp__filter__config.md) {

[ 61](structcomp__mcux__acmp__filter__config.md#a49f9ba4160402d92b4df7f144bd4eeab) bool [enable\_sample](structcomp__mcux__acmp__filter__config.md#a49f9ba4160402d92b4df7f144bd4eeab);

[ 62](structcomp__mcux__acmp__filter__config.md#a9bbedf6f218ed24228b38c07d4765150) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_count](structcomp__mcux__acmp__filter__config.md#a9bbedf6f218ed24228b38c07d4765150);

[ 63](structcomp__mcux__acmp__filter__config.md#a1bdf63f3d034a6e8440f30be99312540) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_period](structcomp__mcux__acmp__filter__config.md#a1bdf63f3d034a6e8440f30be99312540);

64};

65

[ 66](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622)enum [comp\_mcux\_acmp\_dac\_vref\_source](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622) {

[ 67](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622a41fbf3bf10d813c3ef7f1a55217efba8) [COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN1](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622a41fbf3bf10d813c3ef7f1a55217efba8) = 0,

[ 68](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622ad25d18fdef06d865b974323ed26144dc) [COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN2](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622ad25d18fdef06d865b974323ed26144dc),

69};

70

[ 71](structcomp__mcux__acmp__dac__config.md)struct [comp\_mcux\_acmp\_dac\_config](structcomp__mcux__acmp__dac__config.md) {

[ 72](structcomp__mcux__acmp__dac__config.md#a31d46163b5bd50e7da085ede0b15401b) enum [comp\_mcux\_acmp\_dac\_vref\_source](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622) [vref\_source](structcomp__mcux__acmp__dac__config.md#a31d46163b5bd50e7da085ede0b15401b);

[ 73](structcomp__mcux__acmp__dac__config.md#af183580b4cc4e62cbd05e8dfcbccf8c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [value](structcomp__mcux__acmp__dac__config.md#af183580b4cc4e62cbd05e8dfcbccf8c3);

[ 74](structcomp__mcux__acmp__dac__config.md#a757444f5cb22de45509b0ca80a023a6b) bool [enable\_output](structcomp__mcux__acmp__dac__config.md#a757444f5cb22de45509b0ca80a023a6b);

[ 75](structcomp__mcux__acmp__dac__config.md#a68003c7de53d9caedf6f2eafebab8092) bool [enable\_high\_speed\_mode](structcomp__mcux__acmp__dac__config.md#a68003c7de53d9caedf6f2eafebab8092);

76};

77

[ 78](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016)enum [comp\_mcux\_acmp\_dm\_clock](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016) {

[ 79](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016ae92b237fa2ef27ce8b3d05103d5ed0f8) [COMP\_MCUX\_ACMP\_DM\_CLOCK\_SLOW](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016ae92b237fa2ef27ce8b3d05103d5ed0f8) = 0,

[ 80](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016a9bf9046f15baba71f9e033fa9a9cc5da) [COMP\_MCUX\_ACMP\_DM\_CLOCK\_FAST](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016a9bf9046f15baba71f9e033fa9a9cc5da),

81};

82

[ 83](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8b)enum [comp\_mcux\_acmp\_dm\_sample\_time](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8b) {

[ 84](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba7dbdcf7da47ff80e70bd18d9794d47b6) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T1](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba7dbdcf7da47ff80e70bd18d9794d47b6) = 0,

[ 85](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba25c027d23e992f9f0fb34b340930044f) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T2](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba25c027d23e992f9f0fb34b340930044f),

[ 86](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba919b804030945459440c3258633b869c) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T4](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba919b804030945459440c3258633b869c),

[ 87](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba2673615d9e57489cd3d2476b75de201e) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T8](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba2673615d9e57489cd3d2476b75de201e),

[ 88](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba420354c489651267a87ee708350cc64c) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T16](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba420354c489651267a87ee708350cc64c),

[ 89](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8bac1602e91186c1a55c4aa9fd82055108e) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T32](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8bac1602e91186c1a55c4aa9fd82055108e),

[ 90](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba738a689942adba583e702731bf839593) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T64](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba738a689942adba583e702731bf839593),

[ 91](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8baede31b32311f2101ec6b1bc71d4817b6) [COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T256](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8baede31b32311f2101ec6b1bc71d4817b6),

92};

93

[ 94](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441d)enum [comp\_mcux\_acmp\_dm\_phase\_time](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441d) {

[ 95](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da1a55dd59fb842eedb08d813f2f28993d) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT0](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da1a55dd59fb842eedb08d813f2f28993d) = 0,

[ 96](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441dacac4f7d8ce8a2e645a78ed6b447d5dc3) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT1](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441dacac4f7d8ce8a2e645a78ed6b447d5dc3),

[ 97](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da3a05245ed3f35737068767b2eb9a149c) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT2](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da3a05245ed3f35737068767b2eb9a149c),

[ 98](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da9faaac53149adac3c8bbf89f899b8c38) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT3](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da9faaac53149adac3c8bbf89f899b8c38),

[ 99](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da3cbadc09466807a764a13a54bb4558c3) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT4](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da3cbadc09466807a764a13a54bb4558c3),

[ 100](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441dadf8fcb8a99892c71b8ce13d95b3898f3) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT5](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441dadf8fcb8a99892c71b8ce13d95b3898f3),

[ 101](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da5f5427fcdf807a1809a84c08f652ef26) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT6](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da5f5427fcdf807a1809a84c08f652ef26),

[ 102](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da0a1e8f175ba8e526863a01d0b2061645) [COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT7](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da0a1e8f175ba8e526863a01d0b2061645),

103};

104

[ 105](structcomp__mcux__acmp__dm__config.md)struct [comp\_mcux\_acmp\_dm\_config](structcomp__mcux__acmp__dm__config.md) {

[ 106](structcomp__mcux__acmp__dm__config.md#a54f7f0b339b99101c14a82d8955faafb) bool [enable\_positive\_channel](structcomp__mcux__acmp__dm__config.md#a54f7f0b339b99101c14a82d8955faafb);

[ 107](structcomp__mcux__acmp__dm__config.md#ad147342b6838c63a7a458146f2cca35c) bool [enable\_negative\_channel](structcomp__mcux__acmp__dm__config.md#ad147342b6838c63a7a458146f2cca35c);

[ 108](structcomp__mcux__acmp__dm__config.md#a059278036bce5d74722e096634fdfac1) bool [enable\_resistor\_divider](structcomp__mcux__acmp__dm__config.md#a059278036bce5d74722e096634fdfac1);

[ 109](structcomp__mcux__acmp__dm__config.md#aa4ad43635fe8214e3b6963b626cbe0de) enum [comp\_mcux\_acmp\_dm\_clock](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016) [clock\_source](structcomp__mcux__acmp__dm__config.md#aa4ad43635fe8214e3b6963b626cbe0de);

[ 110](structcomp__mcux__acmp__dm__config.md#a8f2a109c624ff2a35615a88831aa9d7b) enum [comp\_mcux\_acmp\_dm\_sample\_time](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8b) [sample\_time](structcomp__mcux__acmp__dm__config.md#a8f2a109c624ff2a35615a88831aa9d7b);

[ 111](structcomp__mcux__acmp__dm__config.md#a21cb08fe1cbd66cbb2f10fb2b9943635) enum [comp\_mcux\_acmp\_dm\_phase\_time](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441d) [phase1\_time](structcomp__mcux__acmp__dm__config.md#a21cb08fe1cbd66cbb2f10fb2b9943635);

[ 112](structcomp__mcux__acmp__dm__config.md#aaeff0b798cbffb4f4bf2454243e6dfd4) enum [comp\_mcux\_acmp\_dm\_phase\_time](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441d) [phase2\_time](structcomp__mcux__acmp__dm__config.md#aaeff0b798cbffb4f4bf2454243e6dfd4);

113};

114

[ 115](comparator_2mcux__acmp_8h.md#a6142f56ad1d713b0962a0d649c7bff2a)int [comp\_mcux\_acmp\_set\_mode\_config](comparator_2mcux__acmp_8h.md#a6142f56ad1d713b0962a0d649c7bff2a)(const struct [device](structdevice.md) \*dev,

116 const struct [comp\_mcux\_acmp\_mode\_config](structcomp__mcux__acmp__mode__config.md) \*config);

117

[ 118](comparator_2mcux__acmp_8h.md#a2e8108f9260c3c190fc6faf58ceb6444)int [comp\_mcux\_acmp\_set\_input\_config](comparator_2mcux__acmp_8h.md#a2e8108f9260c3c190fc6faf58ceb6444)(const struct [device](structdevice.md) \*dev,

119 const struct [comp\_mcux\_acmp\_input\_config](structcomp__mcux__acmp__input__config.md) \*config);

120

[ 121](comparator_2mcux__acmp_8h.md#a31447a8ce5f944733c56807503771fed)int [comp\_mcux\_acmp\_set\_filter\_config](comparator_2mcux__acmp_8h.md#a31447a8ce5f944733c56807503771fed)(const struct [device](structdevice.md) \*dev,

122 const struct [comp\_mcux\_acmp\_filter\_config](structcomp__mcux__acmp__filter__config.md) \*config);

123

[ 124](comparator_2mcux__acmp_8h.md#ac08860be4538436c3ceef42ac040248b)int [comp\_mcux\_acmp\_set\_dac\_config](comparator_2mcux__acmp_8h.md#ac08860be4538436c3ceef42ac040248b)(const struct [device](structdevice.md) \*dev,

125 const struct [comp\_mcux\_acmp\_dac\_config](structcomp__mcux__acmp__dac__config.md) \*config);

126

[ 127](comparator_2mcux__acmp_8h.md#a933c1e1316294d6235f7ce186cd71806)int [comp\_mcux\_acmp\_set\_dm\_config](comparator_2mcux__acmp_8h.md#a933c1e1316294d6235f7ce186cd71806)(const struct [device](structdevice.md) \*dev,

128 const struct [comp\_mcux\_acmp\_dm\_config](structcomp__mcux__acmp__dm__config.md) \*config);

129

[ 130](comparator_2mcux__acmp_8h.md#abb98c68803d17bee32e4fe6fe2480b7d)int [comp\_mcux\_acmp\_set\_window\_mode](comparator_2mcux__acmp_8h.md#abb98c68803d17bee32e4fe6fe2480b7d)(const struct [device](structdevice.md) \*dev, bool enable);

131

132#ifdef \_\_cplusplus

133}

134#endif

135

136#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_MCUX\_ACMP\_H\_ \*/

[comp\_mcux\_acmp\_dm\_sample\_time](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8b)

comp\_mcux\_acmp\_dm\_sample\_time

**Definition** mcux\_acmp.h:83

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T2](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba25c027d23e992f9f0fb34b340930044f)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T2

**Definition** mcux\_acmp.h:85

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T8](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba2673615d9e57489cd3d2476b75de201e)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T8

**Definition** mcux\_acmp.h:87

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T16](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba420354c489651267a87ee708350cc64c)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T16

**Definition** mcux\_acmp.h:88

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T64](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba738a689942adba583e702731bf839593)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T64

**Definition** mcux\_acmp.h:90

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T1](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba7dbdcf7da47ff80e70bd18d9794d47b6)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T1

**Definition** mcux\_acmp.h:84

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T4](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8ba919b804030945459440c3258633b869c)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T4

**Definition** mcux\_acmp.h:86

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T32](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8bac1602e91186c1a55c4aa9fd82055108e)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T32

**Definition** mcux\_acmp.h:89

[COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T256](comparator_2mcux__acmp_8h.md#a02663ed256e65d9428cece7020009b8baede31b32311f2101ec6b1bc71d4817b6)

@ COMP\_MCUX\_ACMP\_DM\_SAMPLE\_TIME\_T256

**Definition** mcux\_acmp.h:91

[comp\_mcux\_acmp\_mux\_input](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3)

comp\_mcux\_acmp\_mux\_input

**Definition** mcux\_acmp.h:37

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN4](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a080e839262220380b90e63ce2e5aded7)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN4

**Definition** mcux\_acmp.h:42

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN1](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a222a536a9d0d358f151beea3c5dca85a)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN1

**Definition** mcux\_acmp.h:39

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN5](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a3f8ae7b0222bac88917784df2db230bb)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN5

**Definition** mcux\_acmp.h:43

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN6](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3a4b0a916f650db858811f1a380021010a)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN6

**Definition** mcux\_acmp.h:44

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN7](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3aac0f390fe34f46986c7b1b8e46bc7edc)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN7

**Definition** mcux\_acmp.h:45

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN3](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ac72c54e0e564773dfe5c1d610f92e044)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN3

**Definition** mcux\_acmp.h:41

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN2](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ad93a4f7606dab63cb5c038e47c4057d6)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN2

**Definition** mcux\_acmp.h:40

[COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN0](comparator_2mcux__acmp_8h.md#a0492419f3fd81bc5f773b688070eb5d3ae66ddfcc7428df449f77d7403d854aed)

@ COMP\_MCUX\_ACMP\_MUX\_INPUT\_IN0

**Definition** mcux\_acmp.h:38

[comp\_mcux\_acmp\_offset\_mode](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1a)

comp\_mcux\_acmp\_offset\_mode

**Definition** mcux\_acmp.h:16

[COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL1](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1aa42db178d2cd8011dbb9268ba9f68fa28)

@ COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL1

**Definition** mcux\_acmp.h:18

[COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL0](comparator_2mcux__acmp_8h.md#a0aa19032738a4896dfa965c768e80d1aa4875ab09cf32c9efb7ef6ff0a50b4dcb)

@ COMP\_MCUX\_ACMP\_OFFSET\_MODE\_LEVEL0

**Definition** mcux\_acmp.h:17

[comp\_mcux\_acmp\_port\_input](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619)

comp\_mcux\_acmp\_port\_input

**Definition** mcux\_acmp.h:48

[COMP\_MCUX\_ACMP\_PORT\_INPUT\_MUX](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619a4cf0087765eecb5e90a96d0f8a171fdb)

@ COMP\_MCUX\_ACMP\_PORT\_INPUT\_MUX

**Definition** mcux\_acmp.h:50

[COMP\_MCUX\_ACMP\_PORT\_INPUT\_DAC](comparator_2mcux__acmp_8h.md#a0c4dda8b42ee7358c269ee0758ca2619a6bd5cb01f180608522b85b19dab13eba)

@ COMP\_MCUX\_ACMP\_PORT\_INPUT\_DAC

**Definition** mcux\_acmp.h:49

[comp\_mcux\_acmp\_set\_input\_config](comparator_2mcux__acmp_8h.md#a2e8108f9260c3c190fc6faf58ceb6444)

int comp\_mcux\_acmp\_set\_input\_config(const struct device \*dev, const struct comp\_mcux\_acmp\_input\_config \*config)

[comp\_mcux\_acmp\_set\_filter\_config](comparator_2mcux__acmp_8h.md#a31447a8ce5f944733c56807503771fed)

int comp\_mcux\_acmp\_set\_filter\_config(const struct device \*dev, const struct comp\_mcux\_acmp\_filter\_config \*config)

[comp\_mcux\_acmp\_set\_mode\_config](comparator_2mcux__acmp_8h.md#a6142f56ad1d713b0962a0d649c7bff2a)

int comp\_mcux\_acmp\_set\_mode\_config(const struct device \*dev, const struct comp\_mcux\_acmp\_mode\_config \*config)

[comp\_mcux\_acmp\_set\_dm\_config](comparator_2mcux__acmp_8h.md#a933c1e1316294d6235f7ce186cd71806)

int comp\_mcux\_acmp\_set\_dm\_config(const struct device \*dev, const struct comp\_mcux\_acmp\_dm\_config \*config)

[comp\_mcux\_acmp\_set\_window\_mode](comparator_2mcux__acmp_8h.md#abb98c68803d17bee32e4fe6fe2480b7d)

int comp\_mcux\_acmp\_set\_window\_mode(const struct device \*dev, bool enable)

[comp\_mcux\_acmp\_set\_dac\_config](comparator_2mcux__acmp_8h.md#ac08860be4538436c3ceef42ac040248b)

int comp\_mcux\_acmp\_set\_dac\_config(const struct device \*dev, const struct comp\_mcux\_acmp\_dac\_config \*config)

[comp\_mcux\_acmp\_hysteresis\_mode](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4)

comp\_mcux\_acmp\_hysteresis\_mode

**Definition** mcux\_acmp.h:21

[COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL3](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a2142add933ef4ec6a1184579d3ee1a10)

@ COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL3

**Definition** mcux\_acmp.h:25

[COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL0](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a32511e4b00c2ebd8d94274d23b0ab68c)

@ COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL0

**Definition** mcux\_acmp.h:22

[COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL2](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4a416170b9857dbd7facb4ec2c47c93309)

@ COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL2

**Definition** mcux\_acmp.h:24

[COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL1](comparator_2mcux__acmp_8h.md#adc9b7e82b83503bcd3ba4038873f61e4ab030cc0482444fd9708cca879856f505)

@ COMP\_MCUX\_ACMP\_HYSTERESIS\_MODE\_LEVEL1

**Definition** mcux\_acmp.h:23

[comp\_mcux\_acmp\_dac\_vref\_source](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622)

comp\_mcux\_acmp\_dac\_vref\_source

**Definition** mcux\_acmp.h:66

[COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN1](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622a41fbf3bf10d813c3ef7f1a55217efba8)

@ COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN1

**Definition** mcux\_acmp.h:67

[COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN2](comparator_2mcux__acmp_8h.md#adee95c9485e970d2eb5659b539e25622ad25d18fdef06d865b974323ed26144dc)

@ COMP\_MCUX\_ACMP\_DAC\_VREF\_SOURCE\_VIN2

**Definition** mcux\_acmp.h:68

[comp\_mcux\_acmp\_dm\_phase\_time](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441d)

comp\_mcux\_acmp\_dm\_phase\_time

**Definition** mcux\_acmp.h:94

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT7](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da0a1e8f175ba8e526863a01d0b2061645)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT7

**Definition** mcux\_acmp.h:102

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT0](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da1a55dd59fb842eedb08d813f2f28993d)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT0

**Definition** mcux\_acmp.h:95

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT2](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da3a05245ed3f35737068767b2eb9a149c)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT2

**Definition** mcux\_acmp.h:97

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT4](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da3cbadc09466807a764a13a54bb4558c3)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT4

**Definition** mcux\_acmp.h:99

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT6](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da5f5427fcdf807a1809a84c08f652ef26)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT6

**Definition** mcux\_acmp.h:101

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT3](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441da9faaac53149adac3c8bbf89f899b8c38)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT3

**Definition** mcux\_acmp.h:98

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT1](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441dacac4f7d8ce8a2e645a78ed6b447d5dc3)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT1

**Definition** mcux\_acmp.h:96

[COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT5](comparator_2mcux__acmp_8h.md#af2dfa67590cbbeccd0b6f67645b0441dadf8fcb8a99892c71b8ce13d95b3898f3)

@ COMP\_MCUX\_ACMP\_DM\_PHASE\_TIME\_ALT5

**Definition** mcux\_acmp.h:100

[comp\_mcux\_acmp\_dm\_clock](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016)

comp\_mcux\_acmp\_dm\_clock

**Definition** mcux\_acmp.h:78

[COMP\_MCUX\_ACMP\_DM\_CLOCK\_FAST](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016a9bf9046f15baba71f9e033fa9a9cc5da)

@ COMP\_MCUX\_ACMP\_DM\_CLOCK\_FAST

**Definition** mcux\_acmp.h:80

[COMP\_MCUX\_ACMP\_DM\_CLOCK\_SLOW](comparator_2mcux__acmp_8h.md#af46bc66f0da831b473d8cd5a89d95016ae92b237fa2ef27ce8b3d05103d5ed0f8)

@ COMP\_MCUX\_ACMP\_DM\_CLOCK\_SLOW

**Definition** mcux\_acmp.h:79

[comparator.h](comparator_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[comp\_mcux\_acmp\_dac\_config](structcomp__mcux__acmp__dac__config.md)

**Definition** mcux\_acmp.h:71

[comp\_mcux\_acmp\_dac\_config::vref\_source](structcomp__mcux__acmp__dac__config.md#a31d46163b5bd50e7da085ede0b15401b)

enum comp\_mcux\_acmp\_dac\_vref\_source vref\_source

**Definition** mcux\_acmp.h:72

[comp\_mcux\_acmp\_dac\_config::enable\_high\_speed\_mode](structcomp__mcux__acmp__dac__config.md#a68003c7de53d9caedf6f2eafebab8092)

bool enable\_high\_speed\_mode

**Definition** mcux\_acmp.h:75

[comp\_mcux\_acmp\_dac\_config::enable\_output](structcomp__mcux__acmp__dac__config.md#a757444f5cb22de45509b0ca80a023a6b)

bool enable\_output

**Definition** mcux\_acmp.h:74

[comp\_mcux\_acmp\_dac\_config::value](structcomp__mcux__acmp__dac__config.md#af183580b4cc4e62cbd05e8dfcbccf8c3)

uint8\_t value

**Definition** mcux\_acmp.h:73

[comp\_mcux\_acmp\_dm\_config](structcomp__mcux__acmp__dm__config.md)

**Definition** mcux\_acmp.h:105

[comp\_mcux\_acmp\_dm\_config::enable\_resistor\_divider](structcomp__mcux__acmp__dm__config.md#a059278036bce5d74722e096634fdfac1)

bool enable\_resistor\_divider

**Definition** mcux\_acmp.h:108

[comp\_mcux\_acmp\_dm\_config::phase1\_time](structcomp__mcux__acmp__dm__config.md#a21cb08fe1cbd66cbb2f10fb2b9943635)

enum comp\_mcux\_acmp\_dm\_phase\_time phase1\_time

**Definition** mcux\_acmp.h:111

[comp\_mcux\_acmp\_dm\_config::enable\_positive\_channel](structcomp__mcux__acmp__dm__config.md#a54f7f0b339b99101c14a82d8955faafb)

bool enable\_positive\_channel

**Definition** mcux\_acmp.h:106

[comp\_mcux\_acmp\_dm\_config::sample\_time](structcomp__mcux__acmp__dm__config.md#a8f2a109c624ff2a35615a88831aa9d7b)

enum comp\_mcux\_acmp\_dm\_sample\_time sample\_time

**Definition** mcux\_acmp.h:110

[comp\_mcux\_acmp\_dm\_config::clock\_source](structcomp__mcux__acmp__dm__config.md#aa4ad43635fe8214e3b6963b626cbe0de)

enum comp\_mcux\_acmp\_dm\_clock clock\_source

**Definition** mcux\_acmp.h:109

[comp\_mcux\_acmp\_dm\_config::phase2\_time](structcomp__mcux__acmp__dm__config.md#aaeff0b798cbffb4f4bf2454243e6dfd4)

enum comp\_mcux\_acmp\_dm\_phase\_time phase2\_time

**Definition** mcux\_acmp.h:112

[comp\_mcux\_acmp\_dm\_config::enable\_negative\_channel](structcomp__mcux__acmp__dm__config.md#ad147342b6838c63a7a458146f2cca35c)

bool enable\_negative\_channel

**Definition** mcux\_acmp.h:107

[comp\_mcux\_acmp\_filter\_config](structcomp__mcux__acmp__filter__config.md)

**Definition** mcux\_acmp.h:60

[comp\_mcux\_acmp\_filter\_config::filter\_period](structcomp__mcux__acmp__filter__config.md#a1bdf63f3d034a6e8440f30be99312540)

uint8\_t filter\_period

**Definition** mcux\_acmp.h:63

[comp\_mcux\_acmp\_filter\_config::enable\_sample](structcomp__mcux__acmp__filter__config.md#a49f9ba4160402d92b4df7f144bd4eeab)

bool enable\_sample

**Definition** mcux\_acmp.h:61

[comp\_mcux\_acmp\_filter\_config::filter\_count](structcomp__mcux__acmp__filter__config.md#a9bbedf6f218ed24228b38c07d4765150)

uint8\_t filter\_count

**Definition** mcux\_acmp.h:62

[comp\_mcux\_acmp\_input\_config](structcomp__mcux__acmp__input__config.md)

**Definition** mcux\_acmp.h:53

[comp\_mcux\_acmp\_input\_config::negative\_mux\_input](structcomp__mcux__acmp__input__config.md#a1b7553e4cc5d6bc541c0bce40592660b)

enum comp\_mcux\_acmp\_mux\_input negative\_mux\_input

**Definition** mcux\_acmp.h:55

[comp\_mcux\_acmp\_input\_config::positive\_mux\_input](structcomp__mcux__acmp__input__config.md#ab1dd34f2d00a041171c91d3253d0786e)

enum comp\_mcux\_acmp\_mux\_input positive\_mux\_input

**Definition** mcux\_acmp.h:54

[comp\_mcux\_acmp\_input\_config::positive\_port\_input](structcomp__mcux__acmp__input__config.md#abed61ab47d6e9f985860674a4d75d623)

enum comp\_mcux\_acmp\_port\_input positive\_port\_input

**Definition** mcux\_acmp.h:56

[comp\_mcux\_acmp\_input\_config::negative\_port\_input](structcomp__mcux__acmp__input__config.md#ad4a8e5b0707fa7fa130c02627030cef1)

enum comp\_mcux\_acmp\_port\_input negative\_port\_input

**Definition** mcux\_acmp.h:57

[comp\_mcux\_acmp\_mode\_config](structcomp__mcux__acmp__mode__config.md)

**Definition** mcux\_acmp.h:28

[comp\_mcux\_acmp\_mode\_config::hysteresis\_mode](structcomp__mcux__acmp__mode__config.md#a29ea0aa9a9cb6917a439e14e8885bad2)

enum comp\_mcux\_acmp\_hysteresis\_mode hysteresis\_mode

**Definition** mcux\_acmp.h:30

[comp\_mcux\_acmp\_mode\_config::use\_unfiltered\_output](structcomp__mcux__acmp__mode__config.md#a2dbf53606d7d7768fa257fa7a63eb9fc)

bool use\_unfiltered\_output

**Definition** mcux\_acmp.h:33

[comp\_mcux\_acmp\_mode\_config::enable\_pin\_output](structcomp__mcux__acmp__mode__config.md#a640d6a9458545003da53a2793dbacd17)

bool enable\_pin\_output

**Definition** mcux\_acmp.h:34

[comp\_mcux\_acmp\_mode\_config::invert\_output](structcomp__mcux__acmp__mode__config.md#ab53147aa215e4fa7659fab56ed8562e6)

bool invert\_output

**Definition** mcux\_acmp.h:32

[comp\_mcux\_acmp\_mode\_config::enable\_high\_speed\_mode](structcomp__mcux__acmp__mode__config.md#ada307019451f3d5f84c96e28aa7b9f1e)

bool enable\_high\_speed\_mode

**Definition** mcux\_acmp.h:31

[comp\_mcux\_acmp\_mode\_config::offset\_mode](structcomp__mcux__acmp__mode__config.md#ada67419325548375d8614b12381a5a53)

enum comp\_mcux\_acmp\_offset\_mode offset\_mode

**Definition** mcux\_acmp.h:29

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [mcux\_acmp.h](comparator_2mcux__acmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
