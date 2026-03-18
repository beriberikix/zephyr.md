---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/npm1100_ek/doc/index.html
original_path: boards/shields/npm1100_ek/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nPM1100 EK

## Overview

The nPM1100 EK lets you test different functions and features of the nPM1100
Power Management Integrated Circuit (PMIC).

![nPM1100 EK](../../../../_images/npm1100_ek.jpg)

nPM1100 EK

## Requirements

The nPM1100 EK board is not designed to fit straight into an Arduino connector.
However, the Zephyr shield is designed expecting it to be connected to the
Arduino shield pins. This allows to use the shield with any host board that
supports the Arduino connector. The connections are:

| PMIC Pin | Arduino Pin |
| --- | --- |
| ISET MODE | D2 D3 |

## Usage

The shield can be used in any application by setting `SHIELD` to
`npm1100_ek`.

## References

- [nPM1100 EK Manual](https://infocenter.nordicsemi.com/topic/ug_npm1100_ek/UG/nPM1100_EK/intro.html)
