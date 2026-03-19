---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/smf/hsm_psicc2/README.html
original_path: samples/subsys/smf/hsm_psicc2/README.html
---

# Hierarchical State Machine Demo based on example from PSiCC2

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/smf/hsm_psicc2/README.rst/..)

## Overview

This sample demonstrates the [State Machine Framework](../../../../services/smf/index.md#smf) subsystem.

## Building and Running

It should be possible to build and run this sample on almost any board or emulator.

### Building and Running for ST Disco L475 IOT01 (B-L475E-IOT01A)

The sample can be built and executed for the [Disco L475 IOT01 (B-L475E-IOT01A)](../../../../boards/st/disco_l475_iot1/doc/index.md#disco_l475_iot1) as follows:

```shell
west build -b disco_l475_iot1 samples/subsys/smf/hsm_psicc2
west flash
```

For other boards just replace the board name.

### Instructions for Use

This application implements the statechart shown in Figure 2.11 of
Practical UML Statecharts in C/C++, 2nd Edition, by Miro Samek (PSiCC2). Ebook available from
[https://www.state-machine.com/psicc2](https://www.state-machine.com/psicc2) This demo was chosen as it contains all possible transition
topologies up to four levels of state nesting and is used with permission of the author.

For each state, the entry, run, and exit actions are logged to the console, as well as logging
when a state handles an event, or explicitly ignores it and passes it up to the parent state.

There are two shell commands defined for controlling the operation.

- `psicc2 event <event>` sends the event (from A to I) to the state machine. These correspond to
  events A through I in PSiCC2 Figure 2.11
- `psicc2 terminate` sends the `EVENT_TERMINATE` event to terminate the state machine. There
  is no way to restart the state machine once terminated, and future events are ignored.

### Comparison to PSiCC2 Output

Not all transitions modelled in UML may be supported by the [State Machine Framework](../../../../services/smf/index.md#smf).
Unsupported transitions may lead to results different to the example run of the application in
PSiCC2 Section 2.3.15. The differences will not be listed here as it is hoped [SMF](../../../../services/smf/index.md#smf)
will support these transitions in the future and the list would become outdated.

## See also

[State Machine Framework API](../../../../doxygen/html/group__smf.md)
