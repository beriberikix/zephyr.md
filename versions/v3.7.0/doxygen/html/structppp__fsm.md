---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structppp__fsm.html
original_path: doxygen/html/structppp__fsm.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp\_fsm Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PPP L2/driver Support Functions](group__ppp.md)

Generic PPP Finite State Machine.
[More...](#details)

`#include <[ppp.h](net_2ppp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work\_delayable](structk__work__delayable.md) | [timer](#ae033ee41d66ec568dc4244115730114a) |
|  | Timeout timer. |
| struct { |  |
| int(\*   [config\_info\_ack](#a42bb4a40d88893d461d93202c4ad8e2a) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct         [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |  |
|  | Acknowledge Configuration Information. [More...](#a42bb4a40d88893d461d93202c4ad8e2a) |
| struct [net\_pkt](structnet__pkt.md) \*(\*   [config\_info\_add](#a5a3c96319ec906968701c3eb72ce3d24) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | Add Configuration Information. [More...](#a5a3c96319ec906968701c3eb72ce3d24) |
| int(\*   [config\_info\_len](#a099cc834fc5e2d062ee4410a1de729c2) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | Length of Configuration Information. [More...](#a099cc834fc5e2d062ee4410a1de729c2) |
| int(\*   [config\_info\_nack](#ad0967edee7fee72368732876ca6bc5e7) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct         [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,         [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) rejected) |  |
|  | Negative Acknowledge Configuration Information. [More...](#ad0967edee7fee72368732876ca6bc5e7) |
| int(\*   [config\_info\_req](#ab430e0240f35718f6eaf8f9052a4edde) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct         [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length,         struct [net\_pkt](structnet__pkt.md) \*ret\_pkt) |  |
|  | Request peer's Configuration Information. [More...](#ab430e0240f35718f6eaf8f9052a4edde) |
| int(\*   [config\_info\_rej](#a90dad2f780b4573559c76e6a67e44f4c) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct         [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |  |
|  | Reject Configuration Information. [More...](#a90dad2f780b4573559c76e6a67e44f4c) |
| void(\*   [config\_info\_reset](#afb0296b0d8e9b60594781cfd5f8acee3) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | Reset Configuration Information. [More...](#afb0296b0d8e9b60594781cfd5f8acee3) |
| void(\*   [up](#aa1ca37605ab7934c16a5260d531efa00) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | FSM goes to OPENED state. [More...](#aa1ca37605ab7934c16a5260d531efa00) |
| void(\*   [down](#a2ba52396156dd1ec63d67dc6ae0a2d5a) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | FSM leaves OPENED state. [More...](#a2ba52396156dd1ec63d67dc6ae0a2d5a) |
| void(\*   [starting](#ad7f2d5d09acb298d29ebc60b4f748478) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | Starting this protocol. [More...](#ad7f2d5d09acb298d29ebc60b4f748478) |
| void(\*   [finished](#aecdcdfa2f7264c7b1b2202a23327fa3b) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | Quitting this protocol. [More...](#aecdcdfa2f7264c7b1b2202a23327fa3b) |
| void(\*   [proto\_reject](#ae4f68c11709ab03445b853c12c11c787) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | We received Protocol-Reject. [More...](#ae4f68c11709ab03445b853c12c11c787) |
| void(\*   [retransmit](#ae0c0b33d5e51a01a63b5afbf5012c0f5) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm) |  |
|  | Retransmit. [More...](#ae0c0b33d5e51a01a63b5afbf5012c0f5) |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\*   [proto\_extension](#aa302cfe79c73fe081d2642cf54d1d3cf) )(struct [ppp\_fsm](structppp__fsm.md) \*fsm, enum         ppp\_packet\_type code, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)         [id](#a844c8747b299d3614e5ccff892b45d5c), struct [net\_pkt](structnet__pkt.md) \*pkt) |  |
|  | Any code that is not understood by PPP is passed to this FSM for further processing. [More...](#aa302cfe79c73fe081d2642cf54d1d3cf) |
| } | [cb](#a0e3cd20db2e06d6d0e85478c013e36db) |
|  | FSM callbacks. |
| struct { |  |
| const struct ppp\_my\_option\_info \*   [info](#a117a5df8fed62b57a59580a2513fc1c3) |  |
|  | Options information. [More...](#a117a5df8fed62b57a59580a2513fc1c3) |
| struct ppp\_my\_option\_data \*   [data](#a64330e89597eac2b8b841d0f95389473) |  |
|  | Options negotiation data. [More...](#a64330e89597eac2b8b841d0f95389473) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [count](#a7e125f9011a9377d18dc523b1f84964f) |  |
|  | Number of negotiated options. [More...](#a7e125f9011a9377d18dc523b1f84964f) |
| } | [my\_options](#a39a7d8b02a0c905ea27565445295c4f2) |
|  | My options. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a489c2d992e03e126ba2d1bbfe7a71b85) |
|  | Option bits. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [retransmits](#a31d84f3fa6246bd70d664dbae6845c4b) |
|  | Number of re-transmissions left. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nack\_loops](#a0a0523fe16fe45a756615b62e8673828) |
|  | Number of NACK loops since last ACK. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [recv\_nack\_loops](#a55c0fe60eb84f33386ec90691ee0f707) |
|  | Number of NACKs received. |
| char | [terminate\_reason](#a054fd1e61e667072a552eadf54634ffc) [32] |
|  | Reason for closing protocol. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [protocol](#a2032a922d2e356155c5a4c86cf48ff3d) |
|  | PPP protocol number for this FSM. |
| enum ppp\_state | [state](#ab955d11b75231e94ec1613d5c8c027e1) |
|  | Current state of PPP link. |
| const char \* | [name](#a9192c71ef82436c519ac3b8ccd38a089) |
|  | Protocol/layer name of this FSM (for debugging). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a844c8747b299d3614e5ccff892b45d5c) |
|  | Current id. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [req\_id](#a8fe52ffe2a17c03ff0432e36c9d43578) |
|  | Current request id. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ack\_received](#a42777bc7c5f904cbac6bb0b16615fb02): 1 |
|  | Have received valid Ack, Nack or Reject to a Request. |

## Detailed Description

Generic PPP Finite State Machine.

## Field Documentation

## [◆ ](#a42777bc7c5f904cbac6bb0b16615fb02)ack\_received

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_fsm::ack\_received |
| --- |

Have received valid Ack, Nack or Reject to a Request.

## [◆ ](#a0e3cd20db2e06d6d0e85478c013e36db)[struct]

| struct { ... } ppp\_fsm::cb |
| --- |

FSM callbacks.

## [◆ ](#a42bb4a40d88893d461d93202c4ad8e2a)config\_info\_ack

| int(\* ppp\_fsm::config\_info\_ack) (struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
| --- |

Acknowledge Configuration Information.

## [◆ ](#a5a3c96319ec906968701c3eb72ce3d24)config\_info\_add

| struct [net\_pkt](structnet__pkt.md) \*(\* ppp\_fsm::config\_info\_add) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

Add Configuration Information.

## [◆ ](#a099cc834fc5e2d062ee4410a1de729c2)config\_info\_len

| int(\* ppp\_fsm::config\_info\_len) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

Length of Configuration Information.

## [◆ ](#ad0967edee7fee72368732876ca6bc5e7)config\_info\_nack

| int(\* ppp\_fsm::config\_info\_nack) (struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) rejected) |
| --- |

Negative Acknowledge Configuration Information.

## [◆ ](#a90dad2f780b4573559c76e6a67e44f4c)config\_info\_rej

| int(\* ppp\_fsm::config\_info\_rej) (struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
| --- |

Reject Configuration Information.

## [◆ ](#ab430e0240f35718f6eaf8f9052a4edde)config\_info\_req

| int(\* ppp\_fsm::config\_info\_req) (struct [ppp\_fsm](structppp__fsm.md) \*fsm, struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, struct [net\_pkt](structnet__pkt.md) \*ret\_pkt) |
| --- |

Request peer's Configuration Information.

## [◆ ](#afb0296b0d8e9b60594781cfd5f8acee3)config\_info\_reset

| void(\* ppp\_fsm::config\_info\_reset) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

Reset Configuration Information.

## [◆ ](#a7e125f9011a9377d18dc523b1f84964f)count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ppp\_fsm::count |
| --- |

Number of negotiated options.

## [◆ ](#a64330e89597eac2b8b841d0f95389473)data

| struct ppp\_my\_option\_data\* ppp\_fsm::data |
| --- |

Options negotiation data.

## [◆ ](#a2ba52396156dd1ec63d67dc6ae0a2d5a)down

| void(\* ppp\_fsm::down) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

FSM leaves OPENED state.

## [◆ ](#aecdcdfa2f7264c7b1b2202a23327fa3b)finished

| void(\* ppp\_fsm::finished) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

Quitting this protocol.

## [◆ ](#a489c2d992e03e126ba2d1bbfe7a71b85)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ppp\_fsm::flags |
| --- |

Option bits.

## [◆ ](#a844c8747b299d3614e5ccff892b45d5c)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_fsm::id |
| --- |

Current id.

## [◆ ](#a117a5df8fed62b57a59580a2513fc1c3)info

| const struct ppp\_my\_option\_info\* ppp\_fsm::info |
| --- |

Options information.

## [◆ ](#a39a7d8b02a0c905ea27565445295c4f2)[struct]

| struct { ... } ppp\_fsm::my\_options |
| --- |

My options.

## [◆ ](#a0a0523fe16fe45a756615b62e8673828)nack\_loops

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ppp\_fsm::nack\_loops |
| --- |

Number of NACK loops since last ACK.

## [◆ ](#a9192c71ef82436c519ac3b8ccd38a089)name

| const char\* ppp\_fsm::name |
| --- |

Protocol/layer name of this FSM (for debugging).

## [◆ ](#aa302cfe79c73fe081d2642cf54d1d3cf)proto\_extension

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* ppp\_fsm::proto\_extension) (struct [ppp\_fsm](structppp__fsm.md) \*fsm, enum ppp\_packet\_type code, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](#a844c8747b299d3614e5ccff892b45d5c), struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Any code that is not understood by PPP is passed to this FSM for further processing.

## [◆ ](#ae4f68c11709ab03445b853c12c11c787)proto\_reject

| void(\* ppp\_fsm::proto\_reject) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

We received Protocol-Reject.

## [◆ ](#a2032a922d2e356155c5a4c86cf48ff3d)protocol

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ppp\_fsm::protocol |
| --- |

PPP protocol number for this FSM.

## [◆ ](#a55c0fe60eb84f33386ec90691ee0f707)recv\_nack\_loops

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ppp\_fsm::recv\_nack\_loops |
| --- |

Number of NACKs received.

## [◆ ](#a8fe52ffe2a17c03ff0432e36c9d43578)req\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_fsm::req\_id |
| --- |

Current request id.

## [◆ ](#ae0c0b33d5e51a01a63b5afbf5012c0f5)retransmit

| void(\* ppp\_fsm::retransmit) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

Retransmit.

## [◆ ](#a31d84f3fa6246bd70d664dbae6845c4b)retransmits

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ppp\_fsm::retransmits |
| --- |

Number of re-transmissions left.

## [◆ ](#ad7f2d5d09acb298d29ebc60b4f748478)starting

| void(\* ppp\_fsm::starting) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

Starting this protocol.

## [◆ ](#ab955d11b75231e94ec1613d5c8c027e1)state

| enum ppp\_state ppp\_fsm::state |
| --- |

Current state of PPP link.

## [◆ ](#a054fd1e61e667072a552eadf54634ffc)terminate\_reason

| char ppp\_fsm::terminate\_reason[32] |
| --- |

Reason for closing protocol.

## [◆ ](#ae033ee41d66ec568dc4244115730114a)timer

| struct [k\_work\_delayable](structk__work__delayable.md) ppp\_fsm::timer |
| --- |

Timeout timer.

## [◆ ](#aa1ca37605ab7934c16a5260d531efa00)up

| void(\* ppp\_fsm::up) (struct [ppp\_fsm](structppp__fsm.md) \*fsm) |
| --- |

FSM goes to OPENED state.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ppp.h](net_2ppp_8h_source.md)

- [ppp\_fsm](structppp__fsm.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
