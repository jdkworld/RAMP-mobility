from input.common_input import *
from src.core_model import User
from input_class import Inputs
from user_appliances import make_users_and_appliances


# file to check the user_appliances.py

inputcountry = Inputs('IND', 'industry')
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


User_list = []


### Working ###

Working_L = User(name="Working - Large car", us_pref=0,
                 n_users=int(round(tot_users * pop_sh['working'] * vehicle_sh['large'])))
User_list.append(Working_L)
Working_M = User(name="Working - Medium car", us_pref=0,
                 n_users=int(round(tot_users * pop_sh['working'] * vehicle_sh['medium'])))
User_list.append(Working_M)
Working_S = User(name="Working - Small car", us_pref=0,
                 n_users=int(round(tot_users * pop_sh['working'] * vehicle_sh['small'])))
User_list.append(Working_S)

### Student ###

Student_L = User(name="Student - Large car", us_pref=0,
                 n_users=int(round(tot_users * pop_sh['student'] * vehicle_sh['large'])))
User_list.append(Student_L)
Student_M = User(name="Student - Medium car", us_pref=0,
                 n_users=int(round(tot_users * pop_sh['student'] * vehicle_sh['medium'])))
User_list.append(Student_M)
Student_S = User(name="Student - Small car", us_pref=0,
                 n_users=int(round(tot_users * pop_sh['student'] * vehicle_sh['small'])))
User_list.append(Student_S)

### Inactive ###

Inactive_L = User(name="Inactive - Large car", us_pref=0,
                  n_users=int(round(tot_users * pop_sh['inactive'] * vehicle_sh['large'])))
User_list.append(Inactive_L)
Inactive_M = User(name="Inactive - Medium car", us_pref=0,
                  n_users=int(round(tot_users * pop_sh['inactive'] * vehicle_sh['medium'])))
User_list.append(Inactive_M)
Inactive_S = User(name="Inactive - Small car", us_pref=0,
                  n_users=int(round(tot_users * pop_sh['inactive'] * vehicle_sh['small'])))
User_list.append(Inactive_S)

# %% Definition of APPLIANCES
"""
APPLIANCES
"""



# %% Working

### Large Car ###

# Working - Large Car - Weekday
Working_EV_large_wd = Working_L.Appliance(Working_L, n=1, Par_power=Par_P_EV['large'], Battery_cap=Battery_cap['large'],
                                          P_var=P_var, w=2,
                                          d_tot=d_tot['weekday'] * perc_usage['weekday']['working']['main'], r_d=r_d,
                                          t_func=t_func['weekday']['business'], r_v=r_v,
                                          d_min=d_min['weekday']['business'], fixed='no', fixed_cycle=0,
                                          occasional_use=occasional_use['weekday'], flat='no', pref_index=0,
                                          wd_we_type=0, P_series=False)
Working_EV_large_wd.windows(w1=window['working']['main'][0], w2=window['working']['main'][1], r_w=r_w['working'])

# Working - Large Car - Weekday - Free Time
Working_EV_large_wd_ft = Working_L.Appliance(Working_L, n=1, Par_power=Par_P_EV['large'],
                                             Battery_cap=Battery_cap['large'], P_var=P_var, w=3,
                                             d_tot=d_tot['weekday'] * perc_usage['weekday']['working']['free time'],
                                             r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                             d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['free time']['weekday'], flat='no',
                                             pref_index=0, wd_we_type=0, P_series=False)
Working_EV_large_wd_ft.windows(w1=window['working']['free time'][0], w2=window['working']['free time'][1],
                               w3=window['working']['free time'][2], r_w=r_w['free time'])

# Working - Large Car - Saturday
Working_EV_large_sat = Working_L.Appliance(Working_L, n=1, Par_power=Par_P_EV['large'],
                                           Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                           d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                           r_d=r_d, t_func=t_func['saturday']['business'], r_v=r_v,
                                           d_min=d_min['saturday']['business'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                           wd_we_type=1, P_series=False)
Working_EV_large_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Working - Large Car - Saturday - Free Time
Working_EV_large_sat_ft = Working_L.Appliance(Working_L, n=1, Par_power=Par_P_EV['large'],
                                              Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                              d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                              d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=1, P_series=False)
Working_EV_large_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# Working - Large Car - Sunday
Working_EV_large_sun = Working_L.Appliance(Working_L, n=1, Par_power=Par_P_EV['large'],
                                           Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                           d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                           t_func=t_func['sunday']['business'], r_v=r_v,
                                           d_min=d_min['sunday']['business'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['sunday'], flat='no', pref_index=0,
                                           wd_we_type=2, P_series=False)
Working_EV_large_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Working - Large Car - Sunday - Free Time
Working_EV_large_sun_ft = Working_L.Appliance(Working_L, n=1, Par_power=Par_P_EV['large'],
                                              Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                              d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                              d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=2, P_series=False)
Working_EV_large_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

### Medium Car ###

# Working - Medium Car - Weekday
Working_EV_medium_wd = Working_M.Appliance(Working_M, n=1, Par_power=Par_P_EV['medium'],
                                           Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                           d_tot=d_tot['weekday'] * perc_usage['weekday']['working']['main'], r_d=r_d,
                                           t_func=t_func['weekday']['business'], r_v=r_v,
                                           d_min=d_min['weekday']['business'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['weekday'], flat='no', pref_index=0,
                                           wd_we_type=0, P_series=False)
Working_EV_medium_wd.windows(w1=window['working']['main'][0], w2=window['working']['main'][1], r_w=r_w['working'])

# Working - Medium Car - Weekday - Free Time
Working_EV_medium_wd_ft = Working_M.Appliance(Working_M, n=1, Par_power=Par_P_EV['medium'],
                                              Battery_cap=Battery_cap['medium'], P_var=P_var, w=3,
                                              d_tot=d_tot['weekday'] * perc_usage['weekday']['working']['free time'],
                                              r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                              d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekday'], flat='no',
                                              pref_index=0, wd_we_type=0, P_series=False)
Working_EV_medium_wd_ft.windows(w1=window['working']['free time'][0], w2=window['working']['free time'][1],
                                w3=window['working']['free time'][2], r_w=r_w['free time'])

# Working - Medium Car - Saturday
Working_EV_medium_sat = Working_M.Appliance(Working_M, n=1, Par_power=Par_P_EV['medium'],
                                            Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                            d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                            r_d=r_d, t_func=t_func['saturday']['business'], r_v=r_v,
                                            d_min=d_min['saturday']['business'], fixed='no', fixed_cycle=0,
                                            occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                            wd_we_type=1, P_series=False)
Working_EV_medium_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Working - Medium Car - Saturday - Free Time
Working_EV_medium_sat_ft = Working_M.Appliance(Working_M, n=1, Par_power=Par_P_EV['medium'],
                                               Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                               d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive'][
                                                   'free time'], r_d=r_d, t_func=t_func['saturday']['personal'],
                                               r_v=r_v, d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                               occasional_use=occasional_use['free time']['weekend'], flat='no',
                                               pref_index=0, wd_we_type=1, P_series=False)
Working_EV_medium_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

# Working - Medium Car - Sunday
Working_EV_medium_sun = Working_M.Appliance(Working_M, n=1, Par_power=Par_P_EV['medium'],
                                            Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                            d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                            t_func=t_func['sunday']['business'], r_v=r_v,
                                            d_min=d_min['sunday']['business'], fixed='no', fixed_cycle=0,
                                            occasional_use=occasional_use['sunday'], flat='no', pref_index=0,
                                            wd_we_type=2, P_series=False)
Working_EV_medium_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Working - Medium Car - Sunday - Free Time
Working_EV_medium_sun_ft = Working_M.Appliance(Working_M, n=1, Par_power=Par_P_EV['medium'],
                                               Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                               d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                               r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                               d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                               occasional_use=occasional_use['free time']['weekend'], flat='no',
                                               pref_index=0, wd_we_type=2, P_series=False)
Working_EV_medium_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

### Small Car ###

# Working - Small Car - Weekday
Working_EV_small_wd = Working_S.Appliance(Working_S, n=1, Par_power=Par_P_EV['small'], Battery_cap=Battery_cap['small'],
                                          P_var=P_var, w=2,
                                          d_tot=d_tot['weekday'] * perc_usage['weekday']['working']['main'], r_d=r_d,
                                          t_func=t_func['weekday']['business'], r_v=r_v,
                                          d_min=d_min['weekday']['business'], fixed='no', fixed_cycle=0,
                                          occasional_use=occasional_use['weekday'], flat='no', pref_index=0,
                                          wd_we_type=0, P_series=False)
Working_EV_small_wd.windows(w1=window['working']['main'][0], w2=window['working']['main'][1], r_w=r_w['working'])

# Working - Small Car - Weekday - Free Time
Working_EV_small_wd_ft = Working_S.Appliance(Working_S, n=1, Par_power=Par_P_EV['small'],
                                             Battery_cap=Battery_cap['small'], P_var=P_var, w=3,
                                             d_tot=d_tot['weekday'] * perc_usage['weekday']['working']['free time'],
                                             r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                             d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['free time']['weekday'], flat='no',
                                             pref_index=0, wd_we_type=0, P_series=False)
Working_EV_small_wd_ft.windows(w1=window['working']['free time'][0], w2=window['working']['free time'][1],
                               w3=window['working']['free time'][2], r_w=r_w['free time'])

# Working - Small Car - Saturday
Working_EV_small_sat = Working_S.Appliance(Working_S, n=1, Par_power=Par_P_EV['small'],
                                           Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                           d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                           r_d=r_d, t_func=t_func['saturday']['business'], r_v=r_v,
                                           d_min=d_min['saturday']['business'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                           wd_we_type=1, P_series=False)
Working_EV_small_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Working - Small Car - Saturday - Free Time
Working_EV_small_sat_ft = Working_S.Appliance(Working_S, n=1, Par_power=Par_P_EV['small'],
                                              Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                              d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                              d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=1, P_series=False)
Working_EV_small_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# Working - Small Car - Sunday
Working_EV_small_sun = Working_S.Appliance(Working_S, n=1, Par_power=Par_P_EV['small'],
                                           Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                           d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                           t_func=t_func['sunday']['business'], r_v=r_v,
                                           d_min=d_min['sunday']['business'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['sunday'], flat='no', pref_index=0,
                                           wd_we_type=2, P_series=False)
Working_EV_small_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Working - Small Car - Sunday - Free Time
Working_EV_small_sun_ft = Working_S.Appliance(Working_S, n=1, Par_power=Par_P_EV['small'],
                                              Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                              d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                              d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=2, P_series=False)
Working_EV_small_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# %% Student

### Large Car ###

# Student - Large Car - Weekday
Student_EV_large_wd = Student_L.Appliance(Student_L, n=1, Par_power=Par_P_EV['large'], Battery_cap=Battery_cap['large'],
                                          P_var=P_var, w=2,
                                          d_tot=d_tot['weekday'] * perc_usage['weekday']['student']['main'], r_d=r_d,
                                          t_func=t_func['weekday']['mean'], r_v=r_v, d_min=d_min['weekday']['mean'],
                                          fixed='no', fixed_cycle=0, occasional_use=occasional_use['weekday'],
                                          flat='no', pref_index=0, wd_we_type=0, P_series=False)
Student_EV_large_wd.windows(w1=window['student']['main'][0], w2=window['student']['main'][1], r_w=r_w['student'])

# Student - Large Car - Weekday - Free Time
Student_EV_large_wd_ft = Student_L.Appliance(Student_L, n=1, Par_power=Par_P_EV['large'],
                                             Battery_cap=Battery_cap['large'], P_var=P_var, w=3,
                                             d_tot=d_tot['weekday'] * perc_usage['weekday']['student']['free time'],
                                             r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                             d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['free time']['weekday'], flat='no',
                                             pref_index=0, wd_we_type=0, P_series=False)
Student_EV_large_wd_ft.windows(w1=window['student']['free time'][0], w2=window['student']['free time'][1],
                               w3=window['student']['free time'][2], r_w=r_w['free time'])

# Student - Large Car - Saturday
Student_EV_large_sat = Student_L.Appliance(Student_L, n=1, Par_power=Par_P_EV['large'],
                                           Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                           d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                           r_d=r_d, t_func=t_func['saturday']['mean'], r_v=r_v,
                                           d_min=d_min['saturday']['mean'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                           wd_we_type=1, P_series=False)
Student_EV_large_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Student - Large Car - Saturday - Free Time
Student_EV_large_sat_ft = Student_L.Appliance(Student_L, n=1, Par_power=Par_P_EV['large'],
                                              Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                              d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                              d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=1, P_series=False)
Student_EV_large_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# Student - Large Car - Sunday
Student_EV_large_sun = Student_L.Appliance(Student_L, n=1, Par_power=Par_P_EV['large'],
                                           Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                           d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                           t_func=t_func['sunday']['mean'], r_v=r_v, d_min=d_min['sunday']['mean'],
                                           fixed='no', fixed_cycle=0, occasional_use=occasional_use['sunday'],
                                           flat='no', pref_index=0, wd_we_type=2, P_series=False)
Student_EV_large_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Student - Large Car - Sunday - Free Time
Student_EV_large_sun_ft = Student_L.Appliance(Student_L, n=1, Par_power=Par_P_EV['large'],
                                              Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                              d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                              d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=2, P_series=False)
Student_EV_large_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

### Medium Car ###

# Student - Medium Car - Weekday
Student_EV_medium_wd = Student_M.Appliance(Student_M, n=1, Par_power=Par_P_EV['medium'],
                                           Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                           d_tot=d_tot['weekday'] * perc_usage['weekday']['student']['main'], r_d=r_d,
                                           t_func=t_func['weekday']['mean'], r_v=r_v, d_min=d_min['weekday']['mean'],
                                           fixed='no', fixed_cycle=0, occasional_use=occasional_use['weekday'],
                                           flat='no', pref_index=0, wd_we_type=0, P_series=False)
Student_EV_medium_wd.windows(w1=window['student']['main'][0], w2=window['student']['main'][1], r_w=r_w['student'])

# Student - Medium Car - Weekday - Free Time
Student_EV_medium_wd_ft = Student_M.Appliance(Student_M, n=1, Par_power=Par_P_EV['medium'],
                                              Battery_cap=Battery_cap['medium'], P_var=P_var, w=3,
                                              d_tot=d_tot['weekday'] * perc_usage['weekday']['student']['free time'],
                                              r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                              d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekday'], flat='no',
                                              pref_index=0, wd_we_type=0, P_series=False)
Student_EV_medium_wd_ft.windows(w1=window['student']['free time'][0], w2=window['student']['free time'][1],
                                w3=window['student']['free time'][2], r_w=r_w['free time'])

# Student - Medium Car - Saturday
Student_EV_medium_sat = Student_M.Appliance(Student_M, n=1, Par_power=Par_P_EV['medium'],
                                            Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                            d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                            r_d=r_d, t_func=t_func['saturday']['mean'], r_v=r_v,
                                            d_min=d_min['saturday']['mean'], fixed='no', fixed_cycle=0,
                                            occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                            wd_we_type=1, P_series=False)
Student_EV_medium_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Student - Medium Car - Saturday - Free Time
Student_EV_medium_sat_ft = Student_M.Appliance(Student_M, n=1, Par_power=Par_P_EV['medium'],
                                               Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                               d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive'][
                                                   'free time'], r_d=r_d, t_func=t_func['saturday']['personal'],
                                               r_v=r_v, d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                               occasional_use=occasional_use['free time']['weekend'], flat='no',
                                               pref_index=0, wd_we_type=1, P_series=False)
Student_EV_medium_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

# Student - Medium Car - Sunday
Student_EV_medium_sun = Student_M.Appliance(Student_M, n=1, Par_power=Par_P_EV['medium'],
                                            Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                            d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                            t_func=t_func['sunday']['mean'], r_v=r_v, d_min=d_min['sunday']['mean'],
                                            fixed='no', fixed_cycle=0, occasional_use=occasional_use['sunday'],
                                            flat='no', pref_index=0, wd_we_type=2, P_series=False)
Student_EV_medium_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Student - Medium Car - Sunday - Free Time
Student_EV_medium_sun_ft = Student_M.Appliance(Student_M, n=1, Par_power=Par_P_EV['medium'],
                                               Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                               d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                               r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                               d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                               occasional_use=occasional_use['free time']['weekend'], flat='no',
                                               pref_index=0, wd_we_type=2, P_series=False)
Student_EV_medium_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

### Small Car ###

# Student - Small Car - Weekday
Student_EV_small_wd = Student_S.Appliance(Student_S, n=1, Par_power=Par_P_EV['small'], Battery_cap=Battery_cap['small'],
                                          P_var=P_var, w=2,
                                          d_tot=d_tot['weekday'] * perc_usage['weekday']['student']['main'], r_d=r_d,
                                          t_func=t_func['weekday']['mean'], r_v=r_v, d_min=d_min['weekday']['mean'],
                                          fixed='no', fixed_cycle=0, occasional_use=occasional_use['weekday'],
                                          flat='no', pref_index=0, wd_we_type=0, P_series=False)
Student_EV_small_wd.windows(w1=window['student']['main'][0], w2=window['student']['main'][1], r_w=r_w['student'])

# Student - Small Car - Weekday - Free Time
Student_EV_small_wd_ft = Student_S.Appliance(Student_S, n=1, Par_power=Par_P_EV['small'],
                                             Battery_cap=Battery_cap['small'], P_var=P_var, w=3,
                                             d_tot=d_tot['weekday'] * perc_usage['weekday']['student']['free time'],
                                             r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                             d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['free time']['weekday'], flat='no',
                                             pref_index=0, wd_we_type=0, P_series=False)
Student_EV_small_wd_ft.windows(w1=window['student']['free time'][0], w2=window['student']['free time'][1],
                               w3=window['student']['free time'][2], r_w=r_w['free time'])

# Student - Small Car - Saturday
Student_EV_small_sat = Student_S.Appliance(Student_S, n=1, Par_power=Par_P_EV['small'],
                                           Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                           d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                           r_d=r_d, t_func=t_func['saturday']['mean'], r_v=r_v,
                                           d_min=d_min['saturday']['mean'], fixed='no', fixed_cycle=0,
                                           occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                           wd_we_type=1, P_series=False)
Student_EV_small_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Student - Small Car - Saturday - Free Time
Student_EV_small_sat_ft = Student_S.Appliance(Student_S, n=1, Par_power=Par_P_EV['small'],
                                              Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                              d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                              d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=1, P_series=False)
Student_EV_small_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# Student - Small Car - Sunday
Student_EV_small_sun = Student_S.Appliance(Student_S, n=1, Par_power=Par_P_EV['small'],
                                           Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                           d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                           t_func=t_func['sunday']['mean'], r_v=r_v, d_min=d_min['sunday']['mean'],
                                           fixed='no', fixed_cycle=0, occasional_use=occasional_use['sunday'],
                                           flat='no', pref_index=0, wd_we_type=2, P_series=False)
Student_EV_small_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Student - Medium Car - Sunday - Free Time
Student_EV_small_sun_ft = Student_S.Appliance(Student_S, n=1, Par_power=Par_P_EV['small'],
                                              Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                              d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                              r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                              d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['free time']['weekend'], flat='no',
                                              pref_index=0, wd_we_type=2, P_series=False)
Student_EV_small_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# %% Inactive

### Large Car ###

# Inactive - Large Car - Weekday
Inactive_EV_large_wd = Inactive_L.Appliance(Inactive_L, n=1, Par_power=Par_P_EV['large'],
                                            Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                            d_tot=d_tot['weekday'] * perc_usage['weekday']['inactive']['main'], r_d=r_d,
                                            t_func=t_func['weekday']['personal'], r_v=r_v,
                                            d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                            occasional_use=occasional_use['weekday'], flat='no', pref_index=0,
                                            wd_we_type=0, P_series=False)
Inactive_EV_large_wd.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Large Car - Weekday - Free Time
Inactive_EV_large_wd_ft = Inactive_L.Appliance(Inactive_L, n=1, Par_power=Par_P_EV['large'],
                                               Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                               d_tot=d_tot['weekday'] * perc_usage['weekday']['inactive']['free time'],
                                               r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                               d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                               occasional_use=occasional_use['free time']['weekday'], flat='no',
                                               pref_index=0, wd_we_type=0, P_series=False)
Inactive_EV_large_wd_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# Inactive - Large Car - Saturday
Inactive_EV_large_sat = Inactive_L.Appliance(Inactive_L, n=1, Par_power=Par_P_EV['large'],
                                             Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                             d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                             r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                             d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                             wd_we_type=1, P_series=False)
Inactive_EV_large_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Large Car - Saturday - Free Time
Inactive_EV_large_sat_ft = Inactive_L.Appliance(Inactive_L, n=1, Par_power=Par_P_EV['large'],
                                                Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                                d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive'][
                                                    'free time'], r_d=r_d, t_func=t_func['saturday']['personal'],
                                                r_v=r_v, d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                                occasional_use=occasional_use['free time']['weekend'], flat='no',
                                                pref_index=0, wd_we_type=1, P_series=False)
Inactive_EV_large_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

# Inactive - Large Car - Sunday
Inactive_EV_large_sun = Inactive_L.Appliance(Inactive_L, n=1, Par_power=Par_P_EV['large'],
                                             Battery_cap=Battery_cap['large'], P_var=P_var, w=1,
                                             d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                             t_func=t_func['sunday']['personal'], r_v=r_v,
                                             d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['sunday'], flat='no', pref_index=0,
                                             wd_we_type=2, P_series=False)
Inactive_EV_large_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Large Car - Sunday - Free Time
Inactive_EV_large_sun_ft = Inactive_L.Appliance(Inactive_L, n=1, Par_power=Par_P_EV['large'],
                                                Battery_cap=Battery_cap['large'], P_var=P_var, w=2,
                                                d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                                r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                                d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                                occasional_use=occasional_use['free time']['weekend'], flat='no',
                                                pref_index=0, wd_we_type=2, P_series=False)
Inactive_EV_large_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

### Medium Car ###

# Inactive - Medium Car - Weekday
Inactive_EV_medium_wd = Inactive_M.Appliance(Inactive_M, n=1, Par_power=Par_P_EV['medium'],
                                             Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                             d_tot=d_tot['weekday'] * perc_usage['weekday']['inactive']['main'],
                                             r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                             d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['weekday'], flat='no', pref_index=0,
                                             wd_we_type=0, P_series=False)
Inactive_EV_medium_wd.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Medium Car - Weekday - Free Time
Inactive_EV_medium_wd_ft = Inactive_M.Appliance(Inactive_M, n=1, Par_power=Par_P_EV['medium'],
                                                Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                                d_tot=d_tot['weekday'] * perc_usage['weekday']['inactive']['free time'],
                                                r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                                d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                                occasional_use=occasional_use['free time']['weekday'], flat='no',
                                                pref_index=0, wd_we_type=0, P_series=False)
Inactive_EV_medium_wd_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

# Inactive - Medium Car - Saturday
Inactive_EV_medium_sat = Inactive_M.Appliance(Inactive_M, n=1, Par_power=Par_P_EV['medium'],
                                              Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                              d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                              r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                              d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                              wd_we_type=1, P_series=False)
Inactive_EV_medium_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Medium Car - Saturday - Free Time
Inactive_EV_medium_sat_ft = Inactive_M.Appliance(Inactive_M, n=1, Par_power=Par_P_EV['medium'],
                                                 Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                                 d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive'][
                                                     'free time'], r_d=r_d, t_func=t_func['saturday']['personal'],
                                                 r_v=r_v, d_min=d_min['saturday']['personal'], fixed='no',
                                                 fixed_cycle=0, occasional_use=occasional_use['free time']['weekend'],
                                                 flat='no', pref_index=0, wd_we_type=1, P_series=False)
Inactive_EV_medium_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                  r_w=r_w['free time'])

# Inactive - Medium Car - Sunday
Inactive_EV_medium_sun = Inactive_M.Appliance(Inactive_M, n=1, Par_power=Par_P_EV['medium'],
                                              Battery_cap=Battery_cap['medium'], P_var=P_var, w=1,
                                              d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                              t_func=t_func['sunday']['personal'], r_v=r_v,
                                              d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                              occasional_use=occasional_use['sunday'], flat='no', pref_index=0,
                                              wd_we_type=2, P_series=False)
Inactive_EV_medium_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Medium Car - Sunday - Free Time
Inactive_EV_medium_sun_ft = Inactive_M.Appliance(Inactive_M, n=1, Par_power=Par_P_EV['medium'],
                                                 Battery_cap=Battery_cap['medium'], P_var=P_var, w=2,
                                                 d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                                 r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                                 d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                                 occasional_use=occasional_use['free time']['weekend'], flat='no',
                                                 pref_index=0, wd_we_type=2, P_series=False)
Inactive_EV_medium_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                  r_w=r_w['free time'])

### Small Car ###

# Inactive - Small Car - Weekday
Inactive_EV_small_wd = Inactive_S.Appliance(Inactive_S, n=1, Par_power=Par_P_EV['small'],
                                            Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                            d_tot=d_tot['weekday'] * perc_usage['weekday']['inactive']['main'], r_d=r_d,
                                            t_func=t_func['weekday']['personal'], r_v=r_v,
                                            d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                            occasional_use=occasional_use['weekday'], flat='no', pref_index=0,
                                            wd_we_type=0, P_series=False)
Inactive_EV_small_wd.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Small Car - Weekday - Free Time
Inactive_EV_small_wd_ft = Inactive_S.Appliance(Inactive_S, n=1, Par_power=Par_P_EV['small'],
                                               Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                               d_tot=d_tot['weekday'] * perc_usage['weekday']['inactive']['free time'],
                                               r_d=r_d, t_func=t_func['weekday']['personal'], r_v=r_v,
                                               d_min=d_min['weekday']['personal'], fixed='no', fixed_cycle=0,
                                               occasional_use=occasional_use['free time']['weekday'], flat='no',
                                               pref_index=0, wd_we_type=0, P_series=False)
Inactive_EV_small_wd_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                r_w=r_w['free time'])

# Inactive - Small Car - Saturday
Inactive_EV_small_sat = Inactive_S.Appliance(Inactive_S, n=1, Par_power=Par_P_EV['small'],
                                             Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                             d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive']['main'],
                                             r_d=r_d, t_func=t_func['saturday']['personal'], r_v=r_v,
                                             d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['saturday'], flat='no', pref_index=0,
                                             wd_we_type=1, P_series=False)
Inactive_EV_small_sat.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Small Car - Saturday - Free Time
Inactive_EV_small_sat_ft = Inactive_S.Appliance(Inactive_S, n=1, Par_power=Par_P_EV['small'],
                                                Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                                d_tot=d_tot['saturday'] * perc_usage['saturday']['inactive'][
                                                    'free time'], r_d=r_d, t_func=t_func['saturday']['personal'],
                                                r_v=r_v, d_min=d_min['saturday']['personal'], fixed='no', fixed_cycle=0,
                                                occasional_use=occasional_use['free time']['weekend'], flat='no',
                                                pref_index=0, wd_we_type=0, P_series=False)
Inactive_EV_small_sat_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])

# Inactive - Small Car - Sunday
Inactive_EV_small_sun = Inactive_S.Appliance(Inactive_S, n=1, Par_power=Par_P_EV['small'],
                                             Battery_cap=Battery_cap['small'], P_var=P_var, w=1,
                                             d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['main'], r_d=r_d,
                                             t_func=t_func['sunday']['personal'], r_v=r_v,
                                             d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                             occasional_use=occasional_use['sunday'], flat='no', pref_index=0,
                                             wd_we_type=2, P_series=False)
Inactive_EV_small_sun.windows(w1=window['inactive']['main'][0], r_w=r_w['inactive'])

# Inactive - Small Car - Sunday - Free Time
Inactive_EV_small_sun_ft = Inactive_S.Appliance(Inactive_S, n=1, Par_power=Par_P_EV['small'],
                                                Battery_cap=Battery_cap['small'], P_var=P_var, w=2,
                                                d_tot=d_tot['sunday'] * perc_usage['sunday']['inactive']['free time'],
                                                r_d=r_d, t_func=t_func['sunday']['personal'], r_v=r_v,
                                                d_min=d_min['sunday']['personal'], fixed='no', fixed_cycle=0,
                                                occasional_use=occasional_use['free time']['weekend'], flat='no',
                                                pref_index=0, wd_we_type=2, P_series=False)
Inactive_EV_small_sun_ft.windows(w1=window['inactive']['free time'][0], w2=window['inactive']['free time'][1],
                                 r_w=r_w['free time'])


def check_if_list_equal(list_1, list_2):
    """ Check if both the lists are of same length and if yes then compare
    sorted versions of both the list to check if both of them are equal
    i.e. contain similar elements with same frequency. """
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

user_dict, appliance_dict = make_users_and_appliances(inputcountry)

NWorking_EV_large_wd = appliance_dict['working']['large']['weekday']['main']
NWorking_EV_large_wd_ft = appliance_dict['working']['large']['weekday']['free time']
    # etc :(
old_app = Working_EV_large_wd_ft
new_app = NWorking_EV_large_wd_ft
for (old, new) in zip(old_app.__dict__, new_app.__dict__):
    old_val = getattr(old_app, old)
    new_val = getattr(new_app, new)
    try:
        if old_val != new_val:
            print(f'{old}: {old_val} NOT EQUAL TO {new_val}')
    except:
        if not check_if_list_equal(old_val, new_val):
            print('lists not equal')

"""
if Working_EV_large_wd != XWorking_EV_large_wd:
    print('ERROR')
    appl = Working_EV_large_wd
    for attr in appl.__dict__:
        if attr
            print(f'{attr} -> {getattr(appl, attr)}')
    appl = XWorking_EV_large_wd
    for attr in appl.__dict__:
        print(f'{attr} -> {getattr(appl, attr)}')
"""
