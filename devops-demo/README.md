# devops-demo

DevOps 入門課的範例 app —— 一個小 FastAPI 服務，貫穿整門課：
**Git 工作流 → pytest → GitHub Actions（CI）→ Docker → K8S → ArgoCD（GitOps）→ 部署策略**。

## Endpoints

| Method | Path | 說明 |
|--------|------|------|
| GET | `/` | 回 `{"service": "hello", "version": "..."}`（版本字串給部署/上線驗證用）|
| GET | `/health` | 回 `{"status": "ok"}`（K8S liveness/readiness）|
| POST | `/login` | email 非空檢查；空白回 `400 {"error": "email is required"}` |

## 本地跑起來

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload        # http://127.0.0.1:8000  （/docs 看 API）
```

## 跑測試

```bash
pytest -v                # 或 pytest --cov=app
```

> PR 截圖教材示範：這一行是用來展示 branch → PR → merge 流程的最小變更。
> 第二次示範：這一行是用來拍 Merge 與 Delete branch 畫面的。

## 用 Docker 跑

```bash
docker build -t hello .
docker run --rm -p 8000:8000 hello
```

## 結構

```
hello/
├── app/
│   ├── main.py          # FastAPI app（/、/health、掛上 login router）
│   └── login.py         # /login：email 非空檢查
├── tests/
│   └── test_main.py     # pytest（health / version / login）
├── requirements.txt
├── Dockerfile           # 非 root 跑（安全基線）
└── .github/workflows/
    └── ci.yml           # push / PR 自動跑 pytest
```

> 第三次示範：這一行是用來重拍教材截圖的。

Delete branch screenshot demo E
