#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
# @author:Clarky Clark Wang
# @license: Apache Licence 
# @file: DataGene.py 
# @time: 2021/10/26
# @contact: wangz@kth,se
# @software: PyCharm 
# Import Libs and Let's get started, shall we?
import pandas as pd
import names
from random_username.generate import generate_username

import random
from random import randint
import numpy as np
import matplotlib.pyplot as plt


def normal_dist(x, mean, sd):
    prob_density = (np.pi * sd) * np.exp(-2.5 * ((x - mean) / sd) ** 2)
    return prob_density


def UsersGenerator(size):
    x = np.linspace(13, 90, size)
    mean = np.mean(x) - 20
    sd = np.std(x)

    pdf = normal_dist(x, mean, sd)

    column_names = ["name", "username", "age"]

    df = pd.DataFrame(columns=column_names)

    for index in range(size):
        df.at[index, 'name'] = names.get_full_name()
        df.at[index, 'username'] = generate_username(1)[0]
        df.at[index, 'age'] = int(random.choices(x, pdf)[0])

    return df


def TaskGenerator(size):
    activity_label = ['Localization', 'Classify', 'Counting', 'Ordering']

    task_label_cars = ['Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Fiat', 'BMW', 'VW', 'Citroen', 'Seat', 'Alfa Romeo',
                       'Bugatti', 'Rivian', 'Mini', 'Range Rover', 'Porsche']
    task_label_animals = ['lion', 'squirrel', 'dog', 'deer', 'bee', 'sheep', 'fish', 'turkey', 'dove', 'chicken',
                          'horse', 'cat', 'owl', 'mouse', 'raccoon']
    task_label_space = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Lynx', 'Cancer',
                        'Leo', 'Andromeda', 'Taurus', 'Sagittarius', 'Corvus']
    task_label_sport = ['Football', 'Golf', 'Karate', 'Lacrosse', 'Paintball', 'Rafting', 'Rugby', 'Sailing',
                        'Skateboarding', 'Snowboarding', 'Swimming', 'Tennis', 'Volleyball', 'Windsurfing', 'Wrestling']

    task_label = []
    task_label.extend([task_label_cars, task_label_animals, task_label_space, task_label_sport])

    column_names = ["activity", "task"]

    df = pd.DataFrame(columns=column_names)

    for index in range(size):
        n_Task = randint(0, len(task_label) - 1)

        df.at[index, 'activity'] = np.random.choice(activity_label, 1, replace=False)[0]
        df.at[index, 'task'] = np.random.choice(task_label[n_Task], randint(5, len(task_label[n_Task])), replace=False)

    return df


def User_Task(size):
    df_Task = TaskGenerator(size)
    df_User = UsersGenerator(size)

    column_names = ["username", "activity", "task"]

    df = pd.DataFrame(columns=column_names)

    # print(df_Task)
    for index in range(size):

        respondes = randint(0, 5)
        listOfActivities = list(set([random.randint(0, size - 1) for i in range(respondes)]))

        listOfTasks = []

        for i in range(len(listOfActivities)):
            listOfTasks.append(list(set([random.randint(0, len(df_Task.iloc[listOfActivities[i]].task)) for i in
                                         range(len(listOfActivities))])))

        df.at[index, 'username'] = df_User.username[index]
        df.at[index, 'activity'] = listOfActivities
        df.at[index, 'task'] = listOfTasks

    return df_User, df_Task, df


def User_Friend(size, df_User):

    column_names = ["username", "friends"]

    df = pd.DataFrame(columns=column_names)

    for index in range(size):
        df.at[index, 'username'] = df_User.username[index]
        df.at[index, 'username'] = generate_username(1)[0]
        temp, limit = [], randint(0, 10)
        for i in range(limit):
            idx = random.randint(0, size)
            if idx != index:
                temp.append(idx)
        df.at[index, 'friends'] = list(set(temp))

    return df



#clablcankbfguobspzoègejnrws