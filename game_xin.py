import random
import streamlit as st
import streamlit.components.v1 as components

# 页面设置
st.set_page_config(page_title="芯芯的决策助手", page_icon=":tada:", layout="wide")

# 添加标题和欢迎信息
st.title("欢迎来到芯芯的决策助手--狗狗")
st.subheader("让我们一起做出选择吧！")

# 决策助手部分
st.header("决策助狗")
options = st.text_area("输入你的选项，每行一个")
if st.button("帮我决定"):
    choices = options.split("\n")
    choice = random.choice(choices)
    st.success(f"芯芯，你应该选择：{choice}")



# 其他个性化信息或功能可以在这里添加
import streamlit as st

# 创建侧边栏
st.sidebar.title("简易计算器")

# 计算器输入
num1 = st.sidebar.number_input("输入第一个数", value=0.0)
num2 = st.sidebar.number_input("输入第二个数", value=0.0)
operation = st.sidebar.selectbox("选择运算符", ["+", "-", "*", "/"])

# 计算结果
if st.sidebar.button("计算"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "除数不能为零"
    
    st.sidebar.write("结果:", result)
