# 모듈 동적 불러오기

import importlib.util
from typing import Any

def dynamicImport(module_name: str) -> Any:
    try:
        # 모듈 파일의 경로 설정
        module_path = f"./{module_name}.py"
        # 모듈 스펙 생성
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        # 모듈 로드
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error while importing module '{module_name}': {e}")
        return None

# 동적으로 임포트할 모듈의 파일 이름
module_name = "custom_module"
# 모듈 임포트
custom_module = dynamicImport(module_name)

custom_module.testFunc()