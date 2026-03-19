---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/event__channel_8h_source.html
original_path: doxygen/html/event__channel_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

event\_channel.h

[Go to the documentation of this file.](event__channel_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* event\_channel.h

5 \*

6 \* Event channels between domains.

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

26 \* Copyright (c) 2003-2004, K A Fraser.

27 \*/

28

29#ifndef \_\_XEN\_PUBLIC\_EVENT\_CHANNEL\_H\_\_

30#define \_\_XEN\_PUBLIC\_EVENT\_CHANNEL\_H\_\_

31

32#include "[xen.h](xen_8h.md)"

33

34/\*

35 \* `incontents 150 evtchn Event Channels

36 \*

37 \* Event channels are the basic primitive provided by Xen for event

38 \* notifications. An event is the Xen equivalent of a hardware

39 \* interrupt. They essentially store one bit of information, the event

40 \* of interest is signalled by transitioning this bit from 0 to 1.

41 \*

42 \* Notifications are received by a guest via an upcall from Xen,

43 \* indicating when an event arrives (setting the bit). Further

44 \* notifications are masked until the bit is cleared again (therefore,

45 \* guests must check the value of the bit after re-enabling event

46 \* delivery to ensure no missed notifications).

47 \*

48 \* Event notifications can be masked by setting a flag; this is

49 \* equivalent to disabling interrupts and can be used to ensure

50 \* atomicity of certain operations in the guest kernel.

51 \*

52 \* Event channels are represented by the evtchn\_\* fields in

53 \* struct shared\_info and struct vcpu\_info.

54 \*/

55

[ 56](event__channel_8h.md#a3483f93d8b78e60ec7856e2a4ee57304)#define EVTCHNOP\_bind\_interdomain 0

[ 57](event__channel_8h.md#a795dc96341925d710075030e45f65750)#define EVTCHNOP\_bind\_virq 1

[ 58](event__channel_8h.md#a42a0680c05b55a0447e0f6bdb1805cf3)#define EVTCHNOP\_bind\_pirq 2

[ 59](event__channel_8h.md#a078653022bf42296dfe21769e4b9c1f0)#define EVTCHNOP\_close 3

[ 60](event__channel_8h.md#a59f6c29f7ef47d003f192d1c8fc9676a)#define EVTCHNOP\_send 4

[ 61](event__channel_8h.md#aa1ba0fec605174cae49dbe4d7d33ffcd)#define EVTCHNOP\_status 5

[ 62](event__channel_8h.md#a688357b79034d6c9cadc9fde62716e67)#define EVTCHNOP\_alloc\_unbound 6

[ 63](event__channel_8h.md#a547b2ee658a9ebaeb38e732da7241575)#define EVTCHNOP\_bind\_ipi 7

[ 64](event__channel_8h.md#a8677a6dccd99efb40a218e0affeee20f)#define EVTCHNOP\_bind\_vcpu 8

[ 65](event__channel_8h.md#a56d70d3fcc8ed685a3282aea1715df56)#define EVTCHNOP\_unmask 9

[ 66](event__channel_8h.md#aa055408833212f615860a0d839f9e749)#define EVTCHNOP\_reset 10

[ 67](event__channel_8h.md#ac27259ea173feb1bdf032f2e5f7d9b24)#define EVTCHNOP\_init\_control 11

[ 68](event__channel_8h.md#ae3638932df91767358c8b1258ee8a14a)#define EVTCHNOP\_expand\_array 12

[ 69](event__channel_8h.md#a2aff242f251d2ac6a3f1d65e10e5d4e0)#define EVTCHNOP\_set\_priority 13

70#ifdef \_\_XEN\_\_

71#define EVTCHNOP\_reset\_cont 14

72#endif

73

[ 74](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f);

[ 75](event__channel_8h.md#afc32a45a04eafa1b7f1ddae5231ac694)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f));

76

77/\*

78 \* EVTCHNOP\_alloc\_unbound: Allocate a port in domain <dom> and mark as

79 \* accepting interdomain bindings from domain <remote\_dom>. A fresh port

80 \* is allocated in <dom> and returned as <port>.

81 \* NOTES:

82 \* 1. If the caller is unprivileged then <dom> must be DOMID\_SELF.

83 \* 2. <remote\_dom> may be DOMID\_SELF, allowing loopback connections.

84 \*/

[ 85](structevtchn__alloc__unbound.md)struct [evtchn\_alloc\_unbound](structevtchn__alloc__unbound.md) {

86 /\* IN parameters \*/

[ 87](structevtchn__alloc__unbound.md#a4443f2b6f2cd24df9d75836f0b490729) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structevtchn__alloc__unbound.md#a4443f2b6f2cd24df9d75836f0b490729), [remote\_dom](structevtchn__alloc__unbound.md#a12e133eb2ba9bb2e1645c006a06f0da3);

88 /\* OUT parameters \*/

[ 89](structevtchn__alloc__unbound.md#a63d400c83f9a0b45c8172f3344b605c4) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__alloc__unbound.md#a63d400c83f9a0b45c8172f3344b605c4);

90};

[ 91](event__channel_8h.md#a2f53913488e4b1105b164c429ef21bac)typedef struct [evtchn\_alloc\_unbound](structevtchn__alloc__unbound.md) [evtchn\_alloc\_unbound\_t](event__channel_8h.md#a2f53913488e4b1105b164c429ef21bac);

92

93/\*

94 \* EVTCHNOP\_bind\_interdomain: Construct an interdomain event channel between

95 \* the calling domain and <remote\_dom>. <remote\_dom,remote\_port> must identify

96 \* a port that is unbound and marked as accepting bindings from the calling

97 \* domain. A fresh port is allocated in the calling domain and returned as

98 \* <local\_port>.

99 \*

100 \* In case the peer domain has already tried to set our event channel

101 \* pending, before it was bound, EVTCHNOP\_bind\_interdomain always sets

102 \* the local event channel pending.

103 \*

104 \* The usual pattern of use, in the guest's upcall (or subsequent

105 \* handler) is as follows: (Re-enable the event channel for subsequent

106 \* signalling and then) check for the existence of whatever condition

107 \* is being waited for by other means, and take whatever action is

108 \* needed (if any).

109 \*

110 \* NOTES:

111 \* 1. <remote\_dom> may be DOMID\_SELF, allowing loopback connections.

112 \*/

[ 113](structevtchn__bind__interdomain.md)struct [evtchn\_bind\_interdomain](structevtchn__bind__interdomain.md) {

114 /\* IN parameters. \*/

[ 115](structevtchn__bind__interdomain.md#a3e46d3aad6d7ce75d49476a62441badf) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [remote\_dom](structevtchn__bind__interdomain.md#a3e46d3aad6d7ce75d49476a62441badf);

[ 116](structevtchn__bind__interdomain.md#a12b3d5fc5a43580f65cc80d82d244483) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [remote\_port](structevtchn__bind__interdomain.md#a12b3d5fc5a43580f65cc80d82d244483);

117 /\* OUT parameters. \*/

[ 118](structevtchn__bind__interdomain.md#a9c29d1cff91fb52e5476c680a8760f7b) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [local\_port](structevtchn__bind__interdomain.md#a9c29d1cff91fb52e5476c680a8760f7b);

119};

[ 120](event__channel_8h.md#ac758af7badcae4377a5df682ff4ea248)typedef struct [evtchn\_bind\_interdomain](structevtchn__bind__interdomain.md) [evtchn\_bind\_interdomain\_t](event__channel_8h.md#ac758af7badcae4377a5df682ff4ea248);

121

122/\*

123 \* EVTCHNOP\_close: Close a local event channel <port>. If the channel is

124 \* interdomain then the remote end is placed in the unbound state

125 \* (EVTCHNSTAT\_unbound), awaiting a new connection.

126 \*/

[ 127](structevtchn__close.md)struct [evtchn\_close](structevtchn__close.md) {

128 /\* IN parameters. \*/

[ 129](structevtchn__close.md#aa1a8e61fbf9d5b264a8f86fb2a951ec9) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__close.md#aa1a8e61fbf9d5b264a8f86fb2a951ec9);

130};

[ 131](event__channel_8h.md#ad19c601c41adcd9e235695073e11fa31)typedef struct [evtchn\_close](structevtchn__close.md) [evtchn\_close\_t](event__channel_8h.md#ad19c601c41adcd9e235695073e11fa31);

132

133/\*

134 \* EVTCHNOP\_send: Send an event to the remote end of the channel whose local

135 \* endpoint is <port>.

136 \*/

[ 137](structevtchn__send.md)struct [evtchn\_send](structevtchn__send.md) {

138 /\* IN parameters. \*/

[ 139](structevtchn__send.md#a436ed583ccfb8b658530cd046e2df53d) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__send.md#a436ed583ccfb8b658530cd046e2df53d);

140};

[ 141](event__channel_8h.md#a7c4630750087f7f7586488f49cd55d4e)typedef struct [evtchn\_send](structevtchn__send.md) [evtchn\_send\_t](event__channel_8h.md#a7c4630750087f7f7586488f49cd55d4e);

142

143/\*

144 \* EVTCHNOP\_status: Get the current status of the communication channel which

145 \* has an endpoint at <dom, port>.

146 \* NOTES:

147 \* 1. <dom> may be specified as DOMID\_SELF.

148 \* 2. Only a sufficiently-privileged domain may obtain the status of an event

149 \* channel for which <dom> is not DOMID\_SELF.

150 \*/

[ 151](structevtchn__status.md)struct [evtchn\_status](structevtchn__status.md) {

152 /\* IN parameters \*/

[ 153](structevtchn__status.md#ab2af6d86b1121d78bcd44a7deab22429) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structevtchn__status.md#ab2af6d86b1121d78bcd44a7deab22429);

[ 154](structevtchn__status.md#a371c715eff52f12ecc45b8c0396724a2) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__status.md#a371c715eff52f12ecc45b8c0396724a2);

155 /\* OUT parameters \*/

[ 156](event__channel_8h.md#a783b78a1ff275d6b2dfa9592bcfebdbc)#define EVTCHNSTAT\_closed 0 /\* Channel is not in use. \*/

[ 157](event__channel_8h.md#aaf73995f43bc61feecd6ab6d77255b7c)#define EVTCHNSTAT\_unbound 1 /\* Channel is waiting interdom connection.\*/

[ 158](event__channel_8h.md#a556deda7942e60afce2f039f93899c5f)#define EVTCHNSTAT\_interdomain 2 /\* Channel is connected to remote domain. \*/

[ 159](event__channel_8h.md#aec1a18deba5a52f84abac495cb2ef698)#define EVTCHNSTAT\_pirq 3 /\* Channel is bound to a phys IRQ line. \*/

[ 160](event__channel_8h.md#ac2db0aaa42a834598a9efaf22e59c7e3)#define EVTCHNSTAT\_virq 4 /\* Channel is bound to a virtual IRQ line \*/

[ 161](event__channel_8h.md#a7214c690ed8bbfd4d68f4c1b44d9ce92)#define EVTCHNSTAT\_ipi 5 /\* Channel is bound to a virtual IPI line \*/

[ 162](structevtchn__status.md#a366e123cce2040e4a9c098b893647077) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [status](structevtchn__status.md#a366e123cce2040e4a9c098b893647077);

[ 163](structevtchn__status.md#a73b3355dc9a49f0f463944c963d9c99a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vcpu](structevtchn__status.md#a73b3355dc9a49f0f463944c963d9c99a); /\* VCPU to which this channel is bound. \*/

164 union {

165 struct {

166 [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structevtchn__status.md#ab2af6d86b1121d78bcd44a7deab22429);

[ 167](structevtchn__status.md#a450e072e1a3e19b118c77f28296b16af) } [unbound](structevtchn__status.md#a450e072e1a3e19b118c77f28296b16af); /\* EVTCHNSTAT\_unbound \*/

168 struct {

169 [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structevtchn__status.md#ab2af6d86b1121d78bcd44a7deab22429);

170 [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__status.md#a371c715eff52f12ecc45b8c0396724a2);

[ 171](structevtchn__status.md#afa5fef85870db40407579ae3d4a0a021) } [interdomain](structevtchn__status.md#afa5fef85870db40407579ae3d4a0a021); /\* EVTCHNSTAT\_interdomain \*/

[ 172](structevtchn__status.md#abbb84f973ee49ddab13783de648cb382) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pirq](structevtchn__status.md#abbb84f973ee49ddab13783de648cb382); /\* EVTCHNSTAT\_pirq \*/

[ 173](structevtchn__status.md#acd976827543c4192186f68da8f8be701) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [virq](structevtchn__status.md#acd976827543c4192186f68da8f8be701); /\* EVTCHNSTAT\_virq \*/

[ 174](structevtchn__status.md#a332ac0bb8666e0e1d8a0ae015cdcacc6) } [u](structevtchn__status.md#a332ac0bb8666e0e1d8a0ae015cdcacc6);

175};

[ 176](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9)typedef struct [evtchn\_status](structevtchn__status.md) [evtchn\_status\_t](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9);

177

178/\*

179 \* EVTCHNOP\_unmask: Unmask the specified local event-channel port and deliver

180 \* a notification to the appropriate VCPU if an event is pending.

181 \*/

[ 182](structevtchn__unmask.md)struct [evtchn\_unmask](structevtchn__unmask.md) {

183 /\* IN parameters. \*/

[ 184](structevtchn__unmask.md#a34554ebad6dea7adb6fcd45111828044) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__unmask.md#a34554ebad6dea7adb6fcd45111828044);

185};

[ 186](event__channel_8h.md#adf108a8c569745708da92551dcad289c)typedef struct [evtchn\_unmask](structevtchn__unmask.md) [evtchn\_unmask\_t](event__channel_8h.md#adf108a8c569745708da92551dcad289c);

187

188/\*

189 \* EVTCHNOP\_reset: Close all event channels associated with specified domain.

190 \* NOTES:

191 \* 1. <dom> may be specified as DOMID\_SELF.

192 \* 2. Only a sufficiently-privileged domain may specify other than DOMID\_SELF.

193 \* 3. Destroys all control blocks and event array, resets event channel

194 \* operations to 2-level ABI if called with <dom> == DOMID\_SELF and FIFO

195 \* ABI was used. Guests should not bind events during EVTCHNOP\_reset call

196 \* as these events are likely to be lost.

197 \*/

[ 198](structevtchn__reset.md)struct [evtchn\_reset](structevtchn__reset.md) {

199 /\* IN parameters. \*/

[ 200](structevtchn__reset.md#af47f294c4bbe90f813c5cae2d40fe676) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structevtchn__reset.md#af47f294c4bbe90f813c5cae2d40fe676);

201};

[ 202](event__channel_8h.md#a6338f2371d708c16d85dcabfe88ebffb)typedef struct [evtchn\_reset](structevtchn__reset.md) [evtchn\_reset\_t](event__channel_8h.md#a6338f2371d708c16d85dcabfe88ebffb);

203

204/\*

205 \* EVTCHNOP\_set\_priority: set the priority for an event channel.

206 \*/

[ 207](structevtchn__set__priority.md)struct [evtchn\_set\_priority](structevtchn__set__priority.md) {

208 /\* IN parameters. \*/

[ 209](structevtchn__set__priority.md#a1a4b69f6cfa0d49ed2de7a0671600d85) [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) [port](structevtchn__set__priority.md#a1a4b69f6cfa0d49ed2de7a0671600d85);

[ 210](structevtchn__set__priority.md#a02cc9246ec3927932e56615ae0e628dc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [priority](structevtchn__set__priority.md#a02cc9246ec3927932e56615ae0e628dc);

211};

[ 212](event__channel_8h.md#a497a6a153a0f6152a9c33686d4601a3b)typedef struct [evtchn\_set\_priority](structevtchn__set__priority.md) [evtchn\_set\_priority\_t](event__channel_8h.md#a497a6a153a0f6152a9c33686d4601a3b);

213

[ 214](event__channel_8h.md#acdcf92372fa5ac60b219cd5e34d82fdf)#define EVTCHN\_2L\_NR\_CHANNELS (sizeof(xen\_ulong\_t) \* sizeof(xen\_ulong\_t) \* 64)

215

216#endif /\* \_\_XEN\_PUBLIC\_EVENT\_CHANNEL\_H\_\_ \*/

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[evtchn\_alloc\_unbound\_t](event__channel_8h.md#a2f53913488e4b1105b164c429ef21bac)

struct evtchn\_alloc\_unbound evtchn\_alloc\_unbound\_t

**Definition** event\_channel.h:91

[evtchn\_set\_priority\_t](event__channel_8h.md#a497a6a153a0f6152a9c33686d4601a3b)

struct evtchn\_set\_priority evtchn\_set\_priority\_t

**Definition** event\_channel.h:212

[evtchn\_reset\_t](event__channel_8h.md#a6338f2371d708c16d85dcabfe88ebffb)

struct evtchn\_reset evtchn\_reset\_t

**Definition** event\_channel.h:202

[evtchn\_send\_t](event__channel_8h.md#a7c4630750087f7f7586488f49cd55d4e)

struct evtchn\_send evtchn\_send\_t

**Definition** event\_channel.h:141

[evtchn\_status\_t](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9)

struct evtchn\_status evtchn\_status\_t

**Definition** event\_channel.h:176

[evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)

uint32\_t evtchn\_port\_t

**Definition** event\_channel.h:74

[evtchn\_bind\_interdomain\_t](event__channel_8h.md#ac758af7badcae4377a5df682ff4ea248)

struct evtchn\_bind\_interdomain evtchn\_bind\_interdomain\_t

**Definition** event\_channel.h:120

[evtchn\_close\_t](event__channel_8h.md#ad19c601c41adcd9e235695073e11fa31)

struct evtchn\_close evtchn\_close\_t

**Definition** event\_channel.h:131

[evtchn\_unmask\_t](event__channel_8h.md#adf108a8c569745708da92551dcad289c)

struct evtchn\_unmask evtchn\_unmask\_t

**Definition** event\_channel.h:186

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[evtchn\_alloc\_unbound](structevtchn__alloc__unbound.md)

**Definition** event\_channel.h:85

[evtchn\_alloc\_unbound::remote\_dom](structevtchn__alloc__unbound.md#a12e133eb2ba9bb2e1645c006a06f0da3)

domid\_t remote\_dom

**Definition** event\_channel.h:87

[evtchn\_alloc\_unbound::dom](structevtchn__alloc__unbound.md#a4443f2b6f2cd24df9d75836f0b490729)

domid\_t dom

**Definition** event\_channel.h:87

[evtchn\_alloc\_unbound::port](structevtchn__alloc__unbound.md#a63d400c83f9a0b45c8172f3344b605c4)

evtchn\_port\_t port

**Definition** event\_channel.h:89

[evtchn\_bind\_interdomain](structevtchn__bind__interdomain.md)

**Definition** event\_channel.h:113

[evtchn\_bind\_interdomain::remote\_port](structevtchn__bind__interdomain.md#a12b3d5fc5a43580f65cc80d82d244483)

evtchn\_port\_t remote\_port

**Definition** event\_channel.h:116

[evtchn\_bind\_interdomain::remote\_dom](structevtchn__bind__interdomain.md#a3e46d3aad6d7ce75d49476a62441badf)

domid\_t remote\_dom

**Definition** event\_channel.h:115

[evtchn\_bind\_interdomain::local\_port](structevtchn__bind__interdomain.md#a9c29d1cff91fb52e5476c680a8760f7b)

evtchn\_port\_t local\_port

**Definition** event\_channel.h:118

[evtchn\_close](structevtchn__close.md)

**Definition** event\_channel.h:127

[evtchn\_close::port](structevtchn__close.md#aa1a8e61fbf9d5b264a8f86fb2a951ec9)

evtchn\_port\_t port

**Definition** event\_channel.h:129

[evtchn\_reset](structevtchn__reset.md)

**Definition** event\_channel.h:198

[evtchn\_reset::dom](structevtchn__reset.md#af47f294c4bbe90f813c5cae2d40fe676)

domid\_t dom

**Definition** event\_channel.h:200

[evtchn\_send](structevtchn__send.md)

**Definition** event\_channel.h:137

[evtchn\_send::port](structevtchn__send.md#a436ed583ccfb8b658530cd046e2df53d)

evtchn\_port\_t port

**Definition** event\_channel.h:139

[evtchn\_set\_priority](structevtchn__set__priority.md)

**Definition** event\_channel.h:207

[evtchn\_set\_priority::priority](structevtchn__set__priority.md#a02cc9246ec3927932e56615ae0e628dc)

uint32\_t priority

**Definition** event\_channel.h:210

[evtchn\_set\_priority::port](structevtchn__set__priority.md#a1a4b69f6cfa0d49ed2de7a0671600d85)

evtchn\_port\_t port

**Definition** event\_channel.h:209

[evtchn\_status](structevtchn__status.md)

**Definition** event\_channel.h:151

[evtchn\_status::u](structevtchn__status.md#a332ac0bb8666e0e1d8a0ae015cdcacc6)

union evtchn\_status::@044031350060371265027151217225227242327377267331 u

[evtchn\_status::status](structevtchn__status.md#a366e123cce2040e4a9c098b893647077)

uint32\_t status

**Definition** event\_channel.h:162

[evtchn\_status::port](structevtchn__status.md#a371c715eff52f12ecc45b8c0396724a2)

evtchn\_port\_t port

**Definition** event\_channel.h:154

[evtchn\_status::unbound](structevtchn__status.md#a450e072e1a3e19b118c77f28296b16af)

struct evtchn\_status::@044031350060371265027151217225227242327377267331::@032037363364372134362310031162135030055037005107 unbound

[evtchn\_status::vcpu](structevtchn__status.md#a73b3355dc9a49f0f463944c963d9c99a)

uint32\_t vcpu

**Definition** event\_channel.h:163

[evtchn\_status::dom](structevtchn__status.md#ab2af6d86b1121d78bcd44a7deab22429)

domid\_t dom

**Definition** event\_channel.h:153

[evtchn\_status::pirq](structevtchn__status.md#abbb84f973ee49ddab13783de648cb382)

uint32\_t pirq

**Definition** event\_channel.h:172

[evtchn\_status::virq](structevtchn__status.md#acd976827543c4192186f68da8f8be701)

uint32\_t virq

**Definition** event\_channel.h:173

[evtchn\_status::interdomain](structevtchn__status.md#afa5fef85870db40407579ae3d4a0a021)

struct evtchn\_status::@044031350060371265027151217225227242327377267331::@204023274163375331230337243223221022201032305106 interdomain

[evtchn\_unmask](structevtchn__unmask.md)

**Definition** event\_channel.h:182

[evtchn\_unmask::port](structevtchn__unmask.md#a34554ebad6dea7adb6fcd45111828044)

evtchn\_port\_t port

**Definition** event\_channel.h:184

[xen.h](xen_8h.md)

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [event\_channel.h](event__channel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
