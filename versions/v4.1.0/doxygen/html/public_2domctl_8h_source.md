---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/public_2domctl_8h_source.html
original_path: doxygen/html/public_2domctl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

domctl.h

[Go to the documentation of this file.](public_2domctl_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

3 \* domctl.h

4 \*

5 \* Domain management operations. For use by node control stack.

6 \*

7 \* Copyright (c) 2002-2003, B Dragovic

8 \* Copyright (c) 2002-2006, K Fraser

9 \*/

10

11#ifndef \_\_XEN\_PUBLIC\_DOMCTL\_H\_\_

12#define \_\_XEN\_PUBLIC\_DOMCTL\_H\_\_

13

14#ifndef CONFIG\_XEN\_DOM0

15#error "domctl operations are intended for use by node control tools only"

16#endif

17

18#include "[xen.h](xen_8h.md)"

19#include "[event\_channel.h](event__channel_8h.md)"

20#include "[grant\_table.h](grant__table_8h.md)"

21#include "[memory.h](public_2memory_8h.md)"

22

[ 23](public_2domctl_8h.md#a1af9bebb704ccbf97d9ec79d3d860f58)#define XEN\_DOMCTL\_INTERFACE\_VERSION 0x00000015

24

25/\*

26 \* NB. xen\_domctl.domain is an IN/OUT parameter for this operation.

27 \* If it is specified as an invalid value (0 or >= DOMID\_FIRST\_RESERVED),

28 \* an id is auto-allocated and returned.

29 \*/

30/\* XEN\_DOMCTL\_createdomain \*/

[ 31](structxen__domctl__createdomain.md)struct [xen\_domctl\_createdomain](structxen__domctl__createdomain.md) {

32 /\* IN parameters \*/

[ 33](structxen__domctl__createdomain.md#a06ffb30e51c2784838fd952407ebb8f9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ssidref](structxen__domctl__createdomain.md#a06ffb30e51c2784838fd952407ebb8f9);

[ 34](structxen__domctl__createdomain.md#adaf41563368b9860936fb65a2877c9da) [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be) [handle](structxen__domctl__createdomain.md#adaf41563368b9860936fb65a2877c9da);

35/\* Is this an HVM guest (as opposed to a PV guest)? \*/

36#define \_XEN\_DOMCTL\_CDF\_hvm 0

[ 37](public_2domctl_8h.md#a260a9fbe6b758ec5db7e45209cd7dafb)#define XEN\_DOMCTL\_CDF\_hvm (1U << \_XEN\_DOMCTL\_CDF\_hvm)

38/\* Use hardware-assisted paging if available? \*/

39#define \_XEN\_DOMCTL\_CDF\_hap 1

[ 40](public_2domctl_8h.md#a0850c8d7219c2ae8b1de1a2fab67886a)#define XEN\_DOMCTL\_CDF\_hap (1U << \_XEN\_DOMCTL\_CDF\_hap)

41/\* Should domain memory integrity be verified by tboot during Sx? \*/

42#define \_XEN\_DOMCTL\_CDF\_s3\_integrity 2

[ 43](public_2domctl_8h.md#a42dd8479fcf148340790bdd3904e421e)#define XEN\_DOMCTL\_CDF\_s3\_integrity (1U << \_XEN\_DOMCTL\_CDF\_s3\_integrity)

44/\* Disable out-of-sync shadow page tables? \*/

45#define \_XEN\_DOMCTL\_CDF\_oos\_off 3

[ 46](public_2domctl_8h.md#a4620d4dbc1f5334d4cf2c30edf3904f3)#define XEN\_DOMCTL\_CDF\_oos\_off (1U << \_XEN\_DOMCTL\_CDF\_oos\_off)

47/\* Is this a xenstore domain? \*/

48#define \_XEN\_DOMCTL\_CDF\_xs\_domain 4

[ 49](public_2domctl_8h.md#aa70feb5d0e5ee56f872fd0e497557b0d)#define XEN\_DOMCTL\_CDF\_xs\_domain (1U << \_XEN\_DOMCTL\_CDF\_xs\_domain)

50/\* Should this domain be permitted to use the IOMMU? \*/

51#define \_XEN\_DOMCTL\_CDF\_iommu 5

[ 52](public_2domctl_8h.md#a5562e6d41cdea2b7bdd4a5b0b7035109)#define XEN\_DOMCTL\_CDF\_iommu (1U << \_XEN\_DOMCTL\_CDF\_iommu)

53#define \_XEN\_DOMCTL\_CDF\_nested\_virt 6

[ 54](public_2domctl_8h.md#aa837725af35d2c855080e4c413904457)#define XEN\_DOMCTL\_CDF\_nested\_virt (1U << \_XEN\_DOMCTL\_CDF\_nested\_virt)

55/\* Should we expose the vPMU to the guest? \*/

[ 56](public_2domctl_8h.md#a7e9c55587080d25fdf1d6fc31030d27f)#define XEN\_DOMCTL\_CDF\_vpmu (1U << 7)

57

58/\* Max XEN\_DOMCTL\_CDF\_\* constant. Used for ABI checking. \*/

[ 59](public_2domctl_8h.md#a7c6f925fdeb64bc84c6e5f18965b4d13)#define XEN\_DOMCTL\_CDF\_MAX XEN\_DOMCTL\_CDF\_vpmu

60

[ 61](structxen__domctl__createdomain.md#a95075979e76ce83d0f6ed6db93441fc9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structxen__domctl__createdomain.md#a95075979e76ce83d0f6ed6db93441fc9);

62

63#define \_XEN\_DOMCTL\_IOMMU\_no\_sharept 0

[ 64](public_2domctl_8h.md#a928664472460bf3656889afe3a381389)#define XEN\_DOMCTL\_IOMMU\_no\_sharep (1U << \_XEN\_DOMCTL\_IOMMU\_no\_sharept)

65

66/\* Max XEN\_DOMCTL\_IOMMU\_\* constant. Used for ABI checking. \*/

[ 67](public_2domctl_8h.md#ab2313d4fcb94c8e6473d67ce9607da48)#define XEN\_DOMCTL\_IOMMU\_MAX XEN\_DOMCTL\_IOMMU\_no\_sharept

68

[ 69](structxen__domctl__createdomain.md#a1b2e3e39c70e95ea46faf8ec10b2fb7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iommu\_opts](structxen__domctl__createdomain.md#a1b2e3e39c70e95ea46faf8ec10b2fb7c);

70

71 /\*

72 \* Various domain limits, which impact the quantity of resources

73 \* (global mapping space, xenheap, etc) a guest may consume. For

74 \* max\_grant\_frames and max\_maptrack\_frames, < 0 means "use the

75 \* default maximum value in the hypervisor".

76 \*/

[ 77](structxen__domctl__createdomain.md#acd79a2c45cdf4d7ff413b385d9709681) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_vcpus](structxen__domctl__createdomain.md#acd79a2c45cdf4d7ff413b385d9709681);

[ 78](structxen__domctl__createdomain.md#a2ce51b652bac61a08190a101a3743b68) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_evtchn\_port](structxen__domctl__createdomain.md#a2ce51b652bac61a08190a101a3743b68);

[ 79](structxen__domctl__createdomain.md#aba5536e3e28cd164779ac6bced9f6eba) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [max\_grant\_frames](structxen__domctl__createdomain.md#aba5536e3e28cd164779ac6bced9f6eba);

[ 80](structxen__domctl__createdomain.md#acde0ef87527498de29d38e885bfb822d) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [max\_maptrack\_frames](structxen__domctl__createdomain.md#acde0ef87527498de29d38e885bfb822d);

81

82/\* Grant version, use low 4 bits. \*/

[ 83](public_2domctl_8h.md#a6f5be8cef355d7bad22785dc29bd4dac)#define XEN\_DOMCTL\_GRANT\_version\_mask 0xf

[ 84](public_2domctl_8h.md#aa38abb4809db00cbe963bcb41d61950a)#define XEN\_DOMCTL\_GRANT\_version(v) ((v) & XEN\_DOMCTL\_GRANT\_version\_mask)

85

[ 86](structxen__domctl__createdomain.md#a6fa7844107a90f97afead3f17ce91c49) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [grant\_opts](structxen__domctl__createdomain.md#a6fa7844107a90f97afead3f17ce91c49);

87

88 /\* Per-vCPU buffer size in bytes. 0 to disable. \*/

[ 89](structxen__domctl__createdomain.md#a6b9bd817c7df997e5f6585868da7d4bd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vmtrace\_size](structxen__domctl__createdomain.md#a6b9bd817c7df997e5f6585868da7d4bd);

90

91 /\* CPU pool to use; specify 0 or a specific existing pool \*/

[ 92](structxen__domctl__createdomain.md#ac2ef8f072975509418de8ef126f2a65a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cpupool\_id](structxen__domctl__createdomain.md#ac2ef8f072975509418de8ef126f2a65a);

93

[ 94](structxen__domctl__createdomain.md#a63186466661618e0f70ac2f2d37f8953) struct xen\_arch\_domainconfig [arch](structxen__domctl__createdomain.md#a63186466661618e0f70ac2f2d37f8953);

95};

96

97/\* XEN\_DOMCTL\_getdomaininfo \*/

[ 98](structxen__domctl__getdomaininfo.md)struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) {

99 /\* OUT variables. \*/

[ 100](structxen__domctl__getdomaininfo.md#a5e7d88b68cadb01f8c07d684a0ad3830) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domain](structxen__domctl__getdomaininfo.md#a5e7d88b68cadb01f8c07d684a0ad3830); /\* Also echoed in domctl.domain \*/

[ 101](structxen__domctl__getdomaininfo.md#a3d95e5632a072051d23f1d55600412c6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pad1](structxen__domctl__getdomaininfo.md#a3d95e5632a072051d23f1d55600412c6);

102/\* Domain is scheduled to die. \*/

103#define \_XEN\_DOMINF\_dying 0

[ 104](public_2domctl_8h.md#afcdfc193f40faf980e2e23d485de4e79)#define XEN\_DOMINF\_dying (1U << \_XEN\_DOMINF\_dying)

105/\* Domain is an HVM guest (as opposed to a PV guest). \*/

106#define \_XEN\_DOMINF\_hvm\_guest 1

[ 107](public_2domctl_8h.md#a140d5075193daeba92f4b83a0c2f1e14)#define XEN\_DOMINF\_hvm\_guest (1U << \_XEN\_DOMINF\_hvm\_guest)

108/\* The guest OS has shut down. \*/

109#define \_XEN\_DOMINF\_shutdown 2

[ 110](public_2domctl_8h.md#af49f7e9e048fafaa4ec004d46919d313)#define XEN\_DOMINF\_shutdown (1U << \_XEN\_DOMINF\_shutdown)

111/\* Currently paused by control software. \*/

112#define \_XEN\_DOMINF\_paused 3

[ 113](public_2domctl_8h.md#a32c611154d6e6bb3c3b5d4ac9cab5e65)#define XEN\_DOMINF\_paused (1U << \_XEN\_DOMINF\_paused)

114/\* Currently blocked pending an event. \*/

115#define \_XEN\_DOMINF\_blocked 4

[ 116](public_2domctl_8h.md#a34e24b31aaadfd78c585a6187fc89187)#define XEN\_DOMINF\_blocked (1U << \_XEN\_DOMINF\_blocked)

117/\* Domain is currently running. \*/

118#define \_XEN\_DOMINF\_running 5

[ 119](public_2domctl_8h.md#a7e0f50072c881ded1670fa4efda493e0)#define XEN\_DOMINF\_running (1U << \_XEN\_DOMINF\_running)

120/\* Being debugged. \*/

121#define \_XEN\_DOMINF\_debugged 6

[ 122](public_2domctl_8h.md#ade451ebb63161b5cdbfab6221cb9c4f0)#define XEN\_DOMINF\_debugged (1U << \_XEN\_DOMINF\_debugged)

123/\* domain is a xenstore domain \*/

124#define \_XEN\_DOMINF\_xs\_domain 7

[ 125](public_2domctl_8h.md#a37e263699b64912d80697a374d127796)#define XEN\_DOMINF\_xs\_domain (1U << \_XEN\_DOMINF\_xs\_domain)

126/\* domain has hardware assisted paging \*/

127#define \_XEN\_DOMINF\_hap 8

[ 128](public_2domctl_8h.md#a919137e7b6b084d368cca8766091754e)#define XEN\_DOMINF\_hap (1U << \_XEN\_DOMINF\_hap)

129/\* XEN\_DOMINF\_shutdown guest-supplied code. \*/

[ 130](public_2domctl_8h.md#a8e242d887ef91743672a2a3ae3bd74f2)#define XEN\_DOMINF\_shutdownmask 255

[ 131](public_2domctl_8h.md#af3cfe05618c9a1bd3dbe48f42e7cea04)#define XEN\_DOMINF\_shutdownshift 16

[ 132](structxen__domctl__getdomaininfo.md#ae65559d31f31c04f77c12a54341eaff7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structxen__domctl__getdomaininfo.md#ae65559d31f31c04f77c12a54341eaff7); /\* XEN\_DOMINF\_\* \*/

[ 133](structxen__domctl__getdomaininfo.md#a1a16010642a6d39c66a6c7f9198e4ed4) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [tot\_pages](structxen__domctl__getdomaininfo.md#a1a16010642a6d39c66a6c7f9198e4ed4);

[ 134](structxen__domctl__getdomaininfo.md#a9bd68dbcd962f6f9e9cb8bd59b61098a) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [max\_pages](structxen__domctl__getdomaininfo.md#a9bd68dbcd962f6f9e9cb8bd59b61098a);

[ 135](structxen__domctl__getdomaininfo.md#a0886d0cc1989df57ca01dd5b5182b864) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [outstanding\_pages](structxen__domctl__getdomaininfo.md#a0886d0cc1989df57ca01dd5b5182b864);

[ 136](structxen__domctl__getdomaininfo.md#a9b174ea0accd536124987c67ff0ebec6) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [shr\_pages](structxen__domctl__getdomaininfo.md#a9b174ea0accd536124987c67ff0ebec6);

[ 137](structxen__domctl__getdomaininfo.md#a9dd6c1d2a3b79cb3f40f471e943a17fe) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [paged\_pages](structxen__domctl__getdomaininfo.md#a9dd6c1d2a3b79cb3f40f471e943a17fe);

[ 138](structxen__domctl__getdomaininfo.md#a454dbc861570f637283e1c5e063f9f9f) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [shared\_info\_frame](structxen__domctl__getdomaininfo.md#a454dbc861570f637283e1c5e063f9f9f); /\* GMFN of shared\_info struct \*/

[ 139](structxen__domctl__getdomaininfo.md#aa9f8baa2443b101cbed57d2779f0b0d3) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [cpu\_time](structxen__domctl__getdomaininfo.md#aa9f8baa2443b101cbed57d2779f0b0d3);

[ 140](structxen__domctl__getdomaininfo.md#a31cfa87a2ef46d2f25b886b0bd05b4d4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nr\_online\_vcpus](structxen__domctl__getdomaininfo.md#a31cfa87a2ef46d2f25b886b0bd05b4d4); /\* Number of VCPUs currently online. \*/

[ 141](public_2domctl_8h.md#a40c471099d055910f5bed2994efec643)#define XEN\_INVALID\_MAX\_VCPU\_ID (~0U) /\* Domain has no vcpus? \*/

[ 142](structxen__domctl__getdomaininfo.md#ad1357c297623c4244d14efbae6d4f0f0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_vcpu\_id](structxen__domctl__getdomaininfo.md#ad1357c297623c4244d14efbae6d4f0f0); /\* Maximum VCPUID in use by this domain. \*/

[ 143](structxen__domctl__getdomaininfo.md#abb8a0270095249a351777b54f747786f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ssidref](structxen__domctl__getdomaininfo.md#abb8a0270095249a351777b54f747786f);

[ 144](structxen__domctl__getdomaininfo.md#aadfc1b75adac22b197228a2107e6e310) [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be) [handle](structxen__domctl__getdomaininfo.md#aadfc1b75adac22b197228a2107e6e310);

[ 145](structxen__domctl__getdomaininfo.md#a13c6ae340f7f8b9b79bb3b62ace156b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cpupool](structxen__domctl__getdomaininfo.md#a13c6ae340f7f8b9b79bb3b62ace156b8);

[ 146](structxen__domctl__getdomaininfo.md#a5c4df1039ec53351693fa880577e39a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gpaddr\_bits](structxen__domctl__getdomaininfo.md#a5c4df1039ec53351693fa880577e39a5); /\* Guest physical address space size. \*/

[ 147](structxen__domctl__getdomaininfo.md#a6f304fc43fc449e21c6fc3591944c1c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pad2](structxen__domctl__getdomaininfo.md#a6f304fc43fc449e21c6fc3591944c1c8)[7];

[ 148](structxen__domctl__getdomaininfo.md#a5b8ed09273407167af2dc9b62da61cd3) struct xen\_arch\_domainconfig [arch\_config](structxen__domctl__getdomaininfo.md#a5b8ed09273407167af2dc9b62da61cd3);

149};

[ 150](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db)typedef struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) [xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db);

[ 151](public_2domctl_8h.md#a4e3858932ea51b98f6594ec863305eaa)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db));

152

153/\*

154 \* Control shadow pagetables operation

155 \*/

156/\* XEN\_DOMCTL\_shadow\_op \*/

157

158/\* Memory allocation accessors. \*/

[ 159](public_2domctl_8h.md#ae4aefb0671418197673fc3055b3e1aa0)#define XEN\_DOMCTL\_SHADOW\_OP\_GET\_ALLOCATION 30

[ 160](public_2domctl_8h.md#ad48421566046507c9773c91e0349e77b)#define XEN\_DOMCTL\_SHADOW\_OP\_SET\_ALLOCATION 31

161

[ 162](structxen__domctl__shadow__op__stats.md)struct [xen\_domctl\_shadow\_op\_stats](structxen__domctl__shadow__op__stats.md) {

[ 163](structxen__domctl__shadow__op__stats.md#a8b9883cbad12554cb22d9d1ca774c851) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fault\_count](structxen__domctl__shadow__op__stats.md#a8b9883cbad12554cb22d9d1ca774c851);

[ 164](structxen__domctl__shadow__op__stats.md#ab632d0fbc7155cd4cc6f84dc848ce3ca) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dirty\_count](structxen__domctl__shadow__op__stats.md#ab632d0fbc7155cd4cc6f84dc848ce3ca);

165};

166

[ 167](structxen__domctl__shadow__op.md)struct [xen\_domctl\_shadow\_op](structxen__domctl__shadow__op.md) {

168 /\* IN variables. \*/

[ 169](structxen__domctl__shadow__op.md#ab0035f740e2518998d4044d0071bb84c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [op](structxen__domctl__shadow__op.md#ab0035f740e2518998d4044d0071bb84c); /\* XEN\_DOMCTL\_SHADOW\_OP\_\* \*/

170

171 /\* OP\_ENABLE: XEN\_DOMCTL\_SHADOW\_ENABLE\_\* \*/

172 /\* OP\_PEAK / OP\_CLEAN: XEN\_DOMCTL\_SHADOW\_LOGDIRTY\_\* \*/

[ 173](structxen__domctl__shadow__op.md#a2cb3ac92aa7da3bb22d9a448226026a9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode](structxen__domctl__shadow__op.md#a2cb3ac92aa7da3bb22d9a448226026a9);

174

175 /\* OP\_GET\_ALLOCATION / OP\_SET\_ALLOCATION \*/

[ 176](structxen__domctl__shadow__op.md#a393981aab9a3c6d22087c7fc93d436c9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mb](structxen__domctl__shadow__op.md#a393981aab9a3c6d22087c7fc93d436c9); /\* Shadow memory allocation in MB \*/

177

178 /\* OP\_PEEK / OP\_CLEAN \*/

[ 179](structxen__domctl__shadow__op.md#a3d42b3ff4d2a97d504ce0fb5b061b7d8) XEN\_GUEST\_HANDLE\_64([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)) [dirty\_bitmap](structxen__domctl__shadow__op.md#a3d42b3ff4d2a97d504ce0fb5b061b7d8);

[ 180](structxen__domctl__shadow__op.md#a5263fc18f88413fc287dbea94e585e01) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [pages](structxen__domctl__shadow__op.md#a5263fc18f88413fc287dbea94e585e01); /\* Size of buffer. Updated with actual size. \*/

[ 181](structxen__domctl__shadow__op.md#a2631c3498d35d5c4293118c5306eadf7) struct [xen\_domctl\_shadow\_op\_stats](structxen__domctl__shadow__op__stats.md) [stats](structxen__domctl__shadow__op.md#a2631c3498d35d5c4293118c5306eadf7);

182};

183

184/\* XEN\_DOMCTL\_max\_mem \*/

[ 185](structxen__domctl__max__mem.md)struct [xen\_domctl\_max\_mem](structxen__domctl__max__mem.md) {

186 /\* IN variables. \*/

[ 187](structxen__domctl__max__mem.md#a011e86e876e2fabdff507bd5947461aa) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [max\_memkb](structxen__domctl__max__mem.md#a011e86e876e2fabdff507bd5947461aa);

188};

189

190/\* XEN\_DOMCTL\_setvcpucontext \*/

191/\* XEN\_DOMCTL\_getvcpucontext \*/

[ 192](structxen__domctl__vcpucontext.md)struct [xen\_domctl\_vcpucontext](structxen__domctl__vcpucontext.md) {

[ 193](structxen__domctl__vcpucontext.md#a65e5f49065fbe974ca8c3dbef373c971) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vcpu](structxen__domctl__vcpucontext.md#a65e5f49065fbe974ca8c3dbef373c971); /\* IN \*/

194

[ 195](structxen__domctl__vcpucontext.md#a31a693279c1556aa8d134f17ac43a4ee) XEN\_GUEST\_HANDLE\_64(vcpu\_guest\_context\_t) [ctxt](structxen__domctl__vcpucontext.md#a31a693279c1556aa8d134f17ac43a4ee); /\* IN/OUT \*/

196};

197

198/\*

199 \* XEN\_DOMCTL\_max\_vcpus:

200 \*

201 \* The parameter passed to XEN\_DOMCTL\_max\_vcpus must match the value passed to

202 \* XEN\_DOMCTL\_createdomain. This hypercall is in the process of being removed

203 \* (once the failure paths in domain\_create() have been improved), but is

204 \* still required in the short term to allocate the vcpus themselves.

205 \*/

[ 206](structxen__domctl__max__vcpus.md)struct [xen\_domctl\_max\_vcpus](structxen__domctl__max__vcpus.md) {

[ 207](structxen__domctl__max__vcpus.md#a5c20bee1c85cf22936f756def24e3317) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max](structxen__domctl__max__vcpus.md#a5c20bee1c85cf22936f756def24e3317); /\* maximum number of vcpus \*/

208};

209

210/\* XEN\_DOMCTL\_scheduler\_op \*/

211/\* Scheduler types. \*/

212/\* #define XEN\_SCHEDULER\_SEDF 4 (Removed) \*/

[ 213](public_2domctl_8h.md#afee5561bd17af9ddba71e01697ee50d3)#define XEN\_SCHEDULER\_CREDIT 5

[ 214](public_2domctl_8h.md#a560830bf6e1c6a96fae85d6788fffc7c)#define XEN\_SCHEDULER\_CREDIT2 6

[ 215](public_2domctl_8h.md#a08dbd46725afbad5fe54879c9d0518c1)#define XEN\_SCHEDULER\_ARINC653 7

[ 216](public_2domctl_8h.md#afaede03296414e2adaeed009bfd4d0e0)#define XEN\_SCHEDULER\_RTDS 8

[ 217](public_2domctl_8h.md#ac0f58da75c220a8afef88585628874f2)#define XEN\_SCHEDULER\_NULL 9

218

[ 219](structxen__domctl__sched__credit.md)struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md) {

[ 220](structxen__domctl__sched__credit.md#a85f8a8b9dc6d9b60c8aee400a9a84e3c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [weight](structxen__domctl__sched__credit.md#a85f8a8b9dc6d9b60c8aee400a9a84e3c);

[ 221](structxen__domctl__sched__credit.md#a3c5a6f1cb3afda055635375cf6178e21) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cap](structxen__domctl__sched__credit.md#a3c5a6f1cb3afda055635375cf6178e21);

222};

223

[ 224](structxen__domctl__sched__credit2.md)struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md) {

[ 225](structxen__domctl__sched__credit2.md#a067b0c2cde4748ae75f712fa4bacc52f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [weight](structxen__domctl__sched__credit2.md#a067b0c2cde4748ae75f712fa4bacc52f);

[ 226](structxen__domctl__sched__credit2.md#acd8e4572edf22d109e8e414364aa68a9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cap](structxen__domctl__sched__credit2.md#acd8e4572edf22d109e8e414364aa68a9);

227};

228

[ 229](structxen__domctl__sched__rtds.md)struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md) {

[ 230](structxen__domctl__sched__rtds.md#a29b481fc9c1cc24677f924c579ecbca7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [period](structxen__domctl__sched__rtds.md#a29b481fc9c1cc24677f924c579ecbca7);

[ 231](structxen__domctl__sched__rtds.md#a38a0822f999f17bd03dcecb43e695e3d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [budget](structxen__domctl__sched__rtds.md#a38a0822f999f17bd03dcecb43e695e3d);

232/\* Can this vCPU execute beyond its reserved amount of time? \*/

233#define \_XEN\_DOMCTL\_SCHEDRT\_extra 0

[ 234](public_2domctl_8h.md#ae765249383b5fc2e83d1474ac49b4fbd)#define XEN\_DOMCTL\_SCHEDRT\_extra (1U<<\_XEN\_DOMCTL\_SCHEDRT\_extra)

[ 235](structxen__domctl__sched__rtds.md#addb5cfbae13dcb4d6993c064ee09dd77) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structxen__domctl__sched__rtds.md#addb5cfbae13dcb4d6993c064ee09dd77);

236};

237

[ 238](structxen__domctl__schedparam__vcpu.md)typedef struct [xen\_domctl\_schedparam\_vcpu](structxen__domctl__schedparam__vcpu.md) {

239 union {

[ 240](structxen__domctl__schedparam__vcpu.md#a17a024fce3c2e1b51e56ddae4928d253) struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md) [credit](structxen__domctl__schedparam__vcpu.md#a17a024fce3c2e1b51e56ddae4928d253);

[ 241](structxen__domctl__schedparam__vcpu.md#a96e8bf39fabec20d86f4caa2a47f8114) struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md) [credit2](structxen__domctl__schedparam__vcpu.md#a96e8bf39fabec20d86f4caa2a47f8114);

[ 242](structxen__domctl__schedparam__vcpu.md#a15fe4501207b8198b5a87591112d9a48) struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md) [rtds](structxen__domctl__schedparam__vcpu.md#a15fe4501207b8198b5a87591112d9a48);

[ 243](structxen__domctl__schedparam__vcpu.md#a0c6818fb83e36a05c2eebad138206cd3) } [u](structxen__domctl__schedparam__vcpu.md#a0c6818fb83e36a05c2eebad138206cd3);

[ 244](structxen__domctl__schedparam__vcpu.md#a063292bc431df3f1677cfd27a3a788f5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vcpuid](structxen__domctl__schedparam__vcpu.md#a063292bc431df3f1677cfd27a3a788f5);

[ 245](public_2domctl_8h.md#adfbd6c6d40e27f06e00d39acd5be271e)} [xen\_domctl\_schedparam\_vcpu\_t](public_2domctl_8h.md#adfbd6c6d40e27f06e00d39acd5be271e);

[ 246](public_2domctl_8h.md#a4bff168adfcb0ee8cc56f22a1b468112)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_domctl\_schedparam\_vcpu\_t](public_2domctl_8h.md#adfbd6c6d40e27f06e00d39acd5be271e));

247

248/\*

249 \* Set or get info?

250 \* For schedulers supporting per-vcpu settings (e.g., RTDS):

251 \* XEN\_DOMCTL\_SCHEDOP\_putinfo sets params for all vcpus;

252 \* XEN\_DOMCTL\_SCHEDOP\_getinfo gets default params;

253 \* XEN\_DOMCTL\_SCHEDOP\_put(get)vcpuinfo sets (gets) params of vcpus;

254 \*

255 \* For schedulers not supporting per-vcpu settings:

256 \* XEN\_DOMCTL\_SCHEDOP\_putinfo sets params for all vcpus;

257 \* XEN\_DOMCTL\_SCHEDOP\_getinfo gets domain-wise params;

258 \* XEN\_DOMCTL\_SCHEDOP\_put(get)vcpuinfo returns error;

259 \*/

[ 260](public_2domctl_8h.md#a82c49a3fe9250e1e9f3cc4d5f5a74dee)#define XEN\_DOMCTL\_SCHEDOP\_putinfo 0

[ 261](public_2domctl_8h.md#a481dbdc86321a9f74ef259fad8d3da08)#define XEN\_DOMCTL\_SCHEDOP\_getinfo 1

[ 262](public_2domctl_8h.md#a6d6e95c97391261ef77dfbccf15de5ba)#define XEN\_DOMCTL\_SCHEDOP\_putvcpuinfo 2

[ 263](public_2domctl_8h.md#ad1db496f608988bae2fe8ef992416d9e)#define XEN\_DOMCTL\_SCHEDOP\_getvcpuinfo 3

[ 264](structxen__domctl__scheduler__op.md)struct [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md) {

[ 265](structxen__domctl__scheduler__op.md#ac6898bc19fb03bce4728a1f682eb5877) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sched\_id](structxen__domctl__scheduler__op.md#ac6898bc19fb03bce4728a1f682eb5877); /\* XEN\_SCHEDULER\_\* \*/

[ 266](structxen__domctl__scheduler__op.md#a535dd489e0c9d75e5f87f71530b51d62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](structxen__domctl__scheduler__op.md#a535dd489e0c9d75e5f87f71530b51d62); /\* XEN\_DOMCTL\_SCHEDOP\_\* \*/

267 /\* IN/OUT \*/

268 union {

[ 269](structxen__domctl__scheduler__op.md#aeac8bec25228d32e9cc2dcc191e30372) struct [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md) [credit](structxen__domctl__scheduler__op.md#aeac8bec25228d32e9cc2dcc191e30372);

[ 270](structxen__domctl__scheduler__op.md#afee50150bdab7f4ade33e080a94f58db) struct [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md) [credit2](structxen__domctl__scheduler__op.md#afee50150bdab7f4ade33e080a94f58db);

[ 271](structxen__domctl__scheduler__op.md#a051aaadadd7a56d0af51f936e8c889e0) struct [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md) [rtds](structxen__domctl__scheduler__op.md#a051aaadadd7a56d0af51f936e8c889e0);

272 struct {

[ 273](structxen__domctl__scheduler__op.md#a5b09041b6658123c57952356b985daf9) XEN\_GUEST\_HANDLE\_64([xen\_domctl\_schedparam\_vcpu\_t](public_2domctl_8h.md#adfbd6c6d40e27f06e00d39acd5be271e)) [vcpus](structxen__domctl__scheduler__op.md#a5b09041b6658123c57952356b985daf9);

274 /\*

275 \* IN: Number of elements in vcpus array.

276 \* OUT: Number of processed elements of vcpus array.

277 \*/

[ 278](structxen__domctl__scheduler__op.md#ac761b945a1e0f4331f547ea3a8ef44d9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nr\_vcpus](structxen__domctl__scheduler__op.md#ac761b945a1e0f4331f547ea3a8ef44d9);

[ 279](structxen__domctl__scheduler__op.md#accc76316cedabc895ea519d567d29f74) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [padding](structxen__domctl__scheduler__op.md#accc76316cedabc895ea519d567d29f74);

[ 280](structxen__domctl__scheduler__op.md#a1865ada180f42b79c77d6cb2d3b66ddc) } [v](structxen__domctl__scheduler__op.md#a1865ada180f42b79c77d6cb2d3b66ddc);

[ 281](structxen__domctl__scheduler__op.md#a9fd7a528fb9673c55e6eb34fa939c9be) } [u](structxen__domctl__scheduler__op.md#a9fd7a528fb9673c55e6eb34fa939c9be);

282};

283

284/\* XEN\_DOMCTL\_iomem\_permission \*/

[ 285](structxen__domctl__iomem__permission.md)struct [xen\_domctl\_iomem\_permission](structxen__domctl__iomem__permission.md) {

[ 286](structxen__domctl__iomem__permission.md#aa7a1361b038618eaa56c23953824cfcc) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [first\_mfn](structxen__domctl__iomem__permission.md#aa7a1361b038618eaa56c23953824cfcc);/\* first page (physical page number) in range \*/

[ 287](structxen__domctl__iomem__permission.md#a655d4bae8e15474eda33c712c784aebf) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [nr\_mfns](structxen__domctl__iomem__permission.md#a655d4bae8e15474eda33c712c784aebf); /\* number of pages in range (>0) \*/

[ 288](structxen__domctl__iomem__permission.md#a6349bda6c7f561fe5d58038b5c0cadeb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [allow\_access](structxen__domctl__iomem__permission.md#a6349bda6c7f561fe5d58038b5c0cadeb); /\* allow (!0) or deny (0) access to range? \*/

289};

290

291/\* XEN\_DOMCTL\_set\_address\_size \*/

292/\* XEN\_DOMCTL\_get\_address\_size \*/

[ 293](structxen__domctl__address__size.md)struct [xen\_domctl\_address\_size](structxen__domctl__address__size.md) {

[ 294](structxen__domctl__address__size.md#adb707a7de2668b577df5fa0d7dd56e94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structxen__domctl__address__size.md#adb707a7de2668b577df5fa0d7dd56e94);

295};

296

297/\* Assign a device to a guest. Sets up IOMMU structures. \*/

298/\* XEN\_DOMCTL\_assign\_device \*/

299/\*

300 \* XEN\_DOMCTL\_test\_assign\_device: Pass DOMID\_INVALID to find out whether the

301 \* given device is assigned to any DomU at all. Pass a specific domain ID to

302 \* find out whether the given device can be assigned to that domain.

303 \*/

304/\*

305 \* XEN\_DOMCTL\_deassign\_device: The behavior of this DOMCTL differs

306 \* between the different type of device:

307 \* - PCI device (XEN\_DOMCTL\_DEV\_PCI) will be reassigned to DOM0

308 \* - DT device (XEN\_DOMCTL\_DEV\_DT) will left unassigned. DOM0

309 \* will have to call XEN\_DOMCTL\_assign\_device in order to use the

310 \* device.

311 \*/

[ 312](public_2domctl_8h.md#a1399012c484a27f9ada6f35688d569d6)#define XEN\_DOMCTL\_DEV\_PCI 0

[ 313](public_2domctl_8h.md#ac6ed84f27459969a769f558297cee32d)#define XEN\_DOMCTL\_DEV\_DT 1

[ 314](structxen__domctl__assign__device.md)struct [xen\_domctl\_assign\_device](structxen__domctl__assign__device.md) {

315 /\* IN \*/

[ 316](structxen__domctl__assign__device.md#afd889f5732c896690b4dd13a763d4fb2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dev](structxen__domctl__assign__device.md#afd889f5732c896690b4dd13a763d4fb2); /\* XEN\_DOMCTL\_DEV\_\* \*/

[ 317](structxen__domctl__assign__device.md#a306ada0659d7ef8434773efd8cdb594e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structxen__domctl__assign__device.md#a306ada0659d7ef8434773efd8cdb594e);

[ 318](public_2domctl_8h.md#ab297d1aaab40b76132199166663b305b)#define XEN\_DOMCTL\_DEV\_RDM\_RELAXED 1 /\* assign only \*/

319 union {

320 struct {

[ 321](structxen__domctl__assign__device.md#a87fea9d75ecd8d4c161550fd5a28105a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [machine\_sbdf](structxen__domctl__assign__device.md#a87fea9d75ecd8d4c161550fd5a28105a); /\* machine PCI ID of assigned device \*/

[ 322](structxen__domctl__assign__device.md#a1d44b15c0e80e2a0082eccce83af549a) } [pci](structxen__domctl__assign__device.md#a1d44b15c0e80e2a0082eccce83af549a);

323 struct {

[ 324](structxen__domctl__assign__device.md#a10c7d5368170e054c54a8b1cc69c8515) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structxen__domctl__assign__device.md#a10c7d5368170e054c54a8b1cc69c8515); /\* Length of the path \*/

325

[ 326](structxen__domctl__assign__device.md#a2f714f8a4580fa956bb707b6f27fc26f) XEN\_GUEST\_HANDLE\_64(char) [path](structxen__domctl__assign__device.md#a2f714f8a4580fa956bb707b6f27fc26f); /\* path to the device tree node \*/

[ 327](structxen__domctl__assign__device.md#a508c528eacf758fed230d5b17fc9a801) } [dt](structxen__domctl__assign__device.md#a508c528eacf758fed230d5b17fc9a801);

[ 328](structxen__domctl__assign__device.md#a76fde5e4eb3713c1db5dba8924e627a1) } [u](structxen__domctl__assign__device.md#a76fde5e4eb3713c1db5dba8924e627a1);

329};

330

331/\* Pass-through interrupts: bind real irq -> hvm devfn. \*/

332/\* XEN\_DOMCTL\_bind\_pt\_irq \*/

333/\* XEN\_DOMCTL\_unbind\_pt\_irq \*/

[ 334](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07)enum [pt\_irq\_type](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07) {

[ 335](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a243f287f1e887559dad46c487d30dfb7) [PT\_IRQ\_TYPE\_PCI](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a243f287f1e887559dad46c487d30dfb7),

[ 336](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a46633da322cceb9716d497db0a6c7684) [PT\_IRQ\_TYPE\_ISA](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a46633da322cceb9716d497db0a6c7684),

[ 337](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a378f677ce6b550e1f2dd1ce7e4a1cefb) [PT\_IRQ\_TYPE\_MSI](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a378f677ce6b550e1f2dd1ce7e4a1cefb),

[ 338](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07ad8c9df22103d8549d00e3da9c0e3a607) [PT\_IRQ\_TYPE\_MSI\_TRANSLATE](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07ad8c9df22103d8549d00e3da9c0e3a607),

[ 339](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a55314f6bde5f058264c442506b23a818) [PT\_IRQ\_TYPE\_SPI](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a55314f6bde5f058264c442506b23a818), /\* ARM: valid range 32-1019 \*/

340};

[ 341](structxen__domctl__bind__pt__irq.md)struct [xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md) {

[ 342](structxen__domctl__bind__pt__irq.md#ac7e169794a1268053698ea63689fb953) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [machine\_irq](structxen__domctl__bind__pt__irq.md#ac7e169794a1268053698ea63689fb953);

[ 343](structxen__domctl__bind__pt__irq.md#aa1085a60b7c25661b85f7c9524b754d7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [irq\_type](structxen__domctl__bind__pt__irq.md#aa1085a60b7c25661b85f7c9524b754d7); /\* enum pt\_irq\_type \*/

344

345 union {

346 struct {

[ 347](structxen__domctl__bind__pt__irq.md#a53e7af42e7181983b80fcfedd8d709ab) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [isa\_irq](structxen__domctl__bind__pt__irq.md#a53e7af42e7181983b80fcfedd8d709ab);

[ 348](structxen__domctl__bind__pt__irq.md#a50399e43aa64a2294e134cb3db16b6a0) } [isa](structxen__domctl__bind__pt__irq.md#a50399e43aa64a2294e134cb3db16b6a0);

349 struct {

[ 350](structxen__domctl__bind__pt__irq.md#aa73344f449c2f794c1b07d81bc5e2613) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bus](structxen__domctl__bind__pt__irq.md#aa73344f449c2f794c1b07d81bc5e2613);

[ 351](structxen__domctl__bind__pt__irq.md#a7f1d36a2965de0d35e9e86f3825218af) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [device](structxen__domctl__bind__pt__irq.md#a7f1d36a2965de0d35e9e86f3825218af);

[ 352](structxen__domctl__bind__pt__irq.md#aac07dc02b436ae553cd73503baa4372c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [intx](structxen__domctl__bind__pt__irq.md#aac07dc02b436ae553cd73503baa4372c);

[ 353](structxen__domctl__bind__pt__irq.md#afd2db2c0861d6098c7ff94aa094450cc) } [pci](structxen__domctl__bind__pt__irq.md#afd2db2c0861d6098c7ff94aa094450cc);

354 struct {

[ 355](structxen__domctl__bind__pt__irq.md#a571d737fec6ba58131b433643edc8a70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gvec](structxen__domctl__bind__pt__irq.md#a571d737fec6ba58131b433643edc8a70);

[ 356](structxen__domctl__bind__pt__irq.md#abd99cec39f010ebbdf6e5cd0ba3c3676) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gflags](structxen__domctl__bind__pt__irq.md#abd99cec39f010ebbdf6e5cd0ba3c3676);

[ 357](public_2domctl_8h.md#ad94911a72ecc25f10b2a58bd3c1fc091)#define XEN\_DOMCTL\_VMSI\_X86\_DEST\_ID\_MASK 0x0000ff

[ 358](public_2domctl_8h.md#ad337d528c4d9eb777d7dd1a438a98dc8)#define XEN\_DOMCTL\_VMSI\_X86\_RH\_MASK 0x000100

[ 359](public_2domctl_8h.md#a2377d6a66411ba1ca2a314965ef8c7be)#define XEN\_DOMCTL\_VMSI\_X86\_DM\_MASK 0x000200

[ 360](public_2domctl_8h.md#ac8d90b0cceefc508e8a56e59d4fa5ce3)#define XEN\_DOMCTL\_VMSI\_X86\_DELIV\_MASK 0x007000

[ 361](public_2domctl_8h.md#a5ca26c5c2b596e10104119d44b8c6f9a)#define XEN\_DOMCTL\_VMSI\_X86\_TRIG\_MASK 0x008000

[ 362](public_2domctl_8h.md#a81cec14a8ea2e245bc664647e0bf70ab)#define XEN\_DOMCTL\_VMSI\_X86\_UNMASKED 0x010000

363

[ 364](structxen__domctl__bind__pt__irq.md#a4fb5cf50743c77a22b7fe95acef43129) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [gtable](structxen__domctl__bind__pt__irq.md#a4fb5cf50743c77a22b7fe95acef43129);

[ 365](structxen__domctl__bind__pt__irq.md#aa489bd4eedf57431c4fbff4aa80255c8) } [msi](structxen__domctl__bind__pt__irq.md#aa489bd4eedf57431c4fbff4aa80255c8);

366 struct {

[ 367](structxen__domctl__bind__pt__irq.md#a6502c409d05ea42bbf0544602c1c140f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spi](structxen__domctl__bind__pt__irq.md#a6502c409d05ea42bbf0544602c1c140f);

[ 368](structxen__domctl__bind__pt__irq.md#a42e318f72ca9810f5f34b8671ffad088) } [spi](structxen__domctl__bind__pt__irq.md#a6502c409d05ea42bbf0544602c1c140f);

[ 369](structxen__domctl__bind__pt__irq.md#a57facd116b7981a353636a698b821062) } [u](structxen__domctl__bind__pt__irq.md#a57facd116b7981a353636a698b821062);

370};

371

372

373/\* Bind machine I/O address range -> HVM address range. \*/

374/\* XEN\_DOMCTL\_memory\_mapping \*/

375/\* Returns

376 \* - zero success, everything done

377 \* - -E2BIG passed in nr\_mfns value too large for the implementation

378 \* - positive partial success for the first <result> page frames (with

379 \* <result> less than nr\_mfns), requiring re-invocation by the

380 \* caller after updating inputs

381 \* - negative error; other than -E2BIG

382 \*/

[ 383](public_2domctl_8h.md#ab137fda9547e636f2a3685a3b88e9f01)#define DPCI\_ADD\_MAPPING 1

[ 384](public_2domctl_8h.md#a88012336e215a1710a575655f4d2b368)#define DPCI\_REMOVE\_MAPPING 0

[ 385](structxen__domctl__memory__mapping.md)struct [xen\_domctl\_memory\_mapping](structxen__domctl__memory__mapping.md) {

[ 386](structxen__domctl__memory__mapping.md#ab1020a34aa9669586b111bb82de8de02) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [first\_gfn](structxen__domctl__memory__mapping.md#ab1020a34aa9669586b111bb82de8de02); /\* first page (hvm guest phys page) in range \*/

[ 387](structxen__domctl__memory__mapping.md#add620917c805b74e52653c9a7adb10d8) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [first\_mfn](structxen__domctl__memory__mapping.md#add620917c805b74e52653c9a7adb10d8); /\* first page (machine page) in range \*/

[ 388](structxen__domctl__memory__mapping.md#a57331de2d5fedc90b3efe7e0b0632fa1) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [nr\_mfns](structxen__domctl__memory__mapping.md#a57331de2d5fedc90b3efe7e0b0632fa1); /\* number of pages in range (>0) \*/

[ 389](structxen__domctl__memory__mapping.md#aac26188fd1ddf8a841755a078c4e73ab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [add\_mapping](structxen__domctl__memory__mapping.md#aac26188fd1ddf8a841755a078c4e73ab); /\* add or remove mapping \*/

[ 390](structxen__domctl__memory__mapping.md#a73eae6b44886b8ec23da0313cac9300d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [padding](structxen__domctl__memory__mapping.md#a73eae6b44886b8ec23da0313cac9300d); /\* padding for 64-bit aligned structure \*/

391};

392

393/\*

394 \* ARM: Clean and invalidate caches associated with given region of

395 \* guest memory.

396 \*/

[ 397](structxen__domctl__cacheflush.md)struct [xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md) {

398 /\* IN: page range to flush. \*/

[ 399](structxen__domctl__cacheflush.md#a044501ddd5e6982b92ec8bcae8567ec8) [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) [start\_pfn](structxen__domctl__cacheflush.md#a5571dfcebb8906a4497105fc89b837fb), [nr\_pfns](structxen__domctl__cacheflush.md#a044501ddd5e6982b92ec8bcae8567ec8);

400};

401

402/\*

403 \* XEN\_DOMCTL\_get\_paging\_mempool\_size / XEN\_DOMCTL\_set\_paging\_mempool\_size.

404 \*

405 \* Get or set the paging memory pool size. The size is in bytes.

406 \*

407 \* This is a dedicated pool of memory for Xen to use while managing the guest,

408 \* typically containing pagetables. As such, there is an implementation

409 \* specific minimum granularity.

410 \*

411 \* The set operation can fail mid-way through the request (e.g. Xen running

412 \* out of memory, no free memory to reclaim from the pool, etc.).

413 \*/

[ 414](structxen__domctl__paging__mempool.md)struct [xen\_domctl\_paging\_mempool](structxen__domctl__paging__mempool.md) {

[ 415](structxen__domctl__paging__mempool.md#a84e1fed7821bbd82f7a0b7db0f229288) [uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128) [size](structxen__domctl__paging__mempool.md#a84e1fed7821bbd82f7a0b7db0f229288); /\* Size in bytes. \*/

416};

417

[ 418](structxen__domctl.md)struct [xen\_domctl](structxen__domctl.md) {

[ 419](structxen__domctl.md#a833a895a5cd7ccaf368eb93cdcb1256b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](structxen__domctl.md#a833a895a5cd7ccaf368eb93cdcb1256b);

[ 420](public_2domctl_8h.md#abacb0e860ee863ddfeabbdd14b024fc0)#define XEN\_DOMCTL\_createdomain 1

[ 421](public_2domctl_8h.md#a6c9f26d2531a20bffce112302be5196f)#define XEN\_DOMCTL\_destroydomain 2

[ 422](public_2domctl_8h.md#a6fc2629c1e6c4e882609e7e0e8214af7)#define XEN\_DOMCTL\_pausedomain 3

[ 423](public_2domctl_8h.md#a7f759b8eba89d5387e880f8aca7fd357)#define XEN\_DOMCTL\_unpausedomain 4

[ 424](public_2domctl_8h.md#add13342f48d90679c9eb941834278cce)#define XEN\_DOMCTL\_getdomaininfo 5

[ 425](public_2domctl_8h.md#a52f4ddee28622818b0d0ad3a660782e4)#define XEN\_DOMCTL\_setvcpuaffinity 9

[ 426](public_2domctl_8h.md#ab310ee5729b47d317fb381ba4a7765b9)#define XEN\_DOMCTL\_shadow\_op 10

[ 427](public_2domctl_8h.md#abc8af7f11bc93e5e335bda2ba00e770a)#define XEN\_DOMCTL\_max\_mem 11

[ 428](public_2domctl_8h.md#a8fff7d4989f605f73dec55d59b10f5db)#define XEN\_DOMCTL\_setvcpucontext 12

[ 429](public_2domctl_8h.md#af99e2f5c9a5b8a3ccd35a19961c0aa44)#define XEN\_DOMCTL\_getvcpucontext 13

[ 430](public_2domctl_8h.md#abff3d223bd31c6f9b888c1293d7eaeca)#define XEN\_DOMCTL\_getvcpuinfo 14

[ 431](public_2domctl_8h.md#ad32b3ac435a726f6eec3baa03e9d2cc6)#define XEN\_DOMCTL\_max\_vcpus 15

[ 432](public_2domctl_8h.md#a4e16878f8f098d4e5033b3d9c7c4fc66)#define XEN\_DOMCTL\_scheduler\_op 16

[ 433](public_2domctl_8h.md#aab5cf53258ae8b11262e5f1b288537f7)#define XEN\_DOMCTL\_setdomainhandle 17

[ 434](public_2domctl_8h.md#a74047cd87a9608188c8412712f43d2f5)#define XEN\_DOMCTL\_setdebugging 18

[ 435](public_2domctl_8h.md#ab350564800ede51e81bd1efbe9d31433)#define XEN\_DOMCTL\_irq\_permission 19

[ 436](public_2domctl_8h.md#ad3775642e389867857b9c7d33922deaf)#define XEN\_DOMCTL\_iomem\_permission 20

[ 437](public_2domctl_8h.md#ab00adfd7a0a99504c0d74fb9a730535e)#define XEN\_DOMCTL\_ioport\_permission 21

[ 438](public_2domctl_8h.md#a131e1409d1d50a9ba638b194430fd63e)#define XEN\_DOMCTL\_hypercall\_init 22

[ 439](public_2domctl_8h.md#a4d75d1a4982ead6f6b2066d562f3137b)#define XEN\_DOMCTL\_settimeoffset 24

[ 440](public_2domctl_8h.md#acd429b8834dc7284b33a66949c5b7ad0)#define XEN\_DOMCTL\_getvcpuaffinity 25

[ 441](public_2domctl_8h.md#afb2feb24f3113dc5b924aaddf9095c10)#define XEN\_DOMCTL\_real\_mode\_area 26 /\* Obsolete PPC only \*/

[ 442](public_2domctl_8h.md#aca08972618f6a931a3dffd924072e7f0)#define XEN\_DOMCTL\_resumedomain 27

[ 443](public_2domctl_8h.md#a3f3aef1714b0d856bafe713ee9a0a096)#define XEN\_DOMCTL\_sendtrigger 28

[ 444](public_2domctl_8h.md#a25286953a431e6f3172ef9a5f90d18e4)#define XEN\_DOMCTL\_subscribe 29

[ 445](public_2domctl_8h.md#a985b6a69f7cb7da875026aed4552aa6a)#define XEN\_DOMCTL\_gethvmcontext 33

[ 446](public_2domctl_8h.md#a6ea99b9477c9e698af222cea8eef8103)#define XEN\_DOMCTL\_sethvmcontext 34

[ 447](public_2domctl_8h.md#a3401578b5bb89676a5c5c2be96424ad7)#define XEN\_DOMCTL\_set\_address\_size 35

[ 448](public_2domctl_8h.md#a6d97e86f699b92655c72c182b82f1594)#define XEN\_DOMCTL\_get\_address\_size 36

[ 449](public_2domctl_8h.md#a5c896cf694ada3f5571e2011fbeb2cdc)#define XEN\_DOMCTL\_assign\_device 37

[ 450](public_2domctl_8h.md#ac21ffc09b097b8a422680c72242c8019)#define XEN\_DOMCTL\_bind\_pt\_irq 38

[ 451](public_2domctl_8h.md#a087034256c26c23fe8aa430224ed4f5e)#define XEN\_DOMCTL\_memory\_mapping 39

[ 452](public_2domctl_8h.md#a8dc90189fb09c0500ab9831a7304258b)#define XEN\_DOMCTL\_ioport\_mapping 40

[ 453](public_2domctl_8h.md#a0d0a882796436312ecede3dcfd9569f3)#define XEN\_DOMCTL\_set\_ext\_vcpucontext 42

[ 454](public_2domctl_8h.md#a9f0000d1c3ea8784f2d7ac91ee086243)#define XEN\_DOMCTL\_get\_ext\_vcpucontext 43

[ 455](public_2domctl_8h.md#adde0cd9f0afc1545bce1e7efe257479b)#define XEN\_DOMCTL\_set\_opt\_feature 44 /\* Obsolete IA64 only \*/

[ 456](public_2domctl_8h.md#a71b8b60fc4a387b89b482f7c0ba6a24f)#define XEN\_DOMCTL\_test\_assign\_device 45

[ 457](public_2domctl_8h.md#a80d963c7a959b9116b27918bb19cce6b)#define XEN\_DOMCTL\_set\_target 46

[ 458](public_2domctl_8h.md#abc323304cdd608bf785af6421b05f3ee)#define XEN\_DOMCTL\_deassign\_device 47

[ 459](public_2domctl_8h.md#a4a5a18f97beae00c8df5a27e8f58630b)#define XEN\_DOMCTL\_unbind\_pt\_irq 48

[ 460](public_2domctl_8h.md#a93ab2e12792f16f249bec06a31bcde29)#define XEN\_DOMCTL\_get\_device\_group 50

[ 461](public_2domctl_8h.md#ab86f756fc6cfcb537497de0745b75e53)#define XEN\_DOMCTL\_debug\_op 54

[ 462](public_2domctl_8h.md#a72b7300f5aeeba20c7cd3c3aba88e243)#define XEN\_DOMCTL\_gethvmcontext\_partial 55

[ 463](public_2domctl_8h.md#a584b0146d9466c742cde954cf933a35e)#define XEN\_DOMCTL\_vm\_event\_op 56

[ 464](public_2domctl_8h.md#a2144e180680f2862fb3c5c4242ab81d1)#define XEN\_DOMCTL\_mem\_sharing\_op 57

[ 465](public_2domctl_8h.md#ac0c8fe09ca02e3d19ffa2253ec56c36a)#define XEN\_DOMCTL\_gettscinfo 59

[ 466](public_2domctl_8h.md#a68f376046c9512b1ba0d536bf9f4da59)#define XEN\_DOMCTL\_settscinfo 60

[ 467](public_2domctl_8h.md#a9e543639c3b1bae35b54ca0e3ae18fcd)#define XEN\_DOMCTL\_getpageframeinfo3 61

[ 468](public_2domctl_8h.md#a95967323209e42eaf73b092c76c1ed8f)#define XEN\_DOMCTL\_setvcpuextstate 62

[ 469](public_2domctl_8h.md#a20fcaf2b9a50516154f6664ecaba4310)#define XEN\_DOMCTL\_getvcpuextstate 63

[ 470](public_2domctl_8h.md#a8e63ecac1fe62447de02590d81454c76)#define XEN\_DOMCTL\_set\_access\_required 64

[ 471](public_2domctl_8h.md#a64f85814d96a31362cca48e2220047ad)#define XEN\_DOMCTL\_audit\_p2m 65

[ 472](public_2domctl_8h.md#a3f56b7bdb2efe676716dca9a8303b502)#define XEN\_DOMCTL\_set\_virq\_handler 66

[ 473](public_2domctl_8h.md#af50563ae8af88f9de94f87986147f532)#define XEN\_DOMCTL\_set\_broken\_page\_p2m 67

[ 474](public_2domctl_8h.md#a64def50fd26a62692718f14d34ac5056)#define XEN\_DOMCTL\_setnodeaffinity 68

[ 475](public_2domctl_8h.md#afcf17d5e7402b39f32b6c7e21bcb0caa)#define XEN\_DOMCTL\_getnodeaffinity 69

[ 476](public_2domctl_8h.md#a7385beae0c2a015166962952029fafc9)#define XEN\_DOMCTL\_cacheflush 71

[ 477](public_2domctl_8h.md#a154eebe2a910f858f89599f1facda875)#define XEN\_DOMCTL\_get\_vcpu\_msrs 72

[ 478](public_2domctl_8h.md#aa5227f853fed668e20d3c15a76278c1c)#define XEN\_DOMCTL\_set\_vcpu\_msrs 73

[ 479](public_2domctl_8h.md#a33454734fa5e0f67818f763c0284bd0b)#define XEN\_DOMCTL\_setvnumainfo 74

[ 480](public_2domctl_8h.md#ac27bce86ab62c437f2338a96f37a7d48)#define XEN\_DOMCTL\_psr\_cmt\_op 75

[ 481](public_2domctl_8h.md#af006015d33d0097664f6a6020873a82c)#define XEN\_DOMCTL\_monitor\_op 77

[ 482](public_2domctl_8h.md#aad00fc3c420bef96edac0233ee94cd47)#define XEN\_DOMCTL\_psr\_alloc 78

[ 483](public_2domctl_8h.md#aa33f73f1dda376298e235892d8322ba6)#define XEN\_DOMCTL\_soft\_reset 79

[ 484](public_2domctl_8h.md#a850fc8c65f70ad1ad1c9d000f94960ff)#define XEN\_DOMCTL\_vuart\_op 81

[ 485](public_2domctl_8h.md#a36432a25f78249e84192ca30f3b9e9e9)#define XEN\_DOMCTL\_get\_cpu\_policy 82

[ 486](public_2domctl_8h.md#ad537d2de47beed8d6f670a863a3d44d2)#define XEN\_DOMCTL\_set\_cpu\_policy 83

[ 487](public_2domctl_8h.md#a9794dd91afdd16869e3a42b6b3239ecd)#define XEN\_DOMCTL\_vmtrace\_op 84

[ 488](public_2domctl_8h.md#a5cb0f5cd9e12260b996f7bd1df0ca4f0)#define XEN\_DOMCTL\_get\_paging\_mempool\_size 85

[ 489](public_2domctl_8h.md#ae35c3b2ead7567f169e79e786d2b915f)#define XEN\_DOMCTL\_set\_paging\_mempool\_size 86

[ 490](public_2domctl_8h.md#a1202be0a9604f52b50539e5f44af9c39)#define XEN\_DOMCTL\_gdbsx\_guestmemio 1000

[ 491](public_2domctl_8h.md#a398802362361a5fc1496baaa4b2f3664)#define XEN\_DOMCTL\_gdbsx\_pausevcpu 1001

[ 492](public_2domctl_8h.md#a5edc650c7f3956bf6e1dfb441b393a83)#define XEN\_DOMCTL\_gdbsx\_unpausevcpu 1002

[ 493](public_2domctl_8h.md#ac97072e148e5951b57ec0e730e621d29)#define XEN\_DOMCTL\_gdbsx\_domstatus 1003

[ 494](structxen__domctl.md#a5bf335484906644f2c19d74c751ce1c4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interface\_version](structxen__domctl.md#a5bf335484906644f2c19d74c751ce1c4); /\* XEN\_DOMCTL\_INTERFACE\_VERSION \*/

[ 495](structxen__domctl.md#a329ec329aec68c0faa2fa7e5d98c19ba) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domain](structxen__domctl.md#a329ec329aec68c0faa2fa7e5d98c19ba);

496 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_pad[3];

497 union {

[ 498](structxen__domctl.md#a111bee61edfc780955a58994fb3ba060) struct [xen\_domctl\_createdomain](structxen__domctl__createdomain.md) [createdomain](structxen__domctl.md#a111bee61edfc780955a58994fb3ba060);

[ 499](structxen__domctl.md#aa6f45bbd91fb3d4283918f2ed374776d) struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) [getdomaininfo](structxen__domctl.md#aa6f45bbd91fb3d4283918f2ed374776d);

[ 500](structxen__domctl.md#abc809477a658a0eb0a027b3606856c05) struct [xen\_domctl\_max\_mem](structxen__domctl__max__mem.md) [max\_mem](structxen__domctl.md#abc809477a658a0eb0a027b3606856c05);

[ 501](structxen__domctl.md#a8bed0bb93553afca175a4fb897fae394) struct [xen\_domctl\_vcpucontext](structxen__domctl__vcpucontext.md) [vcpucontext](structxen__domctl.md#a8bed0bb93553afca175a4fb897fae394);

[ 502](structxen__domctl.md#ac464216bbb0403acef0e2c47e82b7731) struct [xen\_domctl\_max\_vcpus](structxen__domctl__max__vcpus.md) [max\_vcpus](structxen__domctl.md#ac464216bbb0403acef0e2c47e82b7731);

[ 503](structxen__domctl.md#a412d944e92980210af7faf2686871793) struct [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md) [scheduler\_op](structxen__domctl.md#a412d944e92980210af7faf2686871793);

[ 504](structxen__domctl.md#a41c0d47a8d5764d900d17a93ac1bd0e8) struct [xen\_domctl\_iomem\_permission](structxen__domctl__iomem__permission.md) [iomem\_permission](structxen__domctl.md#a41c0d47a8d5764d900d17a93ac1bd0e8);

[ 505](structxen__domctl.md#acf33e4ac5d83e482ded6d0fbaae75e19) struct [xen\_domctl\_address\_size](structxen__domctl__address__size.md) [address\_size](structxen__domctl.md#acf33e4ac5d83e482ded6d0fbaae75e19);

[ 506](structxen__domctl.md#a2897a77b7aafa6bb91e8390a53027b00) struct [xen\_domctl\_assign\_device](structxen__domctl__assign__device.md) [assign\_device](structxen__domctl.md#a2897a77b7aafa6bb91e8390a53027b00);

[ 507](structxen__domctl.md#a07d169fc24c634686e986b9dc2ed0079) struct [xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md) [bind\_pt\_irq](structxen__domctl.md#a07d169fc24c634686e986b9dc2ed0079);

[ 508](structxen__domctl.md#a1baa090dcccc38080bb15b2643228972) struct [xen\_domctl\_memory\_mapping](structxen__domctl__memory__mapping.md) [memory\_mapping](structxen__domctl.md#a1baa090dcccc38080bb15b2643228972);

[ 509](structxen__domctl.md#a2b552007fb7ccfac707f3450ea1f6ae8) struct [xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md) [cacheflush](structxen__domctl.md#a2b552007fb7ccfac707f3450ea1f6ae8);

[ 510](structxen__domctl.md#a625a6b2e8ec8632898615588dba1090a) struct [xen\_domctl\_paging\_mempool](structxen__domctl__paging__mempool.md) [paging\_mempool](structxen__domctl.md#a625a6b2e8ec8632898615588dba1090a);

[ 511](structxen__domctl.md#aee525828504105fcafbcc01ef08eff18) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pad](structxen__domctl.md#aee525828504105fcafbcc01ef08eff18)[128];

[ 512](structxen__domctl.md#af36b8da93f1e4f58a4f079088ac982ec) } [u](structxen__domctl.md#af36b8da93f1e4f58a4f079088ac982ec);

513};

[ 514](public_2domctl_8h.md#a739ed8d92302fb02b53f4f769d57d83e)typedef struct [xen\_domctl](structxen__domctl.md) [xen\_domctl\_t](public_2domctl_8h.md#a739ed8d92302fb02b53f4f769d57d83e);

[ 515](public_2domctl_8h.md#a0d3b8859d3644f60cb1753391b03face)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([xen\_domctl\_t](public_2domctl_8h.md#a739ed8d92302fb02b53f4f769d57d83e));

516

517#endif /\* \_\_XEN\_PUBLIC\_DOMCTL\_H\_\_ \*/

[xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)

uint64\_t xen\_pfn\_t

**Definition** arch-arm.h:204

[uint64\_aligned\_t](arch-arm_8h.md#ac94f3cee60964f8609932e5042590128)

#define uint64\_aligned\_t

**Definition** arch-arm.h:173

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[event\_channel.h](event__channel_8h.md)

[grant\_table.h](grant__table_8h.md)

[xen\_domctl\_t](public_2domctl_8h.md#a739ed8d92302fb02b53f4f769d57d83e)

struct xen\_domctl xen\_domctl\_t

**Definition** domctl.h:514

[xen\_domctl\_getdomaininfo\_t](public_2domctl_8h.md#a975bbf787336d78a2fe063f5f16766db)

struct xen\_domctl\_getdomaininfo xen\_domctl\_getdomaininfo\_t

**Definition** domctl.h:150

[pt\_irq\_type](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07)

pt\_irq\_type

**Definition** domctl.h:334

[PT\_IRQ\_TYPE\_PCI](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a243f287f1e887559dad46c487d30dfb7)

@ PT\_IRQ\_TYPE\_PCI

**Definition** domctl.h:335

[PT\_IRQ\_TYPE\_MSI](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a378f677ce6b550e1f2dd1ce7e4a1cefb)

@ PT\_IRQ\_TYPE\_MSI

**Definition** domctl.h:337

[PT\_IRQ\_TYPE\_ISA](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a46633da322cceb9716d497db0a6c7684)

@ PT\_IRQ\_TYPE\_ISA

**Definition** domctl.h:336

[PT\_IRQ\_TYPE\_SPI](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07a55314f6bde5f058264c442506b23a818)

@ PT\_IRQ\_TYPE\_SPI

**Definition** domctl.h:339

[PT\_IRQ\_TYPE\_MSI\_TRANSLATE](public_2domctl_8h.md#aa0ba08b170800d6d7723b694525ade07ad8c9df22103d8549d00e3da9c0e3a607)

@ PT\_IRQ\_TYPE\_MSI\_TRANSLATE

**Definition** domctl.h:338

[xen\_domctl\_schedparam\_vcpu\_t](public_2domctl_8h.md#adfbd6c6d40e27f06e00d39acd5be271e)

struct xen\_domctl\_schedparam\_vcpu xen\_domctl\_schedparam\_vcpu\_t

[memory.h](public_2memory_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[xen\_domctl\_address\_size](structxen__domctl__address__size.md)

**Definition** domctl.h:293

[xen\_domctl\_address\_size::size](structxen__domctl__address__size.md#adb707a7de2668b577df5fa0d7dd56e94)

uint32\_t size

**Definition** domctl.h:294

[xen\_domctl\_assign\_device](structxen__domctl__assign__device.md)

**Definition** domctl.h:314

[xen\_domctl\_assign\_device::size](structxen__domctl__assign__device.md#a10c7d5368170e054c54a8b1cc69c8515)

uint32\_t size

**Definition** domctl.h:324

[xen\_domctl\_assign\_device::pci](structxen__domctl__assign__device.md#a1d44b15c0e80e2a0082eccce83af549a)

struct xen\_domctl\_assign\_device::@346070346101205137164003321227267235055010101065::@126306216020237363006234226214302063046257022100 pci

[xen\_domctl\_assign\_device::path](structxen__domctl__assign__device.md#a2f714f8a4580fa956bb707b6f27fc26f)

path

**Definition** domctl.h:326

[xen\_domctl\_assign\_device::flags](structxen__domctl__assign__device.md#a306ada0659d7ef8434773efd8cdb594e)

uint32\_t flags

**Definition** domctl.h:317

[xen\_domctl\_assign\_device::dt](structxen__domctl__assign__device.md#a508c528eacf758fed230d5b17fc9a801)

struct xen\_domctl\_assign\_device::@346070346101205137164003321227267235055010101065::@225251342002247351377134134211157327114300011025 dt

[xen\_domctl\_assign\_device::u](structxen__domctl__assign__device.md#a76fde5e4eb3713c1db5dba8924e627a1)

union xen\_domctl\_assign\_device::@346070346101205137164003321227267235055010101065 u

[xen\_domctl\_assign\_device::machine\_sbdf](structxen__domctl__assign__device.md#a87fea9d75ecd8d4c161550fd5a28105a)

uint32\_t machine\_sbdf

**Definition** domctl.h:321

[xen\_domctl\_assign\_device::dev](structxen__domctl__assign__device.md#afd889f5732c896690b4dd13a763d4fb2)

uint32\_t dev

**Definition** domctl.h:316

[xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md)

**Definition** domctl.h:341

[xen\_domctl\_bind\_pt\_irq::gtable](structxen__domctl__bind__pt__irq.md#a4fb5cf50743c77a22b7fe95acef43129)

uint64\_t gtable

**Definition** domctl.h:364

[xen\_domctl\_bind\_pt\_irq::isa](structxen__domctl__bind__pt__irq.md#a50399e43aa64a2294e134cb3db16b6a0)

struct xen\_domctl\_bind\_pt\_irq::@007272240376006057315255007155165227336027147126::@326164326227067320141270032376355136317070171305 isa

[xen\_domctl\_bind\_pt\_irq::isa\_irq](structxen__domctl__bind__pt__irq.md#a53e7af42e7181983b80fcfedd8d709ab)

uint8\_t isa\_irq

**Definition** domctl.h:347

[xen\_domctl\_bind\_pt\_irq::gvec](structxen__domctl__bind__pt__irq.md#a571d737fec6ba58131b433643edc8a70)

uint8\_t gvec

**Definition** domctl.h:355

[xen\_domctl\_bind\_pt\_irq::u](structxen__domctl__bind__pt__irq.md#a57facd116b7981a353636a698b821062)

union xen\_domctl\_bind\_pt\_irq::@007272240376006057315255007155165227336027147126 u

[xen\_domctl\_bind\_pt\_irq::spi](structxen__domctl__bind__pt__irq.md#a6502c409d05ea42bbf0544602c1c140f)

uint16\_t spi

**Definition** domctl.h:367

[xen\_domctl\_bind\_pt\_irq::device](structxen__domctl__bind__pt__irq.md#a7f1d36a2965de0d35e9e86f3825218af)

uint8\_t device

**Definition** domctl.h:351

[xen\_domctl\_bind\_pt\_irq::irq\_type](structxen__domctl__bind__pt__irq.md#aa1085a60b7c25661b85f7c9524b754d7)

uint32\_t irq\_type

**Definition** domctl.h:343

[xen\_domctl\_bind\_pt\_irq::msi](structxen__domctl__bind__pt__irq.md#aa489bd4eedf57431c4fbff4aa80255c8)

struct xen\_domctl\_bind\_pt\_irq::@007272240376006057315255007155165227336027147126::@335203000171206223004156057337274142062375234221 msi

[xen\_domctl\_bind\_pt\_irq::bus](structxen__domctl__bind__pt__irq.md#aa73344f449c2f794c1b07d81bc5e2613)

uint8\_t bus

**Definition** domctl.h:350

[xen\_domctl\_bind\_pt\_irq::intx](structxen__domctl__bind__pt__irq.md#aac07dc02b436ae553cd73503baa4372c)

uint8\_t intx

**Definition** domctl.h:352

[xen\_domctl\_bind\_pt\_irq::gflags](structxen__domctl__bind__pt__irq.md#abd99cec39f010ebbdf6e5cd0ba3c3676)

uint32\_t gflags

**Definition** domctl.h:356

[xen\_domctl\_bind\_pt\_irq::machine\_irq](structxen__domctl__bind__pt__irq.md#ac7e169794a1268053698ea63689fb953)

uint32\_t machine\_irq

**Definition** domctl.h:342

[xen\_domctl\_bind\_pt\_irq::pci](structxen__domctl__bind__pt__irq.md#afd2db2c0861d6098c7ff94aa094450cc)

struct xen\_domctl\_bind\_pt\_irq::@007272240376006057315255007155165227336027147126::@273140227232217216356207073012252101356335062255 pci

[xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md)

**Definition** domctl.h:397

[xen\_domctl\_cacheflush::nr\_pfns](structxen__domctl__cacheflush.md#a044501ddd5e6982b92ec8bcae8567ec8)

xen\_pfn\_t nr\_pfns

**Definition** domctl.h:399

[xen\_domctl\_cacheflush::start\_pfn](structxen__domctl__cacheflush.md#a5571dfcebb8906a4497105fc89b837fb)

xen\_pfn\_t start\_pfn

**Definition** domctl.h:399

[xen\_domctl\_createdomain](structxen__domctl__createdomain.md)

**Definition** domctl.h:31

[xen\_domctl\_createdomain::ssidref](structxen__domctl__createdomain.md#a06ffb30e51c2784838fd952407ebb8f9)

uint32\_t ssidref

**Definition** domctl.h:33

[xen\_domctl\_createdomain::iommu\_opts](structxen__domctl__createdomain.md#a1b2e3e39c70e95ea46faf8ec10b2fb7c)

uint32\_t iommu\_opts

**Definition** domctl.h:69

[xen\_domctl\_createdomain::max\_evtchn\_port](structxen__domctl__createdomain.md#a2ce51b652bac61a08190a101a3743b68)

uint32\_t max\_evtchn\_port

**Definition** domctl.h:78

[xen\_domctl\_createdomain::arch](structxen__domctl__createdomain.md#a63186466661618e0f70ac2f2d37f8953)

struct xen\_arch\_domainconfig arch

**Definition** domctl.h:94

[xen\_domctl\_createdomain::vmtrace\_size](structxen__domctl__createdomain.md#a6b9bd817c7df997e5f6585868da7d4bd)

uint32\_t vmtrace\_size

**Definition** domctl.h:89

[xen\_domctl\_createdomain::grant\_opts](structxen__domctl__createdomain.md#a6fa7844107a90f97afead3f17ce91c49)

uint32\_t grant\_opts

**Definition** domctl.h:86

[xen\_domctl\_createdomain::flags](structxen__domctl__createdomain.md#a95075979e76ce83d0f6ed6db93441fc9)

uint32\_t flags

**Definition** domctl.h:61

[xen\_domctl\_createdomain::max\_grant\_frames](structxen__domctl__createdomain.md#aba5536e3e28cd164779ac6bced9f6eba)

int32\_t max\_grant\_frames

**Definition** domctl.h:79

[xen\_domctl\_createdomain::cpupool\_id](structxen__domctl__createdomain.md#ac2ef8f072975509418de8ef126f2a65a)

uint32\_t cpupool\_id

**Definition** domctl.h:92

[xen\_domctl\_createdomain::max\_vcpus](structxen__domctl__createdomain.md#acd79a2c45cdf4d7ff413b385d9709681)

uint32\_t max\_vcpus

**Definition** domctl.h:77

[xen\_domctl\_createdomain::max\_maptrack\_frames](structxen__domctl__createdomain.md#acde0ef87527498de29d38e885bfb822d)

int32\_t max\_maptrack\_frames

**Definition** domctl.h:80

[xen\_domctl\_createdomain::handle](structxen__domctl__createdomain.md#adaf41563368b9860936fb65a2877c9da)

xen\_domain\_handle\_t handle

**Definition** domctl.h:34

[xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md)

**Definition** domctl.h:98

[xen\_domctl\_getdomaininfo::outstanding\_pages](structxen__domctl__getdomaininfo.md#a0886d0cc1989df57ca01dd5b5182b864)

uint64\_t outstanding\_pages

**Definition** domctl.h:135

[xen\_domctl\_getdomaininfo::cpupool](structxen__domctl__getdomaininfo.md#a13c6ae340f7f8b9b79bb3b62ace156b8)

uint32\_t cpupool

**Definition** domctl.h:145

[xen\_domctl\_getdomaininfo::tot\_pages](structxen__domctl__getdomaininfo.md#a1a16010642a6d39c66a6c7f9198e4ed4)

uint64\_t tot\_pages

**Definition** domctl.h:133

[xen\_domctl\_getdomaininfo::nr\_online\_vcpus](structxen__domctl__getdomaininfo.md#a31cfa87a2ef46d2f25b886b0bd05b4d4)

uint32\_t nr\_online\_vcpus

**Definition** domctl.h:140

[xen\_domctl\_getdomaininfo::pad1](structxen__domctl__getdomaininfo.md#a3d95e5632a072051d23f1d55600412c6)

uint16\_t pad1

**Definition** domctl.h:101

[xen\_domctl\_getdomaininfo::shared\_info\_frame](structxen__domctl__getdomaininfo.md#a454dbc861570f637283e1c5e063f9f9f)

uint64\_t shared\_info\_frame

**Definition** domctl.h:138

[xen\_domctl\_getdomaininfo::arch\_config](structxen__domctl__getdomaininfo.md#a5b8ed09273407167af2dc9b62da61cd3)

struct xen\_arch\_domainconfig arch\_config

**Definition** domctl.h:148

[xen\_domctl\_getdomaininfo::gpaddr\_bits](structxen__domctl__getdomaininfo.md#a5c4df1039ec53351693fa880577e39a5)

uint8\_t gpaddr\_bits

**Definition** domctl.h:146

[xen\_domctl\_getdomaininfo::domain](structxen__domctl__getdomaininfo.md#a5e7d88b68cadb01f8c07d684a0ad3830)

domid\_t domain

**Definition** domctl.h:100

[xen\_domctl\_getdomaininfo::pad2](structxen__domctl__getdomaininfo.md#a6f304fc43fc449e21c6fc3591944c1c8)

uint8\_t pad2[7]

**Definition** domctl.h:147

[xen\_domctl\_getdomaininfo::shr\_pages](structxen__domctl__getdomaininfo.md#a9b174ea0accd536124987c67ff0ebec6)

uint64\_t shr\_pages

**Definition** domctl.h:136

[xen\_domctl\_getdomaininfo::max\_pages](structxen__domctl__getdomaininfo.md#a9bd68dbcd962f6f9e9cb8bd59b61098a)

uint64\_t max\_pages

**Definition** domctl.h:134

[xen\_domctl\_getdomaininfo::paged\_pages](structxen__domctl__getdomaininfo.md#a9dd6c1d2a3b79cb3f40f471e943a17fe)

uint64\_t paged\_pages

**Definition** domctl.h:137

[xen\_domctl\_getdomaininfo::cpu\_time](structxen__domctl__getdomaininfo.md#aa9f8baa2443b101cbed57d2779f0b0d3)

uint64\_t cpu\_time

**Definition** domctl.h:139

[xen\_domctl\_getdomaininfo::handle](structxen__domctl__getdomaininfo.md#aadfc1b75adac22b197228a2107e6e310)

xen\_domain\_handle\_t handle

**Definition** domctl.h:144

[xen\_domctl\_getdomaininfo::ssidref](structxen__domctl__getdomaininfo.md#abb8a0270095249a351777b54f747786f)

uint32\_t ssidref

**Definition** domctl.h:143

[xen\_domctl\_getdomaininfo::max\_vcpu\_id](structxen__domctl__getdomaininfo.md#ad1357c297623c4244d14efbae6d4f0f0)

uint32\_t max\_vcpu\_id

**Definition** domctl.h:142

[xen\_domctl\_getdomaininfo::flags](structxen__domctl__getdomaininfo.md#ae65559d31f31c04f77c12a54341eaff7)

uint32\_t flags

**Definition** domctl.h:132

[xen\_domctl\_iomem\_permission](structxen__domctl__iomem__permission.md)

**Definition** domctl.h:285

[xen\_domctl\_iomem\_permission::allow\_access](structxen__domctl__iomem__permission.md#a6349bda6c7f561fe5d58038b5c0cadeb)

uint8\_t allow\_access

**Definition** domctl.h:288

[xen\_domctl\_iomem\_permission::nr\_mfns](structxen__domctl__iomem__permission.md#a655d4bae8e15474eda33c712c784aebf)

uint64\_t nr\_mfns

**Definition** domctl.h:287

[xen\_domctl\_iomem\_permission::first\_mfn](structxen__domctl__iomem__permission.md#aa7a1361b038618eaa56c23953824cfcc)

uint64\_t first\_mfn

**Definition** domctl.h:286

[xen\_domctl\_max\_mem](structxen__domctl__max__mem.md)

**Definition** domctl.h:185

[xen\_domctl\_max\_mem::max\_memkb](structxen__domctl__max__mem.md#a011e86e876e2fabdff507bd5947461aa)

uint64\_t max\_memkb

**Definition** domctl.h:187

[xen\_domctl\_max\_vcpus](structxen__domctl__max__vcpus.md)

**Definition** domctl.h:206

[xen\_domctl\_max\_vcpus::max](structxen__domctl__max__vcpus.md#a5c20bee1c85cf22936f756def24e3317)

uint32\_t max

**Definition** domctl.h:207

[xen\_domctl\_memory\_mapping](structxen__domctl__memory__mapping.md)

**Definition** domctl.h:385

[xen\_domctl\_memory\_mapping::nr\_mfns](structxen__domctl__memory__mapping.md#a57331de2d5fedc90b3efe7e0b0632fa1)

uint64\_t nr\_mfns

**Definition** domctl.h:388

[xen\_domctl\_memory\_mapping::padding](structxen__domctl__memory__mapping.md#a73eae6b44886b8ec23da0313cac9300d)

uint32\_t padding

**Definition** domctl.h:390

[xen\_domctl\_memory\_mapping::add\_mapping](structxen__domctl__memory__mapping.md#aac26188fd1ddf8a841755a078c4e73ab)

uint32\_t add\_mapping

**Definition** domctl.h:389

[xen\_domctl\_memory\_mapping::first\_gfn](structxen__domctl__memory__mapping.md#ab1020a34aa9669586b111bb82de8de02)

uint64\_t first\_gfn

**Definition** domctl.h:386

[xen\_domctl\_memory\_mapping::first\_mfn](structxen__domctl__memory__mapping.md#add620917c805b74e52653c9a7adb10d8)

uint64\_t first\_mfn

**Definition** domctl.h:387

[xen\_domctl\_paging\_mempool](structxen__domctl__paging__mempool.md)

**Definition** domctl.h:414

[xen\_domctl\_paging\_mempool::size](structxen__domctl__paging__mempool.md#a84e1fed7821bbd82f7a0b7db0f229288)

uint64\_t size

**Definition** domctl.h:415

[xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md)

**Definition** domctl.h:224

[xen\_domctl\_sched\_credit2::weight](structxen__domctl__sched__credit2.md#a067b0c2cde4748ae75f712fa4bacc52f)

uint16\_t weight

**Definition** domctl.h:225

[xen\_domctl\_sched\_credit2::cap](structxen__domctl__sched__credit2.md#acd8e4572edf22d109e8e414364aa68a9)

uint16\_t cap

**Definition** domctl.h:226

[xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md)

**Definition** domctl.h:219

[xen\_domctl\_sched\_credit::cap](structxen__domctl__sched__credit.md#a3c5a6f1cb3afda055635375cf6178e21)

uint16\_t cap

**Definition** domctl.h:221

[xen\_domctl\_sched\_credit::weight](structxen__domctl__sched__credit.md#a85f8a8b9dc6d9b60c8aee400a9a84e3c)

uint16\_t weight

**Definition** domctl.h:220

[xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md)

**Definition** domctl.h:229

[xen\_domctl\_sched\_rtds::period](structxen__domctl__sched__rtds.md#a29b481fc9c1cc24677f924c579ecbca7)

uint32\_t period

**Definition** domctl.h:230

[xen\_domctl\_sched\_rtds::budget](structxen__domctl__sched__rtds.md#a38a0822f999f17bd03dcecb43e695e3d)

uint32\_t budget

**Definition** domctl.h:231

[xen\_domctl\_sched\_rtds::flags](structxen__domctl__sched__rtds.md#addb5cfbae13dcb4d6993c064ee09dd77)

uint32\_t flags

**Definition** domctl.h:235

[xen\_domctl\_schedparam\_vcpu](structxen__domctl__schedparam__vcpu.md)

**Definition** domctl.h:238

[xen\_domctl\_schedparam\_vcpu::vcpuid](structxen__domctl__schedparam__vcpu.md#a063292bc431df3f1677cfd27a3a788f5)

uint32\_t vcpuid

**Definition** domctl.h:244

[xen\_domctl\_schedparam\_vcpu::u](structxen__domctl__schedparam__vcpu.md#a0c6818fb83e36a05c2eebad138206cd3)

union xen\_domctl\_schedparam\_vcpu::@026172365210266001352130004276145310050375341003 u

[xen\_domctl\_schedparam\_vcpu::rtds](structxen__domctl__schedparam__vcpu.md#a15fe4501207b8198b5a87591112d9a48)

struct xen\_domctl\_sched\_rtds rtds

**Definition** domctl.h:242

[xen\_domctl\_schedparam\_vcpu::credit](structxen__domctl__schedparam__vcpu.md#a17a024fce3c2e1b51e56ddae4928d253)

struct xen\_domctl\_sched\_credit credit

**Definition** domctl.h:240

[xen\_domctl\_schedparam\_vcpu::credit2](structxen__domctl__schedparam__vcpu.md#a96e8bf39fabec20d86f4caa2a47f8114)

struct xen\_domctl\_sched\_credit2 credit2

**Definition** domctl.h:241

[xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md)

**Definition** domctl.h:264

[xen\_domctl\_scheduler\_op::rtds](structxen__domctl__scheduler__op.md#a051aaadadd7a56d0af51f936e8c889e0)

struct xen\_domctl\_sched\_rtds rtds

**Definition** domctl.h:271

[xen\_domctl\_scheduler\_op::v](structxen__domctl__scheduler__op.md#a1865ada180f42b79c77d6cb2d3b66ddc)

struct xen\_domctl\_scheduler\_op::@204215365231351031025307062051006224145075020352::@204304235224270141042144334000147051234133015251 v

[xen\_domctl\_scheduler\_op::cmd](structxen__domctl__scheduler__op.md#a535dd489e0c9d75e5f87f71530b51d62)

uint32\_t cmd

**Definition** domctl.h:266

[xen\_domctl\_scheduler\_op::vcpus](structxen__domctl__scheduler__op.md#a5b09041b6658123c57952356b985daf9)

vcpus

**Definition** domctl.h:273

[xen\_domctl\_scheduler\_op::u](structxen__domctl__scheduler__op.md#a9fd7a528fb9673c55e6eb34fa939c9be)

union xen\_domctl\_scheduler\_op::@204215365231351031025307062051006224145075020352 u

[xen\_domctl\_scheduler\_op::sched\_id](structxen__domctl__scheduler__op.md#ac6898bc19fb03bce4728a1f682eb5877)

uint32\_t sched\_id

**Definition** domctl.h:265

[xen\_domctl\_scheduler\_op::nr\_vcpus](structxen__domctl__scheduler__op.md#ac761b945a1e0f4331f547ea3a8ef44d9)

uint32\_t nr\_vcpus

**Definition** domctl.h:278

[xen\_domctl\_scheduler\_op::padding](structxen__domctl__scheduler__op.md#accc76316cedabc895ea519d567d29f74)

uint32\_t padding

**Definition** domctl.h:279

[xen\_domctl\_scheduler\_op::credit](structxen__domctl__scheduler__op.md#aeac8bec25228d32e9cc2dcc191e30372)

struct xen\_domctl\_sched\_credit credit

**Definition** domctl.h:269

[xen\_domctl\_scheduler\_op::credit2](structxen__domctl__scheduler__op.md#afee50150bdab7f4ade33e080a94f58db)

struct xen\_domctl\_sched\_credit2 credit2

**Definition** domctl.h:270

[xen\_domctl\_shadow\_op\_stats](structxen__domctl__shadow__op__stats.md)

**Definition** domctl.h:162

[xen\_domctl\_shadow\_op\_stats::fault\_count](structxen__domctl__shadow__op__stats.md#a8b9883cbad12554cb22d9d1ca774c851)

uint32\_t fault\_count

**Definition** domctl.h:163

[xen\_domctl\_shadow\_op\_stats::dirty\_count](structxen__domctl__shadow__op__stats.md#ab632d0fbc7155cd4cc6f84dc848ce3ca)

uint32\_t dirty\_count

**Definition** domctl.h:164

[xen\_domctl\_shadow\_op](structxen__domctl__shadow__op.md)

**Definition** domctl.h:167

[xen\_domctl\_shadow\_op::stats](structxen__domctl__shadow__op.md#a2631c3498d35d5c4293118c5306eadf7)

struct xen\_domctl\_shadow\_op\_stats stats

**Definition** domctl.h:181

[xen\_domctl\_shadow\_op::mode](structxen__domctl__shadow__op.md#a2cb3ac92aa7da3bb22d9a448226026a9)

uint32\_t mode

**Definition** domctl.h:173

[xen\_domctl\_shadow\_op::mb](structxen__domctl__shadow__op.md#a393981aab9a3c6d22087c7fc93d436c9)

uint32\_t mb

**Definition** domctl.h:176

[xen\_domctl\_shadow\_op::dirty\_bitmap](structxen__domctl__shadow__op.md#a3d42b3ff4d2a97d504ce0fb5b061b7d8)

dirty\_bitmap

**Definition** domctl.h:179

[xen\_domctl\_shadow\_op::pages](structxen__domctl__shadow__op.md#a5263fc18f88413fc287dbea94e585e01)

uint64\_t pages

**Definition** domctl.h:180

[xen\_domctl\_shadow\_op::op](structxen__domctl__shadow__op.md#ab0035f740e2518998d4044d0071bb84c)

uint32\_t op

**Definition** domctl.h:169

[xen\_domctl\_vcpucontext](structxen__domctl__vcpucontext.md)

**Definition** domctl.h:192

[xen\_domctl\_vcpucontext::ctxt](structxen__domctl__vcpucontext.md#a31a693279c1556aa8d134f17ac43a4ee)

ctxt

**Definition** domctl.h:195

[xen\_domctl\_vcpucontext::vcpu](structxen__domctl__vcpucontext.md#a65e5f49065fbe974ca8c3dbef373c971)

uint32\_t vcpu

**Definition** domctl.h:193

[xen\_domctl](structxen__domctl.md)

**Definition** domctl.h:418

[xen\_domctl::bind\_pt\_irq](structxen__domctl.md#a07d169fc24c634686e986b9dc2ed0079)

struct xen\_domctl\_bind\_pt\_irq bind\_pt\_irq

**Definition** domctl.h:507

[xen\_domctl::createdomain](structxen__domctl.md#a111bee61edfc780955a58994fb3ba060)

struct xen\_domctl\_createdomain createdomain

**Definition** domctl.h:498

[xen\_domctl::memory\_mapping](structxen__domctl.md#a1baa090dcccc38080bb15b2643228972)

struct xen\_domctl\_memory\_mapping memory\_mapping

**Definition** domctl.h:508

[xen\_domctl::assign\_device](structxen__domctl.md#a2897a77b7aafa6bb91e8390a53027b00)

struct xen\_domctl\_assign\_device assign\_device

**Definition** domctl.h:506

[xen\_domctl::cacheflush](structxen__domctl.md#a2b552007fb7ccfac707f3450ea1f6ae8)

struct xen\_domctl\_cacheflush cacheflush

**Definition** domctl.h:509

[xen\_domctl::domain](structxen__domctl.md#a329ec329aec68c0faa2fa7e5d98c19ba)

domid\_t domain

**Definition** domctl.h:495

[xen\_domctl::scheduler\_op](structxen__domctl.md#a412d944e92980210af7faf2686871793)

struct xen\_domctl\_scheduler\_op scheduler\_op

**Definition** domctl.h:503

[xen\_domctl::iomem\_permission](structxen__domctl.md#a41c0d47a8d5764d900d17a93ac1bd0e8)

struct xen\_domctl\_iomem\_permission iomem\_permission

**Definition** domctl.h:504

[xen\_domctl::interface\_version](structxen__domctl.md#a5bf335484906644f2c19d74c751ce1c4)

uint32\_t interface\_version

**Definition** domctl.h:494

[xen\_domctl::paging\_mempool](structxen__domctl.md#a625a6b2e8ec8632898615588dba1090a)

struct xen\_domctl\_paging\_mempool paging\_mempool

**Definition** domctl.h:510

[xen\_domctl::cmd](structxen__domctl.md#a833a895a5cd7ccaf368eb93cdcb1256b)

uint32\_t cmd

**Definition** domctl.h:419

[xen\_domctl::vcpucontext](structxen__domctl.md#a8bed0bb93553afca175a4fb897fae394)

struct xen\_domctl\_vcpucontext vcpucontext

**Definition** domctl.h:501

[xen\_domctl::getdomaininfo](structxen__domctl.md#aa6f45bbd91fb3d4283918f2ed374776d)

struct xen\_domctl\_getdomaininfo getdomaininfo

**Definition** domctl.h:499

[xen\_domctl::max\_mem](structxen__domctl.md#abc809477a658a0eb0a027b3606856c05)

struct xen\_domctl\_max\_mem max\_mem

**Definition** domctl.h:500

[xen\_domctl::max\_vcpus](structxen__domctl.md#ac464216bbb0403acef0e2c47e82b7731)

struct xen\_domctl\_max\_vcpus max\_vcpus

**Definition** domctl.h:502

[xen\_domctl::address\_size](structxen__domctl.md#acf33e4ac5d83e482ded6d0fbaae75e19)

struct xen\_domctl\_address\_size address\_size

**Definition** domctl.h:505

[xen\_domctl::pad](structxen__domctl.md#aee525828504105fcafbcc01ef08eff18)

uint8\_t pad[128]

**Definition** domctl.h:511

[xen\_domctl::u](structxen__domctl.md#af36b8da93f1e4f58a4f079088ac982ec)

union xen\_domctl::@271012046276317112147345010275114207367142241034 u

[xen.h](xen_8h.md)

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

[xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be)

uint8\_t xen\_domain\_handle\_t[16]

**Definition** xen.h:375

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [domctl.h](public_2domctl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
