from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from typing import Dict, Tuple, List
from .dataset import Dataset
from .point import Point

plt.style.use('ggplot')
for param in ['axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] ='#f6e6ff'
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '#312e33'

class Plotter:
    POSITIVE_POINT_STYLE = 'cs'
    NEGATIVE_POINT_STYLE = 'ms'
    UNCLASSIFIED_POINT_STYLE = 'ys'
    ADDITIONAL_POINTS_STYLE = 'bs'
    REMARKED_POINT_STYLE = 'orange' 

    def __init__(self, grid_rows: int, grid_columns: int, plot_size: Tuple[int, int] = (2, 2)):
        fig, axes = plt.subplots(grid_rows, grid_columns, figsize=(plot_size[0] * grid_columns, plot_size[1] * grid_rows))
        self.fig: Figure = fig
        self.axes: List[List[Axes]] = axes
        if grid_rows == 1 and grid_columns == 1:
            self.axes = [[self.axes]]
        elif grid_rows == 1 or grid_columns == 1:
            self.axes = [self.axes]
        self.grid_rows = grid_rows
        self.grid_columns = grid_columns
        self.datasets:List[List[Dataset]] = [[None for _ in range(grid_columns)] for _ in range(grid_rows)]
        self.points_legends: Dict[str, any] = {}
        self.lines_legends: Dict[str, any] = {}

    def plot_dataset(self, dataset: Dataset, sub_plot: Tuple[int, int]) -> None:
        self.datasets[sub_plot[0]][sub_plot[1]] = dataset
        ax = self.axes[sub_plot[0]][sub_plot[1]]
        
        for point in dataset.points:
            if point.category == Point.Category.POSITIVE:
                ax.plot(point.x[0], point.x[1],self.POSITIVE_POINT_STYLE)
                self.add_point_legend('clase +1', self.POSITIVE_POINT_STYLE)
            elif point.category == Point.Category.NEGATIVE:
                ax.plot(point.x[0], point.x[1], self.NEGATIVE_POINT_STYLE)
                self.add_point_legend('clase -1', self.NEGATIVE_POINT_STYLE)
            else:
                ax.plot(point.x[0], point.x[1], self.UNCLASSIFIED_POINT_STYLE)
                self.add_point_legend('no clasificado', self.UNCLASSIFIED_POINT_STYLE)
        
    def plot_additional_points(self, points: List[Point], sub_plot: Tuple[int, int], label: str=None) -> None:
        ax = self.axes[sub_plot[0]][sub_plot[1]]
        for point in points:
            ax.plot(point.x[0], point.x[1], self.ADDITIONAL_POINTS_STYLE)
        if label is not None:
            self.add_point_legend(label, self.ADDITIONAL_POINTS_STYLE)

    def plot_line(self, p0: Tuple[float], p1: Tuple[float], sub_plot: Tuple[int, int], line_style:str = '-', line_color:str = 'black', label:str = None) -> None:
        ax = self.axes[sub_plot[0]][sub_plot[1]]
        ax.axline((p0[0], p0[1]), (p1[0], p1[1]), linestyle=line_style, color=line_color)
        if label is not None:
            self.add_line_legend(label, line_color, line_style)

    def plot_segment(self, p0:Tuple[float], p1:Tuple[float], sub_plot: Tuple[int, int], line_style:str, line_color:str, label:str=None) -> None:
        ax = self.axes[sub_plot[0]][sub_plot[1]]
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], linestyle=line_style, color=line_color)
        if label is not None:
            self.add_line_legend(label, line_color, line_style)

    def remark_point(self, point:Tuple[float,float], sub_plot: Tuple[int, int], label:str=None) -> None:
        ax = self.axes[sub_plot[0]][sub_plot[1]]

        if self.datasets[sub_plot[0]][sub_plot[1]] is None:
            raise ValueError(f"Dataset not plotted in the given subplot {sub_plot}")

        point = self.datasets[sub_plot[0]][sub_plot[1]].get_point_at(point)
        
        if point is None:
            raise ValueError(f"Point ({point}) not found in subplot {sub_plot} dataset")
        
        
        ax.plot(point.x[0], point.x[1], 'o', markersize=12, markeredgecolor=self.REMARKED_POINT_STYLE, markerfacecolor='None', markeredgewidth=1.5)
        if label is not None:
            self.add_point_legend(label, self.REMARKED_POINT_STYLE)

    def set_title(self, title:str, sub_plot: Tuple[int, int] = (0, 0)):
        ax = self.axes[sub_plot[0]][sub_plot[1]]
        ax.set_title(title)
    
    def add_text_box_to_figure(self, text:str):
        """
        Add text above the subplots in current figure
        """   
        self.fig.text(0.5, 0.9, text, ha='center', va='center', fontsize=10)
    
    def add_text_box_to_subplot(self, text:str, sub_plot: Tuple[int, int]):
        """
        Add text below the subplot
        """
        ax = self.axes[sub_plot[0]][sub_plot[1]]        
        ax.text(0.5, -0.6, text, va='bottom', ha='center', fontsize=8, transform=ax.transAxes)

    def set_limits(self, x_min:float, x_max:float, y_min:float, y_max:float, sub_plot: Tuple[int, int]):
        if sub_plot is None:
            for i in range(self.grid_rows):
                for j in range(self.grid_columns):
                    ax = self.axes[i][j]
                    ax.set_xlim(x_min, x_max)
                    ax.set_ylim(y_min, y_max)
        else:
            ax = self.axes[sub_plot[0]][sub_plot[1]]
            ax.set_xlim(x_min, x_max)
            ax.set_ylim(y_min, y_max)

    def set_1_1_aspect_ratio(self, sub_plot: Tuple[int, int]):
        ax = self.axes[sub_plot[0]][sub_plot[1]]
        ax.set_aspect('equal', adjustable='box')
    
    def add_point_legend(self, label:str, style:str):
        self.points_legends[label] = style
    
    def add_line_legend(self, label:str, color:str, style:str):
        self.lines_legends[label] = (color, style)
            
    def show(self) -> None:
        for i in range(self.grid_rows):
            for j in range(self.grid_columns):
                ax = self.axes[i][j]

                ax.figure.set_figheight(2)
                
                # Ticks each 1
                ax.set_xticks(range(int(ax.get_xlim()[0]), int(ax.get_xlim()[1])+1))


        # Add legend
        for label, style in self.points_legends.items():
            (plt.plot([], [], style, markersize=10, label=label))
        for label, (color, style) in self.lines_legends.items():
            (plt.plot([], [], linestyle=style, color=color, label=label))
        
        # show legend below the subplots
        self.fig.legend(fancybox=True, shadow=True, loc='lower center', ncol=5)

        mng = plt.get_current_fig_manager()
        mng.resize(1280*.9, 720*.8)
        self.fig.tight_layout()
        plt.show()