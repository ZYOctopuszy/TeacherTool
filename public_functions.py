def split_print_list(l: list[int|float], endless:bool = False) -> str:
    try:
        if len(l) == 0:
            return "全部交齐[撒花][撒花][撒花]"
        text = ""
        max_length: int = len(str(max(l)))                  # 计算列表中最大元素的字符串长度作为对齐基准
        p_p_l: list = []                                    # 创建空白填充后的字符串列表
        for i in range(len(l)):                             # 遍历原始列表，将每个元素转为字符串并进行空白右填充
            p_p_l.append(str(l[i]).ljust(max_length, " "))
        for i in range(len(p_p_l)):                         # 格式化打印输出：每行显示5个元素
            text+=(str(p_p_l[i])+" ")                       # 打印当前元素(不换行)
            if (i + 1) % 5 == 0 and not endless:            # 每打印5个元素后换行
                text+="\n"
        if len(p_p_l) % 5 != 0:                             # 当元素总数不是5的倍数时补充换行
            text+="\n"
        print("text: "+text)
        return text
    except:
        return "Error!!! from split_print_list"
