---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__l2cap__chan__ops.html
original_path: doxygen/html/structbt__l2cap__chan__ops.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_chan\_ops Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

L2CAP Channel operations structure.
[More...](#details)

`#include <[l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#a3a4dd75a11c9867adcade6d288dec2de) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel connected callback. |
| void(\* | [disconnected](#a2e5fcc77a5174de6e3933bb6a14e4ad3) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel disconnected callback. |
| void(\* | [encrypt\_change](#a12f3290f9bd04fb5fe562c620dff6984) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_status) |
|  | Channel encrypt\_change callback. |
| struct [net\_buf](structnet__buf.md) \*(\* | [alloc\_seg](#abb165dbe118dfbb3577d3e56a00a5735) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel alloc\_seg callback. |
| struct [net\_buf](structnet__buf.md) \*(\* | [alloc\_buf](#ab973539dd8b5e3ab115042a03362f141) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel alloc\_buf callback. |
| int(\* | [recv](#a0ab419d3c52c08e0dfda236466d7cadd) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Channel recv callback. |
| void(\* | [sent](#a770c09f3fb10c9d1e069333d22803d1a) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel sent callback. |
| void(\* | [status](#a4be7fadf07368750cc33cf034d3073e7) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*status) |
|  | Channel status callback. |
| void(\* | [released](#a6d974d0e472626cb1e5cd898a3dcbca6) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| void(\* | [reconfigured](#afba426353897bc3a57c936a98acab839) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel reconfigured callback. |
| void(\* | [seg\_recv](#a7759a713038d74748952d5f2eb712429) )(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sdu\_len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) seg\_offset, struct [net\_buf\_simple](structnet__buf__simple.md) \*seg) |
|  | Handle L2CAP segments directly. |

## Detailed Description

L2CAP Channel operations structure.

The object has to stay valid and constant for the lifetime of the channel.

## Field Documentation

## [◆ ](#ab973539dd8b5e3ab115042a03362f141)alloc\_buf

| struct [net\_buf](structnet__buf.md) \*(\* bt\_l2cap\_chan\_ops::alloc\_buf) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

Channel alloc\_buf callback.

If this callback is provided the channel will use it to allocate buffers to store incoming data. Channels that requires segmentation must set this callback. If the application has not set a callback the L2CAP SDU MTU will be truncated to [BT\_L2CAP\_SDU\_RX\_MTU](group__bt__l2cap.md#ga13b93a8f09157fbcf739fa4949840efe "BT_L2CAP_SDU_RX_MTU").

Parameters
:   | chan | The channel requesting a buffer. |
    | --- | --- |

Returns
:   Allocated buffer.

## [◆ ](#abb165dbe118dfbb3577d3e56a00a5735)alloc\_seg

| struct [net\_buf](structnet__buf.md) \*(\* bt\_l2cap\_chan\_ops::alloc\_seg) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

Channel alloc\_seg callback.

If this callback is provided the channel will use it to allocate buffers to store segments. This avoids wasting big SDU buffers with potentially much smaller PDUs. If this callback is supplied, it must return a valid buffer.

Parameters
:   | chan | The channel requesting a buffer. |
    | --- | --- |

Returns
:   Allocated buffer.

## [◆ ](#a3a4dd75a11c9867adcade6d288dec2de)connected

| void(\* bt\_l2cap\_chan\_ops::connected) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

Channel connected callback.

If this callback is provided it will be called whenever the connection completes.

Parameters
:   | chan | The channel that has been connected |
    | --- | --- |

## [◆ ](#a2e5fcc77a5174de6e3933bb6a14e4ad3)disconnected

| void(\* bt\_l2cap\_chan\_ops::disconnected) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

Channel disconnected callback.

If this callback is provided it will be called whenever the channel is disconnected, including when a connection gets rejected.

Parameters
:   | chan | The channel that has been Disconnected |
    | --- | --- |

## [◆ ](#a12f3290f9bd04fb5fe562c620dff6984)encrypt\_change

| void(\* bt\_l2cap\_chan\_ops::encrypt\_change) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_status) |
| --- |

Channel encrypt\_change callback.

If this callback is provided it will be called whenever the security level changed (indirectly link encryption done) or authentication procedure fails. In both cases security initiator and responder got the final status (HCI status) passed by related to encryption and authentication events from local host's controller.

Parameters
:   | chan | The channel which has made encryption status changed. |
    | --- | --- |
    | [status](#a4be7fadf07368750cc33cf034d3073e7) | HCI status of performed security procedure caused by channel security requirements. The value is populated by HCI layer and set to 0 when success and to non-zero (reference to HCI Error Codes) when security/authentication failed. |

## [◆ ](#afba426353897bc3a57c936a98acab839)reconfigured

| void(\* bt\_l2cap\_chan\_ops::reconfigured) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

Channel reconfigured callback.

If this callback is provided it will be called whenever peer or local device requested reconfiguration. Application may check updated MTU and MPS values by inspecting chan->le endpoints.

Parameters
:   | chan | The channel which was reconfigured |
    | --- | --- |

## [◆ ](#a0ab419d3c52c08e0dfda236466d7cadd)recv

| int(\* bt\_l2cap\_chan\_ops::recv) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

Channel recv callback.

Parameters
:   | chan | The channel receiving data. |
    | --- | --- |
    | buf | Buffer containing incoming data. |

Note
:   This callback is mandatory, unless `CONFIG_BT_L2CAP_SEG_RECV` is enabled and seg\_recv is supplied.

If the application returns `-EINPROGRESS`, the application takes ownership of the reference in `buf`. (I.e. This pointer value can simply be given to [bt\_l2cap\_chan\_recv\_complete](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf "bt_l2cap_chan_recv_complete") without any calls [net\_buf\_ref](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f "net_buf_ref") or [net\_buf\_unref](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273 "net_buf_unref").)

Returns
:   0 in case of success or negative value in case of error.
:   -EINPROGRESS in case where user has to confirm once the data has been processed by calling [bt\_l2cap\_chan\_recv\_complete](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf "bt_l2cap_chan_recv_complete") passing back the buffer received with its original user\_data which contains the number of segments/credits used by the packet.

## [◆ ](#a6d974d0e472626cb1e5cd898a3dcbca6)released

| void(\* bt\_l2cap\_chan\_ops::released) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

## [◆ ](#a7759a713038d74748952d5f2eb712429)seg\_recv

| void(\* bt\_l2cap\_chan\_ops::seg\_recv) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sdu\_len, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) seg\_offset, struct [net\_buf\_simple](structnet__buf__simple.md) \*seg) |
| --- |

Handle L2CAP segments directly.

This is an alternative to [bt\_l2cap\_chan\_ops::recv](#a0ab419d3c52c08e0dfda236466d7cadd). They cannot be used together.

This is called immediately for each received segment.

Unlike with [bt\_l2cap\_chan\_ops::recv](#a0ab419d3c52c08e0dfda236466d7cadd), flow control is explicit. Each time this handler is invoked, the remote has permanently used up one credit. Use [bt\_l2cap\_chan\_give\_credits](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6 "bt_l2cap_chan_give_credits") to give credits.

The start of an SDU is marked by seg\_offset == 0. The end of an SDU is marked by seg\_offset + seg->len == sdu\_len.

The stack guarantees that:

- The sender had the credit.
- The SDU length does not exceed MTU.
- The segment length does not exceed MPS.

Additionally, the L2CAP protocol is such that:

- Segments come in order.
- SDUs cannot be interleaved or aborted halfway.

Note
:   With this alternative API, the application is responsible for setting the RX MTU and MPS. The MPS must not exceed [BT\_L2CAP\_RX\_MTU](group__bt__l2cap.md#ga6e458a1758e5012755f3b97f8348c966 "BT_L2CAP_RX_MTU").

Parameters
:   | chan | The receiving channel. |
    | --- | --- |
    | sdu\_len | Byte length of the SDU this segment is part of. |
    | seg\_offset | The byte offset of this segment in the SDU. |
    | seg | The segment payload. |

## [◆ ](#a770c09f3fb10c9d1e069333d22803d1a)sent

| void(\* bt\_l2cap\_chan\_ops::sent) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

Channel sent callback.

This callback will be called once the controller marks the SDU as completed. When the controller does so is implementation dependent. It could be after the SDU is enqueued for transmission, or after it is sent on air.

Parameters
:   | chan | The channel which has sent data. |
    | --- | --- |

## [◆ ](#a4be7fadf07368750cc33cf034d3073e7)status

| void(\* bt\_l2cap\_chan\_ops::status) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*status) |
| --- |

Channel status callback.

If this callback is provided it will be called whenever the channel status changes.

Parameters
:   | chan | The channel which status changed |
    | --- | --- |
    | [status](#a4be7fadf07368750cc33cf034d3073e7) | The channel status |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
