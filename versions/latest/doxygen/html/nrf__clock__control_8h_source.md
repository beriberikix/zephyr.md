---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nrf__clock__control_8h_source.html
original_path: doxygen/html/nrf__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_clock\_control.h

[Go to the documentation of this file.](nrf__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2016 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11#include <hal/nrf\_clock.h>

12#include <[zephyr/sys/onoff.h](onoff_8h.md)>

13#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 23](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494)enum [clock\_control\_nrf\_type](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494) {

[ 24](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494ab72ac85df0cde71e7de9b96967eff37f) [CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494ab72ac85df0cde71e7de9b96967eff37f),

[ 25](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494ad21d1fb9a5167a0b3374c1969ff6caf4) [CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494ad21d1fb9a5167a0b3374c1969ff6caf4),

26#if NRF\_CLOCK\_HAS\_HFCLK192M

27 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M,

28#endif

29#if NRF\_CLOCK\_HAS\_HFCLKAUDIO

30 CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO,

31#endif

[ 32](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494a9ad0884bcc0d37d5f178c1a905f36ccc) [CLOCK\_CONTROL\_NRF\_TYPE\_COUNT](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494a9ad0884bcc0d37d5f178c1a905f36ccc)

33};

34

35/\* Define can be used with clock control API instead of enum directly to

36 \* increase code readability.

37 \*/

[ 38](nrf__clock__control_8h.md#a1ecdf70d00c6792cadbe541dc52f167c)#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF \

39 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK)

[ 40](nrf__clock__control_8h.md#a05ef5b77d85a77907083f9b873519cfd)#define CLOCK\_CONTROL\_NRF\_SUBSYS\_LF \

41 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK)

[ 42](nrf__clock__control_8h.md#a3c37235f76338ddfd66c05a470a919e1)#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HF192M \

43 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK192M)

[ 44](nrf__clock__control_8h.md#a27e5bdc4901fd86dd29d12a4bc5409f2)#define CLOCK\_CONTROL\_NRF\_SUBSYS\_HFAUDIO \

45 ((clock\_control\_subsys\_t)CLOCK\_CONTROL\_NRF\_TYPE\_HFCLKAUDIO)

46

[ 48](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7d)enum [nrf\_lfclk\_start\_mode](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7d) {

[ 49](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec) [CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec),

[ 50](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df) [CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df),

[ 51](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4) [CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4),

52};

53

54/\* Define 32KHz clock source \*/

55#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_RC

56#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_RC

57#endif

58#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_XTAL

59#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL

60#endif

61#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_SYNTH

62#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_SYNTH

63#endif

64#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_EXT\_LOW\_SWING

65#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL\_LOW\_SWING

66#endif

67#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_EXT\_FULL\_SWING

68#define CLOCK\_CONTROL\_NRF\_K32SRC NRF\_CLOCK\_LFCLK\_XTAL\_FULL\_SWING

69#endif

70

71/\* Define 32KHz clock accuracy \*/

72#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_500PPM

73#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 0

74#endif

75#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_250PPM

76#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 1

77#endif

78#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_150PPM

79#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 2

80#endif

81#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_100PPM

82#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 3

83#endif

84#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_75PPM

85#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 4

86#endif

87#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_50PPM

88#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 5

89#endif

90#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_30PPM

91#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 6

92#endif

93#ifdef CONFIG\_CLOCK\_CONTROL\_NRF\_K32SRC\_20PPM

94#define CLOCK\_CONTROL\_NRF\_K32SRC\_ACCURACY 7

95#endif

96

98void z\_nrf\_clock\_calibration\_force\_start(void);

99

106int z\_nrf\_clock\_calibration\_count(void);

107

114int z\_nrf\_clock\_calibration\_skips\_count(void);

115

122struct [onoff\_manager](structonoff__manager.md) \*z\_nrf\_clock\_control\_get\_onoff([clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys);

123

132void z\_nrf\_clock\_control\_lf\_on(enum [nrf\_lfclk\_start\_mode](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7d) start\_mode);

133

146void z\_nrf\_clock\_bt\_ctlr\_hf\_request(void);

147

152void z\_nrf\_clock\_bt\_ctlr\_hf\_release(void);

153

154#ifdef \_\_cplusplus

155}

156#endif

157

158#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_NRF\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[device.h](device_8h.md)

[clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db)

void \* clock\_control\_subsys\_t

clock\_control\_subsys\_t is a type to identify a clock controller sub-system.

**Definition** clock\_control.h:56

[nrf\_lfclk\_start\_mode](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7d)

nrf\_lfclk\_start\_mode

LF clock start modes.

**Definition** nrf\_clock\_control.h:48

[CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df)

@ CLOCK\_CONTROL\_NRF\_LF\_START\_AVAILABLE

**Definition** nrf\_clock\_control.h:50

[CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4)

@ CLOCK\_CONTROL\_NRF\_LF\_START\_STABLE

**Definition** nrf\_clock\_control.h:51

[CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT](nrf__clock__control_8h.md#aadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec)

@ CLOCK\_CONTROL\_NRF\_LF\_START\_NOWAIT

**Definition** nrf\_clock\_control.h:49

[clock\_control\_nrf\_type](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494)

clock\_control\_nrf\_type

Clocks handled by the CLOCK peripheral.

**Definition** nrf\_clock\_control.h:23

[CLOCK\_CONTROL\_NRF\_TYPE\_COUNT](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494a9ad0884bcc0d37d5f178c1a905f36ccc)

@ CLOCK\_CONTROL\_NRF\_TYPE\_COUNT

**Definition** nrf\_clock\_control.h:32

[CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494ab72ac85df0cde71e7de9b96967eff37f)

@ CLOCK\_CONTROL\_NRF\_TYPE\_HFCLK

**Definition** nrf\_clock\_control.h:24

[CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK](nrf__clock__control_8h.md#ab64ed97e8dc26da602e521309a300494ad21d1fb9a5167a0b3374c1969ff6caf4)

@ CLOCK\_CONTROL\_NRF\_TYPE\_LFCLK

**Definition** nrf\_clock\_control.h:25

[onoff.h](onoff_8h.md)

[onoff\_manager](structonoff__manager.md)

State associated with an on-off manager.

**Definition** onoff.h:154

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [nrf\_clock\_control.h](nrf__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
