---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/input_8h.html
original_path: doxygen/html/input_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/dt-bindings/input/input-event-codes.h](input-event-codes_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](input_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [input\_event](structinput__event.md) |
|  | Input event structure. [More...](structinput__event.md#details) |
| struct | [input\_listener](structinput__listener.md) |
|  | Input listener callback structure. [More...](structinput__listener.md#details) |

| Macros | |
| --- | --- |
| #define | [INPUT\_CALLBACK\_DEFINE](group__input__interface.md#gacd0045487023fe9652cbfe46f3b556b6)(\_dev, \_callback) |
|  | Register a callback structure for input events. |

| Functions | |
| --- | --- |
| int | [input\_report](group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Report a new input event. |
| static int | [input\_report\_key](group__input__interface.md#gaeb9fa2d4bb990e67ab0a2bd20a141d20) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Report a new [INPUT\_EV\_KEY](group__input__events.md#ga4a517c31bdbdd1bd82ba456d256ef1f1 "INPUT_EV_KEY") input event, note that value is converted to either 0 or 1. |
| static int | [input\_report\_rel](group__input__interface.md#gaffbf85b82d0cede81410dda8ed559201) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Report a new [INPUT\_EV\_REL](group__input__events.md#ga02de6c85efab3d21eb81e88e54d58e03 "INPUT_EV_REL") input event. |
| static int | [input\_report\_abs](group__input__interface.md#gaf94bdc8ca673de7947e011872f64ce6c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Report a new [INPUT\_EV\_ABS](group__input__events.md#gaa6bcd6755fbdb3eb103f03a72759ce4f "INPUT_EV_ABS") input event. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [input\_queue\_empty](group__input__interface.md#ga401a03bb89dd59d518f7466a035571da) (void) |
|  | Returns true if the input queue is empty. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input.h](input_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
