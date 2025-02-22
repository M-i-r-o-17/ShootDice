# Shoot Dice
## _Игра взятая из Cult the Lamb и переведённая на ЯП python_

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Автор:+Владимир+Мирошниченко)](https://git.io/typing-svg)

Игра воссоздана по правилам кости из игры Cult the Lamb. Для запуска не GUI версии не нужны дополнительные
библеотеки и прочие файлы. Игра способна работать без всяких проблем напрямую.

## Правила игры

 Игровое поле состоит из двух игровых зон 3х3. В ход каждого игрока выпадает случайная кость от 1 до 6.
 Задача игрока заполнить всё поле костяшками. Общие количество очков выводиться рядом с полем. А количество
 каждого из столбцов выводиться прям над столбцом. После заполнения одной из зон, побеждает тот игрок, у 
 у которого больше всего очков. Особености хода:
  - Игроки ходят по очереди, первый игрок выбирается случайно
  - Если выложить кость и в противоположном столбце есть данные кости, то они "сгорают"
  - Еслм в столбце уже есть кость с данным номиналом то сумма столбца считается по следующим формулам:
    - x * 4 + y при двух одинаковых костях (x - одинаковые кости, y - оставшияся)
    - x * 9 при трёх одинаковых костях

  Простая таблица значений
| Выповшая кость | Кол-во костей в столбце | Кол-во костей в столбце  | Кол-во костей в столбце |
| :------------: | :---------------------: | :----------------------: | :---------------------: |
|  |  `1` |  `2` |  `3` |
| **1** |  1 |  4 |  9 | 
| **2** |  2 |  8 | 18 | 
| **3** |  3 | 12 | 27 | 
| **4** |  4 | 16 | 36 | 
| **5** |  5 | 20 | 45 | 
| **6** |  6 | 24 | 54 | 

## Связанные проекты

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=M-i-r-o-17&repo=GuiShootDice)](https://github.com/M-i-r-o-17/GuiShootDice)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

