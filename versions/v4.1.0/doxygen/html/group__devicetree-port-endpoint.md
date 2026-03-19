---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__devicetree-port-endpoint.html
original_path: doxygen/html/group__devicetree-port-endpoint.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree Port Endpoint API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_INST\_PORT\_BY\_ID](#gaf3427020d7d560c5da3df0f553988f71)(inst, pid) |
|  | Get a port node from its id. |
| #define | [DT\_INST\_ENDPOINT\_BY\_ID](#ga0d2315ddc63c986da0e90177e8d8eab8)(inst, pid, eid) |
|  | Get an endpoint node from its id and its parent port id. |
| #define | [DT\_NODE\_BY\_ENDPOINT](#ga37c2b0183196f513fc2222ba5fbe30d7)(ep) |
|  | Get the device node from its endpoint node. |
| #define | [DT\_NODE\_REMOTE\_DEVICE](#gaf1261a1a110fc0b164e6eafbaf885f7d)(ep) |
|  | Get the remote device node from a local endpoint node. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga0d2315ddc63c986da0e90177e8d8eab8)DT\_INST\_ENDPOINT\_BY\_ID

| #define DT\_INST\_ENDPOINT\_BY\_ID | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pid*, |
|  |  |  | *eid* ) |

`#include <[port-endpoint.h](port-endpoint_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)(\_DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid)), \

(\_DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid)), \

([DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)([DT\_INST\_PORT\_BY\_ID](#gaf3427020d7d560c5da3df0f553988f71)(inst, pid), endpoint)))

[DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)

#define DT\_NODE\_EXISTS(node\_id)

Does a node identifier refer to a node?

**Definition** devicetree.h:3644

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)

#define DT\_CHILD(node\_id, child)

Get a node identifier for a child node.

**Definition** devicetree.h:436

[DT\_INST\_PORT\_BY\_ID](#gaf3427020d7d560c5da3df0f553988f71)

#define DT\_INST\_PORT\_BY\_ID(inst, pid)

Get a port node from its id.

**Definition** port-endpoint.h:87

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Get an endpoint node from its id and its parent port id.

Given a device instance number, a port ID and an endpoint ID, return the endpoint node. It handles various ways of how a port and an endpoint could be defined as described in [DT\_INST\_PORT\_BY\_ID](#gaf3427020d7d560c5da3df0f553988f71) and below.

Example usage with [DT\_INST\_ENDPOINT\_BY\_ID()](#ga0d2315ddc63c986da0e90177e8d8eab8) to get the `endpoint` or `endpoint@0` node:

[DT\_INST\_ENDPOINT\_BY\_ID](#ga0d2315ddc63c986da0e90177e8d8eab8)(inst, 0, 0)

[DT\_INST\_ENDPOINT\_BY\_ID](#ga0d2315ddc63c986da0e90177e8d8eab8)

#define DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid)

Get an endpoint node from its id and its parent port id.

**Definition** port-endpoint.h:163

Example devicetree fragment:

&device {

port {

endpoint {

};

};

};

&device {

port {

#address-cells = <1>;

#size-cells = <0>;

endpoint@0 {

reg = <0x0>;

};

};

};

&device {

ports {

#address-cells = <1>;

#size-cells = <0>;

port@0 {

reg = <0x0>;

#address-cells = <1>;

#size-cells = <0>;

endpoint@0 {

reg = <0x0>;

};

};

};

};

Parameters
:   | inst | instance number |
    | --- | --- |
    | pid | port ID |
    | eid | endpoint ID |

Returns
:   endpoint node associated with `eid` and `pid`

## [◆ ](#gaf3427020d7d560c5da3df0f553988f71)DT\_INST\_PORT\_BY\_ID

| #define DT\_INST\_PORT\_BY\_ID | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pid* ) |

`#include <[port-endpoint.h](port-endpoint_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)(\_DT\_INST\_PORT\_BY\_ID(inst, pid)), \

(\_DT\_INST\_PORT\_BY\_ID(inst, pid)), ([DT\_INST\_CHILD](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)(inst, port)))

[DT\_INST\_CHILD](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)

#define DT\_INST\_CHILD(inst, child)

Get a node identifier for a child node of DT\_DRV\_INST(inst).

**Definition** devicetree.h:3938

Get a port node from its id.

Given a device instance number, return a port node specified by its ID. It handles various ways of how a port could be defined.

Example usage with [DT\_INST\_PORT\_BY\_ID()](#gaf3427020d7d560c5da3df0f553988f71) to get the `port@0` or `port` node:

[DT\_INST\_PORT\_BY\_ID](#gaf3427020d7d560c5da3df0f553988f71)(inst, 0)

Example devicetree fragment:

&device {

ports {

#address-cells = <1>;

#size-cells = <0>;

port@0 {

reg = <0x0>;

};

};

};

&device {

#address-cells = <1>;

#size-cells = <0>;

port@0 {

reg = <0x0>;

};

};

&device {

port {

};

};

Parameters
:   | inst | instance number |
    | --- | --- |
    | pid | port ID |

Returns
:   port node associated with `pid`

## [◆ ](#ga37c2b0183196f513fc2222ba5fbe30d7)DT\_NODE\_BY\_ENDPOINT

| #define DT\_NODE\_BY\_ENDPOINT | ( |  | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[port-endpoint.h](port-endpoint_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)([DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)([DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(ep)), ports)), \

([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)([DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(ep))), ([DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(ep)))

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:374

[DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)

#define DT\_GPARENT(node\_id)

Get a node identifier for a grandparent node.

**Definition** devicetree.h:399

Get the device node from its endpoint node.

Given an endpoint node id, return its device node id. This handles various ways of how a port and an endpoint could be defined as described in [DT\_NODE\_BY\_ENDPOINT](#ga37c2b0183196f513fc2222ba5fbe30d7).

Example usage with [DT\_NODE\_BY\_ENDPOINT()](#ga37c2b0183196f513fc2222ba5fbe30d7) to get the `&device` node from its `ep0` node:

[DT\_NODE\_BY\_ENDPOINT](#ga37c2b0183196f513fc2222ba5fbe30d7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(ep0))

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[DT\_NODE\_BY\_ENDPOINT](#ga37c2b0183196f513fc2222ba5fbe30d7)

#define DT\_NODE\_BY\_ENDPOINT(ep)

Get the device node from its endpoint node.

**Definition** port-endpoint.h:215

Example devicetree fragment:

&device {

port {

#address-cells = <1>;

#size-cells = <0>;

ep0: endpoint@0 {

reg = <0x0>;

};

};

};

&device {

ports {

#address-cells = <1>;

#size-cells = <0>;

port@0 {

reg = <0x0>;

#address-cells = <1>;

#size-cells = <0>;

ep0: endpoint@0 {

reg = <0x0>;

};

};

};

};

Parameters
:   | ep | endpoint node |
    | --- | --- |

Returns
:   device node associated with `ep`

## [◆ ](#gaf1261a1a110fc0b164e6eafbaf885f7d)DT\_NODE\_REMOTE\_DEVICE

| #define DT\_NODE\_REMOTE\_DEVICE | ( |  | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[port-endpoint.h](port-endpoint_8h.md)>`

**Value:**

[DT\_NODE\_BY\_ENDPOINT](#ga37c2b0183196f513fc2222ba5fbe30d7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)([DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)(ep, remote\_endpoint\_label)))

[DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)

#define DT\_STRING\_TOKEN(node\_id, prop)

Get a string property's value as a token.

**Definition** devicetree.h:1116

Get the remote device node from a local endpoint node.

Given an endpoint node id, return the remote device node that connects to this device via this local endpoint. This handles various ways of how a port and an endpoint could be defined as described in [DT\_INST\_PORT\_BY\_ID](#gaf3427020d7d560c5da3df0f553988f71) and [DT\_INST\_ENDPOINT\_BY\_ID](#ga0d2315ddc63c986da0e90177e8d8eab8).

Example usage with [DT\_NODE\_REMOTE\_DEVICE()](#gaf1261a1a110fc0b164e6eafbaf885f7d) to get the remote device node `&device1` from the local endpoint `endpoint@0` node of the device `&device0` node:

[DT\_NODE\_REMOTE\_DEVICE](#gaf1261a1a110fc0b164e6eafbaf885f7d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(device0\_ep\_out))

[DT\_NODE\_REMOTE\_DEVICE](#gaf1261a1a110fc0b164e6eafbaf885f7d)

#define DT\_NODE\_REMOTE\_DEVICE(ep)

Get the remote device node from a local endpoint node.

**Definition** port-endpoint.h:264

Example devicetree fragment:

&device0 {

port {

#address-cells = <1>;

#size-cells = <0>;

device0\_ep\_out: endpoint@0 {

reg = <0x0>;

remote-endpoint-label = "device1\_ep\_in";

};

};

};

&device1 {

ports {

#address-cells = <1>;

#size-cells = <0>;

port@0 {

reg = <0x0>;

device1\_ep\_in: endpoint {

remote-endpoint-label = "device0\_ep\_out";

};

};

};

};

Parameters
:   | ep | endpoint node |
    | --- | --- |

Returns
:   remote device node that connects to this device via `ep`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
