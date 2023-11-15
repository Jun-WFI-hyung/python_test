import logging
# Werkzeug 로거 가져오기
werkzeug_logger = logging.getLogger('werkzeug')
# 기본 로그 레벨을 INFO에서 WARNING으로 변경
werkzeug_logger.setLevel(logging.WARNING)
