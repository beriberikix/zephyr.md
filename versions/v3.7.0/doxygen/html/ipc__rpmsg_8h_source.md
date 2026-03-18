---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ipc__rpmsg_8h_source.html
original_path: doxygen/html/ipc__rpmsg_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_rpmsg.h

[Go to the documentation of this file.](ipc__rpmsg_8h.md)

1/\*

2 \* Copyright (c) 2021 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_RPMSG\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_RPMSG\_H\_

9

10#include <[zephyr/ipc/ipc\_service.h](ipc__service_8h.md)>

11#include <openamp/open\_amp.h>

12#include <metal/device.h>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 26](group__ipc__service__rpmsg__api.md#gada0274bbd763278066d01de34c4e7072)#define NUM\_ENDPOINTS CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE

27

28struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md);

29

[ 39](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803)typedef void (\*[rpmsg\_ept\_bound\_cb](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803))(struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept);

40

[ 45](structipc__rpmsg__ept.md)struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) {

[ 47](structipc__rpmsg__ept.md#a43d1c7fc6091bc5ce1d782af1828a76a) struct rpmsg\_endpoint [ep](structipc__rpmsg__ept.md#a43d1c7fc6091bc5ce1d782af1828a76a);

48

[ 50](structipc__rpmsg__ept.md#a052045f7e5cfdcc83a5d3545b41ac18a) char [name](structipc__rpmsg__ept.md#a052045f7e5cfdcc83a5d3545b41ac18a)[RPMSG\_NAME\_SIZE];

51

[ 53](structipc__rpmsg__ept.md#ad6bf7b86ee9a9a739f0b46ee51276f28) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dest](structipc__rpmsg__ept.md#ad6bf7b86ee9a9a739f0b46ee51276f28);

54

[ 56](structipc__rpmsg__ept.md#a8159e224bc1a4ceb17081eea1c16d44d) volatile bool [bound](structipc__rpmsg__ept.md#a8159e224bc1a4ceb17081eea1c16d44d);

57

[ 59](structipc__rpmsg__ept.md#a5029a16ddadb1a6809f28e0c94826ece) const struct [ipc\_service\_cb](structipc__service__cb.md) \*[cb](structipc__rpmsg__ept.md#a5029a16ddadb1a6809f28e0c94826ece);

60

[ 62](structipc__rpmsg__ept.md#ad4f964f88d2cb7498b843f2c6b2804e3) void \*[priv](structipc__rpmsg__ept.md#ad4f964f88d2cb7498b843f2c6b2804e3);

63};

64

[ 69](structipc__rpmsg__instance.md)struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) {

[ 71](structipc__rpmsg__instance.md#afd5e2760bead6932c052c03c1f7f29e5) struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) [endpoint](structipc__rpmsg__instance.md#afd5e2760bead6932c052c03c1f7f29e5)[[NUM\_ENDPOINTS](group__ipc__service__rpmsg__api.md#gada0274bbd763278066d01de34c4e7072)];

72

[ 74](structipc__rpmsg__instance.md#a8017686ab6afc36ff589d6e89dda9feb) struct rpmsg\_virtio\_device [rvdev](structipc__rpmsg__instance.md#a8017686ab6afc36ff589d6e89dda9feb);

75

[ 77](structipc__rpmsg__instance.md#a33da8a446e07b0000405a7381b1db4fb) struct rpmsg\_virtio\_shm\_pool [shm\_pool](structipc__rpmsg__instance.md#a33da8a446e07b0000405a7381b1db4fb);

78

[ 80](structipc__rpmsg__instance.md#a59125783afdf4a879e85ef7abaeb6f55) [rpmsg\_ept\_bound\_cb](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803) [bound\_cb](structipc__rpmsg__instance.md#a59125783afdf4a879e85ef7abaeb6f55);

81

[ 83](structipc__rpmsg__instance.md#a43f8aeddef2d8e1c5b03a0ebc93f252d) rpmsg\_ept\_cb [cb](structipc__rpmsg__instance.md#a43f8aeddef2d8e1c5b03a0ebc93f252d);

84

[ 86](structipc__rpmsg__instance.md#aac59ce6875ce277c9cbb1f2a1b61e732) struct [k\_mutex](structk__mutex.md) [mtx](structipc__rpmsg__instance.md#aac59ce6875ce277c9cbb1f2a1b61e732);

87};

88

[ 108](group__ipc__service__rpmsg__api.md#ga08e97e91d3512a3fe28aa80116c51ddf)int [ipc\_rpmsg\_init](group__ipc__service__rpmsg__api.md#ga08e97e91d3512a3fe28aa80116c51ddf)(struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance,

109 unsigned int role,

110 unsigned int buffer\_size,

111 struct metal\_io\_region \*shm\_io,

112 struct virtio\_device \*vdev,

113 void \*shb, size\_t size,

114 rpmsg\_ns\_bind\_cb ns\_bind\_cb);

115

116

[ 127](group__ipc__service__rpmsg__api.md#gaef3a7306082f88deb394f85a4bb5758b)int [ipc\_rpmsg\_deinit](group__ipc__service__rpmsg__api.md#gaef3a7306082f88deb394f85a4bb5758b)(struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance,

128 unsigned int role);

129

[ 142](group__ipc__service__rpmsg__api.md#ga9c8124e81f385155e3e1338d2ef4a78d)int [ipc\_rpmsg\_register\_ept](group__ipc__service__rpmsg__api.md#ga9c8124e81f385155e3e1338d2ef4a78d)(struct [ipc\_rpmsg\_instance](structipc__rpmsg__instance.md) \*instance, unsigned int role,

143 struct [ipc\_rpmsg\_ept](structipc__rpmsg__ept.md) \*ept);

144

148

149#ifdef \_\_cplusplus

150}

151#endif

152

153#endif /\* ZEPHYR\_INCLUDE\_IPC\_SERVICE\_IPC\_RPMSG\_H\_ \*/

[ipc\_rpmsg\_init](group__ipc__service__rpmsg__api.md#ga08e97e91d3512a3fe28aa80116c51ddf)

int ipc\_rpmsg\_init(struct ipc\_rpmsg\_instance \*instance, unsigned int role, unsigned int buffer\_size, struct metal\_io\_region \*shm\_io, struct virtio\_device \*vdev, void \*shb, size\_t size, rpmsg\_ns\_bind\_cb ns\_bind\_cb)

Init an RPMsg instance.

[ipc\_rpmsg\_register\_ept](group__ipc__service__rpmsg__api.md#ga9c8124e81f385155e3e1338d2ef4a78d)

int ipc\_rpmsg\_register\_ept(struct ipc\_rpmsg\_instance \*instance, unsigned int role, struct ipc\_rpmsg\_ept \*ept)

Register an endpoint.

[rpmsg\_ept\_bound\_cb](group__ipc__service__rpmsg__api.md#gad313c1e25e158bd91a0b0c3050012803)

void(\* rpmsg\_ept\_bound\_cb)(struct ipc\_rpmsg\_ept \*ept)

Define the bound callback.

**Definition** ipc\_rpmsg.h:39

[NUM\_ENDPOINTS](group__ipc__service__rpmsg__api.md#gada0274bbd763278066d01de34c4e7072)

#define NUM\_ENDPOINTS

Number of endpoints.

**Definition** ipc\_rpmsg.h:26

[ipc\_rpmsg\_deinit](group__ipc__service__rpmsg__api.md#gaef3a7306082f88deb394f85a4bb5758b)

int ipc\_rpmsg\_deinit(struct ipc\_rpmsg\_instance \*instance, unsigned int role)

Deinit an RPMsg instance.

[ipc\_service.h](ipc__service_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[ipc\_rpmsg\_ept](structipc__rpmsg__ept.md)

Endpoint structure.

**Definition** ipc\_rpmsg.h:45

[ipc\_rpmsg\_ept::name](structipc__rpmsg__ept.md#a052045f7e5cfdcc83a5d3545b41ac18a)

char name[RPMSG\_NAME\_SIZE]

Name of the endpoint.

**Definition** ipc\_rpmsg.h:50

[ipc\_rpmsg\_ept::ep](structipc__rpmsg__ept.md#a43d1c7fc6091bc5ce1d782af1828a76a)

struct rpmsg\_endpoint ep

RPMsg endpoint.

**Definition** ipc\_rpmsg.h:47

[ipc\_rpmsg\_ept::cb](structipc__rpmsg__ept.md#a5029a16ddadb1a6809f28e0c94826ece)

const struct ipc\_service\_cb \* cb

Callbacks.

**Definition** ipc\_rpmsg.h:59

[ipc\_rpmsg\_ept::bound](structipc__rpmsg__ept.md#a8159e224bc1a4ceb17081eea1c16d44d)

volatile bool bound

Bound flag.

**Definition** ipc\_rpmsg.h:56

[ipc\_rpmsg\_ept::priv](structipc__rpmsg__ept.md#ad4f964f88d2cb7498b843f2c6b2804e3)

void \* priv

Private data to be passed to the endpoint callbacks.

**Definition** ipc\_rpmsg.h:62

[ipc\_rpmsg\_ept::dest](structipc__rpmsg__ept.md#ad6bf7b86ee9a9a739f0b46ee51276f28)

uint32\_t dest

Destination endpoint.

**Definition** ipc\_rpmsg.h:53

[ipc\_rpmsg\_instance](structipc__rpmsg__instance.md)

RPMsg instance structure.

**Definition** ipc\_rpmsg.h:69

[ipc\_rpmsg\_instance::shm\_pool](structipc__rpmsg__instance.md#a33da8a446e07b0000405a7381b1db4fb)

struct rpmsg\_virtio\_shm\_pool shm\_pool

SHM pool.

**Definition** ipc\_rpmsg.h:77

[ipc\_rpmsg\_instance::cb](structipc__rpmsg__instance.md#a43f8aeddef2d8e1c5b03a0ebc93f252d)

rpmsg\_ept\_cb cb

EPT (instance) callback.

**Definition** ipc\_rpmsg.h:83

[ipc\_rpmsg\_instance::bound\_cb](structipc__rpmsg__instance.md#a59125783afdf4a879e85ef7abaeb6f55)

rpmsg\_ept\_bound\_cb bound\_cb

EPT (instance) bound callback.

**Definition** ipc\_rpmsg.h:80

[ipc\_rpmsg\_instance::rvdev](structipc__rpmsg__instance.md#a8017686ab6afc36ff589d6e89dda9feb)

struct rpmsg\_virtio\_device rvdev

RPMsg virtIO device.

**Definition** ipc\_rpmsg.h:74

[ipc\_rpmsg\_instance::mtx](structipc__rpmsg__instance.md#aac59ce6875ce277c9cbb1f2a1b61e732)

struct k\_mutex mtx

Mutex for the instance.

**Definition** ipc\_rpmsg.h:86

[ipc\_rpmsg\_instance::endpoint](structipc__rpmsg__instance.md#afd5e2760bead6932c052c03c1f7f29e5)

struct ipc\_rpmsg\_ept endpoint[CONFIG\_IPC\_SERVICE\_BACKEND\_RPMSG\_NUM\_ENDPOINTS\_PER\_INSTANCE]

Endpoints in the instance.

**Definition** ipc\_rpmsg.h:71

[ipc\_service\_cb](structipc__service__cb.md)

Event callback structure.

**Definition** ipc\_service.h:145

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [ipc\_rpmsg.h](ipc__rpmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
