---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ipm_8h_source.html
original_path: doxygen/html/ipm_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm.h

[Go to the documentation of this file.](ipm_8h.md)

1

6

7/\*

8 \* Copyright (c) 2015 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_IPM\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_IPM\_H\_

15

24

25#include <[zephyr/kernel.h](kernel_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 47](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa)typedef void (\*[ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa))(const struct [device](structdevice.md) \*ipmdev, void \*user\_data,

48 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, volatile void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

49

[ 56](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b)typedef int (\*[ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b))(const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id,

57 const void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), int size);

[ 64](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03)typedef int (\*[ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03))(const struct [device](structdevice.md) \*ipmdev);

65

[ 72](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000))(const struct [device](structdevice.md) \*ipmdev);

73

[ 80](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b)typedef void (\*[ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b))(const struct [device](structdevice.md) \*port,

81 [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) cb,

82 void \*user\_data);

83

[ 90](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784)typedef int (\*[ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784))(const struct [device](structdevice.md) \*ipmdev, int enable);

91

[ 98](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440)typedef void (\*[ipm\_complete\_t](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440))(const struct [device](structdevice.md) \*ipmdev);

99

[ 100](structipm__driver__api.md)\_\_subsystem struct [ipm\_driver\_api](structipm__driver__api.md) {

[ 101](structipm__driver__api.md#ac6f87ae1296bf83759c60e57b8740fd1) [ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b) [send](structipm__driver__api.md#ac6f87ae1296bf83759c60e57b8740fd1);

[ 102](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d) [ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b) [register\_callback](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d);

[ 103](structipm__driver__api.md#a33d936ed9e0606a653a88563268c9543) [ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03) [max\_data\_size\_get](structipm__driver__api.md#a33d936ed9e0606a653a88563268c9543);

[ 104](structipm__driver__api.md#a69f7264ac909a0c9aec3676766e807af) [ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000) [max\_id\_val\_get](structipm__driver__api.md#a69f7264ac909a0c9aec3676766e807af);

[ 105](structipm__driver__api.md#ac17dd018dcf02538c6f2d97005d5494b) [ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784) [set\_enabled](structipm__driver__api.md#ac17dd018dcf02538c6f2d97005d5494b);

106#ifdef CONFIG\_IPM\_CALLBACK\_ASYNC

107 [ipm\_complete\_t](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440) complete;

108#endif

109};

110

[ 146](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043)\_\_syscall int [ipm\_send](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043)(const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id,

147 const void \*data, int size);

148

149static inline int z\_impl\_ipm\_send(const struct [device](structdevice.md) \*ipmdev, int wait,

150 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id,

151 const void \*data, int size)

152{

153 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

154 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

155

156 return api->send(ipmdev, wait, id, data, size);

157}

158

[ 167](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b)static inline void [ipm\_register\_callback](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b)(const struct [device](structdevice.md) \*ipmdev,

168 [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data)

169{

170 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

171 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

172

173 api->[register\_callback](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d)(ipmdev, cb, user\_data);

174}

175

[ 186](group__ipm__interface.md#ga0a11eecaa7254575ab6baf0783a18b5e)\_\_syscall int [ipm\_max\_data\_size\_get](group__ipm__interface.md#ga0a11eecaa7254575ab6baf0783a18b5e)(const struct [device](structdevice.md) \*ipmdev);

187

188static inline int z\_impl\_ipm\_max\_data\_size\_get(const struct [device](structdevice.md) \*ipmdev)

189{

190 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

191 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

192

193 return api->max\_data\_size\_get(ipmdev);

194}

195

196

[ 207](group__ipm__interface.md#ga168fd277b7819b639baa4e630c596a7f)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ipm\_max\_id\_val\_get](group__ipm__interface.md#ga168fd277b7819b639baa4e630c596a7f)(const struct [device](structdevice.md) \*ipmdev);

208

209static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_ipm\_max\_id\_val\_get(const struct [device](structdevice.md) \*ipmdev)

210{

211 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

212 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

213

214 return api->max\_id\_val\_get(ipmdev);

215}

216

[ 226](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b)\_\_syscall int [ipm\_set\_enabled](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b)(const struct [device](structdevice.md) \*ipmdev, int enable);

227

228static inline int z\_impl\_ipm\_set\_enabled(const struct [device](structdevice.md) \*ipmdev,

229 int enable)

230{

231 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

232 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

233

234 return api->set\_enabled(ipmdev, enable);

235}

236

[ 251](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2)\_\_syscall void [ipm\_complete](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2)(const struct [device](structdevice.md) \*ipmdev);

252

253static inline void z\_impl\_ipm\_complete(const struct [device](structdevice.md) \*ipmdev)

254{

255#ifdef CONFIG\_IPM\_CALLBACK\_ASYNC

256 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

257 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

258

259 if (api->complete != NULL) {

260 api->complete(ipmdev);

261 }

262#endif

263}

264

265#ifdef \_\_cplusplus

266}

267#endif

268

272

273#include <zephyr/syscalls/ipm.h>

274

275#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_IPM\_H\_ \*/

[device.h](device_8h.md)

[ipm\_max\_data\_size\_get](group__ipm__interface.md#ga0a11eecaa7254575ab6baf0783a18b5e)

int ipm\_max\_data\_size\_get(const struct device \*ipmdev)

Return the maximum number of bytes possible in an outbound message.

[ipm\_max\_id\_val\_get](group__ipm__interface.md#ga168fd277b7819b639baa4e630c596a7f)

uint32\_t ipm\_max\_id\_val\_get(const struct device \*ipmdev)

Return the maximum id value possible in an outbound message.

[ipm\_complete\_t](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440)

void(\* ipm\_complete\_t)(const struct device \*ipmdev)

Callback API upon command completion.

**Definition** ipm.h:98

[ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa)

void(\* ipm\_callback\_t)(const struct device \*ipmdev, void \*user\_data, uint32\_t id, volatile void \*data)

Callback API for incoming IPM messages.

**Definition** ipm.h:47

[ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03)

int(\* ipm\_max\_data\_size\_get\_t)(const struct device \*ipmdev)

Callback API to get maximum data size.

**Definition** ipm.h:64

[ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b)

int(\* ipm\_send\_t)(const struct device \*ipmdev, int wait, uint32\_t id, const void \*data, int size)

Callback API to send IPM messages.

**Definition** ipm.h:56

[ipm\_complete](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2)

void ipm\_complete(const struct device \*ipmdev)

Signal asynchronous command completion.

[ipm\_register\_callback](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b)

static void ipm\_register\_callback(const struct device \*ipmdev, ipm\_callback\_t cb, void \*user\_data)

Register a callback function for incoming messages.

**Definition** ipm.h:167

[ipm\_set\_enabled](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b)

int ipm\_set\_enabled(const struct device \*ipmdev, int enable)

Enable interrupts and callbacks for inbound channels.

[ipm\_send](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043)

int ipm\_send(const struct device \*ipmdev, int wait, uint32\_t id, const void \*data, int size)

Try to send a message over the IPM device.

[ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b)

void(\* ipm\_register\_callback\_t)(const struct device \*port, ipm\_callback\_t cb, void \*user\_data)

Callback API upon registration.

**Definition** ipm.h:80

[ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000)

uint32\_t(\* ipm\_max\_id\_val\_get\_t)(const struct device \*ipmdev)

Callback API to get the ID's maximum value.

**Definition** ipm.h:72

[ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784)

int(\* ipm\_set\_enabled\_t)(const struct device \*ipmdev, int enable)

Callback API upon enablement of interrupts.

**Definition** ipm.h:90

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[ipm\_driver\_api](structipm__driver__api.md)

**Definition** ipm.h:100

[ipm\_driver\_api::register\_callback](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d)

ipm\_register\_callback\_t register\_callback

**Definition** ipm.h:102

[ipm\_driver\_api::max\_data\_size\_get](structipm__driver__api.md#a33d936ed9e0606a653a88563268c9543)

ipm\_max\_data\_size\_get\_t max\_data\_size\_get

**Definition** ipm.h:103

[ipm\_driver\_api::max\_id\_val\_get](structipm__driver__api.md#a69f7264ac909a0c9aec3676766e807af)

ipm\_max\_id\_val\_get\_t max\_id\_val\_get

**Definition** ipm.h:104

[ipm\_driver\_api::set\_enabled](structipm__driver__api.md#ac17dd018dcf02538c6f2d97005d5494b)

ipm\_set\_enabled\_t set\_enabled

**Definition** ipm.h:105

[ipm\_driver\_api::send](structipm__driver__api.md#ac6f87ae1296bf83759c60e57b8740fd1)

ipm\_send\_t send

**Definition** ipm.h:101

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ipm.h](ipm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
