---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__rtio.html
original_path: doxygen/html/group__rtio.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTIO

[Operating System Services](group__os__services.md)

RTIO.
[More...](#details)

| Topics | |
| --- | --- |
|  | [RTIO CQE Flags](group__rtio__cqe__flags.md) |
|  | RTIO CQE Flags. |
|  | [RTIO Priorities](group__rtio__sqe__prio.md) |
|  | RTIO Predefined Priorities. |
|  | [RTIO SQE Flags](group__rtio__sqe__flags.md) |
|  | RTIO SQE Flags. |

| Data Structures | |
| --- | --- |
| struct | [rtio\_sqe](structrtio__sqe.md) |
|  | A submission queue event. [More...](structrtio__sqe.md#details) |
| struct | [rtio\_cqe](structrtio__cqe.md) |
|  | A completion queue event. [More...](structrtio__cqe.md#details) |
| struct | [rtio\_sqe\_pool](structrtio__sqe__pool.md) |
| struct | [rtio\_cqe\_pool](structrtio__cqe__pool.md) |
| struct | [rtio](structrtio.md) |
|  | An RTIO context containing what can be viewed as a pair of queues. [More...](structrtio.md#details) |
| struct | [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) |
|  | Compute the mempool block index for a given pointer. [More...](structrtio__iodev__sqe.md#details) |
| struct | [rtio\_iodev\_api](structrtio__iodev__api.md) |
|  | API that an RTIO IO device should implement. [More...](structrtio__iodev__api.md#details) |
| struct | [rtio\_iodev](structrtio__iodev.md) |
|  | An IO device with a function table for submitting requests. [More...](structrtio__iodev.md#details) |

| Macros | |
| --- | --- |
| #define | [RTIO\_IODEV\_I2C\_STOP](#gaf923e862d2c6a3fbce5eb96781cf86d8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Equivalent to the I2C\_MSG\_STOP flag. |
| #define | [RTIO\_IODEV\_I2C\_RESTART](#gadba1c5eddeecc431000bd92054f55c3a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Equivalent to the I2C\_MSG\_RESTART flag. |
| #define | [RTIO\_IODEV\_I2C\_10\_BITS](#gaa0c3b047c7205d12775d8d38907119b9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Equivalent to the I2C\_MSG\_ADDR\_10\_BITS. |
| #define | [RTIO\_OP\_NOP](#gad5f073978f641413989d1c6b405d6c36)   0 |
|  | An operation that does nothing and will complete immediately. |
| #define | [RTIO\_OP\_RX](#gafeb05c351207cd1638fa78f6607e1a4a)   ([RTIO\_OP\_NOP](#gad5f073978f641413989d1c6b405d6c36)+1) |
|  | An operation that receives (reads). |
| #define | [RTIO\_OP\_TX](#ga8dcaef0cda159e16520a95543ff62827)   ([RTIO\_OP\_RX](#gafeb05c351207cd1638fa78f6607e1a4a)+1) |
|  | An operation that transmits (writes). |
| #define | [RTIO\_OP\_TINY\_TX](#ga6f95c0a5fbcc020a0d1102d3b08934bd)   ([RTIO\_OP\_TX](#ga8dcaef0cda159e16520a95543ff62827)+1) |
|  | An operation that transmits tiny writes by copying the data to write. |
| #define | [RTIO\_OP\_CALLBACK](#ga18e0ff7d44e4c33900106aefad0a8508)   ([RTIO\_OP\_TINY\_TX](#ga6f95c0a5fbcc020a0d1102d3b08934bd)+1) |
|  | An operation that calls a given function (callback). |
| #define | [RTIO\_OP\_TXRX](#ga9f0e70f5a28be65a8ed67c0257a72692)   ([RTIO\_OP\_CALLBACK](#ga18e0ff7d44e4c33900106aefad0a8508)+1) |
|  | An operation that transceives (reads and writes simultaneously). |
| #define | [RTIO\_OP\_I2C\_RECOVER](#ga3b4f9b1ee1612290323161ecc16e0859)   ([RTIO\_OP\_TXRX](#ga9f0e70f5a28be65a8ed67c0257a72692)+1) |
|  | An operation to recover I2C buses. |
| #define | [RTIO\_OP\_I2C\_CONFIGURE](#gad987be3acfe406b11419c7e8cd068cf5)   ([RTIO\_OP\_I2C\_RECOVER](#ga3b4f9b1ee1612290323161ecc16e0859)+1) |
|  | An operation to configure I2C buses. |
| #define | [RTIO\_IODEV\_DEFINE](#gaae51e2a679d37bc1cfba79961688c406)(name, iodev\_api, iodev\_data) |
|  | Statically define and initialize an RTIO IODev. |
| #define | [RTIO\_BMEM](#ga2437af5061e078950d4a55211d9a902f)   [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_USERSPACE, ([K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([rtio\_partition](#ga86a38086dd85150ab6e479d73db1c6d1)) static), (static)) |
|  | Allocate to bss if available. |
| #define | [RTIO\_DMEM](#ga3b569c01b71e126cff852df50e98fd69)   [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_USERSPACE, ([K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([rtio\_partition](#ga86a38086dd85150ab6e479d73db1c6d1)) static), (static)) |
|  | Allocate as initialized memory if available. |
| #define | [RTIO\_DEFINE](#ga338df088eabf3b8f7fefb4ac517b21d4)(name, sq\_sz, cq\_sz) |
|  | Statically define and initialize an RTIO context. |
| #define | [RTIO\_DEFINE\_WITH\_MEMPOOL](#gae4c2a9384a9ae4ed16dff914b1184ca8)(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign) |
|  | Statically define and initialize an RTIO context. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rtio\_callback\_t](#gad1dbd690e6cf88d7c788436dd04d1a00)) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqe, void \*arg0) |
|  | Callback signature for RTIO\_OP\_CALLBACK. |

| Functions | |
| --- | --- |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [rtio\_mempool\_block\_size](#ga4213be028b0a1264daaa0d30c4c2d089) (const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Get the mempool block size of the RTIO context. |
| static void | [rtio\_sqe\_prep\_nop](#ga599ee43fdf35e1cf895cbbe9272e4c50) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, void \*userdata) |
|  | Prepare a nop (no op) submission. |
| static void | [rtio\_sqe\_prep\_read](#ga89c7cc2494e3dda50737f78f1a1376cf) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, void \*userdata) |
|  | Prepare a read op submission. |
| static void | [rtio\_sqe\_prep\_read\_with\_pool](#ga15c1f623658d27d300d1a31a6f3d6b9d) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, void \*userdata) |
|  | Prepare a read op submission with context's mempool. |
| static void | [rtio\_sqe\_prep\_read\_multishot](#ga9803aa829f8c0eeee746ea7d872c20cc) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, void \*userdata) |
| static void | [rtio\_sqe\_prep\_write](#ga7f7856d1f4fd1d8c4f6eebcccfe77701) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, void \*userdata) |
|  | Prepare a write op submission. |
| static void | [rtio\_sqe\_prep\_tiny\_write](#ga31be14ece09e061a8d42ca8f2395286a) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tiny\_write\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tiny\_write\_len, void \*userdata) |
|  | Prepare a tiny write op submission. |
| static void | [rtio\_sqe\_prep\_callback](#ga9d0dd7d0e2e3d281092f2350d6e1713e) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, [rtio\_callback\_t](#gad1dbd690e6cf88d7c788436dd04d1a00) callback, void \*arg0, void \*userdata) |
|  | Prepare a callback op submission. |
| static void | [rtio\_sqe\_prep\_callback\_no\_cqe](#gae87be354087d038953dae07c7f9cd3b0) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, [rtio\_callback\_t](#gad1dbd690e6cf88d7c788436dd04d1a00) callback, void \*arg0, void \*userdata) |
|  | Prepare a callback op submission that does not create a CQE. |
| static void | [rtio\_sqe\_prep\_transceive](#gab9b605dcbb01d21c88f9ae70588ea3b5) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len, void \*userdata) |
|  | Prepare a transceive op submission. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_sqe\_pool\_alloc](#gae5fb03fc8f3a4a774f476ff552999bfc) (struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool) |
| static void | [rtio\_sqe\_pool\_free](#gac776aea3692cfd77aa5bf675a9e9ed02) (struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_pool\_alloc](#ga8497170f55af1d11d717e919f61806f5) (struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool) |
| static void | [rtio\_cqe\_pool\_free](#ga23c0c5d4b551858eabe057ecb8a28d12) (struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool, struct [rtio\_cqe](structrtio__cqe.md) \*cqe) |
| static int | [rtio\_block\_pool\_alloc](#ga7f14b99fc1dd0697309e7f71a270f5fb) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_sz, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_sz, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len) |
| static void | [rtio\_block\_pool\_free](#gafca7732926a9a7c080e3cb16e5f16108) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rtio\_sqe\_acquirable](#ga1f4fb7bccbaae08a94387e4b11275a78) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Count of acquirable submission queue events. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_txn\_next](#gaef904eb6a8810d8c3ea537c4d6edbee5) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Get the next sqe in the transaction. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_chain\_next](#gada1e3abf92a46e376138435debc8baf4) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Get the next sqe in the chain. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_iodev\_sqe\_next](#gae690e3dc0fc40dda57257b2eed432719) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Get the next sqe in the chain or transaction. |
| static struct [rtio\_sqe](structrtio__sqe.md) \* | [rtio\_sqe\_acquire](#ga8b47c954d15a334621def53acceb6799) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Acquire a single submission queue event if available. |
| static void | [rtio\_sqe\_drop\_all](#ga9486fb7b50e8d2409a50da235203536b) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Drop all previously acquired sqe. |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_acquire](#gad848646651fdf3649b882e5268f72a3c) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Acquire a complete queue event if available. |
| static void | [rtio\_cqe\_produce](#ga6f55202adeca60aed0343a7a0dcab071) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe) |
|  | Produce a complete queue event if available. |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_consume](#gae562cf241911804cdb9f4e3a73b53df4) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Consume a single completion queue event if available. |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_consume\_block](#gaf617d05d9b59ce1f1d0697617ef6f249) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Wait for and consume a single completion queue event. |
| static void | [rtio\_cqe\_release](#gaa0799a5f8ad98425d385a07c5d27d9cb) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe) |
|  | Release consumed completion queue event. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rtio\_cqe\_compute\_flags](#ga75661c8c6c94a0ac6254cec674b478c8) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Compute the CQE flags from the [rtio\_iodev\_sqe](structrtio__iodev__sqe.md "Compute the mempool block index for a given pointer.") entry. |
| int | [rtio\_cqe\_get\_mempool\_buffer](#gaedbf9386a36ed99baa290ef6c318ded1) (const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len) |
|  | Retrieve the mempool buffer that was allocated for the CQE. |
| void | [rtio\_executor\_submit](#gaf191153e83de72ddefb998daad02fa16) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
| void | [rtio\_executor\_ok](#ga7e2ebd9abaf585207bc5b99c5d815c6a) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
| void | [rtio\_executor\_err](#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
| static void | [rtio\_iodev\_sqe\_ok](#gacb1d2ffa2b07418d8a8aa319bd4336ab) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
|  | Inform the executor of a submission completion with success. |
| static void | [rtio\_iodev\_sqe\_err](#gaada07aa6acefa548743b525225fa482f) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
|  | Inform the executor of a submissions completion with error. |
| static void | [rtio\_cqe\_submit](#ga4abc221d5a90ab882000a72caa0ebd0f) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), int result, void \*userdata, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Submit a completion queue event with a given result and userdata. |
| static int | [rtio\_sqe\_rx\_buf](#gaab6843e2038d00a8354f57d7e2ffcf7e) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_buf\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_buf\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len) |
|  | Get the buffer associate with the RX submission. |
| void | [rtio\_release\_buffer](#ga6530bf56ccbab046a362a6448f941609) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len) |
|  | Release memory that was allocated by the RTIO's memory pool. |
| static void | [rtio\_access\_grant](#ga9da42c98546930575525f0f92710f9e4) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [k\_thread](structk__thread.md) \*t) |
|  | Grant access to an RTIO context to a user thread. |
| int | [rtio\_sqe\_cancel](#gac01252e55d2848b38c0ed77b71d600a7) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe) |
|  | Attempt to cancel an SQE. |
| int | [rtio\_sqe\_copy\_in\_get\_handles](#ga830863e6c8d9b96f4c473a038cab8f8c) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, struct [rtio\_sqe](structrtio__sqe.md) \*\*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sqe\_count) |
|  | Copy an array of SQEs into the queue and get resulting handles back. |
| static int | [rtio\_sqe\_copy\_in](#ga65e351af0a16dcf504a51ef4eb9316c7) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sqe\_count) |
|  | Copy an array of SQEs into the queue. |
| int | [rtio\_cqe\_copy\_out](#ga98b2bbef95aea342a9b86a9775dd5c3b) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cqe\_count, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Copy an array of CQEs from the queue. |
| int | [rtio\_submit](#gafee27c64a4a4989c4eb774addde8eb2e) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count) |
|  | Submit I/O requests to the underlying executor. |

| Variables | |
| --- | --- |
| struct [k\_mem\_partition](structk__mem__partition.md) | [rtio\_partition](#ga86a38086dd85150ab6e479d73db1c6d1) |
|  | The memory partition associated with all RTIO context information. |

## Detailed Description

RTIO.

Since
:   3.2

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga2437af5061e078950d4a55211d9a902f)RTIO\_BMEM

| #define RTIO\_BMEM   [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_USERSPACE, ([K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([rtio\_partition](#ga86a38086dd85150ab6e479d73db1c6d1)) static), (static)) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Allocate to bss if available.

If CONFIG\_USERSPACE is selected, allocate to the rtio\_partition bss. Maps to: [K\_APP\_BMEM(rtio\_partition)](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881 "Place data in a partition's bss section.") static

If CONFIG\_USERSPACE is disabled, allocate as plain static: static

## [◆ ](#ga338df088eabf3b8f7fefb4ac517b21d4)RTIO\_DEFINE

| #define RTIO\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *sq\_sz*, |
|  |  |  | *cq\_sz* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

Z\_RTIO\_SQE\_POOL\_DEFINE([CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(name, \_sqe\_pool), sq\_sz); \

Z\_RTIO\_CQE\_POOL\_DEFINE([CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(name, \_cqe\_pool), cq\_sz); \

Z\_RTIO\_DEFINE(name, &[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(name, \_sqe\_pool), \

&[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(name, \_cqe\_pool), NULL)

[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)

#define CONCAT(...)

Concatenate input arguments.

**Definition** util.h:311

Statically define and initialize an RTIO context.

Parameters
:   | name | Name of the RTIO |
    | --- | --- |
    | sq\_sz | Size of the submission queue entry pool |
    | cq\_sz | Size of the completion queue entry pool |

## [◆ ](#gae4c2a9384a9ae4ed16dff914b1184ca8)RTIO\_DEFINE\_WITH\_MEMPOOL

| #define RTIO\_DEFINE\_WITH\_MEMPOOL | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *sq\_sz*, |
|  |  |  | *cq\_sz*, |
|  |  |  | *num\_blks*, |
|  |  |  | *blk\_size*, |
|  |  |  | *balign* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

Z\_RTIO\_SQE\_POOL\_DEFINE(name##\_sqe\_pool, sq\_sz); \

Z\_RTIO\_CQE\_POOL\_DEFINE(name##\_cqe\_pool, cq\_sz); \

Z\_RTIO\_BLOCK\_POOL\_DEFINE(name##\_block\_pool, blk\_size, num\_blks, balign); \

Z\_RTIO\_DEFINE(name, &name##\_sqe\_pool, &name##\_cqe\_pool, &name##\_block\_pool)

Statically define and initialize an RTIO context.

Parameters
:   | name | Name of the RTIO |
    | --- | --- |
    | sq\_sz | Size of the submission queue, must be power of 2 |
    | cq\_sz | Size of the completion queue, must be power of 2 |
    | num\_blks | Number of blocks in the memory pool |
    | blk\_size | The number of bytes in each block |
    | balign | The block alignment |

## [◆ ](#ga3b569c01b71e126cff852df50e98fd69)RTIO\_DMEM

| #define RTIO\_DMEM   [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_USERSPACE, ([K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([rtio\_partition](#ga86a38086dd85150ab6e479d73db1c6d1)) static), (static)) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Allocate as initialized memory if available.

If CONFIG\_USERSPACE is selected, allocate to the rtio\_partition init. Maps to: [K\_APP\_DMEM(rtio\_partition)](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6 "Place data in a partition's data section.") static

If CONFIG\_USERSPACE is disabled, allocate as plain static: static

## [◆ ](#gaae51e2a679d37bc1cfba79961688c406)RTIO\_IODEV\_DEFINE

| #define RTIO\_IODEV\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *iodev\_api*, |
|  |  |  | *iodev\_data* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([rtio\_iodev](structrtio__iodev.md), name) = { \

.api = (iodev\_api), \

.data = (iodev\_data), \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:454

Statically define and initialize an RTIO IODev.

Parameters
:   | name | Name of the iodev |
    | --- | --- |
    | iodev\_api | Pointer to struct [rtio\_iodev\_api](structrtio__iodev__api.md "API that an RTIO IO device should implement.") |
    | iodev\_data | Data pointer |

## [◆ ](#gaa0c3b047c7205d12775d8d38907119b9)RTIO\_IODEV\_I2C\_10\_BITS

| #define RTIO\_IODEV\_I2C\_10\_BITS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Equivalent to the I2C\_MSG\_ADDR\_10\_BITS.

## [◆ ](#gadba1c5eddeecc431000bd92054f55c3a)RTIO\_IODEV\_I2C\_RESTART

| #define RTIO\_IODEV\_I2C\_RESTART   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Equivalent to the I2C\_MSG\_RESTART flag.

## [◆ ](#gaf923e862d2c6a3fbce5eb96781cf86d8)RTIO\_IODEV\_I2C\_STOP

| #define RTIO\_IODEV\_I2C\_STOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Equivalent to the I2C\_MSG\_STOP flag.

## [◆ ](#ga18e0ff7d44e4c33900106aefad0a8508)RTIO\_OP\_CALLBACK

| #define RTIO\_OP\_CALLBACK   ([RTIO\_OP\_TINY\_TX](#ga6f95c0a5fbcc020a0d1102d3b08934bd)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation that calls a given function (callback).

## [◆ ](#gad987be3acfe406b11419c7e8cd068cf5)RTIO\_OP\_I2C\_CONFIGURE

| #define RTIO\_OP\_I2C\_CONFIGURE   ([RTIO\_OP\_I2C\_RECOVER](#ga3b4f9b1ee1612290323161ecc16e0859)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation to configure I2C buses.

## [◆ ](#ga3b4f9b1ee1612290323161ecc16e0859)RTIO\_OP\_I2C\_RECOVER

| #define RTIO\_OP\_I2C\_RECOVER   ([RTIO\_OP\_TXRX](#ga9f0e70f5a28be65a8ed67c0257a72692)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation to recover I2C buses.

## [◆ ](#gad5f073978f641413989d1c6b405d6c36)RTIO\_OP\_NOP

| #define RTIO\_OP\_NOP   0 |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation that does nothing and will complete immediately.

## [◆ ](#gafeb05c351207cd1638fa78f6607e1a4a)RTIO\_OP\_RX

| #define RTIO\_OP\_RX   ([RTIO\_OP\_NOP](#gad5f073978f641413989d1c6b405d6c36)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation that receives (reads).

## [◆ ](#ga6f95c0a5fbcc020a0d1102d3b08934bd)RTIO\_OP\_TINY\_TX

| #define RTIO\_OP\_TINY\_TX   ([RTIO\_OP\_TX](#ga8dcaef0cda159e16520a95543ff62827)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation that transmits tiny writes by copying the data to write.

## [◆ ](#ga8dcaef0cda159e16520a95543ff62827)RTIO\_OP\_TX

| #define RTIO\_OP\_TX   ([RTIO\_OP\_RX](#gafeb05c351207cd1638fa78f6607e1a4a)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation that transmits (writes).

## [◆ ](#ga9f0e70f5a28be65a8ed67c0257a72692)RTIO\_OP\_TXRX

| #define RTIO\_OP\_TXRX   ([RTIO\_OP\_CALLBACK](#ga18e0ff7d44e4c33900106aefad0a8508)+1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

An operation that transceives (reads and writes simultaneously).

## Typedef Documentation

## [◆ ](#gad1dbd690e6cf88d7c788436dd04d1a00)rtio\_callback\_t

| typedef void(\* rtio\_callback\_t) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqe, void \*arg0) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Callback signature for RTIO\_OP\_CALLBACK.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context being used with the callback |
    | --- | --- |
    | sqe | Submission for the callback op |
    | arg0 | Argument option as part of the sqe |

## Function Documentation

## [◆ ](#ga9da42c98546930575525f0f92710f9e4)rtio\_access\_grant()

| | void rtio\_access\_grant | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | struct [k\_thread](structk__thread.md) \* | *t* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Grant access to an RTIO context to a user thread.

## [◆ ](#ga7f14b99fc1dd0697309e7f71a270f5fb)rtio\_block\_pool\_alloc()

| | int rtio\_block\_pool\_alloc | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *min\_sz*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_sz*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *buf\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#gafca7732926a9a7c080e3cb16e5f16108)rtio\_block\_pool\_free()

| | void rtio\_block\_pool\_free | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | void \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *buf\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#gada1e3abf92a46e376138435debc8baf4)rtio\_chain\_next()

| | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* rtio\_chain\_next | ( | const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Get the next sqe in the chain.

Parameters
:   | iodev\_sqe | Submission queue entry |
    | --- | --- |

Return values
:   | NULL | if current sqe is last in chain |
    | --- | --- |
    | struct | [rtio\_sqe](structrtio__sqe.md "A submission queue event.") \* if available |

## [◆ ](#gad848646651fdf3649b882e5268f72a3c)rtio\_cqe\_acquire()

| | struct [rtio\_cqe](structrtio__cqe.md) \* rtio\_cqe\_acquire | ( | struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Acquire a complete queue event if available.

## [◆ ](#ga75661c8c6c94a0ac6254cec674b478c8)rtio\_cqe\_compute\_flags()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rtio\_cqe\_compute\_flags | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Compute the CQE flags from the [rtio\_iodev\_sqe](structrtio__iodev__sqe.md "Compute the mempool block index for a given pointer.") entry.

Parameters
:   | iodev\_sqe | The SQE entry in question. |
    | --- | --- |

Returns
:   The value that should be set for the CQE's flags field.

## [◆ ](#gae562cf241911804cdb9f4e3a73b53df4)rtio\_cqe\_consume()

| | struct [rtio\_cqe](structrtio__cqe.md) \* rtio\_cqe\_consume | ( | struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Consume a single completion queue event if available.

If a completion queue event is returned rtio\_cq\_release(r) must be called at some point to release the cqe spot for the cqe producer.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |

Return values
:   | cqe | A valid completion queue event consumed from the completion queue |
    | --- | --- |
    | NULL | No completion queue event available |

## [◆ ](#gaf617d05d9b59ce1f1d0697617ef6f249)rtio\_cqe\_consume\_block()

| | struct [rtio\_cqe](structrtio__cqe.md) \* rtio\_cqe\_consume\_block | ( | struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Wait for and consume a single completion queue event.

If a completion queue event is returned rtio\_cq\_release(r) must be called at some point to release the cqe spot for the cqe producer.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |

Return values
:   | cqe | A valid completion queue event consumed from the completion queue |
    | --- | --- |

## [◆ ](#ga98b2bbef95aea342a9b86a9775dd5c3b)rtio\_cqe\_copy\_out()

| int rtio\_cqe\_copy\_out | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_cqe](structrtio__cqe.md) \* | *cqes*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *cqe\_count*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Copy an array of CQEs from the queue.

Copies from the RTIO context and its queue completion queue events, waiting for the given time period to gather the number of completions requested.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | cqes | Pointer to an array of SQEs |
    | cqe\_count | Count of sqes in array |
    | timeout | Timeout to wait for each completion event. Total wait time is potentially timeout\*cqe\_count at maximum. |

Return values
:   | copy\_count | Count of copied CQEs (0 to cqe\_count) |
    | --- | --- |

## [◆ ](#gaedbf9386a36ed99baa290ef6c318ded1)rtio\_cqe\_get\_mempool\_buffer()

| int rtio\_cqe\_get\_mempool\_buffer | ( | const struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_cqe](structrtio__cqe.md) \* | *cqe*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *buff*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *buff\_len* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Retrieve the mempool buffer that was allocated for the CQE.

If the RTIO context contains a memory pool, and the SQE was created by calling rtio\_sqe\_read\_with\_pool(), this function can be used to retrieve the memory associated with the read. Once processing is done, it should be released by calling [rtio\_release\_buffer()](#ga6530bf56ccbab046a362a6448f941609).

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- | --- |
    | [in] | cqe | The CQE handling the event. |
    | [out] | buff | Pointer to the mempool buffer |
    | [out] | buff\_len | Length of the allocated buffer |

Returns
:   0 on success
:   -EINVAL if the buffer wasn't allocated for this cqe
:   -ENOTSUP if memory blocks are disabled

## [◆ ](#ga8497170f55af1d11d717e919f61806f5)rtio\_cqe\_pool\_alloc()

| | struct [rtio\_cqe](structrtio__cqe.md) \* rtio\_cqe\_pool\_alloc | ( | struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \* | *pool* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#ga23c0c5d4b551858eabe057ecb8a28d12)rtio\_cqe\_pool\_free()

| | void rtio\_cqe\_pool\_free | ( | struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \* | *pool*, | | --- | --- | --- | --- | |  |  | struct [rtio\_cqe](structrtio__cqe.md) \* | *cqe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#ga6f55202adeca60aed0343a7a0dcab071)rtio\_cqe\_produce()

| | void rtio\_cqe\_produce | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | struct [rtio\_cqe](structrtio__cqe.md) \* | *cqe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Produce a complete queue event if available.

## [◆ ](#gaa0799a5f8ad98425d385a07c5d27d9cb)rtio\_cqe\_release()

| | void rtio\_cqe\_release | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | struct [rtio\_cqe](structrtio__cqe.md) \* | *cqe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Release consumed completion queue event.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | cqe | Completion queue entry |

## [◆ ](#ga4abc221d5a90ab882000a72caa0ebd0f)rtio\_cqe\_submit()

| | void rtio\_cqe\_submit | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | int | *result*, | |  |  | void \* | *userdata*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Submit a completion queue event with a given result and userdata.

Called by the executor to produce a completion queue event, no inherent locking is performed and this is not safe to do from multiple callers.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | result | Integer result code (could be -errno) |
    | userdata | Userdata to pass along to completion |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags to use for the CEQ see RTIO\_CQE\_FLAG\_\* |

## [◆ ](#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a)rtio\_executor\_err()

| void rtio\_executor\_err | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe*, |
| --- | --- | --- | --- |
|  |  | int | *result* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#ga7e2ebd9abaf585207bc5b99c5d815c6a)rtio\_executor\_ok()

| void rtio\_executor\_ok | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe*, |
| --- | --- | --- | --- |
|  |  | int | *result* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#gaf191153e83de72ddefb998daad02fa16)rtio\_executor\_submit()

| void rtio\_executor\_submit | ( | struct [rtio](structrtio.md) \* | *r* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#gaada07aa6acefa548743b525225fa482f)rtio\_iodev\_sqe\_err()

| | void rtio\_iodev\_sqe\_err | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe*, | | --- | --- | --- | --- | |  |  | int | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Inform the executor of a submissions completion with error.

This SHALL fail the remaining submissions in the chain.

Parameters
:   | iodev\_sqe | Submission that has failed |
    | --- | --- |
    | result | Result of the request |

## [◆ ](#gae690e3dc0fc40dda57257b2eed432719)rtio\_iodev\_sqe\_next()

| | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* rtio\_iodev\_sqe\_next | ( | const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Get the next sqe in the chain or transaction.

Parameters
:   | iodev\_sqe | Submission queue entry |
    | --- | --- |

Return values
:   | NULL | if current sqe is last in chain |
    | --- | --- |
    | struct | [rtio\_iodev\_sqe](structrtio__iodev__sqe.md "Compute the mempool block index for a given pointer.") \* if available |

## [◆ ](#gacb1d2ffa2b07418d8a8aa319bd4336ab)rtio\_iodev\_sqe\_ok()

| | void rtio\_iodev\_sqe\_ok | ( | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe*, | | --- | --- | --- | --- | |  |  | int | *result* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Inform the executor of a submission completion with success.

This may start the next asynchronous request if one is available.

Parameters
:   | iodev\_sqe | IODev Submission that has succeeded |
    | --- | --- |
    | result | Result of the request |

## [◆ ](#ga4213be028b0a1264daaa0d30c4c2d089)rtio\_mempool\_block\_size()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rtio\_mempool\_block\_size | ( | const struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Get the mempool block size of the RTIO context.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | The RTIO context |
    | --- | --- | --- |

Returns
:   The size of each block in the context's mempool
:   0 if the context doesn't have a mempool

## [◆ ](#ga6530bf56ccbab046a362a6448f941609)rtio\_release\_buffer()

| void rtio\_release\_buffer | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | void \* | *buff*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *buff\_len* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Release memory that was allocated by the RTIO's memory pool.

If the RTIO context was created by a call to [RTIO\_DEFINE\_WITH\_MEMPOOL()](#gae4c2a9384a9ae4ed16dff914b1184ca8), then the cqe data might contain a buffer that's owned by the RTIO context. In those cases (if the read request was configured via rtio\_sqe\_read\_with\_pool()) the buffer must be returned back to the pool.

Call this function when processing is complete. This function will validate that the memory actually belongs to the RTIO context and will ignore invalid arguments.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | buff | Pointer to the buffer to be released. |
    | buff\_len | Number of bytes to free (will be rounded up to nearest memory block). |

## [◆ ](#ga1f4fb7bccbaae08a94387e4b11275a78)rtio\_sqe\_acquirable()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rtio\_sqe\_acquirable | ( | struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Count of acquirable submission queue events.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |

Returns
:   Count of acquirable submission queue events

## [◆ ](#ga8b47c954d15a334621def53acceb6799)rtio\_sqe\_acquire()

| | struct [rtio\_sqe](structrtio__sqe.md) \* rtio\_sqe\_acquire | ( | struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Acquire a single submission queue event if available.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |

Return values
:   | sqe | A valid submission queue event acquired from the submission queue |
    | --- | --- |
    | NULL | No subsmission queue event available |

## [◆ ](#gac01252e55d2848b38c0ed77b71d600a7)rtio\_sqe\_cancel()

| int rtio\_sqe\_cancel | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Attempt to cancel an SQE.

If possible (not currently executing), cancel an SQE and generate a failure with -ECANCELED result.

Parameters
:   | [in] | sqe | The SQE to cancel |
    | --- | --- | --- |

Returns
:   0 if the SQE was flagged for cancellation
:   <0 on error

## [◆ ](#ga65e351af0a16dcf504a51ef4eb9316c7)rtio\_sqe\_copy\_in()

| | int rtio\_sqe\_copy\_in | ( | struct [rtio](structrtio.md) \* | *r*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_sqe](structrtio__sqe.md) \* | *sqes*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *sqe\_count* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Copy an array of SQEs into the queue.

Useful if a batch of submissions is stored in ROM or RTIO is used from user mode where a copy must be made.

Partial copying is not done as chained SQEs need to be submitted as a whole set.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | sqes | Pointer to an array of SQEs |
    | sqe\_count | Count of sqes in array |

Return values
:   | 0 | success |
    | --- | --- |
    | -ENOMEM | not enough room in the queue |

## [◆ ](#ga830863e6c8d9b96f4c473a038cab8f8c)rtio\_sqe\_copy\_in\_get\_handles()

| int rtio\_sqe\_copy\_in\_get\_handles | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | const struct [rtio\_sqe](structrtio__sqe.md) \* | *sqes*, |
|  |  | struct [rtio\_sqe](structrtio__sqe.md) \*\* | *handle*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *sqe\_count* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Copy an array of SQEs into the queue and get resulting handles back.

Copies one or more SQEs into the RTIO context and optionally returns their generated SQE handles. Handles can be used to cancel events via the [rtio\_sqe\_cancel()](#gac01252e55d2848b38c0ed77b71d600a7) call.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- | --- |
    | [in] | sqes | Pointer to an array of SQEs |
    | [out] | handle | Optional pointer to [rtio\_sqe](structrtio__sqe.md "rtio_sqe") pointer to store the handle of the first generated SQE. Use NULL to ignore. |
    | [in] | sqe\_count | Count of sqes in array |

Return values
:   | 0 | success |
    | --- | --- |
    | -ENOMEM | not enough room in the queue |

## [◆ ](#ga9486fb7b50e8d2409a50da235203536b)rtio\_sqe\_drop\_all()

| | void rtio\_sqe\_drop\_all | ( | struct [rtio](structrtio.md) \* | *r* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Drop all previously acquired sqe.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |

## [◆ ](#gae5fb03fc8f3a4a774f476ff552999bfc)rtio\_sqe\_pool\_alloc()

| | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* rtio\_sqe\_pool\_alloc | ( | struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \* | *pool* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#gac776aea3692cfd77aa5bf675a9e9ed02)rtio\_sqe\_pool\_free()

| | void rtio\_sqe\_pool\_free | ( | struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \* | *pool*, | | --- | --- | --- | --- | |  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#ga9d0dd7d0e2e3d281092f2350d6e1713e)rtio\_sqe\_prep\_callback()

| | void rtio\_sqe\_prep\_callback | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | [rtio\_callback\_t](#gad1dbd690e6cf88d7c788436dd04d1a00) | *callback*, | |  |  | void \* | *arg0*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a callback op submission.

A somewhat special operation in that it may only be done in kernel mode.

Used where general purpose logic is required in a queue of io operations to do transforms or logic.

## [◆ ](#gae87be354087d038953dae07c7f9cd3b0)rtio\_sqe\_prep\_callback\_no\_cqe()

| | void rtio\_sqe\_prep\_callback\_no\_cqe | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | [rtio\_callback\_t](#gad1dbd690e6cf88d7c788436dd04d1a00) | *callback*, | |  |  | void \* | *arg0*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a callback op submission that does not create a CQE.

Similar to [rtio\_sqe\_prep\_callback](#ga9d0dd7d0e2e3d281092f2350d6e1713e), but the [RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11 "RTIO_SQE_NO_RESPONSE") flag is set on the SQE to prevent the generation of a CQE upon completion.

This can be useful when the callback is the last operation in a sequence whose job is to clean up all the previous CQE's. Without [RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11 "RTIO_SQE_NO_RESPONSE") the completion itself will result in a CQE that cannot be consumed in the callback.

## [◆ ](#ga599ee43fdf35e1cf895cbbe9272e4c50)rtio\_sqe\_prep\_nop()

| | void rtio\_sqe\_prep\_nop | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a nop (no op) submission.

## [◆ ](#ga89c7cc2494e3dda50737f78f1a1376cf)rtio\_sqe\_prep\_read()

| | void rtio\_sqe\_prep\_read | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *prio*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a read op submission.

## [◆ ](#ga9803aa829f8c0eeee746ea7d872c20cc)rtio\_sqe\_prep\_read\_multishot()

| | void rtio\_sqe\_prep\_read\_multishot | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *prio*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

## [◆ ](#ga15c1f623658d27d300d1a31a6f3d6b9d)rtio\_sqe\_prep\_read\_with\_pool()

| | void rtio\_sqe\_prep\_read\_with\_pool | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *prio*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a read op submission with context's mempool.

See also
:   [rtio\_sqe\_prep\_read()](#ga89c7cc2494e3dda50737f78f1a1376cf)

## [◆ ](#ga31be14ece09e061a8d42ca8f2395286a)rtio\_sqe\_prep\_tiny\_write()

| | void rtio\_sqe\_prep\_tiny\_write | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *prio*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *tiny\_write\_data*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *tiny\_write\_len*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a tiny write op submission.

Unlike the normal write operation where the source buffer must outlive the call the tiny write data in this case is copied to the sqe. It must be tiny to fit within the specified size of a [rtio\_sqe](structrtio__sqe.md "A submission queue event.").

This is useful in many scenarios with RTL logic where a write of the register to subsequently read must be done.

## [◆ ](#gab9b605dcbb01d21c88f9ae70588ea3b5)rtio\_sqe\_prep\_transceive()

| | void rtio\_sqe\_prep\_transceive | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *prio*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *tx\_buf*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rx\_buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *buf\_len*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a transceive op submission.

## [◆ ](#ga7f7856d1f4fd1d8c4f6eebcccfe77701)rtio\_sqe\_prep\_write()

| | void rtio\_sqe\_prep\_write | ( | struct [rtio\_sqe](structrtio__sqe.md) \* | *sqe*, | | --- | --- | --- | --- | |  |  | const struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, | |  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *prio*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len*, | |  |  | void \* | *userdata* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Prepare a write op submission.

## [◆ ](#gaab6843e2038d00a8354f57d7e2ffcf7e)rtio\_sqe\_rx\_buf()

| | int rtio\_sqe\_rx\_buf | ( | const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *min\_buf\_len*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_buf\_len*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *buf\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Get the buffer associate with the RX submission.

Parameters
:   | [in] | iodev\_sqe | The submission to probe |
    | --- | --- | --- |
    | [in] | min\_buf\_len | The minimum number of bytes needed for the operation |
    | [in] | max\_buf\_len | The maximum number of bytes needed for the operation |
    | [out] | buf | Where to store the pointer to the buffer |
    | [out] | buf\_len | Where to store the size of the buffer |

Returns
:   0 if `buf` and `buf_len` were successfully filled
:   -ENOMEM Not enough memory for `min_buf_len`

## [◆ ](#gafee27c64a4a4989c4eb774addde8eb2e)rtio\_submit()

| int rtio\_submit | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *wait\_count* ) |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Submit I/O requests to the underlying executor.

Submits the queue of submission queue events to the executor. The executor will do the work of managing tasks representing each submission chain, freeing submission queue events when done, and producing completion queue events as submissions are completed.

Parameters
:   | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | RTIO context |
    | --- | --- |
    | wait\_count | Number of submissions to wait for completion of. |

Return values
:   | 0 | On success |
    | --- | --- |

## [◆ ](#gaef904eb6a8810d8c3ea537c4d6edbee5)rtio\_txn\_next()

| | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* rtio\_txn\_next | ( | const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

Get the next sqe in the transaction.

Parameters
:   | iodev\_sqe | Submission queue entry |
    | --- | --- |

Return values
:   | NULL | if current sqe is last in transaction |
    | --- | --- |
    | struct | [rtio\_sqe](structrtio__sqe.md "A submission queue event.") \* if available |

## Variable Documentation

## [◆ ](#ga86a38086dd85150ab6e479d73db1c6d1)rtio\_partition

| | struct [k\_mem\_partition](structk__mem__partition.md) rtio\_partition | | --- | | extern |
| --- | --- | --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The memory partition associated with all RTIO context information.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
