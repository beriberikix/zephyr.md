---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2pwm_2pwm_8h.html
original_path: doxygen/html/dt-bindings_2pwm_2pwm_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwm.h File Reference

[Go to the source code of this file.](dt-bindings_2pwm_2pwm_8h_source.md)

| Macros | |
| --- | --- |
| PWM period set helpers | |
| The period cell in the PWM specifier needs to be provided in nanoseconds.  However, in some applications it is more convenient to use another scale. | |
| #define | [PWM\_NSEC](group__pwm__interface.md#ga17f20d628bcc81d5023c39e4cdfad405)(x) |
|  | Specify PWM period in nanoseconds. |
| #define | [PWM\_USEC](group__pwm__interface.md#ga368f28c8daaee25e546484bd908e675e)(x) |
|  | Specify PWM period in microseconds. |
| #define | [PWM\_MSEC](group__pwm__interface.md#ga1cccc226a23866dd2dcac9467ff3af0e)(x) |
|  | Specify PWM period in milliseconds. |
| #define | [PWM\_SEC](group__pwm__interface.md#ga4da4565d4dbded0efb640bd538cba3c2)(x) |
|  | Specify PWM period in seconds. |
| #define | [PWM\_HZ](group__pwm__interface.md#ga4a5edbee48c4a5706cf75524aef2364a)(x) |
|  | Specify PWM frequency in hertz. |
| #define | [PWM\_KHZ](group__pwm__interface.md#gaf846cf23d31d14296e0cbc1f82a530f4)(x) |
|  | Specify PWM frequency in kilohertz. |
| PWM polarity flags | |
| The PWM\_POLARITY\_\* flags are used with [pwm\_set\_cycles()](group__pwm__interface.md#gaff280789f7b45fdefc354b3f841fe3ef "Set the period and pulse width for a single PWM output."), [pwm\_set()](group__pwm__interface.md#gadd9049c9a56cd9419736b3514e42dc01 "Set the period and pulse width in nanoseconds for a single PWM output.") or [pwm\_configure\_capture()](group__pwm__interface.md#ga9603146d7f9c2690c1e1983113d6c6bb "Configure PWM period/pulse width capture for a single PWM input.") to specify the polarity of a PWM channel.  The flags are on the lower 8bits of the [pwm\_flags\_t](group__pwm__interface.md#gae1dcfb878163da76041efcedf0960fa0 "Provides a type to hold PWM configuration flags.") | |
| #define | [PWM\_POLARITY\_NORMAL](group__pwm__interface.md#ga2c706bbada711f383d7b42f09dace861)   (0 << 0) |
|  | PWM pin normal polarity (active-high pulse). |
| #define | [PWM\_POLARITY\_INVERTED](group__pwm__interface.md#ga930c0ab50f81aeb571af9747947d7fae)   (1 << 0) |
|  | PWM pin inverted polarity (active-low pulse). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pwm](dir_ff747911c88ea6a5644735057b122c0d.md)
- [pwm.h](dt-bindings_2pwm_2pwm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
