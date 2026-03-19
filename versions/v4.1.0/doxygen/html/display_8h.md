---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/display_8h.html
original_path: doxygen/html/display_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

display.h File Reference

Public API for display drivers and applications.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/dt-bindings/display/panel.h](panel_8h_source.md)>`

[Go to the source code of this file.](display_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [display\_capabilities](structdisplay__capabilities.md) |
|  | Structure holding display capabilities. [More...](structdisplay__capabilities.md#details) |
| struct | [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) |
|  | Structure to describe display data buffer layout. [More...](structdisplay__buffer__descriptor.md#details) |
| struct | [display\_driver\_api](structdisplay__driver__api.md) |
|  | Display driver API API which a display driver should expose. [More...](structdisplay__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [DISPLAY\_BITS\_PER\_PIXEL](group__display__interface.md#ga3b305be04da5921ca4087498627dc061)(fmt) |
|  | Bits required per pixel for display format. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [display\_blanking\_on\_api](group__display__interface.md#gacf66a054396ccd8e178591b8fc98ff4d)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to turn on display blanking See [display\_blanking\_on()](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4 "Turn display blanking on.") for argument description. |
| typedef int(\* | [display\_blanking\_off\_api](group__display__interface.md#gab23bbd9305792d6e37d2e4ff91a2b175)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to turn off display blanking See [display\_blanking\_off()](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d "Turn display blanking off.") for argument description. |
| typedef int(\* | [display\_write\_api](group__display__interface.md#ga5cab904b24062fdea531f450a8e5c367)) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, const void \*buf) |
|  | Callback API for writing data to the display See [display\_write()](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18 "Write data to display.") for argument description. |
| typedef int(\* | [display\_read\_api](group__display__interface.md#ga9ed51d3f666f747d9fb7f1f7746611b3)) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, void \*buf) |
|  | Callback API for reading data from the display See [display\_read()](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc "Read data from display.") for argument description. |
| typedef void \*(\* | [display\_get\_framebuffer\_api](group__display__interface.md#ga6dd281032ad400d3adc7f5f812c5fe12)) (const struct [device](structdevice.md) \*dev) |
|  | Callback API to get framebuffer pointer See [display\_get\_framebuffer()](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8 "Get pointer to framebuffer for direct access.") for argument description. |
| typedef int(\* | [display\_set\_brightness\_api](group__display__interface.md#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
|  | Callback API to set display brightness See [display\_set\_brightness()](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c "Set the brightness of the display.") for argument description. |
| typedef int(\* | [display\_set\_contrast\_api](group__display__interface.md#gadf115352908f94b0a0bf225dbdd8ee85)) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast) |
|  | Callback API to set display contrast See [display\_set\_contrast()](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27 "Set the contrast of the display.") for argument description. |
| typedef void(\* | [display\_get\_capabilities\_api](group__display__interface.md#ga474f85a33aef019dddb1c720ea23f3fb)) (const struct [device](structdevice.md) \*dev, struct [display\_capabilities](structdisplay__capabilities.md) \*capabilities) |
|  | Callback API to get display capabilities See [display\_get\_capabilities()](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50 "Get display capabilities.") for argument description. |
| typedef int(\* | [display\_set\_pixel\_format\_api](group__display__interface.md#ga2637286cf3a97c2b532bb33f22263303)) (const struct [device](structdevice.md) \*dev, const enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format) |
|  | Callback API to set pixel format used by the display See [display\_set\_pixel\_format()](group__display__interface.md#ga7ede828663090760c2558a231d9f2150 "Set pixel format used by the display.") for argument description. |
| typedef int(\* | [display\_set\_orientation\_api](group__display__interface.md#gaff3b76a6601cf176782be940139ccb48)) (const struct [device](structdevice.md) \*dev, const enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) orientation) |
|  | Callback API to set orientation used by the display See [display\_set\_orientation()](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394 "Set display orientation.") for argument description. |

| Enumerations | |
| --- | --- |
| enum | [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) {     [PIXEL\_FORMAT\_RGB\_888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a) = BIT(0) , [PIXEL\_FORMAT\_MONO01](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c) = BIT(1) , [PIXEL\_FORMAT\_MONO10](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c) = BIT(2) , [PIXEL\_FORMAT\_ARGB\_8888](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9) = BIT(3) ,     [PIXEL\_FORMAT\_RGB\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16) = BIT(4) , [PIXEL\_FORMAT\_BGR\_565](group__display__interface.md#ggac346bc56771052a8fe919c3ec23d7c9cae9fdd617aaf49148d4c4cb5d47189289) = BIT(5)   } |
|  | Display pixel formats. [More...](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) |
| enum | [display\_screen\_info](group__display__interface.md#ga23030b6c27446c4579103fe38e821341) {     [SCREEN\_INFO\_MONO\_VTILED](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804) = BIT(0) , [SCREEN\_INFO\_MONO\_MSB\_FIRST](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d) = BIT(1) , [SCREEN\_INFO\_EPD](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85) = BIT(2) , [SCREEN\_INFO\_DOUBLE\_BUFFER](group__display__interface.md#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842) = BIT(3) ,     [SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH](group__display__interface.md#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1) = BIT(4)   } |
|  | Display screen information. [More...](group__display__interface.md#ga23030b6c27446c4579103fe38e821341) |
| enum | [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) { [DISPLAY\_ORIENTATION\_NORMAL](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2) , [DISPLAY\_ORIENTATION\_ROTATED\_90](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc) , [DISPLAY\_ORIENTATION\_ROTATED\_180](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29) , [DISPLAY\_ORIENTATION\_ROTATED\_270](group__display__interface.md#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4) } |
|  | Enumeration with possible display orientation. [More...](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) |

| Functions | |
| --- | --- |
| static int | [display\_write](group__display__interface.md#ga3a5114b4537039fc4d3258678b82cd18) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, const void \*buf) |
|  | Write data to display. |
| static int | [display\_read](group__display__interface.md#ga3f497776520b0eac16b8aea80ccbbcfc) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, const struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, void \*buf) |
|  | Read data from display. |
| static void \* | [display\_get\_framebuffer](group__display__interface.md#ga4b66d380e46909caaa7317857f84a9e8) (const struct [device](structdevice.md) \*dev) |
|  | Get pointer to framebuffer for direct access. |
| static int | [display\_blanking\_on](group__display__interface.md#gac6ad1f33067165e4c3bf7c0c345bb4e4) (const struct [device](structdevice.md) \*dev) |
|  | Turn display blanking on. |
| static int | [display\_blanking\_off](group__display__interface.md#ga4d9e288891a6bde679c3aa00b9913e1d) (const struct [device](structdevice.md) \*dev) |
|  | Turn display blanking off. |
| static int | [display\_set\_brightness](group__display__interface.md#gad5cdeb245d17c8d680a5843b3cce1f8c) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) brightness) |
|  | Set the brightness of the display. |
| static int | [display\_set\_contrast](group__display__interface.md#ga855c72f72238b25f23e95e50546e2f27) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) contrast) |
|  | Set the contrast of the display. |
| static void | [display\_get\_capabilities](group__display__interface.md#ga6a13e42773be13b141ebd8f047f8db50) (const struct [device](structdevice.md) \*dev, struct [display\_capabilities](structdisplay__capabilities.md) \*capabilities) |
|  | Get display capabilities. |
| static int | [display\_set\_pixel\_format](group__display__interface.md#ga7ede828663090760c2558a231d9f2150) (const struct [device](structdevice.md) \*dev, const enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixel\_format) |
|  | Set pixel format used by the display. |
| static int | [display\_set\_orientation](group__display__interface.md#ga4e0a4dc2e434144874af014b8e7c4394) (const struct [device](structdevice.md) \*dev, const enum [display\_orientation](group__display__interface.md#gac59b091a3ed39431ab97a5f19fdc4855) orientation) |
|  | Set display orientation. |

## Detailed Description

Public API for display drivers and applications.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [display.h](display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
