import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize_insertion_sort(arr):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Number of iterations: {iteration[0]}")

    def insertion_sort_visualized(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                yield arr
            arr[j + 1] = key
            yield arr

    anim = animation.FuncAnimation(
        fig,
        func=update_fig,
        fargs=(bar_rects, iteration),
        frames=insertion_sort_visualized(arr),
        repeat=False,
        blit=False,
        interval=100,
        save_count=9000,
    )

    plt.show()

if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    visualize_insertion_sort(sample_array)