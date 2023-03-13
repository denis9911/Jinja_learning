from jinja2 import Template
from markupsafe import escape

text = 'Лучшие читы по игре {{name}} находятся на сайте <a href="{{site}}">клик</a>'

games_dict = [{'game': 'ark', 'price': 165}, {'game': 'pubg', 'price': 135}, {'game': 'lol', 'price': 130},
              {'game': 'apex', 'price': 197}]

cheats_template = Template('Лучшие читы по игре {{name}} находятся на сайте <a href="{{site}}">клик</a>').render(
    name='ark', site='funpay.com')

raw_cheats_template = escape(cheats_template)  # экранирование символов - быстрее работает чем 2 вариант

raw_cheats_template2 = Template('{{text | e}}').render(text=cheats_template)  # 2 вариант экранирования

cheats_list = Template('''
<select name='games'>
{% for game in games -%}
{% if game['game'][0] == 'a' -%}
    <option>{{game['game']}}</option>
{% endif -%}
{% endfor -%}
</select>
''').render(games=games_dict)  # цикл for и if

price_sum = Template('''Суммарная стоимость читов: {{cheats | sum(attribute='price')}}''').render(cheats=games_dict)    # фильтр sum, аналогично работают и другие (min, max, sort...)

cheats_filter_by_title = Template('''
{%- for g in games -%}
{%- filter title -%}
{{g.game}}
{% endfilter -%}
{% endfor -%}
''').render(games=games_dict)

print(cheats_filter_by_title)
