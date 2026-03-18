---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/busy__sim_8h.html
original_path: doxygen/html/busy__sim_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

busy\_sim.h File Reference

[Go to the source code of this file.](busy__sim_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [busy\_sim\_cb\_t](#a6b09e8372800e740a653f45f10a3501f)) (void) |

| Functions | |
| --- | --- |
| void | [busy\_sim\_start](#a2bb7c55b7e21ee9e5f927fcecd758705) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_avg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_delta, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idle\_avg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idle\_delta, [busy\_sim\_cb\_t](#a6b09e8372800e740a653f45f10a3501f) cb) |
|  | Start busy simulator. |
| void | [busy\_sim\_stop](#ae7f199942b18363936dcb11fca8d0c96) (void) |
|  | Stop busy simulator. |

## Typedef Documentation

## [◆ ](#a6b09e8372800e740a653f45f10a3501f)busy\_sim\_cb\_t

| typedef void(\* busy\_sim\_cb\_t) (void) |
| --- |

## Function Documentation

## [◆ ](#a2bb7c55b7e21ee9e5f927fcecd758705)busy\_sim\_start()

| void busy\_sim\_start | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *active\_avg*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *active\_delta*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *idle\_avg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *idle\_delta*, |
|  |  | [busy\_sim\_cb\_t](#a6b09e8372800e740a653f45f10a3501f) | *cb* ) |

Start busy simulator.

When started, it is using counter device to generate interrupts at random intervals and busy loop for random period of time in that interrupt. Interrupt source and priority is configured in the devicetree. Default entropy source is used for getting random numbers. System work queue is used to get random values and keep them in a ring buffer.

Parameters
:   | active\_avg | Average time of busy looping in the counter callback (in microseconds). |
    | --- | --- |
    | active\_delta | Specifies deviation from average time of busy looping (in microseconds). |
    | idle\_avg | Average time of counter alarm timeout (in microseconds). |
    | idle\_delta | Specifies deviation from average time of counter alarm (in microseconds). |
    | cb | Callback called from the context of the busy simulator timeout. If ZLI interrupt is used for busy simulator counter then kernel API cannot be used from that callback. Callback is called before busy waiting. |

## [◆ ](#ae7f199942b18363936dcb11fca8d0c96)busy\_sim\_stop()

| void busy\_sim\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Stop busy simulator.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [busy\_sim.h](busy__sim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
