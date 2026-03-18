---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hwspinlock_8h_source.html
original_path: doxygen/html/hwspinlock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hwspinlock.h

[Go to the documentation of this file.](hwspinlock_8h.md)

1/\*

2 \* Copyright (c) 2023 Sequans Communications

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_HWSPINLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_HWSPINLOCK\_H\_

9

16

17#include <[errno.h](errno_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/sys/util.h](util_8h.md)>

20#include <[zephyr/device.h](device_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

27

32typedef int (\*hwspinlock\_api\_trylock)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

33

38typedef void (\*hwspinlock\_api\_lock)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

39

44typedef void (\*hwspinlock\_api\_unlock)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

45

50typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*hwspinlock\_api\_get\_max\_id)(const struct [device](structdevice.md) \*dev);

51

52\_\_subsystem struct hwspinlock\_driver\_api {

53 hwspinlock\_api\_trylock trylock;

54 hwspinlock\_api\_lock lock;

55 hwspinlock\_api\_unlock unlock;

56 hwspinlock\_api\_get\_max\_id get\_max\_id;

57};

61

[ 74](group__hwspinlock__interface.md#ga7b7efadefb9e0810c462ee38c669ef99)\_\_syscall int [hwspinlock\_trylock](group__hwspinlock__interface.md#ga7b7efadefb9e0810c462ee38c669ef99)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

75

76static inline int z\_impl\_hwspinlock\_trylock(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

77{

78 const struct hwspinlock\_driver\_api \*api =

79 (const struct hwspinlock\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

80

81 if (api->trylock == NULL)

82 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

83

84 return api->trylock(dev, id);

85}

86

[ 96](group__hwspinlock__interface.md#ga5b4edd18441bb51012801e15447e860a)\_\_syscall void [hwspinlock\_lock](group__hwspinlock__interface.md#ga5b4edd18441bb51012801e15447e860a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

97

98static inline void z\_impl\_hwspinlock\_lock(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

99{

100 const struct hwspinlock\_driver\_api \*api =

101 (const struct hwspinlock\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

102

103 if (api->lock != NULL)

104 api->lock(dev, id);

105}

106

[ 116](group__hwspinlock__interface.md#ga997a5bd42875e09c671960be9535bcc9)\_\_syscall void [hwspinlock\_unlock](group__hwspinlock__interface.md#ga997a5bd42875e09c671960be9535bcc9)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

117

118static inline void z\_impl\_hwspinlock\_unlock(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

119{

120 const struct hwspinlock\_driver\_api \*api =

121 (const struct hwspinlock\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

122

123 if (api->unlock != NULL)

124 api->unlock(dev, id);

125}

126

[ 138](group__hwspinlock__interface.md#gaac02b3349210f467641161dffd6dc363)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hwspinlock\_get\_max\_id](group__hwspinlock__interface.md#gaac02b3349210f467641161dffd6dc363)(const struct [device](structdevice.md) \*dev);

139

140static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_hwspinlock\_get\_max\_id(const struct [device](structdevice.md) \*dev)

141{

142 const struct hwspinlock\_driver\_api \*api =

143 (const struct hwspinlock\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

144

145 if (api->get\_max\_id == NULL)

146 return 0;

147

148 return api->get\_max\_id(dev);

149}

150

151#ifdef \_\_cplusplus

152}

153#endif

154

156

157#include <zephyr/syscalls/hwspinlock.h>

158

159#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_HWSPINLOCK\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[hwspinlock\_lock](group__hwspinlock__interface.md#ga5b4edd18441bb51012801e15447e860a)

void hwspinlock\_lock(const struct device \*dev, uint32\_t id)

Lock HW spinlock.

[hwspinlock\_trylock](group__hwspinlock__interface.md#ga7b7efadefb9e0810c462ee38c669ef99)

int hwspinlock\_trylock(const struct device \*dev, uint32\_t id)

Try to lock HW spinlock.

[hwspinlock\_unlock](group__hwspinlock__interface.md#ga997a5bd42875e09c671960be9535bcc9)

void hwspinlock\_unlock(const struct device \*dev, uint32\_t id)

Try to unlock HW spinlock.

[hwspinlock\_get\_max\_id](group__hwspinlock__interface.md#gaac02b3349210f467641161dffd6dc363)

uint32\_t hwspinlock\_get\_max\_id(const struct device \*dev)

Get HW spinlock max ID.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [hwspinlock.h](hwspinlock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
