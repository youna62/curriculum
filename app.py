import streamlit as st
import pandas as pd

# 파일 읽기
curri = pd.read_csv("수학과 교육과정 정리 - 교육과정합본.csv")

# 타이틀 설정
st.title("교육과정 찾기")

# 검색 필터 추가
revision_options = curri['개정일시'].dropna().unique().tolist()
level_options = curri['학교급'].dropna().unique().tolist()
area_options = curri['영역'].dropna().unique().tolist()
subject_options = curri['과목'].dropna().unique().tolist()

selected_revisions = st.multiselect("개정 일시 선택", revision_options)
selected_levels = st.multiselect("학교급 선택", level_options)
selected_areas = st.multiselect("영역 선택", area_options)
selected_subjects = st.multiselect("과목 선택", subject_options)


# 키워드 검색 필드 강조
st.markdown("## **키워드 검색**")
keyword = st.text_input("키워드 검색", placeholder="검색할 키워드를 입력하세요...", key="keyword_input", max_chars=50)

# 필터 적용
filtered_curri = curri
if selected_revisions:
    filtered_curri = filtered_curri[filtered_curri['개정일시'].isin(selected_revisions)]
if selected_levels:
    filtered_curri = filtered_curri[filtered_curri['학교급'].isin(selected_levels)]
if selected_areas:
    filtered_curri = filtered_curri[filtered_curri['영역'].isin(selected_areas)]
if selected_subjects:
    filtered_curri = filtered_curri[filtered_curri['과목'].isin(selected_subjects)]
if keyword:
    filtered_curri = filtered_curri[filtered_curri.apply(lambda row: row.astype(str).str.contains(keyword).any(), axis=1)]

# 데이터프레임 출력
st.dataframe(filtered_curri)

# 메시지 출력
if filtered_curri.empty:
    st.write("조건에 맞는 교육과정이 없습니다.")
else:
    st.write(f"총 {len(filtered_curri)}개의 교육과정이 검색되었습니다.")