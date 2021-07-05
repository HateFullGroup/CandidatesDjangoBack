# Сервис отслеживания кандидатов на найм

## Модели бд

### Стандартный логин (админку Django)
* Только логин

### Таблица кандидитов
| Название        | Тип             | Комментарий |
| :-------------  | :-------------: | -------------: |
| Номер           | PrimaryKey      | =id? уточняется. Могут быть пропуски? - уточняется) |
| ФИО             | varchar(255)    | Not NULL |
| Дата рождения   | date            | Not NULL |
| Дата добавления | date            | дата добавления в бд |
| Описание        | varchar(255)    | Not NULL |
| Отзыв           | varchar(255)    | Not NULL |
| Место работы    | varchar(255)    | Not NULL |
| Зп              | varchar(255)    | возможно int |
| Должность       | varchar(255)    | Not NULL |


### Таблица Технологий
| Название        | Тип             | Комментарий    |
| :-------------  | :-------------: | -------------: |
| id              | PrimaryKey      | Not Null       |
| Название        | varchar(255)    | Not Null       |

### Таблица Связь
### Таблица Технологий
| Название        | Тип             | Комментарий    |
| :-------------  | :-------------: | -------------: |
| id              | PrimaryKey      | Not Null       |
| id Кандидата    | ForeignKey      | Not Null       |
| id Технологии   | ForeignKey      | Not Null       |
| id              | ForeignKey      | Not Null       |
| Уровень знания  | varchar(255)    | на текущий вариант решения от 1 до 5       |

