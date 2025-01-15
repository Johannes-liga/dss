import streamlit as st
import requests

st.title("Gemini API와 PDF 파일 업로드")

api_key = st.text_input("API Key를 입력하세요", type="password")
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")

if uploaded_file is not None and api_key:
    st.write("PDF 파일이 업로드되었습니다.")
    
    pdf_content = uploaded_file.read()
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/pdf"
    }
    
    try:
        response = requests.post("https://api.gemini.com/v1/transactions", headers=headers, data=pdf_content)
        
        if response.status_code == 200:
            st.write("Gemini API와의 통신 성공!")
            st.write(response.json())
        else:
            st.write("Gemini API와의 통신 실패!")
            st.write(f"Status Code: {response.status_code}")
            st.write(f"Response Text: {response.text}")
    except requests.exceptions.RequestException as e:
        st.write("요청 중 오류 발생!")
        st.write(e)

# 추가적인 기능이나 결과를 여기에 추가

