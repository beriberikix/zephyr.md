---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/peci/README.html
original_path: samples/drivers/peci/README.html
---

# PECI interface

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/peci/README.rst/..)

## Overview

This sample demonstrates how to use the [PECI API](../../../hardware/peripherals/peci.md#peci-api).
Callbacks are registered that will write to the console indicating PECI events.
These events indicate PECI host interaction.

## Building and Running

The sample can be built and executed on boards supporting PECI.
Please connect ensure the microcontroller used is connected to a PECI Host
in order to execute.

### Sample output

```shell
PECI test
Note: You are expected to see several interactions including ID and
temperature retrieval.
```

## See also

[PECI Interface](../../../doxygen/html/group__peci__interface.md)
