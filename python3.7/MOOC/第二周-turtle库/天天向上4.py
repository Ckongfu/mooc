import MyDay as M #导入MyDay模块/Users/zouguannan/PycharmProjects/untitled/venv/lib/python3.7/site-packages

dayfactory=0

while M.Day(dayfactory)<37.78:
    dayfactory+=0.0002
print('工作日努力的参数是：{:.3f}'.format(dayfactory))
