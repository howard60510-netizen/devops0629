# devops-config — GitOps 設定 repo

這是 DevOps 入門課的 **Config Repo**（搭配 App Repo [`devops-demo`](https://github.com/4-learn/devops-demo)）。

> GitOps 的核心：**app 的程式碼**放 `devops-demo`，**部署用的 K8S 設定**放這裡。ArgoCD 只盯這個 repo，repo 變了就自動部署。

## 結構

| 資料夾 | 內容 | 對應章節 |
|--------|------|----------|
| `k8s/` | 主部署：`deployment.yaml` + `service.yaml`（ArgoCD 預設盯這裡） | ch5 ArgoCD、ch6 串接 |
| `argocd/` | ArgoCD `Application`（指向 `k8s/`） | ch5、ch8 |
| `blue-green/` | 藍綠部署範例（blue/green 兩份 Deployment + 切換用 Service） | ch7 部署策略 |
| `canary/` | 金絲雀部署範例（main + canary ingress，用 weight 分流） | ch7 部署策略 |

## image 從哪來

`devops-demo` 的 CI 會把 image build 後推到 **GHCR**：`ghcr.io/4-learn/devops-demo:<commit-sha>`，
並自動回來改 `k8s/deployment.yaml` 的 image tag（見 ch6）。
