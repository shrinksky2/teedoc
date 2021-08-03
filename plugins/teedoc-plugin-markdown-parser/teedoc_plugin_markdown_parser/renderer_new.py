import mistune
from .renderer import Block_Quote_Renderer, Header_Renderer
from .renderer_math import MathRendererMixin

plugins = [
    # "abbr",
    'strikethrough',
    'footnotes',
    'table',
    'url',
    'task_lists',
    'def_list',
]


class MDRenderer(
                 # HighlightMixin,
                 MathRendererMixin,
                #  TasklistRenderMixin,
                 Block_Quote_Renderer,
                 Header_Renderer,
                 mistune.Renderer):
    def __init__(self):
        mistune.Renderer.__init__(self, escape = False, hard_wrap = True)


