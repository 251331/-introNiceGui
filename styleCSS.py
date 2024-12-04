from nicegui import ui

ui.icon('thumb_up', color='#dc0ceb').classes('text-5xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Ashley').style('color: #dc0ceb; font-family: Courier New; font-size: 32px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()