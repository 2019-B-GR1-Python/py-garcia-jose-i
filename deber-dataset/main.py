# -*- coding: utf-8 -*-

"""
Created on Sun Dec  1 13:53:04 2019

@author: jose.garcia01
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="/home/tkhacker/git/py-garcia-jose-i/deber-dataset/data/kiva_loans.csv"

columns = [
        'loan_amount', 
        'activity', 
        'sector', 
        'country',
        'region',
        'term_in_months',
        'borrower_genders',
        'repayment_interval', 
        'date']

df1 = pd.read_csv(
        path,
        usecols = columns)

#df1['date'] = pd.to_datetime(df1['date'], format="%Y-%m-%d")

#Sum of the top loan sectors by country
sum_sector_by_country = df1.groupby(as_index=False, by=['country', 'sector'])['loan_amount'].sum().sort_values(by='loan_amount', ascending=False)
top_sector_by_country= sum_sector_by_country.groupby(as_index=False, by='country').first().sort_values(by='loan_amount', ascending=False)

top_sector_by_country = top_sector_by_country.set_index('country')
graph_top_sector_by_country = top_sector_by_country.plot(legend=False, kind='bar', figsize = (20, 15), color="coral", fontsize=13)
plt.title(label='Monto de la suma de los préstamos del sector más fundado por país', fontsize=40)

plt.ylabel('Suma de los préstamos', fontsize = 20)
yticks_top_sector_by_country = np.arange(0,20000001,2500000)
plt.yticks(yticks_top_sector_by_country, yticks_top_sector_by_country)

plt.xlabel('Países', fontsize = 20)
bars = graph_top_sector_by_country.patches
sector_labels = top_sector_by_country['sector'].array
for bar, sector_label in zip(bars, sector_labels):
    height = bar.get_height()
    graph_top_sector_by_country.text(
            bar.get_x() + bar.get_width() / 2, 
            height, 
            sector_label, 
            ha='center',
            va='bottom',
            rotation=90)
    
plt.show()

#Number of loans by country
top_sector_by_country_count = df1.groupby(as_index=False, by=['country'])['loan_amount'].count().sort_values(ascending=False, by='loan_amount')
top_sector_by_country_count.rename(columns={'loan_amount':'number_of_loans'}, inplace=True)

top_sector_by_country_count = top_sector_by_country_count.set_index('country')
graph_top_sector_by_country_count = top_sector_by_country_count.plot(legend=False, kind='bar', figsize = (20, 15), color='cyan', fontsize=13)
plt.title(label='Número de préstamos efectuados a cada País', fontsize=40)

plt.ylabel('Número de préstamos', fontsize = 20)
plt.xlabel('Países', fontsize = 20)
bars = graph_top_sector_by_country_count.patches
number_loans_labels = top_sector_by_country_count['number_of_loans'].array
for bar, number_loans_label in zip(bars, number_loans_labels):
    height = bar.get_height()
    graph_top_sector_by_country_count.text(
            bar.get_x() + bar.get_width() / 2, 
            height, 
            number_loans_label, 
            ha='center',
            va='bottom',
            rotation=90)
    
plt.show()

#Get Ecuador Data
ecuador = df1.groupby('country').get_group('Ecuador')

#Percentage by sector in Ecuador
amount_by_sector = ecuador.groupby('sector')['loan_amount'].sum().sort_values(ascending=False)

amount_by_sector_top = amount_by_sector[amount_by_sector>100000]
amount_by_sector_bottom = pd.Series(amount_by_sector[amount_by_sector <= 100000].sum(), index=['Others'])
amount_by_sector_top = amount_by_sector_top.append(amount_by_sector_bottom)

#Amount of loans by sector
amount_by_region = ecuador.groupby('region')['loan_amount'].sum().sort_values(ascending=False).head(10)

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
values_amount_by_region = amount_by_region.array
graph_amount_by_region = amount_by_region.plot(explode = explode, pctdistance=0.9, autopct='%1.1f%%', legend=True, shadow=True, kind='pie', figsize = (20, 15), fontsize=20)
plt.title(label='Top 10 Regiones más beneficiadas', fontsize=40)
#graph_amount_by_sector_top.legend(values_amount_by_region, loc='best', title = 'Values', title_fontsize=16 ,fontsize=13)

circle_donut=plt.Circle( (0,0), 0.6, color='white')
p=plt.gcf()
p.gca().add_artist(circle_donut)
plt.ylabel('')

plt.show()

#Amount by activity
amount_by_activity = ecuador.groupby('activity')['loan_amount'].sum().sort_values(ascending=False)

graph_amount_by_activity = amount_by_activity.plot(legend=False, kind='bar', figsize = (35, 16), color="coral", fontsize=13)
plt.title(label='Total de préstamos fundados por actividad en Ecuador', fontsize=40)

plt.ylabel('Monto fundado', fontsize = 20)
yticks_amount_by_activity = np.arange(0,2000000,250000)
plt.yticks(yticks_amount_by_activity, yticks_amount_by_activity)

plt.xlabel('Actividades', fontsize = 20)
bars = graph_amount_by_activity.patches
activity_amounts = amount_by_activity.array
for bar, activity_amount in zip(bars, activity_amounts):
    height = bar.get_height()
    graph_amount_by_activity.text(
            bar.get_x() + bar.get_width() / 2, 
            height, 
            activity_amount, 
            ha='center',
            va='bottom',
            rotation=90)
    
plt.show()

#Number of loans by activity
number_of_loans_by_activity = ecuador['activity'].value_counts(ascending=False)

graph_number_of_loans_by_activity = number_of_loans_by_activity.plot(legend=False, kind='bar', figsize = (35, 16), color="lawngreen", fontsize=13)
plt.title(label='Número de préstamos fundados por actividad en Ecuador', fontsize=40)

plt.ylabel('Número de préstamos', fontsize = 20)
yticks_number_of_loans_by_activity = np.arange(0,2000,500)
plt.yticks(yticks_number_of_loans_by_activity, yticks_number_of_loans_by_activity)

plt.xlabel('Actividades', fontsize = 20)
bars = graph_number_of_loans_by_activity.patches
activity_counts = number_of_loans_by_activity.array
for bar, activity_count in zip(bars, activity_counts):
    height = bar.get_height()
    graph_number_of_loans_by_activity.text(
            bar.get_x() + bar.get_width() / 2, 
            height, 
            activity_count, 
            ha='center',
            va='bottom',
            rotation=90)
    
plt.show()


#Amount of funded loans by date
amount_by_date = ecuador.groupby('date')['loan_amount'].sum().sort_values(ascending=False).head(20)

graph_amount_by_date = amount_by_date.plot.barh(legend=False, figsize = (20, 12), color="darkorange", fontsize=13)
plt.title(label='Días donde se fundó más préstamos en Ecuador', fontsize=40)

plt.ylabel('Fechas', fontsize = 20)
graph_amount_by_date.invert_yaxis() 

graph_amount_by_date.invert_yaxis()
plt.xlabel('Monto de préstamos fundado', fontsize = 20)
    
plt.show()


#Repayment interval
repayment_interval = ecuador['repayment_interval'].value_counts(ascending=False)
values_repayment_interval = repayment_interval.array
graph_repayment_interval = repayment_interval.plot(pctdistance=0.9, autopct='%1.1f%%', legend=False, shadow=True, kind='pie', figsize = (20, 15), fontsize=20)
plt.title(label='Forma de pago', fontsize=40)
circle_donut=plt.Circle( (0,0), 0.6, color='white')
p=plt.gcf()
p.gca().add_artist(circle_donut)
plt.ylabel('')
plt.show()


highest_loan = ecuador['loan_amount'].max()
average_loan_months = int(np.average(ecuador['term_in_months']))


pd.options.mode.chained_assignment = None
ecuador['borrower_genders'] = ecuador['borrower_genders'].astype(str)
ecuador['male_counts'] = ecuador['borrower_genders'].apply(lambda borrowers: borrowers.split(', ').count('male'))
ecuador['female_counts'] = ecuador['borrower_genders'].apply(lambda borrowers: borrowers.split(', ').count('female'))
male_borrowers = ecuador['male_counts'].sum()
female_borrowers = ecuador['female_counts'].sum()
ecuador['borrower_totals'] = ecuador['male_counts'] + ecuador['female_counts']

ecuador['male_loan_amount'] = ecuador['loan_amount'] * (ecuador['male_counts'] / ecuador['borrower_totals'])
ecuador['female_loan_amount'] = ecuador['loan_amount'] * (ecuador['female_counts'] / ecuador['borrower_totals'])
total_male_loan_amount = ecuador['male_loan_amount'].sum()
total_female_loan_amount = ecuador['female_loan_amount'].sum()

labels = ['Hombres', 'Mujeres']
values = [total_male_loan_amount, total_female_loan_amount]
explode = (0, 0.1)
fig1, graph_gender_loan_amount = plt.subplots()
graph_gender_loan_amount.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.show()

labels = ['Hombres', 'Mujeres']
values = [male_borrowers, female_borrowers]
explode = (0, 0.1)
fig2, graph_gender_loan_amount = plt.subplots()
fig2.set_size_inches(10, 7)
plt.rcParams['font.size'] = 20
graph_gender_loan_amount.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title(label='Porcentaje del número de personas que acceden al préstamo por Sexo', fontsize=32)
plt.show()


