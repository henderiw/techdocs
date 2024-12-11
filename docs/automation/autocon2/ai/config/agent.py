# Copyright (c) 2024 CodiLime
# All rights reserved

from langchain.agents import AgentExecutor
from langchain.agents import StructuredChatAgent

from net_agents.custom_prompt import PREFIX, SUFFIX, FORMAT_INSTRUCTIONS, StructuredChatOutputParser
from net_tools import multi_vendor_tools, topology_tools

# WORKSHOP-PART3 CODE MODIFICATION - START
# UNCOMMENT THE NEXT LINE
from net_tools import add_ospf_tools
# WORKSHOP-PART3 CODE MODIFICATION - END

# ADDED IN WORKSHOP-PART4
from net_tools import add_configuration_tool

tool_list = [
    multi_vendor_tools.run_ping_for_many_devices,
    multi_vendor_tools.run_curl_for_many_devices,
    multi_vendor_tools.show_interfaces_details_for_many_devices,
    multi_vendor_tools.show_bgp_summary_for_many_devices,
    multi_vendor_tools.show_bgp_neighbors_for_many_devices,
    multi_vendor_tools.show_bfd_sessions_for_many_devices,
    multi_vendor_tools.show_ip_route_for_many_devices,
    multi_vendor_tools.show_version_for_many_devices,
    topology_tools.topology_get_info_network_topology,
    topology_tools.topology_get_info_on_links,
    topology_tools.topology_get_links_between_devices,
    topology_tools.topology_get_vendor_of_devices,
    topology_tools.topology_get_list_of_shortnames_of_network_devices,
    topology_tools.topology_get_list_shortnames_of_endpoints
]

# WORKSHOP-PART3 CODE MODIFICATION - START
# UNCOMMENT THE NEXT 2 LINES
tool_list.append(add_ospf_tools.show_ip_ospf_neighbor_detail_for_many_devices)
tool_list.append(add_ospf_tools.show_ip_ospf_interface_for_many_devices)
# WORKSHOP-PART3 CODE MODIFICATION - END

# ADDED IN WORKSHOP-PART4
tool_list.append(add_configuration_tool.show_configuration_for_many_devices)


def init_agent(tools, llm):
    agent = StructuredChatAgent.from_llm_and_tools(llm, tools, prefix=PREFIX, suffix=SUFFIX,
                                                   format_instructions=FORMAT_INSTRUCTIONS, output_parser=StructuredChatOutputParser())
    agent = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, handle_parsing_errors=True,
                                               verbose=True, max_iterations=10,)
    return agent


agent_tools_dict = {
    "Multi-Vendor agent": tool_list,
}