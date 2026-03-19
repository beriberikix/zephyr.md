---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/bluetooth-ctlr-arch.html
original_path: connectivity/bluetooth/bluetooth-ctlr-arch.html
---

# LE Controller

## Overview

![../../_images/ctlr_overview.png](../../_images/ctlr_overview.png)

1. HCI

   - Host Controller Interface, Bluetooth standard
   - Provides Zephyr Bluetooth HCI Driver
2. HAL

   - Hardware Abstraction Layer
   - Vendor Specific, and Zephyr Driver usage
3. Ticker

   - Soft real time radio/resource scheduling
4. LL\_SW

   - Software-based Link Layer implementation
   - States and roles, control procedures, packet controller
5. Util

   - Bare metal memory pool management
   - Queues of variable count, lockless usage
   - FIFO of fixed count, lockless usage
   - Mayfly concept based deferred ISR executions

## Architecture

### Execution Overview

![../../_images/ctlr_exec_overview.png](../../_images/ctlr_exec_overview.png)

### Architecture Overview

![../../_images/ctlr_arch_overview.png](../../_images/ctlr_arch_overview.png)

## Scheduling

![../../_images/ctlr_sched.png](../../_images/ctlr_sched.png)

### Ticker

![../../_images/ctlr_sched_ticker.png](../../_images/ctlr_sched_ticker.png)

### Upper Link Layer and Lower Link Layer

![../../_images/ctlr_sched_ull_lll.png](../../_images/ctlr_sched_ull_lll.png)

### Scheduling Variants

![../../_images/ctlr_sched_variant.png](../../_images/ctlr_sched_variant.png)

### ULL and LLL Timing

![../../_images/ctlr_sched_ull_lll_timing.png](../../_images/ctlr_sched_ull_lll_timing.png)

## Event Handling

![../../_images/ctlr_sched_event_handling.png](../../_images/ctlr_sched_event_handling.png)

### Scheduling Closely Spaced Events

![../../_images/ctlr_sched_msc_close_events.png](../../_images/ctlr_sched_msc_close_events.png)

### Aborting Active Event

![../../_images/ctlr_sched_msc_event_abort.png](../../_images/ctlr_sched_msc_event_abort.png)

### Cancelling Pending Event

![../../_images/ctlr_sched_msc_event_cancel.png](../../_images/ctlr_sched_msc_event_cancel.png)

### Pre-emption of Active Event

![../../_images/ctlr_sched_msc_event_preempt.png](../../_images/ctlr_sched_msc_event_preempt.png)

## Data Flow

### Transmit Data Flow

![../../_images/ctlr_dataflow_tx.png](../../_images/ctlr_dataflow_tx.png)

### Receive Data Flow

![../../_images/ctlr_dataflow_rx.png](../../_images/ctlr_dataflow_rx.png)

## Execution Priorities

![../../_images/ctlr_exec_prio.png](../../_images/ctlr_exec_prio.png)

- Event handle (0, 1) < Event preparation (2, 3) < Event/Rx done (4) < Tx
  request (5) < Role management (6) < Host (7).
- LLL is vendor ISR, ULL is Mayfly ISR concept, Host is kernel thread.

## Link Layer Control Procedures

Following is a brief fly in on the main concepts in the implementation of
control procedures handling in ULL.

### Three main execution contexts

- HCI/LLCP API
  :   - Miscellaneous procedure initiation API
      - From ull\_llcp.c::ull\_cp\_<proc>() for initiating local procedures
      - Interface with running procedures, local and remote
- lll\_prepare context to drive ull\_cp\_run()
  :   - LLCP main state machine entry/tick’er
      - From ull\_peripheral.c/ull\_central.c::ticker\_cb via ull\_conn\_llcp()
- rx\_demux context to drive ull\_cp\_tx\_ack() and ull\_cp\_rx()
  :   - LLCP tx ack handling and PDU reception
      - From ull\_conn.c::ull\_conn\_rx()
      - Handles passing PDUs into running procedures as well as possibly initiating remote procedures

### Data structures and PDU helpers

- struct llcp\_struct
  :   - Main LLCP data store
      - Defined in ull\_conn\_types.h and declared as part of struct ll\_conn
      - Holds local and remote procedure request queues as well as conn specific LLCP data
      - Basic conn-level abstraction
- struct proc\_ctx
  :   - General procedure context data, contains miscellaneous procedure data and state as well as sys\_snode\_t for queueing
      - Defined in ull\_llcp\_internal.h, declared/instantiated through ull\_llcp.c::create\_procedure()
      - Also holds node references used in tx\_ack as well as rx\_node retention mechanisms
- struct llcp\_mem\_pool
  :   - Mem pool used to implement procedure contexts resource - instantiated in both a local and a remote version
      - Used through ull\_llcp.c::create\_procedure()
- Miscellaneous pdu gymnastics
  :   - Encoding and decoding of control pdus done by ull\_llcp\_pdu.c::llcp\_pdu\_encode/decode\_<PDU>()
      - Miscellaneous pdu validation handled by ull\_llcp.c::pdu\_validate\_<PDU>() via ull\_llcp.c::pdu\_is\_valid()

### LLCP local and remote request/procedure state machines

- ull\_llcp\_local.c
  :   - State machine handling local initiated procedures
      - Naming concept: lr \_<…> => local request machine
      - Local procedure queue handling
      - Local run/rx/tx\_ack switch
- ull\_llcp\_remote.c
  :   - Remote versions of the above
      - Naming concept: rr\_<…> => remote request machine
      - Also handling of remote procedure initiation by llcp\_rx\_new()
      - Miscellaneous procedure collision handling (in rr\_st\_idle())
- ull\_llcp\_common/conn\_upd/phy/enc/cc/chmu.c
  :   - Individual procedure implementations (ull\_llcp\_common.c collects the simpler ones)
      - Naming concept: lp\_<…> => local initiated procedure, rp\_<…> => remote initiated procedure
      - Handling of procedure flow from init (possibly through instant) to completion and host notification if applicable

### Miscellaneous concepts

- Procedure collision handling
  :   - See BT spec for explanation
      - Basically some procedures can exist in parallel but some can’t - for instance only one instant based at a time
      - Spec states rules for how to handle/resolve collisions when they happen
- Termination handling
  :   - Specific rules apply re. how termination is handled.
      - Since we have resource handling re. procedure contexts and terminate must always be available this is handled as a special case
      - Note also - there are miscellaneous cases where connection termination is triggered on invalid peer behavior
- New remote procedure handling
  :   - Table new\_proc\_lut[] maps LLCP PDUs to procedures/roles used in llcp\_rr\_new()
      - Note - for any given connection, there can only ever be ONE remote procedure in the remote procedure queue
- Miscellaneous minors
  :   - pause/resume concepts - there are two (see spec for details)
      - procedure execution can be paused by the encryption procedure
      - data TX can be paused by PHY, DLE and ENC procedure
      - RX node retention - ensures no waiting for allocation of RX node when needed for notification

### Miscellaneous unit test concepts

- Individual ZTEST unit test for each procedure
  :   - zephyr/tests/bluetooth/controller/ctrl\_<proc>
- Rx node handling is mocked
  :   - Different configs are handled by separate conf files (see ctrl\_conn\_update for example)
      - ZTEST(periph\_rem\_no\_param\_req, test\_conn\_update\_periph\_rem\_accept\_no\_param\_req)
- Emulated versions of rx\_demux/prepare context used in unit tests - testing ONLY procedure PDU flow
  :   - event\_prepare()/event\_done() helpers emulating LLL prepare/done flow
      - lt\_rx()/lt\_tx() ‘lower tester’ emulation of rx/tx
      - ut\_rx\_node() ‘upper tester’ emulation of notification flow handling
      - Bunch of helpers to generate and parse PDUs, as well as miscellaneous mocked ull\_stuff()

## Lower Link Layer

### LLL Execution

![../../_images/ctlr_exec_lll.png](../../_images/ctlr_exec_lll.png)

#### LLL Resume

![../../_images/ctlr_exec_lll_resume_top.png](../../_images/ctlr_exec_lll_resume_top.png)
![../../_images/ctlr_exec_lll_resume_bottom.png](../../_images/ctlr_exec_lll_resume_bottom.png)

## Bare metal utilities

### Memory FIFO and Memory Queue

![../../_images/ctlr_mfifo_memq.png](../../_images/ctlr_mfifo_memq.png)

### Mayfly

![../../_images/ctlr_mayfly.png](../../_images/ctlr_mayfly.png)

- Mayfly are multi-instance scalable ISR execution contexts
- What a Work is to a Thread, Mayfly is to an ISR
- List of functions executing in ISRs
- Execution priorities map to IRQ priorities
- Facilitate cross execution context scheduling
- Race-to-idle execution
- Lock-less, bare metal

## Legacy Controller

![../../_images/ctlr_legacy.png](../../_images/ctlr_legacy.png)

## Bluetooth Low Energy Controller - Vendor Specific Details

### Hardware Requirements

#### Nordic Semiconductor

The Nordic Semiconductor Bluetooth Low Energy Controller implementation
requires the following hardware peripherals.

SoC Peripheral Use

| Resource | nRF Peripheral | # instances | Zephyr Driver Accessible | Description |
| --- | --- | --- | --- | --- |
| Clock | NRF\_CLOCK | 1 | Yes | - A Low Frequency Clock (LFCLOCK) or sleep clock, for low power   consumption between Bluetooth radio events - A High Frequency Clock (HFCLOCK) or active clock, for high precision   packet timing and software based transceiver state switching with   inter-frame space (tIFS) timing inside Bluetooth radio events |
| RTC [[a]](#a) | NRF\_RTC0 | 1 | **No** | - Uses 2 capture/compare registers |
| Timer | NRF\_TIMER0 or NRF\_TIMER4 [[1]](#id25), and NRF\_TIMER1 [[0]](#id24) | 2 or 1 [[1]](#id25) | **No** | - 2 instances, one each for packet timing and tIFS software switching,   respectively - 7 capture/compare registers (3 mandatory, 1 optional for ISR profiling,   4 for single timer tIFS switching) on first instance - 4 capture/compare registers for second instance, if single tIFS timer   is not used. |
| PPI [[b]](#b) | NRF\_PPI | 21 channels (20 [[2]](#id26)), and 2 channel groups [[3]](#id27) | Yes [[4]](#id28) | - Used for radio mode switching to achieve tIFS timings, for PA/LNA   control |
| DPPI [[c]](#c) | NRF\_DPPI | 20 channels, and 2 channel groups [[3]](#id27) | Yes [[4]](#id28) | - Used for radio mode switching to achieve tIFS timings, for PA/LNA   control |
| SWI [[d]](#d) | NRF\_SWI4 and NRF\_SWI5, or NRF\_SWI2 and NRF\_SWI3 [[5]](#id29) | 2 | **No** | - 2 instances, for Lower Link Layer and Upper Link Layer Low priority   execution context |
| Radio | NRF\_RADIO | 1 | **No** | - 2.4 GHz radio transceiver with multiple radio standards such as 1 Mbps,   2 Mbps and Coded PHY S2/S8 Long Range Bluetooth Low Energy technology |
| RNG [[e]](#e) | NRF\_RNG | 1 | Yes |  |
| ECB [[f]](#f) | NRF\_ECB | 1 | **No** |  |
| CBC-CCM [[g]](#g) | NRF\_CCM | 1 | **No** |  |
| AAR [[h]](#h) | NRF\_AAR | 1 | **No** |  |
| GPIO [[i]](#i) | NRF\_GPIO | 2 GPIO pins for PA and LNA, 1 each | Yes | - Additionally, 10 Debug GPIO pins (optional) |
| GPIOTE [[j]](#j) | NRF\_GPIOTE | 1 | Yes | - Used for PA/LNA |
| TEMP [[k]](#k) | NRF\_TEMP | 1 | Yes | - For RC sourced LFCLOCK calibration |
| UART [[l]](#l) | NRF\_UART0 | 1 | Yes | - For HCI interface in Controller only builds |
| IPC [[m]](#m) | NRF\_IPC [[5]](#id29) | 1 | Yes | - For HCI interface in Controller only builds |

[[a](#id1)]

Real Time Counter (RTC)

[[b](#id5)]

Programmable Peripheral Interconnect (PPI)

[[c](#id9)]

Distributed Programmable Peripheral Interconnect (DPPI)

[[d](#id12)]

Software Interrupt (SWI)

[[e](#id14)]

Random Number Generator (RNG)

[[f](#id15)]

AES Electronic Codebook Mode Encryption (ECB)

[[g](#id16)]

Cipher Block Chaining (CBC) - Message Authentication Code with Counter
Mode encryption (CCM)

[[h](#id17)]

Accelerated Address Resolver (AAR)

[[i](#id18)]

General Purpose Input Output (GPIO)

[[j](#id19)]

GPIO tasks and events (GPIOTE)

[[k](#id20)]

Temperature sensor (TEMP)

[[l](#id21)]

Universal Asynchronous Receiver Transmitter (UART)

[[m](#id22)]

Interprocess Communication peripheral (IPC)

[[0](#id3)]

[`CONFIG_BT_CTLR_TIFS_HW`](../../kconfig.md#CONFIG_BT_CTLR_TIFS_HW "CONFIG_BT_CTLR_TIFS_HW") `=n`

[1]
([1](#id2),[2](#id4))

[`CONFIG_BT_CTLR_SW_SWITCH_SINGLE_TIMER`](../../kconfig.md#CONFIG_BT_CTLR_SW_SWITCH_SINGLE_TIMER "CONFIG_BT_CTLR_SW_SWITCH_SINGLE_TIMER") `=y`

[[2](#id6)]

When not using pre-defined PPI channels

[3]
([1](#id7),[2](#id10))

For software-based tIFS switching

[4]
([1](#id8),[2](#id11))

Drivers that use nRFx interfaces

[5]
([1](#id13),[2](#id23))

For nRF53x Series
