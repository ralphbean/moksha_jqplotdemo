import tw2.jqplugins.jqplot
import tw2.jqplugins.jqplot.base
from tw2.jqplugins.jqplot import PollingJQPlotWidget
from moksha.api.widgets.live import LiveWidget

class LiveJQPlotWidget(PollingJQPlotWidget, LiveWidget):
    """ A live plotting Widget, powered by Moksha & tw.jquery.JQPlot

    :topic: The topic stream to listen to
    :onmessage: Javascript that is called with new messages as they arrive
    """
    topic = None
    onmessage = "window._tw2_jqplots['${id}'](json)"


class plot_widget(LiveJQPlotWidget):
    topic = 'jqplot.demo.plot'
    resources = LiveJQPlotWidget.resources + [
        tw2.jqplugins.jqplot.base.dateAxisRenderer_js,
    ]


class pie_widget(LiveJQPlotWidget):
    topic = 'jqplot.demo.pie'
    resources = LiveJQPlotWidget.resources + [
        tw2.jqplugins.jqplot.base.pieRenderer_js,
    ]
    width = '300px'
    height = '300px'
