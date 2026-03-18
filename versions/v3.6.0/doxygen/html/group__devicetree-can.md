---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-can.html
original_path: doxygen/html/group__devicetree-can.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree CAN API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE](#ga9c56ded2142fbd8a4a7facffd3dd549d)(node\_id, max) |
|  | Get the maximum transceiver bitrate for a CAN controller. |
| #define | [DT\_INST\_CAN\_TRANSCEIVER\_MAX\_BITRATE](#gacac28e33d8a749518485c687a563763f)(inst, max) |
|  | Get the maximum transceiver bitrate for a DT\_DRV\_COMPAT CAN controller. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga9c56ded2142fbd8a4a7facffd3dd549d)DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE

| #define DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *max* ) |

`#include <[can.h](devicetree_2can_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, phys), \

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)(node\_id, phys), max\_bitrate), max), \

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)([DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)(node\_id, can\_transceiver), max\_bitrate, max), max))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3285

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)

#define DT\_CHILD(node\_id, child)

Get a node identifier for a child node.

**Definition** devicetree.h:421

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:777

[DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)

#define DT\_PHANDLE(node\_id, prop)

Get a node identifier for a phandle property's value.

**Definition** devicetree.h:1594

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:373

Get the maximum transceiver bitrate for a CAN controller.

The bitrate will be limited to the maximum bitrate supported by the CAN controller. If no CAN transceiver is present in the devicetree, the maximum bitrate will be that of the CAN controller.

Example devicetree fragment:

```
transceiver0: can-phy0 {
        compatible = "vnd,can-transceiver";
        max-bitrate = <1000000>;
        #phy-cells = <0>;
};

can0: can@... {
        compatible = "vnd,can-controller";
        phys = <&transceiver0>;
};

can1: can@... {
        compatible = "vnd,can-controller";

        can-transceiver {
                max-bitrate = <2000000>;
        };
};
```

Example usage:

```
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can0), 5000000) // 1000000
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can1), 5000000) // 2000000
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can1), 1000000) // 1000000
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | max | maximum bitrate supported by the CAN controller |

Returns
:   the maximum bitrate supported by the CAN controller/transceiver combination

## [◆ ](#gacac28e33d8a749518485c687a563763f)DT\_INST\_CAN\_TRANSCEIVER\_MAX\_BITRATE

| #define DT\_INST\_CAN\_TRANSCEIVER\_MAX\_BITRATE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *max* ) |

`#include <[can.h](devicetree_2can_8h.md)>`

**Value:**

[DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE](#ga9c56ded2142fbd8a4a7facffd3dd549d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), max)

[DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE](#ga9c56ded2142fbd8a4a7facffd3dd549d)

#define DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE(node\_id, max)

Get the maximum transceiver bitrate for a CAN controller.

**Definition** can.h:63

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

Get the maximum transceiver bitrate for a DT\_DRV\_COMPAT CAN controller.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | max | maximum bitrate supported by the CAN controller |

Returns
:   the maximum bitrate supported by the CAN controller/transceiver combination

See also
:   [DT\_CAN\_TRANSCEIVER\_MAX\_BITRATE()](#ga9c56ded2142fbd8a4a7facffd3dd549d)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
