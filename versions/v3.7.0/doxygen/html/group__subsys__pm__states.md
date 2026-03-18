---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__pm__states.html
original_path: doxygen/html/group__subsys__pm__states.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

States

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md)

System Power Management States.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pm\_state\_info](structpm__state__info.md) |
|  | Information about a power management state. [More...](structpm__state__info.md#details) |
| struct | [pm\_state\_constraint](structpm__state__constraint.md) |
|  | Power state information needed to lock a power state. [More...](structpm__state__constraint.md#details) |

| Macros | |
| --- | --- |
| #define | [PM\_STATE\_INFO\_DT\_INIT](#ga1e77683479b589093f06cca9b1d142b9)(node\_id) |
|  | Initializer for struct [pm\_state\_info](structpm__state__info.md "Information about a power management state.") given a DT node identifier with zephyr,power-state compatible. |
| #define | [PM\_STATE\_DT\_INIT](#gadd0dca42aef0a021fed9ca2d588ce393)(node\_id) |
|  | Initializer for enum [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) given a DT node identifier with zephyr,power-state compatible. |
| #define | [DT\_NUM\_CPU\_POWER\_STATES](#ga70e4a8cbc3b0e9427f4bf67ee31b3edd)(node\_id) |
|  | Obtain number of CPU power states supported and enabled by the given CPU node identifier. |
| #define | [PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU](#ga2846f402e20570fc61118b8545cdbe12)(node\_id) |
|  | Initialize an array of struct [pm\_state\_info](structpm__state__info.md "Information about a power management state.") with information from all the states present and enabled in the given CPU node identifier. |
| #define | [PM\_STATE\_LIST\_FROM\_DT\_CPU](#ga8248587108fcb76adefb50a360bc5db7)(node\_id) |
|  | Initialize an array of struct [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) with information from all the states present and enabled in the given CPU node identifier. |

| Enumerations | |
| --- | --- |
| enum | [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) {     [PM\_STATE\_ACTIVE](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a383b8ef562f50d7a3d18914d3c950743) , [PM\_STATE\_RUNTIME\_IDLE](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a73c76572bc04e999d22a3bded9c54b19) , [PM\_STATE\_SUSPEND\_TO\_IDLE](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a781f940d30738d746eb2523155950fc0) , [PM\_STATE\_STANDBY](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a19a09872876d4732d0aebb82e52f2429) ,     [PM\_STATE\_SUSPEND\_TO\_RAM](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a363669b6a6db4bee5b8196442e9f2a00) , [PM\_STATE\_SUSPEND\_TO\_DISK](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5acc7f38698db1ae08365115f8407c9695) , [PM\_STATE\_SOFT\_OFF](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a18d180711616cd9ed59fbe27dd0dbf01) , [PM\_STATE\_COUNT](#gga20e2f5ea9027a3653e5b9cc5aa1e21d5a97c44ed1a8b6873243d6bbd76a382737)   } |
|  | Power management state. [More...](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pm\_state\_cpu\_get\_all](#ga682f75eb5324455ce95a5c7d4c2d6242) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu, const struct [pm\_state\_info](structpm__state__info.md) \*\*states) |
|  | Obtain information about all supported states by a CPU. |

## Detailed Description

System Power Management States.

## Macro Definition Documentation

## [◆ ](#ga70e4a8cbc3b0e9427f4bf67ee31b3edd)DT\_NUM\_CPU\_POWER\_STATES

| #define DT\_NUM\_CPU\_POWER\_STATES | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[state.h](state_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, cpu\_power\_states), \

([DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)(node\_id, cpu\_power\_states, Z\_DT\_PHANDLE\_01, (+))), \

(0))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3479

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3103

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Obtain number of CPU power states supported and enabled by the given CPU node identifier.

Parameters
:   | node\_id | A CPU node identifier. |
    | --- | --- |

Returns
:   Number of supported and enabled CPU power states.

## [◆ ](#gadd0dca42aef0a021fed9ca2d588ce393)PM\_STATE\_DT\_INIT

| #define PM\_STATE\_DT\_INIT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[state.h](state_8h.md)>`

**Value:**

[DT\_ENUM\_IDX](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)(node\_id, power\_state\_name)

[DT\_ENUM\_IDX](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)

#define DT\_ENUM\_IDX(node\_id, prop)

Get a property value's index into its enumeration values.

**Definition** devicetree.h:869

Initializer for enum [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) given a DT node identifier with zephyr,power-state compatible.

Parameters
:   | node\_id | A node identifier with compatible zephyr,power-state |
    | --- | --- |

## [◆ ](#ga1e77683479b589093f06cca9b1d142b9)PM\_STATE\_INFO\_DT\_INIT

| #define PM\_STATE\_INFO\_DT\_INIT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[state.h](state_8h.md)>`

**Value:**

{ \

.state = [PM\_STATE\_DT\_INIT](#gadd0dca42aef0a021fed9ca2d588ce393)(node\_id), \

.substate\_id = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, substate\_id, 0), \

.min\_residency\_us = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, min\_residency\_us, 0), \

.exit\_latency\_us = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, exit\_latency\_us, 0), \

.pm\_device\_disabled = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, zephyr\_pm\_device\_disabled), \

}

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:825

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:663

[PM\_STATE\_DT\_INIT](#gadd0dca42aef0a021fed9ca2d588ce393)

#define PM\_STATE\_DT\_INIT(node\_id)

Initializer for enum pm\_state given a DT node identifier with zephyr,power-state compatible.

**Definition** state.h:249

Initializer for struct [pm\_state\_info](structpm__state__info.md "Information about a power management state.") given a DT node identifier with zephyr,power-state compatible.

Parameters
:   | node\_id | A node identifier with compatible zephyr,power-state |
    | --- | --- |

## [◆ ](#ga2846f402e20570fc61118b8545cdbe12)PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU

| #define PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[state.h](state_8h.md)>`

**Value:**

{ \

LISTIFY([DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)(node\_id, cpu\_power\_states, 0), \

Z\_PM\_STATE\_INFO\_FROM\_DT\_CPU, (), node\_id) \

}

[DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)

#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value)

Like DT\_PROP\_LEN(), but with a fallback to default\_value.

**Definition** devicetree.h:713

Initialize an array of struct [pm\_state\_info](structpm__state__info.md "Information about a power management state.") with information from all the states present and enabled in the given CPU node identifier.

Example devicetree fragment:

cpus {

...

cpu0: cpu@0 {

device\_type = "cpu";

...

cpu-power-states = <&state0 &state1>;

};

power-states {

state0: state0 {

compatible = "zephyr,power-state";

power-state-name = "suspend-to-idle";

min-residency-us = <10000>;

exit-latency-us = <100>;

};

state1: state1 {

compatible = "zephyr,power-state";

power-state-name = "suspend-to-ram";

min-residency-us = <50000>;

exit-latency-us = <500>;

zephyr,pm-device-disabled;

};

};

};

Example usage:

const struct [pm\_state\_info](structpm__state__info.md) states[] =

[PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU](#ga2846f402e20570fc61118b8545cdbe12)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(cpu0));

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:200

[PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU](#ga2846f402e20570fc61118b8545cdbe12)

#define PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU(node\_id)

Initialize an array of struct pm\_state\_info with information from all the states present and enabled ...

**Definition** state.h:308

[pm\_state\_info](structpm__state__info.md)

Information about a power management state.

**Definition** state.h:114

Parameters
:   | node\_id | A CPU node identifier. |
    | --- | --- |

## [◆ ](#ga8248587108fcb76adefb50a360bc5db7)PM\_STATE\_LIST\_FROM\_DT\_CPU

| #define PM\_STATE\_LIST\_FROM\_DT\_CPU | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[state.h](state_8h.md)>`

**Value:**

{ \

LISTIFY([DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)(node\_id, cpu\_power\_states, 0), \

Z\_PM\_STATE\_FROM\_DT\_CPU, (), node\_id) \

}

Initialize an array of struct [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) with information from all the states present and enabled in the given CPU node identifier.

Example devicetree fragment:

cpus {

...

cpu0: cpu@0 {

device\_type = "cpu";

...

cpu-power-states = <&state0 &state1>;

};

power-states {

state0: state0 {

compatible = "zephyr,power-state";

power-state-name = "suspend-to-idle";

min-residency-us = <10000>;

exit-latency-us = <100>;

};

state1: state1 {

compatible = "zephyr,power-state";

power-state-name = "suspend-to-ram";

min-residency-us = <50000>;

exit-latency-us = <500>;

};

};

};

Example usage:

const enum [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) states[] = [PM\_STATE\_LIST\_FROM\_DT\_CPU](#ga8248587108fcb76adefb50a360bc5db7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(cpu0));

[pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)

pm\_state

Power management state.

**Definition** state.h:27

[PM\_STATE\_LIST\_FROM\_DT\_CPU](#ga8248587108fcb76adefb50a360bc5db7)

#define PM\_STATE\_LIST\_FROM\_DT\_CPU(node\_id)

Initialize an array of struct pm\_state with information from all the states present and enabled in th...

**Definition** state.h:355

Parameters
:   | node\_id | A CPU node identifier. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5)pm\_state

| enum [pm\_state](#ga20e2f5ea9027a3653e5b9cc5aa1e21d5) |
| --- |

`#include <[state.h](state_8h.md)>`

Power management state.

| Enumerator | |
| --- | --- |
| PM\_STATE\_ACTIVE | Runtime active state.  The system is fully powered and active.  Note  This state is correlated with ACPI G0/S0 state |
| PM\_STATE\_RUNTIME\_IDLE | Runtime idle state.  Runtime idle is a system sleep state in which all of the cores enter deepest possible idle state and wait for interrupts, no requirements for the devices, leaving them at the states where they are.  Note  This state is correlated with ACPI S0ix state |
| PM\_STATE\_SUSPEND\_TO\_IDLE | Suspend to idle state.  The system goes through a normal platform suspend where it puts all of the cores in deepest possible idle state and *may* puts peripherals into low-power states. No operating state is lost (ie. the cpu core does not lose execution context), so the system can go back to where it left off easily enough.  Note  This state is correlated with ACPI S1 state |
| PM\_STATE\_STANDBY | Standby state.  In addition to putting peripherals into low-power states all non-boot CPUs are powered off. It should allow more energy to be saved relative to suspend to idle, but the resume latency will generally be greater than for that state. But it should be the same state with suspend to idle state on uniprocessor system.  Note  This state is correlated with ACPI S2 state |
| PM\_STATE\_SUSPEND\_TO\_RAM | Suspend to ram state.  This state offers significant energy savings by powering off as much of the system as possible, where memory should be placed into the self-refresh mode to retain its contents. The state of devices and CPUs is saved and held in memory, and it may require some boot- strapping code in ROM to resume the system from it.  Note  This state is correlated with ACPI S3 state |
| PM\_STATE\_SUSPEND\_TO\_DISK | Suspend to disk state.  This state offers significant energy savings by powering off as much of the system as possible, including the memory. The contents of memory are written to disk or other non-volatile storage, and on resume it's read back into memory with the help of boot-strapping code, restores the system to the same point of execution where it went to suspend to disk.  Note  This state is correlated with ACPI S4 state |
| PM\_STATE\_SOFT\_OFF | Soft off state.  This state consumes a minimal amount of power and requires a large latency in order to return to runtime active state. The contents of system(CPU and memory) will not be preserved, so the system will be restarted as if from initial power-up and kernel boot.  Note  This state is correlated with ACPI G2/S5 state |
| PM\_STATE\_COUNT | Number of power management states (internal use). |

## Function Documentation

## [◆ ](#ga682f75eb5324455ce95a5c7d4c2d6242)pm\_state\_cpu\_get\_all()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pm\_state\_cpu\_get\_all | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cpu*, |
| --- | --- | --- | --- |
|  |  | const struct [pm\_state\_info](structpm__state__info.md) \*\* | *states* ) |

`#include <[state.h](state_8h.md)>`

Obtain information about all supported states by a CPU.

Parameters
:   | cpu | CPU index. |
    | --- | --- |
    | states | Where to store the list of supported states. |

Returns
:   Number of supported states.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
