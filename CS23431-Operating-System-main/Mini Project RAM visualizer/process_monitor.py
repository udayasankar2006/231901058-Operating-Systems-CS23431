import psutil

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            mem_info = proc.info['memory_info']
            ram_mb = mem_info.rss / 1024 / 1024
            ram_pct = proc.memory_percent()
            cpu_pct = proc.cpu_percent(interval=None)  # non-blocking

            processes.append((
                pid,
                name,
                round(ram_mb, 2),
                round(ram_pct, 3),
                round(cpu_pct, 2)
            ))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes
