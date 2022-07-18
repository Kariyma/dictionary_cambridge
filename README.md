# Dictionary cambridge voicing
Получаем озвученное слово с сайта https://dictionary.cambridge.org/
## Requirements
* bs4
* googletrans
## Basic Idea
Получить аудио файл с озвученным английским словом с сайта https://dictionary.cambridge.org
Иметь возможность выбрать акцент озвучивания: Британский или Американский.
Иметь возможность вывести все значения слова с переводом.
## How To
1. Получаем аргументы
2. Создаём объект Слово
3. Ищем слово на сайте
4. Парсим страницу, заполняем свойства объекта
5. Печатаем результат, сохраняем файл
## Arguments
word - слова для поиска, обязательный
-p, --pronounce  - акцент, по умолчанию Британский (uk)
-m, -mor - получать ли дополнительную информацию: значение, перевод, по умолчанию False
## Example
#### python main.py dorm

/dɔːm/

Произношение слова dorm c акцентом UK загружено в файл dorm_uk.mp3

общежитие
####python main.py dorm -m

/dɔːm/
Произношение слова dorm c акцентом UK загружено в файл dorm_uk.mp3

a large room containing many beds, for example in a boarding school:
continue...

Большая комната, содержащая много кроватей, например, в школе -интернате:
continue...

a large building at a college or university where students live:
continue...

Большое здание в колледже или университете, где живут студенты:
continue...

общежитие