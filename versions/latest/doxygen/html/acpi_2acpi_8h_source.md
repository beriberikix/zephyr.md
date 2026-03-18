---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/acpi_2acpi_8h_source.html
original_path: doxygen/html/acpi_2acpi_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

acpi.h

[Go to the documentation of this file.](acpi_2acpi_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ACPI\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_ACPI\_H\_

8#include <acpica/source/include/acpi.h>

9#include <[zephyr/drivers/pcie/pcie.h](drivers_2pcie_2pcie_8h.md)>

10

[ 11](acpi_2acpi_8h.md#a5de2990466b70b703d48c6c341e427b3)#define ACPI\_RES\_INVALID ACPI\_RESOURCE\_TYPE\_MAX

12

[ 13](acpi_2acpi_8h.md#a9f534875dab25e2ea48b2676ea8e71b8)#define ACPI\_DRHD\_FLAG\_INCLUDE\_PCI\_ALL BIT(0)

[ 14](acpi_2acpi_8h.md#a92085a7267a8f1569d6d836fc6f8459b)#define ACPI\_DMAR\_FLAG\_INTR\_REMAP BIT(0)

[ 15](acpi_2acpi_8h.md#a346ee226be8400feaf94198db3da4c44)#define ACPI\_DMAR\_FLAG\_X2APIC\_OPT\_OUT BIT(1)

[ 16](acpi_2acpi_8h.md#a695794eaf1ebfa25ed1c0ad0d42105f2)#define ACPI\_DMAR\_FLAG\_DMA\_CTRL\_PLATFORM\_OPT\_IN BIT(2)

17

[ 18](acpi_2acpi_8h.md#a1f8ab630f3c98ceb0c9f59a78b9a24da)#define ACPI\_MMIO\_GET(res) (res)->reg\_base[0].mmio

[ 19](acpi_2acpi_8h.md#a0d45750fe126a6f9641f7f94d843381d)#define ACPI\_IO\_GET(res) (res)->reg\_base[0].port

[ 20](acpi_2acpi_8h.md#abc9aa4017edfc68ac47208e8f758dd60)#define ACPI\_RESOURCE\_SIZE\_GET(res) (res)->reg\_base[0].length

[ 21](acpi_2acpi_8h.md#aa822c0ca234e1b3ea5fc0007c9f490d4)#define ACPI\_RESOURCE\_TYPE\_GET(res) (res)->reg\_base[0].type

22

[ 23](acpi_2acpi_8h.md#af131fc0845a57664d8df8983c074c064)#define ACPI\_MULTI\_MMIO\_GET(res, idx) (res)->reg\_base[idx].mmio

[ 24](acpi_2acpi_8h.md#ad5adfc6540aa9118542970d76d6512bd)#define ACPI\_MULTI\_IO\_GET(res, idx) (res)->reg\_base[idx].port

[ 25](acpi_2acpi_8h.md#ac77fc44c979b87bcb571f77657954d99)#define ACPI\_MULTI\_RESOURCE\_SIZE\_GET(res, idx) (res)->reg\_base[idx].length

[ 26](acpi_2acpi_8h.md#a1e50c8e8f08f6bab0ed12ad97f573b0f)#define ACPI\_MULTI\_RESOURCE\_TYPE\_GET(res, idx) (res)->reg\_base[idx].type

27

[ 28](acpi_2acpi_8h.md#ac174fef6e234ec8452485c199d9de90d)#define ACPI\_RESOURCE\_COUNT\_GET(res) (res)->mmio\_max

29

[ 30](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5b)enum [acpi\_res\_type](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5b) {

[ 32](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f) [ACPI\_RES\_TYPE\_IO](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f),

[ 34](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626) [ACPI\_RES\_TYPE\_MEM](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626),

[ 36](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b) [ACPI\_RES\_TYPE\_UNKNOWN](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b),

37};

38

[ 39](structacpi__dev.md)struct [acpi\_dev](structacpi__dev.md) {

[ 40](structacpi__dev.md#ace9e72f625889d0f84caa17ee6dc8e24) ACPI\_HANDLE [handle](structacpi__dev.md#ace9e72f625889d0f84caa17ee6dc8e24);

[ 41](structacpi__dev.md#a181c2fdd63f316b1d69f3cdc0d924fe2) char \*[path](structacpi__dev.md#a181c2fdd63f316b1d69f3cdc0d924fe2);

[ 42](structacpi__dev.md#a54c5c7c33a425b565b0e1337063a1c1a) ACPI\_RESOURCE \*[res\_lst](structacpi__dev.md#a54c5c7c33a425b565b0e1337063a1c1a);

[ 43](structacpi__dev.md#abc282bce7cdc3de32feb57bc4da790e8) int [res\_type](structacpi__dev.md#abc282bce7cdc3de32feb57bc4da790e8);

[ 44](structacpi__dev.md#a521452067b5751a2a59d156b13ff24f1) ACPI\_DEVICE\_INFO \*[dev\_info](structacpi__dev.md#a521452067b5751a2a59d156b13ff24f1);

45};

46

[ 47](unionacpi__dmar__id.md)union [acpi\_dmar\_id](unionacpi__dmar__id.md) {

48 struct {

[ 49](unionacpi__dmar__id.md#a8fe219b9f4f5871cf14d01079af79614) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [function](unionacpi__dmar__id.md#a8fe219b9f4f5871cf14d01079af79614): 3;

[ 50](unionacpi__dmar__id.md#a03e48f74dae90bbbeba96c4d9f274020) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [device](unionacpi__dmar__id.md#a03e48f74dae90bbbeba96c4d9f274020): 5;

[ 51](unionacpi__dmar__id.md#a3e9194555004762db83d9853594ffca1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bus](unionacpi__dmar__id.md#a3e9194555004762db83d9853594ffca1): 8;

[ 52](unionacpi__dmar__id.md#a0fffa1ca831591b42f732acfd1d86aa6) } [bits](unionacpi__dmar__id.md#a0fffa1ca831591b42f732acfd1d86aa6);

53

[ 54](unionacpi__dmar__id.md#a700729e862c40298e4ebe05b7881f009) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [raw](unionacpi__dmar__id.md#a700729e862c40298e4ebe05b7881f009);

55};

56

[ 57](structacpi__mcfg.md)struct [acpi\_mcfg](structacpi__mcfg.md) {

[ 58](structacpi__mcfg.md#ac3745fb726a32a57992556b9dbaa1365) ACPI\_TABLE\_HEADER [header](structacpi__mcfg.md#ac3745fb726a32a57992556b9dbaa1365);

59 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \_reserved;

[ 60](structacpi__mcfg.md#a8d6bc322dcb14c2892382067275f2426) ACPI\_MCFG\_ALLOCATION [pci\_segs](structacpi__mcfg.md#a8d6bc322dcb14c2892382067275f2426)[];

61} \_\_packed;

62

[ 63](structacpi__irq__resource.md)struct [acpi\_irq\_resource](structacpi__irq__resource.md) {

[ 64](structacpi__irq__resource.md#ac79f9ccd199de7fa52208dee857e7e8f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structacpi__irq__resource.md#ac79f9ccd199de7fa52208dee857e7e8f);

[ 65](structacpi__irq__resource.md#a8d5d5ddb21f52e432862cd0fb16f5f0a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irq\_vector\_max](structacpi__irq__resource.md#a8d5d5ddb21f52e432862cd0fb16f5f0a);

[ 66](structacpi__irq__resource.md#a261bdfee8d5a1137a30bd498e1c5b3c4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[irqs](structacpi__irq__resource.md#a261bdfee8d5a1137a30bd498e1c5b3c4);

67};

68

[ 69](structacpi__reg__base.md)struct [acpi\_reg\_base](structacpi__reg__base.md) {

[ 70](structacpi__reg__base.md#a416f2ff166b33add65eba5e7787c3ef5) enum [acpi\_res\_type](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5b) [type](structacpi__reg__base.md#a416f2ff166b33add65eba5e7787c3ef5);

71 union {

[ 72](structacpi__reg__base.md#ada6ffb943e406068271d56b5a129b717) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [mmio](structacpi__reg__base.md#ada6ffb943e406068271d56b5a129b717);

[ 73](structacpi__reg__base.md#ab845df09e3b4b9734103605ea7c65d1e) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [port](structacpi__reg__base.md#ab845df09e3b4b9734103605ea7c65d1e);

74 };

[ 75](structacpi__reg__base.md#aaca25908e4e16a71627c48208c55d0ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [length](structacpi__reg__base.md#aaca25908e4e16a71627c48208c55d0ef);

76};

77

[ 78](structacpi__mmio__resource.md)struct [acpi\_mmio\_resource](structacpi__mmio__resource.md) {

[ 79](structacpi__mmio__resource.md#a26d31589732a487adbe7b2ab862c4ff4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mmio\_max](structacpi__mmio__resource.md#a26d31589732a487adbe7b2ab862c4ff4);

[ 80](structacpi__mmio__resource.md#ae4ab8715b8f13fa57bc983393c8bd5e6) struct [acpi\_reg\_base](structacpi__reg__base.md) \*[reg\_base](structacpi__mmio__resource.md#ae4ab8715b8f13fa57bc983393c8bd5e6);

81};

82

[ 89](acpi_2acpi_8h.md#a76212438f3a5020919bfde46128f2fb4)#define ACPI\_DT\_HID(node\_id) DT\_PROP(node\_id, acpi\_hid)

90

[ 97](acpi_2acpi_8h.md#a509335d1d6310b109a5047c5a65e1761)#define ACPI\_DT\_UID(node\_id) DT\_PROP\_OR(node\_id, acpi\_uid, NULL)

98

[ 105](acpi_2acpi_8h.md#a9b849938061877cee953fd7257575268)#define ACPI\_DT\_HAS\_HID(node\_id) DT\_NODE\_HAS\_PROP(node\_id, acpi\_hid)

106

[ 113](acpi_2acpi_8h.md#ad91001baf45a0110c85c51b405beaced)#define ACPI\_DT\_HAS\_UID(node\_id) DT\_NODE\_HAS\_PROP(node\_id, acpi\_uid)

114

[ 124](acpi_2acpi_8h.md#ac97acaf39d481f3c3915c763e7f2cdc3)int [acpi\_legacy\_irq\_init](acpi_2acpi_8h.md#ac97acaf39d481f3c3915c763e7f2cdc3)(const char \*hid, const char \*uid);

125

[ 132](acpi_2acpi_8h.md#a139f52f8431a00d34abae1d5a5f31d92)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [acpi\_legacy\_irq\_get](acpi_2acpi_8h.md#a139f52f8431a00d34abae1d5a5f31d92)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf);

133

[ 141](acpi_2acpi_8h.md#ae8d0e92bc9f94d1c70dc893b686c29de)int [acpi\_current\_resource\_get](acpi_2acpi_8h.md#ae8d0e92bc9f94d1c70dc893b686c29de)(char \*dev\_name, ACPI\_RESOURCE \*\*res);

142

[ 150](acpi_2acpi_8h.md#a5787a05051ffb4ccab113cf2e834678d)int [acpi\_possible\_resource\_get](acpi_2acpi_8h.md#a5787a05051ffb4ccab113cf2e834678d)(char \*dev\_name, ACPI\_RESOURCE \*\*res);

151

[ 159](acpi_2acpi_8h.md#a703f435a640e34080a6cf52c2256294e)int [acpi\_current\_resource\_free](acpi_2acpi_8h.md#a703f435a640e34080a6cf52c2256294e)(ACPI\_RESOURCE \*res);

160

[ 168](acpi_2acpi_8h.md#aa5d7b0c25e6e2767c15edbce33971c72)ACPI\_RESOURCE \*[acpi\_resource\_parse](acpi_2acpi_8h.md#aa5d7b0c25e6e2767c15edbce33971c72)(ACPI\_RESOURCE \*res, int res\_type);

169

[ 178](acpi_2acpi_8h.md#a6416a93af8385d3784d205b8811a6a94)struct [acpi\_dev](structacpi__dev.md) \*[acpi\_device\_get](acpi_2acpi_8h.md#a6416a93af8385d3784d205b8811a6a94)(const char \*hid, const char \*uid);

179

[ 186](acpi_2acpi_8h.md#a625d35bab5922b679517fe8d8b0aface)struct [acpi\_dev](structacpi__dev.md) \*[acpi\_device\_by\_index\_get](acpi_2acpi_8h.md#a625d35bab5922b679517fe8d8b0aface)(int index);

187

[ 194](acpi_2acpi_8h.md#a3a0c7a6232c1f1f08ae0be3e5c3fac7a)static inline ACPI\_RESOURCE\_IRQ \*[acpi\_irq\_res\_get](acpi_2acpi_8h.md#a3a0c7a6232c1f1f08ae0be3e5c3fac7a)(ACPI\_RESOURCE \*[res\_lst](structacpi__dev.md#a54c5c7c33a425b565b0e1337063a1c1a))

195{

196 ACPI\_RESOURCE \*res = [acpi\_resource\_parse](acpi_2acpi_8h.md#aa5d7b0c25e6e2767c15edbce33971c72)([res\_lst](structacpi__dev.md#a54c5c7c33a425b565b0e1337063a1c1a), ACPI\_RESOURCE\_TYPE\_IRQ);

197

198 return res ? &res->Data.Irq : NULL;

199}

200

[ 208](acpi_2acpi_8h.md#ab8a0982a3acc857ea059bb617b8b43f7)int [acpi\_device\_irq\_get](acpi_2acpi_8h.md#ab8a0982a3acc857ea059bb617b8b43f7)(struct [acpi\_dev](structacpi__dev.md) \*child\_dev, struct [acpi\_irq\_resource](structacpi__irq__resource.md) \*irq\_res);

209

[ 217](acpi_2acpi_8h.md#a4179d931233431ec61b5e12c1c77931d)int [acpi\_device\_mmio\_get](acpi_2acpi_8h.md#a4179d931233431ec61b5e12c1c77931d)(struct [acpi\_dev](structacpi__dev.md) \*child\_dev, struct [acpi\_mmio\_resource](structacpi__mmio__resource.md) \*mmio\_res);

218

[ 225](acpi_2acpi_8h.md#a44b747b1b7493627a8022c49571b04ff)int [acpi\_device\_type\_get](acpi_2acpi_8h.md#a44b747b1b7493627a8022c49571b04ff)(ACPI\_RESOURCE \*res);

226

[ 234](acpi_2acpi_8h.md#ab6f0b5f0ae6cf1da923051f2e38fa193)void \*[acpi\_table\_get](acpi_2acpi_8h.md#ab6f0b5f0ae6cf1da923051f2e38fa193)(char \*signature, int inst);

235

[ 244](acpi_2acpi_8h.md#abb83809ce252f82f93ea042dfba3fbfd)int [acpi\_madt\_entry\_get](acpi_2acpi_8h.md#abb83809ce252f82f93ea042dfba3fbfd)(int type, ACPI\_SUBTABLE\_HEADER \*\*tables, int \*num\_inst);

245

[ 253](acpi_2acpi_8h.md#a36d899259fe64aea46549e54ebbfbf0a)int [acpi\_dmar\_entry\_get](acpi_2acpi_8h.md#a36d899259fe64aea46549e54ebbfbf0a)(enum AcpiDmarType type, ACPI\_SUBTABLE\_HEADER \*\*tables);

254

[ 265](acpi_2acpi_8h.md#a1d9f2e00bbcc8a0e101091c6d6be4ac5)int [acpi\_drhd\_get](acpi_2acpi_8h.md#a1d9f2e00bbcc8a0e101091c6d6be4ac5)(enum AcpiDmarScopeType scope, ACPI\_DMAR\_DEVICE\_SCOPE \*dev\_scope,

266 union [acpi\_dmar\_id](unionacpi__dmar__id.md) \*dmar\_id, int \*num\_inst, int max\_inst);

267

[ 268](acpi_2acpi_8h.md#af675794f8aa74fb58c7a2c7266f05357)typedef void (\*[dmar\_foreach\_subtable\_func\_t](acpi_2acpi_8h.md#af675794f8aa74fb58c7a2c7266f05357))(ACPI\_DMAR\_HEADER \*subtable, void \*arg);

[ 269](acpi_2acpi_8h.md#a6b294403ca4a5e1c234c42279d201490)typedef void (\*[dmar\_foreach\_devscope\_func\_t](acpi_2acpi_8h.md#a6b294403ca4a5e1c234c42279d201490))(ACPI\_DMAR\_DEVICE\_SCOPE \*devscope, void \*arg);

270

[ 271](acpi_2acpi_8h.md#af62e15025d3442b2db39b34c3e138671)void [acpi\_dmar\_foreach\_subtable](acpi_2acpi_8h.md#af62e15025d3442b2db39b34c3e138671)(ACPI\_TABLE\_DMAR \*dmar, [dmar\_foreach\_subtable\_func\_t](acpi_2acpi_8h.md#af675794f8aa74fb58c7a2c7266f05357) func,

272 void \*arg);

[ 273](acpi_2acpi_8h.md#a77d02fbe12ff3e02368582c489f7c7d5)void [acpi\_dmar\_foreach\_devscope](acpi_2acpi_8h.md#a77d02fbe12ff3e02368582c489f7c7d5)(ACPI\_DMAR\_HARDWARE\_UNIT \*hu,

274 [dmar\_foreach\_devscope\_func\_t](acpi_2acpi_8h.md#a6b294403ca4a5e1c234c42279d201490) func, void \*arg);

275

[ 282](acpi_2acpi_8h.md#a9768a4b3d13edb8456736256ec015e04)int [acpi\_dmar\_ioapic\_get](acpi_2acpi_8h.md#a9768a4b3d13edb8456736256ec015e04)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*ioapic\_id);

283

[ 290](acpi_2acpi_8h.md#a750b6348bfc9f3867b561ff9d7a08b4c)ACPI\_MADT\_LOCAL\_APIC \*[acpi\_local\_apic\_get](acpi_2acpi_8h.md#a750b6348bfc9f3867b561ff9d7a08b4c)(int cpu\_num);

291

[ 300](acpi_2acpi_8h.md#aab272d92004e687bdd2936f648f3f9f9)int [acpi\_invoke\_method](acpi_2acpi_8h.md#aab272d92004e687bdd2936f648f3f9f9)(char \*[path](structacpi__dev.md#a181c2fdd63f316b1d69f3cdc0d924fe2), ACPI\_OBJECT\_LIST \*arg\_list, ACPI\_OBJECT \*ret\_obj);

301

302#endif

[acpi\_legacy\_irq\_get](acpi_2acpi_8h.md#a139f52f8431a00d34abae1d5a5f31d92)

uint32\_t acpi\_legacy\_irq\_get(pcie\_bdf\_t bdf)

Retrieve a legacy interrupt number for a PCI device.

[acpi\_drhd\_get](acpi_2acpi_8h.md#a1d9f2e00bbcc8a0e101091c6d6be4ac5)

int acpi\_drhd\_get(enum AcpiDmarScopeType scope, ACPI\_DMAR\_DEVICE\_SCOPE \*dev\_scope, union acpi\_dmar\_id \*dmar\_id, int \*num\_inst, int max\_inst)

retrieve acpi DRHD info for the given scope.

[acpi\_res\_type](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5b)

acpi\_res\_type

**Definition** acpi.h:30

[ACPI\_RES\_TYPE\_MEM](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626)

@ ACPI\_RES\_TYPE\_MEM

Memory mapped Resource type.

**Definition** acpi.h:34

[ACPI\_RES\_TYPE\_UNKNOWN](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b)

@ ACPI\_RES\_TYPE\_UNKNOWN

Unknown Resource type.

**Definition** acpi.h:36

[ACPI\_RES\_TYPE\_IO](acpi_2acpi_8h.md#a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f)

@ ACPI\_RES\_TYPE\_IO

IO mapped Resource type.

**Definition** acpi.h:32

[acpi\_dmar\_entry\_get](acpi_2acpi_8h.md#a36d899259fe64aea46549e54ebbfbf0a)

int acpi\_dmar\_entry\_get(enum AcpiDmarType type, ACPI\_SUBTABLE\_HEADER \*\*tables)

retrieve DMA remapping structure for the given type.

[acpi\_irq\_res\_get](acpi_2acpi_8h.md#a3a0c7a6232c1f1f08ae0be3e5c3fac7a)

static ACPI\_RESOURCE\_IRQ \* acpi\_irq\_res\_get(ACPI\_RESOURCE \*res\_lst)

Parse resource table for irq info.

**Definition** acpi.h:194

[acpi\_device\_mmio\_get](acpi_2acpi_8h.md#a4179d931233431ec61b5e12c1c77931d)

int acpi\_device\_mmio\_get(struct acpi\_dev \*child\_dev, struct acpi\_mmio\_resource \*mmio\_res)

Parse resource table for MMIO info.

[acpi\_device\_type\_get](acpi_2acpi_8h.md#a44b747b1b7493627a8022c49571b04ff)

int acpi\_device\_type\_get(ACPI\_RESOURCE \*res)

Parse resource table for identify resource type.

[acpi\_possible\_resource\_get](acpi_2acpi_8h.md#a5787a05051ffb4ccab113cf2e834678d)

int acpi\_possible\_resource\_get(char \*dev\_name, ACPI\_RESOURCE \*\*res)

Retrieve possible resource settings of a device.

[acpi\_device\_by\_index\_get](acpi_2acpi_8h.md#a625d35bab5922b679517fe8d8b0aface)

struct acpi\_dev \* acpi\_device\_by\_index\_get(int index)

Retrieve acpi device info from the index.

[acpi\_device\_get](acpi_2acpi_8h.md#a6416a93af8385d3784d205b8811a6a94)

struct acpi\_dev \* acpi\_device\_get(const char \*hid, const char \*uid)

Retrieve ACPI device info for given hardware id and unique id.

[dmar\_foreach\_devscope\_func\_t](acpi_2acpi_8h.md#a6b294403ca4a5e1c234c42279d201490)

void(\* dmar\_foreach\_devscope\_func\_t)(ACPI\_DMAR\_DEVICE\_SCOPE \*devscope, void \*arg)

**Definition** acpi.h:269

[acpi\_current\_resource\_free](acpi_2acpi_8h.md#a703f435a640e34080a6cf52c2256294e)

int acpi\_current\_resource\_free(ACPI\_RESOURCE \*res)

Free current resource list memory which is retrieved by acpi\_current\_resource\_get().

[acpi\_local\_apic\_get](acpi_2acpi_8h.md#a750b6348bfc9f3867b561ff9d7a08b4c)

ACPI\_MADT\_LOCAL\_APIC \* acpi\_local\_apic\_get(int cpu\_num)

Retrieve the 'n'th enabled local apic info.

[acpi\_dmar\_foreach\_devscope](acpi_2acpi_8h.md#a77d02fbe12ff3e02368582c489f7c7d5)

void acpi\_dmar\_foreach\_devscope(ACPI\_DMAR\_HARDWARE\_UNIT \*hu, dmar\_foreach\_devscope\_func\_t func, void \*arg)

[acpi\_dmar\_ioapic\_get](acpi_2acpi_8h.md#a9768a4b3d13edb8456736256ec015e04)

int acpi\_dmar\_ioapic\_get(uint16\_t \*ioapic\_id)

Retrieve IOAPIC id.

[acpi\_resource\_parse](acpi_2acpi_8h.md#aa5d7b0c25e6e2767c15edbce33971c72)

ACPI\_RESOURCE \* acpi\_resource\_parse(ACPI\_RESOURCE \*res, int res\_type)

Parse resource table for a given resource type.

[acpi\_invoke\_method](acpi_2acpi_8h.md#aab272d92004e687bdd2936f648f3f9f9)

int acpi\_invoke\_method(char \*path, ACPI\_OBJECT\_LIST \*arg\_list, ACPI\_OBJECT \*ret\_obj)

invoke an ACPI method and return the result.

[acpi\_table\_get](acpi_2acpi_8h.md#ab6f0b5f0ae6cf1da923051f2e38fa193)

void \* acpi\_table\_get(char \*signature, int inst)

Retrieve acpi table for the given signature.

[acpi\_device\_irq\_get](acpi_2acpi_8h.md#ab8a0982a3acc857ea059bb617b8b43f7)

int acpi\_device\_irq\_get(struct acpi\_dev \*child\_dev, struct acpi\_irq\_resource \*irq\_res)

Parse resource table for irq info.

[acpi\_madt\_entry\_get](acpi_2acpi_8h.md#abb83809ce252f82f93ea042dfba3fbfd)

int acpi\_madt\_entry\_get(int type, ACPI\_SUBTABLE\_HEADER \*\*tables, int \*num\_inst)

retrieve acpi MAD table for the given type.

[acpi\_legacy\_irq\_init](acpi_2acpi_8h.md#ac97acaf39d481f3c3915c763e7f2cdc3)

int acpi\_legacy\_irq\_init(const char \*hid, const char \*uid)

Init legacy interrupt routing table information from ACPI.

[acpi\_current\_resource\_get](acpi_2acpi_8h.md#ae8d0e92bc9f94d1c70dc893b686c29de)

int acpi\_current\_resource\_get(char \*dev\_name, ACPI\_RESOURCE \*\*res)

Retrieve the current resource settings of a device.

[acpi\_dmar\_foreach\_subtable](acpi_2acpi_8h.md#af62e15025d3442b2db39b34c3e138671)

void acpi\_dmar\_foreach\_subtable(ACPI\_TABLE\_DMAR \*dmar, dmar\_foreach\_subtable\_func\_t func, void \*arg)

[dmar\_foreach\_subtable\_func\_t](acpi_2acpi_8h.md#af675794f8aa74fb58c7a2c7266f05357)

void(\* dmar\_foreach\_subtable\_func\_t)(ACPI\_DMAR\_HEADER \*subtable, void \*arg)

**Definition** acpi.h:268

[pcie.h](drivers_2pcie_2pcie_8h.md)

[pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)

uint32\_t pcie\_bdf\_t

A unique PCI(e) endpoint (bus, device, function).

**Definition** pcie.h:37

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[acpi\_dev](structacpi__dev.md)

**Definition** acpi.h:39

[acpi\_dev::path](structacpi__dev.md#a181c2fdd63f316b1d69f3cdc0d924fe2)

char \* path

**Definition** acpi.h:41

[acpi\_dev::dev\_info](structacpi__dev.md#a521452067b5751a2a59d156b13ff24f1)

ACPI\_DEVICE\_INFO \* dev\_info

**Definition** acpi.h:44

[acpi\_dev::res\_lst](structacpi__dev.md#a54c5c7c33a425b565b0e1337063a1c1a)

ACPI\_RESOURCE \* res\_lst

**Definition** acpi.h:42

[acpi\_dev::res\_type](structacpi__dev.md#abc282bce7cdc3de32feb57bc4da790e8)

int res\_type

**Definition** acpi.h:43

[acpi\_dev::handle](structacpi__dev.md#ace9e72f625889d0f84caa17ee6dc8e24)

ACPI\_HANDLE handle

**Definition** acpi.h:40

[acpi\_irq\_resource](structacpi__irq__resource.md)

**Definition** acpi.h:63

[acpi\_irq\_resource::irqs](structacpi__irq__resource.md#a261bdfee8d5a1137a30bd498e1c5b3c4)

uint16\_t \* irqs

**Definition** acpi.h:66

[acpi\_irq\_resource::irq\_vector\_max](structacpi__irq__resource.md#a8d5d5ddb21f52e432862cd0fb16f5f0a)

uint8\_t irq\_vector\_max

**Definition** acpi.h:65

[acpi\_irq\_resource::flags](structacpi__irq__resource.md#ac79f9ccd199de7fa52208dee857e7e8f)

uint32\_t flags

**Definition** acpi.h:64

[acpi\_mcfg](structacpi__mcfg.md)

**Definition** acpi.h:57

[acpi\_mcfg::pci\_segs](structacpi__mcfg.md#a8d6bc322dcb14c2892382067275f2426)

ACPI\_MCFG\_ALLOCATION pci\_segs[]

**Definition** acpi.h:60

[acpi\_mcfg::header](structacpi__mcfg.md#ac3745fb726a32a57992556b9dbaa1365)

ACPI\_TABLE\_HEADER header

**Definition** acpi.h:58

[acpi\_mmio\_resource](structacpi__mmio__resource.md)

**Definition** acpi.h:78

[acpi\_mmio\_resource::mmio\_max](structacpi__mmio__resource.md#a26d31589732a487adbe7b2ab862c4ff4)

uint8\_t mmio\_max

**Definition** acpi.h:79

[acpi\_mmio\_resource::reg\_base](structacpi__mmio__resource.md#ae4ab8715b8f13fa57bc983393c8bd5e6)

struct acpi\_reg\_base \* reg\_base

**Definition** acpi.h:80

[acpi\_reg\_base](structacpi__reg__base.md)

**Definition** acpi.h:69

[acpi\_reg\_base::type](structacpi__reg__base.md#a416f2ff166b33add65eba5e7787c3ef5)

enum acpi\_res\_type type

**Definition** acpi.h:70

[acpi\_reg\_base::length](structacpi__reg__base.md#aaca25908e4e16a71627c48208c55d0ef)

uint32\_t length

**Definition** acpi.h:75

[acpi\_reg\_base::port](structacpi__reg__base.md#ab845df09e3b4b9734103605ea7c65d1e)

uintptr\_t port

**Definition** acpi.h:73

[acpi\_reg\_base::mmio](structacpi__reg__base.md#ada6ffb943e406068271d56b5a129b717)

uintptr\_t mmio

**Definition** acpi.h:72

[acpi\_dmar\_id](unionacpi__dmar__id.md)

**Definition** acpi.h:47

[acpi\_dmar\_id::device](unionacpi__dmar__id.md#a03e48f74dae90bbbeba96c4d9f274020)

uint16\_t device

**Definition** acpi.h:50

[acpi\_dmar\_id::bits](unionacpi__dmar__id.md#a0fffa1ca831591b42f732acfd1d86aa6)

struct acpi\_dmar\_id::@004235266206104020000364357324011322072205222276 bits

[acpi\_dmar\_id::bus](unionacpi__dmar__id.md#a3e9194555004762db83d9853594ffca1)

uint16\_t bus

**Definition** acpi.h:51

[acpi\_dmar\_id::raw](unionacpi__dmar__id.md#a700729e862c40298e4ebe05b7881f009)

uint16\_t raw

**Definition** acpi.h:54

[acpi\_dmar\_id::function](unionacpi__dmar__id.md#a8fe219b9f4f5871cf14d01079af79614)

uint16\_t function

**Definition** acpi.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [acpi](dir_45b4545ed375318b7880b8f15b111e07.md)
- [acpi.h](acpi_2acpi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
