from time import time
from twautomate import get_new_followers
from twautomate import get_old_followers
from twautomate import send_direct_message
from twautomate import save_followers
from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == "__main__":
    def tasks():
        t1 = time()
        old = get_old_followers("paraazz")
        new = get_new_followers("paraazz")
        new_followers = list(set(new).difference(set(old)))


        save_followers("paraazz", new)
        for n in new_followers:
            print("message sent to {}".format(n))
            send_direct_message(n)
        print("Task Complete")
        t2 = time()
        print("Task completed in sec: ", t2-t1)

    tasks()
    sched = BlockingScheduler()
    @sched.scheduled_job('interval', minutes=15)
    def timed_job():
        try:
            tasks()
        except Exception as e:
            print("Schedular Error: ", e)


    sched.start()

