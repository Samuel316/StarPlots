#!/usr/bin/env python3
# coding=utf-8
"""
s1887484, 05/12/2019
samueljohnlloyd12@gmail.com

Parameters
----------

Return
------
"""

from pathlib import Path

import yaml
import matplotlib.pyplot as plt


def plot_star(star, y_axis, ax=None, fig=None):
    """

    Parameters
    ----------
    star : str
        name of star to plot
    y_axis : str
        {"X/H", "X/Fe", "Loge"}
    ax : matplotlib.axis
        axs to add plot to
    fig : matplotlib.fig
        figure to add axis to

    Returns
    -------
    matplotlib.fig

    """

    fig = fig or plt.gcf()
    ax = ax or plt.gca()

    with (Path(__file__).parent / f"../Data/{star}.yml").open() as file:
        he13272326 = yaml.load(file, Loader=yaml.FullLoader)

    with (Path(__file__).parent / "../Data/elements.yml").open() as file:
        elements_names = yaml.load(file, Loader=yaml.FullLoader)

    elements = []
    zs = []
    abundances = []
    upper_limits = []
    errors = []

    for element, abundance in he13272326["Abundance"][y_axis].items():

        el = element.split("(")

        if "UL)" in el:
            upper_limits.append(True)
        else:
            upper_limits.append(False)

        elements.append(el[0])
        ax.text(elements_names["charge_numbers"][el[0]] - 0.4, abundance + 0.3, el[0])

        zs.append(elements_names["charge_numbers"][el[0]])
        abundances.append(float(abundance))

    for element, error in he13272326["Abundance"][f"{y_axis}_error"].items():
        errors.append(float(error))

    ax.errorbar(
        zs, abundances, errors, uplims=upper_limits, fmt=".", label=he13272326["Star"]
    )
    ax.legend()
    ax.set_xlabel("Z")
    ax.set_ylabel(f"[{y_axis}]")

    return fig


if __name__ == "__main__":
    plot_star("HE1327-2326", "X/H")
    plot_star("HE0107-5240", "X/H")
    plt.show()
