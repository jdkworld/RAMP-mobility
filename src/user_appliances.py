import numpy as np
import pandas as pd
import copy
import os
from src.config import ROOT
from input.common_input import *
from parse_yaml import *
from src.core_model import User
from input_class import Inputs


def make_users_and_appliances(inputcountry):
    tot_users = inputcountry.tot_users
    pop_sh = inputcountry.pop_sh
    vehicle_sh = inputcountry.vehicle_sh
    Battery_cap = inputcountry.battery_capacity
    d_tot = inputcountry.d_tot
    t_func = inputcountry.t_func
    d_min = inputcountry.d_min
    perc_usage = inputcountry.perc_usage
    occasional_use = inputcountry.occasional_use
    window = inputcountry.window

    user_dict = {}
    appliance_dict = {}
    User_list = []

    person_list = ['working', 'student', 'inactive']
    carsize_list = ['large', 'medium', 'small']
    day_list = ['weekday', 'saturday', 'sunday']

    for person in person_list:
        user_dict[person] = {}
        for carsize in carsize_list:
            username = person.capitalize() + " - " + carsize.capitalize() + " car"
            user = User(name=username, us_pref=0,
                     n_users=int(round(tot_users * pop_sh[person] * vehicle_sh[carsize])))
            user_dict[person][carsize] = user
            User_list.append(user)

    for person in person_list:
        appliance_dict[person] = {}
        for carsize in carsize_list:
            appliance_dict[person][carsize] = {}
            for i, day in enumerate(day_list):
                appliance_dict[person][carsize][day] = {}
                wdwe_type = i
                if day == 'weekday':
                    actualperson = person
                    wdwe_name = 'weekday'
                else:
                    actualperson = 'inactive'
                    wdwe_name = 'weekend'
                for main_or_free in ['main', 'free time']:
                    if main_or_free == 'main':
                        business_or_personal = 'business'
                        rw_key = actualperson
                    else:
                        business_or_personal = 'personal'
                        rw_key = 'free time'
                    if person == 'inactive':
                        if main_or_free == 'main':
                            window_amount = 1
                        else:
                            window_amount = 2
                    else:
                        if day == 'weekday':
                            if main_or_free == 'main':
                                window_amount = 2
                            else:
                                window_amount = 3
                        else:
                            if main_or_free == 'main':
                                window_amount = 1
                            else:
                                window_amount = 2

                    if main_or_free == 'main':
                        appliance = user_dict[person][carsize].Appliance(user_dict[person][carsize],
                                                                n=1, Par_power=Par_P_EV[carsize],
                                                                  Battery_cap=Battery_cap[carsize],
                                                                  P_var=P_var, w=window_amount,
                                                                  d_tot=d_tot[day] * perc_usage[day][actualperson][
                                                                      main_or_free], r_d=r_d,
                                                                  t_func=t_func[day][business_or_personal], r_v=r_v,
                                                                  d_min=d_min[day][business_or_personal], fixed='no',
                                                                  fixed_cycle=0,
                                                                  occasional_use=occasional_use[day], flat='no',
                                                                  pref_index=0,
                                                                  wd_we_type=wdwe_type, P_series=False)
                    else:
                        appliance = user_dict[person][carsize].Appliance(user_dict[person][carsize],
                                                                         n=1, Par_power=Par_P_EV[carsize],
                                                                         Battery_cap=Battery_cap[carsize],
                                                                         P_var=P_var, w=window_amount,
                                                                         d_tot=d_tot[day] *
                                                                               perc_usage[day][actualperson][
                                                                                   main_or_free], r_d=r_d,
                                                                         t_func=t_func[day][business_or_personal],
                                                                         r_v=r_v,
                                                                         d_min=d_min[day][business_or_personal],
                                                                         fixed='no',
                                                                         fixed_cycle=0,
                                                                         occasional_use=occasional_use[main_or_free][wdwe_name], flat='no',
                                                                         pref_index=0,
                                                                         wd_we_type=wdwe_type, P_series=False)

                    if window_amount == 1:
                        appliance.windows(w1=window[actualperson][main_or_free][0],
                                                r_w=r_w[rw_key])
                    elif window_amount == 2:
                        appliance.windows(w1=window[actualperson][main_or_free][0], w2=window[actualperson][main_or_free][1],
                                                r_w=r_w[rw_key])
                    else:
                        appliance.windows(w1=window[actualperson][main_or_free][0], w2=window[actualperson][main_or_free][1],
                                                w3=window[actualperson][main_or_free][2], r_w=r_w[rw_key])

                    appliance_dict[person][carsize][day][main_or_free] = appliance
    return user_dict, appliance_dict


