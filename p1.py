from src import Point, Dataset, Plotter
from typing import List, Tuple

# instantiate the dataset
# negatives = {(4, 6),(2, 1),(3, 5),(0, 3),(4, 3)}
# positives = {(6, 0),(7, 5),(6, 3),(9, 2),(7, 1)}
dataset = Dataset.from_raw([(6, 0),(7, 5),(6, 3),(9, 2),(7, 1)], [(4, 6),(2, 1),(3, 5),(0, 3),(4, 3)])

'------------------------'

# instantiate plot object
plotter = Plotter(1, 4)
wrong_support_vectors_dataset = Dataset.from_raw([(7,5),(6, 3)],[(4, 3)])

# plot the dataset
subplot = (0, 0)
plotter.set_title("Puntos", subplot)
plotter.plot_dataset(dataset, subplot)

# plot the support vectors
subplot = (0, 1)
plotter.set_title("Support vectors\nincorrectos", subplot)
plotter.plot_dataset(dataset, subplot)
plotter.remark_point((7, 5), subplot)
plotter.remark_point((6, 3), subplot)
plotter.remark_point((4, 3), subplot, label='support vector')

# plot the decision boundary
subplot = (0, 2)
plotter.set_title("Márgenes y frontera de decisión\nincorrectos", subplot)
plotter.plot_dataset(wrong_support_vectors_dataset, subplot)
plotter.remark_point((7, 5), subplot)
plotter.remark_point((6, 3), subplot)
plotter.remark_point((4, 3), subplot, label='support vector')
# change list to tuples
plotter.plot_line((6, 3), (7,5), subplot, line_style='--')
plotter.plot_line((4, 3), (5, 5), subplot, line_style='--', label='márgenes')
plotter.plot_line((5, 3), (6, 5), subplot, line_style='-', label='frontera de decisión')

# Plot the distance between margins
subplot = (0, 3)
plotter.set_title("Distancia entre márgenes", subplot)
plotter.plot_dataset(wrong_support_vectors_dataset, subplot)
plotter.remark_point((7, 5), subplot)
plotter.remark_point((6, 3), subplot)
plotter.remark_point((4, 3), subplot, label='support vector')
plotter.plot_line((6, 3), (7,5), subplot, line_style='--')
plotter.plot_line((4, 3), (5, 5), subplot, line_style='--', label='márgenes')
plotter.plot_line((5, 3), (6, 5), subplot, line_style='-', label='frontera de decisión')
plotter.plot_segment((4,3), (5.6, 2.2), subplot, line_style='-', line_color='green')
plotter.plot_segment((5.6, 2.2),(6,3), subplot, line_style='-', line_color='red')
plotter.plot_segment((4,3), (6,3), subplot, line_style='-', line_color='blue')
plotter.set_1_1_aspect_ratio(subplot)

plotter.set_limits(-1, 10, -1, 7, (0,0))
plotter.set_limits(-1, 10, -1, 7, (0,1))
plotter.set_limits(-1, 10, -1, 7, (0,2))
plotter.set_limits( 3,  8,  1, 6, (0,3))
text = "En este caso el ancho del margen es menor que en la imagen siguiente\n\n"
text +="Notar que el segmento verde es perpendicular a la recta margen, es el ancho de margen\n"
text +="y es menor al segmento azul. En general, el máximo ancho de margen para los puntos\n"
text += "(4,3) y(6,3) los más cercanos de distinta clase, corresponse a márgenes verticales"
plotter.add_text_box_to_figure(text)
plotter.show()

'----------------------------------'

plotter = Plotter(1,3, (3, 3))
support_vectors_dataset = Dataset.from_raw([(6, 0),(6, 3)],[(4, 3),(4, 6)])

# plot the dataset
subplot = (0, 0)
plotter.set_title("Puntos", subplot)
plotter.plot_dataset(dataset, subplot)

# plot the support vectors
subplot = (0, 1)
plotter.set_title("Support vectors\ncorrectos", subplot)
plotter.plot_dataset(dataset, subplot)
plotter.remark_point((6, 0), subplot)
plotter.remark_point((6, 3), subplot)
plotter.remark_point((4, 3), subplot)
plotter.remark_point((4, 6), subplot, label='support vector')

# plot the decision boundary
subplot = (0, 2)
plotter.set_title("Márgenes y frontera de decisión\ncorrectos", subplot)
plotter.plot_dataset(support_vectors_dataset, subplot)
plotter.remark_point((6, 0), subplot)
plotter.remark_point((6, 3), subplot)
plotter.remark_point((4, 3), subplot)
plotter.remark_point((4, 6), subplot, label='support vector')
plotter.plot_line((6, 0), (6, 3), subplot, line_style='--')
plotter.plot_line((4, 3), (4, 6), subplot, line_style='--', label='márgenes')
plotter.plot_line((5, 3), (5, 5), subplot, line_style='-', label='frontera de decisión')

plotter.add_text_box_to_figure("Considerando lo anterior, los márgenes quedan\nde la siguiente forma")
plotter.set_limits(-1, 10, -1, 7, None)
plotter.show()

'----------------------------------'

plotter = Plotter(1, 3, (3, 3))

# plot the decision boundary
subplot = (0, 0)
plotter.set_title("Márgenes y frontera de decisión\n entrenado", subplot)
plotter.plot_dataset(support_vectors_dataset, subplot)
plotter.remark_point((6, 0), subplot)
plotter.remark_point((6, 3), subplot)
plotter.remark_point((4, 3), subplot)
plotter.remark_point((4, 6), subplot, label='support vector')
plotter.plot_line((6, 0), (6, 3), subplot, line_style='--')
plotter.plot_line((4, 3), (4, 6), subplot, line_style='--', label='márgenes')
plotter.plot_line((5, 3), (5, 5), subplot, line_style='-', label='frontera de decisión')


# plot new points
subplot = (0, 1)
plotter.set_title("Puntos adicionales", subplot)
new_points_dataset = Dataset.from_raw([],[],[(2, 3),(5, 5),(0, 0),(6, 0)])
plotter.plot_dataset(new_points_dataset, subplot)
plotter.plot_line((6, 0), (6, 3), subplot, line_style='--')
plotter.plot_line((4, 3), (4, 6), subplot, line_style='--', label='márgenes')
plotter.plot_line((5, 3), (5, 5), subplot, line_style='-', label='frontera de decisión')

# Classify new points
subplot = (0, 2)
plotter.set_title("Clasificación de puntos adicionales", subplot)
new_points_dataset = Dataset.from_raw([(6,0)],[(2, 3),(0, 0)],[(5, 5)])
plotter.plot_line((6, 0), (6, 3), subplot, line_style='--')
plotter.plot_line((4, 3), (4, 6), subplot, line_style='--', label='márgenes')
plotter.plot_line((5, 3), (5, 5), subplot, line_style='-', label='frontera de decisión')
plotter.plot_dataset(new_points_dataset, subplot)

plotter.add_text_box_to_figure( "Finalmente los puntos quedan clasificados como:\n"+
                                "(0,1): clase -1\n"+
                                "(2,3): clase -1\n"+
                                "(5,5): sin clasificar, queda en la frontera de decisión\n"+
                                "(6,0): clase +1, como queda en el margen de decisión corresponde a esa clase, de ser\n"+
                                "reentrenado el modelo sería un support vector, pero en este momento sólo se clasifica"
                               )
plotter.set_limits(-1, 10, -1, 7, None)

plotter.show()

