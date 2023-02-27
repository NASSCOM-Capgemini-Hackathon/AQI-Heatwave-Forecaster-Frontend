from plotly import graph_objects as go


def bargraph(x_data, y_data1, y_data1_name, xaxis_title, yaxis_title, y_data2=None, y_data2_name=None):
    """
    """
    if y_data2 == None and y_data2_name == None:
        fig = go.Figure(data=[
            go.Bar(name=y_data1_name, x=x_data,
                   y=y_data1, marker_color='crimson'),
        ])
    else:
        fig = go.Figure(data=[
            go.Bar(name=y_data1_name, x=x_data,
                   y=y_data1, marker_color='crimson'),
            go.Bar(name=y_data2_name, x=x_data, y=y_data2, marker_color='navy')
        ])

    fig.update_layout(xaxis_title=xaxis_title,
                      yaxis_title=yaxis_title, barmode='group')
    return fig


def linegraph(x_data, y_data1, y_data1_name, xaxis_title, yaxis_title, y_data2=None, y_data2_name=None):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data, y=y_data1, name=y_data1_name))

    if y_data2 != None and y_data2_name != None:
        fig.add_trace(go.Scatter(x=x_data, y=y_data2,
                                 name=y_data2_name, marker_color='crimson'))
    fig.update_layout(
        xaxis_title=xaxis_title, yaxis_title=yaxis_title, font=dict(color="white"))
    return fig
