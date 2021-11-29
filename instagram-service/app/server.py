from  flask_apscheduler import APScheduler
from  app import create_app
from  job.scrappe_job import scrappe

scheduler = APScheduler()
app = create_app()

if __name__ == '__main__':
    # 30 분 간격
    scheduler.add_job(id="Scheduled task",func = scrappe, trigger = 'interval',seconds=30*60)
    scheduler.start()
    app.run(host ='0.0.0.0',port=8000)