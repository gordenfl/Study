import redis
from datetime import datetime, timedelta

r = redis.Redis()

def get_last_7_days():
    today = datetime.utcnow().date()
    return [(today - timedelta(days=i)).strftime('%Y%m%d') for i in range(7)]

def update_play(user_id, song_id):
    today = datetime.utcnow().strftime('%Y%m%d')
    # 用户当天播放记录
    r.zincrby(f"user:top_songs:{today}:{user_id}", 1, song_id)
    # 全站播放计数
    r.zincrby("global:top_songs", 1, song_id)

def merge_user_last7days(user_id):
    keys = [f"user:top_songs:{day}:{user_id}" for day in get_last_7_days()]
    temp_key = f"user:top_songs:last7d:{user_id}"
    r.zunionstore(temp_key, keys)
    r.expire(temp_key, 300)  # 设置5分钟缓存，避免长期占用内存
    return temp_key

def get_song_meta(song_id):
    return r.hgetall(f"song:meta:{song_id}")

def show_user_top10(user_id):
    print(f"🎧 用户 {user_id} 最近 7 天最爱听的歌曲：\n")

    merged_key = merge_user_last7days(user_id)
    top10 = r.zrevrange(merged_key, 0, 9, withscores=False)

    for i, song_id in enumerate(top10, 1):
        global_count = int(r.zscore("global:top_songs", song_id) or 0)
        meta = get_song_meta(song_id)
        title = meta.get(b'title', b'Unknown').decode()
        artist = meta.get(b'artist', b'Unknown').decode()
        print(f"{i}. {title} - {artist}（全站被听 {global_count} 次）")

# 示例初始化数据（运行一次即可）
def seed_example_data():
    r.hset("song:meta:song123", mapping={"title": "Let It Be", "artist": "The Beatles"})
    r.hset("song:meta:song456", mapping={"title": "Bohemian Rhapsody", "artist": "Queen"})
    r.hset("song:meta:song789", mapping={"title": "Imagine", "artist": "John Lennon"})

    # 模拟某人听了几天
    for i in range(7):
        day = (datetime.utcnow().date() - timedelta(days=i)).strftime('%Y%m%d')
        r.zincrby(f"user:top_songs:{day}:user123", 1+i, "song123")
        r.zincrby(f"user:top_songs:{day}:user123", 3+i, "song456")
        r.zincrby(f"user:top_songs:{day}:user123", 2+i, "song789")

        r.zincrby("global:top_songs", 10+i, "song123")
        r.zincrby("global:top_songs", 20+i, "song456")
        r.zincrby("global:top_songs", 30+i, "song789")

# 示例运行
if __name__ == "__main__":
    seed_example_data()
    show_user_top10("user123")
