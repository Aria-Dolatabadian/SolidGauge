import pygal
gauge = pygal.SolidGauge(inner_radius=0.70)
percent_formatter = lambda x: '{:.10g}%'.format(x)
dollar_formatter = lambda x: '{:.10g}$'.format(x)
gauge.value_formatter = percent_formatter

gauge.add('Series 1', [{'value': 225000, 'max_value': 1275000}],
          formatter=dollar_formatter)
gauge.add('Series 2', [{'value': 150, 'max_value': 100}])
gauge.add('Series 3', [{'value': 3, 'max_value': 100}])
gauge.add('Series 4', [{'value': 51, 'max_value': 100}])
gauge.add('Series 5', [{'value': 79, 'max_value': 100}])
gauge.add('Series 6', [{'value': 99, 'max_value': 100}])
gauge.add('Series 7', [{'value': 75, 'max_value': 100}])
gauge.add('Series 8', [{'value': 30, 'max_value': 100}])
gauge.add('Series 9', [{'value': 40, 'max_value': 100}])
gauge.render()
gauge.render_to_file('gauge.svg')
