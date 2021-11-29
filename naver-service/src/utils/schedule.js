const { ToadScheduler, SimpleIntervalJob, AsyncTask } = require('toad-scheduler')

class Scheduler{
    constructor(saveBlogData){
        this.saveBlogData = saveBlogData;
        this.scheduler = new ToadScheduler();
    }

    run(){ 
        const task = new AsyncTask(
            'simple task', 
            this.saveBlogData,
            (err) => {  
                console.log(err);
                console.log('----종료----')
                this.stop();
             }
        )
        const job = new SimpleIntervalJob({ seconds: 110, }, task)
        this.scheduler.addSimpleIntervalJob(job);
    }

    stop(){
        this.scheduler.stop();
    }
}

module.exports = Scheduler;

 