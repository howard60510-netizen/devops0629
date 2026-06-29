# 讓 pytest 把 repo 根目錄加入 import 路徑，這樣 `from app.main import app` 找得到。
# （pytest 會把含 conftest.py 的目錄加進 sys.path）
