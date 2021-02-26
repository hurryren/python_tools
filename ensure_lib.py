def ensure_lib(lib_name:list):
    for item in lib_name:
        print("ensure_lib               ./libraries/{}/".format(item))
        print("vmap     {}               ./libraries/{}/".format(item,item))
b = [
"work",
"work_lib",
"altera_ver",
"lpm_ver",
"sgate_ver",
"altera_mf_ver",
"altera_lnsim_ver",
"twentynm_ver",
"twentynm_hssi_ver",
"twentynm_hip_ver",
"altera",
"lpm",
"sgate",
"altera_mf",
"altera_lnsim",
"twentynm",
"twentynm_hssi",
"twentynm_hip",
"pcie_ed_tb",
"altera_pcie_a10_tbed_191",
"DUT_pcie_tb_ip",
"altera_common_sv_packages",
"altera_conduit_bfm_191",
"pcie_ed_inst_board_pins_bfm_ip",
"altera_merlin_master_translator_191",
"altera_merlin_slave_translator_191",
"altera_merlin_master_agent_191",
"altera_merlin_slave_agent_191",
"altera_avalon_sc_fifo_1930",
"altera_merlin_router_1920",
"altera_avalon_st_pipeline_stage_1920",
"altera_merlin_burst_adapter_1920",
"altera_merlin_demultiplexer_1920",
"altera_merlin_multiplexer_1920",
"altera_mm_interconnect_1920",
"altera_irq_mapper_1920",
"altera_reset_controller_1920",
"pcie_ed",
"ast2avmm_bridge_256_191",
"pcie_ed_APPS",
"altpcie_devkit_191",
"pcie_ed_DK",
"altera_common_sv_packages",
"altera_xcvr_native_a10_191",
"altera_pcie_a10_hip_191",
"altera_xcvr_fpll_a10_191",
"altera_xcvr_atx_pll_a10_191",
"pcie_ed_DUT",
"altera_avalon_onchip_memory2_1920",
"pcie_ed_MEM",
]

def vsim(lib_name:list):
    for item in lib_name:
        print("-L {}".format(item),end=" ")


vsim(b)