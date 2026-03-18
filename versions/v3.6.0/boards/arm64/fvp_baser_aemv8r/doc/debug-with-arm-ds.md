---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm64/fvp_baser_aemv8r/doc/debug-with-arm-ds.html
original_path: boards/arm64/fvp_baser_aemv8r/doc/debug-with-arm-ds.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Debug with Arm DS

## Install Arm DS

Please refer to the official Arm Development Studio Page [[1]](#id4) for details. Here
`Version: 2020.b Build: 2020110909` is used in the following example.

![Arm DS Version](../../../../_images/version-info.jpg)

## Download Arm FVP BaseR AEMv8-R

Please refer to official FVP page [[2]](#id5) for download instructions. Here `$FVP_D`
is used to indicate which directory is FVP located.

## Use DS perspective

From menu choose `Window -> Perspective -> Open Perspective -> Other...`:

![Arm DS Perspective choose Other...](../../../../_images/perspective-choose-other.jpg)

In the opened window, choose `Development Studio (default)`:

![Arm DS Perspective choose DS](../../../../_images/perspective-choose-ds.jpg)

## Create a new configuration database

Create a new configuration database by selecting `File -> New -> Other... -> Configuration Database`:

![Arm DS create new configuration database](../../../../_images/create-new-configuration-database.jpg)

Choose a name for the database. Here `Zephyr` is used:

![Arm DS create new configuration database: choose database name](../../../../_images/create-new-configuration-database_database-name.jpg)

Click `Finish` and the new configuration database can be seen in `Project Explorer`:

![Arm DS create new configuration database: shown in project explorer](../../../../_images/create-new-configuration-database_shown-in-project-explorer.jpg)

## Create a new model configuration

Right click `Zephyr` in `Project Explorer`, choose `New -> Model Configuration`:

![Arm DS create new model configuration](../../../../_images/create-new-model-configuration.jpg)

In the opened window:

1. Choose `Iris` for `Model Interface`, then `Next >`.
2. Choose `Launch and connect to specific model`, then `Next >`.
3. Set `Model Path` to `$FVP_D/FVP_BaseR_AEMv8R`, then `Finish`.

![Arm DS create new model configuration: set model path](../../../../_images/create-new-model-configuration_model-path.jpg)

Then in `FVP_BaseR_AEMv8R` tab, change `ARMAEMv8-R_` to `V8R64-Generic`,
click `Save` and then click `Import`:

![Arm DS create new model configuration: import](../../../../_images/create-new-model-configuration_model-use-V8R64-Generic.jpg)

## Create a new launch configuration

From `Project Explorer`, right click `FVP_BaseR_AEMv8R` and select `Debug as -> Debug configurations...`:

![Arm DS create new launch configuration: context menu](../../../../_images/create-new-launch-configuration_context-menu.jpg)

Select `Generic Arm C/C++ Application` and click `New launch configuration` button.
A new configuration named `New_configuration` will be created.

1. In `Connection` tab:

   - In `Select target` box, select `Imported -> FVP_BaseR_AEMv8R -> Bare Metal Debug -> ARMAEMv8-R_MP_0`
   - In `Connections` box, set `Model parameters` to:

     ```text
     -C bp.dram.enable_atomic_ops=1 -C bp.sram.enable_atomic_ops=1 -C bp.refcounter.non_arch_start_at_default=1 -C gic_distributor.GICD_CTLR-DS-1-means-secure-only=1 -C gic_distributor.has-two-security-states=0 -C bp.vis.disable_visualisation=1 -C cluster0.has_aarch64=1 -a /home/fengqi/zephyrproject/build/zephyr/zephyr.elf
     ```

     These parameters are passed to `FVP_BaseR_AEMv8R` when launches. Run `FVP_BaseR_AEMv8R --help`
     to see all command line options. Run `FVP_BaseR_AEMv8R --list-params` to see all supported parameters.
     The file `zephyr.elf` specified by `-a` is the binary built from Zephyr.

![Arm DS create new launch configuration: connection](../../../../_images/create-new-launch-configuration_connection.jpg)

2. In `Files` tab:

   In `Files` box, set `Load symbols from file` to full path of `zephyr.elf` that you built.

![Arm DS create new launch configuration: files](../../../../_images/create-new-launch-configuration_files.jpg)

3. In `Debugger` tab:

   - In `Run control` box, check `Execute debugger commands` and insert:

     ```text
     add-symbol-file "/home/fengqi/zephyrproject/build/zephyr/zephyr.elf" EL1S:0
     ```

     Replace `/home/fengqi/zephyrproject/build/zephyr/zephyr.elf` with your local path.
   - In `Paths` box, set `Source search directory` to the path to Zephyr source code.

![Arm DS create new launch configuration: debugger](../../../../_images/create-new-launch-configuration_debugger.jpg)

After all these changes are made, click `Apply`, then click `Debug`. DS will
launch `FVP_BaseR_AEMv8R` and connect to it. You can see a new session is
connected in `Debug Control` window.

![Arm DS working](../../../../_images/DS-debug-working.jpg)

## References

[[1](#id2)]

[https://developer.arm.com/tools-and-software/embedded/arm-development-studio](https://developer.arm.com/tools-and-software/embedded/arm-development-studio)

[[2](#id3)]

[https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms/arm-ecosystem-models](https://developer.arm.com/tools-and-software/simulation-models/fixed-virtual-platforms/arm-ecosystem-models)
