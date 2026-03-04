import datetime
import os

today =datetime.date.today()
# 格式化输出
ISOFORMAT='%Y%m%d' #设置输出格式
date = today.strftime(ISOFORMAT)


os.system('git add .')
os.system('git commit -m "updated site %s"' %date)
os.system('git config --global credential.helper wincred')
os.system('git push')