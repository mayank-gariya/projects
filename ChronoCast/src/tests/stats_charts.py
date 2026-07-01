import plotly.express as px

def without_difference(df):
    
    fig = px.line(
        df,
        x=df.index,
        y='Close',
        title='without difference'
    )
    
    fig.update_layout(
        template="plotly_white",
        height=500,
    )
    
    return fig
        
def first_differencing_chart(df):

    fig = px.line(
        df,
        x=df.index,
        y="Differenced",
        title="First Difference",
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
    )

    return fig

def second_differencing_chart(df):

    fig = px.line(
        df,
        x=df.index,
        y="Second_Difference",
        title="Second Difference",
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
    )

    return fig

def log_differencing_chart(df):

    fig = px.line(
        df,
        x=df.index,
        y="Log_Close",
        title="log Difference",
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
    )

    return fig