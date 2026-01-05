"""
Blueprint для обработки формы анкеты пользователя.
"""
from flask import Blueprint, render_template, request

bp = Blueprint('form', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index() -> str:
    """
    Главная страница с формой для ввода данных о пользователе.

    Returns:
        str: HTML-страница с формой или результатами.
    """
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        city = request.form.get('city', '').strip()
        hobby = request.form.get('hobby', '').strip()
        age = request.form.get('age', '').strip()

        return render_template(
            'form/index.html',
            submitted=True,
            name=name,
            city=city,
            hobby=hobby,
            age=age
        )

    return render_template('form/index.html', submitted=False)

