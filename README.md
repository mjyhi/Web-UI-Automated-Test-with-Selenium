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
  config/                配置文件
  core/                  驱动与基类封装
  po/
    pages/               Page Object 页面类
    business/            业务流封装
  testcases/             测试用例
  utils/                 工具类
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

## 配置说明
配置文件：`ui_tests/config/config.ini`
- `base_url`：应用地址
- `browser`：支持 `chrome` / `firefox` / `edge`
- `headless`：是否无头运行
- `window_size`：浏览器窗口大小
- `timeouts`：隐式等待/页面加载/脚本超时时间

## 说明
- Selenium 4.6+ 内置 Selenium Manager，可自动下载驱动。
- 若运行环境无自动下载能力，请手动安装对应浏览器驱动并加入 PATH。
