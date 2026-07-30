import re

# 貼上你最初始的那串包含 State ID 的原始碼
text = """
            ccw_taiwan_0_visible = {
                NOT = {
                    OR = {
                        524 = { is_controlled_by = CHI }
                        1148 = { is_controlled_by = CHI }
                        1149 = { is_controlled_by = CHI }
                        1150 = { is_controlled_by = CHI }
                        648 = { is_controlled_by = CHI }
                    }
                }
            }
            
            ccw_anhui_0_visible = {
                NOT = {
                    OR = {
                        1223 = { is_controlled_by = CHI }
                        606 = { is_controlled_by = CHI }
                        1221 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_beijing_s_0_visible = {
                NOT = {
                    608 = { is_controlled_by = CHI }
                }
            }

            ccw_beijing_0_visible = {
                NOT = {
                    608 = { is_controlled_by = CHI }
                }
            }

            ccw_jiangsu_0_visible = {
                NOT = {
                    OR = {
                        598 = { is_controlled_by = CHI }
                        1228 = { is_controlled_by = CHI }
                        1429 = { is_controlled_by = CHI }
                        613 = { is_controlled_by = CHI }
                        1222 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_shandong_0_visible = {
                NOT = {
                    OR = {
                        1426 = { is_controlled_by = CHI }
                        1231 = { is_controlled_by = CHI }
                        597 = { is_controlled_by = CHI }
                        1230 = { is_controlled_by = CHI }
                        1427 = { is_controlled_by = CHI }
                        1229 = { is_controlled_by = CHI }
                        1393 = { is_controlled_by = CHI }
                        1420 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_hebei_0_visible = {
                NOT = {
                    OR = {
                        609 = { is_controlled_by = CHI }
                        610 = { is_controlled_by = CHI }
                        611 = { is_controlled_by = CHI }
                        1154 = { is_controlled_by = CHI }
                        1232 = { is_controlled_by = CHI }
                        1421 = { is_controlled_by = CHI }
                        614 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_tianjin_s_0_visible = {
                NOT = {
                    1157 = { is_controlled_by = CHI }
                }
            }

            ccw_tianjin_0_visible = {
                NOT = {
                    1157 = { is_controlled_by = CHI }
                }
            }

            ccw_shanxi_0_visible = {
                NOT = {
                    OR = {
                        1233 = { is_controlled_by = CHI }
                        615 = { is_controlled_by = CHI }
                        1194 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_shan3xi_0_visible = {
                NOT = {
                    OR = {
                        1201 = { is_controlled_by = CHI }
                        622 = { is_controlled_by = CHI }
                        1200 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_henan_0_visible = {
                NOT = {
                    OR = {
                        607 = { is_controlled_by = CHI }
                        1226 = { is_controlled_by = CHI }
                        1225 = { is_controlled_by = CHI }
                        1224 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_ningxia_0_visible = {
                NOT = {
                    1199 = { is_controlled_by = CHI }
                }
            }
            
            ccw_chongqing_0_visible = {
                NOT = {
                    1189 = { is_controlled_by = CHI }
                }
            }

            ccw_shanghai_0_visible = {
                NOT = {
                    1215 = { is_controlled_by = CHI }
                }
            }

            ccw_shanghai_s_0_visible = {
                NOT = {
                    1215 = { is_controlled_by = CHI }
                }
            }

            ccw_zhejiang_0_visible = {
                NOT = {
                    OR = {
                        1220 = { is_controlled_by = CHI }
                        1159 = { is_controlled_by = CHI }
                        1219 = { is_controlled_by = CHI }
                        596 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_fujian_0_visible = {
                NOT = {
                    OR = {
                        1217 = { is_controlled_by = CHI }
                        595 = { is_controlled_by = CHI }
                        1218 = { is_controlled_by = CHI }
                        1216 = { is_controlled_by = CHI }
                        1431 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_guangdong_0_visible = {
                NOT = {
                    OR = {
                        1430 = { is_controlled_by = CHI }
                        1207 = { is_controlled_by = CHI }
                        1206 = { is_controlled_by = CHI }
                        592 = { is_controlled_by = CHI }
                        728 = { is_controlled_by = CHI }
                        1395 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_hongkong_0_visible = {
                NOT = {
                    326 = { is_controlled_by = CHI }
                }
            }

            ccw_hongkong_s_0_visible = {
                NOT = {
                    326 = { is_controlled_by = CHI }
                }
            }

            ccw_macau_0_visible = {
                NOT = {
                    729 = { is_controlled_by = CHI }
                }
            }

            ccw_macau_s_0_visible = {
                NOT = {
                    729 = { is_controlled_by = CHI }
                }
            }

            ccw_guangxi_0_visible = {
                NOT = {
                    OR = {
                        599 = { is_controlled_by = CHI }
                        1191 = { is_controlled_by = CHI }
                        593 = { is_controlled_by = CHI }
                        594 = { is_controlled_by = CHI }
                        1203 = { is_controlled_by = CHI }
                        1204 = { is_controlled_by = CHI }
                        1205 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_yunnan_0_visible = {
                NOT = {
                    OR = {
                        1196 = { is_controlled_by = CHI }
                        1192 = { is_controlled_by = CHI }
                        1195 = { is_controlled_by = CHI }
                        325 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_sichuan_0_visible = {
                NOT = {
                    OR = {
                        601 = { is_controlled_by = CHI }
                        1168 = { is_controlled_by = CHI }
                        1190 = { is_controlled_by = CHI }
                        605 = { is_controlled_by = CHI }
                        1188 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_xizang_0_visible = {
                NOT = {
                    OR = {
                        1155 = { is_controlled_by = CHI }
                        322 = { is_controlled_by = CHI }
                        1153 = { is_controlled_by = CHI }
                        1156 = { is_controlled_by = CHI }
                        1152 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_zangsouth_0_visible = {
                NOT = {
                    434 = { is_controlled_by = CHI }
                }
            }

            ccw_hubei_0_visible = {
                NOT = {
                    OR = {
                        1212 = { is_controlled_by = CHI }
                        620 = { is_controlled_by = CHI }
                        1211 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_hunan_0_visible = {
                NOT = {
                    OR = {
                        602 = { is_controlled_by = CHI }
                        1208 = { is_controlled_by = CHI }
                        1209 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_guizhou_0_visible = {
                NOT = {
                    OR = {
                        1210 = { is_controlled_by = CHI }
                        603 = { is_controlled_by = CHI }
                        1197 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_jiangxi_0_visible = {
                NOT = {
                    OR = {
                        1227 = { is_controlled_by = CHI }
                        1428 = { is_controlled_by = CHI }
                        1214 = { is_controlled_by = CHI }
                        1213 = { is_controlled_by = CHI }
                        600 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_hainan_0_visible = {
                NOT = {
                    591 = { is_controlled_by = CHI }
                }
            }

            ccw_xinjiang_0_visible = {
                NOT = {
                    OR = {
                        1158 = { is_controlled_by = CHI }
                        1160 = { is_controlled_by = CHI }
                        1161 = { is_controlled_by = CHI }
                        1162 = { is_controlled_by = CHI }
                        1163 = { is_controlled_by = CHI }
                        1164 = { is_controlled_by = CHI }
                        1165 = { is_controlled_by = CHI }
                        617 = { is_controlled_by = CHI }
                        618 = { is_controlled_by = CHI }
                        619 = { is_controlled_by = CHI }
                        287 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_qinghai_0_visible = {
                NOT = {
                    OR = {
                        1186 = { is_controlled_by = CHI }
                        1187 = { is_controlled_by = CHI }
                        604 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_gansu_0_visible = {
                NOT = {
                    OR = {
                        1198 = { is_controlled_by = CHI }
                        1193 = { is_controlled_by = CHI }
                        616 = { is_controlled_by = CHI }
                        283 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_neimeng_0_visible = {
                NOT = {
                    OR = {
                        1166 = { is_controlled_by = CHI }
                        1167 = { is_controlled_by = CHI }
                        621 = { is_controlled_by = CHI }
                        1202 = { is_controlled_by = CHI }
                        612 = { is_controlled_by = CHI }
                        715 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_mon_0_visible = {
                NOT = {
                    OR = {
                        1388 = { is_controlled_by = CHI }
                        1389 = { is_controlled_by = CHI }
                        1390 = { is_controlled_by = CHI }
                        1391 = { is_controlled_by = CHI }
                        330 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_tuva_0_visible = {
                NOT = {
                    329 = { is_controlled_by = CHI }
                }
            }

            ccw_liaoning_0_visible = {
                NOT = {
                    OR = {
                        1425 = { is_controlled_by = CHI }
                        716 = { is_controlled_by = CHI }
                        1417 = { is_controlled_by = CHI }
                        1413 = { is_controlled_by = CHI }
                        1394 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_jilin_0_visible = {
                NOT = {
                    OR = {
                        1414 = { is_controlled_by = CHI }
                        1415 = { is_controlled_by = CHI }
                        328 = { is_controlled_by = CHI }
                    }
                }
            }

            ccw_hlj_0_visible = {
                NOT = {
                    OR = {
                        1424 = { is_controlled_by = CHI }
                        714 = { is_controlled_by = CHI }
                        717 = { is_controlled_by = CHI }
                        1416 = { is_controlled_by = CHI }
                    }
                }
            }
"""

# 使用正則表達式切分文本，提取出「地區名稱」與「後面的區塊」
# 例如提取出 'taiwan' 和它包含的 state 代碼
parts = re.split(r'ccw_([a-zA-Z0-9_]+)_0_visible\s*=\s*\{', text)

# parts[1] 會是第一個地區名，parts[2] 是它的內容，依此類推
for i in range(1, len(parts), 2):
    prov_name = parts[i]
    block_content = parts[i+1]
    
    # 抓取該區塊內所有的數字 (State ID)
    states = re.findall(r'(\d+) = \{\s*is_controlled_by', block_content)
    
    if states:
        print(f"    ccw_{prov_name}_divider = {{")
        print(f"        icon = GFX_ccw_{prov_name}_divider")
        print(f"        allowed = {{original_tag = CHI}}")
        print(f"        available = {{ hidden_trigger = {{always = no}}}}")
        print(f"        visible = {{")
        print(f"            OR = {{")
        print(f"                check_variable = {{ CHI_ccw_dec_visible = 1 }}")
        print(f"                is_ai = yes")
        print(f"            }}")
        print(f"        }}")
        print(f"        highlight_states = {{")
        print(f"            highlight_state_targets = {{")
        for state in states:
            print(f"                state = {state}")
        print(f"            }}")
        print(f"        }}")
        print(f"    }}\n")