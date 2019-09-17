class Transfer:
    def choose(self):
        '''主体程序，处理输入和输出'''
        print('欢迎使用万能单位转换器'.center(50, '*'))
        menu = {
            '温度转换输入示例：': '1C或者1F',
            '长度转换输入示例：': '1里或者1英里',
            '货币转换输入示例：': '1元或者1美元'
        }
        for k, v in menu.items():
            print(k, v)
        choose = input('请输入内容：')

        if choose.endswith('C'):
            TransferTemp().c_f(choose)
        elif choose.endswith('F'):
            TransferTemp().f_c(choose)
        elif choose.endswith('英里'):
            TransferLen().mi_km(choose)
        elif choose.endswith('里'):
            TransferLen().km_mi(choose)
        elif choose.endswith('美元'):
            TransferCun().usd_cny(choose)
        elif choose.endswith('元'):
            TransferCun().cny_usd(choose)
        else:
            print('单位输入有误，请重新输入！')


class TransferTemp:
    def c_f(self, choose):
        '将摄氏度转为华氏度'
        choose = float(choose.strip('C'))
        Tf = round(( 9 / 5 ) * choose + 32, 2)
        print(f'{choose}C = {Tf}F')
    
    def f_c(self, choose):
        '将华氏度转换为摄氏度'
        choose = float(choose.strip('F'))
        Tc = round(( 5 / 9 ) * ( choose - 32 ), 2)
        print(f'{choose}F = {Tc}C')



class TransferLen:
    def mi_km(self, choose):
        '将英里转化为里'
        choose = float(choose.strip('英里'))
        li = round( choose / 0.310685596119, 2 )
        print(f'{choose}英里 = {li}里')
    
    def km_mi(self, choose):
        '将里转化为英里'
        choose = float(choose.strip('里'))
        mi = round( choose * 0.310685596119, 2 )
        print(f'{choose}里 = {mi}英里')


class TransferCun:
    def usd_cny(self, choose):
        '将美元转换为元'
        choose = float(choose.strip('美元'))
        yuan = round( choose / 0.1393, 2 )
        print(f'{choose}美元 = {yuan}元')
    
    def cny_usd(self, choose):
        '将元转换为美元'
        choose = float(choose.strip('元'))
        dor = round( choose * 0.1393, 2 )
        print(f'{choose}元 = {dor}美元')


def main():
    Transfer().choose()
    while True:
        if input('是否退出（y/n）？') == 'y':
            break
        else:
            Transfer().choose()

if __name__ == "__main__":
    main()
