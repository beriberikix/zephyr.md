---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/virtio_8h_source.html
original_path: doxygen/html/virtio_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtio.h

[Go to the documentation of this file.](virtio_8h.md)

1/\*

2 \* Copyright (c) 2024 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_VIRTIO\_VIRTIO\_H\_

8#define ZEPHYR\_VIRTIO\_VIRTIO\_H\_

9#include <[zephyr/device.h](device_8h.md)>

10#include "[virtio/virtqueue.h](virtqueue_8h.md)"

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

22

[ 31](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) (\*[virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4))(

32 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_queue\_size, void \*opaque

33);

34

[ 38](structvirtio__driver__api.md)\_\_subsystem struct [virtio\_driver\_api](structvirtio__driver__api.md) {

39 struct [virtq](structvirtq.md) \*(\*get\_virtqueue)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx);

[ 40](structvirtio__driver__api.md#a22eb11370ec5ea6a0f91334ae1ccff02) void (\*[notify\_virtqueue](structvirtio__driver__api.md#a22eb11370ec5ea6a0f91334ae1ccff02))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx);

[ 41](structvirtio__driver__api.md#a7add58b2a488e662443d99b5ef12aace) void \*(\*get\_device\_specific\_config)(const struct [device](structdevice.md) \*dev);

[ 42](structvirtio__driver__api.md#a6f324b95d6edcd044bf44734ec6897b9) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[read\_device\_feature\_bit](structvirtio__driver__api.md#a6f324b95d6edcd044bf44734ec6897b9))(const struct [device](structdevice.md) \*dev, int bit);

[ 43](structvirtio__driver__api.md#af6683e8641684e1cc206d1fde6bdb727) int (\*[write\_driver\_feature\_bit](structvirtio__driver__api.md#af6683e8641684e1cc206d1fde6bdb727))(const struct [device](structdevice.md) \*dev, int bit, bool value);

[ 44](structvirtio__driver__api.md#a8f39c335de27446a54ca2bea8d822546) int (\*[commit\_feature\_bits](structvirtio__driver__api.md#a8f39c335de27446a54ca2bea8d822546))(const struct [device](structdevice.md) \*dev);

[ 45](structvirtio__driver__api.md#aeffc9d53ed7bca3ffd7467d3bcbfaf65) int (\*[init\_virtqueues](structvirtio__driver__api.md#aeffc9d53ed7bca3ffd7467d3bcbfaf65))(

46 const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_queues, [virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4) cb,

47 void \*opaque

48 );

[ 49](structvirtio__driver__api.md#a1f9e9ce08443a6ea748ed52bc457bce4) void (\*[finalize\_init](structvirtio__driver__api.md#a1f9e9ce08443a6ea748ed52bc457bce4))(const struct [device](structdevice.md) \*dev);

50};

51

[ 59](group__virtio__interface.md#ga4c1e58e5e34cb40f0a420a52767bff27)static inline struct [virtq](structvirtq.md) \*[virtio\_get\_virtqueue](group__virtio__interface.md#ga4c1e58e5e34cb40f0a420a52767bff27)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx)

60{

61 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

62

63 return api->[get\_virtqueue](structvirtio__driver__api.md#a49fb281829e12fc226e6e2e3cdf47b36)(dev, queue\_idx);

64}

65

[ 76](group__virtio__interface.md#gada51c40981fcdf232b571e1a11dc3cee)static inline void [virtio\_notify\_virtqueue](group__virtio__interface.md#gada51c40981fcdf232b571e1a11dc3cee)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) queue\_idx)

77{

78 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

79

80 api->[notify\_virtqueue](structvirtio__driver__api.md#a22eb11370ec5ea6a0f91334ae1ccff02)(dev, queue\_idx);

81}

82

[ 89](group__virtio__interface.md#ga24987fd9a7603824baed470e4b0ef4d0)static inline void \*[virtio\_get\_device\_specific\_config](group__virtio__interface.md#ga24987fd9a7603824baed470e4b0ef4d0)(const struct [device](structdevice.md) \*dev)

90{

91 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

92

93 return api->[get\_device\_specific\_config](structvirtio__driver__api.md#a7add58b2a488e662443d99b5ef12aace)(dev);

94}

95

[ 103](group__virtio__interface.md#ga55be5a1c2dc457bb1d44b0c302bfb7a8)static inline bool [virtio\_read\_device\_feature\_bit](group__virtio__interface.md#ga55be5a1c2dc457bb1d44b0c302bfb7a8)(const struct [device](structdevice.md) \*dev, int bit)

104{

105 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

106

107 return api->[read\_device\_feature\_bit](structvirtio__driver__api.md#a6f324b95d6edcd044bf44734ec6897b9)(dev, bit);

108}

109

[ 118](group__virtio__interface.md#gab920f8dfee1139585f6af6b22c340912)static inline int [virtio\_write\_driver\_feature\_bit](group__virtio__interface.md#gab920f8dfee1139585f6af6b22c340912)(const struct [device](structdevice.md) \*dev, int bit, bool value)

119{

120 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

121

122 return api->[write\_driver\_feature\_bit](structvirtio__driver__api.md#af6683e8641684e1cc206d1fde6bdb727)(dev, bit, value);

123}

124

[ 131](group__virtio__interface.md#ga7d29735da898548661844356fef966e9)static inline int [virtio\_commit\_feature\_bits](group__virtio__interface.md#ga7d29735da898548661844356fef966e9)(const struct [device](structdevice.md) \*dev)

132{

133 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

134

135 return api->[commit\_feature\_bits](structvirtio__driver__api.md#a8f39c335de27446a54ca2bea8d822546)(dev);

136}

137

[ 147](group__virtio__interface.md#gaf8fde0107ed6da7eb621f334f478666e)static inline int [virtio\_init\_virtqueues](group__virtio__interface.md#gaf8fde0107ed6da7eb621f334f478666e)(

148 const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_queues, [virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4) cb, void \*opaque)

149{

150 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

151

152 return api->[init\_virtqueues](structvirtio__driver__api.md#aeffc9d53ed7bca3ffd7467d3bcbfaf65)(dev, num\_queues, cb, opaque);

153}

154

[ 160](structvirtio__driver__api.md#a49fb281829e12fc226e6e2e3cdf47b36)static inline void [virtio\_finalize\_init](group__virtio__interface.md#ga3ce7e3833b19210d47e563995c39087d)(const struct [device](structdevice.md) \*dev)

161{

162 const struct [virtio\_driver\_api](structvirtio__driver__api.md) \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

163

164 api->[finalize\_init](structvirtio__driver__api.md#a1f9e9ce08443a6ea748ed52bc457bce4)(dev);

165}

166

170

171#ifdef \_\_cplusplus

172}

173#endif

174

175#endif /\* ZEPHYR\_VIRTIO\_VIRTIO\_H\_ \*/

[device.h](device_8h.md)

[virtio\_get\_device\_specific\_config](group__virtio__interface.md#ga24987fd9a7603824baed470e4b0ef4d0)

static void \* virtio\_get\_device\_specific\_config(const struct device \*dev)

Returns device specific config.

**Definition** virtio.h:89

[virtio\_finalize\_init](group__virtio__interface.md#ga3ce7e3833b19210d47e563995c39087d)

static void virtio\_finalize\_init(const struct device \*dev)

Finalizes initialization of the virtio device.

**Definition** virtio.h:160

[virtio\_get\_virtqueue](group__virtio__interface.md#ga4c1e58e5e34cb40f0a420a52767bff27)

static struct virtq \* virtio\_get\_virtqueue(const struct device \*dev, uint16\_t queue\_idx)

Returns virtqueue at given idx.

**Definition** virtio.h:59

[virtio\_read\_device\_feature\_bit](group__virtio__interface.md#ga55be5a1c2dc457bb1d44b0c302bfb7a8)

static bool virtio\_read\_device\_feature\_bit(const struct device \*dev, int bit)

Returns feature bit offered by virtio device.

**Definition** virtio.h:103

[virtio\_commit\_feature\_bits](group__virtio__interface.md#ga7d29735da898548661844356fef966e9)

static int virtio\_commit\_feature\_bits(const struct device \*dev)

Commits feature bits.

**Definition** virtio.h:131

[virtio\_write\_driver\_feature\_bit](group__virtio__interface.md#gab920f8dfee1139585f6af6b22c340912)

static int virtio\_write\_driver\_feature\_bit(const struct device \*dev, int bit, bool value)

Sets feature bit.

**Definition** virtio.h:118

[virtio\_enumerate\_queues](group__virtio__interface.md#gac66779305009c3896eff113f680c29c4)

uint16\_t(\* virtio\_enumerate\_queues)(uint16\_t queue\_idx, uint16\_t max\_queue\_size, void \*opaque)

Callback used during virtqueue enumeration.

**Definition** virtio.h:31

[virtio\_notify\_virtqueue](group__virtio__interface.md#gada51c40981fcdf232b571e1a11dc3cee)

static void virtio\_notify\_virtqueue(const struct device \*dev, uint16\_t queue\_idx)

Notifies virtqueue.

**Definition** virtio.h:76

[virtio\_init\_virtqueues](group__virtio__interface.md#gaf8fde0107ed6da7eb621f334f478666e)

static int virtio\_init\_virtqueues(const struct device \*dev, uint16\_t num\_queues, virtio\_enumerate\_queues cb, void \*opaque)

Initializes virtqueues.

**Definition** virtio.h:147

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[virtio\_driver\_api](structvirtio__driver__api.md)

Virtio api structure.

**Definition** virtio.h:38

[virtio\_driver\_api::finalize\_init](structvirtio__driver__api.md#a1f9e9ce08443a6ea748ed52bc457bce4)

void(\* finalize\_init)(const struct device \*dev)

**Definition** virtio.h:49

[virtio\_driver\_api::notify\_virtqueue](structvirtio__driver__api.md#a22eb11370ec5ea6a0f91334ae1ccff02)

void(\* notify\_virtqueue)(const struct device \*dev, uint16\_t queue\_idx)

**Definition** virtio.h:40

[virtio\_driver\_api::get\_virtqueue](structvirtio__driver__api.md#a49fb281829e12fc226e6e2e3cdf47b36)

struct virtq \*(\* get\_virtqueue)(const struct device \*dev, uint16\_t queue\_idx)

**Definition** virtio.h:39

[virtio\_driver\_api::read\_device\_feature\_bit](structvirtio__driver__api.md#a6f324b95d6edcd044bf44734ec6897b9)

bool(\* read\_device\_feature\_bit)(const struct device \*dev, int bit)

**Definition** virtio.h:42

[virtio\_driver\_api::get\_device\_specific\_config](structvirtio__driver__api.md#a7add58b2a488e662443d99b5ef12aace)

void \*(\* get\_device\_specific\_config)(const struct device \*dev)

**Definition** virtio.h:41

[virtio\_driver\_api::commit\_feature\_bits](structvirtio__driver__api.md#a8f39c335de27446a54ca2bea8d822546)

int(\* commit\_feature\_bits)(const struct device \*dev)

**Definition** virtio.h:44

[virtio\_driver\_api::init\_virtqueues](structvirtio__driver__api.md#aeffc9d53ed7bca3ffd7467d3bcbfaf65)

int(\* init\_virtqueues)(const struct device \*dev, uint16\_t num\_queues, virtio\_enumerate\_queues cb, void \*opaque)

**Definition** virtio.h:45

[virtio\_driver\_api::write\_driver\_feature\_bit](structvirtio__driver__api.md#af6683e8641684e1cc206d1fde6bdb727)

int(\* write\_driver\_feature\_bit)(const struct device \*dev, int bit, bool value)

**Definition** virtio.h:43

[virtq](structvirtq.md)

virtqueue

**Definition** virtqueue.h:148

[virtqueue.h](virtqueue_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [virtio.h](virtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
