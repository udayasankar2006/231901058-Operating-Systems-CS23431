# process_graph.py
import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ProcessGraph:
    def __init__(self, root, pid, name):
        self.root = root
        self.pid = pid
        self.name = name
        self.mem_data = []
        self.time_data = []
        self.max_points = 60  # keep 60 seconds of data

        self.fig, self.ax = plt.subplots(facecolor="#1e1e1e")
        self.ax.set_title(f"Memory Usage (MB)", color="white")
        self.ax.set_facecolor("#2e2e2e")
        self.ax.tick_params(colors='white')
        self.line, = self.ax.plot([], [], color='lime')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.ani = animation.FuncAnimation(self.fig, self.update_graph, interval=1000)

    def update_graph(self, i):
        try:
            proc = psutil.Process(self.pid)
            mem = proc.memory_info().rss / 1024**2
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            mem = 0
        if len(self.mem_data) >= self.max_points:
            self.mem_data.pop(0)
            self.time_data.pop(0)
        self.mem_data.append(mem)
        self.time_data.append(len(self.time_data))
        self.line.set_data(self.time_data, self.mem_data)
        self.ax.relim()
        self.ax.autoscale_view()
