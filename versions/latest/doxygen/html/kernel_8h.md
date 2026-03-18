---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kernel_8h.html
original_path: doxygen/html/kernel_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel.h File Reference

Public kernel APIs.
[More...](#details)

`#include <[zephyr/kernel_includes.h](kernel__includes_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[limits.h](limits_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/tracing/tracing_macros.h](tracing__macros_8h_source.md)>`  
`#include <[zephyr/sys/mem_stats.h](mem__stats_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/tracing/tracing.h](tracing_8h_source.md)>`  
`#include <zephyr/syscalls/kernel.h>`

[Go to the source code of this file.](kernel_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_queue](structk__queue.md) |
| struct | [k\_futex](structk__futex.md) |
|  | futex structure [More...](structk__futex.md#details) |
| struct | [k\_event](structk__event.md) |
|  | Event Structure. [More...](structk__event.md#details) |
| struct | [k\_fifo](structk__fifo.md) |
| struct | [k\_lifo](structk__lifo.md) |
| struct | [k\_mutex](structk__mutex.md) |
|  | Mutex Structure. [More...](structk__mutex.md#details) |
| struct | [k\_condvar](structk__condvar.md) |
| struct | [k\_work](structk__work.md) |
|  | A structure used to submit work. [More...](structk__work.md#details) |
| struct | [k\_work\_delayable](structk__work__delayable.md) |
|  | A structure used to submit work after a delay. [More...](structk__work__delayable.md#details) |
| struct | [k\_work\_sync](structk__work__sync.md) |
|  | A structure holding internal state for a pending synchronous operation on a work item or queue. [More...](structk__work__sync.md#details) |
| struct | [k\_work\_queue\_config](structk__work__queue__config.md) |
|  | A structure holding optional configuration items for a work queue. [More...](structk__work__queue__config.md#details) |
| struct | [k\_work\_q](structk__work__q.md) |
|  | A structure used to hold work until it can be processed. [More...](structk__work__q.md#details) |
| struct | [k\_msgq](structk__msgq.md) |
|  | Message Queue Structure. [More...](structk__msgq.md#details) |
| struct | [k\_msgq\_attrs](structk__msgq__attrs.md) |
|  | Message Queue Attributes. [More...](structk__msgq__attrs.md#details) |
| struct | [k\_mbox\_msg](structk__mbox__msg.md) |
|  | Mailbox Message Structure. [More...](structk__mbox__msg.md#details) |
| struct | [k\_mbox](structk__mbox.md) |
|  | Mailbox Structure. [More...](structk__mbox.md#details) |
| struct | [k\_pipe](structk__pipe.md) |
|  | Pipe Structure. [More...](structk__pipe.md#details) |
| struct | [k\_heap](structk__heap.md) |
| struct | [k\_poll\_signal](structk__poll__signal.md) |
| struct | [k\_poll\_event](structk__poll__event.md) |
|  | Poll Event. [More...](structk__poll__event.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_ANY](#ac627cc4c3da16be4b74f0a4ab036a603)   NULL |
| #define | [K\_PRIO\_COOP](#ac145d4747518572acfc8ee1579007d54)(x) |
| #define | [K\_PRIO\_PREEMPT](#aa0e916aae3ddd0e998cd41ac32afe30a)(x) |
| #define | [K\_HIGHEST\_THREAD\_PRIO](#a5fd4365cb6e8742e750b5e4950fb1e47)   (-CONFIG\_NUM\_COOP\_PRIORITIES) |
| #define | [K\_LOWEST\_THREAD\_PRIO](#afa4bcc2fdfea5cd7c63d56f476b1b32f)   CONFIG\_NUM\_PREEMPT\_PRIORITIES |
| #define | [K\_IDLE\_PRIO](#a8f3f1d910dd847f0b223a4aa00788fa2)   [K\_LOWEST\_THREAD\_PRIO](#afa4bcc2fdfea5cd7c63d56f476b1b32f) |
| #define | [K\_HIGHEST\_APPLICATION\_THREAD\_PRIO](#ab326c7eb1d248650e6017dcaee8d24b2)   ([K\_HIGHEST\_THREAD\_PRIO](#a5fd4365cb6e8742e750b5e4950fb1e47)) |
| #define | [K\_LOWEST\_APPLICATION\_THREAD\_PRIO](#ad4c2df561988fa1194c2f8c768d667cd)   ([K\_LOWEST\_THREAD\_PRIO](#afa4bcc2fdfea5cd7c63d56f476b1b32f) - 1) |
| #define | [K\_ESSENTIAL](group__thread__apis.md#gad503fbcca905a9266b0e154e3ded258c)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0)) |
|  | system thread that must not abort |
| #define | [K\_FP\_IDX](group__thread__apis.md#ga4b2378312ea9b410be025b40e8d6a395)   1 |
|  | FPU registers are managed by context switch. |
| #define | [K\_FP\_REGS](group__thread__apis.md#gab18cf1e8728e7adf53db2ae4bbcdd951)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_FP\_IDX](group__thread__apis.md#ga4b2378312ea9b410be025b40e8d6a395))) |
| #define | [K\_USER](group__thread__apis.md#gacb5340339892f22301e02697c6039ccc)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) |
|  | user mode thread |
| #define | [K\_INHERIT\_PERMS](group__thread__apis.md#gaa1788a413a055745d1de71b4da7c2eb2)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)) |
|  | Inherit Permissions. |
| #define | [K\_CALLBACK\_STATE](group__thread__apis.md#gacbdb579370978fe07e4a863a84bd8bee)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4)) |
|  | Callback item state. |
| #define | [K\_DSP\_IDX](group__thread__apis.md#gacbd163e5bc79fc0282def5ff4321fa30)   6 |
|  | DSP registers are managed by context switch. |
| #define | [K\_DSP\_REGS](group__thread__apis.md#ga8e1aeb428a418ed23e17448b796363cb)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_DSP\_IDX](group__thread__apis.md#gacbd163e5bc79fc0282def5ff4321fa30))) |
| #define | [K\_AGU\_IDX](group__thread__apis.md#gab01cfd20675ebef8f5e81d7d17e6babb)   7 |
|  | AGU registers are managed by context switch. |
| #define | [K\_AGU\_REGS](group__thread__apis.md#ga718088c1a68f03fffa960164cab60b72)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([K\_AGU\_IDX](group__thread__apis.md#gab01cfd20675ebef8f5e81d7d17e6babb))) |
| #define | [K\_SSE\_REGS](group__thread__apis.md#gaa5b7de51b26773aa4485a711a041d9a7)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
|  | FP and SSE registers are managed by context switch on x86. |
| #define | [k\_thread\_access\_grant](group__thread__apis.md#gafec540511e6d2e0a074a5bfb515c53b0)(thread, ...) |
|  | Grant a thread access to a set of kernel objects. |
| #define | [K\_THREAD\_DEFINE](group__thread__apis.md#gab3ced58648ca35788a40676e8478ecd2)(name, stack\_size, entry, p1, p2, p3, prio, options, delay) |
|  | Statically define and initialize a thread. |
| #define | [K\_KERNEL\_THREAD\_DEFINE](group__thread__apis.md#gae25853424ec969f8431862c46b3ec294)(name, stack\_size, entry, p1, p2, p3, prio, options, delay) |
|  | Statically define and initialize a thread intended to run only in kernel mode. |
| #define | [K\_NO\_WAIT](group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f)   Z\_TIMEOUT\_NO\_WAIT |
|  | Generate null timeout delay. |
| #define | [K\_NSEC](group__clock__apis.md#gae2f3a80170afc5fbce0337cdf5a4ce4c)(t) |
|  | Generate timeout delay from nanoseconds. |
| #define | [K\_USEC](group__clock__apis.md#ga91198e325210ec052a8308e642058c0b)(t) |
|  | Generate timeout delay from microseconds. |
| #define | [K\_CYC](group__clock__apis.md#gab41f59fd2b724cb1279e4f6821154b33)(t) |
|  | Generate timeout delay from cycles. |
| #define | [K\_TICKS](group__clock__apis.md#gaeda983960bd25f1dba7a386ad720e395)(t) |
|  | Generate timeout delay from system ticks. |
| #define | [K\_MSEC](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f)(ms) |
|  | Generate timeout delay from milliseconds. |
| #define | [K\_SECONDS](group__clock__apis.md#gadc361472aea59267f6ea38f5e7c7ca2a)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Generate timeout delay from seconds. |
| #define | [K\_MINUTES](group__clock__apis.md#gaef02f20d4d2ebfc9aa29acae01bd3698)(m) |
|  | Generate timeout delay from minutes. |
| #define | [K\_HOURS](group__clock__apis.md#gaa9e0cd890db28965b66d4bc5d719a91f)(h) |
|  | Generate timeout delay from hours. |
| #define | [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)   Z\_FOREVER |
|  | Generate infinite timeout delay. |
| #define | [K\_TIMER\_DEFINE](group__timer__apis.md#gaa267fcb0a2e18cd0da29e9f9612510a6)(name, expiry\_fn, stop\_fn) |
|  | Statically define and initialize a timer. |
| #define | [K\_QUEUE\_DEFINE](group__queue__apis.md#gacd0bc309f0147d4669f65fafa87e0e70)(name) |
|  | Statically define and initialize a queue. |
| #define | [K\_EVENT\_DEFINE](group__event__apis.md#ga093449cc6686d3235944f3faad284893)(name) |
|  | Statically define and initialize an event object. |
| #define | [k\_fifo\_init](group__fifo__apis.md#gaeebf6ef54d4be61e19408f44a734a159)(fifo) |
|  | Initialize a FIFO queue. |
| #define | [k\_fifo\_cancel\_wait](group__fifo__apis.md#gab744080af449e093df8dd4982e013e16)(fifo) |
|  | Cancel waiting on a FIFO queue. |
| #define | [k\_fifo\_put](group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913)(fifo, data) |
|  | Add an element to a FIFO queue. |
| #define | [k\_fifo\_alloc\_put](group__fifo__apis.md#gab1c5212040d12cbb92cede5cf54928ba)(fifo, data) |
|  | Add an element to a FIFO queue. |
| #define | [k\_fifo\_put\_list](group__fifo__apis.md#ga1bf5f52290c83e54ba14358cbbb4051b)(fifo, head, tail) |
|  | Atomically add a list of elements to a FIFO. |
| #define | [k\_fifo\_put\_slist](group__fifo__apis.md#ga4cdc286a7a6f0d43acab63a4846815e7)(fifo, list) |
|  | Atomically add a list of elements to a FIFO queue. |
| #define | [k\_fifo\_get](group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6)(fifo, timeout) |
|  | Get an element from a FIFO queue. |
| #define | [k\_fifo\_is\_empty](group__fifo__apis.md#gab7cec4adc128ed1fd2d194ba6cd8c640)(fifo) |
|  | Query a FIFO queue to see if it has data available. |
| #define | [k\_fifo\_peek\_head](group__fifo__apis.md#ga2e0c8608f095a929740fa94c94a4f389)(fifo) |
|  | Peek element at the head of a FIFO queue. |
| #define | [k\_fifo\_peek\_tail](group__fifo__apis.md#gafbe2ce9a6437b886cf149016187ba92f)(fifo) |
|  | Peek element at the tail of FIFO queue. |
| #define | [K\_FIFO\_DEFINE](group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274)(name) |
|  | Statically define and initialize a FIFO queue. |
| #define | [k\_lifo\_init](group__lifo__apis.md#ga69fb19716a9014f7de79f8e524d64a3e)(lifo) |
|  | Initialize a LIFO queue. |
| #define | [k\_lifo\_put](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)(lifo, data) |
|  | Add an element to a LIFO queue. |
| #define | [k\_lifo\_alloc\_put](group__lifo__apis.md#ga96d885a6a36fcfcb5eaa65898eee0965)(lifo, data) |
|  | Add an element to a LIFO queue. |
| #define | [k\_lifo\_get](group__lifo__apis.md#gad5f1775947b07a2a77f667aa9e41db5a)(lifo, timeout) |
|  | Get an element from a LIFO queue. |
| #define | [K\_LIFO\_DEFINE](group__lifo__apis.md#gaebd450d4181f22491623ea0aed6ee576)(name) |
|  | Statically define and initialize a LIFO queue. |
| #define | [K\_STACK\_DEFINE](group__stack__apis.md#ga8c9ca77e5de3c9757dcd4ecb55797835)(name, stack\_num\_entries) |
|  | Statically define and initialize a stack. |
| #define | [K\_MUTEX\_DEFINE](group__mutex__apis.md#gab6f3d98fabbdc0918bbc9934d61d63f3)(name) |
|  | Statically define and initialize a mutex. |
| #define | [K\_CONDVAR\_DEFINE](group__condvar__apis.md#ga770816651e25f7e7dae992a0b2260c21)(name) |
|  | Statically define and initialize a condition variable. |
| #define | [K\_SEM\_MAX\_LIMIT](group__semaphore__apis.md#ga689359a77a0cebe737ef644c188f7e57)   UINT\_MAX |
|  | Maximum limit value allowed for a semaphore. |
| #define | [K\_SEM\_DEFINE](group__semaphore__apis.md#ga018a8aa43e02e704deee7b6341502946)(name, initial\_count, count\_limit) |
|  | Statically define and initialize a semaphore. |
| #define | [K\_WORK\_DELAYABLE\_DEFINE](group__workqueue__apis.md#ga893b281f3d2bc0088650536899e17903)(work, work\_handler) |
|  | Initialize a statically-defined delayable work item. |
| #define | [K\_WORK\_USER\_DEFINE](group__workqueue__apis.md#ga4f3eac1fc56d5c9c21a3afa9b964b0bf)(work, work\_handler) |
|  | Initialize a statically-defined user work item. |
| #define | [K\_WORK\_DEFINE](group__workqueue__apis.md#gaf8e003eefa5dd66ba883688f9d39c333)(work, work\_handler) |
|  | Initialize a statically-defined work item. |
| #define | [K\_MSGQ\_FLAG\_ALLOC](group__msgq__apis.md#ga4bb73f46fd0818f7f7a90860b792f7ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [K\_MSGQ\_DEFINE](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)(q\_name, q\_msg\_size, q\_max\_msgs, q\_align) |
|  | Statically define and initialize a message queue. |
| #define | [K\_MBOX\_DEFINE](group__mailbox__apis.md#gab55cba898db47113a06641c01f3e3714)(name) |
|  | Statically define and initialize a mailbox. |
| #define | [K\_PIPE\_DEFINE](group__pipe__apis.md#gac2256aa00c59e78199be9bdefd61aa52)(name, pipe\_buffer\_size, pipe\_align) |
|  | Statically define and initialize a pipe. |
| #define | [K\_MEM\_SLAB\_DEFINE](group__mem__slab__apis.md#ga60bc92eee58fcc5f121b8e4d82eaa69e)(name, slab\_block\_size, slab\_num\_blocks, slab\_align) |
|  | Statically define and initialize a memory slab in a public (non-static) scope. |
| #define | [K\_MEM\_SLAB\_DEFINE\_STATIC](group__mem__slab__apis.md#ga90bdbb15f410991f54ba16025c24bc3c)(name, slab\_block\_size, slab\_num\_blocks, slab\_align) |
|  | Statically define and initialize a memory slab in a private (static) scope. |
| #define | [K\_HEAP\_DEFINE](group__heap__apis.md#ga795d7f1e6d5b7b19a7a50198d7829a0f)(name, bytes) |
|  | Define a static [k\_heap](structk__heap.md). |
| #define | [K\_HEAP\_DEFINE\_NOCACHE](group__heap__apis.md#ga968f4c6a201fdf6862d62dd5d9f8d032)(name, bytes) |
|  | Define a static [k\_heap](structk__heap.md) in uncached memory. |
| #define | [K\_POLL\_TYPE\_IGNORE](group__poll__apis.md#gafd5d801eb9e9cf6097b2c08b4933998e)   0 |
| #define | [K\_POLL\_TYPE\_SIGNAL](group__poll__apis.md#ga144d8eb34d85f6053e454410a10bf56a)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SIGNAL) |
| #define | [K\_POLL\_TYPE\_SEM\_AVAILABLE](group__poll__apis.md#ga0fd7605bdffd43dff7480a90a603ffde)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_SEM\_AVAILABLE) |
| #define | [K\_POLL\_TYPE\_DATA\_AVAILABLE](group__poll__apis.md#ga58d656f73f031a39b8a936133fe5504f)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE](group__poll__apis.md#ga71734fee18c523cf70276260118afb91)   [K\_POLL\_TYPE\_DATA\_AVAILABLE](group__poll__apis.md#ga58d656f73f031a39b8a936133fe5504f) |
| #define | [K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE](group__poll__apis.md#gaa83509b54175fb6c98324422a928d5e1)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE](group__poll__apis.md#ga14e113201a3b3ad768c6a5ce917d1912)   Z\_POLL\_TYPE\_BIT(\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_NOT\_READY](group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa)   0 |
| #define | [K\_POLL\_STATE\_SIGNALED](group__poll__apis.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SIGNALED) |
| #define | [K\_POLL\_STATE\_SEM\_AVAILABLE](group__poll__apis.md#gae9e3eefd5a29a538d22f53592578bb37)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_SEM\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_DATA\_AVAILABLE](group__poll__apis.md#gac166d9919d591bace163c5211e7b41f4)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE](group__poll__apis.md#gabd5ac3341698534f39ded718079d6168)   [K\_POLL\_STATE\_DATA\_AVAILABLE](group__poll__apis.md#gac166d9919d591bace163c5211e7b41f4) |
| #define | [K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE](group__poll__apis.md#gac236074cd43f59f28b803fe2c4a4f6f7)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE](group__poll__apis.md#ga9028d6868ee964ca25931ed9170068dd)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE) |
| #define | [K\_POLL\_STATE\_CANCELLED](group__poll__apis.md#gadaf4b4c8e13afb54114af72d133e1fdb)   Z\_POLL\_STATE\_BIT(\_POLL\_STATE\_CANCELLED) |
| #define | [K\_POLL\_SIGNAL\_INITIALIZER](group__poll__apis.md#ga6d6321e189afca73a276cd671ec531ae)(obj) |
| #define | [K\_POLL\_EVENT\_INITIALIZER](group__poll__apis.md#ga8e3889f2bac281a6e65e31068e58047e)(\_event\_type, \_event\_mode, \_event\_obj) |
| #define | [K\_POLL\_EVENT\_STATIC\_INITIALIZER](group__poll__apis.md#gada2366896d913dc916b3c28642648b63)(\_event\_type, \_event\_mode, \_event\_obj, event\_tag) |
| #define | [k\_oops](#abde5aa8ca5e64a045b25b88f91370dcd)() |
|  | Fatally terminate a thread. |
| #define | [k\_panic](#aedd541f707b1463aaac15c7798340329)() |
|  | Fatally terminate the system. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75)) (const struct [k\_thread](structk__thread.md) \*thread, void \*user\_data) |
| typedef void(\* | [k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde)) (struct k\_timer \*timer) |
|  | Timer expiry function type. |
| typedef void(\* | [k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c)) (struct k\_timer \*timer) |
|  | Timer stop function type. |
| typedef void(\* | [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda)) (struct [k\_work](structk__work.md) \*work) |
|  | The signature for a work item handler function. |
| typedef void(\* | [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc)) (struct k\_work\_user \*work) |
|  | Work item handler function type for user work queues. |

| Enumerations | |
| --- | --- |
| enum | [execution\_context\_types](#ab0b42f9804777dfa5fed2b7cd866779c) { [K\_ISR](#ab0b42f9804777dfa5fed2b7cd866779ca30593044743695f8184a157283dac4d5) = 0 , [K\_COOP\_THREAD](#ab0b42f9804777dfa5fed2b7cd866779ca62c0b731a1bb3c5e4aadeba3f93df58b) , [K\_PREEMPT\_THREAD](#ab0b42f9804777dfa5fed2b7cd866779cae84f57f4ac996c751d1f4c9e49789322) } |
| enum | {     [K\_WORK\_RUNNING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebac6bee9a104cf6ee3853579f5eb15c165) = BIT(K\_WORK\_RUNNING\_BIT) , [K\_WORK\_CANCELING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744eba9fdc4327489bcdcca3de0ee9eed6b732) = BIT(K\_WORK\_CANCELING\_BIT) , [K\_WORK\_QUEUED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaa7f8855bc9931bff79062ce53b06eb85) = BIT(K\_WORK\_QUEUED\_BIT) , [K\_WORK\_DELAYED](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebab4bf9e74435077b2bbfe1de1f4e80aed) = BIT(K\_WORK\_DELAYED\_BIT) ,     [K\_WORK\_FLUSHING](group__workqueue__apis.md#ggae539da4c3f3d31b039bc49b9e76744ebaf74fab337ab0694e9dd0692989ca6601) = BIT(K\_WORK\_FLUSHING\_BIT)   } |
| enum | [k\_poll\_modes](group__poll__apis.md#ga36d7978872a83191dd3cc16d62165add) { [K\_POLL\_MODE\_NOTIFY\_ONLY](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681) = 0 , [K\_POLL\_NUM\_MODES](group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda71e08944b3e944c28056f9a5fbfb018c) } |

| Functions | |
| --- | --- |
| void | [k\_thread\_foreach](group__thread__apis.md#gae2596d56800769b06fc03c194a126a97) ([k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data) |
|  | Iterate over all the threads in the system. |
| void | [k\_thread\_foreach\_unlocked](group__thread__apis.md#ga30ef8b445a6c1b4a82651674dbb737fc) ([k\_thread\_user\_cb\_t](group__thread__apis.md#gaf9f23a6ff9dae76af56f25b373e74c75) user\_cb, void \*user\_data) |
|  | Iterate over all the threads in the system without locking. |
| [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \* | [k\_thread\_stack\_alloc](group__thread__apis.md#gafe00cc70bac8a47ba6dda21bde508614) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Dynamically allocate a thread stack. |
| int | [k\_thread\_stack\_free](group__thread__apis.md#ga95560cb85f6656b981a9a50ff2cd70b7) ([k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack) |
|  | Free a dynamically allocated thread stack. |
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_thread\_create](group__thread__apis.md#gad5b0bff3102f1656089f5875d999a367) (struct [k\_thread](structk__thread.md) \*new\_thread, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size, [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry, void \*p1, void \*p2, void \*p3, int prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) options, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Create a thread. |
| FUNC\_NORETURN void | [k\_thread\_user\_mode\_enter](group__thread__apis.md#ga3fbe1c8a5f3ef1c25382c7d6fca35764) ([k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) entry, void \*p1, void \*p2, void \*p3) |
|  | Drop a thread's privileges permanently to user mode. |
| static void | [k\_thread\_heap\_assign](group__thread__apis.md#ga3f46c06833add2a2e0ddb7242f06702c) (struct [k\_thread](structk__thread.md) \*thread, struct [k\_heap](structk__heap.md) \*heap) |
|  | Assign a resource memory pool to a thread. |
| int | [k\_thread\_join](group__thread__apis.md#ga40a733561eb1f64dcaae0e01b167d233) (struct [k\_thread](structk__thread.md) \*thread, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Sleep until a thread exits. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_sleep](group__thread__apis.md#ga48d4b041790454da4d68ac8711f29657) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Put the current thread to sleep. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_msleep](group__thread__apis.md#ga51307cdfe153ab3e918b18755d97c5d9) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ms) |
|  | Put the current thread to sleep. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_usleep](group__thread__apis.md#gaeac56bb072ce295b9fdc372ab8cee67e) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) us) |
|  | Put the current thread to sleep with microsecond resolution. |
| void | [k\_busy\_wait](group__thread__apis.md#ga550b642e071480323e589866abb99c22) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait) |
|  | Cause the current thread to busy wait. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_can\_yield](group__thread__apis.md#ga366b9daa0be65b0a69dbc9f146064b68) (void) |
|  | Check whether it is possible to yield in the current context. |
| void | [k\_yield](group__thread__apis.md#ga08a3484c33444ecedc2d71d78495a295) (void) |
|  | Yield the current thread. |
| void | [k\_wakeup](group__thread__apis.md#ga9275a019c8ff3c7fe49a81f8c078157e) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Wake up a sleeping thread. |
| \_\_attribute\_const\_\_ [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_sched\_current\_thread\_query](group__thread__apis.md#gac3b994b90b5bccded0895304f6b20c5d) (void) |
|  | Query thread ID of the current thread. |
| static \_\_attribute\_const\_\_ [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_current\_get](group__thread__apis.md#ga7ef1ed0fb9513df8096ede1e52fc76b2) (void) |
|  | Get thread ID of the current thread. |
| void | [k\_thread\_abort](group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Abort a thread. |
| void | [k\_thread\_start](group__thread__apis.md#ga88031bd9fcfcd4305bae4029a4d8416f) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Start an inactive thread. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_thread\_timeout\_expires\_ticks](group__thread__apis.md#gab0b1c85b847fe74170c04538fa9949ff) (const struct [k\_thread](structk__thread.md) \*thread) |
|  | Get time when a thread wakes up, in system ticks. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_thread\_timeout\_remaining\_ticks](group__thread__apis.md#ga4688c095c86e037a18594efdb9a5e9b9) (const struct [k\_thread](structk__thread.md) \*thread) |
|  | Get time remaining before a thread wakes up, in system ticks. |
| int | [k\_thread\_priority\_get](group__thread__apis.md#ga3a46ed8ad2c3b12416fafe11325f82b3) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Get a thread's priority. |
| void | [k\_thread\_priority\_set](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int prio) |
|  | Set a thread's priority. |
| void | [k\_thread\_deadline\_set](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int deadline) |
|  | Set deadline expiration time for scheduler. |
| int | [k\_thread\_cpu\_mask\_clear](group__thread__apis.md#ga80b9c58df6600c7e79f16756c128f44c) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Sets all CPU enable masks to zero. |
| int | [k\_thread\_cpu\_mask\_enable\_all](group__thread__apis.md#gaedcfeb0964ae72611791241580b2119d) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Sets all CPU enable masks to one. |
| int | [k\_thread\_cpu\_mask\_enable](group__thread__apis.md#ga306587604a7496db8059bd395fd90fc0) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu) |
|  | Enable thread to run on specified CPU. |
| int | [k\_thread\_cpu\_mask\_disable](group__thread__apis.md#ga89e6c07ac112da75b2ef115d1a557d44) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu) |
|  | Prevent thread to run on specified CPU. |
| int | [k\_thread\_cpu\_pin](group__thread__apis.md#gae9ebd9845e14ed02944ab9282a185c03) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, int cpu) |
|  | Pin a thread to a CPU. |
| void | [k\_thread\_suspend](group__thread__apis.md#ga66cf8682fb65870eceb5e57d667a8d4e) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Suspend a thread. |
| void | [k\_thread\_resume](group__thread__apis.md#ga117b26f8569ec3045ead1fad1851663d) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Resume a suspended thread. |
| void | [k\_sched\_time\_slice\_set](group__thread__apis.md#ga877c1bfeffbf8f097d1656f9e10a66e8) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice, int prio) |
|  | Set time-slicing period and scope. |
| void | [k\_thread\_time\_slice\_set](group__thread__apis.md#ga563928f292a4134acd4142029b60e631) (struct [k\_thread](structk__thread.md) \*th, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks, [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) expired, void \*data) |
|  | Set thread time slice. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_in\_isr](group__isr__apis.md#ga8482b0dd2283d12677a9ebe321667d16) (void) |
|  | Determine if code is running at interrupt level. |
| int | [k\_is\_preempt\_thread](group__isr__apis.md#ga91e1cf0dc7fc93a3214cadb74ed86666) (void) |
|  | Determine if code is running in a preemptible thread. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_is\_pre\_kernel](group__isr__apis.md#gae74e5de996276df767b96d4b50fa47ea) (void) |
|  | Test whether startup is in the before-main-task phase. |
| void | [k\_sched\_lock](group__thread__apis.md#ga4f0c5d0b9f279b12a4ad97db0c116a5f) (void) |
|  | Lock the scheduler. |
| void | [k\_sched\_unlock](group__thread__apis.md#ga7b26f64523cc4c36522cc828ccf85580) (void) |
|  | Unlock the scheduler. |
| void | [k\_thread\_custom\_data\_set](group__thread__apis.md#ga4834d9b81ed60c00eee77b0d4f8ab9e4) (void \*value) |
|  | Set current thread's custom data. |
| void \* | [k\_thread\_custom\_data\_get](group__thread__apis.md#ga19af063cff7b306ba28062996922740d) (void) |
|  | Get current thread's custom data. |
| int | [k\_thread\_name\_set](group__thread__apis.md#ga23107333f134b9c9a8b692374211e841) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, const char \*str) |
|  | Set current thread name. |
| const char \* | [k\_thread\_name\_get](group__thread__apis.md#gadebf45da56dee393164569742459dc0a) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Get thread name. |
| int | [k\_thread\_name\_copy](group__thread__apis.md#ga07b59ade055c69929ccdc08a14361794) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Copy the thread name into a supplied buffer. |
| const char \* | [k\_thread\_state\_str](group__thread__apis.md#ga0c6af32096dc7ca391ffe2522bae4cb6) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_size) |
|  | Get thread state string. |
| void | [k\_timer\_init](group__timer__apis.md#ga318c846a740b901e5d56876a47ad7f61) (struct k\_timer \*timer, [k\_timer\_expiry\_t](group__timer__apis.md#ga2915762e70454d98c73c179a45cafbde) expiry\_fn, [k\_timer\_stop\_t](group__timer__apis.md#ga106733712fc4e62b59bbe6a480bb988c) stop\_fn) |
|  | Initialize a timer. |
| void | [k\_timer\_start](group__timer__apis.md#ga3ba70e9f059ff52fd2057ab89ea7f2ee) (struct k\_timer \*timer, [k\_timeout\_t](structk__timeout__t.md) duration, [k\_timeout\_t](structk__timeout__t.md) period) |
|  | Start a timer. |
| void | [k\_timer\_stop](group__timer__apis.md#ga8d3e3356a10d36570e16f7920e4c8772) (struct k\_timer \*timer) |
|  | Stop a timer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_timer\_status\_get](group__timer__apis.md#gad532f4834cd4cf8be27b089e6ea347ce) (struct k\_timer \*timer) |
|  | Read timer status. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_timer\_status\_sync](group__timer__apis.md#ga81d6d95b7021e26ad4cab161318e04f2) (struct k\_timer \*timer) |
|  | Synchronize thread to timer expiration. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_timer\_expires\_ticks](group__timer__apis.md#ga022b4cf5c8d0ee21b6a3b04fd425533f) (const struct k\_timer \*timer) |
|  | Get next expiration time of a timer, in system ticks. |
| [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_timer\_remaining\_ticks](group__timer__apis.md#ga1176b36b960e786f68eaededf99a88b4) (const struct k\_timer \*timer) |
|  | Get time remaining before a timer next expires, in system ticks. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_timer\_remaining\_get](group__timer__apis.md#ga6c6d8b0aa59bfa0f5924e95ccf756259) (struct k\_timer \*timer) |
|  | Get time remaining before a timer next expires. |
| void | [k\_timer\_user\_data\_set](group__timer__apis.md#gadba1884961e790dd9c5d567de91cc7e2) (struct k\_timer \*timer, void \*user\_data) |
|  | Associate user-specific data with a timer. |
| void \* | [k\_timer\_user\_data\_get](group__timer__apis.md#ga19a7d99a01a83828efd7f0d3bf2dd358) (const struct k\_timer \*timer) |
|  | Retrieve the user-specific data from a timer. |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13) (void) |
|  | Get system uptime, in system ticks. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [k\_uptime\_get](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69) (void) |
|  | Get system uptime. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_uptime\_get\_32](group__clock__apis.md#ga9253cfb7b46af4d8994349323ce9872b) (void) |
|  | Get system uptime (32-bit version). |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_uptime\_seconds](group__clock__apis.md#gae082928ea608a8b180b4cb3a79d21a24) (void) |
|  | Get system uptime in seconds. |
| static [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [k\_uptime\_delta](group__clock__apis.md#gad748b2fe83b36884dc087b4af367de80) ([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*reftime) |
|  | Get elapsed time. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3) (void) |
|  | Read the hardware clock. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [k\_cycle\_get\_64](group__clock__apis.md#gae09f509d02bf75a7b45d2800d823bb3a) (void) |
|  | Read the 64-bit hardware clock. |
| void | [k\_queue\_init](group__queue__apis.md#ga0236222d42768c2bf00942f328146c21) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Initialize a queue. |
| void | [k\_queue\_cancel\_wait](group__queue__apis.md#ga7c39d86cc6509f59ff9223cac3ea5071) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Cancel waiting on a queue. |
| void | [k\_queue\_append](group__queue__apis.md#gaa84522a5ace6e7f8ba61033baca6972f) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Append an element to the end of a queue. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_queue\_alloc\_append](group__queue__apis.md#ga690f3a1450e946d75f31b3e499d1d06a) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Append an element to a queue. |
| void | [k\_queue\_prepend](group__queue__apis.md#ga8ce013d8a037d4be5078797e0050e9c6) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Prepend an element to a queue. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_queue\_alloc\_prepend](group__queue__apis.md#gacf3dba40125073c11075e5a134919f88) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Prepend an element to a queue. |
| void | [k\_queue\_insert](group__queue__apis.md#gad47336f27e433a52600a3b67ab89556a) (struct [k\_queue](structk__queue.md) \*queue, void \*prev, void \*data) |
|  | Inserts an element to a queue. |
| int | [k\_queue\_append\_list](group__queue__apis.md#ga91d1a144fc2aeb3dd655accc94ca43aa) (struct [k\_queue](structk__queue.md) \*queue, void \*head, void \*tail) |
|  | Atomically append a list of elements to a queue. |
| int | [k\_queue\_merge\_slist](group__queue__apis.md#ga4eee0da7442d60572b05d60a9996e69d) (struct [k\_queue](structk__queue.md) \*queue, [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list) |
|  | Atomically add a list of elements to a queue. |
| void \* | [k\_queue\_get](group__queue__apis.md#ga0a77d8556e7d253319275de034f01619) (struct [k\_queue](structk__queue.md) \*queue, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Get an element from a queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_queue\_remove](group__queue__apis.md#ga4bff929ed1d366a06e00865a5bbe2544) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Remove an element from a queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_queue\_unique\_append](group__queue__apis.md#ga287a2d81e2e3041be1cd45164e72f127) (struct [k\_queue](structk__queue.md) \*queue, void \*data) |
|  | Append an element to a queue only if it's not present already. |
| int | [k\_queue\_is\_empty](group__queue__apis.md#gadb2bb8088868b3c5801c72b320389ca9) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Query a queue to see if it has data available. |
| void \* | [k\_queue\_peek\_head](group__queue__apis.md#ga8ccd5137690c127a0f7d67619b88a52b) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Peek element at the head of queue. |
| void \* | [k\_queue\_peek\_tail](group__queue__apis.md#ga27a460c42836d8b093ad9274c14bb176) (struct [k\_queue](structk__queue.md) \*queue) |
|  | Peek element at the tail of queue. |
| int | [k\_futex\_wait](group__futex__apis.md#ga596bfa265f88567ad9e80fd38cd433d3) (struct [k\_futex](structk__futex.md) \*futex, int expected, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Pend the current thread on a futex. |
| int | [k\_futex\_wake](group__futex__apis.md#ga62de1aeb7c5c273aed20d0e05336d7a0) (struct [k\_futex](structk__futex.md) \*futex, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wake\_all) |
|  | Wake one/all threads pending on a futex. |
| void | [k\_event\_init](group__event__apis.md#gacf803590b39b095056f2b1c5090c4019) (struct [k\_event](structk__event.md) \*event) |
|  | Initialize an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_post](group__event__apis.md#gac88d17410a71642a903890e420d23d76) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events) |
|  | Post one or more events to an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_set](group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events) |
|  | Set the events in an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_set\_masked](group__event__apis.md#ga29b3ec1022b12a8c34884da3559c5864) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask) |
|  | Set or clear the events in an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_clear](group__event__apis.md#gad6bfd7bfd0587bc70d3aa0b988010376) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events) |
|  | Clear the events in an event object. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_wait](group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reset, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for any of the specified events. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_wait\_all](group__event__apis.md#gaddd60a99de5ac3d84f643c9433b744c1) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reset, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for all of the specified events. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_event\_test](group__event__apis.md#ga81e66be0959e8cb0414d9772056a6264) (struct [k\_event](structk__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events\_mask) |
|  | Test the events currently tracked in the event object. |
| void | [k\_stack\_init](group__stack__apis.md#ga4400a39ef48289305cf66a092d5c6c7d) (struct k\_stack \*stack, stack\_data\_t \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries) |
|  | Initialize a stack. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [k\_stack\_alloc\_init](group__stack__apis.md#gab97d924db1aef3f6adade156a107d45c) (struct k\_stack \*stack, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_entries) |
|  | Initialize a stack. |
| int | [k\_stack\_cleanup](group__stack__apis.md#ga819f4e7b2cf11cf2e1b80933fdcb67ea) (struct k\_stack \*stack) |
|  | Release a stack's allocated buffer. |
| int | [k\_stack\_push](group__stack__apis.md#gaa6180f4db6ec93ee84149cba054d3e53) (struct k\_stack \*stack, stack\_data\_t data) |
|  | Push an element onto a stack. |
| int | [k\_stack\_pop](group__stack__apis.md#ga36ce6ceb9ea3d5c36d22b10430789480) (struct k\_stack \*stack, stack\_data\_t \*data, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Pop an element from a stack. |
| int | [k\_mutex\_init](group__mutex__apis.md#ga56b64952fb8b78b00268a21c28b41480) (struct [k\_mutex](structk__mutex.md) \*mutex) |
|  | Initialize a mutex. |
| int | [k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0) (struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Lock a mutex. |
| int | [k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31) (struct [k\_mutex](structk__mutex.md) \*mutex) |
|  | Unlock a mutex. |
| int | [k\_condvar\_init](group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc) (struct [k\_condvar](structk__condvar.md) \*condvar) |
|  | Initialize a condition variable. |
| int | [k\_condvar\_signal](group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b) (struct [k\_condvar](structk__condvar.md) \*condvar) |
|  | Signals one thread that is pending on the condition variable. |
| int | [k\_condvar\_broadcast](group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8) (struct [k\_condvar](structk__condvar.md) \*condvar) |
|  | Unblock all threads that are pending on the condition variable. |
| int | [k\_condvar\_wait](group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc) (struct [k\_condvar](structk__condvar.md) \*condvar, struct [k\_mutex](structk__mutex.md) \*mutex, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Waits on the condition variable releasing the mutex lock. |
| int | [k\_sem\_init](group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845) (struct k\_sem \*sem, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int initial\_count, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int limit) |
|  | Initialize a semaphore. |
| int | [k\_sem\_take](group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090) (struct k\_sem \*sem, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Take a semaphore. |
| void | [k\_sem\_give](group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84) (struct k\_sem \*sem) |
|  | Give a semaphore. |
| void | [k\_sem\_reset](group__semaphore__apis.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562) (struct k\_sem \*sem) |
|  | Resets a semaphore's count to zero. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [k\_sem\_count\_get](group__semaphore__apis.md#ga58843b581e170a1811fc38eecbfd01f3) (struct k\_sem \*sem) |
|  | Get a semaphore's count. |
| void | [k\_work\_init](group__workqueue__apis.md#gaf20080884a2893d39cd8e862b34a2a30) (struct [k\_work](structk__work.md) \*work, [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) handler) |
|  | Initialize a (non-delayable) work structure. |
| int | [k\_work\_busy\_get](group__workqueue__apis.md#gaba8a8734768d768b433f9d8490e7df7b) (const struct [k\_work](structk__work.md) \*work) |
|  | Busy state flags from the work item. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_is\_pending](group__workqueue__apis.md#ga0d1d2e1d2ba2e89a560a1bdc5365d9e0) (const struct [k\_work](structk__work.md) \*work) |
|  | Test whether a work item is currently pending. |
| int | [k\_work\_submit\_to\_queue](group__workqueue__apis.md#ga5353e76f73db070614f50d06d292d05c) (struct [k\_work\_q](structk__work__q.md) \*queue, struct [k\_work](structk__work.md) \*work) |
|  | Submit a work item to a queue. |
| int | [k\_work\_submit](group__workqueue__apis.md#gace61b59575093d7442f39ccb7be686d7) (struct [k\_work](structk__work.md) \*work) |
|  | Submit a work item to the system queue. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_flush](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253) (struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Wait for last-submitted instance to complete. |
| int | [k\_work\_cancel](group__workqueue__apis.md#ga389fe2a8fb20f9bd593cf8d990727078) (struct [k\_work](structk__work.md) \*work) |
|  | Cancel a work item. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_cancel\_sync](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9) (struct [k\_work](structk__work.md) \*work, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Cancel a work item and wait for it to complete. |
| void | [k\_work\_queue\_init](group__workqueue__apis.md#gada77d818ea9e4d07c14a960872ed5492) (struct [k\_work\_q](structk__work__q.md) \*queue) |
|  | Initialize a work queue structure. |
| void | [k\_work\_queue\_start](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593) (struct [k\_work\_q](structk__work__q.md) \*queue, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size, int prio, const struct [k\_work\_queue\_config](structk__work__queue__config.md) \*cfg) |
|  | Initialize a work queue. |
| static [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_work\_queue\_thread\_get](group__workqueue__apis.md#ga0b8b496f7e7bd82d08590a07293e38d7) (struct [k\_work\_q](structk__work__q.md) \*queue) |
|  | Access the thread that animates a work queue. |
| int | [k\_work\_queue\_drain](group__workqueue__apis.md#ga0fefe3e0225ac99b47b250849f6cd863) (struct [k\_work\_q](structk__work__q.md) \*queue, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) plug) |
|  | Wait until the work queue has drained, optionally plugging it. |
| int | [k\_work\_queue\_unplug](group__workqueue__apis.md#gaa0463bb79af3ec470f7d3be02052139f) (struct [k\_work\_q](structk__work__q.md) \*queue) |
|  | Release a work queue to accept new submissions. |
| void | [k\_work\_init\_delayable](group__workqueue__apis.md#ga2876c5d82fb2340a093bc4d689a55465) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) handler) |
|  | Initialize a delayable work structure. |
| static struct [k\_work\_delayable](structk__work__delayable.md) \* | [k\_work\_delayable\_from\_work](group__workqueue__apis.md#gabcb822a03ce7ea9ee1ed046afe31ffca) (struct [k\_work](structk__work.md) \*work) |
|  | Get the parent delayable work structure from a work pointer. |
| int | [k\_work\_delayable\_busy\_get](group__workqueue__apis.md#ga1b76969667844f0981d348c9c671bc9f) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Busy state flags from the delayable work item. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_delayable\_is\_pending](group__workqueue__apis.md#ga66e598dbc73f653cbfec03c21168df2e) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Test whether a delayed work item is currently pending. |
| static [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_work\_delayable\_expires\_get](group__workqueue__apis.md#ga1772c37bc62b86180d5cf48fe3037624) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Get the absolute tick count at which a scheduled delayable work will be submitted. |
| static [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) | [k\_work\_delayable\_remaining\_get](group__workqueue__apis.md#gabce78598a014f3ed87730fe6a9fe61b4) (const struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Get the number of ticks until a scheduled delayable work will be submitted. |
| int | [k\_work\_schedule\_for\_queue](group__workqueue__apis.md#ga17f863c9f6ff2fb41dc0f3b7de4fdf23) (struct [k\_work\_q](structk__work__q.md) \*queue, struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Submit an idle work item to a queue after a delay. |
| int | [k\_work\_schedule](group__workqueue__apis.md#ga5c113ea2bc8e8e5cd7a5c8bc5ec595d3) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Submit an idle work item to the system work queue after a delay. |
| int | [k\_work\_reschedule\_for\_queue](group__workqueue__apis.md#gabf5db091eac19b19a4e12c0cb381f0a8) (struct [k\_work\_q](structk__work__q.md) \*queue, struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Reschedule a work item to a queue after a delay. |
| int | [k\_work\_reschedule](group__workqueue__apis.md#gaacaab408fb7c848d466ad1f069dfa648) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Reschedule a work item to the system work queue after a delay. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_flush\_delayable](group__workqueue__apis.md#gad47d54e513030304be2600d75b1a965f) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Flush delayable work. |
| int | [k\_work\_cancel\_delayable](group__workqueue__apis.md#ga92355914ee178d4c3e848a1946bed3e4) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork) |
|  | Cancel delayable work. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_cancel\_delayable\_sync](group__workqueue__apis.md#ga7e7ec237648556fc16bfda8d35f7cd86) (struct [k\_work\_delayable](structk__work__delayable.md) \*dwork, struct [k\_work\_sync](structk__work__sync.md) \*sync) |
|  | Cancel delayable work and wait. |
| static void | [k\_work\_user\_init](group__workqueue__apis.md#ga9de9c7a7f13cc6b325e5453e34afe62d) (struct k\_work\_user \*work, [k\_work\_user\_handler\_t](group__workqueue__apis.md#gaafa4dfac323cab570da1ee31c07d11bc) handler) |
|  | Initialize a userspace work item. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_work\_user\_is\_pending](group__workqueue__apis.md#ga58d05d4127e4cd51104a1f1a87f626cd) (struct k\_work\_user \*work) |
|  | Check if a userspace work item is pending. |
| static int | [k\_work\_user\_submit\_to\_queue](group__workqueue__apis.md#ga50ae1f6f74c0bc0a41dbbf789fff8856) (struct k\_work\_user\_q \*work\_q, struct k\_work\_user \*work) |
|  | Submit a work item to a user mode workqueue. |
| void | [k\_work\_user\_queue\_start](group__workqueue__apis.md#ga3091bc8fab5311252e41634a97a18589) (struct k\_work\_user\_q \*work\_q, [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stack\_size, int prio, const char \*name) |
|  | Start a workqueue in user mode. |
| static [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [k\_work\_user\_queue\_thread\_get](group__workqueue__apis.md#gab487068e9564cd77b6bdbac3d5670923) (struct k\_work\_user\_q \*work\_q) |
|  | Access the user mode thread that animates a work queue. |
| void | [k\_work\_poll\_init](group__workqueue__apis.md#ga371dab33a40622bea19b07d852863443) (struct k\_work\_poll \*work, [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) handler) |
|  | Initialize a triggered work item. |
| int | [k\_work\_poll\_submit\_to\_queue](group__workqueue__apis.md#ga0abafd7f851e42fd3572c8438e600a53) (struct [k\_work\_q](structk__work__q.md) \*work\_q, struct k\_work\_poll \*work, struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Submit a triggered work item. |
| int | [k\_work\_poll\_submit](group__workqueue__apis.md#gad9f222e46d72c4f98739395a0c8bb4ea) (struct k\_work\_poll \*work, struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Submit a triggered work item to the system workqueue. |
| int | [k\_work\_poll\_cancel](group__workqueue__apis.md#ga2a19547d04dc1a202e80b752e3177215) (struct k\_work\_poll \*work) |
|  | Cancel a triggered work item. |
| void | [k\_msgq\_init](group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39) (struct [k\_msgq](structk__msgq.md) \*msgq, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs) |
|  | Initialize a message queue. |
| int | [k\_msgq\_alloc\_init](group__msgq__apis.md#gabe7305b8f442ebdc147dbbc6e8cf92fc) (struct [k\_msgq](structk__msgq.md) \*msgq, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msg\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_msgs) |
|  | Initialize a message queue. |
| int | [k\_msgq\_cleanup](group__msgq__apis.md#gafda4399aa9b8f1e44bdf752e00ea787b) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Release allocated buffer for a queue. |
| int | [k\_msgq\_put](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe) (struct [k\_msgq](structk__msgq.md) \*msgq, const void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Send a message to a message queue. |
| int | [k\_msgq\_get](group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7) (struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Receive a message from a message queue. |
| int | [k\_msgq\_peek](group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915) (struct [k\_msgq](structk__msgq.md) \*msgq, void \*data) |
|  | Peek/read a message from a message queue. |
| int | [k\_msgq\_peek\_at](group__msgq__apis.md#ga69b004a40ab4ca497de314a99960fb8e) (struct [k\_msgq](structk__msgq.md) \*msgq, void \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx) |
|  | Peek/read a message from a message queue at the specified index. |
| void | [k\_msgq\_purge](group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Purge a message queue. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_msgq\_num\_free\_get](group__msgq__apis.md#ga7d154beb4f9c6227eddbef26d406ca24) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Get the amount of free space in a message queue. |
| void | [k\_msgq\_get\_attrs](group__msgq__apis.md#ga8f9d3eef67cbc9c0717a84190bbf7f41) (struct [k\_msgq](structk__msgq.md) \*msgq, struct [k\_msgq\_attrs](structk__msgq__attrs.md) \*attrs) |
|  | Get basic attributes of a message queue. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_msgq\_num\_used\_get](group__msgq__apis.md#ga458793a89f1d9f762bda3422918a9faa) (struct [k\_msgq](structk__msgq.md) \*msgq) |
|  | Get the number of messages in a message queue. |
| void | [k\_mbox\_init](group__mailbox__apis.md#ga686f20c199a9e971822d8279d175d8c2) (struct [k\_mbox](structk__mbox.md) \*mbox) |
|  | Initialize a mailbox. |
| int | [k\_mbox\_put](group__mailbox__apis.md#gaa1e5cdd992d8b9be11f82254e1886ed2) (struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Send a mailbox message in a synchronous manner. |
| void | [k\_mbox\_async\_put](group__mailbox__apis.md#gadd60f7b760371c0a141a1e4da253a0f0) (struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*tx\_msg, struct k\_sem \*sem) |
|  | Send a mailbox message in an asynchronous manner. |
| int | [k\_mbox\_get](group__mailbox__apis.md#ga2ea91154620b139dbed1ad949b97c3ef) (struct [k\_mbox](structk__mbox.md) \*mbox, struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Receive a mailbox message. |
| void | [k\_mbox\_data\_get](group__mailbox__apis.md#ga3d19e648e67f109609259543c9a01d6e) (struct [k\_mbox\_msg](structk__mbox__msg.md) \*rx\_msg, void \*buffer) |
|  | Retrieve mailbox message data into a buffer. |
| void | [k\_pipe\_init](group__pipe__apis.md#gae9e807fb63bb7186b87015664f2c762d) (struct [k\_pipe](structk__pipe.md) \*pipe, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Initialize a pipe. |
| int | [k\_pipe\_cleanup](group__pipe__apis.md#gaad0ab1b97b537da408031e4bcbe04f36) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Release a pipe's allocated buffer. |
| int | [k\_pipe\_alloc\_init](group__pipe__apis.md#ga32a902a5d12ca54b17c2b58783214613) (struct [k\_pipe](structk__pipe.md) \*pipe, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Initialize a pipe and allocate a buffer for it. |
| int | [k\_pipe\_put](group__pipe__apis.md#gaff77638ad7217974a10c23a0a7e336ae) (struct [k\_pipe](structk__pipe.md) \*pipe, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes\_to\_write, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*bytes\_written, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Write data to a pipe. |
| int | [k\_pipe\_get](group__pipe__apis.md#gada9aaf9a336d98a95441212f4223e9ef) (struct [k\_pipe](structk__pipe.md) \*pipe, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes\_to\_read, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*bytes\_read, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read data from a pipe. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_pipe\_read\_avail](group__pipe__apis.md#ga21849ebf856532de6e3ea38489071220) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Query the number of bytes that may be read from *pipe*. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_pipe\_write\_avail](group__pipe__apis.md#gaff3ed3e93591d72c60a3640d195998c3) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Query the number of bytes that may be written to *pipe*. |
| void | [k\_pipe\_flush](group__pipe__apis.md#ga41484bb5c7dcd97e7a7b7f1422f8026f) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Flush the pipe of write data. |
| void | [k\_pipe\_buffer\_flush](group__pipe__apis.md#ga71e0e38a15fa27f27c1f028223936445) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Flush the pipe's internal buffer. |
| int | [k\_mem\_slab\_init](group__mem__slab__apis.md#ga094a8f173f287e29bb287119c26889d1) (struct k\_mem\_slab \*slab, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) block\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks) |
|  | Initialize a memory slab. |
| int | [k\_mem\_slab\_alloc](group__mem__slab__apis.md#gab16a46d8394aca18de740ad044a8734a) (struct k\_mem\_slab \*slab, void \*\*mem, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate memory from a memory slab. |
| void | [k\_mem\_slab\_free](group__mem__slab__apis.md#ga2635ea8f9a30b8751ec966fe62adc0e1) (struct k\_mem\_slab \*slab, void \*mem) |
|  | Free memory allocated from a memory slab. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_slab\_num\_used\_get](group__mem__slab__apis.md#gac76b96d7055e4ad94765c93530dd0720) (struct k\_mem\_slab \*slab) |
|  | Get the number of used blocks in a memory slab. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_slab\_max\_used\_get](group__mem__slab__apis.md#gae0e949c1c3476dd57bc0c0ed627d2346) (struct k\_mem\_slab \*slab) |
|  | Get the number of maximum used blocks so far in a memory slab. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_slab\_num\_free\_get](group__mem__slab__apis.md#gae87577e2873cf746db69216a82f94aea) (struct k\_mem\_slab \*slab) |
|  | Get the number of unused blocks in a memory slab. |
| int | [k\_mem\_slab\_runtime\_stats\_get](group__mem__slab__apis.md#ga32030a5cfb44f663bd31b4e1b3d5dddb) (struct k\_mem\_slab \*slab, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats) |
|  | Get the memory stats for a memory slab. |
| int | [k\_mem\_slab\_runtime\_stats\_reset\_max](group__mem__slab__apis.md#gaa1f44e30f4aee98b38e1ab5e93af505c) (struct k\_mem\_slab \*slab) |
|  | Reset the maximum memory usage for a slab. |
| void | [k\_heap\_init](group__heap__apis.md#ga9273e06dc8d6a351499f2f5abfdcb39f) (struct [k\_heap](structk__heap.md) \*h, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Initialize a [k\_heap](structk__heap.md). |
| void \* | [k\_heap\_aligned\_alloc](group__heap__apis.md#gaf77211a72441de389857bc13e10be4e6) (struct [k\_heap](structk__heap.md) \*h, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate aligned memory from a [k\_heap](structk__heap.md). |
| void \* | [k\_heap\_alloc](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512) (struct [k\_heap](structk__heap.md) \*h, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate memory from a [k\_heap](structk__heap.md). |
| void \* | [k\_heap\_realloc](group__heap__apis.md#gabea4b2beae8ab138f2796fbeaa95d262) (struct [k\_heap](structk__heap.md) \*h, void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Reallocate memory from a [k\_heap](structk__heap.md). |
| void | [k\_heap\_free](group__heap__apis.md#ga6cf917a0b3d91a0101192bd4808ada9c) (struct [k\_heap](structk__heap.md) \*h, void \*mem) |
|  | Free memory allocated by [k\_heap\_alloc()](group__heap__apis.md#ga22b83564e50ae6177388dfe63e32a512 "Allocate memory from a k_heap."). |
| void \* | [k\_aligned\_alloc](group__heap__apis.md#gae16d486aa250f9c07fa6a57342bcd3b4) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate memory from the heap with a specified alignment. |
| void \* | [k\_malloc](group__heap__apis.md#gaa8edf1e63e5d5dd78d7adcfd787394ee) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate memory from the heap. |
| void | [k\_free](group__heap__apis.md#ga79b63cc93b3358cf82d74f40e73b69d5) (void \*ptr) |
|  | Free memory allocated from heap. |
| void \* | [k\_calloc](group__heap__apis.md#gad031d50ed62d08202a5dcf992c20246c) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nmemb, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate memory from heap, array style. |
| void \* | [k\_realloc](group__heap__apis.md#ga852a7a60dce5853b6925897b24a54e02) (void \*ptr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Expand the size of an existing allocation. |
| void | [k\_poll\_event\_init](group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03) (struct [k\_poll\_event](structk__poll__event.md) \*event, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type, int mode, void \*obj) |
|  | Initialize one struct [k\_poll\_event](structk__poll__event.md "Poll Event.") instance. |
| int | [k\_poll](group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) (struct [k\_poll\_event](structk__poll__event.md) \*events, int num\_events, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Wait for one or many of multiple poll events to occur. |
| void | [k\_poll\_signal\_init](group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Initialize a poll signal object. |
| void | [k\_poll\_signal\_reset](group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig) |
|  | Reset a poll signal object's state to unsignaled. |
| void | [k\_poll\_signal\_check](group__poll__apis.md#ga69dae11c7cb2c669caa411c3e7001311) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*signaled, int \*result) |
|  | Fetch the signaled state and result value of a poll signal. |
| int | [k\_poll\_signal\_raise](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723) (struct [k\_poll\_signal](structk__poll__signal.md) \*sig, int result) |
|  | Signal a poll signal object. |
| static void | [k\_cpu\_idle](group__cpu__idle__apis.md#ga7b25e1bed511a813b32fbd0f91b09356) (void) |
|  | Make the CPU idle. |
| static void | [k\_cpu\_atomic\_idle](group__cpu__idle__apis.md#gadf88ece6447b65b7d0d2f3a70ab4fe8f) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
|  | Make the CPU idle in an atomic fashion. |
| int | [k\_float\_disable](group__float__apis.md#ga2df4b2550ace30512cddebd36b6a54a1) (struct [k\_thread](structk__thread.md) \*thread) |
|  | Disable preservation of floating point context information. |
| int | [k\_float\_enable](group__float__apis.md#ga81fb955ddd41658a9aad5c083f173f77) (struct [k\_thread](structk__thread.md) \*thread, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int options) |
|  | Enable preservation of floating point context information. |
| int | [k\_thread\_runtime\_stats\_get](#a82d886a1c911b39c1b47c32200cedac6) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread, [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats) |
|  | Get the runtime statistics of a thread. |
| int | [k\_thread\_runtime\_stats\_all\_get](#abd855bb83b3be393b46833e7854a193e) ([k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \*stats) |
|  | Get the runtime statistics of all threads. |
| int | [k\_thread\_runtime\_stats\_enable](#a3e52beb93fca2231d5860fe1cf1181fd) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Enable gathering of runtime statistics for specified thread. |
| int | [k\_thread\_runtime\_stats\_disable](#ae5ea2e05a602b7d5ee78a65ced61d63b) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Disable gathering of runtime statistics for specified thread. |
| void | [k\_sys\_runtime\_stats\_enable](#a54f2652ba1ed613219941eaaf193180c) (void) |
|  | Enable gathering of system runtime statistics. |
| void | [k\_sys\_runtime\_stats\_disable](#a2e3c96c0b11108ee7eca3f0666c780e0) (void) |
|  | Disable gathering of system runtime statistics. |

## Detailed Description

Public kernel APIs.

## Macro Definition Documentation

## [◆ ](#ac627cc4c3da16be4b74f0a4ab036a603)K\_ANY

| #define K\_ANY   NULL |
| --- |

## [◆ ](#ab326c7eb1d248650e6017dcaee8d24b2)K\_HIGHEST\_APPLICATION\_THREAD\_PRIO

| #define K\_HIGHEST\_APPLICATION\_THREAD\_PRIO   ([K\_HIGHEST\_THREAD\_PRIO](#a5fd4365cb6e8742e750b5e4950fb1e47)) |
| --- |

## [◆ ](#a5fd4365cb6e8742e750b5e4950fb1e47)K\_HIGHEST\_THREAD\_PRIO

| #define K\_HIGHEST\_THREAD\_PRIO   (-CONFIG\_NUM\_COOP\_PRIORITIES) |
| --- |

## [◆ ](#a8f3f1d910dd847f0b223a4aa00788fa2)K\_IDLE\_PRIO

| #define K\_IDLE\_PRIO   [K\_LOWEST\_THREAD\_PRIO](#afa4bcc2fdfea5cd7c63d56f476b1b32f) |
| --- |

## [◆ ](#ad4c2df561988fa1194c2f8c768d667cd)K\_LOWEST\_APPLICATION\_THREAD\_PRIO

| #define K\_LOWEST\_APPLICATION\_THREAD\_PRIO   ([K\_LOWEST\_THREAD\_PRIO](#afa4bcc2fdfea5cd7c63d56f476b1b32f) - 1) |
| --- |

## [◆ ](#afa4bcc2fdfea5cd7c63d56f476b1b32f)K\_LOWEST\_THREAD\_PRIO

| #define K\_LOWEST\_THREAD\_PRIO   CONFIG\_NUM\_PREEMPT\_PRIORITIES |
| --- |

## [◆ ](#abde5aa8ca5e64a045b25b88f91370dcd)k\_oops

| #define k\_oops | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

z\_except\_reason([K\_ERR\_KERNEL\_OOPS](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3))

[K\_ERR\_KERNEL\_OOPS](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3)

@ K\_ERR\_KERNEL\_OOPS

Moderate severity software error.

**Definition** fatal\_types.h:35

Fatally terminate a thread.

This should be called when a thread has encountered an unrecoverable runtime condition and needs to terminate. What this ultimately means is determined by the \_fatal\_error\_handler() implementation, which will be called will reason code K\_ERR\_KERNEL\_OOPS.

If this is called from ISR context, the default system fatal error handler will treat it as an unrecoverable system error, just like [k\_panic()](#aedd541f707b1463aaac15c7798340329).

## [◆ ](#aedd541f707b1463aaac15c7798340329)k\_panic

| #define k\_panic | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

z\_except\_reason([K\_ERR\_KERNEL\_PANIC](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617))

[K\_ERR\_KERNEL\_PANIC](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617)

@ K\_ERR\_KERNEL\_PANIC

High severity software error.

**Definition** fatal\_types.h:38

Fatally terminate the system.

This should be called when the Zephyr kernel has encountered an unrecoverable runtime condition and needs to terminate. What this ultimately means is determined by the \_fatal\_error\_handler() implementation, which will be called will reason code K\_ERR\_KERNEL\_PANIC.

## [◆ ](#ac145d4747518572acfc8ee1579007d54)K\_PRIO\_COOP

| #define K\_PRIO\_COOP | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(-(CONFIG\_NUM\_COOP\_PRIORITIES - (x)))

## [◆ ](#aa0e916aae3ddd0e998cd41ac32afe30a)K\_PRIO\_PREEMPT

| #define K\_PRIO\_PREEMPT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(x)

## Enumeration Type Documentation

## [◆ ](#ab0b42f9804777dfa5fed2b7cd866779c)execution\_context\_types

| enum [execution\_context\_types](#ab0b42f9804777dfa5fed2b7cd866779c) |
| --- |

| Enumerator | |
| --- | --- |
| K\_ISR |  |
| K\_COOP\_THREAD |  |
| K\_PREEMPT\_THREAD |  |

## Function Documentation

## [◆ ](#a2e3c96c0b11108ee7eca3f0666c780e0)k\_sys\_runtime\_stats\_disable()

| void k\_sys\_runtime\_stats\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable gathering of system runtime statistics.

This routine disables the gathering of system runtime statistics. Note that it does not affect the gathering of similar statistics for individual threads.

## [◆ ](#a54f2652ba1ed613219941eaaf193180c)k\_sys\_runtime\_stats\_enable()

| void k\_sys\_runtime\_stats\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable gathering of system runtime statistics.

This routine enables the gathering of system runtime statistics. Note that it does not affect the gathering of similar statistics for individual threads.

## [◆ ](#abd855bb83b3be393b46833e7854a193e)k\_thread\_runtime\_stats\_all\_get()

| int k\_thread\_runtime\_stats\_all\_get | ( | [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \* | *stats* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the runtime statistics of all threads.

Parameters
:   | stats | Pointer to struct to copy statistics into. |
    | --- | --- |

Returns
:   -EINVAL if null pointers, otherwise 0

## [◆ ](#ae5ea2e05a602b7d5ee78a65ced61d63b)k\_thread\_runtime\_stats\_disable()

| int k\_thread\_runtime\_stats\_disable | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable gathering of runtime statistics for specified thread.

This routine disables the gathering of runtime statistics for the specified thread.

Parameters
:   | thread | ID of thread |
    | --- | --- |

Returns
:   -EINVAL if invalid thread ID, otherwise 0

## [◆ ](#a3e52beb93fca2231d5860fe1cf1181fd)k\_thread\_runtime\_stats\_enable()

| int k\_thread\_runtime\_stats\_enable | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable gathering of runtime statistics for specified thread.

This routine enables the gathering of runtime statistics for the specified thread.

Parameters
:   | thread | ID of thread |
    | --- | --- |

Returns
:   -EINVAL if invalid thread ID, otherwise 0

## [◆ ](#a82d886a1c911b39c1b47c32200cedac6)k\_thread\_runtime\_stats\_get()

| int k\_thread\_runtime\_stats\_get | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread*, |
| --- | --- | --- | --- |
|  |  | [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf) \* | *stats* ) |

Get the runtime statistics of a thread.

Parameters
:   | thread | ID of thread. |
    | --- | --- |
    | stats | Pointer to struct to copy statistics into. |

Returns
:   -EINVAL if null pointers, otherwise 0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel.h](kernel_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
