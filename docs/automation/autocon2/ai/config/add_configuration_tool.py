# Copyright (c) 2024 CodiLime
# All rights reserved

from net_tools.common import _base_method, get_not_implemented_message, _base_parallel_executor
from net_tools.frr_tools import PHRASES_TO_CLEAR_LIST
from net_tools.multi_vendor_tools import _base_vendor_dependent_exec
from net_tools.topology_tools import Vendor
from langchain.tools import tool

# THIS MODULE IS ADDED IN WORKSHOP-PART4


def frr_show_running_config(device: str) -> str:
    """The 'show running-config' command on an FRR (Free Range Routing) device displays the current active
    configuration of the routing protocols and settings. It provides detailed information about the router’s setup,
    including the version of the FRR software and global defaults. The output includes various routing protocol
    configurations like BGP and OSPF, showing details such as peer groups, neighbors, router IDs,
    and route redistribution rules. For interfaces, the command lists IP addresses, OSPF configurations,
    and other protocol-specific settings. Prefix-lists and route-maps are also included, defining rules for
    permitting or denying specific network prefixes and routing policies. Overall, this command provides a full
    snapshot of the device’s active configuration, reflecting all operational settings currently in effect.

    Args:
        device (str): host shortname or IP address of the device

    Returns (str): Formatted string with running configuration on the FRR device

    """
    return _base_method(vendor=Vendor.FRR, device=device, command="vtysh -c 'show running-config no-header'",
                        output_phrases_to_clear=PHRASES_TO_CLEAR_LIST)


def vyos_show_configuration(device: str) -> str:
    """
    The show configuration command on a VyOS device displays the current active configuration in a hierarchical format,
    providing a detailed view of how the system is configured. The output is structured into different configuration
    blocks, where each block represents a section such as interfaces, protocols, service, and system settings.
    Within each section, further details are provided in a nested manner, showing specific configurations such as
    interface addresses, routing protocols, or services. Each element, like an interface or routing protocol,
    can have associated parameters, such as MTU, BGP neighbors, or NTP servers. This hierarchical output allows
    for easy reading and understanding of how different components are related and configured within the system.
    The show configuration command is especially useful for administrators to check the running configuration,
    ensuring everything is set up as intended. It provides a high-level view of all active configurations and
    is critical for troubleshooting and configuration audits.

    Args:
        device (str): host shortname or IP address of the device

    Returns (str): Formatted string in the form of json with information of device's configuration

    """
    return _base_method(vendor=Vendor.VYOS, device=device, command="show configuration",
                        output_phrases_to_clear=[])


def show_configuration(device: str) -> str:
    """Commands that display device configuration offer insights into how a network device
    is currently set up and managed. The 'show running-config' command provides
    an overview of the active configuration, including details about routing protocols
    such as BGP or OSPF, interface configurations, IP addresses, and global settings.
    This command is essential for reviewing the current operational state of a device,
    ensuring that all settings reflect the intended configuration. On the other hand,
    the 'show configuration commands' command outputs the active configuration as a series
    of CLI commands, presenting it in a way that can be easily exported or reapplied.
    It provides administrators with a clear, structured format, showing how each
    configuration setting was applied. This command is particularly useful for
    replicating or auditing configurations across multiple devices or environments.
    Together, these commands enable network administrators to audit, troubleshoot,
    and replicate configurations efficiently.

    Args:
        device (str): shortname of the network device or IP address of the device

    Returns (str): Returns detailed information of current configuration of the device.
    """
    return _base_vendor_dependent_exec(device=device,
                                       frr_method=frr_show_running_config,
                                       vyos_method=vyos_show_configuration,
                                       pc_method=get_not_implemented_message)


@tool
def show_configuration_for_many_devices(devices: list[str], empty_str: str) -> str:
    """Returns device configuration of devices identified by their shortnames. It offers insights into how network
    devices are currently set up and managed.
    The tool offers detailed insight into the current routing protocols, interface settings, global system
    parameters, and any specific configurations in place. The output typically includes routing details such as
    OSPF, BGP peers, route redistribution, and specific parameters like MTU or IP addressing. For routing policies
    and access controls, these commands show prefix-lists, route-maps, and service configurations.
    It is useful for network administrators to understand the device's operational state and assist in
    troubleshooting and audits. It enables administrators to quickly verify settings and ensure consistency. They
    help in diagnosing network issues by showing all relevant active configurations at a glance.
    Additionally, they facilitate audits by providing an accurate snapshot of how the device is currently set up,
    which is critical for compliance and troubleshooting.

    Args:
        devices (list[str]): list of shortnames of the devices
        empty_str (str): should be always '' for langchain compatibility

    Returns (str): Returns detailed information of current configuration of specified devices.

    """
    return _base_parallel_executor(devices=devices, method=show_configuration)
