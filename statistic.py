import plotly.graph_objects as pg
import plotly.Figure_fatcory as ff

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index= random.randit(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistic.mean(dataset)
    return mean

def setup ():
    mean_list = []
    for i in range(0,100):
         set_of_mean= random_set_of_mean(30) 
         mean_list.append(set_of_mean)
    show_fig(mean_list)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

first_std_devitation_start,  first_std_devitation_end = mean-first_std_devitation,  mean+std_devitation
second_std_devitation_start, second_std_devitation_end = mean-(2*std_devitation),  mean+(2*std_devitation)
third_std_devitation_start,  third_std_devitation_end = mean-(3*std_devitation),  mean+(3*std_devitation)

print(std1,first_std_devitation_start, first_std_devitation_end)
print(std2,second_std_devitation_start,second_std_devitation_end)
print(std3,third_std_devitation_start, third_std_devitation_end)

