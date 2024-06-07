import time
# Redis 数据库
import redis
# 渲染模版：render_template
from flask import Flask, render_template, request
app = Flask(__name__)

# 启用调试模式
if __name__ == '__main__':
    app.run(debug=True)

# Redis作为应用缓存用于记录网站访问次数
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

# 用户访问根目录
@app.route("/")
def home():
    count = get_hit_count()
    # 传递变量给渲染模版：模版文件位于 code/templates/index.html
    return render_template("index.html",hits=count)
