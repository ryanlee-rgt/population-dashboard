#앱으로 실행해보기 위해 사용했던 streamlit 라이브러리이다.
import streamlit as st
import pandas as pd
import numpy as np

#mysql 라이브러리 import이다.
import mysql.connector
from mysql.connector import Error 


primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"

#메인함수이다.
def main():
	#트라이캐치문을 사용했다.
    try :
        # book_id_list 변수를 초기화합니다.
        book_id_list = []  # 추가된 부분

        #커넥션을 가져온다. 원래는 이 부분 코드를 모두가 볼 수 있는 곳에 삽입하면 안된다.
        connection = mysql.connector.connect(
            host = 'localhost', #데이터베이스의 endpoint가 필요하다. 밑에서 이미지와 관련 링크를 첨부할 것이다.
            database = 'mydb', #작업할 schema의 이름을 써준다.
            user = 'WBEarly', #위에서 등록한 계정의 username을 써준다.
            password = '#woobosys@early!' #위에서 등록한 계정의 password를 써준다.
        )

		#커넥션을 제대로 가져왔을 경우 이 부분이 실행된다.
        if connection.is_connected() :
        
        	#커서를 가져온다.
            cursor = connection.cursor(dictionary= True)
            
            #실행할 쿼리문을 작성하면,
            query = """ select *
                        from myrecords limit 5; """
                        
            #이 부분에서 쿼리를 실행해준다.
            cursor.execute(query)
            
            #쿼리 실행의 결과를 가져와, results라는 변수에 저장한 것이다.
            results = cursor.fetchall()

			#이 부분은 스트림릿 앱 화면에 보여주기 위해 작성된 부분이다.
            for row in results :
                st.write(row)
                # row['id']가 정수형이므로, 올바른 키를 사용하여 값을 가져옵니다.
                book_id_list.append({'id': row['id'], 'name': row['name'], 'email': row['email']})

            df = pd.DataFrame(data=book_id_list)
            st.write(df)
            st.dataframe(df)
            st.table(df)

	#DB 관련 에러가 발생할 시, 터미널에 에러 문구를 출력하게 했다.
    except Error as e :
            print('디비 관련 에러 발생', e)
    
    #마지막엔 커서와 커넥션을 닫아준다.
    #닫아주지 않을 경우 뒤에서 또 커서와 커넥션을 사용하게 됐을 때 제대로 작동하지 않을 수 있다.
    finally :
        cursor.close()
        connection.close()
        print("------ Mysql example Go ----------")

##################################
st.header('라인 차트')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
##################################
st.header('st.checkbox')

st.write ('주문하고 싶은 것이 무엇인가요?')

icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')

if icecream:
     st.write("좋아요! 여기 더 많은 🍦")

if coffee: 
     st.write("알겠습니다, 여기 커피 있어요 ☕")

if cola:
     st.write("여기 있어요 🥤")
##################################

tab1, tab2, tab3, tab4= st.tabs(['신규사업','소하천','저수지','채팅'])

with tab1:
    st.header('Tab1')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with tab2:
    st.header('Tab2')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab3:
    st.header('Tab3')
    st.image('https://static.streamlit.io/examples/owl.jpg')

with tab4:
    st.header('Tab4')
    st.image('https://cdn.pixabay.com/photo/2023/10/19/21/08/ai-generated-8327632_1280.jpg')


with st.expander('examle1'):
    st.write('1111')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with st.expander('examle2'):
    st.write('2222')
    st.image('https://static.streamlit.io/examples/owl.jpg')

col1, col2, col3, col4 = st.columns([3,3,3,6])

with col1:
    st.header('col1')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2:
    st.header('col2')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header('col3')
    st.image('https://static.streamlit.io/examples/owl.jpg')

with col4:
    st.header('col4')
    st.image('https://cdn.pixabay.com/photo/2023/10/19/21/08/ai-generated-8327632_1280.jpg')

with st.sidebar:
    st.title('타이틀 - 대')
    st.header('타이틀 - 중')
    st.subheader('타이틀 - 소')



x=st.sidebar.selectbox('---',['신규사업','소하천','저수지','채팅'])

st.metric(label='우보재난시스템', value='70000', delta='2.3%')

if __name__ == '__main__':
    main()