---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/xen_2public_2sched_8h_source.html
original_path: doxygen/html/xen_2public_2sched_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sched.h

[Go to the documentation of this file.](xen_2public_2sched_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* sched.h

5 \*

6 \* Scheduler state interactions

7 \*

8 \* Permission is hereby granted, free of charge, to any person obtaining a copy

9 \* of this software and associated documentation files (the "Software"), to

10 \* deal in the Software without restriction, including without limitation the

11 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

12 \* sell copies of the Software, and to permit persons to whom the Software is

13 \* furnished to do so, subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be included in

16 \* all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

19 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

20 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

21 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

22 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

23 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

24 \* DEALINGS IN THE SOFTWARE.

25 \*

26 \* Copyright (c) 2005, Keir Fraser <keir@xensource.com>

27 \*/

28

29#ifndef \_\_XEN\_PUBLIC\_SCHED\_H\_\_

30#define \_\_XEN\_PUBLIC\_SCHED\_H\_\_

31

32#include "[event\_channel.h](event__channel_8h.md)"

33

34/\*

35 \* `incontents 150 sched Guest Scheduler Operations

36 \*

37 \* The SCHEDOP interface provides mechanisms for a guest to interact

38 \* with the scheduler, including yield, blocking and shutting itself

39 \* down.

40 \*/

41

42/\*

43 \* The prototype for this hypercall is:

44 \* ` long HYPERVISOR\_sched\_op(enum sched\_op cmd, void \*arg, ...)

45 \*

46 \* @cmd == SCHEDOP\_??? (scheduler operation).

47 \* @arg == Operation-specific extra argument(s), as described below.

48 \* ... == Additional Operation-specific extra arguments, described below.

49 \*

50 \* Versions of Xen prior to 3.0.2 provided only the following legacy version

51 \* of this hypercall, supporting only the commands yield, block and shutdown:

52 \* long sched\_op(int cmd, unsigned long arg)

53 \* @cmd == SCHEDOP\_??? (scheduler operation).

54 \* @arg == 0 (SCHEDOP\_yield and SCHEDOP\_block)

55 \* == SHUTDOWN\_\* code (SCHEDOP\_shutdown)

56 \*

57 \* This legacy version is available to new guests as:

58 \* ` long HYPERVISOR\_sched\_op\_compat(enum sched\_op cmd, unsigned long arg)

59 \*/

60

61/\*

62 \* Voluntarily yield the CPU.

63 \* @arg == NULL.

64 \*/

[ 65](xen_2public_2sched_8h.md#ac6729986fa8f1233fc665ff29e60d4fe)#define SCHEDOP\_yield 0

66

67/\*

68 \* Block execution of this VCPU until an event is received for processing.

69 \* If called with event upcalls masked, this operation will atomically

70 \* reenable event delivery and check for pending events before blocking the

71 \* VCPU. This avoids a "wakeup waiting" race.

72 \* @arg == NULL.

73 \*/

[ 74](xen_2public_2sched_8h.md#a566d14ea508950d32a5b1191642c7315)#define SCHEDOP\_block 1

75

76/\*

77 \* Halt execution of this domain (all VCPUs) and notify the system controller.

78 \* @arg == pointer to sched\_shutdown\_t structure.

79 \*

80 \* If the sched\_shutdown\_t reason is SHUTDOWN\_suspend then

81 \* x86 PV guests must also set RDX (EDX for 32-bit guests) to the MFN

82 \* of the guest's start info page. RDX/EDX is the third hypercall

83 \* argument.

84 \*

85 \* In addition, which reason is SHUTDOWN\_suspend this hypercall

86 \* returns 1 if suspend was cancelled or the domain was merely

87 \* checkpointed, and 0 if it is resuming in a new domain.

88 \*/

[ 89](xen_2public_2sched_8h.md#ac5b250debc01324d7a41c7ae7d6a3b54)#define SCHEDOP\_shutdown 2

90

91/\*

92 \* Poll a set of event-channel ports. Return when one or more are pending. An

93 \* optional timeout may be specified.

94 \* @arg == pointer to sched\_poll\_t structure.

95 \*/

[ 96](xen_2public_2sched_8h.md#aaf686f8f7b11629bf454d1610c2eb242)#define SCHEDOP\_poll 3

97

98/\*

99 \* Declare a shutdown for another domain. The main use of this function is

100 \* in interpreting shutdown requests and reasons for fully-virtualized

101 \* domains. A para-virtualized domain may use SCHEDOP\_shutdown directly.

102 \* @arg == pointer to sched\_remote\_shutdown\_t structure.

103 \*/

[ 104](xen_2public_2sched_8h.md#a5d976e3048f113e09d37115c084bf5dc)#define SCHEDOP\_remote\_shutdown 4

105

106/\*

107 \* Latch a shutdown code, so that when the domain later shuts down it

108 \* reports this code to the control tools.

109 \* @arg == sched\_shutdown\_t, as for SCHEDOP\_shutdown.

110 \*/

[ 111](xen_2public_2sched_8h.md#a2cb33c474fb6d6f7063fde4d3ad06835)#define SCHEDOP\_shutdown\_code 5

112

113/\*

114 \* Setup, poke and destroy a domain watchdog timer.

115 \* @arg == pointer to sched\_watchdog\_t structure.

116 \* With id == 0, setup a domain watchdog timer to cause domain shutdown

117 \* after timeout, returns watchdog id.

118 \* With id != 0 and timeout == 0, destroy domain watchdog timer.

119 \* With id != 0 and timeout != 0, poke watchdog timer and set new timeout.

120 \*/

[ 121](xen_2public_2sched_8h.md#a21298626bad1ba1ca03ed538f6b66677)#define SCHEDOP\_watchdog 6

122

123/\*

124 \* Override the current vcpu affinity by pinning it to one physical cpu or

125 \* undo this override restoring the previous affinity.

126 \* @arg == pointer to sched\_pin\_override\_t structure.

127 \*

128 \* A negative pcpu value will undo a previous pin override and restore the

129 \* previous cpu affinity.

130 \* This call is allowed for the hardware domain only and requires the cpu

131 \* to be part of the domain's cpupool.

132 \*/

[ 133](xen_2public_2sched_8h.md#a6ddcfa16b3a1af5c84360995a13d60ed)#define SCHEDOP\_pin\_override 7

134

[ 135](structsched__shutdown.md)struct [sched\_shutdown](structsched__shutdown.md) {

[ 136](structsched__shutdown.md#ab68ec3e008c9d9eab5f48ad5f55346db) unsigned int [reason](structsched__shutdown.md#ab68ec3e008c9d9eab5f48ad5f55346db); /\* SHUTDOWN\_\* => enum sched\_shutdown\_reason \*/

137};

[ 138](xen_2public_2sched_8h.md#ab7dec9bb2853d145f6e8035e81aacea9)typedef struct [sched\_shutdown](structsched__shutdown.md) [sched\_shutdown\_t](xen_2public_2sched_8h.md#ab7dec9bb2853d145f6e8035e81aacea9);

[ 139](xen_2public_2sched_8h.md#add69380a2fa2c48d1b3d0a2fc9d4c48d)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([sched\_shutdown\_t](xen_2public_2sched_8h.md#ab7dec9bb2853d145f6e8035e81aacea9));

140

[ 141](structsched__poll.md)struct [sched\_poll](structsched__poll.md) {

[ 142](structsched__poll.md#ae3edf9e983927d88d84aea48015e7619) [XEN\_GUEST\_HANDLE](structsched__poll.md#ae3edf9e983927d88d84aea48015e7619)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)) ports;

[ 143](structsched__poll.md#a2dd2e52e0db41c71033a2d64fe984f16) unsigned int [nr\_ports](structsched__poll.md#a2dd2e52e0db41c71033a2d64fe984f16);

[ 144](structsched__poll.md#a1cd79e2b5d5d58b16bc65869fb629e81) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timeout](structsched__poll.md#a1cd79e2b5d5d58b16bc65869fb629e81);

145};

[ 146](xen_2public_2sched_8h.md#aa4cc6a09419667548c61ee024a693b23)typedef struct [sched\_poll](structsched__poll.md) [sched\_poll\_t](xen_2public_2sched_8h.md#aa4cc6a09419667548c61ee024a693b23);

[ 147](xen_2public_2sched_8h.md#a5dbec2ec7d18d52cae3a5fb79749650d)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([sched\_poll\_t](xen_2public_2sched_8h.md#aa4cc6a09419667548c61ee024a693b23));

148

[ 149](structsched__remote__shutdown.md)struct [sched\_remote\_shutdown](structsched__remote__shutdown.md) {

[ 150](structsched__remote__shutdown.md#a1216d7ab944fb8da931f9d24172c5f40) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domain\_id](structsched__remote__shutdown.md#a1216d7ab944fb8da931f9d24172c5f40); /\* Remote domain ID \*/

[ 151](structsched__remote__shutdown.md#a817e05af361ac36befd1805b637555c2) unsigned int [reason](structsched__remote__shutdown.md#a817e05af361ac36befd1805b637555c2); /\* SHUTDOWN\_\* => enum sched\_shutdown\_reason \*/

152};

[ 153](xen_2public_2sched_8h.md#ad9999189885b0556a19dadaa47ae8729)typedef struct [sched\_remote\_shutdown](structsched__remote__shutdown.md) [sched\_remote\_shutdown\_t](xen_2public_2sched_8h.md#ad9999189885b0556a19dadaa47ae8729);

[ 154](xen_2public_2sched_8h.md#ac011ae6dd03db79f31eaf664ef337bd9)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([sched\_remote\_shutdown\_t](xen_2public_2sched_8h.md#ad9999189885b0556a19dadaa47ae8729));

155

[ 156](structsched__watchdog.md)struct [sched\_watchdog](structsched__watchdog.md) {

[ 157](structsched__watchdog.md#a1d0f1f6630712329d6bdf96b68205d7d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structsched__watchdog.md#a1d0f1f6630712329d6bdf96b68205d7d); /\* watchdog ID \*/

[ 158](structsched__watchdog.md#a4ee5e968e6b207cd5314170b0be26415) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structsched__watchdog.md#a4ee5e968e6b207cd5314170b0be26415); /\* timeout \*/

159};

[ 160](xen_2public_2sched_8h.md#a220e31e99c5aded3f4fa30417d949c0a)typedef struct [sched\_watchdog](structsched__watchdog.md) [sched\_watchdog\_t](xen_2public_2sched_8h.md#a220e31e99c5aded3f4fa30417d949c0a);

[ 161](xen_2public_2sched_8h.md#a071598f2732280a61e9ed949691f5745)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([sched\_watchdog\_t](xen_2public_2sched_8h.md#a220e31e99c5aded3f4fa30417d949c0a));

162

[ 163](structsched__pin__override.md)struct [sched\_pin\_override](structsched__pin__override.md) {

[ 164](structsched__pin__override.md#a44d5f4c5efab1c1bc88902347ec90732) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [pcpu](structsched__pin__override.md#a44d5f4c5efab1c1bc88902347ec90732);

165};

[ 166](xen_2public_2sched_8h.md#a008552edd0a746a38e426e70a3f8bc1b)typedef struct [sched\_pin\_override](structsched__pin__override.md) [sched\_pin\_override\_t](xen_2public_2sched_8h.md#a008552edd0a746a38e426e70a3f8bc1b);

[ 167](xen_2public_2sched_8h.md#a1b124f173597b5ae2ee426cd762234e9)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([sched\_pin\_override\_t](xen_2public_2sched_8h.md#a008552edd0a746a38e426e70a3f8bc1b));

168

169/\*

170 \* Reason codes for SCHEDOP\_shutdown. These may be interpreted by control

171 \* software to determine the appropriate action. For the most part, Xen does

172 \* not care about the shutdown code.

173 \*/

174/\* Domain exited normally. Clean up and kill. \*/

[ 175](xen_2public_2sched_8h.md#ab565461b915d7d8350fe4f21d8d7aceb)#define SHUTDOWN\_poweroff 0

176

177/\* Clean up, kill, and then restart. \*/

[ 178](xen_2public_2sched_8h.md#a38df89b49d7eddfcabb9a73289ab8b2a)#define SHUTDOWN\_reboot 1

179

180/\* Clean up, save suspend info, kill. \*/

[ 181](xen_2public_2sched_8h.md#a69edbb2f053d98cfc807a889b3fad958)#define SHUTDOWN\_suspend 2

182

183/\* Tell controller we've crashed. \*/

[ 184](xen_2public_2sched_8h.md#addd2d09c78bbf469ebcd023207533088)#define SHUTDOWN\_crash 3

185

186/\* Restart because watchdog time expired. \*/

[ 187](xen_2public_2sched_8h.md#a45cca8cb6eca9a48a63c12659edf02fd)#define SHUTDOWN\_watchdog 4

188

189/\*

190 \* Domain asked to perform 'soft reset' for it. The expected behavior is to

191 \* reset internal Xen state for the domain returning it to the point where it

192 \* was created but leaving the domain's memory contents and vCPU contexts

193 \* intact. This will allow the domain to start over and set up all Xen specific

194 \* interfaces again.

195 \*/

[ 196](xen_2public_2sched_8h.md#a82ce3d9d9b48872947534b83820a0a37)#define SHUTDOWN\_soft\_reset 5

197

198/\* Maximum valid shutdown reason. \*/

[ 199](xen_2public_2sched_8h.md#acc97d10d75325917d3bb3c47f26d99fe)#define SHUTDOWN\_MAX 5

200

201#endif /\* \_\_XEN\_PUBLIC\_SCHED\_H\_\_ \*/

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[event\_channel.h](event__channel_8h.md)

[evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)

uint32\_t evtchn\_port\_t

**Definition** event\_channel.h:74

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sched\_pin\_override](structsched__pin__override.md)

**Definition** sched.h:163

[sched\_pin\_override::pcpu](structsched__pin__override.md#a44d5f4c5efab1c1bc88902347ec90732)

int32\_t pcpu

**Definition** sched.h:164

[sched\_poll](structsched__poll.md)

**Definition** sched.h:141

[sched\_poll::timeout](structsched__poll.md#a1cd79e2b5d5d58b16bc65869fb629e81)

uint64\_t timeout

**Definition** sched.h:144

[sched\_poll::nr\_ports](structsched__poll.md#a2dd2e52e0db41c71033a2d64fe984f16)

unsigned int nr\_ports

**Definition** sched.h:143

[sched\_poll::XEN\_GUEST\_HANDLE](structsched__poll.md#ae3edf9e983927d88d84aea48015e7619)

XEN\_GUEST\_HANDLE(evtchn\_port\_t) ports

[sched\_remote\_shutdown](structsched__remote__shutdown.md)

**Definition** sched.h:149

[sched\_remote\_shutdown::domain\_id](structsched__remote__shutdown.md#a1216d7ab944fb8da931f9d24172c5f40)

domid\_t domain\_id

**Definition** sched.h:150

[sched\_remote\_shutdown::reason](structsched__remote__shutdown.md#a817e05af361ac36befd1805b637555c2)

unsigned int reason

**Definition** sched.h:151

[sched\_shutdown](structsched__shutdown.md)

**Definition** sched.h:135

[sched\_shutdown::reason](structsched__shutdown.md#ab68ec3e008c9d9eab5f48ad5f55346db)

unsigned int reason

**Definition** sched.h:136

[sched\_watchdog](structsched__watchdog.md)

**Definition** sched.h:156

[sched\_watchdog::id](structsched__watchdog.md#a1d0f1f6630712329d6bdf96b68205d7d)

uint32\_t id

**Definition** sched.h:157

[sched\_watchdog::timeout](structsched__watchdog.md#a4ee5e968e6b207cd5314170b0be26415)

uint32\_t timeout

**Definition** sched.h:158

[sched\_pin\_override\_t](xen_2public_2sched_8h.md#a008552edd0a746a38e426e70a3f8bc1b)

struct sched\_pin\_override sched\_pin\_override\_t

**Definition** sched.h:166

[sched\_watchdog\_t](xen_2public_2sched_8h.md#a220e31e99c5aded3f4fa30417d949c0a)

struct sched\_watchdog sched\_watchdog\_t

**Definition** sched.h:160

[sched\_poll\_t](xen_2public_2sched_8h.md#aa4cc6a09419667548c61ee024a693b23)

struct sched\_poll sched\_poll\_t

**Definition** sched.h:146

[sched\_shutdown\_t](xen_2public_2sched_8h.md#ab7dec9bb2853d145f6e8035e81aacea9)

struct sched\_shutdown sched\_shutdown\_t

**Definition** sched.h:138

[sched\_remote\_shutdown\_t](xen_2public_2sched_8h.md#ad9999189885b0556a19dadaa47ae8729)

struct sched\_remote\_shutdown sched\_remote\_shutdown\_t

**Definition** sched.h:153

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [sched.h](xen_2public_2sched_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
