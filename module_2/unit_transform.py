print('欢迎使用万能单位转换器'.center(50, '*'))
menu = {
    'T': '温度转换',
    'L': '长度转换',
    'C': '货币转换'
}
for k, v in menu.items():
    print(k, v)
choose = input('请输入转换类型：')

if choose == 'T':
    temp = input('请输入温度（示例：1C或者1F）:')
    if temp.endswith('C'):
        temp = float(temp.strip('C'))
        Tf = round(( 9 / 5 ) * temp + 32, 2)
        print(f'{temp}C = {Tf}F')
    elif temp.endswith('F'):
        temp = float(temp.strip('F'))
        Tc = round(( 5 / 9 ) * ( temp - 32 ), 2)
        print(f'{temp}F = {Tc}C')
    else:
        print('单位输入有误，请重新输入！')

elif choose == 'L':
    lenth = input('请输入长度（示例：1里或者1英里）：')
    if lenth.endswith('英里'):
        lenth = float(lenth.strip('英里'))
        li = round( lenth / 0.310685596119, 2 )
        print(f'{lenth}英里 = {li}里')
    elif lenth.endswith('里'):
        lenth = float(lenth.strip('里'))
        mi = round( lenth * 0.310685596119, 2 )
        print(f'{lenth}里 = {mi}英里')
    else:
        print('单位输入有误，请重新输入！')

elif choose == 'C':
    ccy = input('请输入金额（示例：1元或者1美元）：')
    if ccy.endswith('美元'):
        ccy = float(ccy.strip('美元'))
        yuan = round( ccy / 0.1393, 2 )
        print(f'{ccy}美元 = {yuan}元')
    elif ccy.endswith('元'):
        ccy = float(ccy.strip('元'))
        dor = round( ccy * 0.1393, 2 )
        print(f'{ccy}元 = {dor}美元')
    else:
        print('单位输入有误，请重新输入！')

else:
    print('请输入正确的转换类型')