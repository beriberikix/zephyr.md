---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ipm_8h_source.html
original_path: doxygen/html/ipm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22

23#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 45](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa)typedef void (\*[ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa))(const struct [device](structdevice.md) \*ipmdev, void \*user\_data,

46 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, volatile void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

47

[ 54](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b)typedef int (\*[ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b))(const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id,

55 const void \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), int size);

[ 62](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03)typedef int (\*[ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03))(const struct [device](structdevice.md) \*ipmdev);

63

[ 70](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000))(const struct [device](structdevice.md) \*ipmdev);

71

[ 78](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b)typedef void (\*[ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b))(const struct [device](structdevice.md) \*port,

79 [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) cb,

80 void \*user\_data);

81

[ 88](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784)typedef int (\*[ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784))(const struct [device](structdevice.md) \*ipmdev, int enable);

89

[ 96](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440)typedef void (\*[ipm\_complete\_t](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440))(const struct [device](structdevice.md) \*ipmdev);

97

[ 98](structipm__driver__api.md)\_\_subsystem struct [ipm\_driver\_api](structipm__driver__api.md) {

[ 99](structipm__driver__api.md#ac6f87ae1296bf83759c60e57b8740fd1) [ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b) [send](structipm__driver__api.md#ac6f87ae1296bf83759c60e57b8740fd1);

[ 100](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d) [ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b) [register\_callback](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d);

[ 101](structipm__driver__api.md#a33d936ed9e0606a653a88563268c9543) [ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03) [max\_data\_size\_get](structipm__driver__api.md#a33d936ed9e0606a653a88563268c9543);

[ 102](structipm__driver__api.md#a69f7264ac909a0c9aec3676766e807af) [ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000) [max\_id\_val\_get](structipm__driver__api.md#a69f7264ac909a0c9aec3676766e807af);

[ 103](structipm__driver__api.md#ac17dd018dcf02538c6f2d97005d5494b) [ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784) [set\_enabled](structipm__driver__api.md#ac17dd018dcf02538c6f2d97005d5494b);

104#ifdef CONFIG\_IPM\_CALLBACK\_ASYNC

105 [ipm\_complete\_t](group__ipm__interface.md#ga1aff2b36a9b7712a1fa743052282d440) complete;

106#endif

107};

108

[ 144](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043)\_\_syscall int [ipm\_send](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043)(const struct [device](structdevice.md) \*ipmdev, int wait, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id,

145 const void \*data, int size);

146

147static inline int z\_impl\_ipm\_send(const struct [device](structdevice.md) \*ipmdev, int wait,

148 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id,

149 const void \*data, int size)

150{

151 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

152 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

153

154 return api->send(ipmdev, wait, id, data, size);

155}

156

[ 165](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b)static inline void [ipm\_register\_callback](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b)(const struct [device](structdevice.md) \*ipmdev,

166 [ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa) cb, void \*user\_data)

167{

168 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

169 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

170

171 api->[register\_callback](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d)(ipmdev, cb, user\_data);

172}

173

[ 184](group__ipm__interface.md#ga0a11eecaa7254575ab6baf0783a18b5e)\_\_syscall int [ipm\_max\_data\_size\_get](group__ipm__interface.md#ga0a11eecaa7254575ab6baf0783a18b5e)(const struct [device](structdevice.md) \*ipmdev);

185

186static inline int z\_impl\_ipm\_max\_data\_size\_get(const struct [device](structdevice.md) \*ipmdev)

187{

188 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

189 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

190

191 return api->max\_data\_size\_get(ipmdev);

192}

193

194

[ 205](group__ipm__interface.md#ga168fd277b7819b639baa4e630c596a7f)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ipm\_max\_id\_val\_get](group__ipm__interface.md#ga168fd277b7819b639baa4e630c596a7f)(const struct [device](structdevice.md) \*ipmdev);

206

207static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_ipm\_max\_id\_val\_get(const struct [device](structdevice.md) \*ipmdev)

208{

209 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

210 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

211

212 return api->max\_id\_val\_get(ipmdev);

213}

214

[ 224](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b)\_\_syscall int [ipm\_set\_enabled](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b)(const struct [device](structdevice.md) \*ipmdev, int enable);

225

226static inline int z\_impl\_ipm\_set\_enabled(const struct [device](structdevice.md) \*ipmdev,

227 int enable)

228{

229 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

230 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

231

232 return api->set\_enabled(ipmdev, enable);

233}

234

[ 249](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2)\_\_syscall void [ipm\_complete](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2)(const struct [device](structdevice.md) \*ipmdev);

250

251static inline void z\_impl\_ipm\_complete(const struct [device](structdevice.md) \*ipmdev)

252{

253#ifdef CONFIG\_IPM\_CALLBACK\_ASYNC

254 const struct [ipm\_driver\_api](structipm__driver__api.md) \*api =

255 (const struct [ipm\_driver\_api](structipm__driver__api.md) \*)ipmdev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

256

257 if (api->complete != NULL) {

258 api->complete(ipmdev);

259 }

260#endif

261}

262

263#ifdef \_\_cplusplus

264}

265#endif

266

270

271#include <syscalls/ipm.h>

272

273#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_IPM\_H\_ \*/

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

**Definition** ipm.h:96

[ipm\_callback\_t](group__ipm__interface.md#ga20d7547dcea80bc769d5e323bd91cdaa)

void(\* ipm\_callback\_t)(const struct device \*ipmdev, void \*user\_data, uint32\_t id, volatile void \*data)

Callback API for incoming IPM messages.

**Definition** ipm.h:45

[ipm\_max\_data\_size\_get\_t](group__ipm__interface.md#ga34c3a4782175068eda6443c521094a03)

int(\* ipm\_max\_data\_size\_get\_t)(const struct device \*ipmdev)

Callback API to get maximum data size.

**Definition** ipm.h:62

[ipm\_send\_t](group__ipm__interface.md#ga45fb35e92b26b04ed4c665d50912ff3b)

int(\* ipm\_send\_t)(const struct device \*ipmdev, int wait, uint32\_t id, const void \*data, int size)

Callback API to send IPM messages.

**Definition** ipm.h:54

[ipm\_complete](group__ipm__interface.md#ga53f785ecfac17b9fb2e5f3a9505c7fd2)

void ipm\_complete(const struct device \*ipmdev)

Signal asynchronous command completion.

[ipm\_register\_callback](group__ipm__interface.md#ga557b15bc8a353483ca55888dba27493b)

static void ipm\_register\_callback(const struct device \*ipmdev, ipm\_callback\_t cb, void \*user\_data)

Register a callback function for incoming messages.

**Definition** ipm.h:165

[ipm\_set\_enabled](group__ipm__interface.md#ga5884fa95cb38ddfe4493eb70dafebe8b)

int ipm\_set\_enabled(const struct device \*ipmdev, int enable)

Enable interrupts and callbacks for inbound channels.

[ipm\_send](group__ipm__interface.md#ga8f3fe21c1a4ffd3c38b67f81749af043)

int ipm\_send(const struct device \*ipmdev, int wait, uint32\_t id, const void \*data, int size)

Try to send a message over the IPM device.

[ipm\_register\_callback\_t](group__ipm__interface.md#ga8f7b338aa9f5d4aa1c218db412da562b)

void(\* ipm\_register\_callback\_t)(const struct device \*port, ipm\_callback\_t cb, void \*user\_data)

Callback API upon registration.

**Definition** ipm.h:78

[ipm\_max\_id\_val\_get\_t](group__ipm__interface.md#gaa50f765662f9d1dbea75902211de7000)

uint32\_t(\* ipm\_max\_id\_val\_get\_t)(const struct device \*ipmdev)

Callback API to get the ID's maximum value.

**Definition** ipm.h:70

[ipm\_set\_enabled\_t](group__ipm__interface.md#gab1faa1ebf47e2c12286bac0ce8be7784)

int(\* ipm\_set\_enabled\_t)(const struct device \*ipmdev, int enable)

Callback API upon enablement of interrupts.

**Definition** ipm.h:88

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[ipm\_driver\_api](structipm__driver__api.md)

**Definition** ipm.h:98

[ipm\_driver\_api::register\_callback](structipm__driver__api.md#a073f9928135a6e9ed022edf877c2181d)

ipm\_register\_callback\_t register\_callback

**Definition** ipm.h:100

[ipm\_driver\_api::max\_data\_size\_get](structipm__driver__api.md#a33d936ed9e0606a653a88563268c9543)

ipm\_max\_data\_size\_get\_t max\_data\_size\_get

**Definition** ipm.h:101

[ipm\_driver\_api::max\_id\_val\_get](structipm__driver__api.md#a69f7264ac909a0c9aec3676766e807af)

ipm\_max\_id\_val\_get\_t max\_id\_val\_get

**Definition** ipm.h:102

[ipm\_driver\_api::set\_enabled](structipm__driver__api.md#ac17dd018dcf02538c6f2d97005d5494b)

ipm\_set\_enabled\_t set\_enabled

**Definition** ipm.h:103

[ipm\_driver\_api::send](structipm__driver__api.md#ac6f87ae1296bf83759c60e57b8740fd1)

ipm\_send\_t send

**Definition** ipm.h:99

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ipm.h](ipm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
