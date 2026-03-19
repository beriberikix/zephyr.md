---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/timestamp_8h_source.html
original_path: doxygen/html/timestamp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timestamp.h

[Go to the documentation of this file.](timestamp_8h.md)

1/\*

2 \* Copyright (c) 2012-2015 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* @file macroses for measuring time in benchmarking tests

9 \*

10 \* This file contains the macroses for taking and converting time for

11 \* benchmarking tests.

12 \*/

13

14#ifndef \_TIMESTAMP\_H\_

15#define \_TIMESTAMP\_H\_

16#include <[zephyr/kernel.h](kernel_8h.md)>

17

18#include <[limits.h](limits_8h.md)>

19#if defined(\_\_GNUC\_\_)

20#include <[zephyr/test\_asm\_inline\_gcc.h](test__asm__inline__gcc_8h.md)>

21#else

22#include <zephyr/test\_asm\_inline\_other.h>

23#endif

24

25

[ 26](timestamp_8h.md#a95c5be89ea7bce90d2a8a11472ebd2c6)#define TICK\_SYNCH() k\_sleep(K\_TICKS(1))

27

[ 28](timestamp_8h.md#a1b4134f508183af47ef3deff07be4a54)#define OS\_GET\_TIME() k\_cycle\_get\_32()

29

30/\* time necessary to read the time \*/

31extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tm\_off](timestamp_8h.md#a2503eba6a8f75337fe8c7ee84b0b3b21);

32

[ 33](timestamp_8h.md#abb03327df49c0544f863a239a9af0086)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [TIME\_STAMP\_DELTA\_GET](timestamp_8h.md#abb03327df49c0544f863a239a9af0086)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts)

34{

35 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) t;

36

37 /\* serialize so OS\_GET\_TIME() is not reordered \*/

38 timestamp\_serialize();

39

40 t = [OS\_GET\_TIME](timestamp_8h.md#a1b4134f508183af47ef3deff07be4a54)();

41 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) res = (t >= ts) ? (t - ts) : (ULONG\_MAX - ts + t);

42

43 if (ts > 0) {

44 res -= [tm\_off](timestamp_8h.md#a2503eba6a8f75337fe8c7ee84b0b3b21);

45 }

46 return res;

47}

48

49/\*

50 \* Routine initializes the benchmark timing measurement

51 \* The function sets up the global variable tm\_off

52 \*/

[ 53](timestamp_8h.md#a7d2ae16b9d290b7ab914f71155c5e56d)static inline void [bench\_test\_init](timestamp_8h.md#a7d2ae16b9d290b7ab914f71155c5e56d)(void)

54{

55 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) t = [OS\_GET\_TIME](timestamp_8h.md#a1b4134f508183af47ef3deff07be4a54)();

56

57 [tm\_off](timestamp_8h.md#a2503eba6a8f75337fe8c7ee84b0b3b21) = [OS\_GET\_TIME](timestamp_8h.md#a1b4134f508183af47ef3deff07be4a54)() - t;

58}

59

60

61/\* timestamp for checks \*/

[ 62](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44)static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44);

63

64/\*

65 \* Routines are invoked before and after the benchmark and check

66 \* if benchmarking code took less time than necessary for the

67 \* high precision timer register overflow.

68 \* Functions modify the timestamp\_check global variable.

69 \*/

[ 70](timestamp_8h.md#ac476d41973f921a386c9a8341296dcfd)static inline void [bench\_test\_start](timestamp_8h.md#ac476d41973f921a386c9a8341296dcfd)(void)

71{

72 [timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44) = 0;

73 /\* before reading time we synchronize to the start of the timer tick \*/

74 [TICK\_SYNCH](timestamp_8h.md#a95c5be89ea7bce90d2a8a11472ebd2c6)();

75 [timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44) = [k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)(&[timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44));

76}

77

78

79/\* returns 0 if the completed within a second and -1 if not \*/

[ 80](timestamp_8h.md#a6555ffaf6ca7b4f5b81477faa8f43f53)static inline int [bench\_test\_end](timestamp_8h.md#a6555ffaf6ca7b4f5b81477faa8f43f53)(void)

81{

82 [timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44) = [k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)(&[timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44));

83

84 /\* Flag an error if the test ran for more than a second.

85 \* (Note: Existing benchmarks have CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC=1 set,

86 \* in such configs this check can be an indicator of whether

87 \* timer tick interrupt overheads too are getting accounted towards

88 \* benchmark time)

89 \*/

90 if ([timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44) >= [MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd)) {

91 return -1;

92 }

93 return 0;

94}

95

96/\*

97 \* Returns -1 if number of ticks cause high precision timer counter

98 \* overflow and 0 otherwise

99 \* Called after bench\_test\_end to see if we still can use timing

100 \* results or is it completely invalid

101 \*/

[ 102](timestamp_8h.md#a54d527f8fde477822ad2044579a7edd3)static inline int [high\_timer\_overflow](timestamp_8h.md#a54d527f8fde477822ad2044579a7edd3)(void)

103{

104 /\* Check if the time elapsed in msec is sufficient to trigger an

105 \* overflow of the high precision timer

106 \*/

107 if ([timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44) >= ([k\_cyc\_to\_ns\_floor64](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)(UINT\_MAX) /

108 ([NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)))) {

109 return -1;

110 }

111 return 0;

112}

113

114#endif /\* \_TIMESTAMP\_H\_ \*/

[NSEC\_PER\_USEC](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5)

#define NSEC\_PER\_USEC

number of nanoseconds per microsecond

**Definition** sys\_clock.h:83

[MSEC\_PER\_SEC](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd)

#define MSEC\_PER\_SEC

number of milliseconds per second

**Definition** sys\_clock.h:92

[USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)

#define USEC\_PER\_MSEC

number of microseconds per millisecond

**Definition** sys\_clock.h:89

[k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80)

static int64\_t k\_uptime\_delta(int64\_t \*reftime)

Get elapsed time.

**Definition** kernel.h:1908

[k\_cyc\_to\_ns\_floor64](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)

#define k\_cyc\_to\_ns\_floor64(t)

Convert hardware cycles to nanoseconds.

**Definition** time\_units.h:1435

[kernel.h](kernel_8h.md)

Public kernel APIs.

[limits.h](limits_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[test\_asm\_inline\_gcc.h](test__asm__inline__gcc_8h.md)

[OS\_GET\_TIME](timestamp_8h.md#a1b4134f508183af47ef3deff07be4a54)

#define OS\_GET\_TIME()

**Definition** timestamp.h:28

[tm\_off](timestamp_8h.md#a2503eba6a8f75337fe8c7ee84b0b3b21)

uint32\_t tm\_off

[high\_timer\_overflow](timestamp_8h.md#a54d527f8fde477822ad2044579a7edd3)

static int high\_timer\_overflow(void)

**Definition** timestamp.h:102

[timestamp\_check](timestamp_8h.md#a5a399603fca75f3004d45720f03f9d44)

static int64\_t timestamp\_check

**Definition** timestamp.h:62

[bench\_test\_end](timestamp_8h.md#a6555ffaf6ca7b4f5b81477faa8f43f53)

static int bench\_test\_end(void)

**Definition** timestamp.h:80

[bench\_test\_init](timestamp_8h.md#a7d2ae16b9d290b7ab914f71155c5e56d)

static void bench\_test\_init(void)

**Definition** timestamp.h:53

[TICK\_SYNCH](timestamp_8h.md#a95c5be89ea7bce90d2a8a11472ebd2c6)

#define TICK\_SYNCH()

**Definition** timestamp.h:26

[TIME\_STAMP\_DELTA\_GET](timestamp_8h.md#abb03327df49c0544f863a239a9af0086)

static uint32\_t TIME\_STAMP\_DELTA\_GET(uint32\_t ts)

**Definition** timestamp.h:33

[bench\_test\_start](timestamp_8h.md#ac476d41973f921a386c9a8341296dcfd)

static void bench\_test\_start(void)

**Definition** timestamp.h:70

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [timestamp.h](timestamp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
