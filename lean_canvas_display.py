from typing_extensions import TypedDict
from IPython.display import HTML, display

class LeanGraphState(TypedDict):
    # Local variables
    main_task: str  # Основная задача от пользователя
    competitors_analysis: str  # Анализ конкурентов
    feedback: str  # Фидбек от пользователя

    # Lean Canvas
    problem: str  # Проблема, которую пытается решить продукт или услуга.
    solution: str  # Краткое описание предлагаемого решения.
    key_metrics: str  # Ключевые показатели, которые необходимо измерять для отслеживания прогресса.
    unique_value_proposition: str  # Единое сообщение, объясняющее, почему ваш продукт уникален.
    unfair_advantage: str  # То, что конкуренты не могут легко скопировать или купить.
    channels: str  # Пути охвата ваших клиентских сегментов.
    customer_segments: str  # Целевая аудитория или группы людей, которых вы пытаетесь охватить.
    cost_structure: str  # Основные затраты, связанные с ведением бизнеса.
    revenue_streams: str  # Как бизнес будет зарабатывать деньги.


def show_lean_canvas(state: LeanGraphState) -> None:
    """Отрисовывает Lean Canvas в Jupyter-ноутбуке как HTML-сетку."""
    # --- CSS для сетки 5×2 + нижний ряд -----------------------------------
    css = """
    <style>
    .canvas {
        display: grid;
        grid-template-columns: 2fr 1fr 2fr 1fr 2fr;   /* ширины колонок */
        grid-template-rows: auto auto auto;           /* 2 ряда + низ   */
        gap: 8px;
        background: transparent;
        font-family: Arial, sans-serif;
    }
    .box {
        background:#e59a12;
        color:#fff;
        border:1px solid #fff;
        padding:12px 14px;
        line-height:1.3;
    }
    .title { font-weight:700; margin-bottom:6px; }
    /* раскладка по «ячейкам» */
    .problem           { grid-area: 1 / 1 / span 2 / span 1; }
    .solution          { grid-area: 1 / 2 / span 1 / span 1; }
    .key_metrics       { grid-area: 2 / 2 / span 1 / span 1; }
    .uvp               { grid-area: 1 / 3 / span 2 / span 1; }
    .unfair            { grid-area: 1 / 4 / span 1 / span 1; }
    .channels          { grid-area: 2 / 4 / span 1 / span 1; }
    .customer_segments { grid-area: 1 / 5 / span 2 / span 1; }
    .cost_structure    { grid-area: 3 / 1 / span 1 / span 3; }
    .revenue_streams   { grid-area: 3 / 4 / span 1 / span 2; }
    </style>
    """

    # --- HTML-разметка ------------------------------------------------------
    html = f"""
    {css}
    <h2 style="text-align:center;color:#08c;font-family:Arial;margin-top:4px;">
        {state['main_task']}
    </h2>

    <div class="canvas">

        <div class="box problem">
            <div class="title">2. Problem</div>
            {state['problem']}
        </div>

        <div class="box solution">
            <div class="title">4. Solution</div>
            {state['solution']}
        </div>

        <div class="box key_metrics">
            <div class="title">8. Key Metrics</div>
            {state['key_metrics']}
        </div>

        <div class="box uvp">
            <div class="title">3. Unique Value Proposition</div>
            {state['unique_value_proposition']}
        </div>

        <div class="box unfair">
            <div class="title">9. Unfair Advantage</div>
            {state['unfair_advantage']}
        </div>

        <div class="box channels">
            <div class="title">5. Channels</div>
            {state['channels']}
        </div>

        <div class="box customer_segments">
            <div class="title">1. Customer Segments</div>
            {state['customer_segments']}
        </div>

        <div class="box cost_structure">
            <div class="title">7. Cost Structure</div>
            {state['cost_structure']}
        </div>

        <div class="box revenue_streams">
            <div class="title">6. Revenue Streams</div>
            {state['revenue_streams']}
        </div>

    </div>
    """
    display(HTML(html))
