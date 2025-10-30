import matplotlib.pyplot as plt
import numpy as np

def plot_grid(grid, path, start, goal):
    n, m = len(grid), len(grid[0])
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(m + 1) - 0.5)
    ax.set_yticks(np.arange(n + 1) - 0.5)
    ax.grid(True)
    ax.set_xlim(-0.5, m - 0.5)
    ax.set_ylim(-0.5, n - 0.5)
    ax.set_aspect('equal')

    # Plot obstacles
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                ax.add_patch(plt.Rectangle((j - 0.5, n - i - 1 - 0.5), 1, 1, color='black'))

    # Plot path
    for (i, j) in path:
        ax.add_patch(plt.Circle((j, n - i - 1), 0.2, color='yellow'))

    # Plot start and goal
    ax.add_patch(plt.Circle((start[1], n - start[0] - 1), 0.4, color='green'))
    ax.add_patch(plt.Circle((goal[1], n - goal[0] - 1), 0.4, color='red'))

    # Add labels
    ax.text(start[1], n - start[0] - 1, 'Start', color='white', ha='center', va='center', fontsize=10, weight='bold')
    ax.text(goal[1], n - goal[0] - 1, 'Goal', color='white', ha='center', va='center', fontsize=10, weight='bold')

    # Legend (colored markers)
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', label='Start', markerfacecolor='green', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', label='Goal', markerfacecolor='red', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', label='Path', markerfacecolor='yellow', markersize=10),
        plt.Line2D([0], [0], marker='s', color='w', label='Obstacle', markerfacecolor='black', markersize=10)
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    # Add title
    ax.set_title("AI Pathfinder - BFS Visualization", fontsize=14, fontweight='bold')

    plt.show()
