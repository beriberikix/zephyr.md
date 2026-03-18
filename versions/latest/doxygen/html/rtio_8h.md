---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtio_8h.html
original_path: doxygen/html/rtio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h File Reference

Real-Time IO device API for moving bytes with low effort.
[More...](#details)

`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/app_memory/app_memdomain.h](app__memdomain_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/rtio/rtio_mpsc.h](rtio__mpsc_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/sys/mem_blocks.h](mem__blocks_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <syscalls/rtio.h>`

[Go to the source code of this file.](rtio_8h_source.md)

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
| #define | [RTIO\_PRIO\_LOW](group__rtio__sqe__prio.md#gabc81232a7d4b7145d9898afd6ff2ae48)   0U |
|  | Low priority. |
| #define | [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)   127U |
|  | Normal priority. |
| #define | [RTIO\_PRIO\_HIGH](group__rtio__sqe__prio.md#ga220baa9bf2c8ff0cb6f52f0220e72b30)   255U |
|  | High priority. |
| #define | [RTIO\_SQE\_CHAINED](group__rtio__sqe__flags.md#gae9191d521d4ab602b53fefb74020d06b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | The next request in the queue should wait on this one. |
| #define | [RTIO\_SQE\_TRANSACTION](group__rtio__sqe__flags.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | The next request in the queue is part of a transaction. |
| #define | [RTIO\_SQE\_MEMPOOL\_BUFFER](group__rtio__sqe__flags.md#ga2802b46584220afffa0e959e149d5a4d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | The buffer should be allocated by the RTIO mempool. |
| #define | [RTIO\_SQE\_CANCELED](group__rtio__sqe__flags.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | The SQE should not execute if possible. |
| #define | [RTIO\_SQE\_MULTISHOT](group__rtio__sqe__flags.md#ga00f8ead8f043fe40d49d0bc3325fb299)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | The SQE should continue producing CQEs until canceled. |
| #define | [RTIO\_SQE\_NO\_RESPONSE](group__rtio__sqe__flags.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | The SQE does not produce a CQE. |
| #define | [RTIO\_CQE\_FLAG\_MEMPOOL\_BUFFER](group__rtio__cqe__flags.md#ga0f212500447a5e37e225a6997953b609)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | The entry's buffer was allocated from the RTIO's mempool. |
| #define | [RTIO\_CQE\_FLAG\_GET](group__rtio__cqe__flags.md#gaef64ea020a20ac22a0edcb6eca032efc)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| #define | [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_IDX](group__rtio__cqe__flags.md#ga0b5f3f7e7be472ecf87bd2b08c1888da)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get the block index of a mempool flags. |
| #define | [RTIO\_CQE\_FLAG\_MEMPOOL\_GET\_BLK\_CNT](group__rtio__cqe__flags.md#ga087465f866d417d5332602bb582cc1a7)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get the block count of a mempool flags. |
| #define | [RTIO\_CQE\_FLAG\_PREP\_MEMPOOL](group__rtio__cqe__flags.md#ga28b3a5661248b6b3763aab47417114d6)(blk\_idx, blk\_cnt) |
|  | Prepare CQE flags for a mempool read. |
| #define | [RTIO\_IODEV\_I2C\_STOP](group__rtio.md#gaf923e862d2c6a3fbce5eb96781cf86d8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Equivalent to the I2C\_MSG\_STOP flag. |
| #define | [RTIO\_IODEV\_I2C\_RESTART](group__rtio.md#gadba1c5eddeecc431000bd92054f55c3a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Equivalent to the I2C\_MSG\_RESTART flag. |
| #define | [RTIO\_IODEV\_I2C\_10\_BITS](group__rtio.md#gaa0c3b047c7205d12775d8d38907119b9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Equivalent to the I2C\_MSG\_ADDR\_10\_BITS. |
| #define | [RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)   0 |
|  | An operation that does nothing and will complete immediately. |
| #define | [RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)   ([RTIO\_OP\_NOP](group__rtio.md#gad5f073978f641413989d1c6b405d6c36)+1) |
|  | An operation that receives (reads). |
| #define | [RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)   ([RTIO\_OP\_RX](group__rtio.md#gafeb05c351207cd1638fa78f6607e1a4a)+1) |
|  | An operation that transmits (writes). |
| #define | [RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)   ([RTIO\_OP\_TX](group__rtio.md#ga8dcaef0cda159e16520a95543ff62827)+1) |
|  | An operation that transmits tiny writes by copying the data to write. |
| #define | [RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)   ([RTIO\_OP\_TINY\_TX](group__rtio.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)+1) |
|  | An operation that calls a given function (callback). |
| #define | [RTIO\_OP\_TXRX](group__rtio.md#ga9f0e70f5a28be65a8ed67c0257a72692)   ([RTIO\_OP\_CALLBACK](group__rtio.md#ga18e0ff7d44e4c33900106aefad0a8508)+1) |
|  | An operation that transceives (reads and writes simultaneously). |
| #define | [RTIO\_IODEV\_DEFINE](group__rtio.md#gaae51e2a679d37bc1cfba79961688c406)(name, iodev\_api, iodev\_data) |
|  | Statically define and initialize an RTIO IODev. |
| #define | [RTIO\_BMEM](group__rtio.md#ga2437af5061e078950d4a55211d9a902f)   [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_USERSPACE, ([K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1)) static), (static)) |
|  | Allocate to bss if available. |
| #define | [RTIO\_DMEM](group__rtio.md#ga3b569c01b71e126cff852df50e98fd69)   [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_USERSPACE, ([K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1)) static), (static)) |
|  | Allocate as initialized memory if available. |
| #define | [RTIO\_DEFINE](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)(name, sq\_sz, cq\_sz) |
|  | Statically define and initialize an RTIO context. |
| #define | [RTIO\_DEFINE\_WITH\_MEMPOOL](group__rtio.md#gae4c2a9384a9ae4ed16dff914b1184ca8)(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign) |
|  | Statically define and initialize an RTIO context. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqe, void \*arg0) |
|  | Callback signature for RTIO\_OP\_CALLBACK. |

| Functions | |
| --- | --- |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [rtio\_mempool\_block\_size](group__rtio.md#ga4213be028b0a1264daaa0d30c4c2d089) (const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Get the mempool block size of the RTIO context. |
| static void | [rtio\_sqe\_prep\_nop](group__rtio.md#ga599ee43fdf35e1cf895cbbe9272e4c50) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, void \*userdata) |
|  | Prepare a nop (no op) submission. |
| static void | [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, void \*userdata) |
|  | Prepare a read op submission. |
| static void | [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, void \*userdata) |
|  | Prepare a read op submission with context's mempool. |
| static void | [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, void \*userdata) |
| static void | [rtio\_sqe\_prep\_write](group__rtio.md#gab01192577dadf7ab83d3f8029c86a149) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len, void \*userdata) |
|  | Prepare a write op submission. |
| static void | [rtio\_sqe\_prep\_tiny\_write](group__rtio.md#ga31be14ece09e061a8d42ca8f2395286a) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tiny\_write\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tiny\_write\_len, void \*userdata) |
|  | Prepare a tiny write op submission. |
| static void | [rtio\_sqe\_prep\_callback](group__rtio.md#ga9d0dd7d0e2e3d281092f2350d6e1713e) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) callback, void \*arg0, void \*userdata) |
|  | Prepare a callback op submission. |
| static void | [rtio\_sqe\_prep\_transceive](group__rtio.md#ga0129e02abc85526199311846e1830869) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe, const struct [rtio\_iodev](structrtio__iodev.md) \*iodev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len, void \*userdata) |
|  | Prepare a transceive op submission. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_sqe\_pool\_alloc](group__rtio.md#gae5fb03fc8f3a4a774f476ff552999bfc) (struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool) |
| static void | [rtio\_sqe\_pool\_free](group__rtio.md#gac776aea3692cfd77aa5bf675a9e9ed02) (struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \*pool, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_pool\_alloc](group__rtio.md#ga8497170f55af1d11d717e919f61806f5) (struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool) |
| static void | [rtio\_cqe\_pool\_free](group__rtio.md#ga23c0c5d4b551858eabe057ecb8a28d12) (struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \*pool, struct [rtio\_cqe](structrtio__cqe.md) \*cqe) |
| static int | [rtio\_block\_pool\_alloc](group__rtio.md#ga7f14b99fc1dd0697309e7f71a270f5fb) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_sz, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_sz, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len) |
| static void | [rtio\_block\_pool\_free](group__rtio.md#gafca7732926a9a7c080e3cb16e5f16108) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_len) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rtio\_sqe\_acquirable](group__rtio.md#ga1f4fb7bccbaae08a94387e4b11275a78) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Count of acquirable submission queue events. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_txn\_next](group__rtio.md#gaef904eb6a8810d8c3ea537c4d6edbee5) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Get the next sqe in the transaction. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_chain\_next](group__rtio.md#gada1e3abf92a46e376138435debc8baf4) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Get the next sqe in the chain. |
| static struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [rtio\_iodev\_sqe\_next](group__rtio.md#gae690e3dc0fc40dda57257b2eed432719) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Get the next sqe in the chain or transaction. |
| static struct [rtio\_sqe](structrtio__sqe.md) \* | [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Acquire a single submission queue event if available. |
| static void | [rtio\_sqe\_drop\_all](group__rtio.md#ga9486fb7b50e8d2409a50da235203536b) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Drop all previously acquired sqe. |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_acquire](group__rtio.md#gad848646651fdf3649b882e5268f72a3c) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Acquire a complete queue event if available. |
| static void | [rtio\_cqe\_produce](group__rtio.md#ga6f55202adeca60aed0343a7a0dcab071) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe) |
|  | Produce a complete queue event if available. |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_consume](group__rtio.md#gae562cf241911804cdb9f4e3a73b53df4) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Consume a single completion queue event if available. |
| static struct [rtio\_cqe](structrtio__cqe.md) \* | [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Wait for and consume a single completion queue event. |
| static void | [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe) |
|  | Release consumed completion queue event. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rtio\_cqe\_compute\_flags](group__rtio.md#ga75661c8c6c94a0ac6254cec674b478c8) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Compute the CQE flags from the [rtio\_iodev\_sqe](structrtio__iodev__sqe.md "Compute the mempool block index for a given pointer.") entry. |
| int | [rtio\_cqe\_get\_mempool\_buffer](group__rtio.md#gaedbf9386a36ed99baa290ef6c318ded1) (const struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buff\_len) |
|  | Retrieve the mempool buffer that was allocated for the CQE. |
| void | [rtio\_executor\_submit](group__rtio.md#gaf191153e83de72ddefb998daad02fa16) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
| void | [rtio\_executor\_ok](group__rtio.md#ga7e2ebd9abaf585207bc5b99c5d815c6a) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
| void | [rtio\_executor\_err](group__rtio.md#ga15f4a1a4dfb869ef9e4216dc1c1cdc8a) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
| static void | [rtio\_iodev\_sqe\_ok](group__rtio.md#gacb1d2ffa2b07418d8a8aa319bd4336ab) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
|  | Inform the executor of a submission completion with success. |
| static void | [rtio\_iodev\_sqe\_err](group__rtio.md#gaada07aa6acefa548743b525225fa482f) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, int result) |
|  | Inform the executor of a submissions completion with error. |
| static void | [rtio\_iodev\_cancel\_all](group__rtio.md#ga3a2d5e6daebe7b6e557706c75e7f8a41) (struct [rtio\_iodev](structrtio__iodev.md) \*iodev) |
|  | Cancel all requests that are pending for the iodev. |
| static void | [rtio\_cqe\_submit](group__rtio.md#ga4abc221d5a90ab882000a72caa0ebd0f) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), int result, void \*userdata, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Submit a completion queue event with a given result and userdata. |
| static int | [rtio\_sqe\_rx\_buf](group__rtio.md#gaab6843e2038d00a8354f57d7e2ffcf7e) (const struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) min\_buf\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_buf\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_len) |
|  | Get the buffer associate with the RX submission. |
| void | [rtio\_release\_buffer](group__rtio.md#ga6530bf56ccbab046a362a6448f941609) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), void \*buff, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buff\_len) |
|  | Release memory that was allocated by the RTIO's memory pool. |
| static void | [rtio\_access\_grant](group__rtio.md#ga9da42c98546930575525f0f92710f9e4) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [k\_thread](structk__thread.md) \*t) |
|  | Grant access to an RTIO context to a user thread. |
| int | [rtio\_sqe\_cancel](group__rtio.md#gac01252e55d2848b38c0ed77b71d600a7) (struct [rtio\_sqe](structrtio__sqe.md) \*sqe) |
|  | Attempt to cancel an SQE. |
| int | [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, struct [rtio\_sqe](structrtio__sqe.md) \*\*handle, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sqe\_count) |
|  | Copy an array of SQEs into the queue and get resulting handles back. |
| static int | [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), const struct [rtio\_sqe](structrtio__sqe.md) \*sqes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sqe\_count) |
|  | Copy an array of SQEs into the queue. |
| int | [rtio\_cqe\_copy\_out](group__rtio.md#ga98b2bbef95aea342a9b86a9775dd5c3b) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_cqe](structrtio__cqe.md) \*cqes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cqe\_count, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Copy an array of CQEs from the queue. |
| int | [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wait\_count) |
|  | Submit I/O requests to the underlying executor. |

| Variables | |
| --- | --- |
| struct [k\_mem\_partition](structk__mem__partition.md) | [rtio\_partition](group__rtio.md#ga86a38086dd85150ab6e479d73db1c6d1) |
|  | The memory partition associated with all RTIO context information. |

## Detailed Description

Real-Time IO device API for moving bytes with low effort.

RTIO is a context for asynchronous batch operations using a submission and completion queue.

Asynchronous I/O operation are setup in a submission queue. Each entry in the queue describes the operation it wishes to perform with some understood semantics.

These operations may be chained in a such a way that only when the current operation is complete the next will be executed. If the current operation fails all chained operations will also fail.

Operations may also be submitted as a transaction where a set of operations are considered to be one operation.

The completion of these operations typically provide one or more completion queue events.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio.h](rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
