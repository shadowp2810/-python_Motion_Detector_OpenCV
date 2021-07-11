from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool , ColumnDataSource
import pandas

from app import df      #get dataframe from app after execution is complete

# df = pandas.read_csv( "Times.csv" )

df[ "Start" ] = pandas.to_datetime( df.Start, format = "%Y-%m-%d %H:%M:%S" )
df[ "Start_string" ] = df[ "Start" ].dt.strftime( "%Y-%m-%d %H:%M:%S" )

df[ "End" ] = pandas.to_datetime( df.End, format = "%Y-%m-%d %H:%M:%S" )
df[ "End_string" ] = df[ "End" ].dt.strftime( "%Y-%m-%d %H:%M:%S" )

cds = ColumnDataSource( df ) 

p = figure( 
        x_axis_type = "datetime" , 
        height = 100 , width = 500 , 
        sizing_mode = "scale_width" ,
        title = "Motion Graph" )

p.yaxis.minor_tick_line_color = None             # make measure levels on y axis not visible
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool( 
            tooltips = [ 
                ( "Start" , "@Start_string" ) , 
                ( "End" , "@End_string" ) ] )

p.add_tools( hover )

q = p.quad( 
        left = "Start" , 
        right = "End" , 
        bottom = 0 , 
        top = 1 , 
        color = "green" , 
        source = cds )

output_file( "MotionGraph.html" )

show( p )

