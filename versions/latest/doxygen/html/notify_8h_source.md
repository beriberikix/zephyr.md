---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/notify_8h_source.html
original_path: doxygen/html/notify_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

notify.h

[Go to the documentation of this file.](notify_8h.md)

1/\*

2 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

3 \* Copyright (c) 2020 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_SYS\_NOTIFY\_H\_

9#define ZEPHYR\_INCLUDE\_SYS\_NOTIFY\_H\_

10

11#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18struct [sys\_notify](structsys__notify.md);

19

20/\*

21 \* Flag value that overwrites the method field when the operation has

22 \* completed.

23 \*/

[ 24](notify_8h.md#ad408b122f7f121c0739ac09e3399baa4)#define SYS\_NOTIFY\_METHOD\_COMPLETED 0

25

26/\*

27 \* Indicates that no notification will be provided.

28 \*

29 \* Callers must check for completions using

30 \* sys\_notify\_fetch\_result().

31 \*

32 \* See sys\_notify\_init\_spinwait().

33 \*/

[ 34](notify_8h.md#a36fc74f78d421ddf0fe3dfd48d0e5a99)#define SYS\_NOTIFY\_METHOD\_SPINWAIT 1

35

36/\*

37 \* Select notification through @ref k\_poll signal

38 \*

39 \* See sys\_notify\_init\_signal().

40 \*/

[ 41](notify_8h.md#aba2f89370639d6733ec8d75fadb44678)#define SYS\_NOTIFY\_METHOD\_SIGNAL 2

42

43/\*

44 \* Select notification through a user-provided callback.

45 \*

46 \* See sys\_notify\_init\_callback().

47 \*/

[ 48](notify_8h.md#a541b0198e2425c4dfa0d3e7abbdb9c60)#define SYS\_NOTIFY\_METHOD\_CALLBACK 3

49

[ 50](notify_8h.md#a5f13b732e247f2903dcd82dc52f9d797)#define SYS\_NOTIFY\_METHOD\_MASK 0x03U

[ 51](notify_8h.md#a63af5c6773172a0f3881d11b7b2e58b6)#define SYS\_NOTIFY\_METHOD\_POS 0

52

[ 66](notify_8h.md#aa22143622004e478668cdd98a2e04357)#define SYS\_NOTIFY\_EXTENSION\_POS 2

67

68/\*

69 \* Mask isolating the bits of sys\_notify::flags that are available

70 \* for extension.

71 \*/

[ 72](notify_8h.md#a87d3145d44e9638070131dcfb21c6636)#define SYS\_NOTIFY\_EXTENSION\_MASK (~BIT\_MASK(SYS\_NOTIFY\_EXTENSION\_POS))

73

79

[ 98](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499)typedef void (\*[sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499))();

99

[ 138](structsys__notify.md)struct [sys\_notify](structsys__notify.md) {

[ 139](unionsys__notify_1_1method.md) union [method](unionsys__notify_1_1method.md) {

140 /\* Pointer to signal used to notify client.

141 \*

142 \* The signal value corresponds to the res parameter

143 \* of sys\_notify\_callback.

144 \*/

[ 145](unionsys__notify_1_1method.md#a6db217c9960d59b8046457d0503f56d3) struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](unionsys__notify_1_1method.md#a6db217c9960d59b8046457d0503f56d3);

146

147 /\* Generic callback function for callback notification. \*/

[ 148](unionsys__notify_1_1method.md#abb9d173c53db24a5388327cf05110020) [sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) [callback](unionsys__notify_1_1method.md#abb9d173c53db24a5388327cf05110020);

[ 149](structsys__notify.md#a9c74bb70d56f0e5c809b26754c3b6fcd) } [method](structsys__notify.md#a9c74bb70d56f0e5c809b26754c3b6fcd);

150

151 /\*

152 \* Flags recording information about the operation.

153 \*

154 \* Bits below SYS\_NOTIFY\_EXTENSION\_POS are initialized by

155 \* async notify API init functions like

156 \* sys\_notify\_init\_callback(), and must not by modified by

157 \* extensions or client code.

158 \*

159 \* Bits at and above SYS\_NOTIFY\_EXTENSION\_POS are available

160 \* for use by service extensions while the containing object

161 \* is managed by the service. They are not for client use,

162 \* are zeroed by the async notify API init functions, and will

163 \* be zeroed by sys\_notify\_finalize().

164 \*/

[ 165](structsys__notify.md#a0816d524409695b9b1480e7681507073) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) volatile [flags](structsys__notify.md#a0816d524409695b9b1480e7681507073);

166

167 /\*

168 \* The result of the operation.

169 \*

170 \* This is the value that was (or would be) passed to the

171 \* async infrastructure. This field is the sole record of

172 \* success or failure for spin-wait synchronous operations.

173 \*/

[ 174](structsys__notify.md#a6ea09c4e58d0eaaad3dd63ee4a311a21) int volatile [result](structsys__notify.md#a6ea09c4e58d0eaaad3dd63ee4a311a21);

175};

176

[ 178](group__sys__notify__apis.md#ga19a2ca050ef4fcd4fac70e73c3fd3514)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_notify\_get\_method](group__sys__notify__apis.md#ga19a2ca050ef4fcd4fac70e73c3fd3514)(const struct [sys\_notify](structsys__notify.md) \*notify)

179{

180 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) method = notify->[flags](structsys__notify.md#a0816d524409695b9b1480e7681507073) >> [SYS\_NOTIFY\_METHOD\_POS](notify_8h.md#a63af5c6773172a0f3881d11b7b2e58b6);

181

182 return method & [SYS\_NOTIFY\_METHOD\_MASK](notify_8h.md#a5f13b732e247f2903dcd82dc52f9d797);

183}

184

[ 204](group__sys__notify__apis.md#ga71a9ccb690151020a6abea2ec9ffc667)int [sys\_notify\_validate](group__sys__notify__apis.md#ga71a9ccb690151020a6abea2ec9ffc667)(struct [sys\_notify](structsys__notify.md) \*notify);

205

[ 222](group__sys__notify__apis.md#ga424b1c94c1010bdc4170cf06c7f2ec72)[sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) [sys\_notify\_finalize](group__sys__notify__apis.md#ga424b1c94c1010bdc4170cf06c7f2ec72)(struct [sys\_notify](structsys__notify.md) \*notify,

223 int res);

224

[ 237](group__sys__notify__apis.md#ga823397b1917e10593d606daf3ec06a65)static inline int [sys\_notify\_fetch\_result](group__sys__notify__apis.md#ga823397b1917e10593d606daf3ec06a65)(const struct [sys\_notify](structsys__notify.md) \*notify,

238 int \*[result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1))

239{

240 \_\_ASSERT\_NO\_MSG(notify != NULL);

241 \_\_ASSERT\_NO\_MSG([result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1) != NULL);

242 int rv = -[EAGAIN](group__system__errno.md#gaf0fac1cea1165b4debec7f686edf3313);

243

244 if ([sys\_notify\_get\_method](group__sys__notify__apis.md#ga19a2ca050ef4fcd4fac70e73c3fd3514)(notify) == [SYS\_NOTIFY\_METHOD\_COMPLETED](notify_8h.md#ad408b122f7f121c0739ac09e3399baa4)) {

245 rv = 0;

246 \*[result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1) = notify->[result](structsys__notify.md#a6ea09c4e58d0eaaad3dd63ee4a311a21);

247 }

248

249 return rv;

250}

251

[ 264](group__sys__notify__apis.md#gad1a5c3e58ff962ab3cac743dde8c6c1e)static inline void [sys\_notify\_init\_spinwait](group__sys__notify__apis.md#gad1a5c3e58ff962ab3cac743dde8c6c1e)(struct [sys\_notify](structsys__notify.md) \*notify)

265{

266 \_\_ASSERT\_NO\_MSG(notify != NULL);

267

268 \*notify = (struct [sys\_notify](structsys__notify.md)){

269 .[flags](structsys__notify.md#a0816d524409695b9b1480e7681507073) = [SYS\_NOTIFY\_METHOD\_SPINWAIT](notify_8h.md#a36fc74f78d421ddf0fe3dfd48d0e5a99),

270 };

271}

272

[ 292](group__sys__notify__apis.md#ga30f9eff4b20b7d637a3a1df5f4cb38f8)static inline void [sys\_notify\_init\_signal](group__sys__notify__apis.md#ga30f9eff4b20b7d637a3a1df5f4cb38f8)(struct [sys\_notify](structsys__notify.md) \*notify,

293 struct [k\_poll\_signal](structk__poll__signal.md) \*sigp)

294{

295 \_\_ASSERT\_NO\_MSG(notify != NULL);

296 \_\_ASSERT\_NO\_MSG(sigp != NULL);

297

298 \*notify = (struct [sys\_notify](structsys__notify.md)){

299 .[method](structsys__notify.md#a9c74bb70d56f0e5c809b26754c3b6fcd) = {

300 .signal = sigp,

301 },

302 .flags = [SYS\_NOTIFY\_METHOD\_SIGNAL](notify_8h.md#aba2f89370639d6733ec8d75fadb44678),

303 };

304}

305

[ 321](group__sys__notify__apis.md#gaa9f31f78c03f48a3c649bbac15cc3a6c)static inline void [sys\_notify\_init\_callback](group__sys__notify__apis.md#gaa9f31f78c03f48a3c649bbac15cc3a6c)(struct [sys\_notify](structsys__notify.md) \*notify,

322 [sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499) handler)

323{

324 \_\_ASSERT\_NO\_MSG(notify != NULL);

325 \_\_ASSERT\_NO\_MSG(handler != NULL);

326

327 \*notify = (struct [sys\_notify](structsys__notify.md)){

328 .[method](structsys__notify.md#a9c74bb70d56f0e5c809b26754c3b6fcd) = {

329 .callback = handler,

330 },

331 .flags = [SYS\_NOTIFY\_METHOD\_CALLBACK](notify_8h.md#a541b0198e2425c4dfa0d3e7abbdb9c60),

332 };

333}

334

[ 346](group__sys__notify__apis.md#ga9772f8b356685acd707bd905860a2ca7)static inline bool [sys\_notify\_uses\_callback](group__sys__notify__apis.md#ga9772f8b356685acd707bd905860a2ca7)(const struct [sys\_notify](structsys__notify.md) \*notify)

347{

348 \_\_ASSERT\_NO\_MSG(notify != NULL);

349

350 return [sys\_notify\_get\_method](group__sys__notify__apis.md#ga19a2ca050ef4fcd4fac70e73c3fd3514)(notify) == [SYS\_NOTIFY\_METHOD\_CALLBACK](notify_8h.md#a541b0198e2425c4dfa0d3e7abbdb9c60);

351}

352

354

355#ifdef \_\_cplusplus

356}

357#endif

358

359#endif /\* ZEPHYR\_INCLUDE\_SYS\_NOTIFY\_H\_ \*/

[sys\_notify\_get\_method](group__sys__notify__apis.md#ga19a2ca050ef4fcd4fac70e73c3fd3514)

static uint32\_t sys\_notify\_get\_method(const struct sys\_notify \*notify)

**Definition** notify.h:178

[sys\_notify\_generic\_callback](group__sys__notify__apis.md#ga2a9ffe35a5ad44fb7c5b00bb5c5c0499)

void(\* sys\_notify\_generic\_callback)()

Generic signature used to notify of result completion by callback.

**Definition** notify.h:98

[sys\_notify\_init\_signal](group__sys__notify__apis.md#ga30f9eff4b20b7d637a3a1df5f4cb38f8)

static void sys\_notify\_init\_signal(struct sys\_notify \*notify, struct k\_poll\_signal \*sigp)

Initialize a notify object for (k\_poll) signal notification.

**Definition** notify.h:292

[sys\_notify\_finalize](group__sys__notify__apis.md#ga424b1c94c1010bdc4170cf06c7f2ec72)

sys\_notify\_generic\_callback sys\_notify\_finalize(struct sys\_notify \*notify, int res)

Record and signal the operation completion.

[sys\_notify\_validate](group__sys__notify__apis.md#ga71a9ccb690151020a6abea2ec9ffc667)

int sys\_notify\_validate(struct sys\_notify \*notify)

Validate and initialize the notify structure.

[sys\_notify\_fetch\_result](group__sys__notify__apis.md#ga823397b1917e10593d606daf3ec06a65)

static int sys\_notify\_fetch\_result(const struct sys\_notify \*notify, int \*result)

Check for and read the result of an asynchronous operation.

**Definition** notify.h:237

[sys\_notify\_uses\_callback](group__sys__notify__apis.md#ga9772f8b356685acd707bd905860a2ca7)

static bool sys\_notify\_uses\_callback(const struct sys\_notify \*notify)

Detect whether a particular notification uses a callback.

**Definition** notify.h:346

[sys\_notify\_init\_callback](group__sys__notify__apis.md#gaa9f31f78c03f48a3c649bbac15cc3a6c)

static void sys\_notify\_init\_callback(struct sys\_notify \*notify, sys\_notify\_generic\_callback handler)

Initialize a notify object for callback notification.

**Definition** notify.h:321

[sys\_notify\_init\_spinwait](group__sys__notify__apis.md#gad1a5c3e58ff962ab3cac743dde8c6c1e)

static void sys\_notify\_init\_spinwait(struct sys\_notify \*notify)

Initialize a notify object for spin-wait notification.

**Definition** notify.h:264

[EAGAIN](group__system__errno.md#gaf0fac1cea1165b4debec7f686edf3313)

#define EAGAIN

No more contexts.

**Definition** errno.h:50

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[SYS\_NOTIFY\_METHOD\_SPINWAIT](notify_8h.md#a36fc74f78d421ddf0fe3dfd48d0e5a99)

#define SYS\_NOTIFY\_METHOD\_SPINWAIT

**Definition** notify.h:34

[SYS\_NOTIFY\_METHOD\_CALLBACK](notify_8h.md#a541b0198e2425c4dfa0d3e7abbdb9c60)

#define SYS\_NOTIFY\_METHOD\_CALLBACK

**Definition** notify.h:48

[SYS\_NOTIFY\_METHOD\_MASK](notify_8h.md#a5f13b732e247f2903dcd82dc52f9d797)

#define SYS\_NOTIFY\_METHOD\_MASK

**Definition** notify.h:50

[SYS\_NOTIFY\_METHOD\_POS](notify_8h.md#a63af5c6773172a0f3881d11b7b2e58b6)

#define SYS\_NOTIFY\_METHOD\_POS

**Definition** notify.h:51

[SYS\_NOTIFY\_METHOD\_SIGNAL](notify_8h.md#aba2f89370639d6733ec8d75fadb44678)

#define SYS\_NOTIFY\_METHOD\_SIGNAL

**Definition** notify.h:41

[SYS\_NOTIFY\_METHOD\_COMPLETED](notify_8h.md#ad408b122f7f121c0739ac09e3399baa4)

#define SYS\_NOTIFY\_METHOD\_COMPLETED

**Definition** notify.h:24

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5622

[k\_poll\_signal::result](structk__poll__signal.md#ab438c1e36cecda66fe2c4642518a1db1)

int result

custom result value passed to k\_poll\_signal\_raise() if needed

**Definition** kernel.h:5633

[sys\_notify](structsys__notify.md)

State associated with notification for an asynchronous operation.

**Definition** notify.h:138

[sys\_notify::flags](structsys__notify.md#a0816d524409695b9b1480e7681507073)

uint32\_t volatile flags

**Definition** notify.h:165

[sys\_notify::result](structsys__notify.md#a6ea09c4e58d0eaaad3dd63ee4a311a21)

int volatile result

**Definition** notify.h:174

[sys\_notify::method](structsys__notify.md#a9c74bb70d56f0e5c809b26754c3b6fcd)

union sys\_notify::method method

[sys\_notify::method](unionsys__notify_1_1method.md)

**Definition** notify.h:139

[sys\_notify::method::signal](unionsys__notify_1_1method.md#a6db217c9960d59b8046457d0503f56d3)

struct k\_poll\_signal \* signal

**Definition** notify.h:145

[sys\_notify::method::callback](unionsys__notify_1_1method.md#abb9d173c53db24a5388327cf05110020)

sys\_notify\_generic\_callback callback

**Definition** notify.h:148

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [notify.h](notify_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
