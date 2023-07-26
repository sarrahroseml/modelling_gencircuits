# Parameters
beta_1 = 100
gamma = np.array([1, 2, 3])

# Compute dynamics
t = np.linspace(0, 6, 400)
x = [beta_1 / g * (1 - np.exp(-g * t)) for g in gamma]

# Set up plots
colors = bokeh.palettes.Oranges5
p1 = bokeh.plotting.figure(
    frame_height=175,
    width=300,
    x_axis_label="t",
    y_axis_label="x(t)",
    title=f"β₁ = {beta_1}, γ = {gamma}",
)
p2 = bokeh.plotting.figure(
    frame_height=175,
    width=300,
    x_axis_label="t",
    y_axis_label="x(t)",
    title="same plot, normalized by steady states",
)
p2.x_range = p1.x_range

# Populate graphs
for x_vals, g, color in zip(x, gamma, colors):
    p1.line(t, x_vals, color=color, line_width=2)
    p1.circle(1 / g, beta_1 / g * (1 - np.exp(-1)), color=color, size=10)
    p2.line(t, x_vals / x_vals.max(), color=color, line_width=2)
    p2.circle(1 / g, 1 - np.exp(-1), color=color, size=10)

bokeh.io.show(bokeh.layouts.gridplot([p1, p2], ncols=2))
