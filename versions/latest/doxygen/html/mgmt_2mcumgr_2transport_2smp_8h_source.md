---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html
original_path: doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp.h

[Go to the documentation of this file.](mgmt_2mcumgr_2transport_2smp_8h.md)

1/\*

2 \* Copyright Runtime.io 2018. All rights reserved.

3 \* Copyright (c) 2022-2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_MGMT\_SMP\_H\_

9#define ZEPHYR\_INCLUDE\_MGMT\_SMP\_H\_

10

11#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

24struct [smp\_transport](structsmp__transport.md);

25struct zephyr\_smp\_transport;

26struct [net\_buf](structnet__buf.md);

27

[ 37](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155)typedef int (\*[smp\_transport\_out\_fn](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155))(struct [net\_buf](structnet__buf.md) \*nb);

38

[ 52](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) (\*[smp\_transport\_get\_mtu\_fn](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2))(const struct [net\_buf](structnet__buf.md) \*nb);

53

[ 67](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4)typedef int (\*[smp\_transport\_ud\_copy\_fn](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4))(struct [net\_buf](structnet__buf.md) \*dst,

68 const struct [net\_buf](structnet__buf.md) \*src);

69

[ 79](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c)typedef void (\*[smp\_transport\_ud\_free\_fn](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c))(void \*ud);

80

[ 92](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[smp\_transport\_query\_valid\_check\_fn](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089))(struct [net\_buf](structnet__buf.md) \*nb, void \*arg);

93

[ 98](structsmp__transport__api__t.md)struct [smp\_transport\_api\_t](structsmp__transport__api__t.md) {

[ 100](structsmp__transport__api__t.md#aa779d7dcea55385963a0c0054b95f9da) [smp\_transport\_out\_fn](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155) [output](structsmp__transport__api__t.md#aa779d7dcea55385963a0c0054b95f9da);

101

[ 103](structsmp__transport__api__t.md#a798d89289e913d966cbc1b914fe47952) [smp\_transport\_get\_mtu\_fn](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2) [get\_mtu](structsmp__transport__api__t.md#a798d89289e913d966cbc1b914fe47952);

104

[ 106](structsmp__transport__api__t.md#ae3153c9a27123de510e4ee83cc9c0c62) [smp\_transport\_ud\_copy\_fn](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4) [ud\_copy](structsmp__transport__api__t.md#ae3153c9a27123de510e4ee83cc9c0c62);

107

[ 109](structsmp__transport__api__t.md#acc98fb8a8e7e674ec907939831de1809) [smp\_transport\_ud\_free\_fn](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c) [ud\_free](structsmp__transport__api__t.md#acc98fb8a8e7e674ec907939831de1809);

110

[ 112](structsmp__transport__api__t.md#a811fefe5287c7050701705f8db51f16d) [smp\_transport\_query\_valid\_check\_fn](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089) [query\_valid\_check](structsmp__transport__api__t.md#a811fefe5287c7050701705f8db51f16d);

113};

114

[ 118](structsmp__transport.md)struct [smp\_transport](structsmp__transport.md) {

119 /\* Must be the first member. \*/

[ 120](structsmp__transport.md#a2bb0436ae57a1c1d084f3fed1aa16652) struct [k\_work](structk__work.md) [work](structsmp__transport.md#a2bb0436ae57a1c1d084f3fed1aa16652);

121

122 /\* FIFO containing incoming requests to be processed. \*/

[ 123](structsmp__transport.md#a929ff7e97273dd18920ddc8426c6646f) struct [k\_fifo](structk__fifo.md) [fifo](structsmp__transport.md#a929ff7e97273dd18920ddc8426c6646f);

124

125 /\* Function pointers \*/

[ 126](structsmp__transport.md#ab732e7d9574b78635a90ff559306daaa) struct [smp\_transport\_api\_t](structsmp__transport__api__t.md) [functions](structsmp__transport.md#ab732e7d9574b78635a90ff559306daaa);

127

128#ifdef CONFIG\_MCUMGR\_TRANSPORT\_REASSEMBLY

129 /\* Packet reassembly internal data, API access only \*/

130 struct {

131 struct [net\_buf](structnet__buf.md) \*current; /\* net\_buf used for reassembly \*/

132 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) expected; /\* expected bytes to come \*/

133 } \_\_reassembly;

134#endif

135};

136

[ 140](group__mcumgr__transport__smp.md#ga5d886a11df0c49ca18e23e246ab2fab9)enum [smp\_transport\_type](group__mcumgr__transport__smp.md#ga5d886a11df0c49ca18e23e246ab2fab9) {

[ 142](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342) [SMP\_SERIAL\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342) = 0,

[ 144](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe) [SMP\_BLUETOOTH\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe),

[ 146](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43) [SMP\_SHELL\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43),

[ 148](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f) [SMP\_UDP\_IPV4\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f),

[ 150](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7) [SMP\_UDP\_IPV6\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7),

[ 152](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863) [SMP\_USER\_DEFINED\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)

153};

154

[ 158](structsmp__client__transport__entry.md)struct [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) {

[ 159](structsmp__client__transport__entry.md#ad8ebd9f6bc7d322c51e6aecb2e926022) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structsmp__client__transport__entry.md#ad8ebd9f6bc7d322c51e6aecb2e926022);

[ 161](structsmp__client__transport__entry.md#aebf774d7d0fe4eebe2e230a3680e0acf) struct [smp\_transport](structsmp__transport.md) \*[smpt](structsmp__client__transport__entry.md#aebf774d7d0fe4eebe2e230a3680e0acf);

[ 163](structsmp__client__transport__entry.md#a6a8a368d3db1f03b4e6774d4a86123c2) int [smpt\_type](structsmp__client__transport__entry.md#a6a8a368d3db1f03b4e6774d4a86123c2);

164};

165

[ 174](group__mcumgr__transport__smp.md#gaf275034765327b52b900046d71c411ee)int [smp\_transport\_init](group__mcumgr__transport__smp.md#gaf275034765327b52b900046d71c411ee)(struct [smp\_transport](structsmp__transport.md) \*smpt);

175

[ 185](group__mcumgr__transport__smp.md#ga87ccc623b5907d7d65b24ed99bd57ec5)void [smp\_rx\_remove\_invalid](group__mcumgr__transport__smp.md#ga87ccc623b5907d7d65b24ed99bd57ec5)(struct [smp\_transport](structsmp__transport.md) \*zst, void \*arg);

186

[ 192](group__mcumgr__transport__smp.md#ga662f893037193923610de1e8793fd971)void [smp\_rx\_clear](group__mcumgr__transport__smp.md#ga662f893037193923610de1e8793fd971)(struct [smp\_transport](structsmp__transport.md) \*zst);

193

[ 199](group__mcumgr__transport__smp.md#gafb488cd9854b74c8e5802db3c8fe6116)void [smp\_client\_transport\_register](group__mcumgr__transport__smp.md#gafb488cd9854b74c8e5802db3c8fe6116)(struct [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) \*entry);

200

[ 208](group__mcumgr__transport__smp.md#ga67c3481cdc81c20e0c35b4eaa185619e)struct [smp\_transport](structsmp__transport.md) \*[smp\_client\_transport\_get](group__mcumgr__transport__smp.md#ga67c3481cdc81c20e0c35b4eaa185619e)(int smpt\_type);

209

213

214#ifdef \_\_cplusplus

215}

216#endif

217

218#endif

[smp\_transport\_ud\_free\_fn](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c)

void(\* smp\_transport\_ud\_free\_fn)(void \*ud)

SMP free user\_data callback.

**Definition** smp.h:79

[smp\_transport\_get\_mtu\_fn](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2)

uint16\_t(\* smp\_transport\_get\_mtu\_fn)(const struct net\_buf \*nb)

SMP MTU query callback for transport.

**Definition** smp.h:52

[smp\_transport\_out\_fn](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155)

int(\* smp\_transport\_out\_fn)(struct net\_buf \*nb)

SMP transmit callback for transport.

**Definition** smp.h:37

[smp\_transport\_type](group__mcumgr__transport__smp.md#ga5d886a11df0c49ca18e23e246ab2fab9)

smp\_transport\_type

SMP transport type for client registration.

**Definition** smp.h:140

[smp\_rx\_clear](group__mcumgr__transport__smp.md#ga662f893037193923610de1e8793fd971)

void smp\_rx\_clear(struct smp\_transport \*zst)

Used to clear pending queued requests for an SMP transport.

[smp\_client\_transport\_get](group__mcumgr__transport__smp.md#ga67c3481cdc81c20e0c35b4eaa185619e)

struct smp\_transport \* smp\_client\_transport\_get(int smpt\_type)

Discover a registered SMP transport client object.

[smp\_transport\_query\_valid\_check\_fn](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089)

bool(\* smp\_transport\_query\_valid\_check\_fn)(struct net\_buf \*nb, void \*arg)

Function for checking if queued data is still valid.

**Definition** smp.h:92

[smp\_transport\_ud\_copy\_fn](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4)

int(\* smp\_transport\_ud\_copy\_fn)(struct net\_buf \*dst, const struct net\_buf \*src)

SMP copy user\_data callback.

**Definition** smp.h:67

[smp\_rx\_remove\_invalid](group__mcumgr__transport__smp.md#ga87ccc623b5907d7d65b24ed99bd57ec5)

void smp\_rx\_remove\_invalid(struct smp\_transport \*zst, void \*arg)

Used to remove queued requests for an SMP transport that are no longer valid.

[smp\_transport\_init](group__mcumgr__transport__smp.md#gaf275034765327b52b900046d71c411ee)

int smp\_transport\_init(struct smp\_transport \*smpt)

Initializes a Zephyr SMP transport object.

[smp\_client\_transport\_register](group__mcumgr__transport__smp.md#gafb488cd9854b74c8e5802db3c8fe6116)

void smp\_client\_transport\_register(struct smp\_client\_transport\_entry \*entry)

Register a Zephyr SMP transport object for client.

[SMP\_UDP\_IPV6\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7)

@ SMP\_UDP\_IPV6\_TRANSPORT

SMP UDP IPv6.

**Definition** smp.h:150

[SMP\_SHELL\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43)

@ SMP\_SHELL\_TRANSPORT

SMP shell.

**Definition** smp.h:146

[SMP\_BLUETOOTH\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe)

@ SMP\_BLUETOOTH\_TRANSPORT

SMP bluetooth.

**Definition** smp.h:144

[SMP\_USER\_DEFINED\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)

@ SMP\_USER\_DEFINED\_TRANSPORT

SMP user defined type.

**Definition** smp.h:152

[SMP\_SERIAL\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342)

@ SMP\_SERIAL\_TRANSPORT

SMP serial.

**Definition** smp.h:142

[SMP\_UDP\_IPV4\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f)

@ SMP\_UDP\_IPV4\_TRANSPORT

SMP UDP IPv4.

**Definition** smp.h:148

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[smp\_client\_transport\_entry](structsmp__client__transport__entry.md)

SMP Client transport structure.

**Definition** smp.h:158

[smp\_client\_transport\_entry::smpt\_type](structsmp__client__transport__entry.md#a6a8a368d3db1f03b4e6774d4a86123c2)

int smpt\_type

Transport type.

**Definition** smp.h:163

[smp\_client\_transport\_entry::node](structsmp__client__transport__entry.md#ad8ebd9f6bc7d322c51e6aecb2e926022)

sys\_snode\_t node

**Definition** smp.h:159

[smp\_client\_transport\_entry::smpt](structsmp__client__transport__entry.md#aebf774d7d0fe4eebe2e230a3680e0acf)

struct smp\_transport \* smpt

Transport structure pointer.

**Definition** smp.h:161

[smp\_transport\_api\_t](structsmp__transport__api__t.md)

Function pointers of SMP transport functions, if a handler is NULL then it is not supported/implement...

**Definition** smp.h:98

[smp\_transport\_api\_t::get\_mtu](structsmp__transport__api__t.md#a798d89289e913d966cbc1b914fe47952)

smp\_transport\_get\_mtu\_fn get\_mtu

Transport's get-MTU function.

**Definition** smp.h:103

[smp\_transport\_api\_t::query\_valid\_check](structsmp__transport__api__t.md#a811fefe5287c7050701705f8db51f16d)

smp\_transport\_query\_valid\_check\_fn query\_valid\_check

Transport's check function for if a query is valid.

**Definition** smp.h:112

[smp\_transport\_api\_t::output](structsmp__transport__api__t.md#aa779d7dcea55385963a0c0054b95f9da)

smp\_transport\_out\_fn output

Transport's send function.

**Definition** smp.h:100

[smp\_transport\_api\_t::ud\_free](structsmp__transport__api__t.md#acc98fb8a8e7e674ec907939831de1809)

smp\_transport\_ud\_free\_fn ud\_free

Transport buffer user\_data free function.

**Definition** smp.h:109

[smp\_transport\_api\_t::ud\_copy](structsmp__transport__api__t.md#ae3153c9a27123de510e4ee83cc9c0c62)

smp\_transport\_ud\_copy\_fn ud\_copy

Transport buffer user\_data copy function.

**Definition** smp.h:106

[smp\_transport](structsmp__transport.md)

SMP transport object for sending SMP responses.

**Definition** smp.h:118

[smp\_transport::work](structsmp__transport.md#a2bb0436ae57a1c1d084f3fed1aa16652)

struct k\_work work

**Definition** smp.h:120

[smp\_transport::fifo](structsmp__transport.md#a929ff7e97273dd18920ddc8426c6646f)

struct k\_fifo fifo

**Definition** smp.h:123

[smp\_transport::functions](structsmp__transport.md#ab732e7d9574b78635a90ff559306daaa)

struct smp\_transport\_api\_t functions

**Definition** smp.h:126

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
