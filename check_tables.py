from sqlalchemy import create_engine, inspect

#Подключение к базе данных
engine = create_engine('sqlite:///app.db')
inspector = inspect(engine)

# Получаем список всех таблиц
tables = inspector.get_table_names()

print("Созданные таблицы в базе данных:")
if tables:
    for table in tables:
        print(f"\nТаблица: {table}")
        columns = inspector.get_columns(table)
        for column in columns:
            print(f"   - {column['name']}: {column['type']}")
else:
    print("Таблицы не найдены!")

# Проверяем наличие базы данных
import os
if os.path.exists('app.db'):
    size = os.path.getsize('app.db')
    print(f"\nБаза данных app.db создана (размер: {size} байт)")
else:
    print("\nБаза данных не найдена!")