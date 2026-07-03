import datetime
import os
import sys

today =datetime.date.today()
# 格式化输出
ISOFORMAT='%Y%m%d' #设置输出格式
date = today.strftime(ISOFORMAT)

# 自动修复缺失的栅格图
if os.path.exists('scripts/fix_images.py'):
    os.system(f'{sys.executable} scripts/fix_images.py')

os.system('git add .')
os.system('git commit -m "updated site %s"' %date)
os.system('git push')