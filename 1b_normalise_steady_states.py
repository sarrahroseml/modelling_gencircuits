# Parameters
beta_1 = 100

#The three lines in each plot represent the protein concentration over time for three different degradation rates (γ).
#Each line color corresponds to one of these degradation rates.
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

#In the second plot, the protein concentration is normalized by its steady state value for each degradation rate. 
#This allows for a comparison of the response times (how quickly the system reaches a certain fraction of the steady state level) 
#for different degradation rates, independent of the absolute concentration levels.
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

    #normalisation
    #x_vals is the array of protein concentrations over time for a specific degradation rate
    #x_vals.max() is the maximum value in this array, which corresponds to the steady-state protein concentration
    p2.line(t, x_vals / x_vals.max(), color=color, line_width=2)
    p2.circle(1 / g, 1 - np.exp(-1), color=color, size=10)

bokeh.io.show(bokeh.layouts.gridplot([p1, p2], ncols=2))
