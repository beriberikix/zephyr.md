---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/onoff_8h_source.html
original_path: doxygen/html/onoff_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff.h

[Go to the documentation of this file.](onoff_8h.md)

1/\*

2 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

3 \* Copyright (c) 2020 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_SYS\_ONOFF\_H\_

9#define ZEPHYR\_INCLUDE\_SYS\_ONOFF\_H\_

10

11#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13#include <[zephyr/sys/notify.h](notify_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 30](group__resource__mgmt__onoff__apis.md#ga9ae0c3528254b10f5e1a9743aea234dd)#define ONOFF\_FLAG\_ERROR BIT(0)

31

33#define ONOFF\_FLAG\_ONOFF BIT(1)

34#define ONOFF\_FLAG\_TRANSITION BIT(2)

36

[ 45](group__resource__mgmt__onoff__apis.md#ga0e06eafdf5021ce970027f20fc001acc)#define ONOFF\_STATE\_MASK (ONOFF\_FLAG\_ERROR \

46 | ONOFF\_FLAG\_ONOFF \

47 | ONOFF\_FLAG\_TRANSITION)

48

[ 52](group__resource__mgmt__onoff__apis.md#gab9e5380dce026a5dfea770f999400484)#define ONOFF\_STATE\_OFF 0U

53

[ 57](group__resource__mgmt__onoff__apis.md#ga7cd0fba52afba2e337ab7c830d3058d7)#define ONOFF\_STATE\_ON ONOFF\_FLAG\_ONOFF

58

[ 63](group__resource__mgmt__onoff__apis.md#gac005a25d149568208a6fbaa2ceaa1ac6)#define ONOFF\_STATE\_ERROR ONOFF\_FLAG\_ERROR

64

[ 69](group__resource__mgmt__onoff__apis.md#gac4a0d8a7b501adb011aa1c4c4da3f2a3)#define ONOFF\_STATE\_TO\_ON (ONOFF\_FLAG\_TRANSITION | ONOFF\_STATE\_ON)

70

[ 75](group__resource__mgmt__onoff__apis.md#ga235a04122763f1a2cbb849c56df65d26)#define ONOFF\_STATE\_TO\_OFF (ONOFF\_FLAG\_TRANSITION | ONOFF\_STATE\_OFF)

76

[ 81](group__resource__mgmt__onoff__apis.md#gacc0438b5c81c639e0035ada5caec940b)#define ONOFF\_STATE\_RESETTING (ONOFF\_FLAG\_TRANSITION | ONOFF\_STATE\_ERROR)

82

83/\* Forward declarations \*/

84struct [onoff\_manager](structonoff__manager.md);

85struct [onoff\_monitor](structonoff__monitor.md);

86

[ 101](group__resource__mgmt__onoff__apis.md#gac05f7946a14fa23ef67212eba30c98ac)typedef void (\*[onoff\_notify\_fn](group__resource__mgmt__onoff__apis.md#gac05f7946a14fa23ef67212eba30c98ac))(struct [onoff\_manager](structonoff__manager.md) \*mgr,

102 int res);

103

[ 129](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1)typedef void (\*[onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1))(struct [onoff\_manager](structonoff__manager.md) \*mgr,

130 [onoff\_notify\_fn](group__resource__mgmt__onoff__apis.md#gac05f7946a14fa23ef67212eba30c98ac) notify);

131

[ 133](structonoff__transitions.md)struct [onoff\_transitions](structonoff__transitions.md) {

[ 135](structonoff__transitions.md#a86417dd542c8f259ad1fc1c7d3c26545) [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) [start](structonoff__transitions.md#a86417dd542c8f259ad1fc1c7d3c26545);

136

[ 138](structonoff__transitions.md#a91a1805daabae70d362441634bfa508d) [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) [stop](structonoff__transitions.md#a91a1805daabae70d362441634bfa508d);

139

[ 143](structonoff__transitions.md#a335d7d2f8418e78b237cfb4199b6f6aa) [onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1) [reset](structonoff__transitions.md#a335d7d2f8418e78b237cfb4199b6f6aa);

144};

145

[ 154](structonoff__manager.md)struct [onoff\_manager](structonoff__manager.md) {

[ 158](structonoff__manager.md#a3eb50568d4b7c83597a194c7facd383b) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [clients](structonoff__manager.md#a3eb50568d4b7c83597a194c7facd383b);

159

[ 163](structonoff__manager.md#a501bb2c1c84293b1e4fbd011c62f5c69) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [monitors](structonoff__manager.md#a501bb2c1c84293b1e4fbd011c62f5c69);

164

[ 166](structonoff__manager.md#adcbe3b90e1618d3e7e223da106790457) const struct [onoff\_transitions](structonoff__transitions.md) \*[transitions](structonoff__manager.md#adcbe3b90e1618d3e7e223da106790457);

167

[ 169](structonoff__manager.md#af87f180f0494f02054e33086ee940493) struct [k\_spinlock](structk__spinlock.md) [lock](structonoff__manager.md#af87f180f0494f02054e33086ee940493);

170

[ 172](structonoff__manager.md#a5f555de973d72ba1889655c3342c8dc7) int [last\_res](structonoff__manager.md#a5f555de973d72ba1889655c3342c8dc7);

173

[ 175](structonoff__manager.md#a50d51cd3700e610b2f650607373afeb4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structonoff__manager.md#a50d51cd3700e610b2f650607373afeb4);

176

[ 178](structonoff__manager.md#a43c40829b6acd4c91517a34ebd371dd9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [refs](structonoff__manager.md#a43c40829b6acd4c91517a34ebd371dd9);

179};

180

[ 190](group__resource__mgmt__onoff__apis.md#ga8c1171a844ef1d9d6541d342124492ff)#define ONOFF\_TRANSITIONS\_INITIALIZER(\_start, \_stop, \_reset) { \

191 .start = \_start, \

192 .stop = \_stop, \

193 .reset = \_reset, \

194}

195

197#define ONOFF\_MANAGER\_INITIALIZER(\_transitions) { \

198 .transitions = \_transitions, \

199}

201

[ 221](group__resource__mgmt__onoff__apis.md#ga73d52272baab03d1df2f267429390978)int [onoff\_manager\_init](group__resource__mgmt__onoff__apis.md#ga73d52272baab03d1df2f267429390978)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

222 const struct [onoff\_transitions](structonoff__transitions.md) \*transitions);

223

224/\* Forward declaration \*/

225struct [onoff\_client](structonoff__client.md);

226

[ 252](group__resource__mgmt__onoff__apis.md#ga41b94526182c5772d7adebb1d1745068)typedef void (\*[onoff\_client\_callback](group__resource__mgmt__onoff__apis.md#ga41b94526182c5772d7adebb1d1745068))(struct [onoff\_manager](structonoff__manager.md) \*mgr,

253 struct [onoff\_client](structonoff__client.md) \*cli,

254 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

255 int res);

256

[ 274](structonoff__client.md)struct [onoff\_client](structonoff__client.md) {

281 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

283

[ 285](structonoff__client.md#a40f8029732122f7887bb021de362742c) struct [sys\_notify](structsys__notify.md) [notify](structonoff__client.md#a40f8029732122f7887bb021de362742c);

286};

287

[ 300](group__resource__mgmt__onoff__apis.md#gad61d053ae4e9ee12efe8d37372a16c63)#define ONOFF\_CLIENT\_EXTENSION\_POS SYS\_NOTIFY\_EXTENSION\_POS

301

[ 315](group__resource__mgmt__onoff__apis.md#ga347efda0aa0305c134224c59677fa6cb)static inline bool [onoff\_has\_error](group__resource__mgmt__onoff__apis.md#ga347efda0aa0305c134224c59677fa6cb)(const struct [onoff\_manager](structonoff__manager.md) \*mgr)

316{

317 return (mgr->[flags](structonoff__manager.md#a50d51cd3700e610b2f650607373afeb4) & [ONOFF\_FLAG\_ERROR](group__resource__mgmt__onoff__apis.md#ga9ae0c3528254b10f5e1a9743aea234dd)) != 0;

318}

319

[ 347](group__resource__mgmt__onoff__apis.md#ga20dcb358e405deb87b7fbb7846ef9d68)int [onoff\_request](group__resource__mgmt__onoff__apis.md#ga20dcb358e405deb87b7fbb7846ef9d68)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

348 struct [onoff\_client](structonoff__client.md) \*cli);

349

[ 368](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6)int [onoff\_release](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6)(struct [onoff\_manager](structonoff__manager.md) \*mgr);

369

[ 401](group__resource__mgmt__onoff__apis.md#gad05d32f1548e56b508628e84ba101554)int [onoff\_cancel](group__resource__mgmt__onoff__apis.md#gad05d32f1548e56b508628e84ba101554)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

402 struct [onoff\_client](structonoff__client.md) \*cli);

403

[ 435](group__resource__mgmt__onoff__apis.md#ga7aac2aeb66907ec920557f0ef67d6795)static inline int [onoff\_cancel\_or\_release](group__resource__mgmt__onoff__apis.md#ga7aac2aeb66907ec920557f0ef67d6795)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

436 struct [onoff\_client](structonoff__client.md) \*cli)

437{

438 int rv = [onoff\_cancel](group__resource__mgmt__onoff__apis.md#gad05d32f1548e56b508628e84ba101554)(mgr, cli);

439

440 if (rv == -[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4)) {

441 rv = [onoff\_release](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6)(mgr);

442 }

443 return rv;

444}

445

[ 481](group__resource__mgmt__onoff__apis.md#gaf7b46a5f2e43d1bab193c18b8f6c8ba8)int [onoff\_reset](group__resource__mgmt__onoff__apis.md#gaf7b46a5f2e43d1bab193c18b8f6c8ba8)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

482 struct [onoff\_client](structonoff__client.md) \*cli);

483

[ 512](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545)typedef void (\*[onoff\_monitor\_callback](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545))(struct [onoff\_manager](structonoff__manager.md) \*mgr,

513 struct [onoff\_monitor](structonoff__monitor.md) \*mon,

514 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

515 int res);

516

[ 524](structonoff__monitor.md)struct [onoff\_monitor](structonoff__monitor.md) {

[ 529](structonoff__monitor.md#a732a81eb0d9b36376b39b1a340fd1fe6) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structonoff__monitor.md#a732a81eb0d9b36376b39b1a340fd1fe6);

530

[ 535](structonoff__monitor.md#ab26d8ae8a0dac5e03549e2d9aca243a4) [onoff\_monitor\_callback](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545) [callback](structonoff__monitor.md#ab26d8ae8a0dac5e03549e2d9aca243a4);

536};

537

[ 549](group__resource__mgmt__onoff__apis.md#ga9897d93359fe58359c0204da46b4c01e)int [onoff\_monitor\_register](group__resource__mgmt__onoff__apis.md#ga9897d93359fe58359c0204da46b4c01e)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

550 struct [onoff\_monitor](structonoff__monitor.md) \*mon);

551

[ 563](group__resource__mgmt__onoff__apis.md#ga50a51da8e701a3f19f242af5183d807a)int [onoff\_monitor\_unregister](group__resource__mgmt__onoff__apis.md#ga50a51da8e701a3f19f242af5183d807a)(struct [onoff\_manager](structonoff__manager.md) \*mgr,

564 struct [onoff\_monitor](structonoff__monitor.md) \*mon);

565

[ 576](structonoff__sync__service.md)struct [onoff\_sync\_service](structonoff__sync__service.md) {

[ 578](structonoff__sync__service.md#ac08d780a80fed2d89c1334cc3c65eeed) struct [k\_spinlock](structk__spinlock.md) [lock](structonoff__sync__service.md#ac08d780a80fed2d89c1334cc3c65eeed);

579

[ 581](structonoff__sync__service.md#adff029426035dffb57fda0de44f2abae) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [count](structonoff__sync__service.md#adff029426035dffb57fda0de44f2abae);

582};

583

[ 600](group__resource__mgmt__onoff__apis.md#ga174cadf7dfa5d3c4dc5c8185994f3825)int [onoff\_sync\_lock](group__resource__mgmt__onoff__apis.md#ga174cadf7dfa5d3c4dc5c8185994f3825)(struct [onoff\_sync\_service](structonoff__sync__service.md) \*srv,

601 [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) \*keyp);

602

[ 635](group__resource__mgmt__onoff__apis.md#gae3331bdad9d03309ee78e86c487b7f26)int [onoff\_sync\_finalize](group__resource__mgmt__onoff__apis.md#gae3331bdad9d03309ee78e86c487b7f26)(struct [onoff\_sync\_service](structonoff__sync__service.md) \*srv,

636 [k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0) key,

637 struct [onoff\_client](structonoff__client.md) \*cli,

638 int res,

639 bool on);

640

642

643#ifdef \_\_cplusplus

644}

645#endif

646

647#endif /\* ZEPHYR\_INCLUDE\_SYS\_ONOFF\_H\_ \*/

[onoff\_sync\_lock](group__resource__mgmt__onoff__apis.md#ga174cadf7dfa5d3c4dc5c8185994f3825)

int onoff\_sync\_lock(struct onoff\_sync\_service \*srv, k\_spinlock\_key\_t \*keyp)

Lock a synchronous onoff service and provide its state.

[onoff\_release](group__resource__mgmt__onoff__apis.md#ga19da5359f10fa2e2eb034d1e72235ea6)

int onoff\_release(struct onoff\_manager \*mgr)

Release a reserved use of an on-off service.

[onoff\_request](group__resource__mgmt__onoff__apis.md#ga20dcb358e405deb87b7fbb7846ef9d68)

int onoff\_request(struct onoff\_manager \*mgr, struct onoff\_client \*cli)

Request a reservation to use an on-off service.

[onoff\_has\_error](group__resource__mgmt__onoff__apis.md#ga347efda0aa0305c134224c59677fa6cb)

static bool onoff\_has\_error(const struct onoff\_manager \*mgr)

Test whether an on-off service has recorded an error.

**Definition** onoff.h:315

[onoff\_client\_callback](group__resource__mgmt__onoff__apis.md#ga41b94526182c5772d7adebb1d1745068)

void(\* onoff\_client\_callback)(struct onoff\_manager \*mgr, struct onoff\_client \*cli, uint32\_t state, int res)

Signature used to notify an on-off service client of the completion of an operation.

**Definition** onoff.h:252

[onoff\_monitor\_unregister](group__resource__mgmt__onoff__apis.md#ga50a51da8e701a3f19f242af5183d807a)

int onoff\_monitor\_unregister(struct onoff\_manager \*mgr, struct onoff\_monitor \*mon)

Remove a monitor of state changes from a manager.

[onoff\_transition\_fn](group__resource__mgmt__onoff__apis.md#ga51fdf83642c5fa16112ce143382ec5d1)

void(\* onoff\_transition\_fn)(struct onoff\_manager \*mgr, onoff\_notify\_fn notify)

Signature used by service implementations to effect a transition.

**Definition** onoff.h:129

[onoff\_manager\_init](group__resource__mgmt__onoff__apis.md#ga73d52272baab03d1df2f267429390978)

int onoff\_manager\_init(struct onoff\_manager \*mgr, const struct onoff\_transitions \*transitions)

Initialize an on-off service to off state.

[onoff\_cancel\_or\_release](group__resource__mgmt__onoff__apis.md#ga7aac2aeb66907ec920557f0ef67d6795)

static int onoff\_cancel\_or\_release(struct onoff\_manager \*mgr, struct onoff\_client \*cli)

Helper function to safely cancel a request.

**Definition** onoff.h:435

[onoff\_monitor\_register](group__resource__mgmt__onoff__apis.md#ga9897d93359fe58359c0204da46b4c01e)

int onoff\_monitor\_register(struct onoff\_manager \*mgr, struct onoff\_monitor \*mon)

Add a monitor of state changes for a manager.

[ONOFF\_FLAG\_ERROR](group__resource__mgmt__onoff__apis.md#ga9ae0c3528254b10f5e1a9743aea234dd)

#define ONOFF\_FLAG\_ERROR

Flag indicating an error state.

**Definition** onoff.h:30

[onoff\_notify\_fn](group__resource__mgmt__onoff__apis.md#gac05f7946a14fa23ef67212eba30c98ac)

void(\* onoff\_notify\_fn)(struct onoff\_manager \*mgr, int res)

Signature used to notify an on-off manager that a transition has completed.

**Definition** onoff.h:101

[onoff\_cancel](group__resource__mgmt__onoff__apis.md#gad05d32f1548e56b508628e84ba101554)

int onoff\_cancel(struct onoff\_manager \*mgr, struct onoff\_client \*cli)

Attempt to cancel an in-progress client operation.

[onoff\_sync\_finalize](group__resource__mgmt__onoff__apis.md#gae3331bdad9d03309ee78e86c487b7f26)

int onoff\_sync\_finalize(struct onoff\_sync\_service \*srv, k\_spinlock\_key\_t key, struct onoff\_client \*cli, int res, bool on)

Process the completion of a transition in a synchronous service and release lock.

[onoff\_monitor\_callback](group__resource__mgmt__onoff__apis.md#gaee41b38d408cf5f5efc9cd007f377545)

void(\* onoff\_monitor\_callback)(struct onoff\_manager \*mgr, struct onoff\_monitor \*mon, uint32\_t state, int res)

Signature used to notify a monitor of an onoff service of errors or completion of a state transition.

**Definition** onoff.h:512

[onoff\_reset](group__resource__mgmt__onoff__apis.md#gaf7b46a5f2e43d1bab193c18b8f6c8ba8)

int onoff\_reset(struct onoff\_manager \*mgr, struct onoff\_client \*cli)

Clear errors on an on-off service and reset it to its off state.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[k\_spinlock\_key\_t](group__spinlock__apis.md#gacacd3d3bbd31416dbbf6a0239be82ef0)

struct z\_spinlock\_key k\_spinlock\_key\_t

Spinlock key type.

**Definition** spinlock.h:130

[EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4)

#define EALREADY

Operation already in progress.

**Definition** errno.h:105

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[notify.h](notify_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[onoff\_client](structonoff__client.md)

State associated with a client of an on-off service.

**Definition** onoff.h:274

[onoff\_client::notify](structonoff__client.md#a40f8029732122f7887bb021de362742c)

struct sys\_notify notify

Notification configuration.

**Definition** onoff.h:285

[onoff\_manager](structonoff__manager.md)

State associated with an on-off manager.

**Definition** onoff.h:154

[onoff\_manager::clients](structonoff__manager.md#a3eb50568d4b7c83597a194c7facd383b)

sys\_slist\_t clients

List of clients waiting for request or reset completion notifications.

**Definition** onoff.h:158

[onoff\_manager::refs](structonoff__manager.md#a43c40829b6acd4c91517a34ebd371dd9)

uint16\_t refs

Number of active clients for the service.

**Definition** onoff.h:178

[onoff\_manager::monitors](structonoff__manager.md#a501bb2c1c84293b1e4fbd011c62f5c69)

sys\_slist\_t monitors

List of monitors to be notified of state changes including errors and transition completion.

**Definition** onoff.h:163

[onoff\_manager::flags](structonoff__manager.md#a50d51cd3700e610b2f650607373afeb4)

uint16\_t flags

Flags identifying the service state.

**Definition** onoff.h:175

[onoff\_manager::last\_res](structonoff__manager.md#a5f555de973d72ba1889655c3342c8dc7)

int last\_res

The result of the last transition.

**Definition** onoff.h:172

[onoff\_manager::transitions](structonoff__manager.md#adcbe3b90e1618d3e7e223da106790457)

const struct onoff\_transitions \* transitions

Transition functions.

**Definition** onoff.h:166

[onoff\_manager::lock](structonoff__manager.md#af87f180f0494f02054e33086ee940493)

struct k\_spinlock lock

Mutex protection for other fields.

**Definition** onoff.h:169

[onoff\_monitor](structonoff__monitor.md)

Registration state for notifications of onoff service transitions.

**Definition** onoff.h:524

[onoff\_monitor::node](structonoff__monitor.md#a732a81eb0d9b36376b39b1a340fd1fe6)

sys\_snode\_t node

Links the client into the set of waiting service users.

**Definition** onoff.h:529

[onoff\_monitor::callback](structonoff__monitor.md#ab26d8ae8a0dac5e03549e2d9aca243a4)

onoff\_monitor\_callback callback

Callback to be invoked on state change.

**Definition** onoff.h:535

[onoff\_sync\_service](structonoff__sync__service.md)

State used when a driver uses the on-off service API for synchronous operations.

**Definition** onoff.h:576

[onoff\_sync\_service::lock](structonoff__sync__service.md#ac08d780a80fed2d89c1334cc3c65eeed)

struct k\_spinlock lock

Mutex protection for other fields.

**Definition** onoff.h:578

[onoff\_sync\_service::count](structonoff__sync__service.md#adff029426035dffb57fda0de44f2abae)

int32\_t count

Negative is error, non-negative is reference count.

**Definition** onoff.h:581

[onoff\_transitions](structonoff__transitions.md)

On-off service transition functions.

**Definition** onoff.h:133

[onoff\_transitions::reset](structonoff__transitions.md#a335d7d2f8418e78b237cfb4199b6f6aa)

onoff\_transition\_fn reset

Function to force the service state to reset, where supported.

**Definition** onoff.h:143

[onoff\_transitions::start](structonoff__transitions.md#a86417dd542c8f259ad1fc1c7d3c26545)

onoff\_transition\_fn start

Function to invoke to transition the service to on.

**Definition** onoff.h:135

[onoff\_transitions::stop](structonoff__transitions.md#a91a1805daabae70d362441634bfa508d)

onoff\_transition\_fn stop

Function to invoke to transition the service to off.

**Definition** onoff.h:138

[sys\_notify](structsys__notify.md)

State associated with notification for an asynchronous operation.

**Definition** notify.h:138

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [onoff.h](onoff_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
