""""
Implementing a simple first-order system response plot
""""
#beta is the production rate and gamma is the degradation rate
beta = 100
gamma = 1

# Dynamics
#The time variable t is defined as a numpy array ranging from 0 to 6 with 400 points.
t = np.linspace(0, 6, 400)
#The solution to the differential equation x is calculated using the analytical solution of the first-order linear differential equation.
x = beta / gamma * (1 - np.exp(-gamma * t))

# Plot response
p = bokeh.plotting.figure(
    frame_height=275,
    frame_width=375,
    x_axis_label="t",
    y_axis_label="x(t)",
    title=f"β = {beta}, γ = {gamma}",
)
p.line(t, x, line_width=2)

# Calculate  response time t0 (when the system reaches the level 1−1/e), and marks it on the plot with a circle and a dashed line
t0 = 1 / gamma
x0 = beta / gamma * (1 - np.exp(-1))
Response time: The code calculates the response time t0 (when the system reaches the level 

# Add the glyph with label
source = bokeh.models.ColumnDataSource(
    data=dict(t0=[t0], x0=[x0], text=["response time"])
)
p.circle(x="t0", y="x0", source=source, size=10)
p.add_layout(
    bokeh.models.LabelSet(
        x="t0", y="x0", text="text", source=source, x_offset=10, y_offset=-10
    )
)
p.add_layout(
    bokeh.models.Span(
        location=t0,
        level="underlay",
        dimension="height",
        line_color="black",
        line_dash="dashed",
    )
)

bokeh.io.show(p)
