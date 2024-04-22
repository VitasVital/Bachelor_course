# import plotly.graph_objects as go
# import numpy as np
# N = 10000
# fir = go.Figure(data=go.Scattergl(
#     x = np.random.randn(N),
#     y = np.random.randn(N),
#     mode='markers',
#     marker=dict(
#         color=np.random.randn(N),
#         colorscale='speed',
#         line_width=1
#     )
# ))
# fir.show()

#######################################

# import plotly.graph_objects as go
# import numpy as np
# np.random.seed(1)
# y0 = np.random.randn(50)
# y1 = np.random.randn(50)
# y2 = np.random.randn(50)
# y3 = np.random.randn(50)
# fig = go.Figure()
# fig.add_trace(go.Box(x=y0))
# fig.add_trace(go.Box(x=y1))
# fig.add_trace(go.Box(x=y2))
# fig.add_trace(go.Box(x=y3))
# fig.show()

#########################################3

# import plotly.express as px
# df = px.data.iris()
# df["e"] = df["sepal_width"]/10
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", error_x="e", error_y="e")
# fig.show()

##########################################

import plotly.express as px
df = px.data.iris()
df["e_plus"] = df["sepal_width"]/100
df["e_minus"] = df["sepal_width"]/40
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", error_y="e_plus", error_y_minus="e_minus")
fig.show()