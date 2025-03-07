from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('Ver/Ocultar', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=0, max=10).bind_value(demo, 'number')
    ui.toggle({1: 'POO', 2: 'Algebra', 3: 'Contabilidad', 4: 'Probabilidad', 5:'Quimica'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()