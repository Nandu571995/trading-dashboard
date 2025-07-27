import matplotlib.pyplot as plt
import numpy as np

def get_oi_volume_heatmap(symbol):
    fig, ax = plt.subplots()
    heatmap = np.random.rand(10, 10)
    cax = ax.imshow(heatmap, cmap='coolwarm')
    ax.set_title(f"{symbol} OI & Volume Heatmap")
    return fig
