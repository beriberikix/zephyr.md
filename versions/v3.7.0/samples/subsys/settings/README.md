---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/settings/README.html
original_path: samples/subsys/settings/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Settings API

## Overview

This is a simple application demonstrating use of the settings runtime
configuration module. In this application some configuration values are loaded
from persistent storage and exported to persistent storage using different
settings method. The example shows how to implement module handlers, how to
register them.

## Requirements

- A board with settings support, for instance: nrf52840dk/nrf52840
- Or qemu\_x86 target

## Building and Running

This sample can be found under [samples/subsys/settings](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/settings) in
the Zephyr tree.

The sample can be build for several platforms, the following commands build the
application for the qemu\_x86.

```shell
west build -b qemu_x86 samples/subsys/settings
west build -t run
```

After running the image to the board the output on the console shows the
settings manipulation messages.

### Sample Output

```shell
***** Booting Zephyr OS build v2.1.0-rc1-123-g41091eb1d5e0 *****

*** Settings usage example ***

settings subsys initialization: OK.
subtree <alpha> handler registered: OK
subtree <alpha/beta> has static handler

##############
# iteration 0
##############

=================================================
basic load and save using registered handlers

load all key-value pairs using registered handlers
loading all settings under <beta> handler is done
loading all settings under <alpha> handler is done

save <alpha/beta/voltage> key directly: OK.

load <alpha/beta> key-value pairs using registered handlers
<alpha/beta/voltage> = -3025
loading all settings under <beta> handler is done

save all key-value pairs using registered handlers
export keys under <beta> handler
export keys under <alpha> handler

load all key-value pairs using registered handlers
export keys under <beta> handler
export keys under <alpha> handler

=================================================
loading subtree to destination provided by the caller

direct load: <alpha/length/2>
direct load: <alpha/length/1>
direct load: <alpha/length>
  direct.length = 100
  direct.length_1 = 41
  direct.length_2 = 59

=================================================
Delete a key-value pair

immediate load: OK.
  <alpha/length> value exist in the storage
delete <alpha/length>: OK.
  Can't to load the <alpha/length> value as expected

=================================================
Service a key-value pair without dedicated handlers

<gamma> = 0 (default)
save <gamma> key directly: OK.
...
```
