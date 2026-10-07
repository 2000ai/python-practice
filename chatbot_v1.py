import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 加载 .env 文件中的环境变量
load_dotenv()

# 2. 从环境变量中安全地读取API密钥
api_key = os.getenv("ZHIPU_API_KEY")
if not api_key:
    raise ValueError("未在 .env 文件中找到 ZHIPU_API_KEY，请检查配置。")

# 3. 初始化客户端，配置智谱的接口地址
client = OpenAI(
    api_key=api_key,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

def get_ai_response(user_input):
    """向智谱AI发送请求并获取回复"""
    try:
        response = client.chat.completions.create(
            model="glm-4-flash",  # 使用GLM-4-Flash模型，它速度快且对新手友好
            messages=[
                {"role": "system", "content": "你是一个乐于助人的AI助手，请用简洁清晰的中文回答。"},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,  # 控制回答的随机性，0.7是比较平衡的值
        )
        # 从复杂的响应结构中提取出AI的回复文本
        return response.choices[0].message.content
    except Exception as e:
        # 如果请求出错，返回一个友好的错误信息
        return f"抱歉，请求AI时出错了: {e}"

# 4. 主程序：创建一个循环，实现连续对话
def main():
    print("🤖 问答机器人 v1 已启动！输入 'quit' 或 '退出' 来结束对话。")
    while True:
        # 获取用户输入
        user_input = input("\n你: ")
        
        # 检查退出条件
        if user_input.lower() in ["quit", "exit", "退出"]:
            print("机器人: 再见！")
            break
        
        # 调用函数获取AI回复并打印
        print("机器人: ", end="")  # end="" 让打印不换行
        ai_reply = get_ai_response(user_input)
        print(ai_reply)

if __name__ == "__main__":
    main()