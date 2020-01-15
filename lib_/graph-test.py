import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[100,95,92,86,74,88,75,96,90,100,88,72,90,80,77,62,88,89,24,99,76,84,77,98],
    theta=['d01','d02','d03','d04','d05','d06','d07','d08','d09','d10','d11','d12','r01','r02','r03','r04','r05','r06','r07','r08','r09','r10','r11','r12']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')

fig.show()
#fig.write_image("fig1.jpeg")