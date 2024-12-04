from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz clic', on_click=lambda: ui.notify('Hiciste Clic'))
with ui.row():
    ui.checkbox('Acepto los terminos', on_change=show)
    ui.switch('Activado/Desactivado', on_change=show)
ui.radio(['Perro', 'Gato', 'Pez'], value='Gato', on_change=show).props('inline')
with ui.row():
    ui.input('Escribe tu nombre', on_change=show)
    ui.select(['ITICS', 'ICCS'], value='ITICS', on_change=show)
ui.link('para mas informacion...', '/documentacion').classes('mt-8')

ui.run()