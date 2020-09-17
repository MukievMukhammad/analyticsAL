# I({1} -> success)
# I({2} -> success)
# I({3} -> success)
# I({4} -> success)
# I({5} -> success)
# I({1} -> fail)
# I({2} -> fail)
# I({3} -> fail)
# I({4} -> fail)
# I({5} -> fail)
from sql import sql_query


def get_confidence(item_column_name, is_success):
    support_n = sql_query(
        """select count(f) 
        from frequent_items as f 
        where {0} = 1 and is_correct = '{1}' and level = 1;""".format(item_column_name, is_success))[0][0]
    support_d = sql_query(
        """select count(f) 
        from frequent_items as f 
        where {0} = 1 and level = 1;""".format(item_column_name))[0][0]
    return support_n / support_d


def get_fraction(is_success):
    num = sql_query(
        """select count(f) 
        from frequent_items as f 
        where is_correct = '{0}' and level = 1;""".format(is_success))[0][0]
    div = sql_query(
        """select count(f) 
        from frequent_items as f where level = 1;""")[0][0]
    return num / div


if __name__ == '__main__':
    interest1_t = get_confidence('f_item', 'TRUE') - get_fraction('TRUE')
    interest2_t = get_confidence('s_item', 'TRUE') - get_fraction('TRUE')
    interest3_t = get_confidence('th_item', 'TRUE') - get_fraction('TRUE')
    interest4_t = get_confidence('fh_item', 'TRUE') - get_fraction('TRUE')
    interest5_t = get_confidence('fi_item', 'TRUE') - get_fraction('TRUE')

    interest1_f = get_confidence('f_item', 'FALSE') - get_fraction('FALSE')
    interest2_f = get_confidence('s_item', 'FALSE') - get_fraction('FALSE')
    interest3_f = get_confidence('th_item', 'FALSE') - get_fraction('FALSE')
    interest4_f = get_confidence('fh_item', 'FALSE') - get_fraction('FALSE')
    interest5_f = get_confidence('fi_item', 'FALSE') - get_fraction('FALSE')
    print(interest1_t)
