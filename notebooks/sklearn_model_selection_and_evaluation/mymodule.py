import matplotlib.pyplot as plt


def plot_schema(cv, y_classes):

    max_partitions = 30
    n_splits = min(cv.get_n_splits(y_classes), max_partitions)

    x_vline = y_classes.count(0)

    plt.figure(figsize=(8, 0.4 * min(max_partitions, n_splits)))

    for i_cv, (train, test) in enumerate(cv.split(y_classes, y_classes)):

        for i_sample in range(len(y_classes)):

            marker = "o" if y_classes[i_sample] == 0 else "s"
            color = "tab:blue" if i_sample in train else "tab:orange"

            plt.plot(
                i_sample if i_sample < x_vline else i_sample + 1,
                i_cv,
                marker=marker,
                color=color,
                markersize=12,
                alpha=0.8,
                markeredgecolor="black",
            )

        if i_cv >= max_partitions - 1:
            break

    plt.ylim(-1, n_splits)
    plt.axvline(x_vline, linestyle="-", color="k", linewidth=2)
    plt.xticks([], [])
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.yticks(range(0, min(max_partitions, n_splits)))
    plt.gca().invert_yaxis()
    plt.ylabel("CV sample")
    plt.show()