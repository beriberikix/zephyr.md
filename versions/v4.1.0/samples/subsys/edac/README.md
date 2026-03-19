---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/subsys/edac/README.html
original_path: samples/subsys/edac/README.html
---

# EDAC shell

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/edac/README.rst/..)

## Overview

This sample demonstrates the [EDAC driver API](../../../hardware/peripherals/edac/index.md#edac-api) in a simple EDAC shell sample.

## Building and Running

This sample can be found under [samples/subsys/edac](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/edac) in the
Zephyr tree.
The sample can be built as follows for the [Elkhart Lake CRB](../../../boards/intel/ehl/doc/index.md#intel-ehl-crb) board:

```shell
west build -b intel_ehl_crb samples/subsys/edac
```

The Zephyr image that’s created can be run on the [Elkhart Lake CRB](../../../boards/intel/ehl/doc/index.md#intel-ehl-crb) board
as per the instructions in the board documentation. Check out the
[Elkhart Lake CRB](../../../boards/intel/ehl/doc/index.md#intel-ehl-crb) for details.

## Sample output

### Getting help

After the application has started help can be read with the following
command:

```shell
uart:~$ edac -h
edac - EDAC information
Subcommands:
  info    :Show EDAC information
           edac info <subcommands>
  inject  :Inject ECC error commands
           edac inject <subcommands>
```

Help for subcommand info can be read with:

```shell
uart:~$ edac info -h
info - Show EDAC information
       edac info <subcommands>
Subcommands:
  ecc_error     :ECC Error Show / Clear commands
  parity_error  :Parity Error Show / Clear commands
```

Injection help can be received with:

```shell
uart:~$ edac inject -h
inject - Inject ECC error commands
         edac inject <subcommands>
Subcommands:
  addr          :Get / Set physical address
  mask          :Get / Set address mask
  trigger       :Trigger injection
  error_type    :Get / Set injection error type
  disable_nmi   :Disable NMI
  enable_nmi    :Enable NMI
  test_default  :Test default injection parameters
```

### Testing Error Injection

Set Error Injection parameters with:

```shell
uart:~$ edac inject addr 0x1000
Set injection address base to: 0x1000

uart:~$ edac inject mask 0x7fffffffc0
Set injection address mask to 7fffffffc0

uart:~$ edac inject error_type correctable
Set injection error type: correctable
```

Trigger injection with:

```shell
uart:~$ edac inject trigger
Triggering injection
```

Now Read / Write to the injection address to trigger Error Injection with
following devmem commands:

```shell
uart:~$ devmem 0x1000 32 0xabcd
Mapped 0x1000 to 0x2ffcf000

Using data width 32
Writing value 0xabcd

uart:~$ devmem 0x1000
Mapped 0x1000 to 0x2ffce000

Using data width 32
Read value 0xabcd
```

We should get the following message on screen indicating an IBECC event:

```text
Got notification about IBECC event
```

## See also

[EDAC API](../../../doxygen/html/group__edac.md)
