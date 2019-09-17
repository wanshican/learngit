import pickle


class Memo:
    def __init__(self,name,thing,date):
        '初始化数据'
        self._id = 0
        self.name = name
        self.thing = thing
        self.date = date
    
    def input_memo(self):
        '输入记录'
        self._id += 1
        self.name = input('name:')
        self.thing = input('thing:')
        self.date = input('date:')
        one = {'id': self.id, 'name': self.name, 'thing': self.thing, 'date': self.date}
        memo.add(one)
    
    @property
    def id(self): # 只读
        return self._id

class MemoAdmin:
    """管理记录"""
    def __init__(self, memo_list, dir):
        '初始化数据'
        self.dir = dir
        self.memo_list = memo_list
    
    def welcome(self):
        '打印选择菜单'
        print('欢迎使用51备忘录'.center(50, '-'))
        for k,v in self.dir.items():
            print(f'{k}:{v}')        
        select = input('请选择你的操作选项 (示例 1)：')
        return select
    

    def add(self,one): 
        '新增记录'
        self.memo_list.append(one)
        memo.query()
        print('增加成功')
    
    
    def dele(self):
        '删除记录'
        temp = input('请选择你将要删除的记录（示例 1或者2或者3 ）:')
        self.memo_list.pop(int(temp)-1)
        print('删除成功')
        memo.query()
    
    
    def modify(self):
        '删除记录'
        temp1 = input('请输入你要修改的记录（示例 1或者2或者3）:')
        temp2 = input(f'你要修改的记录是{self.memo_list[int(temp1)-1]}，请输入要修改的值（示例：name:zhangsan）:')
        temp3 = temp2.split(':')
        self.memo_list[int(temp1)-1][temp3[0]] = temp3[1]   # 列表中找出嵌套的字典key和value
        print('修改成功')
        memo.query()
    
    
    def save(self): 
        '保存记录'
        with open('db.pkl', 'wb') as f:
            f.write(pickle.dumps(memo_list))
            print('保存成功')
    
    
    def load(self):
        '加载记录'
        with open('db.pkl', 'rb') as f:
            data = pickle.loads(f.read())
            print(data)
            print('下载成功')
    
    
    def query(self): 
        '查询记录'
        i = 0
        for k in memo_list:
            i += 1
            print(f'项目{i}{k}')


def main():
    while True:
        t = memo.welcome()
        if t == '1':
            start.input_memo()
        elif t == '2':
            memo.dele()    
        elif t == '3':
            memo.modify()
        elif t == '4':
            memo.query()
        elif t == '5':
            memo.save()
        elif t == '6':
            memo.load()
        else:
            print('结束')
            break


if __name__ == "__main__":
    memo_list = []
    dir = {'1':'Add',
            '2':'Dele',
            '3':'Modify',
            '4':'Query',
            '5':'Save',
            '6':'Load'
            }
    start = Memo('', '', '')
    memo = MemoAdmin(memo_list,dir)
    main()