from flask import Flask, request, render_template
from database import init_db, save_visit

app = Flask(__name__)

init_db()


def get_real_ip():
    forwarded = request.headers.get("X-Forwarded-For")

    if forwarded:
        return forwarded.split(",")[0].strip()

    return request.remote_addr


@app.route("/")
def index():

    ip = get_real_ip()

    telegram_id = request.args.get(
        "telegram_id",
        default=None,
        type=int
    )

    user_agent = request.headers.get(
        "User-Agent",
        ""
    )

    save_visit(
        telegram_id=telegram_id,
        ip=ip,
        user_agent=user_agent
    )

    return render_template(
        "index.html",
        ip=ip
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
