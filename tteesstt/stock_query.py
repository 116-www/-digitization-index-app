import streamlit as st
import pandas as pd
import numpy as np

def main():
    # 1. 标题与说明
    st.title("上市公司数字化转型指数查询系统")
    st.markdown("""
    - 技术方案：大数据文本挖掘 + AI 指数编制  
    - 数据来源：数字化转型词频统计结果（总）.xlsx  
    - 核心逻辑：词频加权计算转型指数
    """)

    # 2. 读取文本挖掘数据（Excel）
    file_path = r"C:\Users\31030\Desktop\tteesstt\数字化转型词频统计结果（总）.xlsx"
    try:
        df = pd.read_excel(file_path)
        st.success("文本数据挖掘成功！加载 {} 条企业记录".format(len(df)))
    except Exception as e:
        st.error(f"数据读取失败：{str(e)}")
        return

    # 3. 指数编制逻辑（大数据 + AI 简化版）
    # 假设：总词频数直接作为数字化转型指数
    # 实际可扩展：加权、NLP 情感分析、行业基准调整等
    df["转型指数"] = df["总词频数"]  # 基础版，可扩展 AI 模型
    
    # 4. APP 交互设计：股票代码查询
    stock_code = st.text_input("请输入股票代码（如 SZ000682）：")
    if stock_code:
        result = df[df["股票代码"] == stock_code]
        if not result.empty:
            st.subheader("查询结果")
            st.write(f"""
            - 企业名称：{result["企业名称"].values[0]}  
            - 数字化转型指数：{result["转型指数"].values[0]}  
            - 核心词频：人工智能 {result["人工智能技术"].values[0]} | 大数据 {result["大数据技术"].values[0]}
            """)
        else:
            st.warning("未找到该股票代码，请检查输入格式")

    # 5. 数据看板（大数据可视化）
    st.subheader("行业数据看板")
    st.bar_chart(df, x="企业名称", y="转型指数", height=400)
    st.write("指数分布统计：", df["转型指数"].describe())

if __name__ == "__main__":
    main()