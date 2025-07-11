from public_functions import split_print_list


class HomeworkRegister:
    """
    作业登记器,可以实现删除,增加的操作
    """

    def __init__(self, l: list):
        # 初始化学生名单
        self.student_list: list = l
        # 备份学生名单，防止误操作丢失数据
        self.student_list_back = self.student_list[:]
        # 初始化命令字符串，用于存储用户输入的命令
        self.command: str = ''
        # 初始化命令列表，包含允许的操作命令
        self.commands_list: list = ["r", "l"]
        print(self.student_list)

    def finish(self, command: str, split: str=" ") -> bool:  # 移除名单
        self.student_list = self.student_list_back[:]
        if command != "":    
            # 记录已处理的学生ID数量
            n = 0
            try:
                try:
                    # 尝试移除单个学生ID
                    self.student_list.remove(int(command))
                except:
                    # 将输入的命令按空格分割成学生ID列表
                    id_list = command.replace("\n", split).strip(str(split)).split(str(split))
                    for stu_id in id_list[:]:
                        if not stu_id.isdigit():
                            id_list.remove(stu_id)
                    for stu_id in id_list:
                        # 移除每个学生ID
                        if int(stu_id) in self.student_list:
                            self.student_list.remove(int(stu_id))
                            # 增加已处理的学生ID数量
                            n += 1
            except:
                # 其他未知错误处理
                print("Unknown error!!! from Finish")
                return False
            return True

    def show_unsubmitted(self, endless:bool = False) -> str:  # 显示名单
        # 对学生名单进行排序，确保按升序输出
        self.student_list.sort()
        undone_str = split_print_list(self.student_list, endless)
        return undone_str
