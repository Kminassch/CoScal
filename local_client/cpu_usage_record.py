import psutil
import os, datetime, time

record_interval = 0.5  # unit is second


def getMemCpu():
    data = psutil.virtual_memory()
    total = data.total
    free = data.available
    memory = str(int(round(data.percent)))
    cpu = str(psutil.cpu_percent(interval=record_interval))
    return cpu, memory


def main():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fname = "report.csv"
    with open('%s' % fname, 'w') as f:
        title_str = "CPU ,Mem"
        print(title_str)
        f.write("CPU ,Mem" + "\n")
        while True:
            info = getMemCpu()
            tmp_str = "%5s,%4s" % (info[0], info[1])
            print(tmp_str)
            f.write(tmp_str + "\n")
            f.flush()
            time.sleep(0.5)


if __name__ == "__main__":
    main()
