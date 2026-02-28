import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class MultiPlotter9000:
    def __init__(self):
        self.palette1 = sns.color_palette('bright')
        self.palette2 = sns.color_palette('rainbow')
        self.palette = self.palette1+self.palette2
        sns.set_palette(self.palette)
        sns.set_theme(style='darkgrid')

    def multiplot_histogram(self, data, columns, hue_val):
        sns.set(rc={'figure.figsize':(40,25)})
        sns.set_palette("bright")
        k=1
        for column in columns:
            bins  = 15
            plt.subplot(3,3,k)
            if column == 'MonthlyIncome': discrete_value = False
            else: discrete_value = True
            sns.histplot(data=data, x=column, bins=bins, kde=False, hue=hue_val, palette={0: sns.color_palette()[k-7], 1: sns.color_palette()[k-8]}, discrete=discrete_value)
            plt.title(f'{column} Distribution')
            plt.xlabel(f'{column}')
            k+=1
        plt.tight_layout()
        plt.show()

    def multiplot_boxplot(self, data, columns):
        sns.set(rc={'figure.figsize':(20,17)})
        sns.set_palette("bright")
        k=1
        for column in columns:
            plt.subplot(4,4,k)
            sns.boxplot(data=data[column], color=sns.color_palette()[k])
            plt.title(f'{column} Boxplot')
            k+=1

        plt.tight_layout()
        plt.show()

    def multiplot_violin(self,data,columns, **kwargs):
        cluster = kwargs.get('cluster', False)
        pop_data = kwargs.get('pop_data', 0)
        sns.set_palette("bright")
        k=1
        if not cluster:
            sns.set(rc={'figure.figsize':(20,17)})
            for column in columns:
                plt.subplot(4,4,k)
                sns.violinplot(data=data[column], color=sns.color_palette()[k])
                plt.title(f'{column} Violinplot')
                plt.xlabel(f'{column}')
                k+=1

            plt.tight_layout()
            plt.show()
        else:
            sns.set(rc={'figure.figsize':(20,8)})
            feature = columns[0]
            n_clusters = data['Cluster'].max()+1
            for label,n in zip(data['ClusterLabels'].unique(),data['Cluster'].unique()):
                plt.subplot(1,n_clusters+1,n+1)
                sns.violinplot(data=data[data['ClusterLabels']==label][feature], color=sns.color_palette()[k], cut=0)
                plt.title(f'{label}')
                plt.xlabel(f'count')
                k+=1
            plt.subplot(1,n_clusters+1,n_clusters+1)
            sns.violinplot(data=pop_data[feature], color='grey', cut=0)
            plt.title(f'Population')
            plt.xlabel(f'count')
            plt.tight_layout()
            plt.show()

    def multiplot_pies(self, data, columns, **kwargs):
        pie_feature = columns[0]
        pop_data = kwargs.get('pop_data')
        plt.figure(figsize = (15,25))

        for n,label in enumerate(data['ClusterLabels'].unique()):
            counts = data[data['ClusterLabels'] == label][pie_feature].value_counts()
            plt.subplot(1,5,n+1)
            plt.pie(counts, labels=counts.index,
                    autopct='%1.1f%%', startangle=50, shadow=True, colors=self.palette[2:], textprops={'color': 'black', 'fontsize': 14, 'weight': 'bold'})
            plt.title(f'{label}')

        plt.subplot(1,5,5)
        plt.pie(pop_data[pie_feature].value_counts(), labels=pop_data[pie_feature].value_counts().index, autopct='%1.1f%%', startangle=50, shadow=True, textprops={'color': 'black', 'fontsize': 14, 'weight': 'bold'})
        plt.title(f'Population')
        plt.tight_layout()
        plt.show()