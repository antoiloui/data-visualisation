import plotly.graph_objects as go
import plotly.io as pio

colors = ["##FFFFFF","#ff8080","#F2F8FD","#ff4d4d","#F2F8FD","#cc0000","#F2F8FD"]
template="plotly_dark"

fig = go.Figure(go.Sunburst(
    labels=["GHG (%)", "Food", "Other", "Animal products", "Other ", "Beef and Lamb", "Other  "],
    parents=["", "GHG (%)", "GHG (%)", "Food", "Food", "Animal products", "Animal products"],
    values=[100, 26, 74, 15, 11, 7.5, 7.5],
    branchvalues="total",
    marker=dict(colors=colors)
))

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), template=template)
pio.write_html(fig, file='index.html', auto_open=True)
fig.show()


# style="background-color:black"