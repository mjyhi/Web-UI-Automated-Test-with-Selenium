# Web-UI-Automated-Test-with-Selenium

基于 **Python + Selenium + HtmlTestRunner** 的 Web UI 自动化测试框架，采用三层分离的 **PO（Page Object）模式**，用于对前端页面进行自动化回归。

## 技术栈
- Python 3
- Selenium 4
- unittest（测试框架）
- HtmlTestRunner（HTML 测试报告）

## 框架分层
1. **用例层（testcases）**
   - 编写具体测试场景
   - 包含断言与前置/后置处理
   - 每个用例自行断言
2. **PO 层（po/pages + po/business）**
   - `pages`：一个页面一个类，封装页面元素与操作
   - `business`：跨页面的业务流组合操作
3. **公共基类层（core + utils）**
   - Driver 工厂与 BasePage
   - BaseTest 统一管理 driver 生命周期
   - 配置加载、日志、异常、数据加载等工具

## 目录结构
```
ui_tests/
  .github/workflows/      CI 配置
  config/                配置文件
  core/                  驱动与基类封装
  po/
    pages/               Page Object 页面类
    business/            业务流封装
  testcases/             测试用例
  utils/                 工具类
  data/                  测试数据（CSV/JSON）
  logs/                  运行日志（自动生成）
  screenshots/           失败截图（自动生成）
  reports/               HTML报告（自动生成）
  run_tests.py            运行入口
  requirements.txt       依赖
```

## 当前测试内容
- 首页：Hero 标题与导航栏可见性
- 登录页：登录表单元素可见性
- 注册页：注册表单元素可见性
- 社区页：Hero 标题与“Create Post”按钮可见性
- 业务流：注册成功后退出并再次登录成功
- 业务流：注册后发帖成功
- 数据驱动：CSV 登录账号数据、JSON 注册/发帖数据

## 使用方法
### 1. 启动前端服务
默认配置为 `http://localhost:3000`

```
cd frontend
npm run dev
```

### 2. 安装依赖
```
python -m pip install -r ui_tests/requirements.txt
```

### 3. 执行测试并生成报告
```
python ui_tests/run_tests.py
```

运行完成后，HTML 报告输出在：`ui_tests/reports/`

## 测试数据驱动（CSV/JSON）
- JSON：`ui_tests/data/users.json`、`ui_tests/data/posts.json`
- CSV：`ui_tests/data/login_users.csv`

CSV 示例：
```
username,password,enabled
CHANGE_ME,CHANGE_ME,false
```

如需在本地/CI 中验证登录成功，请将 `CHANGE_ME` 替换为真实账号，或者使用环境变量注入（见下文）。

## 配置说明
配置文件：`ui_tests/config/config.ini`
- `base_url`：应用地址
- `browser`：支持 `chrome` / `firefox` / `edge`
- `headless`：是否无头运行
- `window_size`：浏览器窗口大小
- `timeouts`：隐式等待/页面加载/脚本超时时间

### 环境变量覆盖（推荐用于 CI）
- `UI_BASE_URL`：覆盖应用地址
- `UI_BROWSER`：覆盖浏览器
- `UI_HEADLESS`：覆盖无头模式
- `UI_WINDOW_SIZE`：覆盖窗口大小
- `UI_IMPLICIT_WAIT` / `UI_PAGE_LOAD` / `UI_SCRIPT_TIMEOUT`
- `UI_LOGIN_USERNAME` / `UI_LOGIN_PASSWORD`：登录账号（用于 CSV 登录用例）
- `UI_REQUIRE_SERVER`：为 `true` 时服务不可访问直接失败，否则跳过用例

## CI 自动执行
已提供 GitHub Actions 工作流，会自动运行用例并上传 HTML 报告：
- 文件：`.github/workflows/ui-tests.yml`
- 建议在仓库 Secret 中配置 `UI_BASE_URL`（指向可访问的部署环境）

## 说明
- Selenium 4.6+ 内置 Selenium Manager，可自动下载驱动。
- 若运行环境无自动下载能力，请手动安装对应浏览器驱动并加入 PATH。
