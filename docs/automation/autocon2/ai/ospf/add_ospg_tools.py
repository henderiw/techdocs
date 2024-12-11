# Copyright (c) 2024 CodiLime
# All rights reserved

from langchain.tools import tool
from net_tools.common import _base_parallel_executor, _base_method, get_not_implemented_message
from net_tools.frr_tools import PHRASES_TO_CLEAR_LIST
from net_tools.multi_vendor_tools import _base_vendor_dependent_exec
from net_tools.topology_tools import Vendor


def frr_show_ip_ospf_neighbor_detail(device: str) -> str:
    """Returns the output of command 'show ip ospf neighbor detail' on an FRR (Free Range Routing) device.

    Args:
        device (str): shortname of the device or IP address of the device

    Returns (str): string with details of ip ospf neighbors of the device

    """

    # WORKSHOP-PART3 CODE MODIFICATION - START
    # UNCOMMENT THE NEXT LINE
    command = "vtysh -c 'show ip ospf neighbor detail'"
    # WORKSHOP-PART3 CODE MODIFICATION - END

    # _base_method: opens ssh connection, executes command on the device and returns output
    return _base_method(vendor=Vendor.FRR, device=device, command=command,
                        output_phrases_to_clear=PHRASES_TO_CLEAR_LIST)


def vyos_show_ip_ospf_neighbor_detail(device: str) -> str:
    """Returns the output of the command 'show ip ospf neighbor detail' on a VyOS device.

    Args:
        device (str): shortname of the device or IP address of the device

    Returns (str): string with details of ip ospf neighbors of the device

    """

    # WORKSHOP-PART3 CODE MODIFICATION - START
    # UNCOMMENT THE NEXT LINE
    command = "show ip ospf neighbor detail"
    # WORKSHOP-PART3 CODE MODIFICATION - END

    # _base_method: opens ssh connection, executes command on the device and returns output
    return _base_method(vendor=Vendor.VYOS, device=device, command=command,
                        output_phrases_to_clear=[])


def show_ip_ospf_neighbor_detail(device: str) -> str:
    """Returns the output of the command 'show ip ospf neighbor detail' on a network device.
    This is the wrapper executing appropriate script based on device vendor.

    Args:
        device (str): shortname of the device or IP address of the device

    Returns (str): string with details of ip ospf neighbors of the device

    """

    # _base_vendor_dependent_exec: proper selection and execution of script based on device vendor
    return _base_vendor_dependent_exec(device=device,
                                       frr_method=frr_show_ip_ospf_neighbor_detail,
                                       vyos_method=vyos_show_ip_ospf_neighbor_detail,
                                       pc_method=get_not_implemented_message)


@tool
def show_ip_ospf_neighbor_detail_for_many_devices(devices: list[str], empty_str: str) -> str:
    # WORKSHOP-PART3 CODE MODIFICATION - START
    # PROPOSE DESCRIPTION WHAT THE TOOL IS DOING
    # BASED ON THIS LLM WILL SELECT THE TOOL FOR USER QUERY ANSWERING
    # START WITH THE FOLLOWING SENTENCE AND ADD DETAILS WHAT THE COMMAND IS RETURNING

    """Returns the output of the command 'show ip ospf neighbor detail' on many network devices.

    It provides comprehensive information about OSPF (Open Shortest Path First) neighbors on each network device.
    It lists neighboring routers involved in the OSPF process, detailing their IP addresses,
    router IDs, and the interfaces used for the adjacency. Key OSPF metrics, such as
    the neighbor state (e.g., Full, Init) and the neighbor role (e.g., DROther),
    are displayed to help understand the relationship between routers.
    The output also includes priority settings for elections,
    Dead timers (which indicate how long until a neighbor is declared unreachable),
    and BFD (Bidirectional Forwarding Detection) status to track neighbor health.
    Additional information, like OSPF database synchronization lists, area details,
    and interface MTU, ensures the consistency and reliability of routing data.
    For troubleshooting purposes, this command is essential for verifying correct
    OSPF neighbor relationships and resolving adjacency issues.
    If Graceful Restart Helper is enabled, details about non-disruptive OSPF restarts are also included.

    Args:
        devices (list[str]): list of shortnames of the devices
        empty_str (str): should be always '' for langchain compatibility

    Returns (str): Returns details of ip ospf neighbors on specified devices.
    """
    # WORKSHOP-PART3 CODE MODIFICATION - END

    # _base_parallel_executor: parallel execution of scripts for many devices and collection of outputs
    return _base_parallel_executor(devices=devices, method=show_ip_ospf_neighbor_detail)


# section for 'show ip ospf interface'

def frr_show_ip_ospf_interface(device: str) -> str:
    """The output of the command vtysh -c 'show ip ospf interface' on an FRR device provides detailed information
    about the OSPF (Open Shortest Path First) configuration for each network interface on the router.

    Args:
        device (str): shortname of the device or IP address of the device

    Returns (str): string with details of ip ospf interface of the device

    """

    # WORKSHOP-PART3 CODE MODIFICATION - START
    # UNCOMMENT THE NEXT LINE
    command = "vtysh -c 'show ip ospf interface'"
    # WORKSHOP-PART3 CODE MODIFICATION - END

    # _base_method: opens ssh connection, executes command on the device and returns output
    return _base_method(vendor=Vendor.FRR, device=device, command=command,
                        output_phrases_to_clear=PHRASES_TO_CLEAR_LIST)


def vyos_show_ip_ospf_interface(device: str) -> str:
    """The show ip ospf interface command on a VyOS device provides detailed information about the OSPF configuration
    on the device's interfaces.

    Args:
        device (str): shortname of the device or IP address of the device

    Returns (str): string with details of ip ospf interface of the device

    """

    # WORKSHOP-PART3 CODE MODIFICATION - START
    # UNCOMMENT THE NEXT LINE
    command = "show ip ospf interface"
    # WORKSHOP-PART3 CODE MODIFICATION - END

    # _base_method: opens ssh connection, executes command on the device and returns output
    return _base_method(vendor=Vendor.VYOS, device=device, command=command,
                        output_phrases_to_clear=[])


def show_ip_ospf_interface(device: str) -> str:
    """The command show ip ospf interface on a network device provides detailed insights
    into the OSPF (Open Shortest Path First) configuration for each network interface.
    This is the wrapper executing appropriate script based on device vendor.

    Args:
        device (str): shortname of the device or IP address of the device

    Returns (str): string with details of ip ospf interface of the device

    """

    # _base_vendor_dependent_exec: proper selection and execution of script based on device vendor
    return _base_vendor_dependent_exec(device=device,
                                       frr_method=frr_show_ip_ospf_interface,
                                       vyos_method=vyos_show_ip_ospf_interface,
                                       pc_method=get_not_implemented_message)


@tool
def show_ip_ospf_interface_for_many_devices(devices: list[str], empty_str: str) -> str:
    # WORKSHOP-PART3 CODE MODIFICATION - START
    # PROPOSE DESCRIPTION WHAT THE TOOL IS DOING
    # BASED ON THIS LLM WILL SELECT THE TOOL FOR USER QUERY ANSWERING
    # START WITH THE FOLLOWING SENTENCE AND ADD DETAILS WHAT THE COMMAND IS RETURNING

    """Returns the output of the command 'show ip ospf interface' for each network device provided in devices argument.

    The output provides detailed insights into the OSPF (Open Shortest Path First) configuration for each network
    interface. This includes the status of the interface (e.g., whether it's up or down), the interface-specific
    details such as MTU size, bandwidth, and IP address, along with the OSPF area and Router ID associated with
    each interface. Additionally, the command highlights important OSPF parameters like network type, cost,
    Hello and Dead timers, and the current neighbor status, including adjacency details.
    It also provides information about multicast group memberships and protocols like BFD,
    used to monitor the health of OSPF sessions. This information is essential for
    understanding OSPF operation and behavior on network interfaces.

    Args:
        devices (list[str]): list of shortnames of the devices
        empty_str (str): should be always '' for langchain compatibility

    Returns (str): Returns details of ip ospf interface on specified devices.

    """
    # WORKSHOP-PART3 CODE MODIFICATION - END

    # _base_parallel_executor: parallel execution of scripts for many devices and collection of outputs
    return _base_parallel_executor(devices=devices, method=show_ip_ospf_interface)
