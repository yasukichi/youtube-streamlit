import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('ここは右カラム')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#option = st.text_input('あなたの趣味を教えてください。')
#condition = st.slider('あなたの今の調子は?', 0, 100, 50)

#'あなたの趣味は', option, 'です'
#'コンディション', condition
#if st.checkbox('Show Image'):
#    img = Image.open('sample.jpg')
#    st.image(img, caption='test', use_column_width=True)
