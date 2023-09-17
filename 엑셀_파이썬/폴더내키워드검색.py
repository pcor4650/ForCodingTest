# import os
# import pandas as pd

# def 폴더_내_키워드_확인(폴더경로, 키워드_리스트):
#     결과 = []

#     try:
#         for 파일명 in os.listdir(폴더경로):
#             파일경로 = os.path.join(폴더경로, 파일명)
#             if os.path.isfile(파일경로):
#                 try:
#                     with open(파일경로, 'r', encoding='utf-8') as 파일:
#                         내용 = 파일.read()
#                         결과_행 = []

#                         for 키워드 in 키워드_리스트:
#                             if 키워드 in 내용:
#                                 결과_행.append('O')
#                             else:
#                                 결과_행.append('X')

#                         결과.append([파일명] + 결과_행)
#                 except FileNotFoundError:
#                     print(f'파일을 찾을 수 없습니다: {파일경로}')
#     except FileNotFoundError:
#         print(f'폴더를 찾을 수 없습니다: {폴더경로}')

#     return 결과

# 폴더경로 = input('검사할 폴더 경로를 입력하세요: ')
# 키워드_열 = input('키워드가 나열된 열의 이름을 입력하세요: ')

# # 엑셀 파일을 불러와 키워드를 리스트로 추출
# try:
#     df = pd.read_excel(폴더경로, engine='openpyxl')
#     키워드_리스트 = df[키워드_열].tolist()
#     결과 = 폴더_내_키워드_확인(os.getcwd(), 키워드_리스트)

#     if 결과:
#         결과_프레임 = pd.DataFrame(결과, columns=['파일명'] + 키워드_리스트)
#         결과_프레임.to_excel('결과.xlsx', index=False)
#         print('결과가 "결과.xlsx" 파일로 저장되었습니다.')
#     else:
#         print('검사한 결과가 없습니다.')
# except FileNotFoundError:
#     print(f'파일을 찾을 수 없습니다: {폴더경로}')
# except KeyError:
#     print(f'"{키워드_열}" 열을 찾을 수 없습니다.')

# import os
# import chardet

# def 파일_인코딩_감지(파일경로):
#     with open(파일경로, 'rb') as 파일:
#         데이터 = 파일.read()
#         인코딩 = chardet.detect(데이터)
#     return 인코딩['encoding']

# def 폴더_내_키워드_확인(폴더경로, 키워드):
#     try:
#         for 파일명 in os.listdir(폴더경로):
#             파일경로 = os.path.join(폴더경로, 파일명)
#             if os.path.isfile(파일경로):
#                 try:
#                     인코딩 = 파일_인코딩_감지(파일경로)
#                     with open(파일경로, 'r', encoding=인코딩) as 파일:
#                         내용 = 파일.read()
#                         if 키워드 in 내용:
#                             print(f"'{파일명}' 파일에서 '{키워드}' 키워드가 발견되었습니다.")
#                 except FileNotFoundError:
#                     print(f'파일을 찾을 수 없습니다: {파일경로}')
#     except FileNotFoundError:
#         print(f'폴더를 찾을 수 없습니다: {폴더경로}')

# 폴더경로 = input('검사할 폴더 경로를 입력하세요: ')
# 키워드 = "import"

# 폴더_내_키워드_확인(폴더경로, 키워드)

# 맥에서 동작 OK
import os

def check_token_usage(directory_path, token):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".js"):  # 리액트 프로젝트라면 .js 또는 .jsx 파일을 대상으로 합니다.
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    if token in f.read():
                        print(f'Token "{token}" is used in {os.path.join(root, file)}')
                        return True
    print(f'Token "{token}" is not used.')
    return False

# 엑셀에서 토큰 리스트를 가져오는 부분은 별도로 구현해야 합니다.
# 이 예시에서는 단순히 하드코딩된 리스트를 사용합니다.
tokens = ['TOKEN1', 'TOKEN2', 'TOKEN3', '@CP_EPEP_A']  # 실제 토큰 리스트로 교체해야 합니다.

for token in tokens:
    check_token_usage('/Users/parkcha/Desktop/exex', token)  # 실제 디렉토리 경로로 교체해야 합니다.


# 아직 확인 안함
# import os

# def 토큰_사용_확인(폴더경로, 엑셀파일경로, 토큰열):
#     try:
#         # 엑셀 파일에서 토큰을 읽어옵니다.
#         import pandas as pd
#         df = pd.read_excel(엑셀파일경로, engine='openpyxl')
#         토큰_리스트 = df[토큰열].tolist()
#     except Exception as e:
#         print(f'엑셀 파일을 읽어오는 중 오류가 발생했습니다: {e}')
#         return

#     try:
#         for 루트, 디렉토리들, 파일들 in os.walk(폴더경로):
#             for 파일명 in 파일들:
#                 파일경로 = os.path.join(루트, 파일명)
#                 if os.path.isfile(파일경로):
#                     try:
#                         with open(파일경로, 'r', encoding='utf-8') as 파일:
#                             내용 = 파일.read()
#                             for 토큰 in 토큰_리스트:
#                                 if 토큰 in 내용:
#                                     print(f"'{파일명}' 파일에서 '{토큰}' 토큰이 사용되고 있습니다.")
#                     except Exception as e:
#                         print(f'파일을 읽어오는 중 오류가 발생했습니다: {e}')
#     except Exception as e:
#         print(f'폴더를 검사하는 중 오류가 발생했습니다: {e}')

# 폴더경로 = input('검사할 폴더 경로를 입력하세요: ')
# 엑셀파일경로 = input('엑셀 파일 경로를 입력하세요: ')
# 토큰열 = input('토큰이 있는 열의 이름을 입력하세요: ')

# 토큰_사용_확인(폴더경로, 엑셀파일경로, 토큰열)
