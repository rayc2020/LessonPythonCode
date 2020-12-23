import numpy as np
import pickle
import streamlit as st

model_st = pickle.load(open('model.pkl', 'rb'))

def predict_salaryfromHR(工作经验,笔试,面试):
    int_features = [int(x) for x in [工作经验,笔试,面试]]
    final_features = [np.array(int_features)]
    prediction = model_st.predict(final_features)
    prediction = round(prediction[0], 2)
    return prediction

def main():
    st.title("人力资源评分系统")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">人力资源工资映射表 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    工作经验 = st.text_input("工作经验","Type Here")
    笔试 = st.text_input("笔试","输入")
    面试 = st.text_input("面试","输入")
    result=""
    if st.button("预测"):
        result=predict_salaryfromHR(工作经验,笔试,面试)
    st.success('员工工资标准： {}'.format(result))
    if st.button("关于"):
        st.text("Streamlit is so easy")
        st.text("Built from Raymond")

if __name__=='__main__':
    main()
