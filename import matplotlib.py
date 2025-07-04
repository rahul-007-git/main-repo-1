import matplotlib.pyplot as plt
import matplotlib.animation as animation

name = "STEEL BOT BOY"

fig, ax = plt.subplots()
ax.axis('off') 

text = ax.text(0.5, 0.5, '', fontsize=30, color='red',
               fontweight='bold', family='sans-serif', ha='center', va='center')

def update(frame):
    text.set_text(name[:frame])  
    return text,
ani = animation.FuncAnimation(
    fig, update, frames=len(name)+1, interval=300, repeat=False
)

plt.show()
