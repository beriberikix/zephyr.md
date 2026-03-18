---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/stm32/ccm/README.html
original_path: samples/boards/stm32/ccm/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# STM32 CCM example

## Overview

Show usage of the Core Coupled Memory (CCM) that is available
on several STM32 devices. The very important difference with
normal RAM is that CCM can not be used for DMA.

By prefixing a variable with \_\_ccm\_data\_section, \_\_ccm\_bss\_section,
or \_\_ccm\_noinit\_section those variables are placed in the CCM.

The \_\_ccm\_data\_section prefix should be used for variables that
are initialized. Like the normal data section the initial
values take up space in the FLASH image.

The \_\_ccm\_bss\_section prefix should be used for variables that
should be initialized to 0. Like the normal bss section they
do not take up FLASH space.

The \_\_ccm\_noinit\_section prefix should be used for variables
that don’t need to have a defined initial value (for example
buffers that will receive data). Compared to bss or data the
kernel does not need to initialize the noinit section making
the startup slightly faster.

To add CCM support to a board, add the following line to the
board’s DTS file `chosen` section:

```shell
zephyr,ccm = &ccm0;
```

For example the olimex STM32 E407 DTS file looks like this:

```text
  1/*
  2 * Copyright (c) 2017, Erwin Rol <erwin@erwinrol.com>
  3 *
  4 * SPDX-License-Identifier: Apache-2.0
  5 */
  6
  7/dts-v1/;
  8#include <st/f4/stm32f407Xg.dtsi>
  9#include <st/f4/stm32f407z(e-g)tx-pinctrl.dtsi>
 10#include <zephyr/dt-bindings/input/input-event-codes.h>
 11
 12/ {
 13	model = "Olimex STM32-E407 board";
 14	compatible = "olimex,stm32-e407";
 15
 16	chosen {
 17		zephyr,console = &usart1;
 18		zephyr,shell-uart = &usart1;
 19		zephyr,sram = &sram0;
 20		zephyr,flash = &flash0;
 21		zephyr,ccm = &ccm0;
 22	};
 23
 24	leds {
 25		compatible = "gpio-leds";
 26		green_led_1: led_1 {
 27			gpios = <&gpioc 13 GPIO_ACTIVE_HIGH>;
 28			label = "LED1";
 29		};
 30	};
 31
 32	gpio_keys {
 33		compatible = "gpio-keys";
 34		user_button: button {
 35			label = "Key";
 36			gpios = <&gpioa 0 GPIO_ACTIVE_LOW>;
 37			zephyr,code = <INPUT_KEY_0>;
 38		};
 39	};
 40
 41	aliases {
 42		led0 = &green_led_1;
 43		sw0 = &user_button;
 44	};
 45};
 46
 47&clk_lsi {
 48	status = "okay";
 49};
 50
 51&clk_hse {
 52	clock-frequency = <DT_FREQ_M(12)>;
 53	status = "okay";
 54};
 55
 56&pll {
 57	div-m = <12>;
 58	mul-n = <336>;
 59	div-p = <2>;
 60	div-q = <7>;
 61	clocks = <&clk_hse>;
 62	status = "okay";
 63};
 64
 65&rcc {
 66	clocks = <&pll>;
 67	clock-frequency = <DT_FREQ_M(168)>;
 68	ahb-prescaler = <1>;
 69	apb1-prescaler = <4>;
 70	apb2-prescaler = <2>;
 71};
 72
 73&usart1 {
 74	pinctrl-0 = <&usart1_tx_pb6 &usart1_rx_pb7>;
 75	pinctrl-names = "default";
 76	current-speed = <115200>;
 77	status = "okay";
 78};
 79
 80&usart3 {
 81	pinctrl-0 = <&usart3_tx_pb10 &usart3_rx_pb11>;
 82	pinctrl-names = "default";
 83	current-speed = <115200>;
 84	status = "okay";
 85};
 86
 87&usart6 {
 88	pinctrl-0 = <&usart6_tx_pc6 &usart6_rx_pc7>;
 89	pinctrl-names = "default";
 90	current-speed = <115200>;
 91	status = "okay";
 92};
 93
 94&rtc {
 95	clocks = <&rcc STM32_CLOCK_BUS_APB1 0x10000000>,
 96		 <&rcc STM32_SRC_LSI RTC_SEL(2)>;
 97	status = "okay";
 98};
 99
100&rng {
101	status = "okay";
102};
103
104/* Only one interface should be enabled at a time: usbotg_fs or usbotg_hs */
105usb_otg1: &usbotg_fs {
106	pinctrl-0 = <&usb_otg_fs_dm_pa11 &usb_otg_fs_dp_pa12>;
107	pinctrl-names = "default";
108	status = "disabled";
109};
110
111zephyr_udc0: &usbotg_hs {
112	pinctrl-0 = <&usb_otg_hs_dm_pb14 &usb_otg_hs_dp_pb15>;
113	pinctrl-names = "default";
114	status = "okay";
115};
116
117&mac {
118	status = "okay";
119	pinctrl-0 = <&eth_mdc_pc1
120		     &eth_rxd0_pc4
121		     &eth_rxd1_pc5
122		     &eth_ref_clk_pa1
123		     &eth_mdio_pa2
124		     &eth_col_pa3
125		     &eth_crs_dv_pa7
126		     &eth_tx_en_pg11
127		     &eth_txd0_pg13
128		     &eth_txd1_pg14>;
129	pinctrl-names = "default";
130};
```

## Building and Running

```shell
west build -b None samples/boards/stm32/ccm
west flash
```

The first time the example is run after power on, the output will
look like this:

```shell
***** BOOTING ZEPHYR OS v1.10.99 - BUILD: Jan 14 2018 09:32:46 *****

CCM (Core Coupled Memory) usage example

The total used CCM area   : [0x10000000, 0x10000021)
Zero initialized BSS area : [0x10000000, 0x10000007)
Uninitialized NOINIT area : [0x10000008, 0x10000013)
Initialised DATA area     : [0x10000014, 0x10000021)
Start of DATA in FLASH    : 0x08003940

Checking initial variable values: ... PASSED

Initial variable values:
ccm_data_var_8  addr: 0x10000014 value: 0x12
ccm_data_var_16 addr: 0x10000016 value: 0x3456
ccm_data_var_32 addr: 0x10000018 value: 0x789abcde
ccm_data_array  addr: 0x1000001c size: 5 value:
        0x11 0x22 0x33 0x44 0x55
ccm_bss_array addr: 0x10000000 size: 7 value:
        0x00 0x00 0x00 0x00 0x00 0x00 0x00
ccm_noinit_array addr: 0x10000008 size: 11 value:
        0xa9 0x99 0xba 0x90 0xe1 0x2a 0xba 0x93 0x4c 0xfe 0x4b

Variable values after writing:
ccm_data_var_8  addr: 0x10000014 value: 0xed
ccm_data_var_16 addr: 0x10000016 value: 0xcba9
ccm_data_var_32 addr: 0x10000018 value: 0x87654321
ccm_data_array  addr: 0x1000001c size: 5 value:
        0xaa 0xaa 0xaa 0xaa 0xaa
ccm_bss_array addr: 0x10000000 size: 7 value:
        0xbb 0xbb 0xbb 0xbb 0xbb 0xbb 0xbb
ccm_noinit_array addr: 0x10000008 size: 11 value:
        0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc

Example end
```

First, each CCM section is listed with its address and size. Next, some usage
examples are shown. Note that the `noinit` section holds variables with
uninitialized data. After writing to the variables, they all should hold the
values shown above.

When the board is reset (without power-cycling), the output looks like this:

```shell
***** BOOTING ZEPHYR OS v1.10.99 - BUILD: Jan 14 2018 09:32:46 *****

CCM (Core Coupled Memory) usage example

The total used CCM area   : [0x10000000, 0x10000021)
Zero initialized BSS area : [0x10000000, 0x10000007)
Uninitialized NOINIT area : [0x10000008, 0x10000013)
Initialised DATA area     : [0x10000014, 0x10000021)
Start of DATA in FLASH    : 0x08003940

Checking initial variable values: ... PASSED

Initial variable values:
ccm_data_var_8  addr: 0x10000014 value: 0x12
ccm_data_var_16 addr: 0x10000016 value: 0x3456
ccm_data_var_32 addr: 0x10000018 value: 0x789abcde
ccm_data_array  addr: 0x1000001c size: 5 value:
        0x11 0x22 0x33 0x44 0x55
ccm_bss_array addr: 0x10000000 size: 7 value:
        0x00 0x00 0x00 0x00 0x00 0x00 0x00
ccm_noinit_array addr: 0x10000008 size: 11 value:
        0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc

Variable values after writing:
ccm_data_var_8  addr: 0x10000014 value: 0xed
ccm_data_var_16 addr: 0x10000016 value: 0xcba9
ccm_data_var_32 addr: 0x10000018 value: 0x87654321
ccm_data_array  addr: 0x1000001c size: 5 value:
        0xaa 0xaa 0xaa 0xaa 0xaa
ccm_bss_array addr: 0x10000000 size: 7 value:
        0xbb 0xbb 0xbb 0xbb 0xbb 0xbb 0xbb
ccm_noinit_array addr: 0x10000008 size: 11 value:
        0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc 0xcc

Example end
```

The difference with the first run is that the ccm\_noinit section still has the
values from the last write. It is important to notice that this is not guaranteed,
it still should be considered uninitialized leftover data.
