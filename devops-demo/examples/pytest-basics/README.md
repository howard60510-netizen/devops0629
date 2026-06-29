# 範例 1：pytest 測純函式

DevOps 入門課 ch3〈Pytest〉的「範例 1：測一個純函式」。最單純的單元測試，不牽涉框架，直接測一個函式。

## 跑法

    cd examples/pytest-basics
    pip install pytest
    pytest

`main.py` 是被測的純函式 `check_machine(a, b)`；`test_check.py` 用 3A（Arrange / Act / Assert）測它。

想看失敗訊息長怎樣：把 `test_check.py` 裡的 `b` 改成 `2` 再跑一次，pytest 會直接告訴你第幾行、實際值對不上預期值。
