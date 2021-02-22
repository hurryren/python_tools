def ensure_lib(lib_name:list):
    for item in lib_name:
        print("ensure_lib               ./libraries/{}/".format(item))
        print("vmap     {}               ./libraries/{}/".format(item,item))

a = [
"pcie_ed_tb",
"altera_pcie_a10_tbed_191",
"DUT_pcie_tb_ip",
"altera_common_sv_packages",
"altera_conduit_bfm_191",
"pcie_ed_inst_board_pins_bfm_ip",]


ensure_lib(a)