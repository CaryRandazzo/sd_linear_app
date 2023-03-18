import streamlit as st
import pandas as pd
import numpy as np

# pd.set_option('display.float_format', '{:.8f}'.format)

# Create an empty dataframe with 5 rows and 5 columns
df = pd.DataFrame( {"x-data":[], "y-data":[], "x-squared":[], "xy":[], "mx+b":[], "d-squared":[]} )

st.text("Please enter the data in each line as provided - press ENTER to apply changes to the input")


try:
    x_arr = st.text_input("Enter the comma separated x-data such as '1,3,2,5,7' ")
    if x_arr != None:
        x_arr = x_arr.split(",")
        x_arr = [float(val) for val in x_arr] #[int(val) for val in x_arr]

        # x_squared = x_arr**2

    y_arr = "2,6,4,10,14"
    y_arr = st.text_input("Enter the comma separated y-data such as '2,6,4,10,14' ")
    if y_arr != None:
        
        y_arr = y_arr.split(',')
        y_arr = [float(val) for val in y_arr]
except:
    pass

try:
    df["x-data"] = x_arr
    df["y-data"] = y_arr
    df["x-squared"] = [val**2 for val in df["x-data"].values]
    df["xy"] = df["x-data"]*df["y-data"]
    print(df["xy"])
except:
    pass

try:
    if x_arr != None and y_arr != None:

        N = df.shape[0]

        # print("a")
        sumxi = df["x-data"].sum()
        # print("b")
        sumyi = df["y-data"].sum()
        # print("c")
        sumxiyi = df["xy"].sum()
        # print("d")
        sumxi_sq = df["x-squared"].sum()
        # print("e")

        print("sumxiyi:",sumxiyi)
        print("sumxi:",sumxi)
        print("sumyi:",sumyi)
        print("sumxi_sq:",sumxi_sq)
        print("N:",N)
        
        _delta = N*sumxi_sq - sumxi**2 
        print("delta:",_delta)
        m = (N*sumxiyi - sumxi*sumyi) / _delta
        b = (sumxi_sq * sumyi - sumxi*sumxiyi) / _delta
        print("m:",m)
        print("b:",b)
        
        
except Exception as e:
    print("Error1:",e)


try:
    df["mx+b"] = m*df["x-data"]+b #mxb_arr 
    df["d-squared"] = df["y-data"]-(m*df["x-data"]+b)
    print(df["y-data"]-(m*df["x-data"]+b))
    print(df["d-squared"])
except Exception as e:
    print("Error2:",e)
    


# Set the display width of the cells to maximum
pd.set_option('display.max_colwidth', None)

try:
    format_dict = {'x-data': '{:.8f}', 'y-data': '{:.8f}','x-squared': '{:.8f}','xy': '{:.8f}','mx+b': '{:.8f}','d-squared': '{:.8f}'}
    styled_df = df.style.format(format_dict)

    # Display the restyled DataFrame
    st.write(styled_df)

except Exception as e:

    print("Error3:",3)


try:
    st.latex(r"""\Delta""")
    st.text(_delta)
    st.latex(r"""m""")
    st.text(m)
    st.latex(r"""b""")
    st.text(b)

    sigma_y_sq = 1/(N-2) * df["d-squared"].sum()
    st.latex(r"""\sigma_y^2""")
    st.text(sigma_y_sq)

    sigma_m = np.sqrt( (N*sigma_y_sq)/_delta ) * df["d-squared"].sum()
    st.latex(r"""\sigma_m""")
    st.text(sigma_m)

    sigma_b = np.sqrt( (sigma_y_sq * sumxi_sq) / _delta ) * df["d-squared"].sum()
    st.latex(r"""\sigma_b""")
    st.text(sigma_b)
    
except Exception as e:
    print("Error4:", e)