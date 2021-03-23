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
"orange",
"altera_common_sv_packages",
"altera_xcvr_native_a10_191",
"altera_pcie_a10_hip_191",
"altera_xcvr_fpll_a10_191",
"altera_xcvr_atx_pll_a10_191",
"pcie_top",
"pcie_dma_altpcie_devkit_0",
"altpcie_devkit_191",
"pcie_dma_altpcie_devkit_0",
"pcie_dma_clk_0",
"altera_common_sv_packages",
"altera_conduit_bfm_191",
"pcie_dma_inst_dk_board_bfm_ip",
"altera_common_sv_packages",
"altera_avalon_reset_source_191",
"pcie_dma_inst_reconfig_xcvr_reset_bfm_ip",
"altera_common_sv_packages",
"altera_avalon_clock_source_191",
"pcie_dma_inst_reconfig_xcvr_clk_bfm_ip",
"altera_pcie_a10_tbed_191",
"DUT_pcie_tb_ip",
]

def vsim(lib_name:list):
    for item in lib_name:
        print("-L {}".format(item),end=" ")

vsim(b)