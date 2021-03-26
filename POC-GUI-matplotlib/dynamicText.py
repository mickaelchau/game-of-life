#POC dynamic text with matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
text = ax.text(-10, -10, 'Text')

def on_mouse_move(event):
    if None not in (event.xdata, event.ydata):
        text.set_position((event.xdata, event.ydata))
        text.set_text("kdsfkf")
        fig.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
plt.show()
