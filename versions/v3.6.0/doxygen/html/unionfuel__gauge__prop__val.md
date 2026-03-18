---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionfuel__gauge__prop__val.html
original_path: doxygen/html/unionfuel__gauge__prop__val.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fuel\_gauge\_prop\_val Union Reference

[Device Driver APIs](group__io__interfaces.md) » [Fuel Gauge Interface](group__fuel__gauge__interface.md)

Property field to value/type union.
[More...](#details)

`#include <[fuel_gauge.h](fuel__gauge_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [avg\_current](#ad96f07db337c038466dd17401c076d38) |
|  | FUEL\_GAUGE\_AVG\_CURRENT. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [cutoff](#ac8e8e74c2b1f2e0c1f4e65eecf5a745a) |
|  | FUEL\_GAUGE\_CHARGE\_CUTOFF. |
| int | [current](#a9bed3247063f069bb92b2902cc5ff468) |
|  | FUEL\_GAUGE\_CURRENT. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cycle\_count](#ac27ae67a315a7204cea6e88962758587) |
|  | FUEL\_GAUGE\_CYCLE\_COUNT. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#adeb93ed2120e808aac815dcbdf69067f) |
|  | FUEL\_GAUGE\_FLAGS. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [full\_charge\_capacity](#aa29f7163a1637b6aa8cd6a15dc99d55b) |
|  | FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [remaining\_capacity](#adecf57aa90e2b5d483cfd889ec512400) |
|  | FUEL\_GAUGE\_REMAINING\_CAPACITY. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [runtime\_to\_empty](#ae716bdf1346dc7767d98526db6083008) |
|  | FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [runtime\_to\_full](#a2c77e8de7fa40fadfa13dfd4c94df804) |
|  | FUEL\_GAUGE\_RUNTIME\_TO\_FULL. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sbs\_mfr\_access\_word](#a957025a2a9fb7709e2bf478f15fd31a0) |
|  | FUEL\_GAUGE\_SBS\_MFR\_ACCESS. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [absolute\_state\_of\_charge](#a33297ff5bf70b510272eddf77ced411e) |
|  | FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [relative\_state\_of\_charge](#a45b20c5118f7ee408d507b94e6cae1dc) |
|  | FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [temperature](#a36528b111568bd1c90859e454610fd9f) |
|  | FUEL\_GAUGE\_TEMPERATURE. |
| int | [voltage](#abec5cadefa09e088620a9598dec9c473) |
|  | FUEL\_GAUGE\_VOLTAGE. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sbs\_mode](#a7fc0551e303de56e0eb6bdac1ecaccd0) |
|  | FUEL\_GAUGE\_SBS\_MODE. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [chg\_current](#a6f74626deef4debbd8dfe6c188984d1b) |
|  | FUEL\_GAUGE\_CHARGE\_CURRENT. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [chg\_voltage](#a8743f7e7a05919b5469e39527b697e62) |
|  | FUEL\_GAUGE\_CHARGE\_VOLTAGE. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fg\_status](#a65607bb9ba43022c9c566646d4763aac) |
|  | FUEL\_GAUGE\_STATUS. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [design\_cap](#a20aa5736b0ac3c5adda10152660de275) |
|  | FUEL\_GAUGE\_DESIGN\_CAPACITY. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [design\_volt](#a11626713aef0445ad613a5976401d09e) |
|  | FUEL\_GAUGE\_DESIGN\_VOLTAGE. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [sbs\_at\_rate](#aa5529fea5cfe765be9b66f5fad96ab2f) |
|  | FUEL\_GAUGE\_SBS\_ATRATE. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sbs\_at\_rate\_time\_to\_full](#aeeeddb48f22b54f90c603d58e9ffa9a5) |
|  | FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sbs\_at\_rate\_time\_to\_empty](#a7c8b6f9ee98e5b97ddc85b7e72cea4a8) |
|  | FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sbs\_at\_rate\_ok](#a9b5015878c9a77d9c8330139f94843b7) |
|  | FUEL\_GAUGE\_SBS\_ATRATE\_OK. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sbs\_remaining\_capacity\_alarm](#a818ab7faf8f51d4d1a5c5f070d54b997) |
|  | FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sbs\_remaining\_time\_alarm](#aa0e46c727bb31acb5d41ce4bc6d5b106) |
|  | FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM. |

## Detailed Description

Property field to value/type union.

## Field Documentation

## [◆ ](#a33297ff5bf70b510272eddf77ced411e)absolute\_state\_of\_charge

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fuel\_gauge\_prop\_val::absolute\_state\_of\_charge |
| --- |

FUEL\_GAUGE\_ABSOLUTE\_STATE\_OF\_CHARGE.

## [◆ ](#ad96f07db337c038466dd17401c076d38)avg\_current

| int fuel\_gauge\_prop\_val::avg\_current |
| --- |

FUEL\_GAUGE\_AVG\_CURRENT.

## [◆ ](#a6f74626deef4debbd8dfe6c188984d1b)chg\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::chg\_current |
| --- |

FUEL\_GAUGE\_CHARGE\_CURRENT.

## [◆ ](#a8743f7e7a05919b5469e39527b697e62)chg\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::chg\_voltage |
| --- |

FUEL\_GAUGE\_CHARGE\_VOLTAGE.

## [◆ ](#a9bed3247063f069bb92b2902cc5ff468)current

| int fuel\_gauge\_prop\_val::current |
| --- |

FUEL\_GAUGE\_CURRENT.

## [◆ ](#ac8e8e74c2b1f2e0c1f4e65eecf5a745a)cutoff

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fuel\_gauge\_prop\_val::cutoff |
| --- |

FUEL\_GAUGE\_CHARGE\_CUTOFF.

## [◆ ](#ac27ae67a315a7204cea6e88962758587)cycle\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::cycle\_count |
| --- |

FUEL\_GAUGE\_CYCLE\_COUNT.

## [◆ ](#a20aa5736b0ac3c5adda10152660de275)design\_cap

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::design\_cap |
| --- |

FUEL\_GAUGE\_DESIGN\_CAPACITY.

## [◆ ](#a11626713aef0445ad613a5976401d09e)design\_volt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::design\_volt |
| --- |

FUEL\_GAUGE\_DESIGN\_VOLTAGE.

## [◆ ](#a65607bb9ba43022c9c566646d4763aac)fg\_status

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::fg\_status |
| --- |

FUEL\_GAUGE\_STATUS.

## [◆ ](#adeb93ed2120e808aac815dcbdf69067f)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::flags |
| --- |

FUEL\_GAUGE\_FLAGS.

## [◆ ](#aa29f7163a1637b6aa8cd6a15dc99d55b)full\_charge\_capacity

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::full\_charge\_capacity |
| --- |

FUEL\_GAUGE\_FULL\_CHARGE\_CAPACITY.

## [◆ ](#a45b20c5118f7ee408d507b94e6cae1dc)relative\_state\_of\_charge

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fuel\_gauge\_prop\_val::relative\_state\_of\_charge |
| --- |

FUEL\_GAUGE\_RELATIVE\_STATE\_OF\_CHARGE.

## [◆ ](#adecf57aa90e2b5d483cfd889ec512400)remaining\_capacity

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::remaining\_capacity |
| --- |

FUEL\_GAUGE\_REMAINING\_CAPACITY.

## [◆ ](#ae716bdf1346dc7767d98526db6083008)runtime\_to\_empty

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::runtime\_to\_empty |
| --- |

FUEL\_GAUGE\_RUNTIME\_TO\_EMPTY.

## [◆ ](#a2c77e8de7fa40fadfa13dfd4c94df804)runtime\_to\_full

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fuel\_gauge\_prop\_val::runtime\_to\_full |
| --- |

FUEL\_GAUGE\_RUNTIME\_TO\_FULL.

## [◆ ](#aa5529fea5cfe765be9b66f5fad96ab2f)sbs\_at\_rate

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) fuel\_gauge\_prop\_val::sbs\_at\_rate |
| --- |

FUEL\_GAUGE\_SBS\_ATRATE.

## [◆ ](#a9b5015878c9a77d9c8330139f94843b7)sbs\_at\_rate\_ok

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fuel\_gauge\_prop\_val::sbs\_at\_rate\_ok |
| --- |

FUEL\_GAUGE\_SBS\_ATRATE\_OK.

## [◆ ](#a7c8b6f9ee98e5b97ddc85b7e72cea4a8)sbs\_at\_rate\_time\_to\_empty

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::sbs\_at\_rate\_time\_to\_empty |
| --- |

FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_EMPTY.

## [◆ ](#aeeeddb48f22b54f90c603d58e9ffa9a5)sbs\_at\_rate\_time\_to\_full

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::sbs\_at\_rate\_time\_to\_full |
| --- |

FUEL\_GAUGE\_SBS\_ATRATE\_TIME\_TO\_FULL.

## [◆ ](#a957025a2a9fb7709e2bf478f15fd31a0)sbs\_mfr\_access\_word

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::sbs\_mfr\_access\_word |
| --- |

FUEL\_GAUGE\_SBS\_MFR\_ACCESS.

## [◆ ](#a7fc0551e303de56e0eb6bdac1ecaccd0)sbs\_mode

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::sbs\_mode |
| --- |

FUEL\_GAUGE\_SBS\_MODE.

## [◆ ](#a818ab7faf8f51d4d1a5c5f070d54b997)sbs\_remaining\_capacity\_alarm

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::sbs\_remaining\_capacity\_alarm |
| --- |

FUEL\_GAUGE\_SBS\_REMAINING\_CAPACITY\_ALARM.

## [◆ ](#aa0e46c727bb31acb5d41ce4bc6d5b106)sbs\_remaining\_time\_alarm

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::sbs\_remaining\_time\_alarm |
| --- |

FUEL\_GAUGE\_SBS\_REMAINING\_TIME\_ALARM.

## [◆ ](#a36528b111568bd1c90859e454610fd9f)temperature

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fuel\_gauge\_prop\_val::temperature |
| --- |

FUEL\_GAUGE\_TEMPERATURE.

## [◆ ](#abec5cadefa09e088620a9598dec9c473)voltage

| int fuel\_gauge\_prop\_val::voltage |
| --- |

FUEL\_GAUGE\_VOLTAGE.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/[fuel\_gauge.h](fuel__gauge_8h_source.md)

- [fuel\_gauge\_prop\_val](unionfuel__gauge__prop__val.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
