# Пример работы с агентами
Комплексный пример агентной системы. В ноутбуке демонстрируется создание
графового ReAct агента, который постепенно заполняет Lean Canvas и использует
поиск в интернете для анализа конкурентов.

## Свойства агента

- **Интернет-поиск.** Актуализирует данные о конкурентах через DuckDuckGo.
- **Структура графа.** Lean Canvas собирается по шагам с сохранением состояния.
- **Фидбек пользователя.** Возможность корректировать отдельные этапы генерации.
- **Вывод результата.** Готовый Lean Canvas отображается функцией
  `show_lean_canvas` из `lean_canvas_display.py`.

## Запуск

Для установки зависимостей выполните команду:

```bash
uv pip install -r pyproject.toml
```

После установки зависимостей, вы можете открыть и запустить `agents.ipynb` в среде Jupyter.

## Настройка окружения

Перед запуском убедитесь, что у вас настроены учетные данные для GigaChat:

1. Скопируйте файл `.env.example` в новый файл с именем `.env`.
2. В файле `.env` укажите ваши учетные данные для GigaChat.
