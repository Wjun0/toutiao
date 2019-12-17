import time

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler

# 设置最大线程数
executor = ThreadPoolExecutor(max_workers=10)

#创建调度器
scheduler = BackgroundScheduler(executors={'default':executor})

def func():
    print('任务执行')

# 三种模式如下：

#date模式为一次性定时任务
# job1 = scheduler.add_job(func, "date" )

#interval为周期性定时任务，在规定时间内每10秒执行一次
# job2 = scheduler.add_job(func, "interval", seconds=10, start_date='2019-12-16 16:20:00',end_date='2019-12-18 16:25:00')

#cron为周期性定时任务，每分钟的第10秒会执行，可再加参数hour,minute, 设置每天几点几分执行
job3 = scheduler.add_job(func, "cron", second=10)

scheduler.start()

#使用死循环，让程序不结束
while True:
    time.sleep(36000)



