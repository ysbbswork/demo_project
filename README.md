# Demo Echo Service

一个简单的回声服务，接收请求并返回相同的数据。

## 功能

- 提供一个echo API端点
- 支持JSON数据回显
- 提供基础的Web界面

## 使用方法

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行服务

```bash
python app.py
```

或者使用启动脚本:

```bash
./run.sh
```

### API 使用示例

启动服务后，可以使用以下命令测试：

```bash
# GET 请求获取服务信息
curl http://localhost:5000/echo

# POST 请求发送数据进行回显
curl -X POST -H "Content-Type: application/json" -d '{"message":"Hello World","timestamp":12345}' http://localhost:5000/echo
```
