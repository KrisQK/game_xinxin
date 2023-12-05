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

# 嵌入 Bilibili 网站
st.header("快乐一下")
url = "https://www.bilibili.com"
iframe = f'<iframe src="{url}" width="100%" height="800" style="border:none;"></iframe>'
components.html(iframe)

# 其他个性化信息或功能可以在这里添加
