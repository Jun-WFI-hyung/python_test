import traceback

def current_line_number():
    stack = traceback.extract_stack()
    filename, line_number, a, b = stack[-2]  # 현재 함수를 호출한 위치의 정보를 가져옴
    print(f"현재 파일: {filename}, 현재 줄: {line_number}", a, b)

# 예시 함수
def example_function():
    current_line_number()
    # 추가 작업 수행
    pass

# 예시 함수 호출
example_function()
