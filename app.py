from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

# الاتصال بقاعدة البيانات
db = SQL("sqlite:///final.db")


@app.route("/")
def index():
    # جلب جميع العناصر من قاعدة البيانات مرتبة بالأحدث
    items = db.execute("SELECT * FROM items ORDER BY id DESC")
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    category = request.form.get("category")

    if task and category:
        db.execute(
            "INSERT INTO items (task, category) VALUES (?, ?)", task, category
        )

    return redirect("/")


@app.route("/toggle/<int:item_id>", methods=["POST"])
def toggle(item_id):
    # تبديل حالة الإنجاز (من 0 إلى 1 أو العكس)
    db.execute(
        "UPDATE items SET completed = CASE WHEN completed = 0 THEN 1 ELSE 0 END WHERE id = ?",
        item_id,
    )
    return redirect("/")


@app.route("/delete/<int:item_id>", methods=["POST"])
def delete(item_id):
    db.execute("DELETE FROM items WHERE id = ?", item_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
