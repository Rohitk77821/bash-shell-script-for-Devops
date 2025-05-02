
#install psutil: pip install psutil
import psutil
cpu_usage=psutil.cpu_percent(interval=1)
print(f"cpu_usage: {cpu_usage}%")

if cpu_usage >80:
    print("high cpu usage! scale up")
else:
    print("the cpu is normal")