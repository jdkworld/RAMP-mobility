from src.core_model.core import User


def make_users_and_appliances(inputset):

    user_dict = {} # unused at the moment but might be helpful in the future
    appliance_dict = {} # unused at the moment but might be helpful in the future
    user_list = []

    person_list = ['working', 'student', 'inactive']
    carsize_list = ['large', 'medium', 'small']
    day_list = ['weekday', 'saturday', 'sunday']

    for person in person_list:
        user_dict[person] = {}
        appliance_dict[person] = {}
        for carsize in carsize_list:
            appliance_dict[person][carsize] = {}
            username = person.capitalize() + " - " + carsize.capitalize() + " car"
            user = User(name=username, us_pref=0,
                        n_users=int(round(inputset.tot_users * inputset.pop_sh[person] * inputset.vehicle_sh[carsize])))
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
                        appliance = user.Appliance(user,
                                                   n=1,
                                                   Par_power=inputset.par_p_ev[carsize],
                                                   Battery_cap=inputset.battery_capacity[carsize],
                                                   P_var=inputset.p_var, w=window_amount,
                                                   d_tot=inputset.d_tot[day] * inputset.perc_usage[day][actualperson][main_or_free],
                                                   r_d=inputset.r_d,t_func=inputset.t_func[day][business_or_personal],
                                                   r_v=inputset.r_v,d_min=inputset.d_min[day][business_or_personal],
                                                   fixed='no',
                                                   fixed_cycle=0,
                                                   occasional_use=inputset.occasional_use[day],
                                                   flat='no',pref_index=0,wd_we_type=wdwe_type,
                                                   P_series=False)
                    else:
                        appliance = user.Appliance(user,
                                                   n=1,
                                                   Par_power=inputset.par_p_ev[carsize],
                                                   Battery_cap=inputset.battery_capacity[carsize],
                                                   P_var=inputset.p_var, w=window_amount,
                                                   d_tot=inputset.d_tot[day] *inputset.perc_usage[day][actualperson][main_or_free],
                                                   r_d=inputset.r_d,
                                                   t_func=inputset.t_func[day][business_or_personal],
                                                   r_v=inputset.r_v,
                                                   d_min=inputset.d_min[day][business_or_personal],
                                                   fixed='no',
                                                   fixed_cycle=0,
                                                   occasional_use=inputset.occasional_use[main_or_free][wdwe_name], flat='no',
                                                   pref_index=0,
                                                   wd_we_type=wdwe_type, P_series=False)

                    if window_amount == 1:
                        appliance.windows(w1=inputset.window[actualperson][main_or_free][0],
                                          r_w=inputset.r_w[rw_key])
                    elif window_amount == 2:
                        appliance.windows(w1=inputset.window[actualperson][main_or_free][0],
                                          w2=inputset.window[actualperson][main_or_free][1],
                                          r_w=inputset.r_w[rw_key])
                    else:
                        appliance.windows(w1=inputset.window[actualperson][main_or_free][0],
                                          w2=inputset.window[actualperson][main_or_free][1],
                                          w3=inputset.window[actualperson][main_or_free][2],
                                          r_w=inputset.r_w[rw_key])

                    appliance_dict[person][carsize][day][main_or_free] = appliance
            user_dict[person][carsize] = user
            user_list.append(user)
    return user_list


