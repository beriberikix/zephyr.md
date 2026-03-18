---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/acpi_8h.html
original_path: doxygen/html/acpi_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

acpi.h File Reference

`#include <acpica/source/include/acpi.h>`  
`#include <[zephyr/drivers/pcie/pcie.h](drivers_2pcie_2pcie_8h_source.md)>`

[Go to the source code of this file.](acpi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [acpi\_dev](structacpi__dev.md) |
| union | [acpi\_dmar\_id](unionacpi__dmar__id.md) |
| struct | [acpi\_mcfg](structacpi__mcfg.md) |
| struct | [acpi\_irq\_resource](structacpi__irq__resource.md) |
| struct | [acpi\_reg\_base](structacpi__reg__base.md) |
| struct | [acpi\_mmio\_resource](structacpi__mmio__resource.md) |

| Macros | |
| --- | --- |
| #define | [ACPI\_RES\_INVALID](#a5de2990466b70b703d48c6c341e427b3)   ACPI\_RESOURCE\_TYPE\_MAX |
| #define | [ACPI\_DRHD\_FLAG\_INCLUDE\_PCI\_ALL](#a9f534875dab25e2ea48b2676ea8e71b8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ACPI\_DMAR\_FLAG\_INTR\_REMAP](#a92085a7267a8f1569d6d836fc6f8459b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ACPI\_DMAR\_FLAG\_X2APIC\_OPT\_OUT](#a346ee226be8400feaf94198db3da4c44)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ACPI\_DMAR\_FLAG\_DMA\_CTRL\_PLATFORM\_OPT\_IN](#a695794eaf1ebfa25ed1c0ad0d42105f2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ACPI\_MMIO\_GET](#a1f8ab630f3c98ceb0c9f59a78b9a24da)(res) |
| #define | [ACPI\_IO\_GET](#a0d45750fe126a6f9641f7f94d843381d)(res) |
| #define | [ACPI\_RESOURCE\_SIZE\_GET](#abc9aa4017edfc68ac47208e8f758dd60)(res) |
| #define | [ACPI\_RESOURCE\_TYPE\_GET](#aa822c0ca234e1b3ea5fc0007c9f490d4)(res) |
| #define | [ACPI\_MULTI\_MMIO\_GET](#af131fc0845a57664d8df8983c074c064)(res, idx) |
| #define | [ACPI\_MULTI\_IO\_GET](#ad5adfc6540aa9118542970d76d6512bd)(res, idx) |
| #define | [ACPI\_MULTI\_RESOURCE\_SIZE\_GET](#ac77fc44c979b87bcb571f77657954d99)(res, idx) |
| #define | [ACPI\_MULTI\_RESOURCE\_TYPE\_GET](#a1e50c8e8f08f6bab0ed12ad97f573b0f)(res, idx) |
| #define | [ACPI\_RESOURCE\_COUNT\_GET](#ac174fef6e234ec8452485c199d9de90d)(res) |
| #define | [ACPI\_DT\_HID](#a76212438f3a5020919bfde46128f2fb4)(node\_id) |
|  | Get the ACPI HID for a node. |
| #define | [ACPI\_DT\_UID](#a509335d1d6310b109a5047c5a65e1761)(node\_id) |
|  | Get the ACPI UID for a node if one exist. |
| #define | [ACPI\_DT\_HAS\_HID](#a9b849938061877cee953fd7257575268)(node\_id) |
|  | check whether the node has ACPI HID property or not |
| #define | [ACPI\_DT\_HAS\_UID](#ad91001baf45a0110c85c51b405beaced)(node\_id) |
|  | check whether the node has ACPI UID property or not |

| Typedefs | |
| --- | --- |
| typedef void(\* | [dmar\_foreach\_subtable\_func\_t](#af675794f8aa74fb58c7a2c7266f05357)) (ACPI\_DMAR\_HEADER \*subtable, void \*arg) |
| typedef void(\* | [dmar\_foreach\_devscope\_func\_t](#a6b294403ca4a5e1c234c42279d201490)) (ACPI\_DMAR\_DEVICE\_SCOPE \*devscope, void \*arg) |

| Enumerations | |
| --- | --- |
| enum | [acpi\_res\_type](#a225bfac5f9770bd826ae98d2bbbbfc5b) { [ACPI\_RES\_TYPE\_IO](#a225bfac5f9770bd826ae98d2bbbbfc5badde21e335fe3363fd60eb3076dfe7a9f) , [ACPI\_RES\_TYPE\_MEM](#a225bfac5f9770bd826ae98d2bbbbfc5ba609d72a263b7ed46da533aeab6255626) , [ACPI\_RES\_TYPE\_UNKNOWN](#a225bfac5f9770bd826ae98d2bbbbfc5bad9f5eaef7ee5ef391c917786a358278b) } |

| Functions | |
| --- | --- |
| int | [acpi\_legacy\_irq\_init](#ac97acaf39d481f3c3915c763e7f2cdc3) (const char \*hid, const char \*uid) |
|  | Init legacy interrupt routing table information from ACPI. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [acpi\_legacy\_irq\_get](#a139f52f8431a00d34abae1d5a5f31d92) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Retrieve a legacy interrupt number for a PCI device. |
| int | [acpi\_current\_resource\_get](#ae8d0e92bc9f94d1c70dc893b686c29de) (char \*dev\_name, ACPI\_RESOURCE \*\*res) |
|  | Retrieve the current resource settings of a device. |
| int | [acpi\_possible\_resource\_get](#a5787a05051ffb4ccab113cf2e834678d) (char \*dev\_name, ACPI\_RESOURCE \*\*res) |
|  | Retrieve possible resource settings of a device. |
| int | [acpi\_current\_resource\_free](#a703f435a640e34080a6cf52c2256294e) (ACPI\_RESOURCE \*res) |
|  | Free current resource list memory which is retrieved by [acpi\_current\_resource\_get()](#ae8d0e92bc9f94d1c70dc893b686c29de). |
| ACPI\_RESOURCE \* | [acpi\_resource\_parse](#aa5d7b0c25e6e2767c15edbce33971c72) (ACPI\_RESOURCE \*res, int res\_type) |
|  | Parse resource table for a given resource type. |
| struct [acpi\_dev](structacpi__dev.md) \* | [acpi\_device\_get](#a6416a93af8385d3784d205b8811a6a94) (const char \*hid, const char \*uid) |
|  | Retrieve ACPI device info for given hardware id and unique id. |
| struct [acpi\_dev](structacpi__dev.md) \* | [acpi\_device\_by\_index\_get](#a625d35bab5922b679517fe8d8b0aface) (int index) |
|  | Retrieve acpi device info from the index. |
| static ACPI\_RESOURCE\_IRQ \* | [acpi\_irq\_res\_get](#a3a0c7a6232c1f1f08ae0be3e5c3fac7a) (ACPI\_RESOURCE \*res\_lst) |
|  | Parse resource table for irq info. |
| int | [acpi\_device\_irq\_get](#ab8a0982a3acc857ea059bb617b8b43f7) (struct [acpi\_dev](structacpi__dev.md) \*child\_dev, struct [acpi\_irq\_resource](structacpi__irq__resource.md) \*irq\_res) |
|  | Parse resource table for irq info. |
| int | [acpi\_device\_mmio\_get](#a4179d931233431ec61b5e12c1c77931d) (struct [acpi\_dev](structacpi__dev.md) \*child\_dev, struct [acpi\_mmio\_resource](structacpi__mmio__resource.md) \*mmio\_res) |
|  | Parse resource table for MMIO info. |
| int | [acpi\_device\_type\_get](#a44b747b1b7493627a8022c49571b04ff) (ACPI\_RESOURCE \*res) |
|  | Parse resource table for identify resource type. |
| void \* | [acpi\_table\_get](#ab6f0b5f0ae6cf1da923051f2e38fa193) (char \*signature, int inst) |
|  | Retrieve acpi table for the given signature. |
| int | [acpi\_madt\_entry\_get](#abb83809ce252f82f93ea042dfba3fbfd) (int type, ACPI\_SUBTABLE\_HEADER \*\*tables, int \*num\_inst) |
|  | retrieve acpi MAD table for the given type. |
| int | [acpi\_dmar\_entry\_get](#a36d899259fe64aea46549e54ebbfbf0a) (enum AcpiDmarType type, ACPI\_SUBTABLE\_HEADER \*\*tables) |
|  | retrieve DMA remapping structure for the given type. |
| int | [acpi\_drhd\_get](#a1d9f2e00bbcc8a0e101091c6d6be4ac5) (enum AcpiDmarScopeType scope, ACPI\_DMAR\_DEVICE\_SCOPE \*dev\_scope, union [acpi\_dmar\_id](unionacpi__dmar__id.md) \*dmar\_id, int \*num\_inst, int max\_inst) |
|  | retrieve acpi DRHD info for the given scope. |
| void | [acpi\_dmar\_foreach\_subtable](#af62e15025d3442b2db39b34c3e138671) (ACPI\_TABLE\_DMAR \*dmar, [dmar\_foreach\_subtable\_func\_t](#af675794f8aa74fb58c7a2c7266f05357) func, void \*arg) |
| void | [acpi\_dmar\_foreach\_devscope](#a77d02fbe12ff3e02368582c489f7c7d5) (ACPI\_DMAR\_HARDWARE\_UNIT \*hu, [dmar\_foreach\_devscope\_func\_t](#a6b294403ca4a5e1c234c42279d201490) func, void \*arg) |
| int | [acpi\_dmar\_ioapic\_get](#a9768a4b3d13edb8456736256ec015e04) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*ioapic\_id) |
|  | Retrieve IOAPIC id. |
| ACPI\_MADT\_LOCAL\_APIC \* | [acpi\_local\_apic\_get](#a750b6348bfc9f3867b561ff9d7a08b4c) (int cpu\_num) |
|  | Retrieve the 'n'th enabled local apic info. |
| int | [acpi\_invoke\_method](#aab272d92004e687bdd2936f648f3f9f9) (char \*path, ACPI\_OBJECT\_LIST \*arg\_list, ACPI\_OBJECT \*ret\_obj) |
|  | invoke an ACPI method and return the result. |

## Macro Definition Documentation

## [◆ ](#a695794eaf1ebfa25ed1c0ad0d42105f2)ACPI\_DMAR\_FLAG\_DMA\_CTRL\_PLATFORM\_OPT\_IN

| #define ACPI\_DMAR\_FLAG\_DMA\_CTRL\_PLATFORM\_OPT\_IN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a92085a7267a8f1569d6d836fc6f8459b)ACPI\_DMAR\_FLAG\_INTR\_REMAP

| #define ACPI\_DMAR\_FLAG\_INTR\_REMAP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a346ee226be8400feaf94198db3da4c44)ACPI\_DMAR\_FLAG\_X2APIC\_OPT\_OUT

| #define ACPI\_DMAR\_FLAG\_X2APIC\_OPT\_OUT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a9f534875dab25e2ea48b2676ea8e71b8)ACPI\_DRHD\_FLAG\_INCLUDE\_PCI\_ALL

| #define ACPI\_DRHD\_FLAG\_INCLUDE\_PCI\_ALL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a9b849938061877cee953fd7257575268)ACPI\_DT\_HAS\_HID

| #define ACPI\_DT\_HAS\_HID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, acpi\_hid)

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3285

check whether the node has ACPI HID property or not

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |

Returns
:   1 if the node has the HID, 0 otherwise.

## [◆ ](#ad91001baf45a0110c85c51b405beaced)ACPI\_DT\_HAS\_UID

| #define ACPI\_DT\_HAS\_UID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, acpi\_uid)

check whether the node has ACPI UID property or not

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |

Returns
:   1 if the node has the UID, 0 otherwise.

## [◆ ](#a76212438f3a5020919bfde46128f2fb4)ACPI\_DT\_HID

| #define ACPI\_DT\_HID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, acpi\_hid)

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

Get the ACPI HID for a node.

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |

Returns
:   The HID of the ACPI node

## [◆ ](#a509335d1d6310b109a5047c5a65e1761)ACPI\_DT\_UID

| #define ACPI\_DT\_UID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, acpi\_uid, NULL)

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:777

Get the ACPI UID for a node if one exist.

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |

Returns
:   The UID of the ACPI node else NULL if does not exist

## [◆ ](#a0d45750fe126a6f9641f7f94d843381d)ACPI\_IO\_GET

| #define ACPI\_IO\_GET | ( |  | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(res)->reg\_base[0].port

## [◆ ](#a1f8ab630f3c98ceb0c9f59a78b9a24da)ACPI\_MMIO\_GET

| #define ACPI\_MMIO\_GET | ( |  | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(res)->reg\_base[0].mmio

## [◆ ](#ad5adfc6540aa9118542970d76d6512bd)ACPI\_MULTI\_IO\_GET

| #define ACPI\_MULTI\_IO\_GET | ( |  | *res*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

**Value:**

(res)->reg\_base[idx].port

## [◆ ](#af131fc0845a57664d8df8983c074c064)ACPI\_MULTI\_MMIO\_GET

| #define ACPI\_MULTI\_MMIO\_GET | ( |  | *res*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

**Value:**

(res)->reg\_base[idx].mmio

## [◆ ](#ac77fc44c979b87bcb571f77657954d99)ACPI\_MULTI\_RESOURCE\_SIZE\_GET

| #define ACPI\_MULTI\_RESOURCE\_SIZE\_GET | ( |  | *res*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

**Value:**

(res)->reg\_base[idx].length

## [◆ ](#a1e50c8e8f08f6bab0ed12ad97f573b0f)ACPI\_MULTI\_RESOURCE\_TYPE\_GET

| #define ACPI\_MULTI\_RESOURCE\_TYPE\_GET | ( |  | *res*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

**Value:**

(res)->reg\_base[idx].type

## [◆ ](#a5de2990466b70b703d48c6c341e427b3)ACPI\_RES\_INVALID

| #define ACPI\_RES\_INVALID   ACPI\_RESOURCE\_TYPE\_MAX |
| --- |

## [◆ ](#ac174fef6e234ec8452485c199d9de90d)ACPI\_RESOURCE\_COUNT\_GET

| #define ACPI\_RESOURCE\_COUNT\_GET | ( |  | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(res)->mmio\_max

## [◆ ](#abc9aa4017edfc68ac47208e8f758dd60)ACPI\_RESOURCE\_SIZE\_GET

| #define ACPI\_RESOURCE\_SIZE\_GET | ( |  | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(res)->reg\_base[0].length

## [◆ ](#aa822c0ca234e1b3ea5fc0007c9f490d4)ACPI\_RESOURCE\_TYPE\_GET

| #define ACPI\_RESOURCE\_TYPE\_GET | ( |  | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(res)->reg\_base[0].type

## Typedef Documentation

## [◆ ](#a6b294403ca4a5e1c234c42279d201490)dmar\_foreach\_devscope\_func\_t

| typedef void(\* dmar\_foreach\_devscope\_func\_t) (ACPI\_DMAR\_DEVICE\_SCOPE \*devscope, void \*arg) |
| --- |

## [◆ ](#af675794f8aa74fb58c7a2c7266f05357)dmar\_foreach\_subtable\_func\_t

| typedef void(\* dmar\_foreach\_subtable\_func\_t) (ACPI\_DMAR\_HEADER \*subtable, void \*arg) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a225bfac5f9770bd826ae98d2bbbbfc5b)acpi\_res\_type

| enum [acpi\_res\_type](#a225bfac5f9770bd826ae98d2bbbbfc5b) |
| --- |

| Enumerator | |
| --- | --- |
| ACPI\_RES\_TYPE\_IO | IO mapped Resource type. |
| ACPI\_RES\_TYPE\_MEM | Memory mapped Resource type. |
| ACPI\_RES\_TYPE\_UNKNOWN | Unknown Resource type. |

## Function Documentation

## [◆ ](#a703f435a640e34080a6cf52c2256294e)acpi\_current\_resource\_free()

| int acpi\_current\_resource\_free | ( | ACPI\_RESOURCE \* | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

Free current resource list memory which is retrieved by [acpi\_current\_resource\_get()](#ae8d0e92bc9f94d1c70dc893b686c29de).

Parameters
:   | res | the list of acpi resource list |
    | --- | --- |

Returns
:   return 0 on success or error code

## [◆ ](#ae8d0e92bc9f94d1c70dc893b686c29de)acpi\_current\_resource\_get()

| int acpi\_current\_resource\_get | ( | char \* | *dev\_name*, |
| --- | --- | --- | --- |
|  |  | ACPI\_RESOURCE \*\* | *res* ) |

Retrieve the current resource settings of a device.

Parameters
:   | dev\_name | the name of the device |
    | --- | --- |
    | res | the list of acpi resource list |

Returns
:   return 0 on success or error code

## [◆ ](#a625d35bab5922b679517fe8d8b0aface)acpi\_device\_by\_index\_get()

| struct [acpi\_dev](structacpi__dev.md) \* acpi\_device\_by\_index\_get | ( | int | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

Retrieve acpi device info from the index.

Parameters
:   | index | the device index of an acpi child device |
    | --- | --- |

Returns
:   acpi child device info on success or NULL

## [◆ ](#a6416a93af8385d3784d205b8811a6a94)acpi\_device\_get()

| struct [acpi\_dev](structacpi__dev.md) \* acpi\_device\_get | ( | const char \* | *hid*, |
| --- | --- | --- | --- |
|  |  | const char \* | *uid* ) |

Retrieve ACPI device info for given hardware id and unique id.

Parameters
:   | hid | the hardware id of the ACPI child device |
    | --- | --- |
    | uid | the unique id of the ACPI child device. The uid can be NULL if only one device with given HID present in the platform. |

Returns
:   ACPI child device info on success or NULL

## [◆ ](#ab8a0982a3acc857ea059bb617b8b43f7)acpi\_device\_irq\_get()

| int acpi\_device\_irq\_get | ( | struct [acpi\_dev](structacpi__dev.md) \* | *child\_dev*, |
| --- | --- | --- | --- |
|  |  | struct [acpi\_irq\_resource](structacpi__irq__resource.md) \* | *irq\_res* ) |

Parse resource table for irq info.

Parameters
:   | child\_dev | the device object of the ACPI node |
    | --- | --- |
    | irq\_res | irq resource info |

Returns
:   return 0 on success or error code

## [◆ ](#a4179d931233431ec61b5e12c1c77931d)acpi\_device\_mmio\_get()

| int acpi\_device\_mmio\_get | ( | struct [acpi\_dev](structacpi__dev.md) \* | *child\_dev*, |
| --- | --- | --- | --- |
|  |  | struct [acpi\_mmio\_resource](structacpi__mmio__resource.md) \* | *mmio\_res* ) |

Parse resource table for MMIO info.

Parameters
:   | child\_dev | the device object of the ACPI node |
    | --- | --- |
    | mmio\_res | MMIO resource info |

Returns
:   return 0 on success or error code

## [◆ ](#a44b747b1b7493627a8022c49571b04ff)acpi\_device\_type\_get()

| int acpi\_device\_type\_get | ( | ACPI\_RESOURCE \* | *res* | ) |  |
| --- | --- | --- | --- | --- | --- |

Parse resource table for identify resource type.

Parameters
:   | res | the list of acpi resource list |
    | --- | --- |

Returns
:   resource type on success or invalid resource type

## [◆ ](#a36d899259fe64aea46549e54ebbfbf0a)acpi\_dmar\_entry\_get()

| int acpi\_dmar\_entry\_get | ( | enum AcpiDmarType | *type*, |
| --- | --- | --- | --- |
|  |  | ACPI\_SUBTABLE\_HEADER \*\* | *tables* ) |

retrieve DMA remapping structure for the given type.

Parameters
:   | type | type of remapping structure |
    | --- | --- |
    | tables | pointer to the dmar id structure |

Returns
:   return 0 on success or error code

## [◆ ](#a77d02fbe12ff3e02368582c489f7c7d5)acpi\_dmar\_foreach\_devscope()

| void acpi\_dmar\_foreach\_devscope | ( | ACPI\_DMAR\_HARDWARE\_UNIT \* | *hu*, |
| --- | --- | --- | --- |
|  |  | [dmar\_foreach\_devscope\_func\_t](#a6b294403ca4a5e1c234c42279d201490) | *func*, |
|  |  | void \* | *arg* ) |

## [◆ ](#af62e15025d3442b2db39b34c3e138671)acpi\_dmar\_foreach\_subtable()

| void acpi\_dmar\_foreach\_subtable | ( | ACPI\_TABLE\_DMAR \* | *dmar*, |
| --- | --- | --- | --- |
|  |  | [dmar\_foreach\_subtable\_func\_t](#af675794f8aa74fb58c7a2c7266f05357) | *func*, |
|  |  | void \* | *arg* ) |

## [◆ ](#a9768a4b3d13edb8456736256ec015e04)acpi\_dmar\_ioapic\_get()

| int acpi\_dmar\_ioapic\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *ioapic\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

Retrieve IOAPIC id.

Parameters
:   | ioapic\_id | IOAPIC id |
    | --- | --- |

Returns
:   return 0 on success or error code

## [◆ ](#a1d9f2e00bbcc8a0e101091c6d6be4ac5)acpi\_drhd\_get()

| int acpi\_drhd\_get | ( | enum AcpiDmarScopeType | *scope*, |
| --- | --- | --- | --- |
|  |  | ACPI\_DMAR\_DEVICE\_SCOPE \* | *dev\_scope*, |
|  |  | union [acpi\_dmar\_id](unionacpi__dmar__id.md) \* | *dmar\_id*, |
|  |  | int \* | *num\_inst*, |
|  |  | int | *max\_inst* ) |

retrieve acpi DRHD info for the given scope.

Parameters
:   | scope | scope of requested DHRD table |
    | --- | --- |
    | dev\_scope | pointer to the sub table (optional) |
    | dmar\_id | pointer to the DHRD info |
    | num\_inst | number of instance for the requested table |
    | max\_inst | maximum number of entry for the given dmar\_id buffer |

Returns
:   return 0 on success or error code

## [◆ ](#aab272d92004e687bdd2936f648f3f9f9)acpi\_invoke\_method()

| int acpi\_invoke\_method | ( | char \* | *path*, |
| --- | --- | --- | --- |
|  |  | ACPI\_OBJECT\_LIST \* | *arg\_list*, |
|  |  | ACPI\_OBJECT \* | *ret\_obj* ) |

invoke an ACPI method and return the result.

Parameters
:   | path | the path name of the ACPI object |
    | --- | --- |
    | arg\_list | the list of arguments to be pass down |
    | ret\_obj | the ACPI result to be return |

Returns
:   return 0 on success or error code

## [◆ ](#a3a0c7a6232c1f1f08ae0be3e5c3fac7a)acpi\_irq\_res\_get()

| | ACPI\_RESOURCE\_IRQ \* acpi\_irq\_res\_get | ( | ACPI\_RESOURCE \* | *res\_lst* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Parse resource table for irq info.

Parameters
:   | res\_lst | the list of acpi resource list |
    | --- | --- |

Returns
:   irq resource list on success or NULL

## [◆ ](#a139f52f8431a00d34abae1d5a5f31d92)acpi\_legacy\_irq\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) acpi\_legacy\_irq\_get | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

Retrieve a legacy interrupt number for a PCI device.

Parameters
:   | bdf | the BDF of endpoint/PCI device |
    | --- | --- |

Returns
:   return IRQ number or UINT\_MAX if not found

## [◆ ](#ac97acaf39d481f3c3915c763e7f2cdc3)acpi\_legacy\_irq\_init()

| int acpi\_legacy\_irq\_init | ( | const char \* | *hid*, |
| --- | --- | --- | --- |
|  |  | const char \* | *uid* ) |

Init legacy interrupt routing table information from ACPI.

Currently assume platform have only one PCI bus.

Parameters
:   | hid | the hardware id of the ACPI child device |
    | --- | --- |
    | uid | the unique id of the ACPI child device. The uid can be NULL if only one device with given hid present in the platform. |

Returns
:   return 0 on success or error code

## [◆ ](#a750b6348bfc9f3867b561ff9d7a08b4c)acpi\_local\_apic\_get()

| ACPI\_MADT\_LOCAL\_APIC \* acpi\_local\_apic\_get | ( | int | *cpu\_num* | ) |  |
| --- | --- | --- | --- | --- | --- |

Retrieve the 'n'th enabled local apic info.

Parameters
:   | cpu\_num | the cpu number |
    | --- | --- |

Returns
:   local apic info on success or NULL otherwise

## [◆ ](#abb83809ce252f82f93ea042dfba3fbfd)acpi\_madt\_entry\_get()

| int acpi\_madt\_entry\_get | ( | int | *type*, |
| --- | --- | --- | --- |
|  |  | ACPI\_SUBTABLE\_HEADER \*\* | *tables*, |
|  |  | int \* | *num\_inst* ) |

retrieve acpi MAD table for the given type.

Parameters
:   | type | type of requested MAD table |
    | --- | --- |
    | tables | pointer to the MAD table |
    | num\_inst | number of instance for the requested table |

Returns
:   return 0 on success or error code

## [◆ ](#a5787a05051ffb4ccab113cf2e834678d)acpi\_possible\_resource\_get()

| int acpi\_possible\_resource\_get | ( | char \* | *dev\_name*, |
| --- | --- | --- | --- |
|  |  | ACPI\_RESOURCE \*\* | *res* ) |

Retrieve possible resource settings of a device.

Parameters
:   | dev\_name | the name of the device |
    | --- | --- |
    | res | the list of acpi resource list |

Returns
:   return 0 on success or error code

## [◆ ](#aa5d7b0c25e6e2767c15edbce33971c72)acpi\_resource\_parse()

| ACPI\_RESOURCE \* acpi\_resource\_parse | ( | ACPI\_RESOURCE \* | *res*, |
| --- | --- | --- | --- |
|  |  | int | *res\_type* ) |

Parse resource table for a given resource type.

Parameters
:   | res | the list of acpi resource list |
    | --- | --- |
    | res\_type | the acpi resource type |

Returns
:   resource list for the given type on success or NULL

## [◆ ](#ab6f0b5f0ae6cf1da923051f2e38fa193)acpi\_table\_get()

| void \* acpi\_table\_get | ( | char \* | *signature*, |
| --- | --- | --- | --- |
|  |  | int | *inst* ) |

Retrieve acpi table for the given signature.

Parameters
:   | signature | pointer to the 4-character ACPI signature for the requested table |
    | --- | --- |
    | inst | instance number for the requested table |

Returns
:   acpi\_table pointer to the acpi table on success else return NULL

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [acpi](dir_45b4545ed375318b7880b8f15b111e07.md)
- [acpi.h](acpi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
