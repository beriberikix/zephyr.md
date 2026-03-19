---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lp50xx_8h.html
original_path: doxygen/html/lp50xx_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lp50xx.h File Reference

[Go to the source code of this file.](lp50xx_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4)   3 |
| #define | [LP5009\_MAX\_LEDS](#a0cc3344b5a859f2463bda44624cdac6a)   3 |
| #define | [LP5012\_MAX\_LEDS](#ad668908bcff262bf5a27c72cebeabb65)   4 |
| #define | [LP5018\_MAX\_LEDS](#a2ca3a6eb319ad14279fca6115f5d4fca)   6 |
| #define | [LP5024\_MAX\_LEDS](#a45b1d97cb6478e9231a2e22c99d27e6f)   8 |
| #define | [LP5030\_MAX\_LEDS](#ad1c6c734b5222d0d96579c7efd96288f)   10 |
| #define | [LP5036\_MAX\_LEDS](#a45f40ffa12fa78919030081bc158bdf5)   12 |
| #define | [LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8)   0 |
| #define | [LP50XX\_BANK\_BRIGHT\_CHAN](#ac26b03a074670393b10826e35acc92e3)   [LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8) |
| #define | [LP50XX\_BANK\_COL1\_CHAN](#a3220c920a91992087a21fbbf160b5a71)(led) |
| #define | [LP50XX\_BANK\_COL2\_CHAN](#a17f11dcbce0cea164a4a506566ee81b9)(led) |
| #define | [LP50XX\_BANK\_COL3\_CHAN](#a9292372cafb9882f6e573063bdbaf99a)(led) |
| #define | [LP50XX\_LED\_BRIGHT\_CHAN\_BASE](#aedaed7d9a9feb6c2e18ff646dd4f0741)   4 |
| #define | [LP50XX\_LED\_BRIGHT\_CHAN](#a7421dfa3aa4a135fa6d937d467ee7b44)(led) |
| #define | [LP5012\_LED\_COL\_CHAN\_BASE](#a46f005a17ecfeb7ea241d18ed2503029)   8 |
| #define | [LP5012\_LED\_COL1\_CHAN](#ae1461195d755ea951b6bb2ce3f45392d)(led) |
| #define | [LP5012\_LED\_COL2\_CHAN](#ab70cfd7eb411f1f2f6d8370452775ccd)(led) |
| #define | [LP5012\_LED\_COL3\_CHAN](#ae24a2d64b31fb8de59a119b6c1f63b15)(led) |
| #define | [LP5024\_LED\_COL\_CHAN\_BASE](#ac48720b13bd1aa213a4d4951ed96066a)   12 |
| #define | [LP5024\_LED\_COL1\_CHAN](#ab86853d9f0417c2f1afba73cfacdfcd2)(led) |
| #define | [LP5024\_LED\_COL2\_CHAN](#af0e0393357be9850c1944210f28aa32a)(led) |
| #define | [LP5024\_LED\_COL3\_CHAN](#a1df2b6f63b73b1b555a08e06f4da0c2d)(led) |
| #define | [LP5036\_LED\_COL\_CHAN\_BASE](#ae3dcf20db935d5cb64e62bffd44693d1)   16 |
| #define | [LP5036\_LED\_COL1\_CHAN](#a24f8253051a6c6622c3c9d8c938a1c44)(led) |
| #define | [LP5036\_LED\_COL2\_CHAN](#a72cfa3e69e9b9a7ee16a8dd243cc0782)(led) |
| #define | [LP5036\_LED\_COL3\_CHAN](#a4d4d92b15651f34f7c1d9747b10f4267)(led) |

## Macro Definition Documentation

## [◆ ](#a0cc3344b5a859f2463bda44624cdac6a)LP5009\_MAX\_LEDS

| #define LP5009\_MAX\_LEDS   3 |
| --- |

## [◆ ](#ae1461195d755ea951b6bb2ce3f45392d)LP5012\_LED\_COL1\_CHAN

| #define LP5012\_LED\_COL1\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5012\_LED\_COL\_CHAN\_BASE](#a46f005a17ecfeb7ea241d18ed2503029) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4))

[LP5012\_LED\_COL\_CHAN\_BASE](#a46f005a17ecfeb7ea241d18ed2503029)

#define LP5012\_LED\_COL\_CHAN\_BASE

**Definition** lp50xx.h:44

[LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4)

#define LP50XX\_COLORS\_PER\_LED

**Definition** lp50xx.h:12

## [◆ ](#ab70cfd7eb411f1f2f6d8370452775ccd)LP5012\_LED\_COL2\_CHAN

| #define LP5012\_LED\_COL2\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5012\_LED\_COL\_CHAN\_BASE](#a46f005a17ecfeb7ea241d18ed2503029) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4) + 1)

## [◆ ](#ae24a2d64b31fb8de59a119b6c1f63b15)LP5012\_LED\_COL3\_CHAN

| #define LP5012\_LED\_COL3\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5012\_LED\_COL\_CHAN\_BASE](#a46f005a17ecfeb7ea241d18ed2503029) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4) + 2)

## [◆ ](#a46f005a17ecfeb7ea241d18ed2503029)LP5012\_LED\_COL\_CHAN\_BASE

| #define LP5012\_LED\_COL\_CHAN\_BASE   8 |
| --- |

## [◆ ](#ad668908bcff262bf5a27c72cebeabb65)LP5012\_MAX\_LEDS

| #define LP5012\_MAX\_LEDS   4 |
| --- |

## [◆ ](#a2ca3a6eb319ad14279fca6115f5d4fca)LP5018\_MAX\_LEDS

| #define LP5018\_MAX\_LEDS   6 |
| --- |

## [◆ ](#ab86853d9f0417c2f1afba73cfacdfcd2)LP5024\_LED\_COL1\_CHAN

| #define LP5024\_LED\_COL1\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5024\_LED\_COL\_CHAN\_BASE](#ac48720b13bd1aa213a4d4951ed96066a) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4))

[LP5024\_LED\_COL\_CHAN\_BASE](#ac48720b13bd1aa213a4d4951ed96066a)

#define LP5024\_LED\_COL\_CHAN\_BASE

**Definition** lp50xx.h:52

## [◆ ](#af0e0393357be9850c1944210f28aa32a)LP5024\_LED\_COL2\_CHAN

| #define LP5024\_LED\_COL2\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5024\_LED\_COL\_CHAN\_BASE](#ac48720b13bd1aa213a4d4951ed96066a) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4) + 1)

## [◆ ](#a1df2b6f63b73b1b555a08e06f4da0c2d)LP5024\_LED\_COL3\_CHAN

| #define LP5024\_LED\_COL3\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5024\_LED\_COL\_CHAN\_BASE](#ac48720b13bd1aa213a4d4951ed96066a) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4) + 2)

## [◆ ](#ac48720b13bd1aa213a4d4951ed96066a)LP5024\_LED\_COL\_CHAN\_BASE

| #define LP5024\_LED\_COL\_CHAN\_BASE   12 |
| --- |

## [◆ ](#a45b1d97cb6478e9231a2e22c99d27e6f)LP5024\_MAX\_LEDS

| #define LP5024\_MAX\_LEDS   8 |
| --- |

## [◆ ](#ad1c6c734b5222d0d96579c7efd96288f)LP5030\_MAX\_LEDS

| #define LP5030\_MAX\_LEDS   10 |
| --- |

## [◆ ](#a24f8253051a6c6622c3c9d8c938a1c44)LP5036\_LED\_COL1\_CHAN

| #define LP5036\_LED\_COL1\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5036\_LED\_COL\_CHAN\_BASE](#ae3dcf20db935d5cb64e62bffd44693d1) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4))

[LP5036\_LED\_COL\_CHAN\_BASE](#ae3dcf20db935d5cb64e62bffd44693d1)

#define LP5036\_LED\_COL\_CHAN\_BASE

**Definition** lp50xx.h:60

## [◆ ](#a72cfa3e69e9b9a7ee16a8dd243cc0782)LP5036\_LED\_COL2\_CHAN

| #define LP5036\_LED\_COL2\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5036\_LED\_COL\_CHAN\_BASE](#ae3dcf20db935d5cb64e62bffd44693d1) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4) + 1)

## [◆ ](#a4d4d92b15651f34f7c1d9747b10f4267)LP5036\_LED\_COL3\_CHAN

| #define LP5036\_LED\_COL3\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP5036\_LED\_COL\_CHAN\_BASE](#ae3dcf20db935d5cb64e62bffd44693d1) + led \* [LP50XX\_COLORS\_PER\_LED](#a97594c95d9c99b55de0ef7e1624e44e4) + 2)

## [◆ ](#ae3dcf20db935d5cb64e62bffd44693d1)LP5036\_LED\_COL\_CHAN\_BASE

| #define LP5036\_LED\_COL\_CHAN\_BASE   16 |
| --- |

## [◆ ](#a45f40ffa12fa78919030081bc158bdf5)LP5036\_MAX\_LEDS

| #define LP5036\_MAX\_LEDS   12 |
| --- |

## [◆ ](#ac26b03a074670393b10826e35acc92e3)LP50XX\_BANK\_BRIGHT\_CHAN

| #define LP50XX\_BANK\_BRIGHT\_CHAN   [LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8) |
| --- |

## [◆ ](#ad660acc79b6312608072cb21edc902d8)LP50XX\_BANK\_CHAN\_BASE

| #define LP50XX\_BANK\_CHAN\_BASE   0 |
| --- |

## [◆ ](#a3220c920a91992087a21fbbf160b5a71)LP50XX\_BANK\_COL1\_CHAN

| #define LP50XX\_BANK\_COL1\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8) + 1)

[LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8)

#define LP50XX\_BANK\_CHAN\_BASE

**Definition** lp50xx.h:26

## [◆ ](#a17f11dcbce0cea164a4a506566ee81b9)LP50XX\_BANK\_COL2\_CHAN

| #define LP50XX\_BANK\_COL2\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8) + 2)

## [◆ ](#a9292372cafb9882f6e573063bdbaf99a)LP50XX\_BANK\_COL3\_CHAN

| #define LP50XX\_BANK\_COL3\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP50XX\_BANK\_CHAN\_BASE](#ad660acc79b6312608072cb21edc902d8) + 3)

## [◆ ](#a97594c95d9c99b55de0ef7e1624e44e4)LP50XX\_COLORS\_PER\_LED

| #define LP50XX\_COLORS\_PER\_LED   3 |
| --- |

## [◆ ](#a7421dfa3aa4a135fa6d937d467ee7b44)LP50XX\_LED\_BRIGHT\_CHAN

| #define LP50XX\_LED\_BRIGHT\_CHAN | ( |  | *led* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([LP50XX\_LED\_BRIGHT\_CHAN\_BASE](#aedaed7d9a9feb6c2e18ff646dd4f0741) + led)

[LP50XX\_LED\_BRIGHT\_CHAN\_BASE](#aedaed7d9a9feb6c2e18ff646dd4f0741)

#define LP50XX\_LED\_BRIGHT\_CHAN\_BASE

**Definition** lp50xx.h:33

## [◆ ](#aedaed7d9a9feb6c2e18ff646dd4f0741)LP50XX\_LED\_BRIGHT\_CHAN\_BASE

| #define LP50XX\_LED\_BRIGHT\_CHAN\_BASE   4 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led](dir_c34d419ad899f160d883f47e8e6b2aca.md)
- [lp50xx.h](lp50xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
