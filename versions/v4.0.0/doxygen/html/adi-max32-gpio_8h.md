---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/adi-max32-gpio_8h.html
original_path: doxygen/html/adi-max32-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adi-max32-gpio.h File Reference

[Go to the source code of this file.](adi-max32-gpio_8h_source.md)

| Macros | |
| --- | --- |
| MAX32 GPIO drive flags | |
| MAX32 GPIO drive flags  The drive flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2 "gpio_dt_flags_t") as follows:   - Bit 8: GPIO Supply Voltage Select Selects the voltage rail used for the pin. 0: VDDIO 1: VDDIOH - Bit 9: GPIO Drive Strength Select, MAX32\_GPIO\_DRV\_STRENGTH\_0 = 1mA MAX32\_GPIO\_DRV\_STRENGTH\_1 = 2mA MAX32\_GPIO\_DRV\_STRENGTH\_2 = 4mA MAX32\_GPIO\_DRV\_STRENGTH\_3 = 8mA - Bit 10: Weak pull up selection, Weak Pullup to VDDIO (1MOhm) 0: Disable 1: Enable - Bit 11: Weak pull down selection, Weak Pulldown to VDDIOH (1MOhm) 0: Disable 1: Enable | |
| #define | [MAX32\_GPIO\_VSEL\_POS](group__gpio__interface__max32.md#ga267d4548e80843b5b5678d2050cbef73)   (8U) |
|  | GPIO Voltage Select. |
| #define | [MAX32\_GPIO\_VSEL\_MASK](group__gpio__interface__max32.md#ga57b502aa34453a1af1eb5103221c5bde)   (0x01U << [MAX32\_GPIO\_VSEL\_POS](group__gpio__interface__max32.md#ga267d4548e80843b5b5678d2050cbef73)) |
| #define | [MAX32\_GPIO\_VSEL\_VDDIO](group__gpio__interface__max32.md#ga476d2376c91da2a1cf1bdfd0a7a95198)   (0U << [MAX32\_GPIO\_VSEL\_POS](group__gpio__interface__max32.md#ga267d4548e80843b5b5678d2050cbef73)) |
| #define | [MAX32\_GPIO\_VSEL\_VDDIOH](group__gpio__interface__max32.md#ga964594ce9114dc57a9e50e416e948147)   (1U << [MAX32\_GPIO\_VSEL\_POS](group__gpio__interface__max32.md#ga267d4548e80843b5b5678d2050cbef73)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_POS](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)   (9U) |
|  | GPIO Drive Strength Select. |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_MASK](group__gpio__interface__max32.md#gaefce80e7ae44c9f9397e3b4f02a59893)   (0x03U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_0](group__gpio__interface__max32.md#gaf783f2b803f4772b5bf4c83f616b8a8a)   (0U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_1](group__gpio__interface__max32.md#ga2e0abcd63dbbef23c2368be433c1909d)   (1U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_2](group__gpio__interface__max32.md#gae7199008d9e034361d80355651128fdd)   (2U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_DRV\_STRENGTH\_3](group__gpio__interface__max32.md#gacf1c36bc17e552528ef20d4a8ae67f36)   (3U << [MAX32\_GPIO\_DRV\_STRENGTH\_POS](group__gpio__interface__max32.md#ga8f42437e9d5cbc3bb2d9d58fee643bc5)) |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_UP\_POS](group__gpio__interface__max32.md#gad20918791adf470f4421a2cbc1c7beaf)   (10U) |
|  | GPIO bias weak pull up selection, to VDDIO (1MOhm). |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_UP](group__gpio__interface__max32.md#gac3a2881b03a0e130c0dc174a7aad5b04)   (1U << [MAX32\_GPIO\_WEAK\_PULL\_UP\_POS](group__gpio__interface__max32.md#gad20918791adf470f4421a2cbc1c7beaf)) |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS](group__gpio__interface__max32.md#ga81dd2d4a0dbd87b5346c65e608f5ea45)   (11U) |
|  | GPIO bias weak pull down selection, to VDDIOH (1MOhm). |
| #define | [MAX32\_GPIO\_WEAK\_PULL\_DOWN](group__gpio__interface__max32.md#gaa2a5bc76ccfd583c11ee5f18015871be)   (1U << [MAX32\_GPIO\_WEAK\_PULL\_DOWN\_POS](group__gpio__interface__max32.md#ga81dd2d4a0dbd87b5346c65e608f5ea45)) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [adi-max32-gpio.h](adi-max32-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
