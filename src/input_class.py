from parse_yaml import *
from config import ROOT
import pandas as pd
import numpy as np
import copy


class Inputs:
    inputfolder = f'{ROOT}/input/'

    def __init__(self, country, continent):
        self.continent = continent
        self.country = country

        self.country_b = None
        self.tot_users = None
        self.charging_mode = None
        self.logistic = None
        self.infr_prob = None
        self.charging_stations = None
        self.occasional_use = None
        self.battery_capacity = None
        self.add_country_yaml()

        self.year = None
        self.P_var = None
        self.r_d = None
        self.r_v = None
        self.r_w = None
        self.Par_P_EV = None
        self.add_common_yaml()

        self.country_c = None
        self.trips = None
        self.pop_sh = None
        self.vehicle_sh = None
        self.d_tot = None
        self.d_min = None
        self.t_func = None
        self.add_country_equivalents()
        self.add_trips()
        self.add_pop_share()
        self.add_vehicle_share()
        self.add_d_tot()
        self.add_d_min()
        self.add_t_func()

        self.window = None
        self.add_fuctioning_windows()

        self.perc_usage = None
        self.add_perc_usage()

    def add_country_yaml(self):
        inputfile = f'{ROOT}/input/{self.continent}/{self.country}.yaml'
        d = parse_yaml(inputfile)
        self.country_b = d['country']
        self.tot_users = d['tot_users']
        self.charging_mode = d['charging_mode']
        self.logistic = d['logistic']
        self.infr_prob = d['infr_prob']
        self.charging_stations = tuple(d['charging_stations'])
        self.occasional_use = d['occasional_use']
        self.battery_capacity = d['battery_capacity']

    def add_common_yaml(self):
        inputfile = f'{ROOT}/input/common_input.yaml'
        d = parse_yaml(inputfile)

        self.year = d['year']
        self.P_var = d['P_var']
        self.r_d = d['r_d']
        self.r_v = d['r_v']
        self.r_w = d['r_w']
        self.Par_P_EV = d['Par_P_EV']

    def add_country_equivalents(self):
        # For the data coming from the JRC Survey, a dictionary is defined to assign each country to the neighbouring one
        # these data are: d_tot, d_min, t_func, trips distribution by time
        country_dict = {'AT':'DE', 'CH':'DE', 'CZ':'DE', 'DK':'DE', 'FI':'DE', 'HU':'DE', 'NL':'DE', 'NO':'DE','SE':'DE', 'SK':'DE',
                        'PT':'ES',
                        'BE':'FR', 'LU':'FR',
                        'EL':'IT', 'HR':'IT', 'MT':'IT', 'SI':'IT',
                        'IE':'UK',
                        'BG':'PL', 'CY':'PL', 'EE':'PL', 'LT':'PL', 'LV':'PL', 'RO':'PL'}
        # Selection of the equivalent country JRC from the dictionary defined above
        if self.country_b in set(country_dict.values()):
            self.country_c = self.country_b
        else:
            self.country_c = country_dict[self.country_b]

    def add_trips(self):
        # Trips distribution by time
        self.trips = {}
        for day in ['weekday', 'saturday', 'sunday']:
            file = Inputs.inputfolder + f"trips_by_time_{day}.csv"
            self.trips[day] = pd.read_csv(file, header=0)
            try:
                self.trips[day] = self.trips[day][self.country] / 100
            except:
                try:
                    self.trips[day] = self.trips[day][self.country_b] / 100
                    print('country_b used for trips')
                except:
                    self.trips[day] = self.trips[day][self.country_c] / 100
                    print('country_c used for trips')

    def add_pop_share(self):
        # Composition of the population by percentage share
        pop_file = Inputs.inputfolder + "pop_share.csv"
        pop_data = pd.read_csv(pop_file, header=0, index_col=0)
        self.pop_sh = {}
        for us in ['working', 'student', 'inactive']:
            try:
                self.pop_sh[us] = pop_data.loc[self.country, us]
            except:
                try:
                    self.pop_sh[us] = pop_data.loc[self.country_b, us]
                    print('country_b used for pop_share')
                except:
                    self.pop_sh[us] = pop_data.loc[self.country_c, us]
                    print('country_c used for pop_share')

    def add_vehicle_share(self):
        # Share of the type of vehicles in the country
        vehicle_file = Inputs.inputfolder + "vehicle_share.csv"
        vehicle_data = pd.read_csv(vehicle_file, header=0, index_col=0)
        self.vehicle_sh = {}
        for size in ['small', 'medium', 'large']:
            try:
                self.vehicle_sh[size] = vehicle_data.loc[self.country, size]
            except:
                try:
                    self.vehicle_sh[size] = vehicle_data.loc[self.country_b, size]
                    print('country_b used for vehicle_share')
                except:
                    self.vehicle_sh[size] = vehicle_data.loc[self.country_c, size]
                    print('country_c used for vehicle_share')

    def add_d_tot(self):
        # Total daily distance [km]
        d_tot_file = Inputs.inputfolder + "d_tot.csv"
        d_tot_data = pd.read_csv(d_tot_file, header=0, index_col=0)
        self.d_tot = {}
        for day in ['weekday', 'saturday', 'sunday']:
            if day == 'weekday':
                week_or_weekend = 'weekday'
            else:
                week_or_weekend = 'weekend'
            try:
                self.d_tot[day] = d_tot_data.loc[self.country, week_or_weekend]
            except:
                try:
                    self.d_tot[day] = d_tot_data.loc[self.country_b, week_or_weekend]
                    print('country_b used for d_tot')
                except:
                    self.d_tot[day] = d_tot_data.loc[self.country_c, week_or_weekend]
                    print('country_c used for d_tot')

    def add_d_min(self):
        # Distance by trip [km]
        d_min_file = Inputs.inputfolder + "d_min.csv"
        d_min_data = pd.read_csv(d_min_file, header=0, index_col=[0, 1])
        self.d_min = {}
        for day in ['weekday', 'saturday', 'sunday']:
            self.d_min[day] = {}
            for travel_type in ['business', 'personal']:
                try:
                    self.d_min[day][travel_type] = d_min_data[self.country][travel_type][day]
                except:
                    try:
                        self.d_min[day][travel_type] = d_min_data[self.country_b][travel_type][day]
                        print('country_b used for d_min')
                    except:
                        self.d_min[day][travel_type] = d_min_data[self.country_c][travel_type][day]
                        print('country_c used for d_min')
            self.d_min[day]['mean'] = round(np.array([self.d_min[day][k] for k in self.d_min[day]]).mean())

    def add_t_func(self):
        # Functioning time by trip [min]
        t_func_file = Inputs.inputfolder + "t_func.csv"
        t_func_data = pd.read_csv(t_func_file, header=0, index_col=[0, 1])
        self.t_func = {}
        for day in ['weekday', 'saturday', 'sunday']:
            self.t_func[day] = {}
            for travel_type in ['business', 'personal']:
                try:
                    self.t_func[day][travel_type] = t_func_data[self.country][travel_type][day]
                except:
                    try:
                        self.t_func[day][travel_type] = t_func_data[self.country_b][travel_type][day]
                        print('country_b used for t_func')
                    except:
                        self.t_func[day][travel_type] = t_func_data[self.country_c][travel_type][day]
                        print('country_c used for t_func')
            self.t_func[day]['mean'] = round(np.array([self.t_func[day][k] for k in self.t_func[day]]).mean())

    def add_fuctioning_windows(self):
        # Functioning windows
        window_file = Inputs.inputfolder + "windows.csv"
        window_data = pd.read_csv(window_file, header=[0, 1], index_col=[0, 1, 2])
        window_data = window_data * 60
        window_data = window_data.astype(int)
        if self.country in window_data.columns.get_level_values(0):
            country_window = self.country
        else:
            print(
                '\n[WARNING] There are no specific functioning windows defined for the selected country, standard windows will be used. \nEdit the "windows.csv" file to add specific functioning windows.\n')
            country_window = 'Standard'
        self.window = {}
        self.window['working'] = {'main': [[window_data[country_window]['Start']['Working']['Main'][1],
                                       window_data[country_window]['End']['Working']['Main'][1]],
                                      [window_data[country_window]['Start']['Working']['Main'][2],
                                       window_data[country_window]['End']['Working']['Main'][2]]],
                             'free time': [[window_data[country_window]['Start']['Working']['Free time'][1],
                                            window_data[country_window]['End']['Working']['Free time'][1]],
                                           [window_data[country_window]['Start']['Working']['Free time'][2],
                                            window_data[country_window]['End']['Working']['Free time'][2]],
                                           [window_data[country_window]['Start']['Working']['Free time'][3],
                                            window_data[country_window]['End']['Working']['Free time'][3]]]}
        self.window['student'] = {'main': [[window_data[country_window]['Start']['Student']['Main'][1],
                                       window_data[country_window]['End']['Student']['Main'][1]],
                                      [window_data[country_window]['Start']['Student']['Main'][2],
                                       window_data[country_window]['End']['Student']['Main'][2]]],
                             'free time': [[window_data[country_window]['Start']['Student']['Free time'][1],
                                            window_data[country_window]['End']['Student']['Free time'][1]],
                                           [window_data[country_window]['Start']['Student']['Free time'][2],
                                            window_data[country_window]['End']['Student']['Free time'][2]],
                                           [window_data[country_window]['Start']['Student']['Free time'][3],
                                            window_data[country_window]['End']['Student']['Free time'][3]]]}
        self.window['inactive'] = {'main': [[window_data[country_window]['Start']['Inactive']['Main'][1],
                                        window_data[country_window]['End']['Inactive']['Main'][1]]],
                              'free time': [[window_data[country_window]['Start']['Inactive']['Free time'][1],
                                             window_data[country_window]['End']['Inactive']['Free time'][1]],
                                            [window_data[country_window]['Start']['Inactive']['Free time'][2],
                                             window_data[country_window]['End']['Inactive']['Free time'][2]]]}

    def add_perc_usage(self): # todo outside of class because it is not bare input
        # Re-format functioning windows to calculare the Percentage of travels in functioning windows
        wind_temp = copy.deepcopy(self.window)
        for key in wind_temp.keys():
            for act in ['main', 'free time']:
                wind_temp[key][act] = [item for sublist in self.window[key][act] for item in sublist]
                wind_temp[key][act] = [(x / 60) for x in wind_temp[key][act]]

        # Percentage of travels in functioning windows

        # main and free time is defined according to the functioning windows
        # If the windows are modified, also the perentages should be modified accordingly
        self.perc_usage = {}
        self.perc_usage['weekday'] = {'working': {'main': self.trips['weekday'].iloc[
            np.r_[wind_temp['working']['main'][0]:wind_temp['working']['main'][1],
            wind_temp['working']['main'][2]:wind_temp['working']['main'][3]]].sum()},
                                 'student': {'main': self.trips['weekday'].iloc[
                                     np.r_[wind_temp['student']['main'][0]:wind_temp['student']['main'][1],
                                     wind_temp['student']['main'][2]:wind_temp['student']['main'][3]]].sum()},
                                 'inactive': {'main': self.trips['weekday'].iloc[
                                     np.r_[
                                     wind_temp['inactive']['main'][0]:wind_temp['inactive']['main'][1]]].sum()}}
        self.perc_usage['saturday'] = {'working': {'main': self.trips['saturday'].iloc[
            np.r_[wind_temp['working']['main'][0]:wind_temp['working']['main'][1],
            wind_temp['working']['main'][2]:wind_temp['working']['main'][3]]].sum()},
                                  'student': {'main': self.trips['saturday'].iloc[
                                      np.r_[wind_temp['student']['main'][0]:wind_temp['student']['main'][1],
                                      wind_temp['student']['main'][2]:wind_temp['student']['main'][3]]].sum()},
                                  'inactive': {'main': self.trips['saturday'].iloc[
                                      np.r_[
                                      wind_temp['inactive']['main'][0]:wind_temp['inactive']['main'][1]]].sum()}}
        self.perc_usage['sunday'] = {'working': {'main': self.trips['saturday'].iloc[
            np.r_[wind_temp['working']['main'][0]:wind_temp['working']['main'][1],
            wind_temp['working']['main'][2]:wind_temp['working']['main'][3]]].sum()},
                                'student': {'main': self.trips['saturday'].iloc[
                                    np.r_[wind_temp['student']['main'][0]:wind_temp['student']['main'][1],
                                    wind_temp['student']['main'][2]:wind_temp['student']['main'][3]]].sum()},
                                'inactive': {'main': self.trips['saturday'].iloc[
                                    np.r_[
                                    wind_temp['inactive']['main'][0]:wind_temp['inactive']['main'][1]]].sum()}}

        # Calulate the Percentage of travels in functioning windows for free time
        # as complementary to the main time
        for key in self.perc_usage.keys():
            for us_type in ['working', 'student', 'inactive']:
                self.perc_usage[key][us_type]['free time'] = 1 - self.perc_usage[key][us_type]['main']